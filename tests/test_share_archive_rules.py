"""One small test per refusal rule in runesmith.share._safe_members()."""

from __future__ import annotations

import sys
import zipfile

import pytest

from runesmith import share
from runesmith.share import ImportRefused, _safe_members


def _write_zip(path, members: dict[str, str]):
    with zipfile.ZipFile(path, "w") as archive:
        for name, text in members.items():
            archive.writestr(name, text)
    return path


def _refusal(tmp_path, members: dict[str, str]):
    archive = _write_zip(tmp_path / "a.zip", members)
    with zipfile.ZipFile(archive) as opened, pytest.raises(ImportRefused) as refused:
        _safe_members(opened)
    return str(refused.value)


@pytest.mark.parametrize(
    "name",
    [
        pytest.param("/organs/x.py", id="absolute-path"),
        pytest.param("organs/../x.py", id="dotdot"),
        pytest.param("notes/x.py", id="file-outside-organs"),
        pytest.param("organs/x.txt", id="non-py-file-in-organs"),
    ],
)
def test_refuses_unexpected_member(tmp_path, name):
    message = _refusal(tmp_path, {"MANIFEST.json": "{}", name: "x = 1\n"})
    assert "unexpected archive member" in message and name in message


@pytest.mark.skipif(sys.platform == "win32", reason="zipfile turns backslashes into / on Windows")
def test_refuses_backslash_in_name(tmp_path):
    message = _refusal(tmp_path, {"MANIFEST.json": "{}", "organs/sub\\x.py": "x = 1\n"})
    assert "unexpected archive member" in message


def test_refuses_file_over_max_file_bytes(tmp_path, monkeypatch):
    monkeypatch.setattr(share, "MAX_FILE_BYTES", 10)
    monkeypatch.setattr(share, "MAX_TOTAL_BYTES", 1_000)
    message = _refusal(tmp_path, {"MANIFEST.json": "{}", "organs/big.py": "x" * 11})
    assert "organs/big.py is larger than 10 bytes" in message


def test_refuses_total_over_max_total_bytes(tmp_path, monkeypatch):
    monkeypatch.setattr(share, "MAX_FILE_BYTES", 100)
    monkeypatch.setattr(share, "MAX_TOTAL_BYTES", 15)
    message = _refusal(
        tmp_path,
        {"MANIFEST.json": "{}", "organs/a.py": "a" * 10, "organs/b.py": "b" * 10},
    )
    assert "archive too large" in message


def test_refuses_archive_without_manifest(tmp_path):
    message = _refusal(tmp_path, {"organs/repair.py": "x = 1\n"})
    assert "no MANIFEST.json" in message


def test_valid_archive_returns_both_members(tmp_path):
    archive = _write_zip(
        tmp_path / "a.zip",
        {"MANIFEST.json": "{}", "organs/": "", "organs/repair.py": "x = 1\n"},
    )
    with zipfile.ZipFile(archive) as opened:
        members = _safe_members(opened)
    assert {m.filename for m in members} == {"MANIFEST.json", "organs/repair.py"}

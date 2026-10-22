"""KeyStore: saved keys are written once, listed by name only, and never leak through a listing."""

import json
import os
import stat
import sys

import pytest

from runesmith.keystore import KeyStore


def test_set_then_supplier_reads_the_value_at_call_time(tmp_path):
    ks = KeyStore(tmp_path)
    supply = ks.supplier("groq")
    assert supply() == ""                      # nothing saved yet
    ks.set("groq", "  gsk-first  ")
    assert supply() == "gsk-first"             # stripped, read when called
    ks.set("groq", "gsk-second")
    assert supply() == "gsk-second"            # a later change takes effect


def test_listings_never_contain_the_value(tmp_path):
    ks = KeyStore(tmp_path)
    ks.set("openrouter", "sk-or-secret-value")
    ks.set("gemini", "AIza-secret-value")
    assert ks.names() == ["gemini", "openrouter"]
    described = ks.describe()
    assert [row["name"] for row in described] == ["gemini", "openrouter"]
    assert all(set(row) == {"name", "saved_utc"} for row in described)
    assert "secret-value" not in json.dumps(described)


@pytest.mark.parametrize("name", ["", "has space", "slash/name", "x" * 65])
def test_invalid_names_are_refused(tmp_path, name):
    with pytest.raises(ValueError):
        KeyStore(tmp_path).set(name, "value")


@pytest.mark.parametrize("value", ["", "   ", None])
def test_empty_values_are_refused(tmp_path, value):
    with pytest.raises(ValueError):
        KeyStore(tmp_path).set("groq", value)
    assert not (tmp_path / "secrets.json").exists()


def test_delete_and_has(tmp_path):
    ks = KeyStore(tmp_path)
    assert ks.delete("missing") is False
    ks.set("groq", "v")
    assert ks.has("groq")
    assert ks.delete("groq") is True
    assert not ks.has("groq")
    assert ks.names() == []


@pytest.mark.parametrize("content", ["not json", "[1, 2, 3]", ""])
def test_damaged_file_reads_as_empty(tmp_path, content):
    (tmp_path / "secrets.json").write_text(content, encoding="utf-8")
    ks = KeyStore(tmp_path)
    assert ks.names() == []
    ks.set("groq", "v")                        # and can be written over cleanly
    assert ks.names() == ["groq"]


def test_no_temporary_file_is_left_behind(tmp_path):
    KeyStore(tmp_path).set("groq", "v")
    assert sorted(p.name for p in tmp_path.iterdir()) == ["secrets.json"]


@pytest.mark.skipif(sys.platform == "win32", reason="POSIX permission bits")
def test_file_is_owner_only_on_posix(tmp_path):
    KeyStore(tmp_path).set("groq", "v")
    mode = stat.S_IMODE(os.stat(tmp_path / "secrets.json").st_mode)
    assert mode == stat.S_IRUSR | stat.S_IWUSR

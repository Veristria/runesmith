"""Ledger.verify(): every kind of tampering is reported, with the record where it starts."""

from __future__ import annotations

import json
from pathlib import Path

from runesmith.canon import canonical, digest
from runesmith.ledger import Ledger

BODY_KEYS = ("seq", "utc", "kind", "data", "prev")


def five_records(tmp_path: Path) -> Path:
    path = tmp_path / "ledger.jsonl"
    ledger = Ledger(path)
    for i in range(5):
        ledger.append("test.event", {"i": i})
    assert ledger.verify()["ok"] is True
    return path


def read_lines(path: Path) -> list[str]:
    return path.read_text(encoding="ascii").splitlines()


def write_lines(path: Path, lines: list[str]) -> None:
    path.write_text("\n".join(lines) + "\n", encoding="ascii")


def test_a_changed_record_is_reported_as_content_changed(tmp_path):
    path = five_records(tmp_path)
    lines = read_lines(path)
    record = json.loads(lines[2])
    record["data"]["i"] = 99                 # the payload changes, its hash does not
    lines[2] = canonical(record)
    write_lines(path, lines)
    assert Ledger(path).verify() == {
        "ok": False, "records": 3, "error": "content changed at seq 3"}


def test_a_deleted_record_is_reported_as_a_sequence_gap(tmp_path):
    path = five_records(tmp_path)
    lines = read_lines(path)
    del lines[2]                             # the fourth record now sits where the third should be
    write_lines(path, lines)
    assert Ledger(path).verify() == {
        "ok": False, "records": 3, "error": "sequence gap at record 3"}


def test_a_misdirected_link_is_reported_as_broken(tmp_path):
    path = five_records(tmp_path)
    lines = read_lines(path)
    record = json.loads(lines[2])
    record["prev"] = json.loads(lines[0])["hash"]    # a real hash, one record too early
    record["hash"] = digest({key: record[key] for key in BODY_KEYS})
    lines[2] = canonical(record)             # seq and hash agree; only prev points elsewhere
    write_lines(path, lines)
    assert Ledger(path).verify() == {
        "ok": False, "records": 3, "error": "broken link at seq 3"}


def test_events_filters_kinds_and_a_wildcard(tmp_path):
    ledger = Ledger(tmp_path / "ledger.jsonl")
    for kind in ("a.one", "ab.one", "a.two", "b.two"):
        ledger.append(kind, {})
    assert [record["kind"] for record in ledger.events("a.*")] == ["a.one", "a.two"]
    assert [record["kind"] for record in ledger.events()] == ["a.one", "ab.one", "a.two", "b.two"]
    assert [record["kind"] for record in ledger.events("b.two")] == ["b.two"]

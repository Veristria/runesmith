"""Tests for runesmith.home.init_home: first call, repeat call, and hand edits."""

import json

import pytest

from runesmith import generations
from runesmith.config import DEFAULT_CONFIG
from runesmith.home import GITIGNORE, init_home
from runesmith.ledger import Ledger


@pytest.fixture
def home(tmp_path):
    return tmp_path / ".runesmith"


def test_first_call_creates_the_home(home):
    result = init_home(home)

    assert result["created"] is True
    assert (home / ".gitignore").read_bytes() == GITIGNORE.encode("utf-8")
    written = json.loads((home / "runesmith.json").read_text(encoding="utf-8"))
    assert written == DEFAULT_CONFIG
    assert result["active_generation"]
    assert result["active_generation"] == generations.active(home)


def test_second_call_changes_nothing(home):
    first = init_home(home)
    second = init_home(home)

    assert second["created"] is False
    assert second["active_generation"] == first["active_generation"]
    ledger = Ledger(home / "ledger.jsonl")
    assert len(list(ledger.events("home.initialized"))) == 1
    assert ledger.verify()["ok"] is True


def test_hand_edited_files_survive_a_second_call(home):
    init_home(home)
    config, ignore = home / "runesmith.json", home / ".gitignore"
    edited_config = b'{"schema": "runesmith.config.v1", "note": "edited by hand"}\n'
    edited_ignore = b"# my own rules\nkeys/\n"
    config.write_bytes(edited_config)
    ignore.write_bytes(edited_ignore)

    init_home(home)

    assert config.read_bytes() == edited_config
    assert ignore.read_bytes() == edited_ignore
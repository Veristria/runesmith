"""Journal basics for runesmith.notes.NoteStore."""

import pytest

from runesmith.notes import MAX_TEXT, NoteStore


@pytest.fixture
def store(tmp_path):
    return NoteStore(tmp_path)


def _add(store, text="hello", target_type="object", target_id="t1"):
    return store.add(target_type=target_type, target_id=target_id, text=text)


def test_add_rejects_empty_text(store):
    with pytest.raises(ValueError):
        _add(store, text="")


def test_add_rejects_whitespace_only_text(store):
    with pytest.raises(ValueError):
        _add(store, text="   \n\t  ")


def test_add_truncates_text_to_max_text(store):
    note = _add(store, text="x" * (MAX_TEXT + 50))
    assert len(note["text"]) == MAX_TEXT
    assert len(store.all()[0]["text"]) == MAX_TEXT


def test_resolve_keeps_note_and_appends_one_line(store, tmp_path):
    note = _add(store)
    journal = tmp_path / "notes.jsonl"
    before = journal.read_text(encoding="utf-8")

    store.resolve(note["id"], resolution="done")

    after = journal.read_text(encoding="utf-8")
    notes = store.all()
    assert len(notes) == 1
    assert notes[0]["id"] == note["id"]
    assert notes[0]["resolved"]["resolution"] == "done"
    # append-only: one new line, nothing rewritten or removed
    assert len(after.splitlines()) == len(before.splitlines()) + 1
    assert after.startswith(before)


def test_for_target_hides_resolved_note(store):
    note = _add(store)
    store.resolve(note["id"], resolution="done")

    assert store.for_target("object", "t1") == []

    shown = store.for_target("object", "t1", open_only=False)
    assert [n["id"] for n in shown] == [note["id"]]


def test_counts_drops_target_once_all_notes_resolved(store):
    first = _add(store, text="one")
    second = _add(store, text="two")
    _add(store, text="other target", target_id="t2")
    assert store.counts() == {"object:t1": 2, "object:t2": 1}

    store.resolve(first["id"], resolution="done")
    assert store.counts()["object:t1"] == 1

    store.resolve(second["id"], resolution="done")
    counts = store.counts()
    assert "object:t1" not in counts
    assert counts["object:t2"] == 1


def test_garbage_line_in_journal_is_skipped(store, tmp_path):
    good = _add(store, text="good note")
    with open(tmp_path / "notes.jsonl", "a", encoding="utf-8", newline="\n") as f:
        f.write("this is not json {\n")
    later = _add(store, text="added after the garbage line")

    ids = {n["id"] for n in store.all()}
    assert ids == {good["id"], later["id"]}
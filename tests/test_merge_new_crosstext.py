"""merge_new_crosstext.py — append new cluster notes into the book (dedup by key).

Target file: data/sundara_commentary_to_add.json. The checkout root is a
hard-coded Windows path in the script; conftest rewrites that single line to
the sandbox. Curated floors at authoring: 896 notes, 170 cross_text (see tests/curated_floors.py).
"""
from conftest import Stage, records

SCRIPT = "merge_new_crosstext.py"
BOOK = "data/sundara_commentary_to_add.json"
KAVYA = "data/crosstext/kavya.json"


def staged(stage: Stage) -> Stage:
    stage.fixture("merge_new_crosstext")
    stage.script(SCRIPT, root=str(stage.root))
    return stage


def test_idempotent_second_run_dedups_everything(stage):
    s = staged(stage)
    r1 = s.run(SCRIPT)
    assert "kavya: 1 added, 1 skipped" in r1.stderr
    assert "veda: 1 added, 0 skipped" in r1.stderr
    assert "upanishads: file missing" in r1.stderr
    assert "FINAL: 4 notes = 1 base + 3 cross-text" in r1.stderr
    after1 = s.read(BOOK)
    r2 = s.run(SCRIPT)
    assert "kavya: 0 added, 2 skipped" in r2.stderr
    assert "veda: 0 added, 1 skipped" in r2.stderr
    assert "FINAL: 4 notes = 1 base + 3 cross-text" in r2.stderr
    assert s.read(BOOK) == after1


def test_non_shrink_existing_records_survive_and_meta_recounts(stage):
    s = staged(stage)
    before = records(s.load(BOOK))
    s.run(SCRIPT)
    doc = s.load(BOOK)
    after = records(doc)
    assert len(after) >= len(before) >= 2
    for n in before:
        assert n in after, f"pre-existing note {n['shloka']} lost by merge"
    meta = doc[0]["_meta"]
    assert meta["total_notes"] == len(after) == 4
    assert meta["cross_text_notes"] == 3 and meta["base_notes"] == 1
    assert meta["per_chapter_notes"]["13"] == 2 and meta["per_chapter_notes"]["5"] == 1
    assert [n["shloka"] for n in after] == ["V.1.1", "V.5.1", "V.13.11", "V.13.12"]
    new = next(n for n in after if n["shloka"] == "V.13.12")
    assert new["review_required"] is True and new["cluster"] == "kavya"


def test_truncated_cluster_file_aborts_without_write(stage):
    s = staged(stage)
    s.truncate(KAVYA)
    snap = s.snapshot(BOOK)
    r = s.run(SCRIPT, expect=None)
    assert r.returncode != 0
    s.assert_unchanged(snap)


def test_truncated_book_aborts_without_write(stage):
    s = staged(stage)
    s.truncate(BOOK)
    snap = s.snapshot(BOOK)
    r = s.run(SCRIPT, expect=None)
    assert r.returncode != 0
    s.assert_unchanged(snap)

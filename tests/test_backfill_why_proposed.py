"""backfill_why_proposed.py — one-off why_proposed injection into pilot sargas.

Targets: data/analysis/phase2_pilot/sarga_*_candidates.json (in place).
Curated floor at authoring: sarga_35 = 6 notes (see tests/curated_floors.py).
"""
from conftest import Stage

SCRIPT = "backfill_why_proposed.py"
S35 = "data/analysis/phase2_pilot/sarga_35_candidates.json"
S36 = "data/analysis/phase2_pilot/sarga_36_candidates.json"


def staged(stage: Stage) -> Stage:
    stage.fixture("backfill_why_proposed")
    stage.script(SCRIPT)
    return stage


def test_idempotent_second_run_changes_nothing(stage):
    s = staged(stage)
    r1 = s.run(SCRIPT)
    assert "back-filled why_proposed on 2 notes" in r1.stdout
    after35, after36 = s.read(S35), s.read(S36)
    r2 = s.run(SCRIPT)
    assert "back-filled why_proposed on 0 notes" in r2.stdout
    assert s.read(S35) == after35 and s.read(S36) == after36


def test_non_shrink_notes_rejected_and_meta_survive(stage):
    s = staged(stage)
    before = s.load(S35)
    s.run(SCRIPT)
    after = s.load(S35)
    assert len(after["notes"]) == len(before["notes"]) >= 2
    assert after["rejected"] == before["rejected"]
    assert after["_meta"] == before["_meta"]
    filled = next(n for n in after["notes"] if n["verse_id"] == "5.35.3")
    assert filled["why_proposed"].startswith("Уточняет bhūyaḥ")
    untouched = next(n for n in after["notes"] if n["verse_id"] == "5.35.99")
    assert untouched == next(n for n in before["notes"] if n["verse_id"] == "5.35.99")


def test_truncated_sarga_file_aborts_without_partial_write(stage):
    """A truncated SECOND file must not leave the first one already rewritten."""
    s = staged(stage)
    s.truncate(S36)
    snap = s.snapshot(S35, S36)
    r = s.run(SCRIPT, expect=None)
    assert r.returncode != 0
    s.assert_unchanged(snap)

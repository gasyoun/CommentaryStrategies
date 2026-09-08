"""merge_phase2_pilot.py — per-sarga candidate files merged into one batch set.

Targets: data/analysis/<batch>/<prefix>_candidates.json + <prefix>_rejected.json
(full rewrite from sources). Curated floor at authoring: pilot_candidates.json
= 16 notes (see conftest).
"""
from conftest import Stage

SCRIPT = "merge_phase2_pilot.py"
DIR = "data/analysis/phase2_pilot/"
OUT = DIR + "pilot_candidates.json"
REJ = DIR + "pilot_rejected.json"
S36 = DIR + "sarga_36_candidates.json"


def staged(stage: Stage) -> Stage:
    stage.fixture("merge_phase2_pilot")
    stage.script(SCRIPT)
    return stage


def test_idempotent_rerun_is_byte_identical(stage):
    s = staged(stage)
    r1 = s.run(SCRIPT)
    assert "merged 2 files -> 3 notes (158 considered" in r1.stdout
    out1, rej1 = s.read(OUT), s.read(REJ)
    doc = s.load(OUT)
    assert [n["verse_id"] for n in doc["notes"]] == ["5.35.3", "5.35.11", "5.36.13"]
    assert doc["_meta"]["total_notes"] == 3 and doc["_meta"]["total_rejected_entries"] == 3
    assert doc["_meta"]["reject_taxonomy"] == {
        "formulaic_panegyric": 1, "merged_range_marker": 1, "restates_podstrochnik": 1}
    s.run(SCRIPT)
    assert s.read(OUT) == out1 and s.read(REJ) == rej1


def test_non_shrink_output_holds_every_source_note(stage):
    s = staged(stage)
    src = [n for f in ("sarga_35_candidates.json", "sarga_36_candidates.json")
           for n in s.load(DIR + f)["notes"]]
    # a stale, smaller previous output must be superseded, never trusted
    s.write_json(OUT, {"_meta": {"total_notes": 1}, "notes": [src[0]]})
    s.run(SCRIPT)
    doc = s.load(OUT)
    assert len(doc["notes"]) == len(src) >= 3
    for n in src:
        assert n in doc["notes"]
    assert all(n["review_required"] is True for n in doc["notes"])
    rej = s.load(REJ)["rejected"]
    assert len(rej) == 3 and {r["sarga"] for r in rej} == {35, 36}


def test_truncated_sarga_file_aborts_without_partial_write(stage):
    s = staged(stage)
    s.run(SCRIPT)                      # establish a good previous output
    snap = s.snapshot(OUT, REJ)
    s.truncate(S36)
    r = s.run(SCRIPT, expect=None)
    assert r.returncode != 0
    s.assert_unchanged(snap)


def test_note_without_review_required_is_refused(stage):
    s = staged(stage)
    s.run(SCRIPT)
    snap = s.snapshot(OUT, REJ)
    doc = s.load(S36)
    doc["notes"][0]["review_required"] = False
    s.write_json(S36, doc)
    r = s.run(SCRIPT, expect=1)
    assert "missing review_required" in r.stderr
    s.assert_unchanged(snap)

"""apply_phase2_decisions.py — M.G.'s Phase-2 gate grafted into the book.

Targets: data/sundara_ch{N}_commentary_to_add.json, data/sundara_commentary_to_add.json,
data/sundara_book_stats.json, the batch candidates + rejected log. Curated
floors at authoring: book 896 notes, ch35 6, ch36 6, ch37 4, pilot 16 candidates.
"""
from conftest import Stage, records

SCRIPT = "apply_phase2_decisions.py"
VOTES = "votes/phase2_decisions.json"
BOOK = "data/sundara_commentary_to_add.json"
CH35 = "data/sundara_ch35_commentary_to_add.json"
CH36 = "data/sundara_ch36_commentary_to_add.json"
STATS = "data/sundara_book_stats.json"
CAND = "data/analysis/phase2_pilot/pilot_candidates.json"
REJ = "data/analysis/phase2_pilot/pilot_gate_rejected.json"
TARGETS = (BOOK, CH35, CH36, STATS, CAND, REJ)


def staged(stage: Stage) -> Stage:
    stage.fixture("apply_phase2_decisions")
    stage.script(SCRIPT)
    return stage


def test_idempotent_second_run_skips_already_grafted_notes(stage):
    s = staged(stage)
    r1 = s.run(SCRIPT, VOTES, "--batch", "pilot")
    assert "ch35: +1 notes" in r1.stdout and "book: +1 notes" in r1.stdout
    ch35_1 = s.load(CH35)
    book_1 = s.load(BOOK)
    assert ch35_1[0]["_meta"]["notes_count"] == 2 == len(records(ch35_1))
    assert book_1[0]["_meta"]["total_notes"] == 3 == len(records(book_1))
    assert s.load(REJ)["rejected"][0]["verse_id"] == "5.35.11"

    r2 = s.run(SCRIPT, VOTES, "--batch", "pilot")
    assert "already in ch35 file; skipped" in r2.stderr
    assert "ch35: +0 notes" in r2.stdout and "book: +0 notes" in r2.stdout
    assert records(s.load(CH35)) == records(ch35_1)
    assert records(s.load(BOOK)) == records(book_1)
    assert s.load(STATS)["total_notes"] == 3


def test_non_shrink_book_and_chapter_counts_only_grow(stage):
    s = staged(stage)
    book_before = records(s.load(BOOK))
    ch35_before = records(s.load(CH35))
    ch36_before = s.read(CH36)
    s.run(SCRIPT, VOTES, "--batch", "pilot")
    book_after = records(s.load(BOOK))
    ch35_after = records(s.load(CH35))
    assert len(book_after) >= len(book_before) and len(ch35_after) >= len(ch35_before)
    # every pre-existing record survives verbatim
    assert book_after[: len(book_before)] == book_before
    assert ch35_after[: len(ch35_before)] == ch35_before
    # an untouched chapter file is not rewritten at all
    assert s.read(CH36) == ch36_before
    grafted = book_after[-1]
    assert grafted["shloka"] == "V.35.3" and grafted["review_required"] is True
    assert grafted["gate"]["action"] == "accept"
    assert grafted["provenance"]["applied_by"] == "scripts/apply_phase2_decisions.py"
    stats = s.load(STATS)
    assert stats["total_verses"] == 2859, "verse totals are never recomputed here"
    assert stats["per_chapter"]["35"]["notes"] == 2


def test_dry_run_writes_nothing(stage):
    s = staged(stage)
    snap = s.snapshot(*TARGETS)
    r = s.run(SCRIPT, VOTES, "--batch", "pilot", "--dry-run")
    assert "[DRY RUN]" in r.stdout
    s.assert_unchanged(snap)


def test_truncated_export_is_refused_without_partial_write(stage):
    s = staged(stage)
    s.truncate(VOTES)
    snap = s.snapshot(*TARGETS)
    r = s.run(SCRIPT, VOTES, "--batch", "pilot", expect=None)
    assert r.returncode != 0
    s.assert_unchanged(snap)


def test_malformed_export_shapes_are_refused(stage):
    s = staged(stage)
    snap = s.snapshot(*TARGETS)
    good = s.load(VOTES)

    s.write_json("votes/no_key.json", {"reviewed_at": good["reviewed_at"]})
    r = s.run(SCRIPT, "votes/no_key.json", "--batch", "pilot", expect=None)
    assert r.returncode != 0

    unknown = dict(good, reviewer_decisions=dict(good["reviewer_decisions"]))
    unknown["reviewer_decisions"]["5.99.1"] = dict(good["reviewer_decisions"]["5.35.3"])
    s.write_json("votes/unknown.json", unknown)
    r = s.run(SCRIPT, "votes/unknown.json", "--batch", "pilot", expect=1)
    assert "unknown candidates" in r.stderr

    flagged = dict(good, reviewer_decisions=dict(good["reviewer_decisions"]))
    flagged["reviewer_decisions"]["5.36.13"] = dict(good["reviewer_decisions"]["5.35.3"])
    s.write_json("votes/flagged.json", flagged)
    r = s.run(SCRIPT, "votes/flagged.json", "--batch", "pilot", expect=1)
    assert "--allow-flagged-anchor" in r.stderr

    # auto-detect with a verse outside every batch's candidate set
    r = s.run(SCRIPT, "votes/unknown.json", expect=1)
    assert "match no batch" in r.stderr

    s.assert_unchanged(snap)

"""rebuild_crosstext.py — full rebuild: BASE + deduped verified CROSS -> book,
decision ledger, book stats, _rebuild_summary.json.

Curated floors at authoring: 896 notes (170 cross_text) in the book, 5507
ledger entries (228 cross_text), kavya 12 / gita 24 source notes (see conftest).
"""
from conftest import Stage, records

SCRIPT = "rebuild_crosstext.py"
BOOK = "data/sundara_commentary_to_add.json"
LEDGER = "data/sundara_decision_ledger.json"
STATS = "data/sundara_book_stats.json"
SUMMARY = "scripts/_rebuild_summary.json"
KAVYA = "data/crosstext/kavya.json"
TARGETS = (BOOK, LEDGER, STATS, SUMMARY)


def staged(stage: Stage) -> Stage:
    stage.fixture("rebuild_crosstext")
    stage.script(SCRIPT)
    return stage


def test_idempotent_rerun_is_byte_identical(stage):
    s = staged(stage)
    r1 = s.run(SCRIPT)
    assert "BASE notes: 2" in r1.stdout
    assert "CROSS candidates (verified/confirmed): 3" in r1.stdout
    assert "After exact-triple dedup: 2 (dropped 1)" in r1.stdout
    assert "WROTE commentary: 4 notes" in r1.stdout
    assert "WROTE ledger: cand 7, acc 4, rej 3" in r1.stdout
    snap1 = s.snapshot(*TARGETS)
    s.run(SCRIPT)
    assert s.snapshot(*TARGETS) == snap1


def test_non_shrink_base_notes_and_base_ledger_entries_survive(stage):
    s = staged(stage)
    book_before = records(s.load(BOOK))
    base_before = [n for n in book_before if n.get("subtype") != "cross_text"]
    ledger_before = s.load(LEDGER)["entries"]
    base_entries_before = [e for e in ledger_before if e.get("subtype") != "cross_text"]

    s.run(SCRIPT)

    doc = s.load(BOOK)
    after = records(doc)
    base_after = [n for n in after if n.get("subtype") != "cross_text"]
    assert len(after) >= len(book_before) >= 3
    assert len(base_after) == len(base_before) == 2
    for b in base_before:
        keep = {k: v for k, v in b.items() if k != "subtype"}
        assert any({k: v for k, v in a.items() if k != "subtype"} == keep for a in base_after)
    assert next(n for n in base_after if n["shloka"] == "V.1.1")["subtype"] == "base"
    cross_after = [n for n in after if n.get("subtype") == "cross_text"]
    assert {(n["shloka"], n["cluster"]) for n in cross_after} == {("V.13.11", "kavya"), ("V.13.11", "gita")}
    assert all(n["review_required"] is True for n in cross_after)
    assert all(len(n["also"]) == 1 for n in cross_after), "same shloka+lemma across works cross-links via 'also'"
    assert doc[0]["_meta"]["total_notes"] == 4 and doc[0]["_meta"]["total_verses"] == 319

    ledger = s.load(LEDGER)
    base_entries_after = [e for e in ledger["entries"] if e.get("subtype") != "cross_text"]
    assert base_entries_after == base_entries_before, "base ledger rows are preserved verbatim"
    reasons = sorted(e["reason"] for e in ledger["entries"] if e.get("subtype") == "cross_text")
    assert reasons == ["accepted_cross_text", "accepted_cross_text",
                       "rejected_crosstext_trivial", "rejected_duplicate"]
    assert ledger["meta"]["accepted"] == 4 == doc[0]["_meta"]["total_notes"]
    stats = s.load(STATS)
    assert stats["total_notes"] == 4 and stats["per_chapter"]["13"]["notes"] == 2


def test_truncated_cluster_file_aborts_without_write(stage):
    s = staged(stage)
    s.truncate(KAVYA)
    snap = s.snapshot(*TARGETS)
    r = s.run(SCRIPT, expect=None)
    assert r.returncode != 0
    s.assert_unchanged(snap)


def test_truncated_ledger_aborts_without_partial_write(stage):
    """The ledger is read AFTER the book would be rewritten; a truncated ledger
    must still leave the book untouched."""
    s = staged(stage)
    s.truncate(LEDGER)
    snap = s.snapshot(*TARGETS)
    r = s.run(SCRIPT, expect=None)
    assert r.returncode != 0
    s.assert_unchanged(snap)

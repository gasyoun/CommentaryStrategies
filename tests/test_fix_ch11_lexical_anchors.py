"""fix_ch11_lexical_anchors.py — resolve the sarga-11 phantom anchors (H276 WS-3b).

Two notes are re-anchored into ch17/ch25, the rest are parked into
ch11.qa_removed.json — nothing is deleted. Target files: data/lexical/ch11.json
(+ ch11.qa_removed.json, ch17.json, ch25.json), the book aggregate and
data/sundara_book_stats.json. Curated floors: tests/curated_floors.py.

Write-order caveat, recorded rather than fixed (edit scope of H4368 excludes
this script): ch11.json is written BEFORE the book aggregate is read, so a
malformed *book* would leave a partial write behind. The refusal case below
therefore corrupts the FIRST input read (ch11.json), which is the input a
truncated export actually produces here.
"""
from conftest import Stage, records

SCRIPT = "fix_ch11_lexical_anchors.py"
CH11 = "data/lexical/ch11.json"
QA = "data/lexical/ch11.qa_removed.json"
CH17 = "data/lexical/ch17.json"
CH25 = "data/lexical/ch25.json"
BOOK = "data/sundara_commentary_to_add.json"
STATS = "data/sundara_book_stats.json"
TARGETS = (CH11, QA, CH17, CH25, BOOK, STATS)

PARKED = {"mālyahīna", "duḥkha"}


def staged(stage: Stage) -> Stage:
    stage.fixture("fix_ch11_lexical_anchors")
    stage.script(SCRIPT)
    return stage


def test_idempotent_guard_stops_the_second_run_without_touching_anything(stage):
    s = staged(stage)
    r1 = s.run(SCRIPT)
    assert "ch11.json: 1 notes remain (-2 parked, -2 re-anchored away)" in r1.stdout
    assert "ch17.json: +1 re-anchored (kṣāma @ V.17.30)" in r1.stdout
    assert "ch25.json: +1 re-anchored (vivarṇa @ V.25.8)" in r1.stdout
    snap = s.snapshot(*TARGETS)

    r2 = s.run(SCRIPT, expect=None)
    assert r2.returncode != 0
    assert "idempotent guard" in (r2.stderr + r2.stdout)
    s.assert_unchanged(snap)


def test_non_shrink_every_ch11_card_survives_somewhere(stage):
    s = staged(stage)
    before = records(s.load(CH11))
    keys_before = {(n["shloka"], n["lemma_iast"]) for n in before}
    assert len(before) == 5

    s.run(SCRIPT)

    kept = records(s.load(CH11))
    parked = records(s.load(QA))
    moved = [n for n in records(s.load(CH17)) + records(s.load(CH25))
             if "reanchored" in n]
    assert len(kept) + len(parked) + len(moved) == len(before), \
        "no curated card may be dropped — each is kept, parked or re-anchored"
    assert {n["lemma_iast"] for n in kept} == {"surāpāna"}
    assert {n["lemma_iast"] for n in parked} == PARKED
    assert {n["lemma_iast"] for n in moved} == {"kṣāma", "vivarṇa"}

    # every parked card keeps its original anchor and carries the reason
    for n in parked:
        assert n["qa_removed"]["original_shloka"].startswith("V.11.")
        assert n["qa_removed"]["reason"]
        assert (n["shloka"], n["lemma_iast"]) in keys_before

    # re-anchored cards keep provenance and get anchoring=2 + a re-derived verdict
    by_lemma = {n["lemma_iast"]: n for n in moved}
    assert by_lemma["kṣāma"]["shloka"] == "V.17.30"
    assert by_lemma["kṣāma"]["reanchored"]["from"] == "V.11.9"
    assert by_lemma["kṣāma"]["judge"]["scores"]["anchoring"] == 2
    assert by_lemma["kṣāma"]["judge"]["verdict"] == "keep"
    assert by_lemma["vivarṇa"]["shloka"] == "V.25.8"
    assert by_lemma["vivarṇa"]["judge"]["verdict"] == "edit", \
        "register 1 re-derives to edit, not keep"
    assert all(n["review_required"] is True for n in kept + parked + moved)

    # per-file _meta counters follow the moves
    assert s.load(CH11)[0]["_meta"]["notes_count"] == 1
    assert s.load(CH17)[0]["_meta"]["notes_count"] == 2
    assert s.load(CH25)[0]["_meta"]["notes_count"] == 2
    assert s.load(QA)[0]["_meta"]["removed_count"] == 2


def test_book_and_stats_stay_consistent_with_the_lexical_files(stage):
    s = staged(stage)
    book_before = records(s.load(BOOK))
    s.run(SCRIPT)

    book = s.load(BOOK)
    notes = records(book)
    assert len(notes) == len(book_before) - len(PARKED)
    keys = {(n["shloka"], n["lemma_iast"]) for n in notes}
    assert ("V.17.30", "kṣāma") in keys and ("V.25.8", "vivarṇa") in keys
    assert not any(lem in PARKED for _, lem in keys)
    base = next(n for n in notes if n["subtype"] == "base")
    assert base["note_ru"].startswith("Дворец Раваны"), "base notes are untouched"

    bm = book[0]["_meta"]
    assert bm["total_notes"] == len(notes) == 4
    assert bm["verses_with_note"] == len({n["shloka"] for n in notes})
    assert bm["verses_without_note"] == bm["total_verses"] - bm["verses_with_note"]

    stats = s.load(STATS)
    assert stats["total_notes"] == len(notes)
    assert stats["per_chapter"]["11"]["notes"] == 2
    assert stats["per_chapter"]["17"]["notes"] == 1
    assert stats["per_chapter"]["25"]["notes"] == 1
    assert stats["per_chapter"]["11"]["verses_unnoted"] == \
        stats["per_chapter"]["11"]["verses"] - stats["per_chapter"]["11"]["verses_noted"]


def test_truncated_ch11_is_refused_without_partial_write(stage):
    s = staged(stage)
    s.truncate(CH11)
    snap = s.snapshot(*TARGETS)
    r = s.run(SCRIPT, expect=None)
    assert r.returncode != 0
    s.assert_unchanged(snap)


def test_a_target_chapter_that_already_holds_the_card_aborts(stage):
    """The re-anchor step refuses to create a duplicate in ch17/ch25."""
    s = staged(stage)
    doc = s.load(CH17)
    doc.append({"shloka": "V.17.30", "lemma_iast": "kṣāma", "subtype": "lexical",
                "note_ru": "Дубль.", "review_required": True})
    s.write_json(CH17, doc)
    r = s.run(SCRIPT, expect=None)
    assert r.returncode != 0
    assert "already in ch17" in (r.stderr + r.stdout)
    # the book aggregate is read only after this abort — it must be untouched
    assert len(records(s.load(BOOK))) == 6

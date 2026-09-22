"""lexical_judge_merge.py — graft the lexical-judge verdicts back (H276 WS-2).

Target files: the book aggregate data/sundara_commentary_to_add.json, every
touched data/lexical/ch{N}.json, and data/analysis/lexical_judge/summary.json.
Curated floors at authoring: ch2 = 16 cards, ch3 = 13 cards, book = 896 notes
(see tests/curated_floors.py).
"""
from conftest import Stage, records

SCRIPT = "lexical_judge_merge.py"
BOOK = "data/sundara_commentary_to_add.json"
CH2 = "data/lexical/ch2.json"
CH3 = "data/lexical/ch3.json"
CHUNK1 = "data/analysis/lexical_judge/chunk_01_input.json"
SUMMARY = "data/analysis/lexical_judge/summary.json"
TARGETS = (BOOK, CH2, CH3, SUMMARY)


def staged(stage: Stage) -> Stage:
    stage.fixture("lexical_judge_merge")
    stage.script(SCRIPT)
    return stage


def test_idempotent_rerun_is_byte_identical(stage):
    s = staged(stage)
    r1 = s.run(SCRIPT)
    assert "judged notes collected: 3" in r1.stdout
    assert "book aggregate: 3 judge objects grafted" in r1.stdout
    assert "lexical ch files: 3 grafted; 1 ch-file notes not in book aggregate" in r1.stdout
    snap1 = s.snapshot(*TARGETS)
    assert all(snap1.values()), "every target was actually written"

    s.run(SCRIPT)
    assert s.snapshot(*TARGETS) == snap1


def test_non_shrink_no_record_is_added_or_dropped_anywhere(stage):
    s = staged(stage)
    book_before = records(s.load(BOOK))
    ch2_before = records(s.load(CH2))
    ch3_before = records(s.load(CH3))

    s.run(SCRIPT)

    book_after = records(s.load(BOOK))
    assert len(book_after) == len(book_before) == 4
    assert [(n["shloka"], n["lemma_iast"]) for n in book_after] == \
           [(n["shloka"], n["lemma_iast"]) for n in book_before]
    assert len(records(s.load(CH2))) == len(ch2_before) == 3
    assert len(records(s.load(CH3))) == len(ch3_before) == 1

    # the grafted judge object is the ONLY new key, and only on lexical notes
    for b, a in zip(book_before, book_after):
        assert {k: v for k, v in a.items() if k != "judge"} == b
        assert ("judge" in a) is (a["subtype"] == "lexical")
    verdicts = {(n["shloka"], n["lemma_iast"]): n["judge"]["verdict"]
                for n in book_after if "judge" in n}
    assert verdicts == {("V.2.1", "laṅkā"): "keep",
                        ("V.2.2", "rākṣasī"): "edit",
                        ("V.3.1", "cintā"): "park"}

    # a ch-file card that never reached the aggregate stays unjudged, not deleted
    orphan = next(n for n in records(s.load(CH2)) if n["lemma_iast"] == "vimāna")
    assert "judge" not in orphan
    assert all(n["review_required"] is True for n in records(s.load(CH2)))


def test_summary_and_meta_counts_match_the_grafted_verdicts(stage):
    s = staged(stage)
    s.run(SCRIPT)

    summary = s.load(SUMMARY)
    assert summary["notes_judged"] == 3
    assert summary["verdicts"] == {"keep": 1, "edit": 1, "park": 1}
    assert summary["per_chapter"] == {"2": {"keep": 1, "edit": 1}, "3": {"park": 1}}

    bm = s.load(BOOK)[0]["_meta"]["lexical_judge"]
    assert bm["notes_judged"] == 3
    assert bm["verdicts"] == summary["verdicts"]
    assert s.load(CH2)[0]["_meta"]["lexical_judge"]["verdicts"] == {"keep": 1, "edit": 1}
    assert s.load(CH3)[0]["_meta"]["lexical_judge"]["verdicts"] == {"park": 1}


def test_truncated_chunk_is_refused_without_partial_write(stage):
    s = staged(stage)
    s.truncate(CHUNK1)
    snap = s.snapshot(BOOK, CH2, CH3)
    r = s.run(SCRIPT, expect=None)
    assert r.returncode != 0
    s.assert_unchanged(snap)
    assert not s.path(SUMMARY).exists()


def test_unjudged_chunk_is_refused_without_write(stage):
    s = staged(stage)
    doc = s.load(CHUNK1)
    doc["_meta"]["judged"] = False
    s.write_json(CHUNK1, doc)
    snap = s.snapshot(BOOK, CH2, CH3)
    r = s.run(SCRIPT, expect=1)
    assert "not judged yet" in (r.stdout + r.stderr)
    s.assert_unchanged(snap)


def test_a_book_note_nobody_judged_aborts_before_the_book_is_written(stage):
    s = staged(stage)
    doc = s.load(CHUNK1)
    doc["items"] = doc["items"][:1]
    s.write_json(CHUNK1, doc)
    snap = s.snapshot(BOOK, CH2, CH3)
    r = s.run(SCRIPT, expect=1)
    assert "was never judged" in (r.stdout + r.stderr)
    s.assert_unchanged(snap)

"""backfill_grintser_crossrefs.py — corpus-driven Grintser cross-refs on В-notes.

Target file: data/sundara_commentary_to_add.json (cwd-relative). The corpus
root is a hard-coded Windows path in the script; conftest rewrites that single
line to the sandbox's corpus/ directory. Curated floors at authoring: 896 notes,
155 of type В (see conftest).
"""
from conftest import Stage, records

SCRIPT = "backfill_grintser_crossrefs.py"
BOOK = "data/sundara_commentary_to_add.json"
GLOSS = "corpus/slovar-grintsera-iz-ramayany-1-2.jsonl"


def staged(stage: Stage) -> Stage:
    stage.fixture("backfill_grintser_crossrefs")
    stage.script(SCRIPT, jsonl=str(stage.root / "corpus") + "/")
    return stage


def test_idempotent_second_run_backfills_nothing(stage):
    s = staged(stage)
    r1 = s.run(SCRIPT)
    assert "backfilled 1 Grintser cross-refs" in r1.stdout
    assert "V.1.5" in r1.stdout and "Рам. I.1.7" in r1.stdout
    after1 = s.read(BOOK)
    r2 = s.run(SCRIPT)
    assert "backfilled 0 Grintser cross-refs" in r2.stdout
    assert s.read(BOOK) == after1


def test_non_shrink_records_and_existing_refs_untouched(stage):
    s = staged(stage)
    before = records(s.load(BOOK))
    s.run(SCRIPT)
    after = records(s.load(BOOK))
    assert len(after) == len(before) >= 3
    assert [(n["shloka"], n["lemma_iast"]) for n in after] == \
           [(n["shloka"], n["lemma_iast"]) for n in before]
    filled = next(n for n in after if n["shloka"] == "V.1.5")
    assert filled["cross_ref"] == "Рам. I.1.7 (Гринцер)"
    assert filled["cross_ref_method"] == "corpus_first_appearance"
    assert filled["review_required"] is True
    assert filled["note_ru"].startswith("Агастья — великий мудрец.")
    # a note that already carries a ref, and a non-В note, are byte-identical
    assert next(n for n in after if n["shloka"] == "V.1.6") == \
           next(n for n in before if n["shloka"] == "V.1.6")
    assert next(n for n in after if n["shloka"] == "V.1.7") == \
           next(n for n in before if n["shloka"] == "V.1.7")


def test_truncated_book_is_refused_without_partial_write(stage):
    s = staged(stage)
    s.truncate(BOOK)
    snap = s.snapshot(BOOK)
    r = s.run(SCRIPT, expect=None)
    assert r.returncode != 0
    s.assert_unchanged(snap)


def test_truncated_corpus_line_aborts_before_any_write(stage):
    s = staged(stage)
    s.truncate(GLOSS, keep=0.8)
    snap = s.snapshot(BOOK)
    r = s.run(SCRIPT, expect=None)
    assert r.returncode != 0
    s.assert_unchanged(snap)

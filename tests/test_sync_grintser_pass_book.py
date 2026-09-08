"""sync_grintser_pass_book.py — lands a Grintser style pass on the book twins.

Target file: data/sundara_commentary_to_add.json (cwd-relative), the aggregate
build_sarga_apparatus.py prefers over data/lexical/chN.json. Curated floor at
authoring: 896 notes in the book (see tests/curated_floors.py).
"""
from conftest import Stage, records

SCRIPT = "sync_grintser_pass_book.py"
BOOK = "data/sundara_commentary_to_add.json"
PATCH = "data/lexical/style_pass_h9999/ch2_patch.json"
AUDIT = "data/lexical/style_pass_h9999/book_s2_audit.json"
ARGS = ("--chapter", "2", "--handoff", "h9999")


def staged(stage: Stage) -> Stage:
    stage.fixture("sync_grintser_pass_book")
    stage.script(SCRIPT)
    return stage


def test_idempotent_second_run_is_a_noop(stage):
    s = staged(stage)
    r1 = s.run(SCRIPT, *ARGS)
    assert "book sarga 2: synced=2 unchanged=0 skipped(reject/park)=1" in r1.stdout
    after1 = s.read(BOOK)
    audit1 = s.load(AUDIT)
    assert {a["lemma_iast"] for a in audit1} == {"lanka", "cintā"}
    assert {a["before"] for a in audit1} == {"Старый текст книги 1.",
                                             "Старый текст книги 3."}

    r2 = s.run(SCRIPT, *ARGS)
    assert "book sarga 2: synced=0 unchanged=2 skipped(reject/park)=1" in r2.stdout
    assert s.read(BOOK) == after1, "second run must leave the book byte-identical"
    assert s.load(AUDIT) == audit1, "the audit ledger is not rewritten on a no-op run"


def test_non_shrink_note_multiset_and_out_of_scope_notes_untouched(stage):
    s = staged(stage)
    before = records(s.load(BOOK))
    s.run(SCRIPT, *ARGS)
    after = records(s.load(BOOK))

    assert len(after) == len(before) == 5
    assert [(n["shloka"], n["lemma_iast"]) for n in after] == \
           [(n["shloka"], n["lemma_iast"]) for n in before]

    by_key = {(n["shloka"], n["lemma_iast"]): n for n in after}
    assert by_key[("V.2.1", "lanka")]["note_ru"] == "Ланка — новый гринцеровский текст 1."
    assert by_key[("V.2.1", "lanka")]["style_pass"] == "grintser-H9999"

    rejected = by_key[("V.2.2", "rakshasi")]
    assert rejected["note_ru"] == "Старый текст книги 2.", "reject/park twins are never synced"
    assert "style_pass" not in rejected

    base = by_key[("V.2.4", "setu")]
    assert base["note_ru"].startswith("Базовая заметка"), "non-lexical notes are out of scope"
    assert "style_pass" not in base

    other_sarga = by_key[("V.3.1", "cintā")]
    assert other_sarga["note_ru"] == "Заметка сарги 3 — вне охвата --chapter 2."
    assert "style_pass" not in other_sarga

    # every field other than the two the pass owns survives verbatim
    for b in before:
        a = by_key[(b["shloka"], b["lemma_iast"])]
        assert {k: v for k, v in a.items() if k not in ("note_ru", "style_pass")} == \
               {k: v for k, v in b.items() if k not in ("note_ru", "style_pass")}
        assert a["review_required"] is True


def test_truncated_patch_is_refused_without_partial_write(stage):
    s = staged(stage)
    s.truncate(PATCH)
    snap = s.snapshot(BOOK, AUDIT)
    r = s.run(SCRIPT, *ARGS, expect=None)
    assert r.returncode != 0
    s.assert_unchanged(snap)


def test_patch_without_patches_key_is_refused_without_write(stage):
    s = staged(stage)
    s.write_json(PATCH, {"_meta": {"description": "no patches block"}})
    snap = s.snapshot(BOOK, AUDIT)
    r = s.run(SCRIPT, *ARGS, expect=None)
    assert r.returncode != 0
    s.assert_unchanged(snap)


def test_missing_patch_file_is_refused_without_write(stage):
    s = staged(stage)
    snap = s.snapshot(BOOK, AUDIT)
    r = s.run(SCRIPT, "--chapter", "9", "--handoff", "h9999", expect=None)
    assert r.returncode != 0
    s.assert_unchanged(snap)

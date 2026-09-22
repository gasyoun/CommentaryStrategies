"""sync_grintser_pass_book_s1.py — the H2833 sarga-1 pass on the book aggregate.

Three jobs in one writer: patched lexical twins, two aggregate-only lexical
entries (parivesa, tṛtīya) carrying their own EXTRA texts, and the phantom
«см. примеч. к …» tails dropped from base notes. Target file:
data/sundara_commentary_to_add.json (curated floor 896 notes, tests/curated_floors.py).
"""
from conftest import Stage, records

SCRIPT = "sync_grintser_pass_book_s1.py"
BOOK = "data/sundara_commentary_to_add.json"
PATCH = "data/lexical/style_pass_h2833/ch1_patch.json"
AUDIT = "data/lexical/style_pass_h2833/book_s1_audit.json"


def staged(stage: Stage) -> Stage:
    stage.fixture("sync_grintser_pass_book_s1")
    stage.script(SCRIPT)
    return stage


def keyed(doc) -> dict:
    return {(n["shloka"], n["lemma_iast"]): n for n in records(doc)}


def test_idempotent_second_run_is_a_noop(stage):
    s = staged(stage)
    r1 = s.run(SCRIPT)
    assert "lexical synced=3 base ref-fixes=1" in r1.stdout
    after1 = s.read(BOOK)
    audit1 = s.load(AUDIT)
    assert len(audit1) == 4

    r2 = s.run(SCRIPT)
    assert "lexical synced=0 base ref-fixes=0" in r2.stdout
    assert s.read(BOOK) == after1, "second run must leave the book byte-identical"
    assert s.load(AUDIT) == audit1, "the audit ledger is not rewritten on a no-op run"


def test_non_shrink_note_multiset_and_only_sarga_1_is_touched(stage):
    s = staged(stage)
    before = records(s.load(BOOK))
    s.run(SCRIPT)
    after = records(s.load(BOOK))

    assert len(after) == len(before) == 5
    assert [(n["shloka"], n["lemma_iast"]) for n in after] == \
           [(n["shloka"], n["lemma_iast"]) for n in before]

    by_key = keyed(s.load(BOOK))
    assert by_key[("V.1.1", "cāraṇa")]["note_ru"].startswith("Чараны (cāraṇa)")
    # the two aggregate-only entries get their EXTRA texts, not the patch file's
    assert by_key[("V.1.62", "parivesa")]["note_ru"].startswith("Ореол (pariveṣa")
    assert by_key[("V.1.172", "tṛtīya")]["note_ru"].startswith("Третье (tṛtīya)")
    assert all(by_key[k]["style_pass"] == "grintser-H2833"
               for k in (("V.1.1", "cāraṇa"), ("V.1.62", "parivesa"),
                         ("V.1.172", "tṛtīya"), ("V.1.16", "mainaka")))

    base = by_key[("V.1.16", "mainaka")]
    assert base["note_ru"] == "Майнака поднимается из океана.", \
        "the phantom Grintser tail is dropped, the sentence before it survives"

    out_of_scope = by_key[("V.2.1", "lanka")]
    assert "см. примеч. к I.1.1 (Гринцер)." in out_of_scope["note_ru"], \
        "sarga 2 is out of scope even for the dangling-ref sweep"
    assert "style_pass" not in out_of_scope

    for b in before:
        a = by_key[(b["shloka"], b["lemma_iast"])]
        assert {k: v for k, v in a.items() if k not in ("note_ru", "style_pass")} == \
               {k: v for k, v in b.items() if k not in ("note_ru", "style_pass")}
        assert a["review_required"] is True


def test_audit_ledger_records_every_before_and_after(stage):
    s = staged(stage)
    s.run(SCRIPT)
    audit = s.load(AUDIT)
    rows = {(r["shloka"], r["lemma_iast"]): r for r in audit}
    assert set(rows) == {("V.1.1", "cāraṇa"), ("V.1.62", "parivesa"),
                         ("V.1.172", "tṛtīya"), ("V.1.16", "mainaka")}
    assert rows[("V.1.16", "mainaka")]["subtype"] == "base"
    assert all(r["before"] != r["after"] for r in audit)


def test_truncated_patch_is_refused_without_partial_write(stage):
    s = staged(stage)
    s.truncate(PATCH)
    snap = s.snapshot(BOOK, AUDIT)
    r = s.run(SCRIPT, expect=None)
    assert r.returncode != 0
    s.assert_unchanged(snap)


def test_patch_without_patches_key_is_refused_without_write(stage):
    s = staged(stage)
    s.write_json(PATCH, {"_meta": {"description": "no patches block"}})
    snap = s.snapshot(BOOK, AUDIT)
    r = s.run(SCRIPT, expect=None)
    assert r.returncode != 0
    s.assert_unchanged(snap)

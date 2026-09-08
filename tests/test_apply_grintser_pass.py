"""apply_grintser_pass.py — Grintser style pass, note_ru rewritten in place.

Target file: data/lexical/ch{N}.json (cwd-relative). Curated floors at
authoring: ch2 = 16 cards, ch3 = 13 cards (see conftest).
"""
from conftest import Stage, records

SCRIPT = "apply_grintser_pass.py"
SRC = "data/lexical/ch2.json"
PATCH = "data/lexical/style_pass_h9999/ch2_patch.json"
AUDIT = "data/lexical/style_pass_h9999/ch2_audit.json"
ARGS = ("--chapter", "2", "--handoff", "h9999", "--date", "08-09-2026")


def staged(stage: Stage) -> Stage:
    stage.fixture("apply_grintser_pass")
    stage.script(SCRIPT)
    return stage


def test_idempotent_second_run_is_a_noop(stage):
    s = staged(stage)
    r1 = s.run(SCRIPT, *ARGS)
    assert "applied=2 unchanged=0 skipped(reject/park)=1" in r1.stdout
    after1 = s.read(SRC)
    audit1 = s.load(AUDIT)
    assert len(audit1) == 2 and {a["before"] for a in audit1} == {"Старый текст 1.", "Старый текст 3."}

    r2 = s.run(SCRIPT, *ARGS)
    assert "applied=0 unchanged=2 skipped(reject/park)=1" in r2.stdout
    assert s.read(SRC) == after1, "second run must leave the file byte-identical"
    assert s.load(AUDIT) == audit1, "audit ledger is not rewritten on a no-op run"


def test_non_shrink_card_multiset_and_reject_verdicts_preserved(stage):
    s = staged(stage)
    before = records(s.load(SRC))
    s.run(SCRIPT, *ARGS)
    after = records(s.load(SRC))
    assert len(after) == len(before) >= 3
    assert [(c["shloka"], c["lemma_iast"]) for c in after] == \
           [(c["shloka"], c["lemma_iast"]) for c in before]
    rejected = next(c for c in after if c["shloka"] == "V.2.2")
    assert rejected["note_ru"] == "Старый текст 2.", "reject/park cards are never patched"
    assert "style_pass" not in rejected
    assert all(c["style_pass"] == "grintser-H9999" for c in after if c["shloka"] != "V.2.2")


def test_truncated_patch_is_refused_without_partial_write(stage):
    s = staged(stage)
    s.truncate(PATCH)
    snap = s.snapshot(SRC, AUDIT)
    r = s.run(SCRIPT, *ARGS, expect=None)
    assert r.returncode != 0
    s.assert_unchanged(snap)


def test_patch_key_without_card_is_refused_without_write(stage):
    s = staged(stage)
    patch = s.load(PATCH)
    patch["patches"]["V.2.99|ghost"] = "Карточки нет."
    s.write_json(PATCH, patch)
    snap = s.snapshot(SRC, AUDIT)
    r = s.run(SCRIPT, *ARGS, expect=1)
    assert "patch keys with no matching card" in r.stdout
    s.assert_unchanged(snap)


def test_patch_without_patches_key_is_refused(stage):
    s = staged(stage)
    s.write_json(PATCH, {"_meta": {"description": "no patches block"}})
    snap = s.snapshot(SRC, AUDIT)
    r = s.run(SCRIPT, *ARGS, expect=None)
    assert r.returncode != 0
    s.assert_unchanged(snap)

"""apply_grintser_pass_ch1.py — the sarga-1 (H2833) variant with fixed paths.

Target file: data/lexical/ch1.json (cwd-relative constant). Curated floor at
authoring: 58 cards (see tests/curated_floors.py).
"""
from conftest import Stage, records

SCRIPT = "apply_grintser_pass_ch1.py"
SRC = "data/lexical/ch1.json"
PATCH = "data/lexical/style_pass_h2833/ch1_patch.json"
AUDIT = "data/lexical/style_pass_h2833/ch1_audit.json"


def staged(stage: Stage) -> Stage:
    stage.fixture("apply_grintser_pass_ch1")
    stage.script(SCRIPT)
    return stage


def test_idempotent_second_run_is_a_noop(stage):
    s = staged(stage)
    r1 = s.run(SCRIPT)
    assert "applied=2 unchanged=0 skipped(reject/park)=1" in r1.stdout
    after1 = s.read(SRC)
    r2 = s.run(SCRIPT)
    assert "applied=0 unchanged=2 skipped(reject/park)=1" in r2.stdout
    assert s.read(SRC) == after1


def test_non_shrink_card_multiset_and_park_verdict_preserved(stage):
    s = staged(stage)
    before = records(s.load(SRC))
    s.run(SCRIPT)
    after = records(s.load(SRC))
    assert len(after) == len(before) >= 3
    assert [(c["shloka"], c["lemma_iast"]) for c in after] == \
           [(c["shloka"], c["lemma_iast"]) for c in before]
    parked = next(c for c in after if c["shloka"] == "V.1.2")
    assert parked["note_ru"] == "Старый текст 2."
    assert s.load(SRC)[0]["_meta"]["style_pass"].startswith("grintser-H2833")


def test_truncated_patch_is_refused_without_partial_write(stage):
    s = staged(stage)
    s.truncate(PATCH)
    snap = s.snapshot(SRC, AUDIT)
    r = s.run(SCRIPT, expect=None)
    assert r.returncode != 0
    s.assert_unchanged(snap)


def test_patch_key_without_card_is_refused_without_write(stage):
    s = staged(stage)
    patch = s.load(PATCH)
    patch["patches"]["V.1.99|ghost"] = "Карточки нет."
    s.write_json(PATCH, patch)
    snap = s.snapshot(SRC, AUDIT)
    r = s.run(SCRIPT, expect=1)
    assert "patch keys with no matching card" in r.stdout
    s.assert_unchanged(snap)

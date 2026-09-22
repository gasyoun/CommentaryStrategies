"""apply_translit_decisions.py — the h2864 transliteration vote as string repairs.

Targets: every note-bearing source JSON from translit_hygiene.target_files()
(here data/lexical/ch1.json). Curated floors at authoring: 45 residue cards,
ch1 = 58 cards (see tests/curated_floors.py).
"""
from conftest import Stage, records

SCRIPT = "apply_translit_decisions.py"
VOTES = "votes/translit_decisions.json"
CH1 = "data/lexical/ch1.json"


def staged(stage: Stage) -> Stage:
    stage.fixture("apply_translit_decisions")
    stage.script("translit_hygiene.py")
    stage.script(SCRIPT)
    return stage


def test_dry_run_by_default_then_idempotent_apply(stage):
    s = staged(stage)
    snap = s.snapshot(CH1)
    r0 = s.run(SCRIPT, VOTES)
    assert "сухой прогон" in r0.stdout and "к исправлению 2" in r0.stdout
    s.assert_unchanged(snap)

    r1 = s.run(SCRIPT, VOTES, "--apply")
    assert "изменено файлов: 1" in r1.stdout
    after1 = s.read(CH1)
    text = after1.decode("utf-8")
    assert "каруна" in text and "каруṇa" not in text
    assert "Рама" in text and "Рāма" not in text

    r2 = s.run(SCRIPT, VOTES, "--apply")
    assert "изменено файлов: 0" in r2.stdout
    assert s.read(CH1) == after1


def test_non_shrink_records_and_untouched_fields_survive(stage):
    s = staged(stage)
    before = records(s.load(CH1))
    s.run(SCRIPT, VOTES, "--apply")
    after = records(s.load(CH1))
    assert len(after) == len(before) >= 2
    assert [(c["shloka"], c["lemma_iast"]) for c in after] == \
           [(c["shloka"], c["lemma_iast"]) for c in before]
    for b, a in zip(before, after):
        assert {k: v for k, v in a.items() if k != "note_ru"} == \
               {k: v for k, v in b.items() if k != "note_ru"}


def test_wrong_sheet_is_refused_without_write(stage):
    s = staged(stage)
    snap = s.snapshot(CH1)
    doc = s.load(VOTES)
    doc["sheet_id"] = "some_other_sheet"
    s.write_json("votes/wrong.json", doc)
    r = s.run(SCRIPT, "votes/wrong.json", "--apply", expect=1)
    assert "REFUSE" in r.stderr
    s.assert_unchanged(snap)


def test_truncated_export_is_refused_without_write(stage):
    s = staged(stage)
    s.truncate(VOTES)
    snap = s.snapshot(CH1)
    r = s.run(SCRIPT, VOTES, "--apply", expect=None)
    assert r.returncode != 0
    s.assert_unchanged(snap)


def test_missing_policy_vote_blocks_before_any_write(stage):
    s = staged(stage)
    snap = s.snapshot(CH1)
    doc = s.load(VOTES)
    doc["items"] = [i for i in doc["items"] if i["id"] != "policy-fork-rows"]
    s.write_json("votes/no_policy.json", doc)
    r = s.run(SCRIPT, "votes/no_policy.json", "--apply", expect=2)
    assert "ОСТАНОВ" in r.stdout and "policy-fork-rows" in r.stdout
    s.assert_unchanged(snap)

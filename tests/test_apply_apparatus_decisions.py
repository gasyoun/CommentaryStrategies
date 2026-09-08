"""apply_apparatus_decisions.py — reviewer verdicts into the gate ledger overlay.

Target file: data/apparatus/gate_ledger.json (schema v2, entries keyed by
apparatus note id). Curated floor at authoring: 126 entries (see tests/curated_floors.py).
"""
from conftest import Stage

SCRIPT = "apply_apparatus_decisions.py"
LEDGER = "data/apparatus/gate_ledger.json"
VOTES = "votes/decisions_sarga_1.json"


def staged(stage: Stage) -> Stage:
    stage.fixture("apply_apparatus_decisions")
    stage.script("gate_ledger.py")
    stage.script(SCRIPT)
    return stage


def test_idempotent_second_run_replaces_only_own_verdicts(stage):
    s = staged(stage)
    before = s.load(LEDGER)
    assert len(before["entries"]) == 2

    r1 = s.run(SCRIPT, VOTES, "--reviewer", "Леонов")
    after1 = s.load(LEDGER)
    # 2 pre-existing + 2 new ids (lexical:5.1.1:0 already existed, gains a verdict)
    assert len(after1["entries"]) == 4
    assert "own re-votes replaced: 0" in r1.stdout
    assert after1["entries"]["lexical:5.1.1:0"]["verdicts"]["Леонов"]["action"] == "accept"

    r2 = s.run(SCRIPT, VOTES, "--reviewer", "Леонов")
    after2 = s.load(LEDGER)
    assert len(after2["entries"]) == 4, "second run must not add entries"
    assert "own re-votes replaced: 3" in r2.stdout
    assert after2["entries"] == after1["entries"], "re-vote with same ballot is a no-op"


def test_non_shrink_colleague_verdicts_and_other_sargas_survive(stage):
    s = staged(stage)
    before = s.load(LEDGER)
    kostina_before = before["entries"]["lexical:5.1.1:0"]["verdicts"]["Костина"]
    other_sarga_before = before["entries"]["lexical:5.2.4:0"]

    s.run(SCRIPT, VOTES, "--reviewer", "Леонов")
    after = s.load(LEDGER)
    assert len(after["entries"]) >= len(before["entries"])
    # A colleague's verdict on the same id is never touched …
    assert after["entries"]["lexical:5.1.1:0"]["verdicts"]["Костина"] == kostina_before
    # … and the conflict is reported, not resolved.
    assert set(after["entries"]["lexical:5.1.1:0"]["verdicts"]) == {"Костина", "Леонов"}
    # Entries from other sargas are untouched byte-for-byte.
    assert after["entries"]["lexical:5.2.4:0"] == other_sarga_before


def test_require_agreement_refuses_and_writes_nothing(stage):
    s = staged(stage)
    snap = s.snapshot(LEDGER)
    r = s.run(SCRIPT, VOTES, "--reviewer", "Леонов", "--require-agreement", expect=1)
    assert "disagreement" in r.stdout + r.stderr
    s.assert_unchanged(snap)


def test_dry_run_writes_nothing(stage):
    s = staged(stage)
    snap = s.snapshot(LEDGER)
    r = s.run(SCRIPT, VOTES, "--reviewer", "Леонов", "--dry-run")
    assert "[DRY RUN]" in r.stdout
    s.assert_unchanged(snap)


def test_truncated_export_is_refused_without_partial_write(stage):
    s = staged(stage)
    s.truncate(VOTES)
    snap = s.snapshot(LEDGER)
    r = s.run(SCRIPT, VOTES, "--reviewer", "Леонов", expect=None)
    assert r.returncode != 0
    s.assert_unchanged(snap)


def test_malformed_export_shapes_are_refused(stage):
    s = staged(stage)
    snap = s.snapshot(LEDGER)
    good = s.load(VOTES)

    no_sarga = dict(good)
    no_sarga.pop("sarga")
    s.write_json("votes/no_sarga.json", no_sarga)
    r = s.run(SCRIPT, "votes/no_sarga.json", "--reviewer", "Леонов", expect=1)
    assert "no integer 'sarga'" in r.stderr

    empty = dict(good, decisions={})
    s.write_json("votes/empty.json", empty)
    r = s.run(SCRIPT, "votes/empty.json", "--reviewer", "Леонов", expect=1)
    assert "carries no 'decisions'" in r.stderr

    bad_action = dict(good)
    bad_action["decisions"] = {k: dict(v) for k, v in good["decisions"].items()}
    bad_action["decisions"]["lexical:5.1.1:1"]["action"] = "maybe"
    s.write_json("votes/bad_action.json", bad_action)
    r = s.run(SCRIPT, "votes/bad_action.json", "--reviewer", "Леонов", expect=1)
    assert "unknown action" in r.stderr

    drifted = dict(good)
    drifted["decisions"] = dict(good["decisions"])
    drifted["decisions"]["lexical:5.9.9:0"] = dict(good["decisions"]["lexical:5.1.1:0"])
    s.write_json("votes/drifted.json", drifted)
    r = s.run(SCRIPT, "votes/drifted.json", "--reviewer", "Леонов", expect=1)
    assert "absent from the current apparatus" in r.stderr

    tier1 = dict(good)
    tier1["decisions"] = dict(good["decisions"])
    tier1["decisions"]["tier1:5.1.1:0"] = dict(good["decisions"]["lexical:5.1.1:0"])
    s.write_json("votes/tier1.json", tier1)
    r = s.run(SCRIPT, "votes/tier1.json", "--reviewer", "Леонов", expect=1)
    assert "non-votable" in r.stderr

    s.assert_unchanged(snap)

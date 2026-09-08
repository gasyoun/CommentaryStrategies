"""h1685_merge_ledger.py — merge the rule tier and the Opus tier into one ledger.

Target file: data/analysis/h1685_adjudication/ledger_final.json — one row per
queued card, the file the H1685 Definition of Done is measured against. Every
card must carry exactly one verdict; zero or two is a loud failure.
"""
from conftest import Stage

SCRIPT = "h1685_merge_ledger.py"
AD = "data/analysis/h1685_adjudication"
EVIDENCE = f"{AD}/evidence.json"
RULE = f"{AD}/ledger.json"
OPUS_B2 = f"{AD}/opus_verdicts_batch2.json"
OUT = f"{AD}/ledger_final.json"


def staged(stage: Stage) -> Stage:
    stage.fixture("h1685_merge_ledger")
    stage.script(SCRIPT)
    return stage


def test_idempotent_rerun_is_byte_identical(stage):
    s = staged(stage)
    r1 = s.run(SCRIPT)
    assert "cards: 4  tiers: {'rule': 1, 'opus': 3}" in r1.stdout
    first = s.read(OUT)
    s.run(SCRIPT)
    assert s.read(OUT) == first, "a second merge must produce the same ledger"


def test_non_shrink_every_queued_card_gets_exactly_one_row(stage):
    s = staged(stage)
    cards = s.load(EVIDENCE)["cards"]
    s.run(SCRIPT)

    doc = s.load(OUT)
    rows = doc["verdicts"]
    assert len(rows) == len(cards) == 4
    assert [r["card_id"] for r in rows] == [c["card_id"] for c in cards], \
        "row order follows the evidence pack, one row per card"
    assert len({r["card_id"] for r in rows}) == len(rows), "no card decided twice"
    assert all(r["verdict"] for r in rows), "no card left without a verdict"

    by_id = {r["card_id"]: r for r in rows}
    assert by_id["b2-0001"]["tier"] == "rule" and by_id["b2-0001"]["rule_id"] == "R1"
    assert by_id["b2-0002"]["tier"] == "opus"
    assert by_id["b2-0002"]["adjudicator"].startswith("Opus 5")
    # apply_action is the gate apply_phase2_decisions.py reads: park never applies
    assert by_id["b2-0002"]["apply_action"] == "reject"
    assert by_id["fn-0001"]["apply_action"] is None
    # a scalar evidence string is normalised to a list, never dropped
    assert by_id["lex-0001"]["evidence_cited"] == ["MW s.v. cintā"]

    m = doc["_meta"]
    assert m["total_cards"] == len(rows)
    assert m["by_tier"] == {"rule": 1, "opus": 3}
    assert m["by_verdict"] == {"accept": 1, "reject": 1, "edit": 1, "park": 1}
    assert m["by_queue"]["batch2"] == {"accept": 1, "reject": 1}
    assert m["cards_with_a_prior_judge_verdict"] == 3
    assert m["adjudicator_overturns"] == 1
    assert m["overturned_cards"] == [{"card_id": "b2-0002", "judge": "park",
                                      "adjudicator": "reject"}]


def test_truncated_evidence_is_refused_without_a_ledger(stage):
    s = staged(stage)
    s.truncate(EVIDENCE)
    r = s.run(SCRIPT, expect=None)
    assert r.returncode != 0
    assert not s.path(OUT).exists(), "no partial ledger is written"


def test_truncated_opus_packet_is_refused_without_a_ledger(stage):
    s = staged(stage)
    s.truncate(OPUS_B2)
    r = s.run(SCRIPT, expect=None)
    assert r.returncode != 0
    assert not s.path(OUT).exists()


def test_a_card_with_no_verdict_aborts_without_write(stage):
    s = staged(stage)
    doc = s.load(OPUS_B2)
    doc["verdicts"] = []
    s.write_json(OPUS_B2, doc)
    r = s.run(SCRIPT, expect=1)
    assert "cards with NO verdict" in (r.stdout + r.stderr)
    assert not s.path(OUT).exists()


def test_a_card_decided_twice_aborts_without_write(stage):
    s = staged(stage)
    doc = s.load(OPUS_B2)
    doc["verdicts"].append({"key": "5.2.1|laṅkā", "verdict": "reject",
                            "reason": "второй вердикт на ту же карточку",
                            "evidence_cited": []})
    s.write_json(OPUS_B2, doc)
    r = s.run(SCRIPT, expect=1)
    assert "decided twice" in (r.stdout + r.stderr)
    assert not s.path(OUT).exists()


def test_an_opus_verdict_matching_no_card_aborts_without_write(stage):
    s = staged(stage)
    doc = s.load(OPUS_B2)
    doc["verdicts"].append({"key": "5.9.9|ghost", "verdict": "accept",
                            "reason": "карточки нет", "evidence_cited": []})
    s.write_json(OPUS_B2, doc)
    r = s.run(SCRIPT, expect=1)
    assert "match no card" in (r.stdout + r.stderr)
    assert not s.path(OUT).exists()


def test_a_missing_queue_packet_aborts_without_write(stage):
    s = staged(stage)
    s.path(f"{AD}/opus_verdicts_batch3.json").unlink()
    r = s.run(SCRIPT, expect=1)
    assert "missing" in (r.stdout + r.stderr)
    assert not s.path(OUT).exists()

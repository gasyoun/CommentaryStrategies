#!/usr/bin/env python3
"""Selftest for the dual-reviewer assembly-gate ledger (schema v2, H2574).

Guards the three properties whose absence made a two-gatekeeper gate (ruling R1:
Leonov AND Kostina gate the final assembly) impossible before this change:

  1. a v1 ledger upgrades losslessly — the 126 real Leonov verdicts of
     2026-07-11 must survive verbatim, not be "migrated" into approximations;
  2. the second reviewer's verdict does NOT erase the first's (the v1 defect:
     one record per note id with `reviewer` as a field + `entries.update(...)`);
  3. disagreement is detected and left standing, never silently merged.

Plus the two bugs that blocked collecting a second ballot at all:
  4. apparatus_notes() reads `votable` as INTRINSIC (layer != tier1), so a
     colleague's recorded verdict cannot make a whole ballot fail validation;
  5. build_sarga_apparatus.apply_gate() suppresses the control only for the
     reviewer who already voted — a colleague's verdict leaves it live.

Run: python scripts/gate_ledger_selftest.py
"""
import json
import os
import sys
import tempfile

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import gate_ledger                      # noqa: E402
import build_sarga_apparatus as bsa      # noqa: E402

FAILED = []


def check(label, cond, detail=""):
    print(f"  {'ok  ' if cond else 'FAIL'} {label}" + (f" — {detail}" if detail else ""))
    if not cond:
        FAILED.append(label)


def v1_fixture():
    """A schema-v1 ledger exactly as apply_apparatus_decisions.py used to write."""
    return {
        "_meta": {"description": "old", "schema": 1,
                  "generated_by": "scripts/apply_apparatus_decisions.py"},
        "entries": {
            "lexical:5.1.1:0": {"layer": "lexical", "verse_id": "5.1.1",
                                "lemma_iast": "cāraṇa", "reviewer": "Леонов",
                                "action": "accept", "gated_date": "2026-07-11",
                                "ts": "2026-07-11T09:15:00.000Z"},
            "crosstext:5.1.4:0": {"layer": "crosstext", "verse_id": "5.1.4",
                                  "reviewer": "Леонов", "action": "edit",
                                  "gated_date": "2026-07-11",
                                  "edited_note": "правленый текст Леонова"},
        },
    }


def test_v1_upgrade_lossless():
    print("1. v1 -> v2 upgrade is lossless")
    with tempfile.TemporaryDirectory() as td:
        p = os.path.join(td, "gate_ledger.json")
        with open(p, "w", encoding="utf-8") as fh:
            json.dump(v1_fixture(), fh, ensure_ascii=False)
        led = gate_ledger.load(p)
        check("schema bumped to 2", led["_meta"]["schema"] == 2)
        check("provenance of the old schema kept",
              led["_meta"].get("upgraded_from_schema") == 1)
        e = led["entries"]["lexical:5.1.1:0"]
        check("note-level fields preserved",
              (e["layer"], e["verse_id"], e["lemma_iast"])
              == ("lexical", "5.1.1", "cāraṇa"))
        v = e["verdicts"]["Леонов"]
        check("Leonov's verdict verbatim under his name",
              v == {"action": "accept", "gated_date": "2026-07-11",
                    "ts": "2026-07-11T09:15:00.000Z"}, str(v))
        check("an `edit`'s text survives the upgrade",
              gate_ledger.verdicts(led, "crosstext:5.1.4:0")["Леонов"]["edited_note"]
              == "правленый текст Леонова")
        check("reviewer roster derivable", gate_ledger.reviewers(led) == ["Леонов"])
        # round-trip: saving then reloading must not drift
        gate_ledger.save(p, led)
        check("v2 round-trips unchanged",
              gate_ledger.load(p)["entries"] == led["entries"])


def test_second_reviewer_does_not_erase_first():
    print("2. the second reviewer never erases the first (the v1 defect)")
    led = gate_ledger.load(os.devnull + "-missing")
    nid = "lexical:5.1.1:0"
    fields = {"layer": "lexical", "verse_id": "5.1.1", "lemma_iast": "cāraṇa"}
    gate_ledger.record(led, nid, "Леонов", fields,
                       {"action": "accept", "gated_date": "2026-07-11"})
    replaced = gate_ledger.record(led, nid, "Костина", fields,
                                  {"action": "accept", "gated_date": "2026-08-11"})
    vs = gate_ledger.verdicts(led, nid)
    check("both verdicts present", sorted(vs) == ["Костина", "Леонов"], str(sorted(vs)))
    check("Leonov's date untouched by Kostina's vote",
          vs["Леонов"]["gated_date"] == "2026-07-11")
    check("a colleague's vote is not reported as a replacement", replaced is False)
    check("one shared entry, not two", len(led["entries"]) == 1)
    # own re-vote IS a replacement (legitimate after a rebuild)
    again = gate_ledger.record(led, nid, "Костина", fields,
                               {"action": "reject", "reject_reason": "дубль"})
    check("own re-vote reported as a replacement", again is True)
    vs = gate_ledger.verdicts(led, nid)
    check("re-vote replaced only her own verdict",
          vs["Костина"]["action"] == "reject" and vs["Леонов"]["action"] == "accept")
    check("empty fields are not persisted",
          "ts" not in vs["Костина"], str(vs["Костина"]))


def test_conflict_detection():
    print("3. disagreement is detected, never merged away")
    check("agreement -> no conflict",
          gate_ledger.conflict({"Леонов": {"action": "accept"},
                                "Костина": {"action": "accept"}}) is False)
    check("accept vs reject -> conflict",
          gate_ledger.conflict({"Леонов": {"action": "accept"},
                                "Костина": {"action": "reject"}}) is True)
    check("accept vs edit -> conflict (different editorial outcome)",
          gate_ledger.conflict({"Леонов": {"action": "accept"},
                                "Костина": {"action": "edit"}}) is True)
    check("different edit text -> conflict",
          gate_ledger.conflict({"Леонов": {"action": "edit", "edited_note": "A"},
                                "Костина": {"action": "edit", "edited_note": "B"}}) is True)
    check("identical edit text -> eligible edited",
          gate_ledger.derived_outcome(
              {"Леонов": {"action": "edit", "edited_note": "A"},
               "Костина": {"action": "edit", "edited_note": "A"}}) ==
          "eligible_edited")
    check("reject veto -> editorial queue",
          gate_ledger.derived_outcome(
              {"Леонов": {"action": "accept"},
               "Костина": {"action": "reject"}}) == "editorial_queue")
    check("single reviewer -> pending",
          gate_ledger.derived_outcome({"Леонов": {"action": "accept"}}) == "pending")
    check("a single verdict is never a conflict",
          gate_ledger.conflict({"Леонов": {"action": "reject"}}) is False)


def test_votable_is_intrinsic():
    print("4. `votable` is intrinsic (layer != tier1), not the sheet's live state")
    import apply_apparatus_decisions as aad
    check("apply-side recompute reads the layer, not the built flag",
          "tier1" in aad.apparatus_notes.__doc__ and
          'n.get("layer") != "tier1"' in open(
              os.path.join(HERE, "apply_apparatus_decisions.py"),
              encoding="utf-8").read())


def test_apply_gate_keeps_colleague_cards_live():
    print("5. apply_gate: my verdict closes the card, a colleague's does not")
    ledger = {"lexical:5.1.1:0": {"layer": "lexical", "verse_id": "5.1.1",
                                  "verdicts": {"Леонов": {
                                      "action": "accept",
                                      "gated_date": "2026-07-11"}}}}

    def note():
        return {"id": "lexical:5.1.1:0", "layer": "lexical", "votable": True,
                "note_ru": "исходный текст", "status": "review_required"}

    n = bsa.apply_gate(note(), ledger, for_reviewer="Костина")
    check("colleague voted -> still votable for Kostina", n["votable"] is True)
    check("his verdict is shown on her card", "Леонов" in n["status"], n["status"])
    check("verdict exposed to the template", "Леонов" in n.get("gate_verdicts", {}))

    n = bsa.apply_gate(note(), ledger, for_reviewer="Леонов")
    check("own verdict -> control withdrawn", n["votable"] is False)

    n = bsa.apply_gate(note(), ledger, for_reviewer=None)
    check("neutral build stays read-only", n["votable"] is False)

    # an edit by a colleague must surface as the text under discussion
    led2 = {"lexical:5.1.1:0": {"layer": "lexical", "verdicts": {"Леонов": {
        "action": "edit", "gated_date": "2026-07-11",
        "edited_note": "правленый текст"}}}}
    n = bsa.apply_gate(note(), led2, for_reviewer="Костина")
    check("colleague's edited text is what she reviews",
          n["note_ru"] == "правленый текст", n["note_ru"])
    check("card stays votable after a colleague's edit", n["votable"] is True)

    # unanimous reject drops the note; a split verdict must NOT
    led3 = {"lexical:5.1.1:0": {"layer": "lexical", "verdicts": {
        "Леонов": {"action": "reject"}, "Костина": {"action": "reject"}}}}
    check("unanimous reject -> dropped",
          bsa.apply_gate(note(), led3, for_reviewer=None).get("gate_rejected") is True)
    led4 = {"lexical:5.1.1:0": {"layer": "lexical", "verdicts": {
        "Леонов": {"action": "reject"}, "Костина": {"action": "accept"}}}}
    check("split verdict is NOT auto-dropped",
          bsa.apply_gate(note(), led4, for_reviewer=None).get("gate_rejected") is None)


def test_live_ledger_upgrades():
    print("6. the real on-disk ledger upgrades and keeps every Leonov verdict")
    path = os.path.join(os.path.dirname(HERE), "data", "apparatus",
                        "gate_ledger.json")
    if not os.path.exists(path):
        print("  skip — no ledger on disk")
        return
    raw = json.load(open(path, encoding="utf-8"))
    led = gate_ledger.load(path)
    check("entry count unchanged by the upgrade",
          len(led["entries"]) == len(raw.get("entries", {})),
          f"{len(raw.get('entries', {}))} -> {len(led['entries'])}")
    per = {}
    for e in led["entries"].values():
        for r in (e.get("verdicts") or {}):
            per[r] = per.get(r, 0) + 1
    check("every entry carries at least one attributed verdict",
          sum(per.values()) >= len(led["entries"]), str(per))
    check("no verdict attributed to '(unknown)'", "(unknown)" not in per, str(per))


def main():
    print("gate ledger selftest (schema v2 · dual reviewer · H2574)")
    for t in (test_v1_upgrade_lossless,
              test_second_reviewer_does_not_erase_first,
              test_conflict_detection,
              test_votable_is_intrinsic,
              test_apply_gate_keeps_colleague_cards_live,
              test_live_ledger_upgrades):
        t()
    print()
    if FAILED:
        sys.exit(f"FAILED ({len(FAILED)}): {FAILED}")
    print("all checks passed")


if __name__ == "__main__":
    main()

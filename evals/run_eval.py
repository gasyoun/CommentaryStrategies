#!/usr/bin/env python3
"""Deterministic eval runner for CommentaryStrategies (H6846).

Suite ``apparatus-gate-locus`` grades the human final-assembly gate overlay
(``data/apparatus/gate_ledger.json``) against the per-sarga apparatus files it
was applied to. It creates no gold and calls no model: every check is an exact
match over committed data.

Usage::

    python evals/run_eval.py             # gold replay, exit 0 iff all loci resolve
    python evals/run_eval.py --canary    # gold passes AND a mutated ledger fails
    python evals/run_eval.py --json      # machine-readable result
"""

import argparse
import copy
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
APPARATUS = REPO / "data" / "apparatus"
LEDGER = APPARATUS / "gate_ledger.json"
ACTIONS = {"accept", "reject"}

_verse_cache = {}


def load_ledger(path=LEDGER):
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def _notes_for(verse_id):
    """Return {verse_id: {note_id: note}} for the sarga named by verse_id."""
    try:
        sarga = int(verse_id.split(".")[1])
    except (IndexError, ValueError):
        raise KeyError("unparseable verse_id: %r" % verse_id)
    path = APPARATUS / ("sarga_%02d.json" % sarga)
    if path not in _verse_cache:
        with open(path, "r", encoding="utf-8") as fh:
            data = json.load(fh)
        _verse_cache[path] = {
            verse["verse_id"]: {n["id"]: n for n in verse.get("notes", [])}
            for verse in data.get("verses", [])
        }
    return _verse_cache[path]


def grade(ledger):
    """Return a list of human-readable errors; empty means the ledger is sound."""
    errors = []
    for key, entry in ledger.get("entries", {}).items():
        parts = key.split(":")
        if len(parts) != 3:
            errors.append("%s: key is not layer:verse_id:index" % key)
            continue
        layer, verse_id, _idx = parts
        if entry.get("layer") != layer:
            errors.append("%s: entry layer %r != key layer %r" % (key, entry.get("layer"), layer))
        if entry.get("verse_id") != verse_id:
            errors.append("%s: entry verse_id %r != key verse_id %r" % (key, entry.get("verse_id"), verse_id))
        verdicts = entry.get("verdicts") or {}
        if not verdicts:
            errors.append("%s: no reviewer verdicts" % key)
        for reviewer, verdict in verdicts.items():
            if verdict.get("action") not in ACTIONS:
                errors.append("%s: %s action %r not in %s" % (key, reviewer, verdict.get("action"), sorted(ACTIONS)))
        try:
            verses = _notes_for(verse_id)
        except (KeyError, OSError) as exc:
            errors.append("%s: sarga unavailable (%s)" % (key, exc))
            continue
        if verse_id not in verses:
            errors.append("%s: verse %s absent from the apparatus" % (key, verse_id))
            continue
        note = verses[verse_id].get(key)
        if note is None:
            errors.append("%s: note absent from verse %s" % (key, verse_id))
            continue
        if note.get("layer") != layer:
            errors.append("%s: note layer %r != %r" % (key, note.get("layer"), layer))
        entry_lemma = entry.get("lemma_iast") or ""
        note_lemma = note.get("lemma_iast") or ""
        if entry_lemma and note_lemma and entry_lemma != note_lemma:
            errors.append("%s: ledger lemma %r != note lemma %r" % (key, entry_lemma, note_lemma))
    return errors


def mutate(ledger):
    """Return a copy with the first verdict re-pointed at a nonexistent verse."""
    mutated = copy.deepcopy(ledger)
    entries = mutated.get("entries") or {}
    if not entries:
        return mutated
    key = next(iter(entries))
    entry = entries.pop(key)
    layer, _verse_id, idx = key.split(":", 2)
    bad_verse = "5.1.999"
    entry["verse_id"] = bad_verse
    entries["%s:%s:%s" % (layer, bad_verse, idx)] = entry
    return mutated


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--canary", action="store_true", help="also require a mutated ledger to fail")
    parser.add_argument("--json", action="store_true", help="print a JSON result object")
    args = parser.parse_args()

    ledger = load_ledger()
    gold_errors = grade(ledger)
    result = {
        "suite": "apparatus-gate-locus",
        "cases": len(ledger.get("entries", {})),
        "gold": "PASS" if not gold_errors else "FAIL",
        "gold_errors": gold_errors,
    }

    ok = not gold_errors
    if args.canary:
        mutated_errors = grade(mutate(ledger))
        result["canary"] = {
            "mutation": "first verdict re-pointed to verse 5.99.99",
            "mutation_result": "FAIL" if mutated_errors else "PASS",
            "mutation_errors": mutated_errors,
        }
        ok = ok and bool(mutated_errors)

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=1))
    else:
        print("== apparatus-gate-locus: gold %s (%d cases) ==" % (result["gold"], result["cases"]))
        for err in gold_errors:
            print("  - " + err)
        if args.canary:
            canary = result["canary"]
            print("== canary: mutated answer %s (expected FAIL) ==" % canary["mutation_result"])
            for err in canary["mutation_errors"][:3]:
                print("  - " + err)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())

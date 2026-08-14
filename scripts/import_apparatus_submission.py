#!/usr/bin/env python3
"""Transaction-like, idempotent schema-v2 import of a validated raw submission."""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")
HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
import gate_ledger  # noqa: E402
from validate_apparatus_submission import canonical, validate  # noqa: E402


def reviewer_subtree(doc: dict, reviewer: str) -> dict:
    return {note_id: entry["verdicts"][reviewer]
            for note_id, entry in doc.get("entries", {}).items()
            if reviewer in (entry.get("verdicts") or {})}


def subtree_hash(doc: dict, reviewer: str) -> str:
    return hashlib.sha256(canonical(reviewer_subtree(doc, reviewer))).hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("submission", type=Path)
    ap.add_argument("--ledger", type=Path,
                    default=ROOT / "data" / "apparatus" / "gate_ledger.json")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    submission = json.loads(args.submission.read_text(encoding="utf-8"))
    failures = validate(submission)
    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1
    before = gate_ledger.load(str(args.ledger))
    leonov_before = subtree_hash(before, "Леонов")
    out = copy.deepcopy(before)
    inserted = idempotent = 0
    stamp = str(submission.get("client_timestamp", ""))
    gated_date = stamp[:10]
    for row in submission["sargas"]:
        for note_id, decision in row["decisions"].items():
            prior = gate_ledger.verdicts(out, note_id).get("Костина")
            verdict = {k: decision.get(k) for k in
                       ("action", "edited_note", "reject_reason", "ts")
                       if decision.get(k) not in (None, "")}
            verdict.setdefault("ts", stamp)
            verdict["gated_date"] = gated_date
            if prior:
                comparable = {k: prior.get(k) for k in verdict}
                if comparable != verdict:
                    print(f"FAIL: conflicting prior Kostina import for {note_id}; raw evidence is immutable")
                    return 1
                idempotent += 1
                continue
            parts = note_id.split(":")
            note_fields = {"layer": decision.get("layer") or parts[0],
                           "verse_id": decision.get("verse_id") or parts[1],
                           "lemma_iast": decision.get("lemma_iast", "")}
            gate_ledger.record(out, note_id, "Костина", note_fields, verdict)
            inserted += 1
    leonov_after = subtree_hash(out, "Леонов")
    if leonov_after != leonov_before:
        print("FAIL: Leonov subtree changed; refusing write")
        return 1
    gate_ledger.save(str(args.ledger), out, dry=args.dry_run)
    print(f"PASS: inserted={inserted}; idempotent={idempotent}; dry_run={args.dry_run}")
    print(f"PASS: Leonov count={len(reviewer_subtree(out, 'Леонов'))}; sha256={leonov_after}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

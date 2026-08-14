#!/usr/bin/env python3
"""Strict validation for immutable 68-sarga reviewer submissions."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "data" / "apparatus" / "reviewer_manifest.json"
ACTIONS = {"accept", "edit", "reject"}


def canonical(doc: object) -> bytes:
    return json.dumps(doc, ensure_ascii=False, sort_keys=True,
                      separators=(",", ":")).encode("utf-8")


def validate(doc: dict, manifest: dict | None = None) -> list[str]:
    manifest = manifest or json.loads(MANIFEST.read_text(encoding="utf-8"))
    errors: list[str] = []
    if doc.get("schema_version") != 1 or doc.get("reviewer") != "Костина":
        errors.append("schema_version/reviewer mismatch")
    if doc.get("manifest_hash") != manifest.get("manifest_hash"):
        errors.append("manifest_hash mismatch")
    if doc.get("source_hash") != manifest.get("source_hash"):
        errors.append("source_hash mismatch")
    rows = doc.get("sargas")
    if not isinstance(rows, list) or [r.get("sarga") for r in rows] != list(range(1, 69)):
        errors.append("sargas must be exactly ordered unique 1–68")
        return errors
    allowed_by_sarga: dict[int, dict[str, dict]] = {}
    for entry in manifest["sargas"]:
        ballot = json.loads((MANIFEST.parent / entry["data_url"]).read_text(encoding="utf-8"))
        allowed_by_sarga[entry["sarga"]] = {
            note["id"]: note for verse in ballot["verses"] for note in verse["notes"]
            if note.get("votable")
        }
    seen: set[str] = set()
    for row, entry in zip(rows, manifest["sargas"]):
        if row.get("source_hash") != entry["source_hash"]:
            errors.append(f"sarga {entry['sarga']}: source_hash mismatch")
        decisions = row.get("decisions")
        if not isinstance(decisions, dict):
            errors.append(f"sarga {entry['sarga']}: decisions must be an object")
            continue
        for note_id, decision in decisions.items():
            if note_id in seen:
                errors.append(f"duplicate decision id: {note_id}")
            seen.add(note_id)
            if note_id not in allowed_by_sarga[entry["sarga"]]:
                errors.append(f"sarga {entry['sarga']}: unknown/stale/non-votable id {note_id}")
                continue
            if not isinstance(decision, dict) or decision.get("action") not in ACTIONS:
                errors.append(f"{note_id}: invalid action")
                continue
            if decision["action"] == "edit" and not str(decision.get("edited_note", "")).strip():
                errors.append(f"{note_id}: edit requires edited_note")
            if decision["action"] == "reject" and not str(decision.get("reject_reason", "")).strip():
                errors.append(f"{note_id}: reject requires reject_reason")
            expected = allowed_by_sarga[entry["sarga"]]
            if decision.get("verse_id") not in (None, expected[note_id].get("verse_id")):
                errors.append(f"{note_id}: verse_id mismatch")
    supplied = doc.get("content_hash", "")
    unsigned = dict(doc)
    unsigned.pop("content_hash", None)
    actual = hashlib.sha256(canonical(unsigned)).hexdigest()
    if supplied != actual:
        errors.append("content_hash mismatch")
    if len(canonical(doc)) > 2_000_000:
        errors.append("submission exceeds 2 MB")
    return errors


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("submission", type=Path)
    args = ap.parse_args()
    try:
        doc = json.loads(args.submission.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"FAIL: {exc}")
        return 1
    failures = validate(doc)
    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1
    decisions = sum(len(row["decisions"]) for row in doc["sargas"])
    print(f"PASS: immutable submission; reviewer=Костина; sargas=68; decisions={decisions}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

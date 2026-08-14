#!/usr/bin/env python3
"""Shared reader/writer for the tier-2 assembly gate ledger (schema v2).

Ruling R1 gives the final book assembly TWO gatekeepers — Leonov *and* Kostina.
Schema v1 could not express that: it kept exactly one record per apparatus note
id, with `reviewer` as a FIELD inside it, so the second reviewer's verdict
overwrote the first's (`entries.update(...)` even counted the replacements).
Two consequences, both fatal to a two-editor gate:

  * whoever voted second silently erased the first reviewer's verdict;
  * inter-reviewer agreement (Cohen's κ, as measured for the translator axes in
    scripts/compute_iaa_kappa.py) was not computable, because only one of the
    two verdicts ever survived on disk.

Schema v2 keeps the note-level identity at the entry level and nests one record
per reviewer under `verdicts`:

    entries["lexical:5.1.1:0"] = {
        "layer": "lexical", "verse_id": "5.1.1", "lemma_iast": "cāraṇa",
        "verdicts": {
            "Леонов":  {"action": "accept", "gated_date": "2026-07-11", "ts": ...},
            "Костина": {"action": "reject", "reject_reason": "…", ...},
        }}

Nothing is resolved here. When two reviewers disagree the entry carries BOTH
verdicts and `conflict()` reports True; picking a winner (and whose `edited_note`
reaches the print master) is an editorial act for a human, not a merge rule.

v1 ledgers are upgraded in memory on read and persisted as v2 on the next write,
so the 126 Leonov verdicts from 2026-07-11 survive verbatim.
"""
from __future__ import annotations

import json
import os

SCHEMA = 2

DESCRIPTION = (
    "Human final-assembly gate overlay for the per-sarga apparatus (ruling R1: "
    "Leonov AND Kostina gate the assembly). Keyed by apparatus note id "
    "{layer}:{verse_id}:{idx}; one verdict per reviewer under `verdicts`. "
    "Consumed by build_sarga_apparatus.py and gate_reviewer_agreement.py."
)

# Note-level (reviewer-independent) keys that live on the entry itself.
NOTE_KEYS = ("layer", "verse_id", "lemma_iast")
# Per-reviewer keys that live inside verdicts[<reviewer>].
VERDICT_KEYS = ("action", "gated_date", "ts", "edited_note", "reject_reason")


def default_ledger() -> dict:
    return {"_meta": {"description": DESCRIPTION,
                      "schema": SCHEMA,
                      "generated_by": "scripts/apply_apparatus_decisions.py"},
            "entries": {}}


def _upgrade_entry(rec: dict) -> dict:
    """v1 flat record -> v2 {note keys..., verdicts: {reviewer: {...}}}."""
    if "verdicts" in rec:
        return rec
    reviewer = rec.get("reviewer") or "(unknown)"
    verdict = {k: rec[k] for k in VERDICT_KEYS if rec.get(k)}
    out = {k: rec.get(k, "") for k in NOTE_KEYS}
    out["verdicts"] = {reviewer: verdict}
    return out


def load(path: str) -> dict:
    """Read a ledger, upgrading v1 -> v2 in memory. Missing file -> empty v2."""
    if not os.path.exists(path):
        return default_ledger()
    with open(path, encoding="utf-8") as fh:
        doc = json.load(fh)
    doc.setdefault("_meta", {}).setdefault("generated_by",
                                           "scripts/apply_apparatus_decisions.py")
    entries = doc.get("entries") or {}
    upgraded = {i: _upgrade_entry(r) for i, r in entries.items()}
    was = doc["_meta"].get("schema", 1)
    doc["_meta"]["schema"] = SCHEMA
    doc["_meta"]["description"] = DESCRIPTION
    if was != SCHEMA:
        doc["_meta"]["upgraded_from_schema"] = was
    doc["entries"] = upgraded
    return doc


def save(path: str, doc: dict, dry: bool = False) -> None:
    if dry:
        return
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(doc, fh, ensure_ascii=False, indent=2)


def record(ledger: dict, note_id: str, reviewer: str,
           note_fields: dict, verdict: dict) -> bool:
    """Write one reviewer's verdict. Returns True if it replaced their own prior
    verdict on this id (re-voting is legitimate; erasing a COLLEAGUE's is not,
    and cannot happen — verdicts are keyed by reviewer)."""
    entry = ledger["entries"].setdefault(note_id, {})
    for k in NOTE_KEYS:
        if note_fields.get(k) and not entry.get(k):
            entry[k] = note_fields[k]
    verdicts = entry.setdefault("verdicts", {})
    replaced = reviewer in verdicts
    verdicts[reviewer] = {k: v for k, v in verdict.items() if v not in ("", None)}
    return replaced


def verdicts(ledger: dict, note_id: str) -> dict:
    return (ledger.get("entries", {}).get(note_id, {}) or {}).get("verdicts", {}) or {}


def reviewers(ledger: dict) -> list[str]:
    seen: set[str] = set()
    for e in ledger.get("entries", {}).values():
        seen.update((e.get("verdicts") or {}).keys())
    return sorted(seen)


def conflict(vs: dict) -> bool:
    """True when actions differ or two edits propose different text."""
    signatures = {
        (v.get("action"), v.get("edited_note", "") if v.get("action") == "edit" else "")
        for v in vs.values()
    }
    return len(signatures) > 1


def derived_outcome(vs: dict) -> str:
    """Conservative, non-destructive outcome for two-reviewer evidence."""
    actions = [v.get("action") for v in vs.values() if v.get("action")]
    if len(actions) < 2:
        return "pending"
    if any(action == "reject" for action in actions):
        return "exclude" if len(set(actions)) == 1 else "editorial_queue"
    if conflict(vs):
        return "editorial_queue"
    if set(actions) == {"accept"}:
        return "eligible"
    if set(actions) == {"edit"}:
        return "eligible_edited"
    return "editorial_queue"

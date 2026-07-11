#!/usr/bin/env python3
"""Apply a reviewer's per-sarga *apparatus* gate decisions (final-assembly gate).

Companion to apply_phase2_decisions.py, but for the OTHER decisions.json format:
the one exported by the per-sarga apparatus (scripts/build_sarga_apparatus.py,
«Скачать decisions.json»). That file keys votes by the apparatus note id
`{layer}:{verse_id}:{idx}` and covers every votable layer at once
(lexical / edition / phase2 / crosstext), whereas apply_phase2_decisions.py
consumes the `reviewer_decisions`/`verse_id` format of a single Phase-2 batch.

Ruling R1: M.G. gates the Phase-2 pilot; **Leonov/Kostina gate the final book
assembly** — and the per-sarga apparatus IS that final-assembly surface. This
script records their accept/edit/reject verdicts into a single book-wide
overlay ledger:

    data/apparatus/gate_ledger.json
        { "_meta": {...},
          "entries": { "<layer>:<verse_id>:<idx>": {
              "action": "accept|edit|reject", "layer": ..., "verse_id": ...,
              "lemma_iast": ..., "reviewer": "Леонов", "gated_date": "YYYY-MM-DD",
              "edited_note": "<only when the reviewer changed the text>",
              "reject_reason": "<only on reject>", "ts": "<vote timestamp>" } } }

The ledger is an **overlay**, not a mutation of the shared source data files
(data/lexical/ch{N}.json, data/edition_footnotes/, data/crosstext/*.json), which
are keyed differently and span many sargas. build_sarga_apparatus.py reads this
ledger and reflects each gated note's status (accept → «принято <reviewer>»,
edit → gated text, reject → dropped) — so the ledger is the single source of
truth for the human gate and no underlying record is overwritten.

Every decided id is validated against the CURRENT apparatus (data/apparatus/
sarga_{NN}.json) — a vote on an id the generator no longer emits is a hard error
(the source data drifted; rebuild + re-vote). Votable notes left undecided stay
review_required (a WARN lists them).

Usage:
  python scripts/apply_apparatus_decisions.py votes/decisions_sarga_1.json \
      --reviewer Леонов [--dry-run]

After a real (non-dry) apply, rebuild the downstream artifacts so the gate shows:
  python scripts/build_sarga_apparatus.py
"""
import sys
import os
import json
import argparse
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
DATA = os.path.join(REPO, "data")
APPARATUS = os.path.join(DATA, "apparatus")
LEDGER = os.path.join(APPARATUS, "gate_ledger.json")

VALID_ACTIONS = {"accept", "edit", "reject"}


def load(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def dump(path, obj, dry):
    if dry:
        return
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(obj, fh, ensure_ascii=False, indent=2)


def apparatus_notes(sarga):
    """id -> note dict for the current sarga apparatus build."""
    path = os.path.join(APPARATUS, f"sarga_{sarga:02d}.json")
    if not os.path.exists(path):
        sys.exit(f"ERROR: no apparatus build at {path} — run "
                 f"build_sarga_apparatus.py first")
    doc = load(path)
    notes = {}
    for verse in doc.get("verses", []):
        for n in verse.get("notes", []):
            notes[n["id"]] = n
    return notes


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("decisions")
    ap.add_argument("--reviewer", required=True,
                    help="who cast these votes, e.g. Леонов / Костина")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    dry = args.dry_run

    doc = load(args.decisions)
    sarga = doc.get("sarga")
    if not isinstance(sarga, int):
        sys.exit("ERROR: decisions file has no integer 'sarga' field")
    decisions = doc.get("decisions") or {}
    if not decisions:
        sys.exit("ERROR: decisions file carries no 'decisions'")

    # gated_date = the latest vote timestamp (ISO date prefix), fallback none
    ts_all = [v.get("ts", "") for v in decisions.values() if v.get("ts")]
    gated_date = max(ts_all)[:10] if ts_all else ""

    notes = apparatus_notes(sarga)
    votable = {i for i, n in notes.items() if n.get("votable")}

    unknown = sorted(set(decisions) - set(notes))
    if unknown:
        sys.exit(f"ERROR: {len(unknown)} decided ids absent from the current "
                 f"apparatus (source drifted — rebuild + re-vote): {unknown[:10]}")
    non_votable = sorted(set(decisions) & (set(notes) - votable))
    if non_votable:
        sys.exit(f"ERROR: decisions on non-votable (tier-1) notes: {non_votable}")
    undecided = sorted(votable - set(decisions))
    if undecided:
        sys.stderr.write(f"WARN: {len(undecided)} votable note(s) left undecided "
                         f"(stay review_required): {undecided}\n")

    bad = sorted(i for i, d in decisions.items()
                 if d.get("action") not in VALID_ACTIONS)
    if bad:
        sys.exit(f"ERROR: unknown action on ids: {bad[:10]}")

    # ---- build the overlay entries for this sarga+reviewer ----
    new_entries = {}
    silent_edits, rejects = [], []
    for i, d in decisions.items():
        note = notes[i]
        action = d["action"]
        src_text = (note.get("note_ru") or "").strip()
        ed_text = (d.get("edited_note") or "").strip()
        rec = {
            "action": action,
            "layer": note.get("layer"),
            "verse_id": d.get("verse_id"),
            "lemma_iast": d.get("lemma_iast") or note.get("lemma_iast", ""),
            "reviewer": args.reviewer,
            "gated_date": gated_date,
            "ts": d.get("ts", ""),
        }
        if action in ("accept", "edit") and ed_text and ed_text != src_text:
            rec["edited_note"] = ed_text
            silent_edits.append(i)
        if action == "reject":
            rec["reject_reason"] = d.get("reject_reason", "")
            rejects.append(i)
        new_entries[i] = rec

    # ---- merge into the book-wide ledger (idempotent per id) ----
    if os.path.exists(LEDGER):
        ledger = load(LEDGER)
    else:
        ledger = {"_meta": {
            "description": "Human final-assembly gate overlay for the per-sarga "
                           "apparatus (ruling R1: Leonov/Kostina gate the assembly). "
                           "Consumed by build_sarga_apparatus.py; keyed by apparatus "
                           "note id {layer}:{verse_id}:{idx}.",
            "generated_by": "scripts/apply_apparatus_decisions.py",
        }, "entries": {}}
    ledger.setdefault("entries", {})
    replaced = sum(1 for i in new_entries if i in ledger["entries"])
    ledger["entries"].update(new_entries)
    ledger["_meta"]["last_applied"] = {
        "sarga": sarga, "reviewer": args.reviewer, "gated_date": gated_date,
        "decisions_file": os.path.relpath(args.decisions, REPO).replace("\\", "/"),
    }

    acts = Counter(d["action"] for d in decisions.values())
    print(f"sarga {sarga} · reviewer {args.reviewer} · gated {gated_date}"
          + (" [DRY RUN]" if dry else ""))
    print(f"  apparatus votable notes: {len(votable)} · decided: {len(decisions)}"
          f" · undecided: {len(undecided)}")
    print(f"  actions: {dict(acts)}")
    print(f"  reviewer edits (text changed): {len(silent_edits)} {silent_edits[:5]}")
    print(f"  rejects: {len(rejects)} {rejects[:5]}")
    print(f"  ledger entries: +{len(new_entries) - replaced} new, "
          f"{replaced} replaced -> {os.path.relpath(LEDGER, REPO)}")

    dump(LEDGER, ledger, dry)
    if not dry:
        print(f"REBUILD NOW: python scripts/build_sarga_apparatus.py {sarga}")


if __name__ == "__main__":
    main()

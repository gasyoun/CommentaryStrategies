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

    data/apparatus/gate_ledger.json   (schema v2 — see scripts/gate_ledger.py)
        { "_meta": {...},
          "entries": { "<layer>:<verse_id>:<idx>": {
              "layer": ..., "verse_id": ..., "lemma_iast": ...,
              "verdicts": { "Леонов": {
                  "action": "accept|edit|reject", "gated_date": "YYYY-MM-DD",
                  "edited_note": "<only when the reviewer changed the text>",
                  "reject_reason": "<only on reject>", "ts": "<vote timestamp>" },
                "Костина": { ... } } } } }

**Both reviewers are recorded side by side** (schema v2, H2574). Under the old
flat schema a note held ONE verdict with `reviewer` as a field, so the second
reviewer to vote silently overwrote the first — and κ between the two gatekeepers
was not computable because only one verdict survived on disk. Re-voting replaces
only that reviewer's OWN prior verdict; a colleague's is never touched.

Disagreements are NOT resolved here: the entry keeps both verdicts, the run
prints a conflict table, and `--require-agreement` makes conflicts a hard error
for callers that want the gate to stop. Choosing a winner is an editorial act.

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
      --reviewer Леонов [--dry-run] [--require-agreement]

This command is the explicit legacy single-sarga path. Complete authenticated
68-sarga submissions must go through `validate_apparatus_submission.py` and
`import_apparatus_submission.py`; do not split an aggregate into 68 invocations
or trust reviewer identity from a CLI flag.

After a real (non-dry) apply, rebuild the downstream artifacts so the gate shows:
  python scripts/build_sarga_apparatus.py
"""
import sys
import os
import json
import argparse
from collections import Counter

import gate_ledger

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
    """id -> note dict for the current sarga apparatus build.

    `votable` is read as the note's INTRINSIC eligibility (layer != tier1), not
    as the built sheet's live control state. build_sarga_apparatus.py sets
    votable=False on any note the ledger already carries, so trusting that flag
    here made the SECOND reviewer's whole ballot fail validation as "decisions on
    non-votable (tier-1) notes" — 126 of 127 sarga-1 cards, none of them tier-1
    (H2574). Tier-1 remains genuinely unvotable: it is printed Leonov/Kostina
    text, not a proposal.
    """
    path = os.path.join(APPARATUS, f"sarga_{sarga:02d}.json")
    if not os.path.exists(path):
        sys.exit(f"ERROR: no apparatus build at {path} — run "
                 f"build_sarga_apparatus.py first")
    doc = load(path)
    notes = {}
    for verse in doc.get("verses", []):
        for n in verse.get("notes", []):
            n["votable"] = n.get("layer") != "tier1"
            notes[n["id"]] = n
    return notes


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("decisions")
    ap.add_argument("--reviewer", required=True,
                    help="who cast these votes, e.g. Леонов / Костина")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--require-agreement", action="store_true",
                    help="hard-fail if the reviewers disagree on any decided "
                         "note (default: record both verdicts and report)")
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
        sys.exit(f"ERROR: decisions on tier-1 (printed, non-votable) notes: "
                 f"{non_votable}")
    undecided = sorted(votable - set(decisions))
    if undecided:
        sys.stderr.write(f"WARN: {len(undecided)} votable note(s) left undecided "
                         f"(stay review_required): {undecided}\n")

    bad = sorted(i for i, d in decisions.items()
                 if d.get("action") not in VALID_ACTIONS)
    if bad:
        sys.exit(f"ERROR: unknown action on ids: {bad[:10]}")

    # ---- merge this reviewer's verdicts into the book-wide ledger ----
    # Schema v2: one record per (note id, reviewer). A colleague's verdict on the
    # same id is never touched; only this reviewer's own prior vote can be
    # replaced (legitimate re-voting after a rebuild).
    ledger = gate_ledger.load(LEDGER)
    silent_edits, rejects, own_revotes = [], [], []
    for i, d in sorted(decisions.items()):
        note = notes[i]
        action = d["action"]
        src_text = (note.get("note_ru") or "").strip()
        ed_text = (d.get("edited_note") or "").strip()
        verdict = {"action": action,
                   "gated_date": gated_date,
                   "ts": d.get("ts", "")}
        if action in ("accept", "edit") and ed_text and ed_text != src_text:
            verdict["edited_note"] = ed_text
            silent_edits.append(i)
        if action == "reject":
            verdict["reject_reason"] = d.get("reject_reason", "")
            rejects.append(i)
        note_fields = {"layer": note.get("layer"),
                       "verse_id": d.get("verse_id") or i.split(":")[1],
                       "lemma_iast": d.get("lemma_iast") or note.get("lemma_iast", "")}
        if gate_ledger.record(ledger, i, args.reviewer, note_fields, verdict):
            own_revotes.append(i)

    ledger["_meta"]["last_applied"] = {
        "sarga": sarga, "reviewer": args.reviewer, "gated_date": gated_date,
        "decisions_file": os.path.relpath(args.decisions, REPO).replace("\\", "/"),
    }

    # ---- inter-reviewer disagreement (reported, never auto-resolved) ----
    conflicts = []
    for i in sorted(decisions):
        vs = gate_ledger.verdicts(ledger, i)
        if len(vs) > 1 and gate_ledger.conflict(vs):
            conflicts.append((i, {r: v.get("action") for r, v in vs.items()}))

    acts = Counter(d["action"] for d in decisions.values())
    all_reviewers = gate_ledger.reviewers(ledger)
    print(f"sarga {sarga} · reviewer {args.reviewer} · gated {gated_date}"
          + (" [DRY RUN]" if dry else ""))
    print(f"  apparatus votable notes: {len(votable)} · decided: {len(decisions)}"
          f" · undecided: {len(undecided)}")
    print(f"  actions: {dict(acts)}")
    print(f"  reviewer edits (text changed): {len(silent_edits)} {silent_edits[:5]}")
    print(f"  rejects: {len(rejects)} {rejects[:5]}")
    print(f"  own re-votes replaced: {len(own_revotes)} {own_revotes[:5]}")
    print(f"  ledger reviewers now: {all_reviewers}")
    print(f"  ledger entries: {len(ledger['entries'])} "
          f"-> {os.path.relpath(LEDGER, REPO)}")

    if conflicts:
        print(f"  DISAGREEMENTS ({len(conflicts)}) — kept side by side, "
              f"NOT auto-resolved; a human picks the winner:")
        for i, per in conflicts[:20]:
            print(f"    {i}: " + " · ".join(f"{r}={a}" for r, a in sorted(per.items())))
        if len(conflicts) > 20:
            print(f"    … +{len(conflicts) - 20} more")
        if args.require_agreement:
            sys.exit(f"ERROR: --require-agreement and {len(conflicts)} "
                     f"disagreement(s) — resolve them before applying")

    gate_ledger.save(LEDGER, ledger, dry)
    if not dry:
        print(f"REBUILD NOW: python scripts/build_sarga_apparatus.py {sarga}")
        if len(all_reviewers) > 1:
            print("AGREEMENT:  python scripts/gate_reviewer_agreement.py")


if __name__ == "__main__":
    main()

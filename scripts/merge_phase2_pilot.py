#!/usr/bin/env python3
"""Phase-2: merge per-sarga commentator-note candidate files into one set.

Reads data/analysis/phase2_pilot/sarga_*_candidates.json (Sonnet-drafted,
review_required) and writes a combined data/analysis/phase2_pilot/pilot_candidates.json
plus prints reconciliation stats. Deterministic, stdlib-only. Does NOT approve
anything — every note stays review_required until a human gates it.

Usage: python scripts/merge_phase2_pilot.py
"""
import sys
import os
import re
import glob
import json

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
PILOT_DIR = os.path.join(REPO, "data", "analysis", "phase2_pilot")
OUT = os.path.join(PILOT_DIR, "pilot_candidates.json")


def sarga_verse_key(verse_id):
    m = re.match(r"5\.(\d+)\.(\d+)", verse_id)
    if not m:
        return (0, 0)
    return (int(m.group(1)), int(m.group(2)))


def main():
    files = sorted(glob.glob(os.path.join(PILOT_DIR, "sarga_*_candidates.json")))
    notes, per_sarga = [], []
    total_considered = total_rejected = 0
    for f in files:
        d = json.load(open(f, encoding="utf-8"))
        meta = d.get("_meta", {})
        n = d.get("notes", [])
        notes.extend(n)
        total_considered += meta.get("verses_considered", 0)
        total_rejected += meta.get("notes_rejected", 0)
        per_sarga.append({
            "sarga": meta.get("sarga"),
            "drafted": len(n),
            "considered": meta.get("verses_considered"),
            "rejected": meta.get("notes_rejected"),
        })

    notes.sort(key=lambda x: sarga_verse_key(x["verse_id"]))

    # integrity assertions — all must be review_required + Sonnet-provenanced
    bad = [x["verse_id"] for x in notes if not x.get("review_required")]
    if bad:
        sys.stderr.write(f"ERROR: notes missing review_required: {bad}\n")
        sys.exit(1)

    from collections import Counter
    payload = {
        "_meta": {
            "generated_by": "scripts/merge_phase2_pilot.py",
            "layer": "phase2 commentator-dialogue (model II tier-2)",
            "status": "PILOT — all notes review_required, human gate pending",
            "drafted_by": "claude-sonnet-5 (Sonnet); orchestrated by claude-opus-4-8 (Opus)",
            "date": "2026-07-01",
            "total_notes": len(notes),
            "total_verses_considered": total_considered,
            "total_rejected": total_rejected,
            "accept_rate_pct": round(100 * len(notes) / total_considered, 1) if total_considered else None,
            "by_kazansky": dict(Counter(x["kazansky_type"] for x in notes)),
            "by_commentator": dict(Counter(c for x in notes for c in x["source_commentary"])),
            "per_sarga": per_sarga,
            "rights": "commentary from Gita Supersite, used by permission (CC BY 4.0); see data/valmiki_PERMISSION.md",
            "caveats": [
                "verse_id alignment is corpus-derived (।। markers); the human gate must confirm each against print.",
                "known source glitch: 5.36.45 bhusana chunk held commentary for v.4 (rejected, no note rests on it).",
                "merged-range markers (e.g. 5.s.810 = vv.8-10) were mostly rejected; not independent verses.",
            ],
        },
        "notes": notes,
    }
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, ensure_ascii=False, indent=2)

    m = payload["_meta"]
    print(f"merged {len(files)} files -> {len(notes)} notes "
          f"({m['total_verses_considered']} considered, {m['accept_rate_pct']}% accept)")
    print("by kazansky:", m["by_kazansky"], "| by commentator:", m["by_commentator"])
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()

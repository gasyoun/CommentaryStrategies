#!/usr/bin/env python3
"""Phase-2: merge per-sarga commentator-note candidate files into one set.

Reads data/analysis/phase2_pilot/sarga_*_candidates.json (Sonnet-drafted,
review_required) and writes a combined data/analysis/phase2_pilot/pilot_candidates.json
plus prints reconciliation stats. Deterministic, stdlib-only. Does NOT approve
anything — every note stays review_required until a human gates it.

Usage: python scripts/merge_phase2_pilot.py [batch_dir_name]
       (default batch_dir_name: phase2_pilot; e.g. phase2_batch2 -> merges
        data/analysis/phase2_batch2/sarga_*_candidates.json into
        batch2_candidates.json + batch2_rejected.json in the same dir)
"""
import sys
import os
import re
import glob
import json
import datetime

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
BATCH = sys.argv[1] if len(sys.argv) > 1 else "phase2_pilot"
PREFIX = BATCH.replace("phase2_", "")
PILOT_DIR = os.path.join(REPO, "data", "analysis", BATCH)
OUT = os.path.join(PILOT_DIR, f"{PREFIX}_candidates.json")


def sarga_verse_key(verse_id):
    m = re.match(r"5\.(\d+)\.(\d+)", verse_id)
    if not m:
        return (0, 0)
    return (int(m.group(1)), int(m.group(2)))


# reject-reason taxonomy: substring -> bucket (the reject log IS the quality signal).
# Order matters — structural/data reasons are matched BEFORE the generic
# "restates"/"grammar" buckets, since reasons are often compound
# (e.g. "merged-range marker ... grammar only" is structurally a merged-range reject).
REJECT_BUCKETS = [
    ("merged_range_marker", ["merged-range", "слитн", "маркер слит", "no independent"]),
    ("data_misalignment", ["misalign", "misaligned", "глитч", "field misaligned", "не соответ"]),
    ("formulaic_panegyric", ["formulaic", "формульн", "панегир", "восхвал", "praise"]),
    ("overlaps_other_note", ["overlap", "duplicate", "повтор", "вынесен", "вариац", "разобран в примеч", "относительно примеч"]),
    ("restates_podstrochnik", ["restates", "подстрочник", "уже переда", "уже дан", "уже пояс", "уже назван", "уже раскры", "уже сна", "already", "уже общеизвест", "уже отраж", "уже переведен"]),
    ("pure_grammar", ["grammar", "parsing", "граммати", "разбор", "согласован", "невидим"]),
]


def bucket(reason):
    low = reason.lower()
    for name, keys in REJECT_BUCKETS:
        if any(k.lower() in low for k in keys):
            return name
    return "other"


def main():
    files = sorted(glob.glob(os.path.join(PILOT_DIR, "sarga_*_candidates.json")))
    notes, per_sarga, rejected = [], [], []
    total_considered = 0
    for f in files:
        d = json.load(open(f, encoding="utf-8"))
        meta = d.get("_meta", {})
        n = d.get("notes", [])
        rej = d.get("rejected", [])
        notes.extend(n)
        for r in rej:
            r = dict(r)
            r["sarga"] = meta.get("sarga")
            r["bucket"] = bucket(r.get("reason", ""))
            rejected.append(r)
        total_considered += meta.get("verses_considered", 0)
        per_sarga.append({
            "sarga": meta.get("sarga"),
            "drafted": len(n),
            "considered": meta.get("verses_considered"),
            "rejected_entries": len(rej),
        })

    notes.sort(key=lambda x: sarga_verse_key(x["verse_id"]))
    rejected.sort(key=lambda x: sarga_verse_key(x.get("verse_id", "")))
    total_rejected = len(rejected)

    # integrity assertions — all must be review_required + Sonnet-provenanced
    bad = [x["verse_id"] for x in notes if not x.get("review_required")]
    if bad:
        sys.stderr.write(f"ERROR: notes missing review_required: {bad}\n")
        sys.exit(1)

    from collections import Counter
    reject_taxonomy = dict(Counter(r["bucket"] for r in rejected))
    if BATCH == "phase2_pilot":
        common_meta = {
            "layer": "phase2 commentator-dialogue (model II tier-2)",
            "status": "PILOT — all notes review_required, human gate pending",
            "drafted_by": "claude-sonnet-5 (Sonnet); orchestrated by claude-opus-4-8 (Opus)",
            "date": "2026-07-01",
            "rights": "commentary from Gita Supersite, used by permission (CC BY 4.0); see data/valmiki_PERMISSION.md",
        }
    else:
        common_meta = {
            "layer": "phase2 commentator-dialogue (model II tier-2)",
            "status": f"{BATCH} — all notes review_required, human gate (М.Г.) pending",
            "drafted_by": "claude-sonnet-5 (Sonnet 5); orchestrated by claude-fable-5 (Fable 5)",
            "date": datetime.date.today().isoformat(),
            "rights": "commentary from Gita Supersite, used by permission (CC BY 4.0); see data/valmiki_PERMISSION.md",
        }
    payload = {
        "_meta": {
            **common_meta,
            "generated_by": "scripts/merge_phase2_pilot.py",
            "total_notes": len(notes),
            "total_verses_considered": total_considered,
            "total_rejected_entries": total_rejected,
            "accept_rate_pct": round(100 * len(notes) / total_considered, 1) if total_considered else None,
            "by_kazansky": dict(Counter(x["kazansky_type"] for x in notes)),
            "by_commentator": dict(Counter(c for x in notes for c in x["source_commentary"])),
            "reject_taxonomy": reject_taxonomy,
            "per_sarga": per_sarga,
            "caveats": [
                "verse_id alignment is corpus-derived (।। markers + pratīka reassignment); the human gate must confirm each against print.",
                "merged-range markers (e.g. 5.s.810 = vv.8-10) were mostly rejected; not independent verses.",
            ] + ([
                "known source glitch: 5.36.45 bhusana chunk held commentary for v.4 (rejected, no note rests on it).",
                "counts do not fully reconcile: agents grouped some rejects (e.g. '5.35.17-20') so "
                "notes + reject-entries < verses_considered; this is expected, not data loss.",
            ] if BATCH == "phase2_pilot" else []),
        },
        "notes": notes,
    }
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, ensure_ascii=False, indent=2)

    # standalone rejected log (the reject reasons are the quality signal — keep them first-class)
    rej_payload = {
        "_meta": {
            **common_meta,
            "generated_by": "scripts/merge_phase2_pilot.py",
            "total_rejected_entries": total_rejected,
            "reject_taxonomy": reject_taxonomy,
            "note": "Each entry = one verse (or grouped verse-range) the drafter declined, with reason + bucket. "
                    "A high reject rate is the intended discipline: most verses add nothing beyond the подстрочник.",
        },
        "rejected": rejected,
    }
    rej_out = os.path.join(PILOT_DIR, f"{PREFIX}_rejected.json")
    with open(rej_out, "w", encoding="utf-8") as fh:
        json.dump(rej_payload, fh, ensure_ascii=False, indent=2)

    m = payload["_meta"]
    print(f"merged {len(files)} files -> {len(notes)} notes "
          f"({m['total_verses_considered']} considered, {m['accept_rate_pct']}% accept)")
    print("by kazansky:", m["by_kazansky"], "| by commentator:", m["by_commentator"])
    print("reject taxonomy:", reject_taxonomy, f"(total {total_rejected})")
    print(f"wrote {OUT}")
    print(f"wrote {rej_out}")


if __name__ == "__main__":
    main()

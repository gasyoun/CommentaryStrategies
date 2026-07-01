#!/usr/bin/env python3
"""Answer Kostina/Leonov memo lines 34 & 56: which traditional commentators does
Leonov follow most, and how large is the "в Тилаке X / в Широмани Y" contrastive
layer (vs Grintser's ~8%)?

Reads data/leonov_own_notes.json (1058 digitized notes) and counts, per named
commentator, how many notes cite it; the union share (any commentator); and the
contrastive share (>=2 distinct commentators in one note = the Leonov signature).
Deterministic, stdlib-only.

Usage: python scripts/leonov_commentator_stats.py
Output: data/analysis/leonov_commentator_stats.json (+ printed table)
"""
import sys
import os
import json

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
SRC = os.path.join(REPO, "data", "leonov_own_notes.json")
OUT = os.path.join(REPO, "data", "analysis", "leonov_commentator_stats.json")

# commentator -> case-insensitive stems (Russian oblique forms + Latin/IAST)
COMMENTATORS = {
    "Тилака (Tilaka)":        ["тилак", "tilaka"],
    "Бхушана (Bhūṣaṇa)":      ["бхушан", "bhusana", "bhūṣaṇa", "bhūṣaṇa"],
    "Широмани (Śiromaṇi)":    ["широмани", "siromani", "śiroma", "śiroma"],
    "Таттвадипика (Tattvadīpikā)": ["таттвадипик", "tattvadipik", "tattvadīpik"],
    "Катака (Kataka)":        ["катак", "kataka"],
    "Говиндараджа (Govindarāja)": ["говиндарадж", "govindar"],
    "Дхармакутам (Dharmākūṭam)": ["дхармакут", "dharmakut", "dharmāk"],
    "Махешваратиртха (Maheśvaratīrtha)": ["махешвара", "mahesvara", "maheśvara"],
}


def main():
    data = json.load(open(SRC, encoding="utf-8"))
    notes = data["notes"]
    total = len(notes)

    per = {k: 0 for k in COMMENTATORS}
    any_count = 0
    contrastive = 0          # >=2 distinct commentators in one note
    contrastive_examples = []
    per_sarga_contrastive = {}

    for n in notes:
        t = n.get("raw_text", "").lower()
        hits = [name for name, stems in COMMENTATORS.items() if any(s in t for s in stems)]
        for name in hits:
            per[name] += 1
        if hits:
            any_count += 1
        if len(set(hits)) >= 2:
            contrastive += 1
            s = n.get("sarga")
            per_sarga_contrastive[s] = per_sarga_contrastive.get(s, 0) + 1
            if len(contrastive_examples) < 8:
                contrastive_examples.append({
                    "verse_id": n.get("verse_id"),
                    "commentators": hits,
                    "excerpt": n.get("raw_text", "")[:180],
                })

    pct = lambda x: round(100 * x / total, 1) if total else 0
    ranked = sorted(per.items(), key=lambda kv: -kv[1])

    payload = {
        "_meta": {
            "generated_by": "scripts/leonov_commentator_stats.py",
            "source": "data/leonov_own_notes.json",
            "total_notes": total,
            "answers": "Kostina/Leonov memo lines 34 (which commentators most) & 56 (contrastive share vs Grintser ~8%)",
        },
        "notes_citing_any_commentator": {"count": any_count, "pct": pct(any_count)},
        "contrastive_layer": {
            "definition": ">=2 distinct named commentators contrasted in one note (the «в Тилаке X / в Широмани Y» signature)",
            "count": contrastive, "pct": pct(contrastive),
            "grintser_reference_pct": 8,
            "per_sarga_top": dict(sorted(per_sarga_contrastive.items(), key=lambda kv: -kv[1])[:10]),
            "examples": contrastive_examples,
        },
        "by_commentator": [{"commentator": k, "notes": v, "pct": pct(v)} for k, v in ranked],
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, ensure_ascii=False, indent=2)

    print(f"total notes: {total}")
    print(f"cite any commentator: {any_count} ({pct(any_count)}%)")
    print(f"contrastive (>=2 commentators): {contrastive} ({pct(contrastive)}%) vs Grintser ~8%")
    print("by commentator:")
    for k, v in ranked:
        print(f"  {k:34s} {v:4d} ({pct(v)}%)")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""H268 WS-A: merged apparatus density per sarga vs the Leonov ~37% ЛП target.

Measures, for every sarga of the southern vulgate Sundarakāṇḍa:
  - canonical verse count (SamudraManthanam corpus, seg 'sa');
  - tier-1 coverage (Leonov's own notes; Kostina's editorial-control marks are
    counted SEPARATELY — WS-E: they are not reader footnotes);
  - tier-2 coverage by subtype (base / lexical / cross_text / hist_cultural /
    commentator), all still review_required;
  - merged reader-apparatus density (tier-1 Leonov ∪ tier-2) and the verse gap
    to the 37% target;
  - tier-1∩tier-2 overlap (dedup pressure for the assembly gate).

Writes data/analysis/book_density_stats.json and prints a compact table.
Deterministic, stdlib-only.
"""
import sys
import os
import json
import re
from collections import defaultdict

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from sa_align import find_sibling  # noqa: E402

TARGET = 0.37

JSONL = os.path.join(find_sibling("SamudraManthanam") or "",
                     "web", "corpus_builder", "jsonl", "05_ramayana-sundarakanda.jsonl")
T1 = os.path.join(REPO, "data", "leonov_own_notes.json")
T2 = os.path.join(REPO, "data", "sundara_commentary_to_add.json")
OUT = os.path.join(REPO, "data", "analysis", "book_density_stats.json")


def verse_counts():
    counts = defaultdict(set)
    with open(JSONL, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                d = json.loads(line)
            except json.JSONDecodeError:
                continue
            p = d.get("passage", "")
            m = re.match(r"(\d+)\.(\d+)$", p)
            if m and d.get("seg") == "sa":
                counts[int(m.group(1))].add(int(m.group(2)))
    return {s: len(v) for s, v in counts.items()}


def main():
    vc = verse_counts()
    t1 = json.load(open(T1, encoding="utf-8"))["notes"]
    t2 = [n for n in json.load(open(T2, encoding="utf-8")) if "shloka" in n]

    leo = defaultdict(set)    # sarga -> verses with a Leonov note
    kos = defaultdict(set)    # sarga -> verses with a Kostina mark
    for n in t1:
        s, v = int(n["sarga"]), n["verse"]
        if not str(v).isdigit():
            continue
        (kos if n.get("editor") == "kostina" else leo)[s].add(int(v))

    t2v = defaultdict(set)                    # sarga -> verses with any tier-2 note
    t2_by_sub = defaultdict(lambda: defaultdict(set))
    for n in t2:
        m = re.match(r"V\.(\d+)\.(\d+)", n["shloka"])
        if not m:
            continue
        s, v = int(m.group(1)), int(m.group(2))
        t2v[s].add(v)
        t2_by_sub[n.get("subtype", "base")][s].add(v)

    # gate-pending Phase-2 batches (judge keep/edit or not yet judged) — the
    # same inclusion rule as the print master (build_book_apparatus.py).
    import glob
    for bp in sorted(glob.glob(os.path.join(REPO, "data", "analysis",
                                            "phase2_batch*", "batch*_candidates.json"))):
        for n in json.load(open(bp, encoding="utf-8")).get("notes", []):
            if (n.get("judge") or {}).get("verdict") in ("park", "reject", "flag_anchor"):
                continue
            m = re.match(r"5\.(\d+)\.(\d+)$", n.get("verse_id", ""))
            if not m:
                continue
            s, v = int(m.group(1)), int(m.group(2))
            t2v[s].add(v)
            t2_by_sub["commentator_pending"][s].add(v)

    rows = []
    tot = defaultdict(int)
    for s in sorted(vc):
        n_v = vc[s]
        lv, kv, t2s = leo[s], kos[s], t2v[s]
        merged = lv | t2s
        overlap = lv & t2s
        gap = max(0, int(round(TARGET * n_v)) - len(merged))
        rows.append({
            "sarga": s, "verses": n_v,
            "t1_leonov": len(lv), "t1_kostina": len(kv),
            "t2": len(t2s),
            "t2_by_subtype": {k: len(t2_by_sub[k][s]) for k in sorted(t2_by_sub) if t2_by_sub[k][s]},
            "overlap_t1_t2": len(overlap),
            "merged": len(merged),
            "density_t1_leonov": round(len(lv) / n_v, 3),
            "density_merged": round(len(merged) / n_v, 3),
            "gap_to_37pct": gap,
        })
        tot["verses"] += n_v
        tot["t1_leonov"] += len(lv)
        tot["t1_kostina"] += len(kv)
        tot["t2"] += len(t2s)
        tot["overlap"] += len(overlap)
        tot["merged"] += len(merged)
        tot["gap"] += gap

    book = {
        "verses": tot["verses"],
        "t1_leonov_verses": tot["t1_leonov"],
        "t1_kostina_verses": tot["t1_kostina"],
        "t2_verses": tot["t2"],
        "overlap_t1_t2_verses": tot["overlap"],
        "merged_verses": tot["merged"],
        "density_t1_leonov": round(tot["t1_leonov"] / tot["verses"], 3),
        "density_merged": round(tot["merged"] / tot["verses"], 3),
        "target": TARGET,
        "gap_verses_to_target": tot["gap"],
        "note": ("density = fraction of verses carrying ≥1 note; merged = tier-1 Leonov ∪ tier-2 "
                 "(Kostina's editorial-control marks EXCLUDED from the reader apparatus per WS-E; "
                 "reported separately). All tier-2 notes remain review_required — merged density "
                 "is the ceiling the assembly gate can release, not what is approved."),
    }
    payload = {"_meta": {"generated_by": "scripts/book_density_stats.py",
                         "purpose": "H268 WS-A merged-density measurement vs Leonov ~37% ЛП target"},
               "book": book, "sargas": rows}
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, ensure_ascii=False, indent=2)

    print(f"{'sarga':>5} {'vv':>4} {'t1L':>4} {'t1K':>4} {'t2':>4} {'ovl':>4} "
          f"{'merged':>6} {'d_t1':>6} {'d_mrg':>6} {'gap37':>5}")
    for r in rows:
        print(f"{r['sarga']:>5} {r['verses']:>4} {r['t1_leonov']:>4} {r['t1_kostina']:>4} "
              f"{r['t2']:>4} {r['overlap_t1_t2']:>4} {r['merged']:>6} "
              f"{r['density_t1_leonov']:>6.0%} {r['density_merged']:>6.0%} {r['gap_to_37pct']:>5}")
    b = book
    print(f"\nBOOK: {b['verses']} verses | tier-1 Leonov {b['t1_leonov_verses']} "
          f"({b['density_t1_leonov']:.1%}) + Kostina marks {b['t1_kostina_verses']} (separate) | "
          f"tier-2 {b['t2_verses']} | merged {b['merged_verses']} ({b['density_merged']:.1%}) | "
          f"gap to 37%: {b['gap_verses_to_target']} verses")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()

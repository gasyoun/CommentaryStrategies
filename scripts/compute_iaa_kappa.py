"""compute_iaa_kappa.py — Cohen's κ for H1469 axis_2 / axis_4 IAA.

Compares Pass A (human gold: data/{translator}_markup_50.json) to
Pass B (blind LLM: data/{translator}_full.json) for all six translators.

Stdlib only. Bootstrap CI: 2_000 resamples, seed 20260724.

Usage:
    python scripts/compute_iaa_kappa.py
    python scripts/compute_iaa_kappa.py --write   # also write data/iaa/*.json
"""
from __future__ import annotations

import argparse
import json
import random
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
IAA = DATA / "iaa"
TRANSLATORS = ["kalyanov", "vassilkov", "erman", "grintser", "syrkin", "leonov"]
SEED = 20260724
N_BOOT = 2000
AXIS2 = ["A", "B", "V", "G"]
AXIS4 = ["P", "K", "D"]


def cohen_kappa(pairs: list[tuple[str, str]], labels: list[str] | None = None) -> float:
    n = len(pairs)
    if n == 0:
        return float("nan")
    po = sum(1 for a, b in pairs if a == b) / n
    ca = Counter(a for a, _ in pairs)
    cb = Counter(b for _, b in pairs)
    cats = labels if labels is not None else sorted(set(ca) | set(cb))
    pe = sum((ca[c] / n) * (cb[c] / n) for c in cats)
    if pe >= 1.0 - 1e-15:
        return 1.0
    return (po - pe) / (1.0 - pe)


def bootstrap_ci(pairs: list[tuple[str, str]], labels: list[str], seed: int = SEED,
                 n_boot: int = N_BOOT) -> tuple[float, float, float]:
    n = len(pairs)
    point = cohen_kappa(pairs, labels)
    if n == 0:
        return point, float("nan"), float("nan")
    rng = random.Random(seed)
    boots = sorted(
        cohen_kappa([pairs[rng.randrange(n)] for _ in range(n)], labels)
        for _ in range(n_boot)
    )
    lo = boots[int(0.025 * n_boot)]
    hi = boots[min(int(0.975 * n_boot), n_boot - 1)]
    return point, lo, hi


def confusion(pairs: list[tuple[str, str]], labels: list[str]) -> dict:
    mat = {a: {b: 0 for b in labels} for a in labels}
    for a, b in pairs:
        if a not in mat:
            mat[a] = {x: 0 for x in labels}
        if b not in mat[a]:
            mat[a][b] = 0
        mat[a][b] = mat[a].get(b, 0) + 1
    return mat


def load_pairs(translator: str) -> tuple[list[dict], list[tuple], list[tuple]] | None:
    gold_path = DATA / f"{translator}_markup_50.json"
    pred_path = DATA / f"{translator}_full.json"
    if not gold_path.exists() or not pred_path.exists():
        return None
    gold = json.loads(gold_path.read_text(encoding="utf-8"))
    pred = json.loads(pred_path.read_text(encoding="utf-8"))
    n = min(len(gold), len(pred), 50)
    rows = []
    p2, p4 = [], []
    for i in range(n):
        g, p = gold[i], pred[i]
        a2g = g.get("axis_2_kazansky", "?")
        a2p = p.get("axis_2_kazansky", "?")
        a4g = g.get("axis_4_paribok", "P") or "P"
        a4p = p.get("axis_4_paribok", "P") or "P"
        p2.append((a2g, a2p))
        p4.append((a4g, a4p))
        rows.append({
            "translator": translator,
            "idx": i + 1,
            "comment_id_gold": g.get("comment_id"),
            "comment_id_pred": p.get("comment_id"),
            "raw_text": g.get("raw_text", "")[:240],
            "axis_2_gold": a2g,
            "axis_2_pred": a2p,
            "axis_4_gold": a4g,
            "axis_4_pred": a4p,
            "axis_2_agree": a2g == a2p,
            "axis_4_agree": a4g == a4p,
        })
    return rows, p2, p4


def summarize_axis(pairs: list[tuple[str, str]], labels: list[str], name: str) -> dict:
    n = len(pairs)
    agree = sum(1 for a, b in pairs if a == b)
    kappa, lo, hi = bootstrap_ci(pairs, labels)
    return {
        "axis": name,
        "n": n,
        "raw_agreement": round(agree / n, 4) if n else None,
        "raw_agree_count": agree,
        "kappa": round(kappa, 4),
        "kappa_ci95": [round(lo, 4), round(hi, 4)],
        "bootstrap": {"resamples": N_BOOT, "seed": SEED},
        "confusion_gold_rows_pred_cols": confusion(pairs, labels),
        "gold_dist": dict(Counter(a for a, _ in pairs)),
        "pred_dist": dict(Counter(b for _, b in pairs)),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true", help="Write JSON artifacts under data/iaa/")
    args = ap.parse_args()

    all_rows: list[dict] = []
    all_p2: list[tuple[str, str]] = []
    all_p4: list[tuple[str, str]] = []
    per_tr: dict = {}

    print("## H1469 IAA — human gold vs blind LLM (Pass B)\n")
    for tr in TRANSLATORS:
        loaded = load_pairs(tr)
        if loaded is None:
            print(f"  [{tr}] MISSING gold or full — skip")
            continue
        rows, p2, p4 = loaded
        s2 = summarize_axis(p2, AXIS2, "axis_2_kazansky")
        s4 = summarize_axis(p4, AXIS4, "axis_4_paribok")
        per_tr[tr] = {"axis_2": s2, "axis_4": s4, "n": len(rows)}
        all_rows.extend(rows)
        all_p2.extend(p2)
        all_p4.extend(p4)
        print(
            f"  [{tr}] n={len(rows)}  "
            f"axis_2 κ={s2['kappa']:.3f} [{s2['kappa_ci95'][0]:.3f}–{s2['kappa_ci95'][1]:.3f}] "
            f"agr={s2['raw_agreement']:.1%}  |  "
            f"axis_4 κ={s4['kappa']:.3f} [{s4['kappa_ci95'][0]:.3f}–{s4['kappa_ci95'][1]:.3f}] "
            f"agr={s4['raw_agreement']:.1%}"
        )

    if not all_p2:
        print("No pairs loaded.")
        return 1

    overall2 = summarize_axis(all_p2, AXIS2, "axis_2_kazansky")
    overall4 = summarize_axis(all_p4, AXIS4, "axis_4_paribok")
    print("\n## Overall (pooled n={})".format(len(all_p2)))
    print(
        f"  axis_2 κ={overall2['kappa']:.3f} "
        f"[{overall2['kappa_ci95'][0]:.3f}–{overall2['kappa_ci95'][1]:.3f}] "
        f"agr={overall2['raw_agreement']:.1%} ({overall2['raw_agree_count']}/{overall2['n']})"
    )
    print(
        f"  axis_4 κ={overall4['kappa']:.3f} "
        f"[{overall4['kappa_ci95'][0]:.3f}–{overall4['kappa_ci95'][1]:.3f}] "
        f"agr={overall4['raw_agreement']:.1%} ({overall4['raw_agree_count']}/{overall4['n']})"
    )

    disag2 = [r for r in all_rows if not r["axis_2_agree"]]
    disag4 = [r for r in all_rows if not r["axis_4_agree"]]
    print(f"\n  axis_2 disagreements: {len(disag2)}")
    print(f"  axis_4 disagreements: {len(disag4)}")

    out = {
        "study": "H1469 axis_2/axis_4 blind LLM second-annotator IAA",
        "date": "2026-07-24",
        "pass_a": "human gold data/*_markup_50.json",
        "pass_b": "DeepSeek Chat (deepseek-chat) via scripts/annotate_batch.py + prompts/classify_note.md",
        "protocol": "PROTOCOL_BLIND_LLM_SECOND_ANNOTATOR_RELIABILITY_2026.md + ruling D2",
        "bootstrap": {"resamples": N_BOOT, "seed": SEED},
        "overall": {"axis_2": overall2, "axis_4": overall4},
        "per_translator": per_tr,
        "disagreements_axis_2": disag2,
        "disagreements_axis_4": disag4,
    }

    if args.write:
        IAA.mkdir(parents=True, exist_ok=True)
        stats_path = IAA / "iaa_kappa_stats.json"
        stats_path.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n",
                              encoding="utf-8", newline="\n")
        (IAA / "disagreements_axis_2.json").write_text(
            json.dumps(disag2, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8", newline="\n")
        (IAA / "disagreements_axis_4.json").write_text(
            json.dumps(disag4, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8", newline="\n")
        print(f"\nWrote {stats_path.relative_to(ROOT)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

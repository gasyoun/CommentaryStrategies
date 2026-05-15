"""
eval_pipeline.py — compare LLM pipeline output to human-labeled ground truth.

Usage:
    python scripts/eval_pipeline.py kalyanov
    python scripts/eval_pipeline.py --all

Compares:
    data/{translator}_full.json  (LLM output from annotate_batch.py)
    data/{translator}_markup_50.json  (human-labeled gold standard, n=50)

Reports accuracy and confusion matrix for axis_2_kazansky and axis_4_paribok.
These are the two axes that matter most for Article 1 (ВЯ) argument.
"""

import sys, json, pathlib, argparse
from collections import Counter, defaultdict

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

ROOT   = pathlib.Path(__file__).parent.parent
DATA   = ROOT / "data"

TRANSLATORS = ["kalyanov", "vassilkov", "erman", "grintser", "syrkin", "leonov"]


def load(path: pathlib.Path) -> list[dict]:
    return json.loads(path.read_text(encoding="utf-8"))


def confusion_matrix(pairs: list[tuple]) -> dict:
    """pairs = [(gold, pred), ...]"""
    labels = sorted(set(g for g, _ in pairs) | set(p for _, p in pairs))
    matrix = defaultdict(Counter)
    for gold, pred in pairs:
        matrix[gold][pred] += 1
    return {k: dict(v) for k, v in matrix.items()}, labels


def print_confusion(matrix: dict, labels: list, axis_name: str) -> None:
    print(f"\n  Confusion matrix — {axis_name}")
    print(f"  {'':>6}" + "".join(f"{l:>6}" for l in labels) + "  ← predicted")
    for gold in labels:
        row = matrix.get(gold, {})
        print(f"  {gold:>6}" + "".join(f"{row.get(p, 0):>6}" for p in labels))
    print("  ↑ gold")


def eval_translator(translator: str, verbose: bool = False) -> dict | None:
    gold_path = DATA / f"{translator}_markup_50.json"
    pred_path = DATA / f"{translator}_full.json"

    if not gold_path.exists():
        print(f"  [{translator}] no gold file: {gold_path.name}")
        return None
    if not pred_path.exists():
        print(f"  [{translator}] no pipeline output yet: {pred_path.name}")
        print(f"    Run: python scripts/annotate_batch.py {translator} --limit 50")
        return None

    gold_notes = load(gold_path)
    pred_notes = load(pred_path)

    # Match by position (first N notes); both should be in same order
    n = min(len(gold_notes), len(pred_notes), 50)
    if n == 0:
        print(f"  [{translator}] no notes to compare")
        return None

    pairs_k2 = []   # axis_2_kazansky
    pairs_k4 = []   # axis_4_paribok (only for notes where human labeled it non-default)

    for i in range(n):
        g = gold_notes[i]
        p = pred_notes[i]

        gold_k2 = g.get("axis_2_kazansky", "?")
        pred_k2 = p.get("axis_2_kazansky", "?")
        pairs_k2.append((gold_k2, pred_k2))

        # axis_4: only meaningful where human assigned K or D (not default P)
        gold_k4 = g.get("axis_4_paribok", "P")
        pred_k4 = p.get("axis_4_paribok", "P")
        pairs_k4.append((gold_k4, pred_k4))

    acc_k2 = sum(g == p for g, p in pairs_k2) / len(pairs_k2)
    acc_k4 = sum(g == p for g, p in pairs_k4) / len(pairs_k4)

    print(f"\n  [{translator}]  n={n}")
    print(f"    axis_2_kazansky accuracy: {acc_k2:.1%}")
    print(f"    axis_4_paribok  accuracy: {acc_k4:.1%}")

    if verbose:
        mat_k2, lab_k2 = confusion_matrix(pairs_k2)
        print_confusion(mat_k2, lab_k2, "axis_2_kazansky")
        mat_k4, lab_k4 = confusion_matrix(pairs_k4)
        print_confusion(mat_k4, lab_k4, "axis_4_paribok")

        # Show mismatches
        mismatches = [(i+1, g, p) for i, (g, p) in enumerate(pairs_k2) if g != p]
        if mismatches:
            print(f"\n  axis_2 mismatches ({len(mismatches)}):")
            for idx, g, p in mismatches[:10]:
                raw = gold_notes[idx-1].get("raw_text", "")[:80]
                print(f"    [{idx}] gold={g} pred={p}  {raw}...")

    return {"translator": translator, "n": n, "acc_k2": acc_k2, "acc_k4": acc_k4}


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate annotation pipeline accuracy")
    parser.add_argument("translator", nargs="?", help="Translator slug, or omit for --all")
    parser.add_argument("--all", action="store_true", help="Evaluate all translators")
    parser.add_argument("--verbose", "-v", action="store_true",
                        help="Show confusion matrices and mismatches")
    args = parser.parse_args()

    targets = TRANSLATORS if args.all else ([args.translator] if args.translator else [])
    if not targets:
        parser.print_help()
        sys.exit(1)

    print("\n## Pipeline evaluation — axis_2_kazansky and axis_4_paribok\n")
    results = []
    for tr in targets:
        r = eval_translator(tr, verbose=args.verbose)
        if r:
            results.append(r)

    if len(results) > 1:
        avg_k2 = sum(r["acc_k2"] for r in results) / len(results)
        avg_k4 = sum(r["acc_k4"] for r in results) / len(results)
        print(f"\n## Summary ({len(results)} translators)")
        print(f"   axis_2_kazansky avg accuracy: {avg_k2:.1%}")
        print(f"   axis_4_paribok  avg accuracy: {avg_k4:.1%}")
        print(f"   Target: ≥85% on both axes (Article 1 data quality threshold)")


if __name__ == "__main__":
    main()

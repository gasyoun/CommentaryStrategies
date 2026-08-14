#!/usr/bin/env python3
"""Build deterministic JSON/HTML for conservative two-reviewer outcomes."""
from __future__ import annotations

import argparse
import html
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")
HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
import gate_ledger  # noqa: E402


def build(doc: dict) -> dict:
    rows = []
    counts = {"eligible": 0, "eligible_edited": 0, "exclude": 0,
              "editorial_queue": 0, "pending": 0}
    for note_id, entry in sorted(doc.get("entries", {}).items()):
        vs = entry.get("verdicts") or {}
        outcome = gate_ledger.derived_outcome(vs)
        counts[outcome] += 1
        if outcome in {"editorial_queue", "pending"}:
            rows.append({"id": note_id, "layer": entry.get("layer", ""),
                         "verse_id": entry.get("verse_id", ""), "outcome": outcome,
                         "editorial_veto": any(v.get("action") == "reject" for v in vs.values()),
                         "verdicts": vs})
    return {"schema_version": 1, "policy": "conservative-dual-review-v1",
            "counts": counts, "queue": rows}


def render(report: dict) -> str:
    rows = []
    for row in report["queue"]:
        verdicts = "<br>".join(f"<b>{html.escape(name)}</b>: {html.escape(json.dumps(v, ensure_ascii=False, sort_keys=True))}" for name, v in sorted(row["verdicts"].items()))
        rows.append(f"<tr><td>{html.escape(row['id'])}</td><td>{html.escape(row['outcome'])}</td><td>{'да' if row['editorial_veto'] else 'нет'}</td><td>{verdicts}</td></tr>")
    return """<!doctype html><html lang=\"ru\"><head><meta charset=\"utf-8\"><link rel=\"stylesheet\" href=\"../../css/commentary.css\"><title>Очередь разногласий</title></head><body><main class=\"container\"><h1>Леонов–Костина: редакционная очередь</h1><p>Разногласия не разрешаются автоматически; любой reject сохраняет редакционное вето.</p><table><thead><tr><th>ID</th><th>Исход</th><th>Вето</th><th>Свидетельства</th></tr></thead><tbody>""" + "".join(rows) + "</tbody></table></main></body></html>"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--ledger", type=Path, default=ROOT / "data" / "apparatus" / "gate_ledger.json")
    ap.add_argument("--json", type=Path, default=ROOT / "data" / "apparatus" / "gate_disagreements.json")
    ap.add_argument("--html", type=Path, default=ROOT / "data" / "apparatus" / "gate_disagreements.html")
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    report = build(gate_ledger.load(str(args.ledger)))
    outputs = {args.json: json.dumps(report, ensure_ascii=False, indent=2) + "\n",
               args.html: render(report)}
    if args.check:
        stale = [str(path) for path, content in outputs.items()
                 if not path.exists() or path.read_text(encoding="utf-8") != content]
        if stale:
            print("FAIL: stale queue outputs: " + ", ".join(stale))
            return 1
    else:
        for path, content in outputs.items():
            path.write_text(content, encoding="utf-8")
    print(f"PASS: queue={len(report['queue'])}; counts={report['counts']}; check={args.check}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

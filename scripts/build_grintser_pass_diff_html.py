"""Build the human-readable до/после page for the H2833 Grintser style pass.

Renders both ledgers (data/lexical/style_pass_h2833/ch1_audit.json +
book_s1_audit.json) as a static side-by-side page —
data/analysis/grintser_pass_h2833_diff.html. Informational, not a ballot:
the votable ballot remains data/apparatus/sarga_01_kostina.html.

Run: python scripts/build_grintser_pass_diff_html.py
"""

import html
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
LEDGERS = [
    ("data/lexical/ch1.json (Phase-1 лексический слой)",
     ROOT / "data" / "lexical" / "style_pass_h2833" / "ch1_audit.json"),
    ("data/sundara_commentary_to_add.json (агрегат книги, песнь 1)",
     ROOT / "data" / "lexical" / "style_pass_h2833" / "book_s1_audit.json"),
]
OUT = ROOT / "data" / "analysis" / "grintser_pass_h2833_diff.html"


def main():
    parts = [
        "<!DOCTYPE html>",
        '<html lang="ru"><head><meta charset="utf-8">',
        "<title>H2833 — правка лексических примечаний песни 1: до/после</title>",
        '<link rel="stylesheet" href="../../css/commentary.css">',
        "<style>.pair{display:grid;grid-template-columns:1fr 1fr;gap:1rem;"
        "margin:1rem 0;padding:.8rem;border:1px solid #ddd;border-radius:6px}"
        ".before{color:#7a3030}.after{color:#1e5c1e}"
        ".lemma{font-weight:bold;margin-top:1.5rem}</style>",
        "</head><body>",
        '<main class="container"><div>',
        "<h1>H2833 — Гринцеровская правка лексических примечаний песни 1</h1>",
        "<p>Конвенции: docs/LEXICAL_NOTE_STYLE_GRINTSER_2026.md. Правка внесена "
        "в источники (JSON); бюллетень пересобран. Слева — до, справа — после.</p>",
    ]
    total = 0
    for label, path in LEDGERS:
        if not path.exists():
            continue
        ledger = json.loads(path.read_text(encoding="utf-8"))
        parts.append(f"<h2>{html.escape(label)} — {len(ledger)} правок</h2>")
        for row in ledger:
            total += 1
            parts.append(
                f'<div class="lemma">{html.escape(str(row.get("shloka") or ""))} · '
                f"{html.escape(str(row.get('lemma_iast') or ''))}</div>"
                '<div class="pair">'
                f'<div class="before">{html.escape(row["before"])}</div>'
                f'<div class="after">{html.escape(row["after"])}</div></div>'
            )
    parts.append(f"<p>Всего правок: {total}. Модель: Fable 5 (claude-fable-5), 16-08-2026.</p>")
    parts.append("</div></main></body></html>")
    OUT.write_text("\n".join(parts), encoding="utf-8")
    print(f"{OUT} — {total} pairs")


if __name__ == "__main__":
    main()

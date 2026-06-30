"""
Generate B5_ANNOTATION_SHEET.tsv — a clean sheet for the second coder (Kostina)
to annotate axis_2 and axis_4 without seeing the machine/author labels.

Usage:
    python scripts/generate_b5_sheet.py

Output:
    sources/B5_ANNOTATION_SHEET.tsv   — for Kostina to fill
    sources/B5_ANSWER_KEY.tsv         — machine labels (not shown to Kostina)
"""

import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

REPO = Path(__file__).parent.parent
SRC  = REPO / "data" / "leonov_markup_50.json"
OUT  = REPO / "sources"

records = json.loads(SRC.read_text(encoding="utf-8"))

# ── Sheet for Kostina (no labels) ─────────────────────────────────────────────
sheet_lines = ["#\tАдрес\tТекст примечания\taxis_2_your\taxis_4_your\tПримечание"]
for i, r in enumerate(records, 1):
    text = r.get("raw_text", "").replace("\t", " ").replace("\n", " ")
    addr = r.get("shloka_addr", "")
    sheet_lines.append(f"{i}\t{addr}\t{text}\t\t\t")

(OUT / "B5_ANNOTATION_SHEET.tsv").write_text(
    "\n".join(sheet_lines), encoding="utf-8"
)
print(f"Sheet: {len(records)} notes → sources/B5_ANNOTATION_SHEET.tsv")

# ── Answer key (machine labels, keep private) ──────────────────────────────────
key_lines = [
    "#\tАдрес\taxis_2_machine\taxis_4_machine\taxis_1_topic\traw_text"
]
for i, r in enumerate(records, 1):
    text = r.get("raw_text", "").replace("\t", " ").replace("\n", " ")
    addr = r.get("shloka_addr", "")
    a2   = r.get("axis_2_kazansky", "")
    a4   = r.get("axis_4_paribok", "")
    a1   = "|".join(r.get("axis_1_topic", []))
    key_lines.append(f"{i}\t{addr}\t{a2}\t{a4}\t{a1}\t{text}")

(OUT / "B5_ANSWER_KEY.tsv").write_text(
    "\n".join(key_lines), encoding="utf-8"
)
print(f"Key:   {len(records)} notes → sources/B5_ANSWER_KEY.tsv  (do not share)")

# ── Distribution summary ───────────────────────────────────────────────────────
from collections import Counter
a2_counts = Counter(r.get("axis_2_kazansky") for r in records)
a4_counts = Counter(r.get("axis_4_paribok")  for r in records)
print("\nDistribution in machine labels:")
print(f"  axis_2: {dict(sorted(a2_counts.items()))}")
print(f"  axis_4: {dict(sorted(a4_counts.items()))}")

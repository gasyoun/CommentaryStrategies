"""
BG cross-commentator divergence on core philosophical terms.

For each Sanskrit term, finds which BG verses mention it across the 13 Sanskrit
commentaries, then measures divergence (coefficient of variation of comment lengths).
High CV = commentators wildly disagree on how much to say → philosophically contested.

Output:
    data/analysis/bg_divergence.json
    data/analysis/bg_divergence.html
"""

import json
import re
import statistics
import sys
from collections import defaultdict
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

REPO = Path(__file__).parent.parent
DATA = REPO / "data" / "gita"
OUT  = REPO / "data" / "analysis"

SC_FIELDS = [
    "scsh", "scram", "scanand", "scang", "scjaya", "scmad",
    "scval", "scms", "scsri", "scvv", "scpur", "scneel", "scdhan",
]
SC_LABELS = {
    "scsh":    "Śaṅkara",
    "scram":   "Rāmānuja",
    "scanand": "Ānandagiri",
    "scang":   "Abhinavagupta",
    "scjaya":  "Jayatīrtha",
    "scmad":   "Madhva",
    "scval":   "Vallabha",
    "scms":    "Madhusudan S.",
    "scsri":   "Śrīdhara",
    "scvv":    "Veṅkaṭanātha",
    "scpur":   "Puruṣottama",
    "scneel":  "Nīlakaṇṭha",
    "scdhan":  "Dhanapati",
}

# Devanagari search strings per concept (substring match — catches inflected forms)
TERMS = {
    "brahman":  ["ब्रह्म"],
    "ātman":    ["आत्म"],
    "karma":    ["कर्म"],
    "yoga":     ["योग"],
    "mokṣa":   ["मोक्ष", "मुक्ति"],
    "dharma":   ["धर्म"],
    "jñāna":   ["ज्ञान"],
    "bhakti":   ["भक्ति"],
    "māyā":    ["माया"],
    "buddhi":   ["बुद्धि"],
    "guṇa":    ["सत्त्व", "रजस्", "तमस्"],
    "jīva":    ["जीव"],
    "īśvara":  ["ईश्वर"],
}


def load_verses() -> list[dict]:
    verses = []
    for ch_dir in sorted(DATA.glob("chapter_*")):
        for vf in sorted(ch_dir.glob("verse_*.json")):
            d = json.loads(vf.read_text(encoding="utf-8"))
            verses.append(d)
    return verses


def contains_term(text: str, strings: list[str]) -> bool:
    return any(s in text for s in strings)


def coeff_variation(values: list[int]) -> float:
    nonzero = [v for v in values if v > 0]
    if len(nonzero) < 2:
        return 0.0
    mean = statistics.mean(nonzero)
    if mean == 0:
        return 0.0
    return statistics.stdev(nonzero) / mean


def analyze(verses: list[dict]) -> dict:
    results = {}

    for term, strings in TERMS.items():
        # Per verse: which commentators mention the term and their lengths
        verse_hits = []
        # Per commentator: how many verses they mention the term in
        comm_mention_count = defaultdict(int)
        comm_present_count = defaultdict(int)

        for v in verses:
            ch, vn = v.get("chapter", 0), v.get("verse", 0)
            verse_id = f"{ch}.{vn}"
            per_comm = {}
            for f in SC_FIELDS:
                text = v.get(f, "")
                if text:
                    comm_present_count[f] += 1
                    if contains_term(text, strings):
                        per_comm[f] = len(text)
                        comm_mention_count[f] += 1
                    else:
                        per_comm[f] = 0
                else:
                    per_comm[f] = None  # field absent for this verse

            n_mentioning = sum(1 for x in per_comm.values() if x)
            if n_mentioning == 0:
                continue

            lengths = [x for x in per_comm.values() if x is not None]
            cv = coeff_variation(lengths)
            verse_hits.append({
                "verse_id": verse_id,
                "chapter": ch,
                "verse": vn,
                "n_commentators_mentioning": n_mentioning,
                "cv": round(cv, 3),
                "lengths": per_comm,
            })

        # Sort by CV descending for top divergence
        verse_hits.sort(key=lambda x: x["cv"], reverse=True)

        mention_rates = {}
        for f in SC_FIELDS:
            total = comm_present_count[f]
            mentions = comm_mention_count[f]
            mention_rates[f] = round(mentions / total, 3) if total else 0.0

        results[term] = {
            "strings": strings,
            "total_verses_with_hit": len(verse_hits),
            "mention_rates": mention_rates,
            "top_divergent": verse_hits[:10],
            "all_hits": verse_hits,
        }

    return results


# ── HTML rendering ─────────────────────────────────────────────────────────────

def pct_color(rate: float) -> str:
    """Green shade proportional to mention rate 0..1."""
    g = int(180 * rate)
    return f"background:#{'%02x' % (255-g)}ff{'%02x' % (255-g)}"


def len_color(chars: int, max_chars: int) -> str:
    if not chars or not max_chars:
        return "background:#f0f0f0;color:#aaa"
    g = int(160 * chars / max_chars)
    return f"background:#{'%02x' % (255-g)}ff{'%02x' % (255-g)}"


def render_html(results: dict) -> str:
    comm_heads = "".join(
        f"<th title='{f}'>{SC_LABELS[f]}</th>" for f in SC_FIELDS
    )

    sections = []
    for term, data in results.items():
        rates = data["mention_rates"]
        top = data["top_divergent"][:8]

        # Summary row: mention rates per commentator
        rate_cells = "".join(
            f"<td style='{pct_color(rates[f])};text-align:center'>"
            f"{int(rates[f]*100)}%</td>"
            for f in SC_FIELDS
        )

        # Top divergent verses table
        if top:
            max_len = max(
                (v["lengths"].get(f) or 0)
                for v in top for f in SC_FIELDS
            ) or 1
            verse_rows = []
            for v in top:
                lengths = v["lengths"]
                cells = "".join(
                    f"<td style='{len_color(lengths.get(f) or 0, max_len)};text-align:right'>"
                    f"{lengths.get(f) or 0}</td>"
                    for f in SC_FIELDS
                )
                verse_rows.append(
                    f"<tr><td><b>{v['verse_id']}</b></td>"
                    f"<td style='text-align:center'>{v['n_commentators_mentioning']}</td>"
                    f"<td style='text-align:center'><b>{v['cv']:.2f}</b></td>"
                    f"{cells}</tr>"
                )
            detail = (
                f"<table border='1' cellpadding='4' cellspacing='0' "
                f"style='border-collapse:collapse;font-size:11px;margin-top:6px'>"
                f"<tr style='background:#ddd'><th>Verse</th><th>#comm</th>"
                f"<th>CV↓</th>{comm_heads}</tr>"
                + "".join(verse_rows)
                + "</table>"
            )
        else:
            detail = "<p><i>No hits.</i></p>"

        sections.append(f"""
<h2 style='margin-top:2em;border-bottom:2px solid #666'>{term}
  <small style='color:#666;font-weight:normal'>
    ({', '.join(data['strings'])}) &mdash; {data['total_verses_with_hit']} verses
  </small>
</h2>
<p style='font-size:12px;color:#444'>Mention rate per commentator
  (% of verses where that commentator has a field AND mentions this term):</p>
<table border='1' cellpadding='4' cellspacing='0'
  style='border-collapse:collapse;font-size:11px'>
  <tr style='background:#ddd'>{comm_heads}</tr>
  <tr>{rate_cells}</tr>
</table>
<p style='font-size:12px;color:#444;margin-top:1em'>
  Top verses by divergence (CV = stddev/mean of commentator lengths;
  high CV = commentators disagree on how much to say):
</p>
{detail}
""")

    return f"""<!DOCTYPE html>
<html><head><meta charset='utf-8'>
<title>BG Cross-Commentator Divergence</title>
<link rel="stylesheet" href="../../css/commentary.css">
<style>
  body{{font-family:Georgia,serif;max-width:1400px;margin:2em auto;padding:0 1em}}
  h1{{color:#333}} h2{{color:#444}} table{{margin-bottom:1em}}
  td,th{{padding:4px 6px;vertical-align:top}}
</style>
</head><body>
<main class="container">
<h1>Bhagavad Gita — Cross-Commentator Divergence on Core Terms</h1>
<p>13 Sanskrit commentaries, 700 verses. CV (coefficient of variation) measures
how unevenly commentators distribute their attention on a term across a verse —
high CV ≈ philosophically contested or school-specific interpretation.</p>
<p><b>Commentators:</b> {', '.join(f'{SC_LABELS[f]} ({f})' for f in SC_FIELDS)}</p>
{''.join(sections)}
</main>
</body></html>"""


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    print("Loading verses...", end=" ", flush=True)
    verses = load_verses()
    print(f"{len(verses)} loaded.")

    print("Analyzing terms...")
    results = analyze(verses)

    for term, data in results.items():
        n = data["total_verses_with_hit"]
        top_cv = data["top_divergent"][0]["cv"] if data["top_divergent"] else 0
        print(f"  {term:12s}: {n:3d} verses, top CV={top_cv:.2f}")

    # Save JSON (exclude all_hits for brevity, keep top_divergent)
    json_out = {
        term: {k: v for k, v in data.items() if k != "all_hits"}
        for term, data in results.items()
    }
    (OUT / "bg_divergence.json").write_text(
        json.dumps(json_out, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"JSON → data/analysis/bg_divergence.json")

    html = render_html(results)
    (OUT / "bg_divergence.html").write_text(html, encoding="utf-8")
    print(f"HTML → data/analysis/bg_divergence.html")


if __name__ == "__main__":
    main()

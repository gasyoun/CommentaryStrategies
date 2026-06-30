"""
Sundarakanda commentary coverage vs. Leonov's annotation density.

Builds a 68-sarga × 4-commentary matrix of char counts, cross-referenced
with Leonov's accepted note count per sarga. Flags four quadrants:
  🟢 High traditional + High Leonov   — well-covered
  🟡 High traditional + Low Leonov    — untapped traditional material
  🔴 High Leonov + Low traditional    — Leonov working without support
  ⚪ Low both                          — thin zone

Output:
    data/analysis/sundara_coverage.json
    data/analysis/sundara_coverage.html
"""

import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

REPO = Path(__file__).parent.parent
COMM_DIR = REPO / "data" / "valmiki_commentaries" / "kanda_5_sundarakanda"
DATA_DIR = REPO / "data"
OUT      = REPO / "data" / "analysis"

COMMENTARIES = ["tilaka", "bhusana", "siromani", "tattvadipika"]
COMM_LABELS  = {
    "tilaka":       "Tilaka",
    "bhusana":      "Bhūṣaṇa",
    "siromani":     "Śiromaṇi",
    "tattvadipika": "Tattvadīpikā",
}
N_SARGAS = 68


def load_commentary_chars() -> dict[str, dict[int, int]]:
    """Return {commentary: {sarga: char_count}}. 0 = file absent."""
    data = {c: {} for c in COMMENTARIES}
    for c in COMMENTARIES:
        for sarga in range(1, N_SARGAS + 1):
            path = COMM_DIR / f"{c}_sarga_{sarga:02d}.txt"
            if path.exists():
                data[c][sarga] = len(path.read_text(encoding="utf-8"))
            else:
                data[c][sarga] = 0
    return data


def load_leonov_notes() -> dict[int, dict]:
    """Return {sarga: {notes, cited_comms, types}} for sargas 1..68."""
    result = {}
    for sarga in range(1, N_SARGAS + 1):
        path = DATA_DIR / f"sundara_ch{sarga}_commentary_to_add.json"
        if not path.exists():
            result[sarga] = {"notes": 0, "cited_comms": set(), "types": {}}
            continue
        items = json.loads(path.read_text(encoding="utf-8"))
        notes = [x for x in items if "_meta" not in x]
        cited = set()
        types = {}
        for n in notes:
            for c in (n.get("cited_indian_commentators") or []):
                cited.add(c)
            t = n.get("type", "?")
            types[t] = types.get(t, 0) + 1
        result[sarga] = {
            "notes": len(notes),
            "cited_comms": cited,
            "types": types,
        }
    return result


def quadrant(trad_chars: int, leonov_notes: int,
             trad_threshold: int, leo_threshold: float) -> str:
    hi_t = trad_chars >= trad_threshold
    hi_l = leonov_notes >= leo_threshold
    if hi_t and hi_l:
        return "🟢"
    if hi_t and not hi_l:
        return "🟡"
    if not hi_t and hi_l:
        return "🔴"
    return "⚪"


def build_matrix(comm_chars, leonov) -> list[dict]:
    rows = []
    for s in range(1, N_SARGAS + 1):
        total_trad = sum(comm_chars[c][s] for c in COMMENTARIES)
        n_present  = sum(1 for c in COMMENTARIES if comm_chars[c][s] > 0)
        leo        = leonov[s]
        rows.append({
            "sarga":        s,
            "comm_chars":   {c: comm_chars[c][s] for c in COMMENTARIES},
            "total_trad":   total_trad,
            "n_comms":      n_present,
            "leonov_notes": leo["notes"],
            "cited_comms":  sorted(leo["cited_comms"]),
            "types":        leo["types"],
        })
    return rows


# ── HTML rendering ─────────────────────────────────────────────────────────────

def cell_bg(val: int, max_val: int, hue: str = "green") -> str:
    if not val or not max_val:
        return "background:#f0f0f0;color:#bbb"
    intensity = val / max_val
    if hue == "green":
        r = int(255 - 160 * intensity)
        return f"background:rgb({r},255,{r})"
    if hue == "blue":
        r = int(255 - 160 * intensity)
        return f"background:rgb({r},{r},255)"
    return ""


def render_html(matrix: list[dict]) -> str:
    max_comm = {c: max(r["comm_chars"][c] for r in matrix) or 1
                for c in COMMENTARIES}
    max_leo  = max(r["leonov_notes"] for r in matrix) or 1
    max_trad = max(r["total_trad"] for r in matrix) or 1

    # Thresholds for quadrant: median of non-zero
    trad_vals = [r["total_trad"] for r in matrix if r["total_trad"] > 0]
    leo_vals  = [r["leonov_notes"] for r in matrix if r["leonov_notes"] > 0]
    trad_med  = sorted(trad_vals)[len(trad_vals) // 2] if trad_vals else 1
    leo_med   = sorted(leo_vals)[len(leo_vals) // 2]   if leo_vals  else 1

    comm_heads = "".join(
        f"<th style='writing-mode:vertical-lr;min-width:28px'>{COMM_LABELS[c]}</th>"
        for c in COMMENTARIES
    )

    rows_html = []
    for r in matrix:
        s = r["sarga"]
        q = quadrant(r["total_trad"], r["leonov_notes"], trad_med, leo_med)

        comm_chars_row = r["comm_chars"]
        comm_cells = "".join(
            "<td style='" + cell_bg(comm_chars_row[c], max_comm[c]) + ";text-align:right;"
            "font-size:10px'>"
            + ("✓" if comm_chars_row[c] else "")
            + "<span style='color:#777'>"
            + (str(comm_chars_row[c] // 100) if comm_chars_row[c] else "")
            + "</span></td>"
            for c in COMMENTARIES
        )

        cited_str = ", ".join(r["cited_comms"]) if r["cited_comms"] else ""
        types_str = " ".join(f"{k}:{v}" for k, v in sorted(r["types"].items()))

        rows_html.append(
            f"<tr>"
            f"<td style='text-align:center;font-weight:bold'>{s}</td>"
            f"{comm_cells}"
            f"<td style='{cell_bg(r['total_trad'], max_trad)};text-align:right'>"
            f"{r['total_trad']}</td>"
            f"<td style='{cell_bg(r['leonov_notes'], max_leo, 'blue')};text-align:center'>"
            f"<b>{r['leonov_notes']}</b></td>"
            f"<td style='text-align:center;font-size:16px'>{q}</td>"
            f"<td style='font-size:10px;color:#555'>{cited_str}</td>"
            f"<td style='font-size:10px;color:#555'>{types_str}</td>"
            f"</tr>"
        )

    # Summary stats
    q_counts = {"🟢": 0, "🟡": 0, "🔴": 0, "⚪": 0}
    for r in matrix:
        q_counts[quadrant(r["total_trad"], r["leonov_notes"], trad_med, leo_med)] += 1

    summary = "".join(
        f"<span style='font-size:1.4em'>{q}</span> {label}: <b>{q_counts[q]}</b> sargas &nbsp;&nbsp;"
        for q, label in [
            ("🟢", "High trad + High Leonov"),
            ("🟡", "High trad + Low Leonov"),
            ("🔴", "Low trad + High Leonov"),
            ("⚪", "Low both"),
        ]
    )

    return f"""<!DOCTYPE html>
<html><head><meta charset='utf-8'>
<title>Sundarakanda Coverage</title>
<style>
  body{{font-family:Georgia,serif;max-width:1200px;margin:2em auto;padding:0 1em}}
  h1,h2{{color:#333}} table{{border-collapse:collapse;width:100%}}
  td,th{{border:1px solid #ccc;padding:3px 6px;vertical-align:middle}}
  th{{background:#e8e8e8;font-size:12px}}
</style>
</head><body>
<h1>Sundarakanda — Commentary Coverage vs. Leonov Annotation Density</h1>

<h2>Legend</h2>
<p>{summary}</p>
<p style='font-size:12px;color:#555'>
  Thresholds: traditional chars ≥ {trad_med} (median of covered sargas),
  Leonov notes ≥ {leo_med} (median of annotated sargas).
  Green cell intensity ∝ char count (÷100 shown). Blue ∝ Leonov note count.
  "Cited" = Indian commentators explicitly cited by Leonov in that sarga.
</p>

<table>
<tr style='background:#ccc'>
  <th>Sarga</th>
  {comm_heads}
  <th>Total trad chars</th>
  <th>Leonov notes</th>
  <th>Q</th>
  <th>Cited by Leonov</th>
  <th>Note types</th>
</tr>
{''.join(rows_html)}
</table>

<h2 style='margin-top:2em'>Key findings</h2>
<ul>
  <li><b>🟡 Untapped traditional material</b> ({q_counts['🟡']} sargas):
    traditional commentators have substantial content that Leonov's apparatus
    has not yet drawn on — prime candidates for Phase 2 lexical/cross-text notes.</li>
  <li><b>🔴 Leonov working without support</b> ({q_counts['🔴']} sargas):
    Leonov annotates heavily where traditional coverage is thin —
    check whether these are structurally significant sargas (battles, descriptions)
    that commentators skip but translators must explain.</li>
  <li><b>Tattvadīpikā</b> coverage is very sparse (6 sargas) —
    treat its hits as high-value data points, not representative coverage.</li>
</ul>
</body></html>"""


def main():
    OUT.mkdir(parents=True, exist_ok=True)

    print("Loading commentary char counts...")
    comm_chars = load_commentary_chars()
    for c in COMMENTARIES:
        present = sum(1 for s in range(1, N_SARGAS+1) if comm_chars[c][s] > 0)
        total   = sum(comm_chars[c][s] for s in range(1, N_SARGAS+1))
        print(f"  {COMM_LABELS[c]:16s}: {present:2d} sargas, {total:,} chars")

    print("Loading Leonov notes...")
    leonov = load_leonov_notes()
    total_notes = sum(v["notes"] for v in leonov.values())
    print(f"  Total accepted notes: {total_notes} across {N_SARGAS} sargas")

    matrix = build_matrix(comm_chars, leonov)

    # JSON output
    json_data = {
        "sargas": matrix,
        "commentary_totals": {
            c: sum(comm_chars[c][s] for s in range(1, N_SARGAS+1))
            for c in COMMENTARIES
        },
        "leonov_total_notes": total_notes,
    }
    # Convert sets to lists for JSON
    for row in json_data["sargas"]:
        row["cited_comms"] = list(row["cited_comms"])
    (OUT / "sundara_coverage.json").write_text(
        json.dumps(json_data, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print("JSON → data/analysis/sundara_coverage.json")

    html = render_html(matrix)
    (OUT / "sundara_coverage.html").write_text(html, encoding="utf-8")
    print("HTML → data/analysis/sundara_coverage.html")

    # Quick quadrant summary to stdout
    trad_vals = [r["total_trad"] for r in matrix if r["total_trad"] > 0]
    leo_vals  = [r["leonov_notes"] for r in matrix if r["leonov_notes"] > 0]
    trad_med  = sorted(trad_vals)[len(trad_vals) // 2] if trad_vals else 1
    leo_med   = sorted(leo_vals)[len(leo_vals) // 2]   if leo_vals  else 1
    print(f"\nQuadrant summary (trad≥{trad_med} / leo≥{leo_med}):")
    q_counts = {"🟢": [], "🟡": [], "🔴": [], "⚪": []}
    for r in matrix:
        q = quadrant(r["total_trad"], r["leonov_notes"], trad_med, leo_med)
        q_counts[q].append(r["sarga"])
    for q, sargas in q_counts.items():
        print(f"  {q} {len(sargas):2d} sargas: {sargas[:10]}"
              f"{'...' if len(sargas) > 10 else ''}")


if __name__ == "__main__":
    main()

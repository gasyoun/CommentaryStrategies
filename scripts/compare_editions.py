#!/usr/bin/env python3
"""Compare the CRITICAL edition (GRETIL / Baroda) vs the SOUTHERN vulgate
(the text M. Leonov translates) for the Sundarakāṇḍa.

Discussed in ramayana-leonov/Костина.txt (Leonov: critical vs southern vs Gita
Press; missing chapters/shlokas). Produces:
  * per-sarga & book-level verse counts + deltas
  * content alignment (identical / southern-only / critical-only / variant)
  * a critical↔southern concordance
  * footnote-ready "significant absences" (southern passages absent in critical)

Sources (read-only):
  critical = GitHub/SamudraManthanam/GRETIL-1_sanskr/2_epic/ramayana/ram_05_u.htm
             (Baroda critical ed.; half-verse ids 5.SSS.VVVa / .VVVc, IAST)
  southern = GitHub/SamudraManthanam/web/corpus_builder/jsonl/05_ramayana-sundarakanda.jsonl
             (seg 'sa'; passage "sarga.verse"; the text Leonov translates)

Deterministic, stdlib-only (difflib). Outputs under data/edition_comparison/.
Usage: python scripts/compare_editions.py
"""
import sys
import os
import re
import json
import unicodedata
from difflib import SequenceMatcher

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
CRIT = os.path.join(REPO, "..", "SamudraManthanam", "GRETIL-1_sanskr",
                    "2_epic", "ramayana", "ram_05_u.htm")
SOUTH = os.path.join(REPO, "..", "SamudraManthanam", "web", "corpus_builder",
                     "jsonl", "05_ramayana-sundarakanda.jsonl")
OUTDIR = os.path.join(REPO, "data", "edition_comparison")

VERSE_RE = re.compile(r"5\.(\d+)\.(\d+)([ac])\s+(.+)")


def norm(s):
    """Normalize an IAST verse for content comparison."""
    s = unicodedata.normalize("NFC", s).lower()
    s = re.sub(r"[०-९0-9]", "", s)          # verse digits
    s = re.sub(r"[।॥|/.,;:\-—()\[\]']", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def load_critical():
    """-> ordered list of (sarga, verse, text); dict counts per sarga."""
    txt = open(CRIT, encoding="utf-8", errors="replace").read()
    txt = re.sub(r"<[^>]+>", " ", txt)
    halves = {}
    order = []
    for line in txt.splitlines():
        m = VERSE_RE.search(line.strip())
        if not m:
            continue
        s, v, half, body = int(m.group(1)), int(m.group(2)), m.group(3), m.group(4).strip()
        key = (s, v)
        if key not in halves:
            halves[key] = {"a": "", "c": ""}
            order.append(key)
        halves[key][half] = body
    verses = [(s, v, (halves[(s, v)]["a"] + " " + halves[(s, v)]["c"]).strip())
              for (s, v) in order]
    return verses


def load_southern():
    verses = []
    for line in open(SOUTH, encoding="utf-8"):
        line = line.strip()
        if not line:
            continue
        d = json.loads(line)
        if d.get("seg") != "sa":
            continue
        p = d.get("passage", "")
        if "." not in p:
            continue
        s, v = p.split(".", 1)
        if not (s.isdigit() and v.isdigit()):
            continue
        verses.append((int(s), int(v), d.get("text", "")))
    verses.sort(key=lambda x: (x[0], x[1]))
    return verses


def per_sarga_counts(verses):
    from collections import Counter
    return Counter(s for s, v, t in verses)


def main():
    crit = load_critical()
    south = load_southern()
    os.makedirs(OUTDIR, exist_ok=True)

    cc, sc = per_sarga_counts(crit), per_sarga_counts(south)
    all_sargas = sorted(set(cc) | set(sc))
    per_sarga = [{
        "sarga": s,
        "critical_verses": cc.get(s, 0),
        "southern_verses": sc.get(s, 0),
        "delta_southern_minus_critical": sc.get(s, 0) - cc.get(s, 0),
        "only_in_one_edition": (cc.get(s, 0) == 0) or (sc.get(s, 0) == 0),
    } for s in all_sargas]

    # ---- content alignment at BOOK level (robust to sarga renumbering) ----
    cn = [norm(t) for _, _, t in crit]
    sn = [norm(t) for _, _, t in south]
    sm = SequenceMatcher(a=cn, b=sn, autojunk=False)

    concordance = []      # aligned/inserted/deleted rows
    south_only = []       # southern verses absent in critical (footnote candidates)
    crit_only = []        # critical verses absent in southern
    variants = []         # replace regions -> per-pair variant
    identical = 0

    def cid(i):
        s, v, t = crit[i]
        return {"critical": f"5.{s}.{v}", "text": t}

    def sid(j):
        s, v, t = south[j]
        return {"southern": f"5.{s}.{v}", "text": t}

    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            for k in range(i2 - i1):
                identical += 1
                concordance.append({"status": "identical",
                                    **{"critical": f"5.{crit[i1+k][0]}.{crit[i1+k][1]}",
                                       "southern": f"5.{south[j1+k][0]}.{south[j1+k][1]}"}})
        elif tag == "insert":
            for j in range(j1, j2):
                s, v, t = south[j]
                south_only.append({"southern": f"5.{s}.{v}", "text": t})
                concordance.append({"status": "southern_only", "southern": f"5.{s}.{v}"})
        elif tag == "delete":
            for i in range(i1, i2):
                s, v, t = crit[i]
                crit_only.append({"critical": f"5.{s}.{v}", "text": t})
                concordance.append({"status": "critical_only", "critical": f"5.{s}.{v}"})
        elif tag == "replace":
            # pair up by best similarity; leftovers = edition-only
            ci, sj = list(range(i1, i2)), list(range(j1, j2))
            used_s = set()
            for i in ci:
                best, bestr = None, 0.0
                for j in sj:
                    if j in used_s:
                        continue
                    r = SequenceMatcher(None, cn[i], sn[j]).ratio()
                    if r > bestr:
                        best, bestr = j, r
                if best is not None and bestr >= 0.6:
                    used_s.add(best)
                    variants.append({"critical": f"5.{crit[i][0]}.{crit[i][1]}",
                                     "southern": f"5.{south[best][0]}.{south[best][1]}",
                                     "similarity": round(bestr, 2),
                                     "critical_text": crit[i][2], "southern_text": south[best][2]})
                    concordance.append({"status": "variant",
                                        "critical": f"5.{crit[i][0]}.{crit[i][1]}",
                                        "southern": f"5.{south[best][0]}.{south[best][1]}",
                                        "similarity": round(bestr, 2)})
                else:
                    crit_only.append(cid(i))
                    concordance.append({"status": "critical_only", "critical": f"5.{crit[i][0]}.{crit[i][1]}"})
            for j in sj:
                if j not in used_s:
                    s, v, t = south[j]
                    south_only.append({"southern": f"5.{s}.{v}", "text": t})
                    concordance.append({"status": "southern_only", "southern": f"5.{s}.{v}"})

    # group southern-only into runs (contiguous passages) for footnotes
    south_only_sorted = sorted(south_only, key=lambda r: tuple(int(x) for x in r["southern"][2:].split(".")))
    runs = []
    for r in south_only_sorted:
        s, v = (int(x) for x in r["southern"][2:].split("."))
        if runs and runs[-1]["sarga"] == s and v == runs[-1]["_last"] + 1:
            runs[-1]["verses"].append(v)
            runs[-1]["_last"] = v
        else:
            runs.append({"sarga": s, "verses": [v], "_last": v})
    for run in runs:
        run["range"] = f"5.{run['sarga']}.{run['verses'][0]}" + (
            f"–{run['verses'][-1]}" if len(run["verses"]) > 1 else "")
        run["count"] = len(run["verses"])
        del run["_last"]

    # ---- derive SARGA correspondence from verse alignment (numbering drifts) ----
    from collections import Counter, defaultdict
    votes = defaultdict(Counter)   # critical_sarga -> Counter(southern_sarga)
    for row in concordance:
        if row["status"] in ("identical", "variant") and "critical" in row and "southern" in row:
            cs = int(row["critical"].split(".")[1])
            ss = int(row["southern"].split(".")[1])
            votes[cs][ss] += 1
    crit_to_south = {cs: c.most_common(1)[0][0] for cs, c in votes.items()}
    mapped_south = set(crit_to_south.values())
    per_sarga_aligned = []
    for s in sorted(cc):
        js = crit_to_south.get(s)
        per_sarga_aligned.append({
            "critical_sarga": s, "critical_verses": cc.get(s, 0),
            "southern_sarga": js, "southern_verses": sc.get(js, 0) if js else 0,
            "delta_southern_minus_critical": (sc.get(js, 0) if js else 0) - cc.get(s, 0),
        })
    southern_extra_sargas = sorted(set(sc) - mapped_south)   # southern sargas with no critical counterpart

    summary = {
        "_meta": {
            "generated_by": "scripts/compare_editions.py",
            "critical": "GRETIL Baroda critical edition (ram_05_u.htm)",
            "southern": "southern vulgate (samskrtam.ru / Gita Supersite) — text translated by M. Leonov",
            "method": "content alignment of normalized IAST verses (difflib), book-level",
        },
        "book_totals": {
            "critical_verses": len(crit),
            "southern_verses": len(south),
            "delta_southern_minus_critical": len(south) - len(crit),
            "critical_sargas": len(cc),
            "southern_sargas": len(sc),
            "identical_verses": identical,
            "variant_verses": len(variants),
            "southern_only_verses": len(south_only),
            "critical_only_verses": len(crit_only),
            "southern_only_runs": len(runs),
            "southern_extra_sargas": southern_extra_sargas,
        },
        "per_sarga_aligned": per_sarga_aligned,
        "southern_extra_sargas": southern_extra_sargas,
        "per_sarga_by_number_RAW": per_sarga,
        "_caveat": "Use per_sarga_aligned (sargas matched by verse content). per_sarga_by_number_RAW "
                   "compares by sarga NUMBER and is misleading after the numbering diverges. "
                   "identical/variant/only counts are content-based; near-identical verses with minor "
                   "orthographic/sandhi differences inflate 'variant' and the 'only' buckets — the "
                   "reliable absence signal is the large contiguous southern_only runs.",
    }

    json.dump(summary, open(os.path.join(OUTDIR, "book_summary.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)
    json.dump({"_meta": summary["_meta"], "concordance": concordance},
              open(os.path.join(OUTDIR, "concordance.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)
    json.dump({"_meta": {"note": "Southern verses/passages with NO critical counterpart — footnote candidates "
                                 "(«в критическом издании (Барода) отсутствует»). Grouped into contiguous runs."},
               "runs": runs, "verses": south_only},
              open(os.path.join(OUTDIR, "significant_absences.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)
    json.dump({"_meta": {"note": "Critical verses absent in southern + word-variant pairs."},
               "critical_only": crit_only, "variants": variants},
              open(os.path.join(OUTDIR, "critical_only_and_variants.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)

    bt = summary["book_totals"]
    print("BOOK:", json.dumps(bt, ensure_ascii=False))
    print(f"sargas: critical {bt['critical_sargas']} vs southern {bt['southern_sargas']}")
    print(f"southern EXTRA sargas (no critical counterpart): {southern_extra_sargas}")
    print(f"southern-only runs (footnote candidates): {len(runs)}; "
          f"largest: " + ", ".join(f"{r['range']}({r['count']})" for r in sorted(runs, key=lambda x:-x['count'])[:5]))
    print(f"wrote 4 files -> {OUTDIR}")


if __name__ == "__main__":
    main()

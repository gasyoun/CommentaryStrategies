#!/usr/bin/env python3
"""TRIAL (H4742): the REAL upstream `helayo` binary (chchch/sanskrit-alignment)
on a Sundarakāṇḍa Sa-Sa witness sample.

The 12-07-2026 spike (scripts/spike_helayo_align.py) reimplemented helayo's
METHOD in Python and explicitly did NOT run the upstream Haskell binary. This
trial closes exactly that gap: the prebuilt macOS binary from
chchch/sanskrit-alignment (helayo/dist/) is run, unmodified, over 30
critical↔southern Sundarakāṇḍa verse pairs drawn from the committed
difflib-matched pairs in data/edition_comparison/critical_only_and_variants.json.

Sample composition (deterministic, seed=42): ALL 19 spike pairs (critical
sargas 3 and 6) for continuity with the July spike + 11 more stratified over
difflib-similarity quartiles.

Per verse and per lemma mode (-l aksara, -l character) helayo writes TEI XML
with aligned <w> columns. The trial:
  1. ROUND-TRIP CANARY — de-gap each witness's columns, strip
     spaces/punctuation/digits, and require equality with the same
     normalisation of the input verse text (own-data canary, 30/30 must pass);
  2. LOCUS EXTRACTION — consecutive variant columns are grouped into
     word-level apparatus loci (word boundaries read from trailing spaces in
     the CRIT row, helayo's own "Group all words" cue);
  3. QUALITY ASSESSMENT — loci classified substantive vs orthographic-only
     (readings equal under the near-equivalence folding ā~a, ṃ~m, ś~ṣ,
     n~ṇ, t~ṭ, d~ḍ, bv, l~ḷ — the spike's matrix) vs insertion/deletion.

Stdlib-only. Read-only inputs (writes only to --out-dir).
Usage:
  python3 scripts/trial_helayo_upstream.py \
      --helayo /path/to/helayo --matrix /path/to/substitution_matrix.csv
"""
import argparse
import json
import random
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

TEI_NS = {"tei": "http://www.tei-c.org/ns/1.0"}
SIGLA = {"CRIT", "SOUTH"}

# spike_helayo_align.py near-equivalence classes (verbatim) — used ONLY to
# classify helayo's loci as orthographic vs substantive, never to align.
_NEAR = [
    set("aā"), set("iī"), set("uū"), set("ṛṝ"), set("eē"), set("oō"),
    set("nṇṅñm"), set("ṃṁ"),
    set("sśṣ"),
    set("tṭ"), set("dḍ"),
    set("bv"), set("lḷ"),
]
_NEARMAP = {}
for _cls in _NEAR:
    for _c in _cls:
        _NEARMAP.setdefault(_c, set()).update(_cls)

_STRIP = re.compile(r"[।॥|\s0-9०-९]+")


def norm_for_canary(text):
    """The normalisation helayo applies (spaces, punctuation, digits removed);
    used for the round-trip canary on OUR side of the interface."""
    return _STRIP.sub("", text or "")


def spike_pairs(variants):
    """Indices of the committed pairs the 12-07 spike exercised: critical
    sarga 3 (14 pairs) and sarga 6 (5 pairs)."""
    out = []
    for i, p in enumerate(variants):
        sarga = p["critical"].split(".")[1]
        if sarga in ("3", "6"):
            out.append(i)
    return out


def sample30(variants, seed=42):
    """All 19 spike pairs + 11 seeded, similarity-quartile-stratified extras."""
    chosen = set(spike_pairs(variants))
    rest = [i for i in range(len(variants)) if i not in chosen]
    by_sim = {}
    for i in rest:
        b = min(int(variants[i]["similarity"] * 4), 3)   # 0..3 quartile bucket
        by_sim.setdefault(b, []).append(i)
    rng = random.Random(seed)
    per_bucket = 11 // len(by_sim) + 1
    extras = []
    for b in sorted(by_sim):
        pool = sorted(by_sim[b])
        rng.shuffle(pool)
        extras.extend(pool[:per_bucket])
    chosen.update(extras[: 30 - len(chosen)])
    return sorted(chosen)


def clean(text):
    """Harness-side normalisation BEFORE helayo (mirrors the spike's clean()):
    helayo's own normaliser strips Western punctuation/sandhi but NOT the IAST
    daṇḍas (।॥) or Devanagari/Latin verse digits, and in our pair set only the
    southern witness carries them — they would attach to word-final readings
    and spawn false punctuation loci."""
    t = re.sub(r"[।॥|;,]", " ", text or "")
    t = re.sub(r"[0-9०-९]+", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def write_fastt(path, crit, south):
    with open(path, "w", encoding="utf-8") as f:
        f.write(f">CRIT\n{clean(crit)}\n\n>SOUTH\n{clean(south)}\n")


def run_helayo(helayo, matrix, mode, fas_path, xml_path):
    cmd = [helayo, "-x", matrix, "-l", mode, str(fas_path)]
    for attempt in range(3):                      # transient-error retry ×3
        try:
            r = subprocess.run(cmd, capture_output=True, timeout=120)
        except subprocess.TimeoutExpired:
            continue
        if r.returncode == 0 and r.stdout.startswith(b"<?xml"):
            xml_path.write_bytes(r.stdout)
            return
    raise RuntimeError(f"helayo failed after 3 attempts: {cmd}\n"
                       f"stderr={r.stderr.decode(errors='replace')[:300]}")


def parse_alignment(xml_path):
    """-> {siglum: [cell strings]} with '' for gap cells."""
    root = ET.parse(xml_path).getroot()
    out = {}
    for tei in root.findall("tei:TEI", TEI_NS):
        sig = tei.get("n")
        cells = [w.text or "" for w in tei.findall(".//tei:w", TEI_NS)]
        out[sig] = cells
    if not SIGLA.issubset(out):
        raise ValueError(f"{xml_path}: missing witnesses {SIGLA - set(out)}")
    n = {len(v) for v in out.values()}
    if len(n) != 1:
        raise ValueError(f"{xml_path}: ragged alignment {n}")
    return out


def group_words_pair(crit_cells, south_cells):
    """Group consecutive aligned columns into words using SHARED boundaries:
    columns are index-aligned across witnesses (verified in parse_alignment),
    so a word closes at the first column where EITHER row's cell carries a
    trailing space (helayo keeps word-final spacing on the cell). Returns two
    equal-length word lists."""
    wc, ws, ca, sa = [], [], [], []
    for c, s in zip(crit_cells, south_cells):
        ca.append(c)
        sa.append(s)
        if c.endswith(" ") or s.endswith(" "):
            wc.append("".join(ca).strip())
            ws.append("".join(sa).strip())
            ca, sa = [], []
    if ca:
        wc.append("".join(ca).strip())
        ws.append("".join(sa).strip())
    return wc, ws


def loci(crit_cells, south_cells):
    """Variant word-level loci: (crit_reading, south_reading, kind)."""
    wc, ws = group_words_pair(crit_cells, south_cells)
    if len(wc) != len(ws):   # unreachable: shared boundaries keep lists equal
        return [("ALIGNMENT-MISGROUPED", f"{len(wc)}|{len(ws)}", "error")]
    out = []
    for a, b in zip(wc, ws):
        if a == b:
            continue
        if not a or not b:
            kind = "ins/del"
        elif norm_for_canary(a) == norm_for_canary(b):
            kind = "orth-only"
        elif len(norm_for_canary(a)) == len(norm_for_canary(b)) and all(
                y in _NEARMAP.get(x, ()) for x, y in zip(norm_for_canary(a),
                                                         norm_for_canary(b))):
            kind = "orth-only"
        else:
            kind = "substantive"
        out.append((a, b, kind))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--helayo", required=True)
    ap.add_argument("--matrix", required=True)
    ap.add_argument("--variants-json",
                    default="data/edition_comparison/critical_only_and_variants.json")
    ap.add_argument("--out-dir", default="data/analysis/helayo_upstream_trial")
    ap.add_argument("--modes", nargs="+", default=["aksara", "character"])
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--n", type=int, default=30)
    args = ap.parse_args()

    repo = Path(__file__).resolve().parent.parent
    variants = json.loads((repo / args.variants_json).read_text())["variants"]
    out = repo / args.out_dir
    out.mkdir(parents=True, exist_ok=True)

    idx = sample30(variants, seed=args.seed)
    assert len(idx) == args.n, f"sample is {len(idx)}, want {args.n}"

    results, canary_fail = [], 0
    for i in idx:
        p = variants[i]
        vid = p["critical"].replace(".", "_")
        crit_c, south_c = clean(p["critical_text"]), clean(p["southern_text"])
        fas = out / f"{vid}.fas"
        write_fastt(fas, crit_c, south_c)
        rec = {"critical": p["critical"], "southern": p["southern"],
               "difflib_similarity": p["similarity"], "modes": {}}
        for mode in args.modes:
            xml = out / f"{vid}.{mode}.xml"
            run_helayo(args.helayo, args.matrix, mode, fas, xml)
            al = parse_alignment(xml)
            # round-trip canary (own data, vs the cleaned FASTT input)
            ok = True
            for sig, src in (("CRIT", crit_c), ("SOUTH", south_c)):
                got = norm_for_canary("".join(al[sig]).replace("-", ""))
                if got != norm_for_canary(src):
                    ok = False
                    rec.setdefault("canary_fail", []).append(
                        {"sig": sig, "mode": mode})
            if not ok:
                canary_fail += 1
            L = loci(al["CRIT"], al["SOUTH"])
            kinds = Counter(k for _, _, k in L)
            rec["modes"][mode] = {
                "lemmata": len(al["CRIT"]),
                "loci": len(L),
                "kinds": dict(kinds),
                "loci_detail": [{"crit": a, "south": b, "kind": k}
                                for a, b, k in L],
            }
        results.append(rec)
        print(f"{p['critical']}~{p['southern']} sim={p['similarity']:.2f} "
              + " ".join(f"{m}:{rec['modes'][m]['loci']}loci"
                         f"({rec['modes'][m]['kinds']})" for m in args.modes))

    agg = {}
    for mode in args.modes:
        tot = Counter()
        for r in results:
            tot.update(r["modes"][mode]["kinds"])
        agg[mode] = {"total_loci": sum(tot.values()), "kinds": dict(tot),
                     "verses": len(results)}
    summary = {"upstream": "chchch/sanskrit-alignment helayo/dist (macOS binary)",
               "sample": {"n": len(results), "seed": args.seed,
                          "spike_pairs_included": 19},
               "canary_failures": canary_fail, "aggregate": agg,
               "verses": results}
    (out / "trial_results.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"\nCANARY: {len(results) * len(args.modes) - canary_fail}/"
          f"{len(results) * len(args.modes)} round-trips PASS, "
          f"{canary_fail} FAIL")
    print(json.dumps(agg, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()

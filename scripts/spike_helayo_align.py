#!/usr/bin/env python3
"""SPIKE: helayo-style optimal alignment vs difflib, on one Sundarakāṇḍa sarga.

Tests whether adopting Charles Li's `helayo` method (SHARED_CODE §18) beats the
current difflib approach in scripts/compare_editions.py for producing a *critical
apparatus* (which reading, where) rather than a scalar per-verse similarity.

The current tool (sa_align.sim → difflib.SequenceMatcher.ratio) gives ONE number
per verse pair ("variant, sim=0.95") and buckets southern-only verses by a crude
token-Jaccard threshold. It cannot say *which word* is the variant or *what* the
competing readings are — the exact information an apparatus criticus needs.

helayo's documented method has three levers difflib lacks:
  1. AFFINE-GAP global alignment (Gotoh) — a globally optimal edit path under a
     linguistic cost model, vs difflib's greedy longest-matching-block heuristic.
  2. A Sanskrit-aware SUBSTITUTION MATRIX — ā~a, ṃ~m, ś~ṣ, n~ṇ score as *near*,
     not as hard mismatches, so orthographic/sandhi noise stops inflating variants.
  3. Multiple-sequence Center-Star (latent here: only 2 witnesses digitised; the
     3rd, Gita Press, would activate it).

This spike implements 1+2 faithfully at CHARACTER level (one of helayo's three
granularities) and compares, pair by pair, against difflib on the SAME committed
variant pairs from data/edition_comparison/critical_only_and_variants.json.

Stdlib-only. Read-only inputs. Usage: python spike_helayo_align.py [CRIT_SARGA]
"""
import sys
import os
import re
import json
import difflib

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

# ---------------------------------------------------------------------------
# IAST character classes for the substitution matrix (helayo lever #2).
# ---------------------------------------------------------------------------
VOWELS = set("aāiīuūṛṝḷḹeēoō") | {"ai", "au"}
_VOWEL_CHARS = set("aāiīuūṛṝḷḹeēoō")
MODIFIERS = set("ṃṁḥ̐")           # anusvāra, visarga, candrabindu
# consonants: everything else that is a letter

# near-equivalence classes: within a class, a mismatch is CHEAP (orthographic /
# sandhi / recension noise), because these routinely alternate between the
# southern vulgate and the Baroda critical text without being a real variant.
_NEAR = [
    set("aā"), set("iī"), set("uū"), set("ṛṝ"), set("eē"), set("oō"),   # vowel length
    set("nṇṅñm"), set("ṃṁ"),                                            # nasal series / anusvāra
    set("sśṣ"),                                                         # sibilants
    set("tṭ"), set("dḍ"), set("thṭh"), set("dhḍh"),                     # dental/retroflex
    set("bv"), set("lḷ"),
]
_NEARMAP = {}
for _cls in _NEAR:
    for _c in _cls:
        _NEARMAP.setdefault(_c, set()).update(_cls)


def _cls(ch):
    if ch in _VOWEL_CHARS:
        return "V"
    if ch in MODIFIERS:
        return "M"
    return "C"


def sub_score(a, b):
    """Substitution score for two IAST characters (helayo lever #2).

    +2 identical; +1 near-equivalent (length/nasal/sibilant/retroflex alternation);
    then class-graded mismatch: vowel↔vowel mild, cons↔cons medium, cross harsh.
    """
    if a == b:
        return 2.0
    if b in _NEARMAP.get(a, ()):        # near-equivalent -> almost free
        return 1.0
    ca, cb = _cls(a), _cls(b)
    if ca == cb == "V":
        return -0.5
    if ca == cb == "C":
        return -1.5
    if ca == cb == "M":
        return 0.0
    return -2.0                          # vowel↔consonant etc. — real divergence


GAP_OPEN, GAP_EXT = -2.5, -0.5          # affine gap (helayo lever #1)


def gotoh(a, b):
    """Global affine-gap alignment (Gotoh). Returns (score, aligned_a, aligned_b)
    as strings with '-' for gaps. O(len(a)*len(b))."""
    n, m = len(a), len(b)
    NEG = float("-inf")
    # M=match/sub, X=gap in b (deletion from a), Y=gap in a (insertion into b)
    Mt = [[NEG] * (m + 1) for _ in range(n + 1)]
    X = [[NEG] * (m + 1) for _ in range(n + 1)]
    Y = [[NEG] * (m + 1) for _ in range(n + 1)]
    Mt[0][0] = 0.0
    for i in range(1, n + 1):
        X[i][0] = GAP_OPEN + (i - 1) * GAP_EXT
    for j in range(1, m + 1):
        Y[0][j] = GAP_OPEN + (j - 1) * GAP_EXT
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            s = sub_score(a[i - 1], b[j - 1])
            Mt[i][j] = s + max(Mt[i - 1][j - 1], X[i - 1][j - 1], Y[i - 1][j - 1])
            X[i][j] = max(Mt[i - 1][j] + GAP_OPEN, X[i - 1][j] + GAP_EXT)
            Y[i][j] = max(Mt[i][j - 1] + GAP_OPEN, Y[i][j - 1] + GAP_EXT)
    # traceback
    i, j = n, m
    best = max((Mt[n][m], "M"), (X[n][m], "X"), (Y[n][m], "Y"))
    state = best[1]
    score = best[0]
    ra, rb = [], []
    while i > 0 or j > 0:
        if state == "M" and i > 0 and j > 0:
            ra.append(a[i - 1]); rb.append(b[j - 1])
            prev = Mt[i][j] - sub_score(a[i - 1], b[j - 1])
            i -= 1; j -= 1
            state = ("M" if abs(prev - Mt[i][j]) < 1e-9 else
                     "X" if abs(prev - X[i][j]) < 1e-9 else "Y")
        elif state == "X" and i > 0:
            ra.append(a[i - 1]); rb.append("-")
            state = "M" if abs(X[i][j] - (Mt[i - 1][j] + GAP_OPEN)) < 1e-9 else "X"
            i -= 1
        elif state == "Y" and j > 0:
            ra.append("-"); rb.append(b[j - 1])
            state = "M" if abs(Y[i][j] - (Mt[i][j - 1] + GAP_OPEN)) < 1e-9 else "Y"
            j -= 1
        elif i > 0:
            ra.append(a[i - 1]); rb.append("-"); i -= 1
        else:
            ra.append("-"); rb.append(b[j - 1]); j -= 1
    return score, "".join(reversed(ra)), "".join(reversed(rb))


# ---------------------------------------------------------------------------
# markup stripping — daṇḍas, verse numbers ॥4॥, page/section junk; keep spaces
# so we can still map a locus back to a word for the human apparatus.
# ---------------------------------------------------------------------------
def clean(text):
    t = re.sub(r"[।॥\|]", " ", text or "")
    t = re.sub(r"[0-9०-९]+", " ", t)
    t = re.sub(r"\s+", " ", t).strip()
    return t


def _word_span(text, lo, hi):
    """Expand char span [lo,hi) in `text` outward to whitespace-word boundaries,
    returning the containing word(s) — a readable apparatus reading. Empty span
    (pure gap) collapses to '' (an insertion/deletion)."""
    if lo >= hi:
        return ""
    while lo > 0 and text[lo - 1] != " ":
        lo -= 1
    while hi < len(text) and text[hi] != " ":
        hi += 1
    return text[lo:hi].strip()


def collapse_loci(aa, bb, ta, tb):
    """From two aligned strings, extract apparatus loci: maximal runs that are
    NOT identical-or-near matches, each expanded to the containing word(s) of the
    ORIGINAL texts ta/tb. Spaces count as matches so a word-boundary-only
    difference (maṇisphaṭika muktābhir | vajrasphaṭikamuktābhir) still yields ONE
    readable locus rather than mid-syllable fragments."""
    loci = []
    ia = ib = 0                      # cursor into original ta / tb
    run = None                       # [a_lo, a_hi, b_lo, b_hi]
    for x, y in zip(aa, bb):
        same = (x == y) or (x != "-" and y != "-" and y in _NEARMAP.get(x, ())) \
            or (x == " " or y == " ")
        if not same:
            if run is None:
                run = [ia, ia, ib, ib]
            if x != "-":
                run[1] = ia + 1
            if y != "-":
                run[3] = ib + 1
        else:
            if run is not None:
                loci.append(run); run = None
        if x != "-":
            ia += 1
        if y != "-":
            ib += 1
    if run is not None:
        loci.append(run)
    out = []
    for a_lo, a_hi, b_lo, b_hi in loci:
        ca = _word_span(ta, a_lo, a_hi)
        cb = _word_span(tb, b_lo, b_hi)
        if ca or cb:
            out.append((ca, cb))
    # merge adjacent loci that resolved to the same containing word pair
    merged = []
    for c, s in out:
        if merged and merged[-1] == (c, s):
            continue
        merged.append((c, s))
    return merged


def aligned_identity(aa, bb):
    """Fraction of aligned columns that are identical-or-near (a clean, gap-aware
    similarity — the helayo analogue of difflib's ratio, but on the optimal path)."""
    tot = same = 0
    for x, y in zip(aa, bb):
        if x == " " and y == " ":
            continue
        tot += 1
        if x == y or (x != "-" and y != "-" and y in _NEARMAP.get(x, ())):
            same += 1
    return same / tot if tot else 1.0


def main():
    # repo = parent of scripts/ (this file lives in scripts/); data is committed.
    repo = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    cvp = os.path.join(repo, "data", "edition_comparison",
                       "critical_only_and_variants.json")
    cv = json.load(open(cvp, encoding="utf-8"))
    sarga = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    pairs = [v for v in cv["variants"]
             if v.get("critical", "").startswith(f"5.{sarga}.") and "critical_text" in v]
    pairs.sort(key=lambda v: int(v["critical"].split(".")[2]))

    out = {"sarga": sarga, "method": {
        "difflib": "SequenceMatcher.ratio on nfold-canon string (current tool)",
        "helayo_spike": "char-level Gotoh affine-gap global alignment + "
                        "consonant/vowel/modifier substitution matrix",
        "gap": {"open": GAP_OPEN, "extend": GAP_EXT}}, "pairs": []}
    print(f"=== crit sarga {sarga}: {len(pairs)} difflib-'variant' pairs ===\n")
    diff_blocks_tot = helayo_loci_tot = 0
    for v in pairs:
        ct, st = clean(v["critical_text"]), clean(v["southern_text"])
        # difflib side (what the current tool sees)
        sm = difflib.SequenceMatcher(None, ct, st, autojunk=False)
        dratio = sm.ratio()
        dblocks = sum(1 for tag, *_ in sm.get_opcodes() if tag != "equal")
        # helayo side
        score, aa, bb = gotoh(ct, st)
        loci = collapse_loci(aa, bb, ct, st)
        app = [{"reading_crit": c or "∅", "reading_south": s or "∅"}
               for c, s in loci]
        ident = aligned_identity(aa, bb)
        diff_blocks_tot += dblocks
        helayo_loci_tot += len(loci)
        out["pairs"].append({
            "id": v["critical"], "south": v["southern"],
            "difflib_ratio": round(dratio, 3), "difflib_edit_blocks": dblocks,
            "helayo_aligned_identity": round(ident, 3),
            "helayo_apparatus_loci": len(loci), "apparatus": app,
        })
        print(f"{v['critical']} ~ {v['southern']}")
        print(f"  difflib : ratio={dratio:.3f}  ({dblocks} edit block(s), no readings)")
        print(f"  helayo  : identity={ident:.3f}  {len(loci)} apparatus locus/loci:")
        for a in app:
            print(f"            · {a['reading_crit']}  (crit)  |  {a['reading_south']}  (south)")
        print()

    out["totals"] = {"pairs": len(pairs),
                     "difflib_edit_blocks": diff_blocks_tot,
                     "helayo_apparatus_loci": helayo_loci_tot}
    print("TOTALS:", json.dumps(out["totals"], ensure_ascii=False))
    outdir = os.path.join(repo, "data", "analysis", "helayo_spike")
    os.makedirs(outdir, exist_ok=True)
    dst = os.path.join(outdir, f"spike_sarga{sarga}_result.json")
    json.dump(out, open(dst, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("wrote", os.path.relpath(dst, repo))


if __name__ == "__main__":
    main()

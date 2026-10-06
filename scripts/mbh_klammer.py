#!/usr/bin/env python3
"""mbh_klammer.py — full-Mahābhāṣya Klammeranalyse, scale pass v1 (H6055).

Rulings (Uprava/reports/GRILL_RESEARCH_WIDENING_04-10-2026.md §H):
  H1  — first full pass = MBh of Patañjali (ashtadhyayi-com/data bhashya.txt)
  H2  — one full commentary, not partial waves
  H11 — Klammer data as a JSON schema (not TEI/COVAS)
  H12 — κ gate with a second annotator (H5312/H5313 protocol shape)

What this builds (deterministic, stdlib-only, no network at build time):
  data/panini_klammer/source/{bhashya,vartika}.txt  — mirror-only cache
        (ashtadhyayi-com/data carries NO license file → never committed;
        .gitignore'd; only DERIVED measurements are committed)
  data/panini_klammer/build/mbh_klammer_bank.json    — full candidate bank
  data/panini_klammer/mbh_klammer_per_sutra.tsv      — per-sūtra counts (derived)
  data/panini_klammer/mbh_klammer_sample.json        — κ sample, both passes
  data/panini_klammer/mbh_klammer_disagreements.json — every exact mismatch
  data/panini_klammer/mbh_klammer_topcompounds.tsv   — frequency table
  data/panini_klammer/mbh_klammer_kappa.json         — κ + bootstrap CI
  data/panini_klammer/second_annotator_sheet.html    — human lane (H5312 shape)

Double annotation (the κ control): two INDEPENDENT mechanical annotators
segment every compound candidate —
  pass A: greedy longest-match, left-to-right
  pass B: greedy longest-match, right-to-left
over a corpus-induced vocabulary (tokens ≤ VOCAB_MAX_LEN chars, frequency
≥ VOCAB_MIN_FREQ, pooled over both layers). A candidate is "dually segmented"
only when both passes fully segment it. κ is Cohen's κ over the canonical
segmentation label (multi-class) plus a boundary-level binary κ, with a
2,000-resample bootstrap CI. A low κ is reported as measured, never softened.

The bracket TREE (which member modifies which — the labelled Klammerdiagramm
node structure) is deliberately NOT fabricated: v1 records members + boundaries
only; `tree` stays null with tree_status "deferred_v2" pending the human lane.

Usage:
  python3 scripts/mbh_klammer.py --fetch     # populate mirror-only cache
  python3 scripts/mbh_klammer.py --build     # rebuild every committed artifact
  python3 scripts/mbh_klammer.py --check     # parity gate: rebuild == committed
  python3 scripts/mbh_klammer.py --selftest  # hermetic internal checks
"""
from __future__ import annotations

import json
import random
import re
import sys
import urllib.request
from collections import Counter
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DATA = REPO / "data" / "panini_klammer"
SRC = DATA / "source"
BUILD = DATA / "build"

RAW = "https://raw.githubusercontent.com/ashtadhyayi-com/data/master/sutraani/"
LAYERS = {"bhashya": "bhashya.txt", "vartika": "vartika.txt"}

# Pre-registered parameters (frozen before the run; README documents them).
MIN_TOKEN_LEN = 9      # orthographic token this long => compound candidate
VOCAB_MAX_LEN = 7      # corpus token this short => simple-word vocabulary
VOCAB_MIN_FREQ = 3
MIN_CHUNK = 2          # shortest acceptable residual chunk
SAMPLE_N = 300         # κ sample size (layer-stratified, proportional)
SHEET_ROWS = 60        # human-sheet rows (stratified over disagreements)
SEED = 20261006
N_BOOT = 2000

DEVANAGARI = re.compile(r"[ऀ-ॿ]+")
CLEAN_MARK = re.compile(r"\[\[[^\]]*\]\]")
# split tokens on avagraha (clitic, never compound-internal)
SPLIT_AVAGRAHA = "ऽ"


def fetch_layer(layer: str) -> Path:
    SRC.mkdir(parents=True, exist_ok=True)
    dest = SRC / LAYERS[layer]
    if dest.exists() and dest.stat().st_size > 0:
        return dest
    url = RAW + LAYERS[layer]
    print(f"fetch {url} -> {dest}")
    with urllib.request.urlopen(url, timeout=120) as r, open(dest, "wb") as f:
        f.write(r.read())
    return dest


def parse_layer(layer: str, raw_text: str) -> list[dict]:
    """Two upstream shapes (ashtadhyayi-com/data):
    bhashya.txt — dict keyed by concatenated a.p.n -> text (3,983 sūtras)
    vartika.txt — {"name": ..., "data": [{"sutra": "1.1.9", "vartika": text}]}
    """
    data = json.loads(raw_text)
    rows = []
    if layer == "vartika":
        for rec in data["data"]:
            plain = CLEAN_MARK.sub(" ", rec["vartika"]).replace(SPLIT_AVAGRAHA, " ")
            rows.append({"sutra": rec["sutra"], "layer": layer, "text": plain})
    else:
        for key, text in data.items():
            a, p, n = int(key[:1]), int(key[1:2]), int(key[2:])
            plain = CLEAN_MARK.sub(" ", text).replace(SPLIT_AVAGRAHA, " ")
            rows.append({"sutra": f"{a}.{p}.{n}", "layer": layer, "text": plain})
    rows.sort(key=lambda r: tuple(int(x) for x in r["sutra"].split(".")))
    return rows


def tokenize(text: str) -> list[str]:
    out = []
    for tok in DEVANAGARI.findall(text):
        if len(tok) >= 2:  # single-akshara noise (प, च as discourse particles
            out.append(tok)  # after danda-splitting) still counts as a token
    return out


def build_vocab(all_tokens: list[str]) -> set[str]:
    freq = Counter(t for t in all_tokens if len(t) <= VOCAB_MAX_LEN)
    return {t for t, c in freq.items() if c >= VOCAB_MIN_FREQ}


def seg_left(token: str, vocab: set[str]) -> list[str] | None:
    """Pass A — greedy longest-match, left-to-right."""
    members, i = [], 0
    while i < len(token):
        # try the longest in-vocab chunk first; shortest allowed is MIN_CHUNK
        for end in range(len(token), i + MIN_CHUNK - 1, -1):
            if token[i:end] in vocab:
                members.append(token[i:end])
                i = end
                break
        else:
            return None
    return members or None


def seg_right(token: str, vocab: set[str]) -> list[str] | None:
    """Pass B — greedy longest-match, right-to-left (independent strategy)."""
    members, j = [], len(token)
    while j > 0:
        for start in range(0, j - MIN_CHUNK + 1):
            if token[start:j] in vocab:
                members.append(token[start:j])
                j = start
                break
        else:
            return None
    members.reverse()
    return members or None


def cohen_kappa(labels_a: list[str], labels_b: list[str]) -> float:
    """House reference implementation (csl-observatory compute_component_kappa)."""
    n = len(labels_a)
    if n == 0:
        return float("nan")
    po = sum(1 for a, b in zip(labels_a, labels_b) if a == b) / n
    ca, cb = Counter(labels_a), Counter(labels_b)
    cats = set(ca) | set(cb)
    pe = sum((ca[c] / n) * (cb[c] / n) for c in cats)
    if pe == 1.0:
        return 1.0
    return (po - pe) / (1 - pe)


def bootstrap_ci(labels_a: list[str], labels_b: list[str], seed: int,
                  n_boot: int) -> list[float]:
    rng = random.Random(seed)
    n = len(labels_a)
    vals = []
    for _ in range(n_boot):
        ia = [rng.randrange(n) for _ in range(n)]
        vals.append(cohen_kappa([labels_a[i] for i in ia],
                                [labels_b[i] for i in ia]))
    vals.sort()
    return [vals[int(0.025 * n_boot)], vals[int(0.975 * n_boot)]]


def boundary_labels(token: str, members: list[str]) -> set[int]:
    offs, pos = set(), 0
    for m in members:
        pos += len(m)
        offs.add(pos)
    offs.discard(len(token))
    return offs


def boundary_kappa(bank_rows: list[dict]) -> dict:
    """Boundary-level κ over EVERY interior code-point position of each item
    (label B = boundary / '-' = not), so -/- agreement counts like any
    standard per-position agreement — not a union-conditioned sample."""
    la, lb = [], []
    for r in bank_rows:
        ba, bb = set(r["boundaries_A"]), set(r["boundaries_B"])
        for pos in range(1, r["len"]):
            la.append("B" if pos in ba else "-")
            lb.append("B" if pos in bb else "-")
    return {"n_decisions": len(la),
            "kappa": round(cohen_kappa(la, lb), 4)}


def build(fetch: bool = False) -> dict:
    if fetch:
        for layer in LAYERS:
            fetch_layer(layer)
    rows, all_tokens = [], []
    for layer in LAYERS:
        raw = (SRC / LAYERS[layer]).read_text(encoding="utf-8")
        rows += parse_layer(layer, raw)
    for r in rows:
        toks = tokenize(r["text"])
        r["tokens"] = toks
        all_tokens += toks
    vocab = build_vocab(all_tokens)

    bank = []
    for r in rows:
        for tok in r["tokens"]:
            if len(tok) < MIN_TOKEN_LEN:
                continue
            ma, mb = seg_left(tok, vocab), seg_right(tok, vocab)
            bank.append({
                "layer": r["layer"], "sutra": r["sutra"], "form": tok,
                "len": len(tok), "freq": None,
                "members_A": ma, "members_B": mb,
                "boundaries_A": sorted(boundary_labels(tok, ma)) if ma else None,
                "boundaries_B": sorted(boundary_labels(tok, mb)) if mb else None,
                "tree": None, "tree_status": "deferred_v2",
                "schema": "mbh-klammer-v1",
            })
    freq = Counter(b["form"] for b in bank)
    for b in bank:
        b["freq"] = freq[b["form"]]

    dual = [b for b in bank if b["members_A"] and b["members_B"]]

    # --- per-sūtra counts (compact derived layer, committed) ---
    per = {}
    for b in bank:
        key = (b["sutra"], b["layer"])
        d = per.setdefault(key, {"tokens": 0, "cand": 0, "dual": 0, "agree": 0})
        d["cand"] += 1
        if b["members_A"] and b["members_B"]:
            d["dual"] += 1
            if b["members_A"] == b["members_B"]:
                d["agree"] += 1
    for r in rows:
        key = (r["sutra"], r["layer"])
        per.setdefault(key, {"tokens": 0, "cand": 0, "dual": 0, "agree": 0})
        per[key]["tokens"] = len(r["tokens"])

    # --- κ sample: layer-stratified, proportional, seeded ---
    rng = random.Random(SEED)
    sample = []
    for layer in LAYERS:
        pool = [b for b in dual if b["layer"] == layer]
        k = round(SAMPLE_N * len(pool) / max(1, len(dual)))
        sample += rng.sample(pool, min(k, len(pool)))
    la = ["|".join(b["members_A"]) for b in sample]
    lb = ["|".join(b["members_B"]) for b in sample]
    kappa_item = cohen_kappa(la, lb)
    ci = bootstrap_ci(la, lb, SEED, N_BOOT)
    po_item = sum(1 for a, b in zip(la, lb) if a == b) / max(1, len(la))
    kappa_stats = {
        "protocol": "H5312/H5313 second-annotation κ, dual mechanical passes",
        "unit": "candidate segmentation (canonical label = '|'.join(members))",
        "sample_n": len(sample), "seed": SEED, "bootstrap": N_BOOT,
        "kappa_item": round(kappa_item, 4),
        "ci95_item": [round(ci[0], 4), round(ci[1], 4)],
        "raw_agreement_item": round(po_item, 4),
        "boundary": boundary_kappa(sample),
        "labels_note": "low κ is reported as measured, never softened",
    }

    disagreements = [b for b in dual if b["members_A"] != b["members_B"]]

    # --- write artifacts ---
    BUILD.mkdir(parents=True, exist_ok=True)
    (BUILD / "mbh_klammer_bank.json").write_text(
        json.dumps(bank, ensure_ascii=False), encoding="utf-8")

    lines = ["sutra\tlayer\ttokens\tcandidates\tdually_segmented\texact_agree"]
    for (sutra, layer) in sorted(per, key=lambda k: tuple(map(int, k[0].split(".")))):
        d = per[(sutra, layer)]
        lines.append(f"{sutra}\t{layer}\t{d['tokens']}\t{d['cand']}\t{d['dual']}\t{d['agree']}")
    (DATA / "mbh_klammer_per_sutra.tsv").write_text("\n".join(lines) + "\n", encoding="utf-8")

    for b in sample + disagreements:
        for k in ("boundaries_A", "boundaries_B"):
            if b[k] is not None:
                b[k] = sorted(b[k])
    (DATA / "mbh_klammer_sample.json").write_text(
        json.dumps(sample, ensure_ascii=False, indent=1), encoding="utf-8")
    sheet_pool = disagreements[:SHEET_ROWS] if len(disagreements) <= SHEET_ROWS else []
    if len(disagreements) > SHEET_ROWS:
        per_layer_cap = {}
        for layer in LAYERS:
            pool = [b for b in disagreements if b["layer"] == layer]
            k = round(SHEET_ROWS * len(pool) / max(1, len(disagreements)))
            sheet_pool += rng.sample(pool, min(k, len(pool)))
            per_layer_cap[layer] = min(k, len(pool))
    (DATA / "mbh_klammer_disagreements.json").write_text(
        json.dumps(sheet_pool, ensure_ascii=False, indent=1), encoding="utf-8")

    top = freq.most_common(100)
    toplines = ["form\tfreq\tlen"]
    for form, c in top:
        toplines.append(f"{form}\t{c}\t{len(form)}")
    (DATA / "mbh_klammer_topcompounds.tsv").write_text(
        "\n".join(toplines) + "\n", encoding="utf-8")

    (DATA / "mbh_klammer_kappa.json").write_text(
        json.dumps(kappa_stats, ensure_ascii=False, indent=1), encoding="utf-8")

    write_sheet(sheet_pool, kappa_stats)
    return {"bank": len(bank), "dual": len(dual),
            "disagree": len(disagreements), "kappa": kappa_stats}


def write_sheet(rows: list[dict], kappa: dict) -> None:
    tr = []
    for i, r in enumerate(rows, 1):
        tr.append(
            f"<tr><td>{i}</td><td>{r['sutra']}</td><td>{r['layer']}</td>"
            f"<td class='sk'>{r['form']}</td>"
            f"<td class='sk'>{' | '.join(r['members_A'])}</td>"
            f"<td class='sk'>{' | '.join(r['members_B'])}</td>"
            f"<td class='fill'></td></tr>")
    html = f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<title>MBh Klammeranalyse — second-annotator sheet v1 (H6055)</title>
<style>
body{{font-family:Georgia,serif;max-width:1100px;margin:2rem auto;padding:0 1rem}}
table{{border-collapse:collapse;width:100%}}
td,th{{border:1px solid #999;padding:.35rem .5rem;font-size:.95rem;text-align:left;vertical-align:top}}
.sk{{font-family:'Noto Sans Devanagari',serif}}
.fill{{background:#fdf6e3;min-width:22ch}}
.note{{background:#f4f4f4;border-left:4px solid #888;padding:.5rem 1rem;margin:1rem 0;font-size:.9rem}}
</style></head><body>
<h1>Mahābhāṣya Klammeranalyse — second-annotator sheet v1</h1>
<p>H6055 · generated {SEED} · protocol H5312/H5313 shape: this sheet shows the
<strong>disagreements</strong> between the two mechanical passes (A = greedy
longest-match left-to-right; B = right-to-left) over corpus-induced vocabulary.
A human annotator writes the authoritative segmentation in the last column;
it never overwrites the machine passes.</p>
<div class="note">Item-level κ (machine A vs B, n={kappa['sample_n']}):
<b>{kappa['kappa_item']}</b> · 95% CI [{kappa['ci95_item'][0]}, {kappa['ci95_item'][1]}] ·
raw agreement {kappa['raw_agreement_item']} · boundary κ {kappa['boundary']['kappa']}.
Reported as measured.</div>
<table><thead><tr><th>#</th><th>sūtra</th><th>layer</th><th>form</th>
<th>pass A</th><th>pass B</th><th>human segmentation (fill)</th></tr></thead>
<tbody>
{chr(10).join(tr)}
</tbody></table>
<p style="font-size:.85rem;color:#555">Source: ashtadhyayi-com/data (no license
file — mirror-only cache, never committed). This sheet and every other committed
artifact are derived measurements. tree_status: deferred_v2 — bracket-node
labelling is the human lane, not fabricated here.</p>
</body></html>"""
    (DATA / "second_annotator_sheet.html").write_text(html, encoding="utf-8")


def selftest() -> None:
    assert parse_layer("bhashya", '{"11001": "वृद्धिरादैच् ॥[[1.1.1]] ॥ ऽकारः"}')[0]["sutra"] == "1.1.1"
    toks = tokenize("कुत्वं कस्मान्न भवति")
    assert toks == ["कुत्वं", "कस्मान्न", "भवति"], toks
    vocab = {"समास", "अन्त", "वृद्धि", "आदैच्", "इति"}
    assert seg_left("वृद्धिरादैच्", vocab) is None  # sandhied form, not in vocab
    m = seg_left("समासअन्त", vocab)
    assert m == ["समास", "अन्त"], m
    assert seg_right("समासअन्त", vocab) == ["समास", "अन्त"]
    assert seg_left("समासअन्त" + "य्य्य्य", vocab) is None  # unknown residue fails
    assert cohen_kappa(["a", "b", "a"], ["a", "b", "a"]) == 1.0
    k = cohen_kappa(["a", "a", "b", "b"], ["a", "b", "a", "b"])
    assert k < 0.01, k  # pure chance ≈ 0
    assert boundary_labels("समासअन्त", ["समास", "अन्त"]) == {4}  # code-point offset
    print("SELFTEST PASS")


def check() -> None:
    """Parity gate: committed artifacts must equal a fresh rebuild."""
    keep = {}
    for name in ("mbh_klammer_per_sutra.tsv", "mbh_klammer_sample.json",
                 "mbh_klammer_disagreements.json", "mbh_klammer_topcompounds.tsv",
                 "mbh_klammer_kappa.json", "second_annotator_sheet.html"):
        p = DATA / name
        keep[name] = p.read_text(encoding="utf-8") if p.exists() else None
    build(fetch=False)
    bad = [n for n, old in keep.items()
           if old is None or (DATA / n).read_text(encoding="utf-8") != old]
    if bad:
        print(f"CHECK FAIL — drifted: {bad}")
        sys.exit(1)
    print("CHECK PASS — all committed artifacts reproduce byte-identically")


def main() -> None:
    args = sys.argv[1:]
    if "--fetch" in args:
        for layer in LAYERS:
            fetch_layer(layer)
        stats = build(fetch=False)
    elif "--build" in args:
        stats = build(fetch=False)
    elif "--check" in args:
        check()
        return
    elif "--selftest" in args:
        selftest()
        return
    else:
        print(__doc__)
        return
    print(json.dumps(stats, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()

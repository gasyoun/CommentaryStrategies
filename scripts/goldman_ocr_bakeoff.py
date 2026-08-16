#!/usr/bin/env python3
"""H2832 — one fixed page sample, several extraction engines, one table.

Why a harness instead of "we OCR'd it and it looked fine": the handoff's
Fail-condition is exactly that sentence, plus "different engines compared on
different pages". So the sample is hardcoded here, every engine sees the same
rendered pixels / the same PDF pages, and every run records wall time.

Engines
-------
embedded        PyMuPDF `page.get_text()` over the PDF's own text layer
pdfminer        pdfminer.six over the same layer (isolates extractor vs. layer)
tesseract-eng   render at --dpi, Tesseract 5 `-l eng`
tesseract-engsan  same pixels, `-l eng+san` (Devanagari model added)
vision          renders the pages only; the transcription is done by the
                session model reading the PNGs and dropped into
                <out>/vision/p####.txt — the harness then scores it like any
                other engine. Timing for this engine is recorded by hand in the
                report, not here.

Metrics
-------
Gold-free (run on all sample pages):
  iast          count of IAST diacritic codepoints produced
  deva          count of Devanagari codepoints produced
  junk_tok      share of whitespace tokens containing an OCR-damage character
                (~ ¼ ½ ¢ | \\ ! ; : inside a word) — the signature of a layer
                that has flattened ā ī ū ṛ ṇ ṣ ḥ ṭ ḍ into punctuation
  fffd          U+FFFD replacement characters
Gold-scored (only on pages with data/goldman/gold/p####.txt):
  cer           character error rate vs gold (Levenshtein / len(gold))
  wer           word error rate
  iast_recall   share of the gold's IAST diacritic characters that survive

Usage
-----
    python scripts/goldman_ocr_bakeoff.py render --pdf X.pdf --out DIR --dpi 300
    python scripts/goldman_ocr_bakeoff.py run    --pdf X.pdf --out DIR \
        --engines embedded,pdfminer,tesseract-eng,tesseract-engsan
    python scripts/goldman_ocr_bakeoff.py score  --out DIR --gold data/goldman/gold \
        --json data/goldman/bakeoff_vol5.json

`--out` must point OUTSIDE the repo (scratchpad): the rendered pages and the
extracted text of a copyrighted Princeton volume are working material and are
never committed. Only the scores are.
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import time

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

import fitz  # noqa: E402

# --- the fixed sample -------------------------------------------------------
# 1-based PDF page numbers in the Princeton Sundarakāṇḍa volume, chosen to span
# every layout class the handoff names: running prose, IAST-dense scholarly
# notes, a diacritics chart, a footnoted introduction, and three dense
# multi-column back-matter pages.
SAMPLE: dict[int, str] = {
    10: "front matter — List of Abbreviations (dense sigla, two columns)",
    18: "Guide to Sanskrit Pronunciation (the diacritics chart itself)",
    108: "Introduction §8 Text, Translation, Commentaries (footnoted prose)",
    130: "Part II translation — verse-numbered prose, sarga 1",
    250: "Part II translation — verse-numbered prose, sarga 41",
    321: "Part III Notes to sarga 1 — IAST-dense scholarly apparatus",
    333: "Part III Notes to sarga 1 — lemma + commentator sigla",
    565: "Glossary of Important Sanskrit Words (dense IAST, two columns)",
    571: "Bibliography of Works Consulted (mixed scripts, hanging indents)",
    585: "Index (dense multi-column IAST, smallest type in the book)",
}

IAST = set("āĀīĪūŪṛṚṝṜḷḶḹḸṅṄñÑṭṬḍḌṇṆśŚṣṢṃṂḥḤṁ")
DEVA = range(0x0900, 0x0980)
JUNK = set("~¼½¢|\\!;")

TESSERACT = shutil.which("tesseract") or r"C:\Program Files\Tesseract-OCR\tesseract.exe"


# --- helpers ----------------------------------------------------------------
def png_path(out: str, pno: int) -> str:
    return os.path.join(out, "png", f"p{pno:04d}.png")


def txt_path(out: str, engine: str, pno: int) -> str:
    return os.path.join(out, engine, f"p{pno:04d}.txt")


def write_text(path: str, text: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)


def read_text(path: str) -> str | None:
    if not os.path.exists(path):
        return None
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def levenshtein(a: str, b: str) -> int:
    """Two-row DP. Pages are ~4 kB so this is a few seconds at worst."""
    if a == b:
        return 0
    if not a:
        return len(b)
    if not b:
        return len(a)
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]


def normalize(s: str) -> str:
    """Whitespace-insensitive comparison — line wrapping is not an OCR error."""
    return " ".join(s.split())


# --- engines ----------------------------------------------------------------
def engine_embedded(pdf: str, pno: int, out: str, dpi: int) -> str:
    doc = fitz.open(pdf)
    return doc.load_page(pno - 1).get_text("text")


def engine_pdfminer(pdf: str, pno: int, out: str, dpi: int) -> str:
    from pdfminer.high_level import extract_text

    return extract_text(pdf, page_numbers=[pno - 1])


def _tesseract(out: str, pno: int, lang: str) -> str:
    src = png_path(out, pno)
    if not os.path.exists(src):
        raise FileNotFoundError(f"render first: {src}")
    base = os.path.join(out, "_tess_tmp")
    os.makedirs(os.path.dirname(base) or ".", exist_ok=True)
    cmd = [TESSERACT, src, base, "-l", lang, "--psm", "1"]
    subprocess.run(cmd, check=True, capture_output=True, encoding="utf-8", errors="replace")
    with open(base + ".txt", encoding="utf-8") as fh:
        return fh.read()


def engine_tess_eng(pdf: str, pno: int, out: str, dpi: int) -> str:
    return _tesseract(out, pno, "eng")


def engine_tess_engsan(pdf: str, pno: int, out: str, dpi: int) -> str:
    return _tesseract(out, pno, "eng+san")


ENGINES = {
    "embedded": engine_embedded,
    "pdfminer": engine_pdfminer,
    "tesseract-eng": engine_tess_eng,
    "tesseract-engsan": engine_tess_engsan,
}


# --- metrics ----------------------------------------------------------------
def gold_free(text: str) -> dict:
    toks = text.split()
    junk = sum(1 for t in toks if any(c in JUNK for c in t))
    return {
        "chars": len(text),
        "tokens": len(toks),
        "iast": sum(1 for c in text if c in IAST),
        "deva": sum(1 for c in text if ord(c) in DEVA),
        "fffd": text.count("\ufffd"),
        "junk_tokens": junk,
        "junk_token_rate": round(junk / len(toks), 4) if toks else 0.0,
    }


def gold_scored(hyp: str, gold: str) -> dict:
    h, g = normalize(hyp), normalize(gold)
    dist = levenshtein(h, g)
    hw, gw = h.split(), g.split()
    wdist = levenshtein_words(hw, gw)
    gold_iast = [c for c in g if c in IAST]
    hyp_iast_ct: dict[str, int] = {}
    for c in h:
        if c in IAST:
            hyp_iast_ct[c] = hyp_iast_ct.get(c, 0) + 1
    kept = 0
    need: dict[str, int] = {}
    for c in gold_iast:
        need[c] = need.get(c, 0) + 1
    for c, n in need.items():
        kept += min(n, hyp_iast_ct.get(c, 0))
    return {
        "cer": round(dist / max(1, len(g)), 4),
        "wer": round(wdist / max(1, len(gw)), 4),
        "gold_iast_chars": len(gold_iast),
        "iast_recall": round(kept / max(1, len(gold_iast)), 4),
    }


def levenshtein_words(a: list[str], b: list[str]) -> int:
    if a == b:
        return 0
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]


# --- commands ---------------------------------------------------------------
def cmd_render(args) -> int:
    doc = fitz.open(args.pdf)
    os.makedirs(os.path.join(args.out, "png"), exist_ok=True)
    zoom = args.dpi / 72.0
    for pno in sorted(SAMPLE):
        t0 = time.perf_counter()
        pix = doc.load_page(pno - 1).get_pixmap(matrix=fitz.Matrix(zoom, zoom))
        pix.save(png_path(args.out, pno))
        print(f"p{pno:>4}  {pix.width}x{pix.height}  {time.perf_counter() - t0:.2f}s")
    return 0


def cmd_run(args) -> int:
    engines = [e.strip() for e in args.engines.split(",") if e.strip()]
    timings: dict[str, dict[str, float]] = {}
    for eng in engines:
        if eng not in ENGINES:
            print(f"unknown engine {eng}", file=sys.stderr)
            return 2
        fn = ENGINES[eng]
        per: dict[str, float] = {}
        t_all = time.perf_counter()
        for pno in sorted(SAMPLE):
            t0 = time.perf_counter()
            text = fn(args.pdf, pno, args.out, args.dpi)
            per[str(pno)] = round(time.perf_counter() - t0, 3)
            write_text(txt_path(args.out, eng, pno), text)
        total = round(time.perf_counter() - t_all, 3)
        timings[eng] = {"per_page": per, "total_s": total, "sec_per_page": round(total / len(SAMPLE), 3)}
        print(f"{eng:<18} {total:>7.2f}s  ({total / len(SAMPLE):.2f} s/page)")
    tpath = os.path.join(args.out, "timings.json")
    prior = {}
    if os.path.exists(tpath):
        with open(tpath, encoding="utf-8") as fh:
            prior = json.load(fh)
    prior.update(timings)
    with open(tpath, "w", encoding="utf-8") as fh:
        json.dump(prior, fh, ensure_ascii=False, indent=1)
    return 0


def cmd_score(args) -> int:
    tpath = os.path.join(args.out, "timings.json")
    timings = {}
    if os.path.exists(tpath):
        with open(tpath, encoding="utf-8") as fh:
            timings = json.load(fh)

    engines = sorted(
        d for d in os.listdir(args.out) if os.path.isdir(os.path.join(args.out, d)) and d != "png"
    )
    report: dict = {"sample": {str(k): v for k, v in SAMPLE.items()}, "engines": {}}
    for eng in engines:
        pages: dict[str, dict] = {}
        for pno in sorted(SAMPLE):
            hyp = read_text(txt_path(args.out, eng, pno))
            if hyp is None:
                continue
            row = gold_free(hyp)
            gold = read_text(os.path.join(args.gold, f"p{pno:04d}.txt")) if args.gold else None
            if gold:
                row.update(gold_scored(hyp, gold))
            pages[str(pno)] = row
        if not pages:
            continue
        scored = [p for p in pages.values() if "cer" in p]
        agg = {
            "pages": len(pages),
            "chars": sum(p["chars"] for p in pages.values()),
            "iast": sum(p["iast"] for p in pages.values()),
            "deva": sum(p["deva"] for p in pages.values()),
            "fffd": sum(p["fffd"] for p in pages.values()),
            "junk_token_rate": round(
                sum(p["junk_tokens"] for p in pages.values())
                / max(1, sum(p["tokens"] for p in pages.values())),
                4,
            ),
        }
        if scored:
            agg["gold_pages"] = len(scored)
            agg["cer"] = round(sum(p["cer"] for p in scored) / len(scored), 4)
            agg["wer"] = round(sum(p["wer"] for p in scored) / len(scored), 4)
            agg["iast_recall"] = round(
                sum(p["gold_iast_chars"] * p["iast_recall"] for p in scored)
                / max(1, sum(p["gold_iast_chars"] for p in scored)),
                4,
            )
        if eng in timings:
            agg["sec_per_page"] = timings[eng]["sec_per_page"]
            agg["total_s"] = timings[eng]["total_s"]
        report["engines"][eng] = {"aggregate": agg, "per_page": pages}

    if args.json:
        os.makedirs(os.path.dirname(args.json) or ".", exist_ok=True)
        with open(args.json, "w", encoding="utf-8", newline="\n") as fh:
            json.dump(report, fh, ensure_ascii=False, indent=1)
        print(f"-> {args.json}")

    hdr = f"{'engine':<18}{'chars':>9}{'IAST':>7}{'deva':>6}{'junk%':>8}{'CER':>8}{'WER':>8}{'IASTrec':>9}{'s/page':>9}"
    print(hdr)
    print("-" * len(hdr))
    for eng, d in report["engines"].items():
        a = d["aggregate"]
        print(
            f"{eng:<18}{a['chars']:>9,}{a['iast']:>7,}{a['deva']:>6,}"
            f"{a['junk_token_rate'] * 100:>7.2f}%"
            f"{a.get('cer', float('nan')):>8.4f}{a.get('wer', float('nan')):>8.4f}"
            f"{a.get('iast_recall', float('nan')):>9.4f}{a.get('sec_per_page', float('nan')):>9.2f}"
        )
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    r = sub.add_parser("render")
    r.add_argument("--pdf", required=True)
    r.add_argument("--out", required=True)
    r.add_argument("--dpi", type=int, default=300)
    r.set_defaults(fn=cmd_render)

    x = sub.add_parser("run")
    x.add_argument("--pdf", required=True)
    x.add_argument("--out", required=True)
    x.add_argument("--dpi", type=int, default=300)
    x.add_argument("--engines", default="embedded,pdfminer,tesseract-eng,tesseract-engsan")
    x.set_defaults(fn=cmd_run)

    s = sub.add_parser("score")
    s.add_argument("--out", required=True)
    s.add_argument("--gold", help="directory of gold p####.txt files")
    s.add_argument("--json")
    s.set_defaults(fn=cmd_score)

    args = ap.parse_args()
    return args.fn(args)


if __name__ == "__main__":
    raise SystemExit(main())

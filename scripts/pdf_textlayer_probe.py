#!/usr/bin/env python3
"""Is there a text layer, and is it clean? — the H2832 pre-OCR gate.

The H370 lesson (docs/SUNDARA_OCR_PHASE2_SUPERSEDED.md): never start an OCR
bake-off before proving that no cheaper source exists. For a PDF the cheapest
source is its own embedded text layer, so this probes it first:

  * page count, per-page extracted character count
  * embedded fonts (a scan-only PDF has none; an OCR'd scan usually has one
    synthetic font such as `GlyphLessFont`)
  * image inventory per page (a pure scan = 1 full-page image, no text)
  * a diacritics census over the extracted text — the Goldman volumes are
    dense IAST (ā ī ū ṛ ṝ ḷ ṅ ñ ṭ ḍ ṇ ś ṣ ṃ ḥ), which is exactly what a bad
    OCR pass destroys, so its presence/absence is the single best signal
  * Devanagari codepoint census (U+0900–U+097F)

Usage
-----
    python scripts/pdf_textlayer_probe.py <file.pdf> [--pages 1-40] [--json out.json]
    python scripts/pdf_textlayer_probe.py <file.pdf> --dump-page 500

Read-only. Writes only where --json points.
"""

from __future__ import annotations

import argparse
import json
import statistics
import sys
import unicodedata

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

try:
    import fitz  # PyMuPDF
except ImportError:  # pragma: no cover
    print("needs PyMuPDF:  pip install pymupdf", file=sys.stderr)
    raise SystemExit(2)

# The IAST inventory a Sanskritist actually cares about losing.
IAST = "āĀīĪūŪṛṚṝṜḷḶḹḸṅṄñÑṭṬḍḌṇṆśŚṣṢṃṂḥḤēēōṁ"
DEVA = range(0x0900, 0x0980)


def parse_pages(spec: str | None, n: int) -> list[int]:
    if not spec:
        return list(range(n))
    out: list[int] = []
    for part in spec.split(","):
        part = part.strip()
        if "-" in part:
            a, b = part.split("-", 1)
            out.extend(range(int(a) - 1, int(b)))
        else:
            out.append(int(part) - 1)
    return [p for p in out if 0 <= p < n]


def probe(path: str, pages_spec: str | None) -> dict:
    doc = fitz.open(path)
    pages = parse_pages(pages_spec, doc.page_count)

    fonts: dict[str, int] = {}
    per_page = []
    iast_total = 0
    deva_total = 0
    ctrl_total = 0
    chars_total = 0
    repl_total = 0

    for pno in pages:
        page = doc.load_page(pno)
        text = page.get_text("text")
        chars = len(text)
        chars_total += chars
        iast = sum(1 for c in text if c in IAST)
        deva = sum(1 for c in text if ord(c) in DEVA)
        repl = text.count("�")
        ctrl = sum(1 for c in text if unicodedata.category(c) == "Cc" and c not in "\n\r\t")
        iast_total += iast
        deva_total += deva
        ctrl_total += ctrl
        repl_total += repl
        for f in page.get_fonts(full=True):
            name = f[3] or "?"
            fonts[name] = fonts.get(name, 0) + 1
        per_page.append(
            {
                "page": pno + 1,
                "chars": chars,
                "iast": iast,
                "deva": deva,
                "replacement": repl,
                "images": len(page.get_images(full=True)),
            }
        )

    counts = [p["chars"] for p in per_page]
    empty = [p["page"] for p in per_page if p["chars"] < 20]
    imageonly = [p["page"] for p in per_page if p["chars"] < 20 and p["images"] > 0]

    return {
        "file": path,
        "page_count": doc.page_count,
        "pages_probed": len(pages),
        "metadata": {k: v for k, v in (doc.metadata or {}).items() if v},
        "fonts": dict(sorted(fonts.items(), key=lambda kv: -kv[1])),
        "font_count": len(fonts),
        "chars_total": chars_total,
        "chars_median_per_page": statistics.median(counts) if counts else 0,
        "iast_chars": iast_total,
        "devanagari_chars": deva_total,
        "replacement_chars": repl_total,
        "control_chars": ctrl_total,
        "empty_pages": empty[:50],
        "empty_page_count": len(empty),
        "image_only_pages": imageonly[:50],
        "toc_entries": len(doc.get_toc() or []),
        "per_page": per_page,
    }


def verdict(rep: dict) -> str:
    if rep["chars_total"] < 200 * rep["pages_probed"] / 10:
        return "NO TEXT LAYER — scan only; OCR bake-off is warranted"
    synthetic = any("glyphless" in f.lower() for f in rep["fonts"])
    if synthetic:
        return "OCR'd TEXT LAYER (synthetic font) — verify quality before trusting"
    if rep["iast_chars"] == 0:
        return "TEXT LAYER PRESENT but ZERO IAST diacritics — suspect a lossy/mojibake layer"
    return "BORN-DIGITAL / CLEAN TEXT LAYER — extract directly, no OCR needed"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("pdf")
    ap.add_argument("--pages", help="1-based page spec, e.g. 1-40,500,900-910")
    ap.add_argument("--json", help="write the full report here")
    ap.add_argument("--dump-page", type=int, help="print the raw text of this 1-based page")
    args = ap.parse_args()

    if args.dump_page:
        doc = fitz.open(args.pdf)
        print(doc.load_page(args.dump_page - 1).get_text("text"))
        return 0

    rep = probe(args.pdf, args.pages)
    rep["verdict"] = verdict(rep)
    if args.json:
        with open(args.json, "w", encoding="utf-8") as fh:
            json.dump(rep, fh, ensure_ascii=False, indent=1)
    print(f"file            : {rep['file']}")
    print(f"pages           : {rep['page_count']}  (probed {rep['pages_probed']})")
    print(f"producer        : {rep['metadata'].get('producer', '?')}")
    print(f"fonts           : {rep['font_count']} -> {list(rep['fonts'])[:8]}")
    print(f"chars total     : {rep['chars_total']:,}  median/page {rep['chars_median_per_page']:,}")
    print(f"IAST diacritics : {rep['iast_chars']:,}")
    print(f"Devanagari      : {rep['devanagari_chars']:,}")
    print(f"U+FFFD          : {rep['replacement_chars']:,}")
    print(f"empty pages     : {rep['empty_page_count']}  image-only {len(rep['image_only_pages'])}")
    print(f"TOC entries     : {rep['toc_entries']}")
    print(f"VERDICT         : {rep['verdict']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Offset-corrected collation of Goldman's sarga-1 notes against our apparatus.

H2832, step 5 — the *repair* of `goldman_apparatus_collate.py`.

The naive collation joins on the bare verse number and is wrong. Goldman &
Goldman translate the **Baroda critical edition**; our text and apparatus follow
the southern/vulgate numbering of the Gita Supersite scrape. The two series slip
apart wherever the critical editors relegated lines to star passages, and they
never resynchronise: `goldman_verse_offset_measure.py` measured the drift on 19
lemma anchors and found it growing monotonically from +1 near the head of the
sarga to +21 by verse 183. A join on `verse N` therefore compares different
verses, more badly the further into the sarga it goes.

This script rebuilds the join through a **monotone step map** interpolated from
those anchors, and labels every row with how far it sits from the nearest anchor
so a reader can tell a measured alignment from a carried-forward guess.

    python scripts/goldman_apparatus_collate_aligned.py \
        --apparatus data/apparatus/sarga_01_kostina.json \
        --offsets data/goldman/offset_sarga01.json \
        --goldman-dir <scratch>/sarga01_notes_ocr \
        --json data/goldman/collate_sarga01_aligned.json

`--goldman-dir` must point OUTSIDE the repo: the extracted text of a
copyrighted Princeton volume is working material and is never committed.
"""

from __future__ import annotations

import argparse
import bisect
import glob
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

# Same note-head grammar as the naive collator: a verse number, optionally a
# span, a full stop, then the head. The OCR renders a line-initial `1` as `I`
# or `l` often enough that the first digit has to admit them.
NOTE_HEAD = re.compile(r'(?m)^[ \t]*([IlJ1-9]\d{0,2})(?:-(\d{1,3}))?\.\s+(\S.{0,88})')
_QUOTED = re.compile(r'["“]([^"”]{1,90})["”]')
_OCR_ONE = str.maketrans({"I": "1", "l": "1", "J": "1"})

# Anchor-distance bands. An anchor is a note whose transliterated lemma was
# located verbatim inside one of our verses, so the mapping at that point is
# measured, not inferred.
NEAR = 2      # <= this many verses from an anchor -> "measured"
MID = 8       # <= this many -> "interpolated"; beyond -> "carried"


def load_anchors(path: str) -> list[tuple[int, int]]:
    with open(path, encoding="utf-8") as fh:
        doc = json.load(fh)
    seen: dict[int, int] = {}
    for m in doc.get("matches", []):
        seen[int(m["goldman_verse"])] = int(m["offset"])
    anchors = sorted(seen.items())
    # The drift is physically monotone (star passages are only ever inserted),
    # so an anchor that would lower the running offset is an extraction
    # accident, not a fact about the text. Drop it rather than smooth it.
    kept: list[tuple[int, int]] = []
    for v, off in anchors:
        if kept and off < kept[-1][1]:
            continue
        kept.append((v, off))
    return kept


def make_map(anchors: list[tuple[int, int]]):
    """Return (map_fn, band_fn) over Goldman verse numbers."""
    xs = [v for v, _ in anchors]
    ys = [o for _, o in anchors]

    def offset(n: int) -> int:
        if not xs:
            return 0
        i = bisect.bisect_right(xs, n) - 1
        if i < 0:
            return ys[0]
        if i >= len(xs) - 1:
            return ys[-1]
        # linear interpolation between the bracketing anchors, floored: a
        # half-verse of drift is not a thing.
        x0, x1, y0, y1 = xs[i], xs[i + 1], ys[i], ys[i + 1]
        if y0 == y1 or x1 == x0:
            return y0
        return y0 + int(round((y1 - y0) * (n - x0) / (x1 - x0)))

    def band(n: int) -> str:
        if not xs:
            return "unanchored"
        d = min(abs(n - x) for x in xs)
        if d <= NEAR:
            return "measured"
        if d <= MID:
            return "interpolated"
        return "carried"

    return offset, band


def load_apparatus(path: str) -> tuple[dict[int, list[dict]], dict]:
    with open(path, encoding="utf-8") as fh:
        doc = json.load(fh)
    out: dict[int, list[dict]] = {}
    for v in doc.get("verses", []):
        key = str(v.get("verse") or "")
        if not key.isdigit():
            continue
        notes = [n for n in (v.get("notes") or []) if isinstance(n, dict)]
        if notes:
            out.setdefault(int(key), []).extend(notes)
    return out, doc.get("_meta", {})


def note_label(n: dict) -> str:
    lemma = n.get("lemma_iast") or ""
    head = (n.get("note_ru") or n.get("text") or "").split("—")[0].strip()
    return f"[{n.get('layer', '?')}] {lemma or head[:60]}"


def load_goldman(directory: str) -> dict[int, list[str]]:
    out: dict[int, list[str]] = {}
    for path in sorted(glob.glob(os.path.join(directory, "p*.txt"))):
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        for num, _span, head in NOTE_HEAD.findall(text):
            n = num.translate(_OCR_ONE).lstrip("0") or "0"
            if not n.isdigit() or not 1 <= int(n) <= 250:
                continue
            q = _QUOTED.search(head)
            out.setdefault(int(n), []).append((q.group(1) if q else head).strip())
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apparatus", required=True)
    ap.add_argument("--offsets", required=True)
    ap.add_argument("--goldman-dir", required=True)
    ap.add_argument("--json")
    args = ap.parse_args()

    anchors = load_anchors(args.offsets)
    offset, band = make_map(anchors)
    ours, meta = load_apparatus(args.apparatus)
    theirs = load_goldman(args.goldman_dir)

    rows = []
    for g in sorted(theirs):
        off = offset(g)
        mapped = g + off
        our_notes = ours.get(mapped, [])
        rows.append(
            {
                "goldman_verse": g,
                "offset": off,
                "our_verse": mapped,
                "band": band(g),
                "goldman_heads": theirs[g],
                "our_notes": [note_label(n) for n in our_notes],
                "ours": len(our_notes),
            }
        )

    covered = {r["our_verse"] for r in rows}
    only_ours = sorted(v for v in ours if v not in covered)

    both = [r for r in rows if r["ours"]]
    only_g = [r for r in rows if not r["ours"]]
    by_band: dict[str, dict[str, int]] = {}
    for r in rows:
        b = by_band.setdefault(r["band"], {"rows": 0, "with_our_note": 0})
        b["rows"] += 1
        b["with_our_note"] += 1 if r["ours"] else 0

    naive_hits = sum(1 for r in rows if ours.get(r["goldman_verse"]))
    report = {
        "apparatus": args.apparatus,
        "numbering_ours": meta.get("numbering", "?"),
        "numbering_goldman": "Baroda critical edition (Princeton translation)",
        "anchors": [{"goldman_verse": v, "offset": o} for v, o in anchors],
        "anchor_count": len(anchors),
        "our_note_count": sum(len(v) for v in ours.values()),
        "our_verses_with_notes": len(ours),
        "goldman_verses_with_notes": len(theirs),
        "goldman_note_count": sum(len(v) for v in theirs.values()),
        "both": len(both),
        "only_goldman": [r["goldman_verse"] for r in only_g],
        "only_ours": only_ours,
        "by_band": by_band,
        "naive_join_hits": naive_hits,
        "aligned_join_hits": len(both),
        "rows": rows,
    }
    if args.json:
        os.makedirs(os.path.dirname(args.json) or ".", exist_ok=True)
        with open(args.json, "w", encoding="utf-8", newline="\n") as fh:
            json.dump(report, fh, ensure_ascii=False, indent=1)
        print(f"-> {args.json}")

    print(f"anchors            : {len(anchors)}  (offset {anchors[0][1]:+d} .. {anchors[-1][1]:+d})")
    print(f"ours               : {report['our_note_count']} notes over {report['our_verses_with_notes']} verses")
    print(f"goldman            : {report['goldman_note_count']} notes over {report['goldman_verses_with_notes']} verses")
    print(f"aligned join hits  : {len(both)}   (naive verse-number join would give {naive_hits})")
    print(f"only Goldman       : {len(only_g)}   only ours: {len(only_ours)}")
    for b, d in sorted(by_band.items()):
        print(f"  band {b:<13} rows {d['rows']:>3}  with our note {d['with_our_note']:>3}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Collate the Goldman/Princeton notes to Sundarakāṇḍa sarga 1 against our own
apparatus (`data/apparatus/sarga_01_kostina.json`) — H2832 step 5.

The join key is the **verse number**. Goldman's notes are keyed by verse with a
lemma in italics; our apparatus is keyed by verse with a Russian note. This
script does the mechanical half:

  * dump our apparatus as `verse -> [note titles]`
  * extract Goldman's note headwords per verse from an extracted-text file
    (one PDF page per file, as produced by the bake-off harness)
  * emit the coverage join: verses where both have a note, where only Goldman
    does, where only we do

The *judgement* half — whether two notes on the same verse actually say the same
thing — is not automatable and is done by the session model reading both.

    python scripts/goldman_apparatus_collate.py --apparatus data/apparatus/sarga_01_kostina.json
    python scripts/goldman_apparatus_collate.py --apparatus ... --goldman-dir DIR --json out.json

`--goldman-dir` must point OUTSIDE the repo: the extracted text of a
copyrighted volume is working material, never committed.
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

# Goldman's note heads are verse-numbered: `6. "great serpents" nāga- (…)` — but
# a fair number carry no quoted lemma at all (`37. The verse does not lend
# itself…`) and some cover a verse span (`1-2.`). Requiring the quote undercounts
# by roughly half, so match the number and keep whatever follows as the head.
# The OCR layer renders a line-initial `1` as `I` about as often as not, so the
# first character of the number is allowed to be `I` or `l` too.
NOTE_HEAD = re.compile(r'(?m)^[ \t]*([IlJ1-9]\d{0,2})(?:-\d{1,3})?\.\s+(\S.{0,88})')
_QUOTED = re.compile(r'["“]([^"”]{1,90})["”]')
_OCR_ONE = str.maketrans({"I": "1", "l": "1", "J": "1"})


def load_apparatus(path: str) -> dict[str, list[dict]]:
    with open(path, encoding="utf-8") as fh:
        doc = json.load(fh)
    out: dict[str, list[dict]] = {}
    for v in doc.get("verses", []):
        key = str(v.get("verse") or v.get("verse_id") or "?")
        notes = [n for n in (v.get("notes") or []) if isinstance(n, dict)]
        if notes:
            out.setdefault(key, []).extend(notes)
    return out


def note_label(n: dict) -> str:
    """One-line identity for one of our notes: layer + lemma (or note head)."""
    lemma = n.get("lemma_iast") or ""
    head = (n.get("note_ru") or n.get("text") or "").split("—")[0].strip()
    return f"[{n.get('layer', '?')}] {lemma or head[:60]}"


def load_goldman(directory: str) -> dict[str, list[str]]:
    out: dict[str, list[str]] = {}
    for path in sorted(glob.glob(os.path.join(directory, "*.txt"))):
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        for num, head in NOTE_HEAD.findall(text):
            verse = num.translate(_OCR_ONE).lstrip("0") or "0"
            if not verse.isdigit() or int(verse) > 250:   # not a verse number
                continue
            q = _QUOTED.search(head)
            out.setdefault(verse, []).append((q.group(1) if q else head).strip())
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--apparatus", required=True)
    ap.add_argument("--goldman-dir", help="directory of per-page extracted .txt")
    ap.add_argument("--json", help="write the join here")
    args = ap.parse_args()

    ours = load_apparatus(args.apparatus)
    theirs = load_goldman(args.goldman_dir) if args.goldman_dir else {}

    keys = sorted(set(ours) | set(theirs), key=lambda k: (not k.isdigit(), int(k) if k.isdigit() else 0, k))
    rows = []
    for k in keys:
        rows.append(
            {
                "verse": k,
                "ours": len(ours.get(k, [])),
                "goldman": len(theirs.get(k, [])),
                "goldman_lemmas": theirs.get(k, []),
                "our_notes": [note_label(n) for n in ours.get(k, [])],
            }
        )

    both = [r for r in rows if r["ours"] and r["goldman"]]
    only_g = [r for r in rows if r["goldman"] and not r["ours"]]
    only_o = [r for r in rows if r["ours"] and not r["goldman"]]

    report = {
        "apparatus": args.apparatus,
        "our_verses_with_notes": len(ours),
        "our_note_count": sum(len(v) for v in ours.values()),
        "goldman_verses_with_notes": len(theirs),
        "goldman_note_count": sum(len(v) for v in theirs.values()),
        "both": len(both),
        "only_goldman": [r["verse"] for r in only_g],
        "only_ours": [r["verse"] for r in only_o],
        "rows": rows,
    }
    if args.json:
        os.makedirs(os.path.dirname(args.json) or ".", exist_ok=True)
        with open(args.json, "w", encoding="utf-8", newline="\n") as fh:
            json.dump(report, fh, ensure_ascii=False, indent=1)
        print(f"-> {args.json}")

    print(f"ours    : {report['our_note_count']} notes over {report['our_verses_with_notes']} verses")
    print(f"goldman : {report['goldman_note_count']} notes over {report['goldman_verses_with_notes']} verses")
    print(f"both    : {report['both']} verses · only-Goldman {len(only_g)} · only-ours {len(only_o)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

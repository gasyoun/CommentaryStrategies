#!/usr/bin/env python3
"""Digitize Leonov/Kostina's OWN Sundarakāṇḍa apparatus from the source HTML.

This is the tier-1 (print) note layer of model II — the ~36 % density benchmark
and the correct dedup baseline for the Phase-2 commentator layer. The source is
`ramayana-leonov/Рамаяна. Книга 5. Сундараканда 2026.html`, where each verse is a
`<div class="citation_block" id="S.V">` and its notes are `comment_item`s inside.

Output: data/leonov_own_notes.json  — one record per note, keyed to verse "5.S.V".
Deterministic, stdlib-only (html.parser).

Usage: python scripts/extract_leonov_notes.py
"""
import sys
import os
import re
import json
from html.parser import HTMLParser

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
SRC = os.path.join(REPO, "ramayana-leonov", "Рамаяна. Книга 5. Сундараканда 2026.html")
OUT = os.path.join(REPO, "data", "leonov_own_notes.json")

VOID = {"br", "img", "hr", "meta", "input", "link"}
IAST = set("āĀīĪūŪṛṚṝṭṬḍḌṇṆśŚṣṢṃṂḥḤñṅḷēō")


def has_iast(s):
    return any(c in IAST for c in s)


def editor_of(text):
    if "Костина" in text or "Костиной" in text:
        return "kostina"
    if "Леонов" in text or "Леонова" in text:
        return "leonov"
    return None


class Parser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.verse = None
        self.cap = False
        self.depth = 0
        self.buf = []
        self.cur_id = None
        self.notes = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        cls = a.get("class", "")
        if tag == "div" and "citation_block" in cls:
            self.verse = a.get("id")  # "S.V"
        if not self.cap and "comment_text" in cls:
            self.cap = True
            self.depth = 1
            self.buf = []
            return
        if self.cap and tag not in VOID:
            self.depth += 1

    def handle_startendtag(self, tag, attrs):
        pass  # void self-closing; ignore for depth

    def handle_endtag(self, tag):
        if self.cap and tag not in VOID:
            self.depth -= 1
            if self.depth == 0:
                text = re.sub(r"\s+", " ", "".join(self.buf)).strip()
                if text and self.verse:
                    self.notes.append((self.verse, self.cur_id, text))
                self.cap = False

    def handle_data(self, data):
        if self.cap:
            self.buf.append(data)


def main():
    if not os.path.exists(SRC):
        sys.stderr.write(f"ERROR: source not found: {SRC}\n")
        sys.exit(1)
    html = open(SRC, encoding="utf-8", errors="replace").read()
    # tag each comment_item id so we can carry it (parser sees class not id order easily)
    # simplest: capture ids in document order and zip — comment_item ids appear right before comment_text
    ids = re.findall(r'class="comment_item" id="([^"]+)"', html)

    p = Parser()
    p.feed(html)
    notes = p.notes
    # align ids by order (both are in document order, 1:1 with comment_text blocks)
    records = []
    for i, (verse, _cid, text) in enumerate(notes):
        m = re.match(r"(\d+)\.(\d+)", verse or "")
        if not m:
            continue
        s, v = int(m.group(1)), int(m.group(2))
        records.append({
            "verse_id": f"5.{s}.{v}",
            "sarga": s,
            "verse": v,
            "comment_id": ids[i] if i < len(ids) else None,
            "editor": editor_of(text),
            "raw_text": text,
            "char_count": len(text),
            "has_iast": has_iast(text),
        })

    from collections import Counter
    by_sarga = Counter(r["sarga"] for r in records)
    payload = {
        "_meta": {
            "generated_by": "scripts/extract_leonov_notes.py",
            "source": "ramayana-leonov/Рамаяна. Книга 5. Сундараканда 2026.html",
            "layer": "Leonov/Kostina OWN apparatus — model II tier-1 (print), the ~36% density benchmark",
            "total_notes": len(records),
            "sargas_covered": len(by_sarga),
            "verses_with_note": len({r["verse_id"] for r in records}),
            "by_editor": dict(Counter(r["editor"] for r in records)),
            "note": "Dedup baseline for Phase-2: a commentator note that duplicates a Leonov/Kostina note "
                    "on the same verse+point should be rejected or merged.",
        },
        "notes": records,
    }
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, ensure_ascii=False, indent=2)

    print(f"extracted {len(records)} Leonov/Kostina notes -> {OUT}")
    print("by editor:", payload["_meta"]["by_editor"])
    print("sarga 35 notes:", by_sarga.get(35), "| verses covered book-wide:",
          payload["_meta"]["verses_with_note"])


if __name__ == "__main__":
    main()

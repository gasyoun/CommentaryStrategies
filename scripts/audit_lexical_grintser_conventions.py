"""Audit sarga-1 lexical notes against the Grintser conventions (H2833).

Scans data/lexical/ch1.json + the lexical-subtype entries of
data/sundara_ch1_commentary_to_add.json for violations of the conventions
derived by scripts/profile_grintser_note_style.py (documented in
docs/LEXICAL_NOTE_STYLE_GRINTSER_2026.md): lemma repetition, inline
dictionary citations, «X + Y» morpheme sums, «Букв.» case/position/colon,
' = ' equations, exclamations, dangling editorial residue.

Run: python scripts/audit_lexical_grintser_conventions.py [--chapter N]
"""

import argparse
import json
import re
import sys
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

IAST_WORD = r"[a-zA-Zāīūṛṝḷḹṅñṭḍṇśṣṃḥ]+"


def lexical_cards(chapter):
    cards = []
    with open(f"data/lexical/ch{chapter}.json", encoding="utf-8") as f:
        for c in json.load(f):
            if "_meta" in c:
                continue
            v = (c.get("judge") or {}).get("verdict", "keep")
            cards.append((f"ch{chapter}.json", c.get("shloka"), c.get("lemma_iast"), c.get("note_ru", ""), v))
    with open(f"data/sundara_ch{chapter}_commentary_to_add.json", encoding="utf-8") as f:
        for c in json.load(f):
            if isinstance(c, dict) and c.get("subtype") == "lexical":
                cards.append((f"sundara_ch{chapter}_commentary_to_add.json", c.get("shloka"), c.get("lemma_iast"), c.get("note_ru", "") or c.get("note", ""), "-"))
    return cards


def audit(cards):
    stats = Counter()
    per_card = []
    for src, shloka, lemma, text, verdict in cards:
        probs = []
        toks = [w.lower() for w in re.findall(r"\b({0})\b".format(IAST_WORD), text) if len(w) > 3]
        counts = Counter(toks)
        lem = (lemma or "").lower()
        if lem and counts.get(lem, 0) >= 2:
            probs.append(f"lemma×{counts[lem]}")
        if re.search(r"\b(MW|Apte|PW|Monier|Kocherginа|Кочергина)\b", text):
            probs.append("inline-dict")
        if " + " in text:
            probs.append("plus-sum")
        if re.search(r"—\s*Букв\.", text) is None and re.search(r"\bБукв\.", text):
            probs.append("Букв-not-after-dash")
        if re.search(r"[Бб]укв\.(?!:)", text):
            probs.append("букв-no-colon")
        if re.search(r"\S = \S", text):
            probs.append("equation")
        if "!" in text:
            probs.append("exclam")
        if "Парадокс" in text:
            probs.append("paradox")
        if re.search(r"уточнить|TODO|\?\?", text):
            probs.append("dangling")
        if re.search(r"В подстрочнике", text):
            probs.append("podstr-meta")
        for p in probs:
            stats[p] += 1
        per_card.append((src, shloka, lemma, verdict, probs))
    return stats, per_card


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--chapter", type=int, default=1)
    ap.add_argument("--verbose", action="store_true")
    args = ap.parse_args()
    cards = lexical_cards(args.chapter)
    stats, per_card = audit(cards)
    print(f"Cards scanned: {len(cards)}")
    for k, v in stats.most_common():
        print(f"  {k}: {v}")
    clean = sum(1 for *_, p in per_card if not p)
    print(f"  clean: {clean}")
    if args.verbose:
        for src, shloka, lemma, verdict, probs in per_card:
            if probs:
                print(f"  {shloka:<10} {lemma or '-':<28} [{verdict}] {', '.join(probs)}  ({src})")


if __name__ == "__main__":
    main()

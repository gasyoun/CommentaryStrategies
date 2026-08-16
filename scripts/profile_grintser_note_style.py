"""Profile Grintser's lexical-note conventions from the verbatim corpus (H2833).

Counts the formal conventions of P. A. Grintser's verse notes (Rāmāyaṇa I–III,
seg comm1..comm4 in the SamudraManthanam corpus) and his glossary
(slovar-grintsera-iz-ramayany-1-2.jsonl): lemma repetition in the opener,
«Букв.»/«букв.» case and position, compound hyphenation, inline dictionary
citations, cross-reference form, register markers. The numbers feed
docs/LEXICAL_NOTE_STYLE_GRINTSER_2026.md — conventions are derived from these
counts, never assigned from taste.

Run: python scripts/profile_grintser_note_style.py
"""

import json
import re
import sys
from collections import Counter
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

CORPUS = Path(r"C:\Users\user\Documents\GitHub\SamudraManthanam\web\corpus_builder\jsonl")
BOOKS = [
    "01_ramayana-balakanda.jsonl",
    "02_ramayana-ayodhyakanda.jsonl",
    "03_ramayana-aranyakanda.jsonl",
]
SLOVAR = "slovar-grintsera-iz-ramayany-1-2.jsonl"

IAST_WORD = r"[a-zA-Zāīūṛṝḷḹṅñṭḍṇśṣṃḥ]+"


def load_notes():
    notes = []
    for name in BOOKS:
        with open(CORPUS / name, encoding="utf-8") as f:
            for line in f:
                j = json.loads(line)
                if j.get("seg", "").startswith("comm") and j.get("text"):
                    notes.append((name.split("_")[0], j["passage"], j["text"]))
    return notes


def load_slovar():
    entries = []
    with open(CORPUS / SLOVAR, encoding="utf-8") as f:
        for line in f:
            j = json.loads(line)
            if j.get("text"):
                entries.append(j["text"])
    return entries


def main():
    notes = load_notes()
    slovar = load_slovar()
    texts = [t for _, _, t in notes]
    print(f"Corpus: {len(notes)} verse notes (books I–III) + {len(slovar)} glossary entries")

    # 1. Lemma repetition: within one note, how often does the same IAST token recur?
    rep2 = rep3 = with_iast = 0
    for t in texts:
        toks = [w.lower() for w in re.findall(r"\(({0}(?:[- ]{0})*)\)".format(IAST_WORD), t)]
        if not toks:
            continue
        with_iast += 1
        counts = Counter(toks)
        if any(c >= 2 for c in counts.values()):
            rep2 += 1
        if any(c >= 3 for c in counts.values()):
            rep3 += 1
    print(f"\n[1] Notes with parenthesized IAST: {with_iast}")
    print(f"    same IAST form twice in one note:  {rep2}")
    print(f"    same IAST form three+ times:       {rep3}")

    # 2. «Букв.» — case, punctuation, position.
    cap = sum(t.count("Букв.:") for t in texts)
    cap_nocolon = sum(len(re.findall(r"Букв\.(?!:)", t)) for t in texts)
    low = sum(len(re.findall(r"(?<![А-ЯЁ])букв\.", t)) for t in texts)
    # position: does «Букв.:» come immediately after the closing paren + dash?
    right_after = sum(len(re.findall(r"\)\.{0,3}\s*—\s*Букв\.:", t)) for t in texts)
    print(f"\n[2] «Букв.:» (capitalized, with colon): {cap}")
    print(f"    «Букв.» without colon:              {cap_nocolon}")
    print(f"    «букв.» lowercase:                  {low}")
    print(f"    «Букв.:» directly after (iast) —    {right_after}")

    # 3. Hyphenation of compounds / stems.
    hyph_compound = sum(len(re.findall(r"\({0}(?:-{0})+".format(IAST_WORD), t)) for t in texts)
    plus_split = sum(t.count(" + ") for t in texts)
    trailing_stem = sum(len(re.findall(r"«{0}-»".format(IAST_WORD), t)) for t in texts)
    print(f"\n[3] Hyphenated compounds inside (…): {hyph_compound}")
    print(f"    «stem-» trailing-hyphen citations:  {trailing_stem}")
    print(f"    ' + ' morpheme-sum decompositions:  {plus_split}")

    # 4. Inline dictionary citations.
    for pat in ("MW", "Apte", "Monier", "PW"):
        n = sum(len(re.findall(r"\b{0}\b".format(pat), t)) for t in texts)
        print(f"[4] inline '{pat}': {n}" if pat == "MW" else f"    inline '{pat}': {n}")

    # 5. Cross-reference form.
    sm = sum(len(re.findall(r"[Сс]м\. примеч\. к [IVX]+\. \d", t)) for t in texts)
    sm_loose = sum(len(re.findall(r"[Сс]м\. примеч", t)) for t in texts)
    print(f"\n[5] «см. примеч. к <кн>. <песнь>. <стих>»: {sm} (of {sm_loose} см.-примеч. refs)")

    # 6. Register markers.
    excl = sum(t.count("!") for t in texts)
    paradox = sum(t.count("Парадокс") for t in texts)
    eq = sum(len(re.findall(r"\S = \S", t)) for t in texts)
    print(f"\n[6] '!' in notes: {excl} · «Парадокс»: {paradox} · ' = ' equations: {eq}")

    # 7. Opener shape: «...цитата (iast)... —» at note start (after the verse number).
    opener = sum(
        1
        for t in texts
        if re.match(r"^\d+[a-d]?\.\s*(\.\.\.|…)?[^()]{1,80}\(" + IAST_WORD, t)
    )
    print(f"\n[7] Notes opening with quoted lemma + (iast): {opener} of {len(texts)}")

    # 8. Glossary entry shape: «Имя\t(IAST[ — «gloss»]) — определение».
    g_gloss = sum(1 for t in slovar if re.match(r"^[^\t]+\t\({0}".format(IAST_WORD), t))
    g_litgloss = sum(1 for t in slovar if re.search(r"\({0}[^)]*—\s*«".format(IAST_WORD), t))
    print(f"[8] Glossary entries «Имя (IAST) — …»: {g_gloss} of {len(slovar)}; with inline «…» literal gloss: {g_litgloss}")

    # Feminine agreement spot-list: notes containing «имеющий/имеющая» near an -ā/-ī stem.
    fem = [t[:120] for t in texts if re.search(r"имеющ(ий|ая|ее)", t)]
    print(f"\n[9] notes using «имеющий/-ая/-ее» (manual gender check): {len(fem)}")
    for s in fem[:6]:
        print("   ·", s)


if __name__ == "__main__":
    main()

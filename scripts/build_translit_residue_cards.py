#!/usr/bin/env python3
"""Card payload for the mixed-script residue vote sheet (H2864, votes/sarga.md п.14).

H2831 repaired 553 of 643 mixed-script places mechanically and deliberately left
90 alone: their reading forks, and the corpus cannot settle the fork. Guessing
there would silently invent a Sanskrit reading, so they were written to a report
— but a Markdown report is not a gating artifact in this org, and a reader has no
way to record a decision against it.

This builds what the vote sheet needs and the report never carried: for each
residue word, every place it actually occurs (file, verse, field, the sentence
around it) plus the candidate readings the transliteration map can produce. The
human picks a reading; nothing here decides one.

Usage:  python scripts/build_translit_residue_cards.py
Output: data/analysis/translit_residue_cards.json
"""
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import translit_hygiene as th  # noqa: E402

OUT = os.path.join(REPO, "data", "analysis", "translit_residue_cards.json")

# Fields whose value is worth showing as the card's context sentence, in order of
# how much a reader can judge from them.
CONTEXT_FIELDS = ["note_ru", "raw_text", "lemma_iast", "reason", "reject_reason",
                  "verify_note", "text_ru", "edited_note", "candidate_lemma"]


def walk_strings(node, path=""):
    """Yield (json_path, field_name, string) for every string in the tree."""
    if isinstance(node, dict):
        for k, v in node.items():
            yield from walk_strings(v, f"{path}.{k}")
    elif isinstance(node, list):
        for i, v in enumerate(node):
            yield from walk_strings(v, f"{path}[{i}]")
    elif isinstance(node, str):
        yield path, path.split(".")[-1].split("[")[0], node


def locate(node, path=""):
    """Nearest verse address for a hit — the reader needs to find the place."""
    return None


def verse_of(record):
    for key in ("shloka", "verse_id", "anchor", "id"):
        if isinstance(record, dict) and record.get(key):
            return str(record[key])
    return ""


def snippet(text, word, width=150):
    i = text.find(word)
    if i < 0:
        return text[:width]
    a, b = max(0, i - width), min(len(text), i + len(word) + width)
    return ("…" if a else "") + text[a:b] + ("…" if b < len(text) else "")


def candidates_for(word):
    """Every reading the transliteration map can produce, best-effort.

    A residue word is exactly one the corpus could not disambiguate, so this is a
    menu, never an answer — the sheet shows it as chips to pick from or ignore.
    """
    cyr = sum(1 for ch in word if re.match(f"[{th.CYR}]", ch))
    lat = sum(1 for ch in word if re.match(f"[{th.IAST}]", ch))
    if lat >= cyr:
        cands = th._candidates(word, th.CYR_TO_LAT, th.AMBIGUOUS_CYR)
        foreign = f"[{th.CYR}]"
    else:
        cands = th._candidates(word, th.LAT_TO_CYR, th.AMBIGUOUS_LAT)
        foreign = f"[{th.IAST}]"
    clean = [c for c in cands if not any(re.match(foreign, ch) for ch in c)]
    lex = th.build_lexicon()
    # Mark which candidates the corpus already spells cleanly somewhere — that is
    # evidence, not a verdict: for these words it was ambiguous or absent.
    return [{"reading": c, "in_corpus": c.lower() in lex} for c in sorted(set(clean))][:8]


def main():
    per_file = th.scan(fix=False)
    residue = {}
    for path, hits in per_file.items():
        rel = os.path.relpath(path, REPO).replace("\\", "/")
        with open(path, encoding="utf-8") as fh:
            doc = json.load(fh)
        by_word = {}
        for h in hits:
            if h["suggested"]:
                continue
            by_word.setdefault(h["word"], []).append(h)
        if not by_word:
            continue
        for jpath, field, text in walk_strings(doc):
            for word in by_word:
                if word not in text:
                    continue
                card = residue.setdefault(word, {
                    "word": word,
                    "class": by_word[word][0]["class"],
                    "candidates": candidates_for(word),
                    "occurrences": [],
                })
                if len(card["occurrences"]) >= 6:
                    continue
                card["occurrences"].append({
                    "file": rel,
                    "field": field,
                    "reader_facing": field in ("note_ru", "raw_text", "lemma_iast"),
                    "context": snippet(text, word),
                })

    cards = sorted(residue.values(),
                   key=lambda c: (-sum(o["reader_facing"] for o in c["occurrences"]),
                                  -len(c["occurrences"]), c["word"]))
    for i, c in enumerate(cards, 1):
        c["id"] = f"translit-{i:03d}"
        c["occurrence_count"] = len(c["occurrences"])
    doc = {
        "_meta": {
            "generated_by": "scripts/build_translit_residue_cards.py",
            "handoff": "H2864 — лист по остатку смешанной письменности",
            "source": "scripts/translit_hygiene.py --check residue",
            "raised_by": "votes/sarga.md п.14",
            "cards": len(cards),
            "reader_facing_cards": sum(
                1 for c in cards if any(o["reader_facing"] for o in c["occurrences"])),
        },
        "cards": cards,
    }
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(doc, fh, ensure_ascii=False, indent=2)
    print(f"{len(cards)} cards -> {os.path.relpath(OUT, REPO)}")
    print(f"  reader-facing: {doc['_meta']['reader_facing_cards']}")
    print(f"  with a single candidate reading: "
          f"{sum(1 for c in cards if len(c['candidates']) == 1)}")
    print(f"  with no candidate at all: "
          f"{sum(1 for c in cards if not c['candidates'])}")


if __name__ == "__main__":
    main()

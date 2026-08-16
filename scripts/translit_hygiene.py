#!/usr/bin/env python3
"""Transliteration hygiene for the Sundarakāṇḍa apparatus (H2831, votes/sarga.md п.14).

MG, reviewing the sarga-1 ballot, hit one instance —

    Эпитеты: saketakodDālakа и nālikera (кокосы) — что за мусор с транслитерацией?

— and it is not one instance. `saketakodDālakа` alone carries TWO defects: an
HK/SLP1 camelCase leak (`odDālaka` for `oddālaka`) and a Cyrillic «а» sitting
inside a Latin word. Scanning every note-bearing JSON turns up hundreds of the
same shape, invisible to the eye and to every string search that assumes one
script per word.

Three defect classes, deliberately separated by how safely they can be repaired:

  cyr-in-latin  a Cyrillic homoglyph inside a majority-Latin word — `raktа`,
                `prāvaraṇа`, `saketakodDālakа`.  AUTO-FIXABLE: the two glyphs are
                visually identical, so the intent is never in doubt.
  lat-in-cyr    a Latin homoglyph (or a bare macron vowel) inside a majority-
                Cyrillic word — `рāкшасов`, `члена`, `шāстра`.  AUTO-FIXABLE for
                the homoglyph set plus ā→а (Russian orthography has no macrons).
  camel         HK/SLP1 leakage into IAST — `vivIDadrumabhūṣitaṃ`,
                `ekaVeṇīdhārā`.  NOT auto-fixable in general: the correct reading
                has to be checked against the verse, so only the entries verified
                against `data/analysis/sundara_commentary_segmented.json` and
                listed in CAMEL_FIXES are repaired; the rest are reported.
  other         mixed-script with no safe mapping (`шāpopahata` → `śāpopahata`,
                `bою` → «бою»).  Report only — a guess here would silently invent
                a reading.

Usage:
    python scripts/translit_hygiene.py --check    # exit 1 if any defect remains
    python scripts/translit_hygiene.py --fix      # repair the safe classes
    python scripts/translit_hygiene.py --report data/analysis/translit_hygiene_report.md
"""
import argparse
import json
import os
import re
import sys
import glob
import collections

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
DATA = os.path.join(REPO, "data")

# Latin block used by IAST, including every diacritic letter the corpus uses.
IAST = "A-Za-zĀāĪīŪūṚṛṜṝḶḷḸḹṄṅÑñṬṭḌḍṆṇŚśṢṣḤḥṂṃḸḹṞṟ"
CYR = "А-Яа-яЁё"
WORD = re.compile(rf"[{IAST}{CYR}]+")

# The repair map is TRANSLITERATION, not visual shape. That distinction is the
# whole correctness argument here: Cyrillic «р» looks like Latin `p`, but every
# real instance in this corpus stands for `r` — `dhарmic` is `dharmic`, `niрvā`
# is `nirvā`, `Раghuvamsha` is `Raghuvamsha`. A visual map would have written
# `dhapmic` into 111 places and called it a fix.
CYR_TO_LAT = {"а": "a", "б": "b", "в": "v", "г": "g", "д": "d", "е": "e",
              "ж": "j", "з": "z", "и": "i", "к": "k", "л": "l", "м": "m",
              "н": "n", "о": "o", "п": "p", "р": "r", "т": "t", "у": "u",
              "ф": "f", "х": "h", "А": "A", "Б": "B", "В": "V", "Г": "G",
              "Д": "D", "Е": "E", "З": "Z", "И": "I", "К": "K", "Л": "L",
              "М": "M", "Н": "N", "О": "O", "П": "P", "Р": "R", "Т": "T",
              "У": "U", "Ф": "F", "Х": "H", "і": "i", "ј": "j"}
LAT_TO_CYR = {"a": "а", "b": "б", "d": "д", "e": "е", "f": "ф", "g": "г",
              "h": "х", "i": "и", "j": "ж", "k": "к", "l": "л", "m": "м",
              "n": "н", "o": "о", "p": "п", "r": "р", "t": "т", "u": "у",
              "v": "в", "z": "з", "A": "А", "B": "Б", "D": "Д", "E": "Е",
              "F": "Ф", "G": "Г", "H": "Х", "I": "И", "K": "К", "L": "Л",
              "M": "М", "N": "Н", "O": "О", "P": "П", "R": "Р", "T": "Т",
              "U": "У", "V": "В", "Z": "З",
              # Not a transliteration choice at all: Russian orthography has no
              # macron, so a macron vowel inside a Cyrillic word is always the
              # Latin key left behind by a dropped IME switch.
              "ā": "а", "Ā": "А", "ī": "и", "Ī": "И", "ū": "у", "Ū": "У"}

# Letters whose reading genuinely forks, so no fixed map can settle them:
#   с → `s` in `Кālidāса` (Kālidāsa) but `c` in `saṃcukoсa` (saṃcukoca)
#   c → `с` in «cлово» but `ц` in a word like «cарь»
#   y/у → `u` or `y`;  x/х → `h` or `x`
# These are resolved per-word against the corpus lexicon (see disambiguate);
# a word whose fork the lexicon cannot settle goes to the report, not the fixer.
AMBIGUOUS_CYR = {"с": ("s", "c"), "С": ("S", "C"), "у": ("u", "y"),
                 "У": ("U", "Y"), "х": ("h", "x"), "Х": ("H", "X"),
                 "ц": ("c", "ts"), "ы": ("y", "i")}
AMBIGUOUS_LAT = {"c": ("с", "ц"), "C": ("С", "Ц"), "y": ("у", "й"),
                 "Y": ("У", "Й"), "s": ("с", "з"), "S": ("С", "З"),
                 "x": ("х", "кс"), "X": ("Х", "Кс")}

# HK/SLP1 camelCase leaks whose correct IAST was read off the verse text in
# data/analysis/sundara_commentary_segmented.json. Each comment names the verse
# the reading was checked against — never extend this table from guesswork.
CAMEL_FIXES = {
    "vivIDadrumabhūṣitaṃ": "vividhadrumabhūṣitam",   # 5.1.204 vividhadrumabhūṣitam
    "saketakodDālak": "saketakoddālak",              # 5.1.211 saketakoddālakanālikele
    "meGhasaṃkāśaḥ": "meghasaṃkāśaḥ",                # 5.1.x meghasaṃkāśa-
    "ekaVeṇīdhārā": "ekaveṇīdharā",                  # 5.57.39 ekaveṇīdharā
    "ekaVeṇī": "ekaveṇī",                            # 5.57.39 ekaveṇī-
    "pratyanikeSu": "pratyanīkeṣu",                  # 5.20.20 pratyanīkeṣu
    "surasurAh": "surāsurāḥ",                        # 5.20.20 surāsurāḥ
}
CAMEL_RE = re.compile(rf"\b[a-zāīūṛṝḷḹṅñṭḍṇśṣḥṃ]{{2,}}[A-ZĀĪŪṚṜḶḸṄÑṬḌṆŚṢḤṂ][{IAST}]*")

# camelCase is a DEFECT only in reader-facing prose. The corpus also stores SLP1
# on purpose — `stem`, `source: dic_mw:sampAti`, `mw`, `apte` — where `sampAti`
# is the correct key, not junk; scanning those fields for camelCase turns 20 real
# defects into 2 368 false ones. Mixed-script checks still run everywhere.
CAMEL_FIELDS = {"note_ru", "lemma_iast", "raw_text", "candidate_lemma",
                "edited_note", "text_ru"}

# Declared exceptions — the h2864 vote settled everything else, so `--check` can
# gate CI. Each of these is deliberate, not tolerated:
#   ruH        `*bʰruH-`, a PIE root with a laryngeal — the mixing is normative
#   medъ       `*medъ`, Slavic with a yer — same
#   maharJayai quoted from Goldman p. 483 inside Kostina's own service note; the
#              reviewer deferred it («запись в санскрите невозможна, вероятно
#              ошибка транслитерации — переспросить Костину»), and a quotation is
#              not ours to silently correct
# Removing a row here is a claim that the word got fixed; the check will prove it.
DECLARED_EXCEPTIONS = {"ruH", "medъ", "maharJayai"}


def target_files():
    """Every note-bearing JSON that is a SOURCE of truth, not a build artifact.

    data/apparatus/* is regenerated from these by build_sarga_apparatus.py, so
    fixing it here would be fixing the shadow instead of the object.
    """
    pats = [
        os.path.join(DATA, "lexical", "ch*.json"),
        os.path.join(DATA, "crosstext", "*.json"),
        os.path.join(DATA, "analysis", "phase2_*", "*.json"),
        os.path.join(DATA, "edition_footnotes", "*.json"),
    ]
    files = []
    for p in pats:
        files.extend(glob.glob(p))
    files.append(os.path.join(DATA, "leonov_own_notes.json"))
    files.append(os.path.join(DATA, "sundara_commentary_to_add.json"))
    # `_`-prefixed crosstext files are raw mining indexes, not curated notes —
    # build_sarga_apparatus.py skips them for the same reason, and they never
    # reach a reader's eye.
    return sorted(f for f in set(files)
                  if os.path.exists(f) and "qa_removed" not in f
                  and not os.path.basename(f).startswith("_"))


LEXICON = set()          # single-script words the corpus already spells cleanly


def build_lexicon():
    """Every clean (single-script) word in the corpus, folded to lower case.

    This is what settles the ambiguous letters: `Кālidāса` has two readings,
    `Kālidāsa` and `Kālidāca`, and the corpus writes `kālidāsa` cleanly 40-odd
    times and `kālidāca` never. Evidence from the corpus itself beats any
    hand-picked preference, and when the corpus is silent the word is reported
    instead of guessed.
    """
    global LEXICON
    if LEXICON:
        return LEXICON
    for path in target_files():
        with open(path, encoding="utf-8") as fh:
            raw = fh.read()
        for w in WORD.findall(raw):
            cyr = any(re.match(f"[{CYR}]", ch) for ch in w)
            lat = any(re.match(f"[{IAST}]", ch) for ch in w)
            if cyr != lat and len(w) > 2:
                LEXICON.add(w.lower())
    return LEXICON


def _candidates(word, table, ambiguous):
    """All repairs of `word` under `table`, forking on every ambiguous letter."""
    outs = [""]
    for ch in word:
        if ch in ambiguous:
            outs = [o + alt for o in outs for alt in ambiguous[ch]]
        else:
            outs = [o + table.get(ch, ch) for o in outs]
        if len(outs) > 32:            # pathological fork count -> give up
            return []
    return outs


def _pick(word, table, ambiguous, foreign_re):
    """Resolve `word` to one repair, or None if the corpus cannot settle it."""
    cands = [c for c in _candidates(word, table, ambiguous)
             if not any(re.match(foreign_re, ch) for ch in c)]
    if not cands:
        return None
    if len(cands) == 1:
        return cands[0]
    lex = build_lexicon()
    known = [c for c in cands if c.lower() in lex]
    return known[0] if len(known) == 1 else None


def classify(word, camel_ok=True):
    """-> (class, repaired_word_or_None). `camel_ok` False on SLP1-carrier fields."""
    cyr = sum(1 for ch in word if re.match(f"[{CYR}]", ch))
    lat = sum(1 for ch in word if re.match(f"[{IAST}]", ch))
    if cyr and lat:
        if lat >= cyr:
            fixed = _pick(word, CYR_TO_LAT, AMBIGUOUS_CYR, f"[{CYR}]")
            if fixed and CAMEL_RE.fullmatch(fixed):
                # `saketakodDālakа` carries both defects at once; repairing the
                # stray Cyrillic «а» must not hide the `odD` camel underneath.
                for bad, good in CAMEL_FIXES.items():
                    if fixed.startswith(bad):
                        fixed = good + fixed[len(bad):]
                        break
            return ("cyr-in-latin" if fixed else "other", fixed)
        fixed = _pick(word, LAT_TO_CYR, AMBIGUOUS_LAT, f"[{IAST}]")
        return ("lat-in-cyr" if fixed else "other", fixed)
    if lat and camel_ok and CAMEL_RE.fullmatch(word):
        for bad, good in CAMEL_FIXES.items():
            if word.startswith(bad):
                return ("camel", good + word[len(bad):])
        return ("camel", None)
    return (None, None)


def walk(node, path, hits, fix):
    """Recursively scan (and optionally repair) every string in a JSON tree."""
    if isinstance(node, dict):
        return {k: walk(v, f"{path}.{k}", hits, fix) for k, v in node.items()}
    if isinstance(node, list):
        return [walk(v, f"{path}[{i}]", hits, fix) for i, v in enumerate(node)]
    if not isinstance(node, str):
        return node
    field = path.split(".")[-1].split("[")[0]
    camel_ok = field in CAMEL_FIELDS
    out, last, changed = [], 0, False
    for m in WORD.finditer(node):
        cls, fixed = classify(m.group(), camel_ok=camel_ok)
        if cls is None:
            continue
        hits.append({"path": path, "word": m.group(), "class": cls,
                     "suggested": fixed})
        if fix and fixed:
            out.append(node[last:m.start()])
            out.append(fixed)
            last = m.end()
            changed = True
    if changed:
        out.append(node[last:])
        return "".join(out)
    return node


def scan(fix=False):
    """Decide repairs on the PARSED tree, apply them to the RAW file text.

    Deciding on the parsed tree is what gives each hit its field name (camelCase
    is a defect in `note_ru`, correct in `stem`). Applying to the raw text is
    what keeps the fix reviewable: a json.dump round-trip reformatted files whose
    content never changed — 32 000 diff lines in one untouched raw index — and a
    diff nobody can read is a diff nobody checks.
    """
    per_file = {}
    for path in target_files():
        with open(path, encoding="utf-8") as fh:
            doc = json.load(fh)
        hits = []
        walk(doc, "", hits, False)
        if hits:
            per_file[path] = hits
        if not fix:
            continue
        repairs = {h["word"]: h["suggested"] for h in hits if h["suggested"]}
        if not repairs:
            continue
        with open(path, encoding="utf-8", newline="") as fh:
            raw = fh.read()
        for bad, good in sorted(repairs.items(), key=lambda kv: -len(kv[0])):
            raw = raw.replace(bad, good)
        json.loads(raw)          # never write a file we just broke
        with open(path, "w", encoding="utf-8", newline="") as fh:
            fh.write(raw)
    return per_file


def summarize(per_file):
    by_class = collections.Counter()
    words = collections.Counter()
    for hits in per_file.values():
        for h in hits:
            by_class[h["class"]] += 1
            words[(h["class"], h["word"], h["suggested"])] += 1
    return by_class, words


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--check", action="store_true",
                    help="report and exit 1 if any defect remains")
    ap.add_argument("--fix", action="store_true",
                    help="repair the auto-fixable classes in place")
    ap.add_argument("--report", default=None, help="write a Markdown report here")
    args = ap.parse_args()

    per_file = scan(fix=args.fix)
    by_class, words = summarize(per_file)
    total = sum(by_class.values())
    print(f"files scanned: {len(target_files())}, defect occurrences: {total}")
    for cls, n in by_class.most_common():
        auto = sum(c for (c2, _w, s), c in words.items() if c2 == cls and s)
        print(f"  {cls:14} {n:5}  (auto-fixable {auto})")

    if args.fix:
        print("\nrepaired the auto-fixable classes; re-run --check to see the residue")

    if args.report:
        lines = ["# Transliteration hygiene report",
                 "",
                 "_Auto-generated by scripts/translit_hygiene.py._",
                 "",
                 "Raised by [votes/sarga.md](../../votes/sarga.md) п.14 "
                 "(«saketakodDālakа — что за мусор с транслитерацией?»); the "
                 "single instance MG saw turned out to be a corpus-wide class.",
                 "",
                 "| class | occurrences | auto-fixable |",
                 "|---|---:|---:|"]
        for cls, n in by_class.most_common():
            auto = sum(c for (c2, _w, s), c in words.items() if c2 == cls and s)
            lines.append(f"| `{cls}` | {n} | {auto} |")
        lines += ["", "## Residue — needs a human reading, never a guess", "",
                  "| word | class | occurrences |", "|---|---|---:|"]
        residue = [(w, c, n) for (c, w, s), n in words.most_common() if not s]
        for w, c, n in residue:
            lines.append(f"| `{w}` | `{c}` | {n} |")
        if not residue:
            lines.append("| _(none)_ | | |")
        with open(args.report, "w", encoding="utf-8") as fh:
            fh.write("\n".join(lines) + "\n")
        print(f"report -> {args.report}")

    if args.check:
        undeclared = sorted({w for (_c, w, _s) in words
                             if w not in DECLARED_EXCEPTIONS})
        if undeclared:
            print(f"\nFAIL: {len(undeclared)} undeclared mixed-script word(s): "
                  + ", ".join(undeclared[:12]))
            print("Fix them, or — if the mixing is deliberate — add the word to "
                  "DECLARED_EXCEPTIONS with the reason.")
            sys.exit(1)
        print(f"\nPASS: only the {len(DECLARED_EXCEPTIONS)} declared exceptions "
              "remain.")


if __name__ == "__main__":
    main()

#!/usr/bin/env python
"""
Build data/gita_tm.json — Gita translation memory for PWG→EN enrichment.

Source: data/gita/chapter_NN/verse_NNN.json (700 verses × 18 chapters)

Best field for term coverage:
  setgb  — Shankaracharya EN by Gambirananda; word-by-word gloss
            pattern: "Term, English gloss; Term2, English gloss2; ..."
  etradi — Rāmānuja EN by Adidevananda; prose (philosophical terms in prose)
  etassa — Abhinavagupta EN; prose with Sanskrit terms inline

Output: data/gita_tm.json
  {
    "normalized_term": {
      "glosses": ["gloss1 (BG 2.47 setgb)", ...],
      "count": N
    }
  }

Key format: lowercase romanized Sanskrit, letters and hyphens only (no diacritics).
This is HK-adjacent — sufficient for fuzzy matching against PWG philosophical
terms. A SLP1 crosswalk against mw_en_tm.json headwords can follow in step 2.

Usage:
    python scripts/build_gita_tm.py
    python scripts/build_gita_tm.py --preview 30
    python scripts/build_gita_tm.py --stats
"""
import argparse
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

REPO = Path(__file__).parent.parent
GITA = REPO / "data" / "gita"
OUT  = REPO / "data" / "gita_tm.json"

# ── setgb clause parser ────────────────────────────────────────────────────────
# setgb is Gambirananda's word-by-word commentary on Śaṅkarācārya.
# Structure: "Term(s), gloss text; Term2, gloss text; ..."
# The term is everything before the first ', ' in each semicolon-clause.
# Problem: English connector words (is, not, even, a, the, thus, may, you, i.e.)
# sometimes precede the Sanskrit term. Heuristic: the Sanskrit term is the LAST
# token in the pre-comma segment that looks Sanskrit-shaped.

_SANSKRIT_SHAPE = re.compile(
    r'\b([a-z][a-z]*(?:ah|am|i[hm]?|um|a[hn]?|at|ayah|esu|e|o|u)'
    r'|[a-z]{3,}(?:-[a-z]+)+)\b',
    re.I
)
# Sanskrit function words / particles — not useful as TM keys (too generic)
_SANSK_STOP = frozenset("""
    ma te ca na api eva iva tu hi yat tat idam etat sa tad kim ayam asya
    mam iti evam tatah enam iha tatha yah tam tena tasya tesam tebhyah
    esah imam atra tatra yatra tada yada sada asmin asmad tasmat tasmad
    yadyapi tathapi param nanu tena kintu athava vapi capi nacet ced
    atha ca kim nu vai ha bho re aho yadi svayam mad tvam tvad aham
    sah sA tat te saH
""".split())

# Common English words that might bleed through as 'terms'
_ENGLISH_STOP = frozenset("""
    similarly therefore however thus hence also moreover furthermore
    because since when while although though yet still indeed already
    again always never often just even very here there only both
    either neither nor but and not all this that these those what which
    who whom whose why how when where never always sometimes usually
    generally specifically particularly certainly clearly certainly
    according hence indeed immediately literally namely obviously
    originally precisely previously primarily probably recently
    relatively simply sometimes specially subsequently sufficiently
    therefore toward unless unlike usually whether further having
    being becoming know knowing said saying given giving taken
    spoken written called named termed knowledge wisdom action
    devotion liberation bondage inaction result fruit desire
    understanding consciousness self mind intellect senses organ
    creature person supreme absolute eternal impermanent transient
""".split())

# Sanskrit relative/demonstrative pronouns that appear as term keys but add no TM value
_SANSK_STOP = _SANSK_STOP | frozenset("""
    yaya yena yasya yatha yad yadyapi tatha tatah tasya tasmai
    tesu tasmad tebhyah tesam tena sarvasya sarvatra sarvasah
    bhuyah yah etad ayam asau imam asmin asmad atra tatra yatra
""".split())

# Terms starting with these English-word prefixes are noise
_ENGLISH_PREFIXES = ("the-", "so-", "a-the", "an-", "or-", "of-", "in-the", "to-")


def normalize_term(raw):
    """Lowercase, letters+hyphens only, strip leading/trailing hyphens."""
    t = raw.lower().strip()
    t = re.sub(r'[^a-z\-]', '', t)
    t = t.strip('-')
    return t


def extract_term_from_preclause(pre):
    """
    Given the text before the comma (e.g., 'is karmani eva' or 'karma-phalahetuh'),
    return the best Sanskrit term candidate (last Sanskrit-shaped token cluster).
    """
    pre = pre.strip()
    # Try: whole pre-clause if it looks like a single compound term
    whole_norm = normalize_term(pre)
    if whole_norm and ' ' not in pre:
        return whole_norm

    # Multi-word: find the last Sanskrit-looking token or compound
    tokens = pre.split()
    # Walk backward and collect contiguous Sanskrit-looking tokens
    collected = []
    for tok in reversed(tokens):
        t = normalize_term(tok)
        if not t:
            continue
        if _SANSKRIT_SHAPE.search(tok) or len(t) >= 4:
            collected.insert(0, t)
        else:
            if collected:
                break   # hit a non-Sanskrit word after collecting some terms
    if collected:
        return '-'.join(collected) if len(collected) > 1 else collected[0]

    # Fallback: normalize whole pre
    return whole_norm or None


def parse_setgb(text, verse_ref):
    """
    Yield (term_key, gloss_with_ref) from a setgb field.
    Gloss is annotated with verse reference and source.
    """
    if not text:
        return
    # Strip leading verse reference like "2.47 "
    text = re.sub(r'^\d+\.\d+\s+', '', text)

    clauses = re.split(r';\s+', text)
    for clause in clauses:
        clause = clause.strip()
        # Find first ', ' that could separate term from gloss
        m = re.search(r',\s+', clause)
        if not m:
            continue
        pre   = clause[:m.start()]
        gloss = clause[m.end():].strip()
        # Gloss must be substantial English
        if len(gloss) < 4 or not re.search(r'[a-zA-Z]', gloss):
            continue
        # Don't treat things like "i.e., ..." as new entries
        if pre.strip().lower() in ('i.e', 'i.e.', 'viz', 'e.g', 'e.g.'):
            continue

        term_key = extract_term_from_preclause(pre)
        if not term_key:
            continue

        # Truncate very long glosses (they're usually explanatory prose)
        gloss_short = gloss[:200].rstrip()
        yield term_key, f"{gloss_short} ({verse_ref} setgb)"


def parse_etradi(text, verse_ref):
    """
    Extract philosophical term→gloss pairs from Rāmānuja EN (etradi).
    Pattern: prose containing 'X, meaning Y' or 'X (Sanskrit) means ...'
    Also capture leading Sanskrit compound before ':' that opens a clause.
    """
    if not text:
        return
    text = re.sub(r'^\d+\.\d+\s+', '', text)
    # Find patterns: "Term — gloss" or "Term: gloss" or "term, gloss." at sentence start
    for m in re.finditer(
        r'(?:^|(?<=[.!?]\s))([A-Za-z\-]{4,}(?:\s+[A-Za-z\-]{3,}){0,2})'
        r'(?:\s*—\s*|\s*:\s*|\s*,\s*)([A-Z][^.;]{15,80})',
        text
    ):
        term_key = normalize_term(m.group(1))
        gloss    = m.group(2).strip()
        if not term_key or len(term_key) < 3:
            continue
        yield term_key, f"{gloss[:150]} ({verse_ref} etradi)"


def _is_noise(term_key):
    """Return True if term_key should be excluded from the TM."""
    if not term_key or len(term_key) < 3:
        return True
    # Sanskrit particles and English stopwords
    if term_key in _SANSK_STOP or term_key in _ENGLISH_STOP:
        return True
    # Terms starting with English article/preposition prefixes
    if any(term_key.startswith(p) for p in _ENGLISH_PREFIXES):
        return True
    # Compound where ALL parts are Sanskrit particles (e.g. ca-eva, eva-ca)
    parts = term_key.split('-')
    if len(parts) > 1 and all(p in _SANSK_STOP or p in _ENGLISH_STOP for p in parts):
        return True
    # Pure English words: no Sanskrit morpheme shape AND short
    if (not re.search(r'(?:ah|am|ih|im|um|ayah|esu|anam|aya|ini|ika|tvam|tva|anam|arah|asya|ena|ani|ata|anu|abhi|ava|sam|pra|pari|nir|nis|vi|upa)$', term_key)
            and '-' not in term_key
            and len(term_key) < 8
            and term_key.isalpha()):
        return True
    return False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--preview", type=int, default=0, metavar="N",
                    help="Print top-N terms after building")
    ap.add_argument("--stats",   action="store_true",
                    help="Print frequency statistics")
    args = ap.parse_args()

    tm = {}   # term_key -> list[gloss_with_ref]

    chapter_dirs = sorted(GITA.glob("chapter_*"))
    total_verses = 0
    total_pairs  = 0

    for chdir in chapter_dirs:
        ch_num = int(chdir.name.split("_")[1])
        for vfile in sorted(chdir.glob("verse_*.json")):
            raw  = json.loads(vfile.read_text(encoding="utf-8"))
            verse_num = raw.get("verse", 0)
            ref  = f"BG {ch_num}.{verse_num}"

            for term, gloss in parse_setgb(raw.get("setgb", ""), ref):
                if _is_noise(term):
                    continue
                tm.setdefault(term, []).append(gloss)
                total_pairs += 1

            for term, gloss in parse_etradi(raw.get("etradi", ""), ref):
                if _is_noise(term):
                    continue
                tm.setdefault(term, []).append(gloss)
                total_pairs += 1

            total_verses += 1

    # Build output: dedupe glosses, sort by frequency desc
    out_data = {}
    for term in sorted(tm, key=lambda k: -len(tm[k])):
        seen_gl  = []
        seen_set = set()
        for g in tm[term]:
            gl_key = g[:60].lower()
            if gl_key not in seen_set:
                seen_set.add(gl_key)
                seen_gl.append(g)
        out_data[term] = {"glosses": seen_gl, "count": len(tm[term])}

    OUT.write_text(json.dumps(out_data, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Verses processed : {total_verses}")
    print(f"Term-gloss pairs : {total_pairs}")
    print(f"Unique terms     : {len(out_data)}")
    print(f"Output           : {OUT}")

    if args.preview or args.stats:
        items = list(out_data.items())
        print(f"\n{'—'*60}")
        print(f"Top {min(args.preview or 30, len(items))} terms by frequency:")
        for term, v in items[:args.preview or 30]:
            sample = v["glosses"][0][:80] if v["glosses"] else ""
            print(f"  {term!r:30s}  ×{v['count']:3d}  → {sample}")


if __name__ == "__main__":
    main()

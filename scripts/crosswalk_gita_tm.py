#!/usr/bin/env python
"""
Crosswalk data/gita_tm.json → SLP1 headwords from mw_en_tm.json.

MW encoding in mw_en_tm.json — standard SLP1 (not Cologne):
  Aspirates:  K=kh  G=gh  C=ch  J=jh  T=th  D=dh  P=ph  B=bh
  Sibilants:  S=ś  z=ṣ
  Nasals:  Y=ñ  N=ṅ  R=ṇ (retroflex nasal — common! guṇa=guRa)
  Long vowels:  A=ā  I=ī  U=ū  E=ai  O=au
  Retroflexes: w=ṭ  W=ṭh  q=ḍ  Q=ḍh
  Anusvara/visarga:  M=ṃ  H=ḥ (stripped in simplified form)

gita_tm.json keys are lowercase romanized Sanskrit, no diacritics:
  - long/short vowels merged (ā=a, ī=i, ū=u)
  - aspirates written as digraphs (dh, th, kh, bh, etc.)
  - ñ→n, ṣ/ś→s, ṇ→n
  - inflected forms (not stems): karmani, atmanam, buddhih, tapah

Strategy:
  1. Build simplified_index: mw_simple(key) → SLP1_key
  2. For each gita_tm key, try multiple stem variants
  3. Look up in simplified_index → get SLP1_key
  4. Output data/gita_tm_slp1.json: SLP1_key → Gita glosses

Output:
  data/gita_tm_slp1.json  — same glosses, keyed by matched SLP1 headword
  (unmatched terms retained under their original key with prefix 'gita:')

Usage:
  python scripts/crosswalk_gita_tm.py
  python scripts/crosswalk_gita_tm.py --report     # show match/miss stats
  python scripts/crosswalk_gita_tm.py --check karma,jnanam,tapah
"""
import argparse
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

REPO    = Path(__file__).parent.parent
GITA_TM = REPO / "data" / "gita_tm.json"
OUT     = REPO / "data" / "gita_tm_slp1.json"

# mw_en_tm.json (and mw_en_tm.py) live in the SanskritLexicography sibling repo
MW_TM   = (REPO.parent / "SanskritLexicography" / "RussianTranslation"
           / "src" / "mw_en_tm.json")
sys.path.insert(0, str(MW_TM.parent))
from mw_en_tm import build_simplified_index  # noqa: E402


# ── Gita key → candidate stem forms ──────────────────────────────────────────
# gita_tm keys are inflected forms. We try stripping common endings to find
# the dictionary stem that mw_en_tm uses as key.

_ENDINGS = [
    # (suffix, replacement_stem_suffix) — ordered longest first
    ('anam',  'an'),   # ātmānam → ātman
    ('anam',  'a'),    # phalam → phala (via am→a then try anam→a)
    ('asya',  'a'),    # dharmasya → dharma
    ('aya',   'a'),    # karmaya → karma (less common)
    ('esu',   'a'),    # karmeṣu → karma
    ('ani',   'a'),    # bhūtāni → bhūta
    ('ini',   'in'),   # yoginī → yogin
    ('inam',  'in'),   # yoginam → yogin
    ('anah',  'an'),   # ātmanaḥ → ātman
    ('aih',   'a'),    # guṇaiḥ → guṇa (instr. pl.)
    ('ebhyah','a'),    # lokebhyaḥ → loka (dat/abl pl.)
    ('ah',    'as'),   # tapaḥ → tapas (s-stem)
    ('ah',    'a'),    # dharmaḥ → dharma
    ('ah',    ''),     # ātmaḥ-like (try bare stem)
    ('ih',    'i'),    # buddhiḥ → buddhi (nom. sg. i-stem)
    ('im',    'i'),    # śāntim → śānti, gatim → gati (acc. sg. i-stem)
    ('uh',    'u'),    # guruḥ → guru
    ('um',    'u'),    # gurum → guru (acc. sg. u-stem)
    ('am',    'a'),    # yogam → yoga
    ('am',    ''),     # brahman (neut. am → strip)
    ('rtim',  'rti'),  # prakṛtim → prakṛti (special ṛ-stem)
    ('i',     ''),     # karmaṇi → karma (loc. sg.)
    ('a',     'an'),   # ātmā → ātman
    ('e',     'a'),    # yoge → yoga (loc. sg.)
    ('at',    'at'),   # (keep as-is for participles)
]


def gita_stem_variants(key: str) -> list:
    """Return a deduplicated list of possible stem forms for a gita_tm key."""
    variants = [key]
    for suffix, replacement in _ENDINGS:
        if key.endswith(suffix) and len(key) > len(suffix) + 1:
            stem = key[: -len(suffix)] + replacement
            if len(stem) >= 2:
                variants.append(stem)
    # Also try the key itself with final 'h' stripped (visarga → nothing)
    if key.endswith('h') and len(key) > 2:
        variants.append(key[:-1])

    # For compound keys (hyphens): also try each component independently
    if '-' in key:
        for part in key.split('-'):
            if len(part) >= 3:
                variants.extend(gita_stem_variants(part))

    return list(dict.fromkeys(variants))   # preserve order, dedupe


# ── Main ──────────────────────────────────────────────────────────────────────

def resolve(gita_key: str, idx: dict, mw_data: dict) -> str | None:
    """Return the best SLP1 key match for a gita_tm key, or None."""
    # Sort by length descending: longer stems are more specific and preferred
    variants = sorted(dict.fromkeys(gita_stem_variants(gita_key)), key=len, reverse=True)
    for stem in variants:
        candidates = idx.get(stem, [])
        if not candidates:
            continue
        if len(candidates) == 1:
            return candidates[0]
        # Multiple homonyms — prefer the one whose gloss is longer (more content)
        best = max(candidates, key=lambda k: len(mw_data.get(k, '')))
        return best
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--report', action='store_true',
                    help='Print match/miss statistics and top unmatched terms')
    ap.add_argument('--check', metavar='KEYS',
                    help='Comma-separated gita_tm keys to resolve (for debugging)')
    args = ap.parse_args()

    if not MW_TM.exists():
        print(f"ERROR: mw_en_tm.json not found at {MW_TM}", file=sys.stderr)
        print("Make sure SanskritLexicography repo is a sibling of CommentaryStrategies.",
              file=sys.stderr)
        sys.exit(1)

    print("Loading mw_en_tm.json …", flush=True)
    mw_data = json.loads(MW_TM.read_text(encoding='utf-8'))
    print(f"  MW TM: {len(mw_data):,} entries")

    print("Building simplified index …", flush=True)
    idx = build_simplified_index(mw_data)
    print(f"  Index: {len(idx):,} simplified forms")

    print("Loading gita_tm.json …", flush=True)
    gita_data = json.loads(GITA_TM.read_text(encoding='utf-8'))
    print(f"  Gita TM: {len(gita_data):,} terms")

    # ── Debug mode ──
    if args.check:
        for key in args.check.split(','):
            key = key.strip()
            slp1 = resolve(key, idx, mw_data)
            stems = gita_stem_variants(key)
            print(f"\n{key!r}:")
            print(f"  stem variants tried: {stems}")
            print(f"  matched SLP1 key:    {slp1!r}")
            if slp1:
                print(f"  MW gloss: {mw_data.get(slp1,'')[:120]}")
            entry = gita_data.get(key, {})
            if entry:
                print(f"  Gita glosses ({entry.get('count',0)}×): "
                      f"{entry['glosses'][0][:100] if entry.get('glosses') else ''}")
        return

    # ── Build output ──
    out = {}
    matched = 0
    unmatched_terms = []

    for gita_key, entry in gita_data.items():
        slp1 = resolve(gita_key, idx, mw_data)
        if slp1:
            # Merge: if key already in out (multiple inflections → same lemma), extend
            if slp1 not in out:
                out[slp1] = {'glosses': [], 'count': 0, 'gita_keys': []}
            out[slp1]['glosses'].extend(entry.get('glosses', []))
            out[slp1]['count'] += entry.get('count', 0)
            out[slp1]['gita_keys'].append(gita_key)
            matched += 1
        else:
            # Keep under original key with 'gita:' prefix (for unmatched)
            out[f"gita:{gita_key}"] = entry
            unmatched_terms.append((gita_key, entry.get('count', 0)))

    # Dedupe glosses within each merged entry
    for slp1, v in out.items():
        if 'gita_keys' in v:
            seen = set()
            deduped = []
            for g in v['glosses']:
                k = g[:50].lower()
                if k not in seen:
                    seen.add(k)
                    deduped.append(g)
            v['glosses'] = deduped

    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding='utf-8')

    print(f"\nMatched   : {matched:,} / {len(gita_data):,} gita_tm terms "
          f"({100*matched//len(gita_data)}%)")
    print(f"Unmatched : {len(unmatched_terms):,}")
    print(f"Output    : {OUT}")

    if args.report:
        print(f"\n── Top 20 unmatched (by frequency) ──")
        for key, cnt in sorted(unmatched_terms, key=lambda x: -x[1])[:20]:
            entry = gita_data.get(key, {})
            sample = entry['glosses'][0][:70] if entry.get('glosses') else ''
            print(f"  {key!r:30s} ×{cnt:3d}  {sample}")


if __name__ == '__main__':
    main()

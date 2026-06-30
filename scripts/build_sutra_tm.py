#!/usr/bin/env python
"""
Build Sanskrit philosophical term maps from Brahmasutra and Yogasutra.

Sources:
  data/brahmasutra/ (571 sutras, Sanskrit only)
  data/yogasutra/   (195 sutras, Sanskrit only)

Strategy:
  1. Transliterate Devanagari sutra_text → SLP1 (indic_transliteration)
  2. Tokenize by whitespace; for each token run greedy compound segmentation
     against the MW headword simplified index
  3. Collect matched MW SLP1 headwords → {mw_gloss, count, sutra_ids}

Output:
  data/bs_term_map_slp1.json
  data/ys_term_map_slp1.json

Both files share the same format as data/gita_tm_slp1.json so they can be
merged into the same TM lookup:
  {
    "SLP1_key": {
      "mw_gloss": "...",
      "count": N,
      "sutra_ids": ["1.1.1", ...]
    }
  }

Usage:
  python scripts/build_sutra_tm.py
  python scripts/build_sutra_tm.py --corpus bs     # Brahmasutra only
  python scripts/build_sutra_tm.py --corpus ys     # Yogasutra only
  python scripts/build_sutra_tm.py --report        # show top terms
  python scripts/build_sutra_tm.py --check yoga,citta,brahman  # debug lookup
"""
import argparse
import glob
import json
import os
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

try:
    from indic_transliteration import sanscript
    from indic_transliteration.sanscript import transliterate as _tr
    HAS_INDIC = True
except ImportError:
    HAS_INDIC = False

REPO   = Path(__file__).parent.parent
MW_TM  = (REPO.parent / "SanskritLexicography" / "RussianTranslation"
          / "src" / "mw_en_tm.json")
BS_DIR = REPO / "data" / "brahmasutra"
YS_DIR = REPO / "data" / "yogasutra"
BS_OUT = REPO / "data" / "bs_term_map_slp1.json"
YS_OUT = REPO / "data" / "ys_term_map_slp1.json"


# ── Transliteration ───────────────────────────────────────────────────────────

def dev_to_slp1(text: str) -> str:
    """Transliterate Devanagari text to SLP1 using indic_transliteration."""
    if not HAS_INDIC:
        raise RuntimeError("indic_transliteration not installed")
    # Strip Devanagari punctuation first so it doesn't affect transliteration
    text = re.sub(r'[।॥|]', ' ', text)
    text = re.sub(r'[0-9०-९]', ' ', text)
    text = re.sub(r"'", ' ', text)  # avagraha → space
    slp1 = _tr(text, sanscript.DEVANAGARI, sanscript.SLP1)
    return slp1


# ── Simplification (for MW index lookup) ─────────────────────────────────────
# mw_to_simple: normalise MW Cologne SLP1 keys → no-diacritic ASCII.
# slp1_to_simple: same but for indic_transliteration output (R=ṇ, w=ṭ, q=ḍ).

def mw_to_simple(key: str) -> str:
    """Reduce an MW SLP1 key to a simplified no-diacritic ASCII form."""
    key = (key
           .replace('K', 'kh').replace('G', 'gh')
           .replace('C', 'ch').replace('J', 'jh')
           .replace('T', 'th').replace('D', 'dh')
           .replace('P', 'ph').replace('B', 'bh'))
    key = key.replace('S', 's').replace('z', 's')
    # Nasals: Y=ñ, N=ṅ, R=ṇ → all 'n'
    key = key.replace('Y', 'n').replace('N', 'n').replace('R', 'n')
    key = key.replace('A', 'a').replace('I', 'i').replace('U', 'u')
    key = key.replace('E', 'ai').replace('O', 'au')
    key = key.replace('f', 'r').replace('F', 'r').replace('x', 'l')
    key = key.replace('M', 'm').replace('H', '')
    # Retroflexes → dental equivalents
    key = key.replace('W', 'th').replace('Q', 'dh')
    key = key.replace('w', 't').replace('q', 'd')
    return key.lower()


def slp1_to_simple(key: str) -> str:
    """Like mw_to_simple but handles indic_transliteration SLP1 extras."""
    key = (key
           .replace('K', 'kh').replace('G', 'gh')
           .replace('C', 'ch').replace('J', 'jh')
           .replace('T', 'th').replace('D', 'dh')
           .replace('P', 'ph').replace('B', 'bh'))
    key = key.replace('S', 's').replace('z', 's')
    key = key.replace('Y', 'n')
    key = key.replace('A', 'a').replace('I', 'i').replace('U', 'u')
    # Diphthongs: E=ai, O=au (SLP1 convention)
    key = key.replace('E', 'ai').replace('O', 'au')
    key = key.replace('f', 'r').replace('F', 'r').replace('x', 'l')
    key = key.replace('M', 'm').replace('H', '')
    key = key.replace('R', 'n')   # indic_transliteration: ṇ = R (≠ MW's N)
    key = key.replace('N', 'n')   # MW's ṇ just in case
    key = key.replace('w', 't')   # indic_transliteration: ṭ = w
    key = key.replace('q', 'd')   # indic_transliteration: ḍ = q
    return key.lower()


# ── Index and lookup ──────────────────────────────────────────────────────────

def build_mw_index(mw_data: dict) -> dict:
    """simplified_form → list of MW SLP1 keys."""
    idx = {}
    for k in mw_data:
        s = mw_to_simple(k)
        idx.setdefault(s, []).append(k)
    return idx


def resolve_slp1(simple_form: str, idx: dict, mw_data: dict) -> str | None:
    """Look up a simplified form in the MW index; return best SLP1 key."""
    candidates = idx.get(simple_form, [])
    if not candidates:
        return None
    if len(candidates) == 1:
        return candidates[0]
    return max(candidates, key=lambda k: len(mw_data.get(k, '')))


# ── Sanskrit stop list ────────────────────────────────────────────────────────
# All entries MUST be simplified forms (all lowercase, digraphs, no long vowels,
# visarga/anusvara stripped) so is_stop(slp1_to_simple(x)) works correctly.

_STOP = frozenset("""
    atha ata ca na api eva iva tu hi yat tat idam etat sa tad kim ayam
    iti evam tata enam iha tatha yah tam tena tasya tesam tebhyah esah
    imam atra tatra yatra tada yada sada asmin asmat tasmat yadyapi
    tathapi param nanu tasmin kintu athava vapi capi nacet ced svayam
    vai ha aho yadi mad tvam aham sah sa te asmad
    pratham dvitiya trtiya caturtha pada adhyaya chapter padam
    tad tu hi na va
""".split())


def is_stop(simple: str) -> bool:
    """Return True if the simplified form is a Sanskrit particle/function word."""
    return simple in _STOP or len(simple) < 4


# ── Greedy compound segmentation ──────────────────────────────────────────────

def greedy_segment(slp1_token: str, idx: dict, mw_data: dict,
                   min_chars: int = 4) -> list[str]:
    """
    Greedily segment a SLP1 compound into MW headwords (SLP1 keys).
    Uses longest-prefix-first matching via the MW simplified index.
    Returns a list of matched MW SLP1 keys.
    """
    token = slp1_token
    # Strip terminal visarga (always an inflectional ending, not part of stem)
    if token.endswith('H'):
        token = token[:-1]
    # Strip terminal anusvara before checking
    if token.endswith('M'):
        token = token[:-1]

    results = []
    pos = 0
    while pos < len(token):
        best_len, best_key = 0, None
        for end in range(len(token), pos + min_chars - 1, -1):
            cand = token[pos:end]
            # Try the candidate as-is
            simple = slp1_to_simple(cand)
            if not is_stop(simple):
                slp1_key = resolve_slp1(simple, idx, mw_data)
                if slp1_key:
                    best_len = end - pos
                    best_key = slp1_key
                    break
            # Also try stripping a trailing 'a' (stem form without final vowel)
            if cand.endswith('a') and len(cand) > min_chars:
                simple2 = slp1_to_simple(cand[:-1])
                if not is_stop(simple2):
                    slp1_key2 = resolve_slp1(simple2, idx, mw_data)
                    if slp1_key2:
                        best_len = end - pos
                        best_key = slp1_key2
                        break
        if best_key:
            results.append(best_key)
            pos += best_len
        else:
            pos += 1   # skip one char (handles sandhi consonants like S=ś)
    return results


# ── Corpus loaders ────────────────────────────────────────────────────────────

def load_bs_sutras(bs_dir: Path) -> list[dict]:
    """Load all Brahmasutra sutra JSON files sorted by sutra_id."""
    sutras = []
    for f in sorted(bs_dir.glob("**/*.json")):
        if f.stem.startswith("sutra_"):
            try:
                d = json.loads(f.read_text(encoding="utf-8"))
                sutras.append(d)
            except Exception:
                pass
    return sutras


def load_ys_sutras(ys_dir: Path) -> list[dict]:
    """Load all Yogasutra sutra JSON files sorted by sutra_id."""
    sutras = []
    for f in sorted(ys_dir.glob("**/*.json")):
        if f.stem.startswith("sutra_"):
            try:
                d = json.loads(f.read_text(encoding="utf-8"))
                sutras.append(d)
            except Exception:
                pass
    return sutras


# ── Main processing ───────────────────────────────────────────────────────────

def process_sutras(sutras: list[dict], id_field: str, idx: dict,
                   mw_data: dict) -> dict:
    """
    Extract philosophical term → {mw_gloss, count, sutra_ids} from sutra texts.
    Returns a dict keyed by MW SLP1 headword.
    """
    tm = {}   # slp1_key -> {count, sutra_ids}
    skipped = 0

    for sutra in sutras:
        sid = sutra.get(id_field, '?')
        text = sutra.get('sutra_text', '')
        if not text.strip():
            continue
        try:
            slp1 = dev_to_slp1(text)
        except Exception:
            skipped += 1
            continue

        # Process each space-separated token
        for token in slp1.split():
            token = token.strip(".,;:!?\"'()")
            if len(token) < 2:
                continue
            # Skip section-header tokens that appear in sutra_text of first sutras
            # e.g. "praTamoDyAyaH" (prathamādhyāyaḥ) and "pAdaH" (pādaḥ)
            tok_simple = slp1_to_simple(token)
            if any(tok_simple.startswith(p) for p in
                   ('pratham', 'dvitiya', 'trtiya', 'caturtha',
                    'praTam', 'dvit', 'catuH')):
                continue
            if tok_simple in ('pada', 'padam', 'adhyaya', 'adhyayah'):
                continue
            # Greedy compound segmentation
            keys = greedy_segment(token, idx, mw_data)
            for slp1_key in keys:
                entry = tm.setdefault(slp1_key, {'count': 0, 'sutra_ids': []})
                entry['count'] += 1
                if sid not in entry['sutra_ids']:
                    entry['sutra_ids'].append(sid)

    if skipped:
        print(f"  (skipped {skipped} sutras due to transliteration errors)")
    return tm


def _gloss_is_real(gloss: str) -> bool:
    """Return False for cross-reference-only MW entries like 'in for 2 | See 2'."""
    if not gloss or len(gloss) < 15:
        return False
    # Real glosses have multi-char alphabetic words; cross-refs are mostly numbers/symbols
    real_words = re.findall(r'[a-zA-Z]{4,}', gloss)
    return len(real_words) >= 2


def build_output(tm: dict, mw_data: dict) -> dict:
    """Enrich TM entries with MW gloss; skip cross-reference entries; sort by count."""
    out = {}
    for slp1_key in sorted(tm, key=lambda k: -tm[k]['count']):
        entry = tm[slp1_key]
        gloss = mw_data.get(slp1_key, '')
        if not _gloss_is_real(gloss):
            continue
        out[slp1_key] = {
            'mw_gloss': gloss[:300] if gloss else '',
            'count': entry['count'],
            'sutra_ids': sorted(entry['sutra_ids']),
        }
    return out


# ── CLI ───────────────────────────────────────────────────────────────────────

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--corpus', choices=['bs', 'ys', 'both'], default='both',
                    help='Which corpus to process (default: both)')
    ap.add_argument('--report', action='store_true',
                    help='Print top-30 terms per corpus after building')
    ap.add_argument('--check', metavar='KEYS',
                    help='Comma-separated simplified Sanskrit forms to look up')
    args = ap.parse_args()

    if not HAS_INDIC:
        print("ERROR: indic_transliteration not installed. Run: pip install indic-transliteration",
              file=sys.stderr)
        sys.exit(1)
    if not MW_TM.exists():
        print(f"ERROR: mw_en_tm.json not found at {MW_TM}", file=sys.stderr)
        sys.exit(1)

    print("Loading mw_en_tm.json …", flush=True)
    mw_data = json.loads(MW_TM.read_text(encoding='utf-8'))
    print(f"  MW TM: {len(mw_data):,} entries", flush=True)

    print("Building MW simplified index …", flush=True)
    idx = build_mw_index(mw_data)
    print(f"  Index: {len(idx):,} simplified forms", flush=True)

    # ── Debug mode ──
    if args.check:
        for key in args.check.split(','):
            key = key.strip()
            slp1_key = resolve_slp1(key, idx, mw_data)
            print(f"\n{key!r} → SLP1: {slp1_key!r}")
            if slp1_key:
                print(f"  MW gloss: {mw_data.get(slp1_key, '')[:120]}")
        return

    do_bs = args.corpus in ('bs', 'both')
    do_ys = args.corpus in ('ys', 'both')

    # ── Brahmasutra ──
    if do_bs:
        print("\nProcessing Brahmasutra …", flush=True)
        bs_sutras = load_bs_sutras(BS_DIR)
        print(f"  Loaded {len(bs_sutras)} sutras", flush=True)
        bs_tm = process_sutras(bs_sutras, 'sutra_id', idx, mw_data)
        bs_out = build_output(bs_tm, mw_data)
        BS_OUT.write_text(json.dumps(bs_out, ensure_ascii=False, indent=2),
                          encoding='utf-8')
        print(f"  Unique terms: {len(bs_out):,}")
        print(f"  Output: {BS_OUT}")
        if args.report:
            print(f"\n── Top 30 BS terms ──")
            for k, v in list(bs_out.items())[:30]:
                print(f"  {k!r:20s} ×{v['count']:3d}  "
                      f"{v['mw_gloss'][:60]}")

    # ── Yogasutra ──
    if do_ys:
        print("\nProcessing Yogasutra …", flush=True)
        ys_sutras = load_ys_sutras(YS_DIR)
        print(f"  Loaded {len(ys_sutras)} sutras", flush=True)
        ys_tm = process_sutras(ys_sutras, 'sutra_id', idx, mw_data)
        ys_out = build_output(ys_tm, mw_data)
        YS_OUT.write_text(json.dumps(ys_out, ensure_ascii=False, indent=2),
                          encoding='utf-8')
        print(f"  Unique terms: {len(ys_out):,}")
        print(f"  Output: {YS_OUT}")
        if args.report:
            print(f"\n── Top 30 YS terms ──")
            for k, v in list(ys_out.items())[:30]:
                print(f"  {k!r:20s} ×{v['count']:3d}  "
                      f"{v['mw_gloss'][:60]}")


if __name__ == '__main__':
    main()

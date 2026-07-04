#!/usr/bin/env python3
"""Shared Sanskrit alignment helpers (Phase-2 §11 accuracy lever).

Canonicalizes IAST for content matching via the org toolkit `sanskrit_util`
(SHARED_CODE §1-2 — do NOT re-implement transcoding/normalization), and provides
similarity + classify used by both the edition comparison and the commentary
segmenter. Aggressive fold (`nfold`: strips diacritics/length, folds nasals→n) is
chosen deliberately: it neutralizes sandhi/orthographic noise so the SAME shloka
across editions matches, which the previous diacritic-sensitive normalizer missed.

Retroflex-loss caveat (SHARED_CODE ळ→x) lives in the Devanagari→SLP1 path; here we
canonicalize IAST, so it does not apply. Falls back to a stdlib normalizer if the
toolkit is not importable.
"""
import os
import sys
import re
import difflib
import unicodedata

def find_sibling(name):
    """Locate a sibling repo by walking up from this repo's root — a git
    worktree can sit nested (e.g. .claude/worktrees/X), so REPO/.. is not
    guaranteed to be the GitHub/ root."""
    d = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    for _ in range(6):
        cand = os.path.join(d, name)
        if os.path.isdir(cand):
            return cand
        d = os.path.dirname(d)
    return None


_UTIL_ROOT = find_sibling("sanskrit-util")
_UTIL = os.path.join(_UTIL_ROOT, "py") if _UTIL_ROOT else ""
if _UTIL and os.path.isdir(_UTIL) and _UTIL not in sys.path:
    sys.path.insert(0, _UTIL)

try:
    import sanskrit_util as _su
    _HAVE_SU = True

    def canon(text):
        """Aggressive canonical key for content matching (IAST in).

        nfold folds letters/nasals but leaves daṇḍa/digits/punctuation — strip
        those so verse-number markers (॥1॥) and daṇḍas don't block exact matches.
        """
        s = _su.nfold(text or "").lower()
        s = re.sub(r"[^a-z ]", " ", s)
        return re.sub(r"\s+", " ", s).strip()

    def deva_to_iast(text):
        return _su.deva_to_iast(text or "")
except Exception:                                   # pragma: no cover
    _HAVE_SU = False

    def canon(text):
        t = unicodedata.normalize("NFD", (text or "").lower())
        t = "".join(c for c in t if unicodedata.category(c) != "Mn")
        t = re.sub(r"[^a-z ]", " ", t)
        return re.sub(r"\s+", " ", t).strip()

    def deva_to_iast(text):
        return text or ""


def canon_tokens(text):
    return [t for t in canon(text).split() if t]


def sim(a, b):
    ca, cb = canon(a), canon(b)
    if not ca and not cb:
        return 1.0
    return difflib.SequenceMatcher(None, ca, cb).ratio()


def classify(a, b, hi=0.95, lo=0.60):
    r = sim(a, b)
    tag = "identical" if r >= hi else "variant" if r >= lo else "distinct"
    return tag, round(r, 3)


def backend():
    return "sanskrit_util" if _HAVE_SU else "stdlib-fallback"


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    print("backend:", backend())
    pairs = [("cāraṇācarite pathi", "cāraṇācarite pathi"),
             ("niṣpratidvandvaṃ", "nispratidvandvam"),
             ("rāmasya cihnāni", "rāmasya liṅgāni")]
    for a, b in pairs:
        print(f"{a!r} ~ {b!r} -> {classify(a, b)}")

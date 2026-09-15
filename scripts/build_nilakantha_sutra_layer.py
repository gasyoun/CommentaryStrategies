#!/usr/bin/env python3
"""H4736 — Join Nilakantha licence-register deviation_term_sa to Panini sutra numbers.

Joins each unique deviation_term_sa (IAST-style grammar-operation term) in
data/licence_register/commentary_licence_register_nilakantha.tsv to sutra ids in
kosha's data/concordance/sutra_coverage_map.tsv via SLP1 token matching.

Match tiers (deterministic, recorded per match):
  phrase    - the full term's SLP1 form occurs in a sutra text
  word      - a term token equals a sutra word (trailing visarga H / anusvara M
              stripped on the sutra side; sandhi word-internal substrings excluded)
  substring - a term token occurs inside a sutra word (weakest evidence)

Outputs (additive layer; the register itself is never rewritten):
  data/licence_register/nilakantha_sutra_layer.tsv  (one row per register row)
  reports/NILAKANTHA_SUTRA_LAYER_<date>.md          (built with --report)

Idempotent: re-running regenerates identical bytes. `--check` exits 0 when the
committed layer file matches a fresh derivation (derive-don't-store parity gate).

Kosha path resolution: --kosha flag, or $KOSHA_HOME, or ../kosha relative to repo root.
"""
import argparse
import csv
import re
import sys
import unicodedata
from pathlib import Path
from typing import Optional

sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
sys.stderr.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]

REPO = Path(__file__).resolve().parent.parent
REGISTER = REPO / "data/licence_register/commentary_licence_register_nilakantha.tsv"
LAYER = REPO / "data/licence_register/nilakantha_sutra_layer.tsv"

# IAST -> SLP1 (longest-first application; extends the i2s map in
# scripts/backfill_grintser_crossrefs.py with t+th and d+dh digraphs).
IAST_TO_SLP1 = [
    ("ā", "A"), ("ī", "I"), ("ū", "U"), ("ṝ", "F"), ("ṛ", "f"), ("ḹ", "X"),
    ("ḷ", "x"), ("ṅ", "N"), ("ñ", "Y"), ("ṭh", "W"), ("ṭ", "w"), ("ḍh", "Q"),
    ("ḍ", "q"), ("ṇ", "R"), ("ś", "S"), ("ṣ", "z"), ("ṃ", "M"), ("ḥ", "H"),
    ("ch", "C"), ("kh", "K"), ("gh", "G"), ("jh", "J"), ("ṣh", "z"), ("th", "T"),
    ("dh", "D"), ("ph", "P"), ("bh", "B"), ("ai", "E"), ("au", "O"),
]

# English connectors / gloss suffixes that must never be transliterated and matched.
ENGLISH_STOP = {"for", "and", "the", "of", "vs"}
# Suffixes marking negated/derived operations: 'X-abhāva' / 'X-bhāva' match on X,
# never on the suffix itself (e.g. 3.2.45 karaRaBAvayoH would otherwise swallow
# every -bhāva term as a false 'bhāva' word match).
NEG_SUFFIXES = {"abhāva", "bhāva"}

# Hand-checked sample (H4736, OxAlpha worker, 15-09-2026): term -> sutra id ->
# verdict, each read directly against the kosha map's SLP1 text this session.
VERIFIED_SAMPLE = [
    ("lopa", "1.1.60", "adarśanaṁ lopaḥ — THE lopa definition; literal word match"),
    ("supāṃ suluk", "7.1.39", "phrase present verbatim inside the sutra text"),
    ("mum-āgama", "6.3.67", "arur dviṣad ajantasya mum — the mum-āgama sutra; literal"),
    ("num-abhāva", "7.1.58", "idito num dhātoḥ — the num-āgama sutra; literal"),
    ("laṭ", "3.2.118", "laṭ śme — laṭ present (law = laṭ in SLP1)"),
    ("ru-tva-abhāva", "8.3.1", "matu-vaso ru sambuddhau chandasi — the ru-sutra; literal"),
    ("guṇa-abhāva", "1.1.2", "adeṅ guṇaḥ — the guṇa definition sutra"),
    ("pūrvasavarṇa", "6.1.102", "prathamayoḥ pūrvasavarṇaḥ — literal word match"),
    ("iṭ", "7.2.41", "iṭ sani vā — iṭ-āgama rule (1.2.2 `vija iw` also matched)"),
    ("taddhita-luk", "4.1.17", "prācāṁ ṣaṣ ṭaddhitaḥ — taddhita word; luk ids joined separately"),
]


def i2s(s: str) -> str:
    """IAST-ish romanization -> SLP1 letters only."""
    out = s.lower()
    for a, b in IAST_TO_SLP1:
        out = out.replace(a, b)
    return re.sub(r"[^A-Za-z]", "", out)


def asciify(s: str) -> str:
    """Pure-ASCII form used to detect English connector tokens."""
    return "".join(c for c in unicodedata.normalize("NFD", s.lower())
                   if unicodedata.category(c) != "Mn")


def term_tokens(term: str) -> list[str]:
    """Split a register term into SLP1 candidate tokens (deterministic)."""
    cleaned = re.split(r"[(/,;]", term)
    toks: list[str] = []
    for part in cleaned:
        for word in part.split():
            w = word.strip().strip("-—")
            if not w or asciify(w) in ENGLISH_STOP or w in ENGLISH_STOP:
                continue
            if w in NEG_SUFFIXES:
                continue  # 'X-abhāva' matches via X
            for sub in re.split(r"[-—]", w):
                if sub in NEG_SUFFIXES:
                    continue  # 'X-bhāva' compound: the suffix never becomes a token
                slp = i2s(sub)
                if len(slp) >= 2:
                    toks.append(slp)
    # dedupe preserving order
    seen, out = set(), []
    for t in toks:
        if t not in seen:
            seen.add(t)
            out.append(t)
    return out


def phrase_slp(term: str) -> str:
    """Whole-term SLP1 phrase (spaces collapsed), or '' when <1 usable token."""
    words = [i2s(w) for w in term.split()
             if i2s(w) and asciify(w) not in ENGLISH_STOP and w not in ENGLISH_STOP
             and w not in NEG_SUFFIXES]
    return " ".join(words)


def strip_endings(word: str) -> str:
    """Sutra-side word normalisation: strip trailing visarga/anusvara."""
    return word.rstrip("HM")


def load_sutras(kosha_map: Path) -> dict[str, str]:
    sutras: dict[str, str] = {}
    with open(kosha_map, encoding="utf-8") as f:
        for row in csv.DictReader(f, delimiter="\t"):
            sutras[row["sutra_id"]] = row["sutra_text_slp1"]
    return sutras


def match_term(term: str, sutras: dict[str, str]) -> tuple[list[str], list[str], list[str]]:
    """Return (phrase_ids, word_ids, substring_ids) sorted by sutra id.

    Phrase matching is space-normalised on both sides (kosha AG-harvest texts
    are often sandhi-compounded with no spaces, e.g. 7.1.39 supAMsuluk...).
    """
    sutra_sort = lambda ids: sorted(ids, key=lambda s: [int(p) for p in s.split(".")])
    phrase = phrase_slp(term)
    phrase_ns = phrase.replace(" ", "")
    multi_phrase = bool(phrase_ns) and " " in phrase  # >=2 tokens
    phrase_ids, word_ids, sub_ids = set(), set(), set()
    for sid, text in sutras.items():
        words = text.split()
        stripped = [strip_endings(w) for w in words]
        if multi_phrase and phrase_ns in text.replace(" ", ""):
            phrase_ids.add(sid)
            continue
        for tok in term_tokens(term):
            if tok in stripped:
                word_ids.add(sid)
            elif tok in text:
                sub_ids.add(sid)
    return sutra_sort(phrase_ids), sutra_sort(word_ids), sutra_sort(sub_ids)


def build_rows(sutras: dict[str, str]) -> list[dict]:
    rows: list[dict] = []
    with open(REGISTER, encoding="utf-8") as f:
        for reg in csv.DictReader(f, delimiter="\t"):
            term = reg["deviation_term_sa"].strip()
            if not term:
                rows.append({**{k: reg[k] for k in REGISTER_COLS},
                             "term_tokens_slp1": "", "matched_sutra_ids": "",
                             "match_kind": "", "matched_sutra_texts_slp1": ""})
                continue
            pids, wids, sids = match_term(term, sutras)
            ids = pids or wids or sids
            kind = ("phrase" if pids else "word" if wids else
                    "substring" if sids else "")
            rows.append({
                **{k: reg[k] for k in REGISTER_COLS},
                "term_tokens_slp1": ",".join(term_tokens(term)),
                "matched_sutra_ids": ";".join(ids[:10]),
                "match_kind": kind,
                "matched_sutra_texts_slp1": " | ".join(
                    sutras[i].replace("\t", " ") for i in ids[:5]),
            })
    return rows


REGISTER_COLS = ["row_id", "locus", "locus_id", "parva", "deviation_type",
                 "deviation_term_sa", "classification"]


def write_layer(rows: list[dict]) -> str:
    import io
    buf = io.StringIO()
    cols = REGISTER_COLS + ["term_tokens_slp1", "matched_sutra_ids",
                            "match_kind", "matched_sutra_texts_slp1"]
    w = csv.DictWriter(buf, fieldnames=cols, delimiter="\t",
                       lineterminator="\n", extrasaction="ignore")
    w.writeheader()
    w.writerows(rows)
    return buf.getvalue()


def find_kosha_map(arg: Optional[str]) -> Path:
    if arg:
        return Path(arg)
    import os
    env = os.environ.get("KOSHA_HOME")
    cands = ([Path(env) / "data/concordance/sutra_coverage_map.tsv"] if env else []) + [
        REPO.parent / "kosha/data/concordance/sutra_coverage_map.tsv",
        Path.home() / "Documents/GitHub/kosha/data/concordance/sutra_coverage_map.tsv",
    ]
    for c in cands:
        if c.is_file():
            return c
    raise SystemExit("kosha sutra_coverage_map.tsv not found; pass --kosha")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--kosha", default=None, help="path to sutra_coverage_map.tsv")
    ap.add_argument("--check", action="store_true",
                    help="exit 1 when committed layer differs from fresh build")
    ap.add_argument("--report", action="store_true",
                    help="also write the dated report markdown")
    a = ap.parse_args()
    kosha_map = find_kosha_map(a.kosha)
    sutras = load_sutras(kosha_map)
    rows = build_rows(sutras)
    payload = write_layer(rows)

    if a.check:
        committed = LAYER.read_text(encoding="utf-8") if LAYER.is_file() else ""
        if committed == payload:
            print(f"CHECK PASS {LAYER.relative_to(REPO)} matches fresh build "
                  f"({len(rows)} rows, map={len(sutras)} sutras)")
            return 0
        print("CHECK FAIL: committed layer differs from fresh build "
              f"({len(rows)} rows, map={len(sutras)} sutras) — rerun without --check")
        return 1

    LAYER.write_text(payload, encoding="utf-8")
    matched = sum(1 for r in rows if r["match_kind"])
    print(f"WROTE {LAYER.relative_to(REPO)}: {len(rows)} rows, "
          f"{matched} matched ({kosha_map})")
    if a.report:
        write_report(rows, sutras, kosha_map)
    return 0


def write_report(rows: list[dict], sutras: dict[str, str], kosha_map: Path) -> None:
    """Dated report: method, term->sutra table, coverage, hand-check, residue."""
    by_term: dict[str, list[dict]] = {}
    for r in rows:
        by_term.setdefault(r["deviation_term_sa"], []).append(r)
    matched_terms = {t for t, rs in by_term.items() if t and rs[0]["match_kind"]}
    unmatched = sorted(t for t in by_term if t and t not in matched_terms)
    n_rows = len(rows)
    n_matched_rows = sum(1 for r in rows if r["match_kind"])
    today = "2026-09-15"
    lines = [
        "# Nilakantha licence register → Panini sutra layer (H4736)",
        "",
        f"_Created: {today} · Last updated: {today}_",
        "",
        "Join of `deviation_term_sa` in `commentary_licence_register_nilakantha.tsv` "
        f"({len(by_term) - (1 if '' in by_term else 0)} unique terms over {n_rows} register rows) "
        f"to `sutra_coverage_map.tsv` ({len(sutras)} sutras, kosha data-v0.3.0).",
        "",
        "## Method",
        "",
        "1. Register terms are IAST-style grammar-operation labels; each is split into",
        "   SLP1 candidate tokens (`X-abhāva` matches on X; English connectors dropped).",
        "2. Match tiers, strongest first: `phrase` (whole term inside a sutra text),",
        "   `word` (token equals a sutra word, trailing visarga/anusvāra stripped),",
        "   `substring` (token inside a sutra word — weakest, may be accidental).",
        "3. Layer rows carry up to 10 sutra ids per term; the register itself is untouched",
        "   (additive file `nilakantha_sutra_layer.tsv`, rebuilt idempotently by",
        "   `scripts/build_nilakantha_sutra_layer.py --check`).",
        "",
        "## Coverage",
        "",
        f"- register rows: {n_rows}; rows with ≥1 sutra match: {n_matched_rows}",
        f"- unique terms matched: {len(matched_terms)}; unmatched: {len(unmatched)}",
        f"- kosha map: `{kosha_map}`",
        "",
        "## Term → sutra table",
        "",
        "term | rows | tier | sutra ids",
        "--- | --- | --- | ---",
    ]
    for term in sorted(by_term, key=str.lower):
        if not term:
            continue
        rs = by_term[term]
        tier, ids = rs[0]["match_kind"], rs[0]["matched_sutra_ids"].split(";") if rs[0]["matched_sutra_ids"] else []
        lines.append(f"{term} | {len(rs)} | {tier or 'UNMATCHED'} | {'; '.join(ids[:6])}")
    lines += ["", "## Hand-checked sample", "",
              "Verified by reading the matched sutra SLP1 text directly (worker, OxAlpha tier).",
              ""]
    for term, sid, verdict in VERIFIED_SAMPLE:
        lines.append(f"- **{term}** → {sid} — `{sutras.get(sid, '?')}` · {verdict}")
    lines += [
        "",
        "## Unmatched residue (honest)",
        "",
    ]
    lines += [f"- {t}" for t in unmatched] if unmatched else ["- none"]
    lines += [
        "",
        "Unmatched terms are commentarial labels or derived formations absent from the",
        "Aṣṭādhyāyī text as harvested (e.g. 'sandhi', 'vyatyaya', 'samāsānta' —",
        "meta-terms of the commentary tradition, never sutra verbatim).",
        "",
        "## Handoff",
        "",
        "Executed under H4736 (OxAlpha tier). Evidence: layer TSV + this report +",
        "`python scripts/build_nilakantha_sutra_layer.py --check`.",
        "",
        "_Гасунс_",
        "",
    ]
    out = REPO / f"reports/NILAKANTHA_SUTRA_LAYER_{today}.md"
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"WROTE {out.relative_to(REPO)}")


if __name__ == "__main__":
    sys.exit(main())

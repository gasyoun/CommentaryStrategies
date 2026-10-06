# MBh Klammeranalyse v1 (H6055) — full-Patañjali scale pass

_Created: 06-10-2026 · Gasūns · tier: GLM 5.3 (`opencode/zai-coding-plan/glm-5.3`)_

Rulings: [GRILL_RESEARCH_WIDENING_04-10-2026.md](https://github.com/gasyoun/Uprava/blob/main/reports/GRILL_RESEARCH_WIDENING_04-10-2026.md) §H —
H1 (first full pass = Patañjali's MBh) · H2 (one full commentary) · H11 (JSON schema) · H12 (κ with second annotation, H5312/H5313 shape).

## Provenance / rights

- Source: [ashtadhyayi-com/data](https://github.com/ashtadhyayi-com/data) `sutraani/bhashya.txt` (3,983 sūtras, dict keyed by concatenated a.p.n) and `sutraani/vartika.txt` (921 records, `{"name","data":[{"sutra","vartika"}]}`), fetched 06-10-2026.
- That repository carries **no license file** (checked 06-10-2026 via GitHub API: `license: None`). Mirror-only discipline: raw text lives in `source/` (gitignored, re-fetchable via `--fetch`), **never committed**. Every committed file below is a derived measurement.
- Same dataset as the SanskritGrammar `panini_cache` lineage (H413/H414) — no second canonical copy exists here.

## Artifacts (all derived, all committed)

| file | content |
|---|---|
| `mbh_klammer_per_sutra.tsv` | per-sūtra × layer: tokens, candidates, dually-segmented, exact-agree |
| `mbh_klammer_bank.json` → `build/` (gitignored) | full candidate bank (92,271 rows) |
| `mbh_klammer_sample.json` | the seeded κ sample (300 rows, both passes) |
| `mbh_klammer_disagreements.json` | stratified disagreement subset feeding the sheet |
| `mbh_klammer_topcompounds.tsv` | top-100 candidate frequency table |
| `mbh_klammer_kappa.json` | κ + bootstrap CI + raw agreement |
| `second_annotator_sheet.html` | human lane sheet (H5312 shape) |

Record schema (`mbh-klammer-v1`, ruling H11): `layer, sutra, form, len` (code points), `freq`, `members_A/members_B` (null = pass failed), `boundaries_A/B`, `tree: null`, `tree_status: "deferred_v2"`.

## Pre-registered parameters (frozen before the run)

`MIN_TOKEN_LEN=9` (compound-candidate threshold) · `VOCAB_MAX_LEN=7`, `VOCAB_MIN_FREQ=3` (corpus-induced vocabulary, pooled layers) · `MIN_CHUNK=2` · `SAMPLE_N=300` layer-proportional · `SHEET_ROWS=60` · seed `20261006` · bootstrap `2000`.

## Method

Two **independent mechanical annotators** segment every candidate over the shared vocabulary: pass A = greedy longest-match left-to-right; pass B = right-to-left. "Dually segmented" = both fully segment. κ = Cohen's κ on the canonical segmentation label, plus a boundary-level κ over every interior position; 95% bootstrap CI.

## Honest limitations (read before using)

1. **κ measures machine–machine agreement, not correctness.** Both passes share the vocabulary and the greedy family, so high κ (0.98) is expected and claims nothing about gold accuracy.
2. The dual-segmented subset contains **true compounds correctly split** (दोषभाष्यम् → दोष | भाष्यम्) **and false positives**: sandhi-fused word sequences (पुरुषस्येति = पुरुषस्य इति) and over-split simple inflected words (निष्ठायां → निष्ठा | यां). Precision is unknown pending the human sheet.
3. Dual coverage is ~8–9% of the candidate bank — most long tokens resist segmentation by a ≤7-char simple-word vocabulary (member-internal sandhi, morphology). The bank itself is the full census.
4. Bracket-node labelling (which member modifies which) is **deferred to v2** — deliberately not fabricated (`tree: null`).

## Reproduce

```
python3 scripts/mbh_klammer.py --fetch    # populate gitignored source/ mirror
python3 scripts/mbh_klammer.py --build    # rebuild every committed artifact
python3 scripts/mbh_klammer.py --check    # parity gate (CHECK PASS)
python3 scripts/mbh_klammer.py --selftest
```

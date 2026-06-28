# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

> Two broader instruction files already load above this one: the global `~/.claude/CLAUDE.md`
> and the org-level `GitHub/CLAUDE.md` (Sanskrit Lexicon spine). This file is **repo-specific**
> and does not repeat them. The deepest cold-start briefing for this repo is
> [docs/GEMINI.md](docs/GEMINI.md) — read it first for domain context; read
> [.ai_state.md](.ai_state.md) at the start of every session for live state.

## What this repo is

A scholarly corpus + Python tooling for the comparative study of **commentary strategies**
used by Russian academic translators of Sanskrit texts (Mahābhārata, Rāmāyaṇa, Upaniṣads).
Output is **peer-reviewed articles** (`articles/`, `tronsky-XXX/`) plus a FAIR/DH corpus.
It is *not* an application — there is no server or build artifact to ship; the deliverables
are JSON data, generated TEI/HTML, and Markdown articles.

Two corpus tiers — **do not conflate them**:
| Tier | Size | Where |
|---|---|---|
| Analytical (full material) | 17 863+ annotations, 7 translators | hand-written `*_commentary_analysis.html` (repo root) |
| Marked-up **gold sample** | 300 notes (6×50), 4 axes | [data/](data/)`{translator}_markup_50.json` |

The gold sample is the machine-readable source of truth; the hand-written HTML essays are
richer prose *outside* the pipeline — never regenerate or overwrite them from data.

## The data → artifacts pipeline (core architectural rule)

**Edit JSON, never the generated outputs.** `tei/`, `pages/`, and `visualizations.html` are
all rebuilt from `data/`. Hand-written `*_commentary_analysis.html` files at the repo root are
the exception: they are authored, not generated, and the CI corpus job deliberately leaves them
alone. See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) §4 for the full flow.

```
data/{translator}_markup_50.json   ── source of truth (4-axis gold sample)
    ├─ derive_urn.py     → injects/validates CTS-URN field
    ├─ export_tei.py     → tei/{translator}.xml  (TEI P5)
    ├─ build_pages.py    → pages/{translator}.html (table view, NOT the essays)
    └─ profile_translator.py → axis profiles (stdout)
```

### Commands

```sh
# Corpus integrity (mirrors the CI "corpus" job — run before committing data changes)
python scripts/validate.py            # forbidden strings + schema-subset + HTML structure
python scripts/derive_urn.py --check  # CTS-URN book↔number cross-check; nonzero on drift

# Regenerate ALL data-derived artifacts (CI fails if these leave a git diff)
python scripts/export_tei.py
python scripts/build_pages.py
python scripts/parse_formulas.py
python scripts/profile_nilakantha.py            # needs indic-transliteration
python scripts/extract_false_friends_profile.py
python scripts/build_visualizations.py

# LLM annotation pipeline (gated on ANTHROPIC_API_KEY)
python scripts/annotate_batch.py kalyanov --limit 5   # claude-haiku-4-5 default, resumable
python scripts/eval_pipeline.py kalyanov --verbose    # accuracy vs gold, threshold ≥85%
```

There is **no test suite** — CI's "Pytest" job is a no-op stub. The real gate is the
**Corpus integrity** job ([.github/workflows/ci.yml](.github/workflows/ci.yml)): `validate.py`
+ URN cross-check + "every generator reproduces its artifact with no git diff". Lint is `ruff`
and format is `black` (both warn-only / non-blocking).

## Sundarakāṇḍa commentary pipeline (the active workstream)

Most current churn is generating Russian scholarly notes for Rāmāyaṇa V (Leonov/Kostina).
The generators are deterministic Python (a hand-curated `REGISTRY`/KB, not live LLM calls),
each writing per-chapter JSON under `data/`:

- `data/sundara_ch{N}_commentary_to_add.json` — accepted notes per chapter (ch. 1–68)
- `data/lexical/ch{N}.json` + `ch{N}.rejected.json` — lexical/etymological gloss layer; every
  rejected candidate keeps its `reject_reason` (the adversarial pass *is* the quality signal)
- `data/sundara_decision_ledger.json` + [SUNDARA_COMMENTARY_RATIONALE.md](SUNDARA_COMMENTARY_RATIONALE.md) — accept/reject ledger for the whole book
- `scripts/sundara_*.py`, `scripts/crosstext_*.py`, `scripts/lexical_pilot.py` — the generators

These scripts read verse text from a **sibling repo**: `GitHub/SamudraManthanam/web/corpus_builder/jsonl/`
(hardcoded absolute paths). That repo and dictionary JSONL (`dic_mw`, `dic_apte`, `kochergina`,
`warnemyr`) must be present locally; the scripts are not self-contained.

Design target for new lexical notes: **~25% density (Grintser level)** with a strict adversarial
gate (reject transparent p.p.p., standard epithets, compounds whose meaning = sum of parts, and
in-chapter root duplicates). See [data/lexical/PILOT_REPORT.md](data/lexical/PILOT_REPORT.md).

## The 4-axis annotation framework

Every gold-sample note carries coordinates on 4 axes (canonical enum: [data/commentary_schema.json](data/commentary_schema.json)):
1. **Topic** — 9 empirical rubrics (`sanskrit_term`, `myth`, `realia`, `poetics`, …)
2. **Kazansky 2025** — A philological / B **textological** (metatext on source/translation
   state — *not* realia) / V historical-cultural & realia / G cultural. Realia go in **V, never B**.
3. **Lidova 2024** — L1–L5 *lakṣaṇa*
4. **Paribok 2011** — **P/K/D** (concept / culturally-loaded / codifier). *Note:* `docs/ARCHITECTURE.md`
   historically mislabels this "P/C/K" in places — the schema and data are authoritative: **P/K/D**.

Verse addressing is canonical **CTS-URN** (`urn:cts:sanskritLit:<work>:<passage>`), one work per
epic, book = first passage element — derived deterministically by `derive_urn.py`.

## Hard rules (from docs/GEMINI.md — `validate.py` enforces the first two)

1. **No «М.: Наука, 2022» for Leonov** — that volume does not exist; use "продолжающийся перевод; лит. ред. Е. Костина".
2. **«Парибка»** is the only correct oblique form (never Парибока/Парибоку/Парибоо).
3. **Never add a 5th analytical axis** without explicit user permission.
4. Don't cite the 5 traditional Rāmāyaṇa commentators or use Kazansky's name in the article title.

Run `python scripts/validate.py` after any content edit to catch 1–2.

## Conventions

- **Python**: stdlib-only by default (3.10+); third-party only in `annotate_batch.py` (`anthropic`)
  and `profile_nilakantha.py` (`indic-transliteration`). Every script starts with
  `sys.stdout.reconfigure(encoding='utf-8')` / `sys.stderr.reconfigure(...)`.
- **No BOM**: write files with `open(f, 'w', encoding='utf-8')`, never `utf-8-sig`.
- **`.ai_state.md`** is the tracked session journal — keep its `Next Steps / WIP / Dev Notes /
  Completed` sections current (org `GitHub/CLAUDE.md` mandates this) and micro-commit with the
  `ai-wip:` prefix after logical milestones.
- Generated web-asset dumps (`महाभारत_files/`, `Рамаяна…_files/`) are committed but noise —
  `validate.py` skips them; don't treat them as source.

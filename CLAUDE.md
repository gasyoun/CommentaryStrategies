# CLAUDE.md

_Created: 28-06-2026 · Last updated: 26-08-2026_

A scholarly corpus + Python tooling for the comparative study of **commentary
strategies** used by Russian academic translators of Sanskrit texts
(Mahābhārata, Rāmāyaṇa, Upaniṣads). Deliverables are peer-reviewed articles
(`articles/`, `tronsky-XXX/`) plus a FAIR/DH corpus — not a server.

Org conventions live in [`../CLAUDE.md`](https://github.com/gasyoun/github-spine/blob/main/CLAUDE.md).
Before encodings or corpus data, read the
[Sanskrit context primer](https://github.com/gasyoun/github-spine/blob/main/SANSKRIT_CONTEXT_PRIMER.md).
Cold-start briefing:
[docs/GEMINI.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/GEMINI.md).
Live queue:
[.ai_state.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/.ai_state.md).

## Two corpus tiers — do not conflate

| Tier | Size | Where |
|---|---|---|
| Analytical (full material) | 17 863+ annotations, 7 translators | hand-written `*_commentary_analysis.html` (repo root) |
| Marked-up **gold sample** | 300 notes (6×50), 4 axes | [`data/{translator}_markup_50.json`](https://github.com/gasyoun/CommentaryStrategies/tree/main/data) |

The gold sample is the machine-readable source of truth. Hand-written HTML
essays are richer prose *outside* the pipeline — never regenerate or
overwrite them from data.

## How to run

**Edit JSON, never the generated outputs.** `tei/`, `pages/`, and
`visualizations.html` rebuild from `data/`. Architecture:
[docs/ARCHITECTURE.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/ARCHITECTURE.md).

```sh
python scripts/validate.py
python scripts/derive_urn.py --check
python scripts/export_tei.py
python scripts/validate_tei_rng.py   # RelaxNG vs tei_all; SKIP without xmllint/schema
python scripts/build_pages.py
python scripts/parse_formulas.py
python scripts/profile_nilakantha.py
python scripts/extract_false_friends_profile.py
python scripts/build_visualizations.py
```

There is **no real test suite** — CI's Pytest job is a stub. The gate is the
**Corpus integrity** job in
[`.github/workflows/ci.yml`](https://github.com/gasyoun/CommentaryStrategies/blob/main/.github/workflows/ci.yml):
`validate.py` + URN check + "every generator reproduces its artifact with no
git diff". `ruff` / `black` are warn-only.

LLM annotation (needs `ANTHROPIC_API_KEY`):

```sh
python scripts/annotate_batch.py kalyanov --limit 5
python scripts/eval_pipeline.py kalyanov --verbose
```

Sundarakāṇḍa generators (Leonov/Kostina) are deterministic Python, not live
LLM. They read verse text from sibling
`GitHub/SamudraManthanam/web/corpus_builder/jsonl/` (hardcoded paths). Operator
docs: [docs/MANUAL.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/MANUAL.md)
and the three role guides (`LEONOV_` / `KOSTINA_` / `GASUNS_SUNDARAKANDA_GUIDE.md`).
Changing sheet/apply/page mechanics updates MANUAL **and** the affected
guides in the same PR.

## 4-axis gold sample

Canonical enum:
[data/commentary_schema.json](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/commentary_schema.json).
Topic · Kazansky 2025 (A/B/V/G — realia go in **V, never B**) · Lidova L1–L5 ·
P/K/D operational note-depth (not Paribok's term typology —
[docs/AXIS4_KD_DECISION.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/AXIS4_KD_DECISION.md)).
Verse addressing is CTS-URN via `derive_urn.py`.

## Hard rules (`validate.py` enforces the first two)

1. No «М.: Наука, 2022» for Leonov — that volume does not exist.
2. «Парибка» is the only correct oblique form.
3. Never add a 5th analytical axis without explicit permission.
4. Human review artifacts are interactive HTML with a decisions export —
   never Markdown checkbox sheets.

## Do not touch

- Hand-written `*_commentary_analysis.html` at repo root.
- Generated `tei/`, `pages/`, `visualizations.html` — regenerate.
- Generated web-asset dumps (`महाभारत_files/`, `Рамаяна…_files/`) — untracked and
  `.gitignore`d since 26-08-2026 (H3558); still on disk, still not repo material.
  The two parent `.html` saved pages **stay tracked** — they are the source the
  Sundarakāṇḍa extractors read; a fresh clone renders them unstyled, by design.
- UTF-8 BOM — `encoding='utf-8'`, never `utf-8-sig`.

Danger facts:
[Uprava DANGER_FACTS.md](https://github.com/gasyoun/Uprava/blob/main/DANGER_FACTS.md)
and the generated block of
[AGENTS.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/AGENTS.md).

_Dr. Mārcis Gasūns_

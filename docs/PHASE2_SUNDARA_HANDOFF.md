# Phase 2 — Sundarakāṇḍa Sanskrit-commentator dialogue layer · build handoff

> **Status: SCOPED, ready to build. Rights cleared 2026-07-01.** This is the density-lift layer that
> takes the Sundara apparatus from Phase-1 **24.2 %** toward Leonov/Kostina's own **~36 %**, by putting
> the Russian translation into dialogue with the traditional Sanskrit commentaries — now that those
> commentaries are locally available and licensed.
>
> Cold-start reading order: [`docs/GEMINI.md`](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/GEMINI.md) →
> [`.ai_state.md`](https://github.com/gasyoun/CommentaryStrategies/blob/main/.ai_state.md) →
> this file → [`SUNDARA_COMMENTARY_RATIONALE.md`](https://github.com/gasyoun/CommentaryStrategies/blob/main/SUNDARA_COMMENTARY_RATIONALE.md).

## 1. What Phase 2 is (and is not)

Phase-1 built three layers from **dictionaries** (`base` 95 + `lexical` 611 + `cross_text` 71 +
`hist_cultural` 11 = **788 notes, 24.2 %**, all `review_required`). Those are deterministic Python glosses
of *terms*. Phase 2 is different in kind: it is the **Type Б commentator-dialogue layer** — notes that
report what the traditional Sanskrit commentators (Tilaka / Bhūṣaṇa / Śiromaṇi …) actually *say* about a
verse (a gloss, a disambiguation, a supplied ellipsis, a variant, a grammatical parse), rendered as a
terse Russian scholarly note in the **Литературные памятники (ЛП)** register.

It is **not** a translation of the commentaries, and **not** a running Sanskrit-language ṭīkā. It is a
distilled затекстовое примечание in the ЛП house style — the style of Grintser's Rāmāyaṇa (books I–III,
Ладомир/ЛП), which is the density and tone benchmark for this whole project.

**Decision already taken (C0/D2, 2026-07-01, M.G.): apparatus model II — two-tier hybrid.** Tier 1 = print
minimum; tier 2 = the digital philological layer. Phase-2 notes belong to **tier 2**. Tier-2 must remain
compatible with Leonov/Kostina's own notes sitting verbatim alongside.

## 2. Inputs (all present locally, rights CLEARED)

- **Commentaries** (Devanagari Sanskrit, one file per commentary × sarga):
  [`data/valmiki_commentaries/kanda_5_sundarakanda/`](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/valmiki_commentaries/kanda_5_sundarakanda)
  — `tilaka_sarga_{NN}.txt`, `bhusana_sarga_{NN}.txt`, `siromani_sarga_{NN}.txt`, `tattvadipika_sarga_{NN}.txt`.
  Each file interleaves commentary prose with verse markers `।। 5.<sarga>.<verse> ।।` → **segmentable by verse deterministically**.
- **Sundara coverage of the commentaries** (usable cells): **tilaka 66, bhūṣaṇa 68, śiromaṇi 65** of 68 sargas.
  `tattvadipika` only 6; `kataka`/`dharmakutam`/`tanisloki` = 0 in Sundara. → the layer rests on **tilaka + bhūṣaṇa + śiromaṇi**.
- **Verse text + Leonov подстрочник**: sibling repo `GitHub/SamudraManthanam/web/corpus_builder/jsonl/05_ramayana-sundarakanda.jsonl`
  (the `#ru` field IS Leonov's literal layer — never cite «М.: Наука 2022»; see hard rule).
- **Existing apparatus** to dedup against: [`data/sundara_commentary_to_add.json`](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/sundara_commentary_to_add.json)
  (788 notes) + per-chapter `data/lexical/ch{N}.json`.
- **Coverage / density map**: [`data/analysis/sundara_coverage.json`](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/analysis/sundara_coverage.json)
  — 🟢20 / 🟡14 / 🔴11 / ⚪23. The **14 🟡 sargas (22, 24, 26, 30, 34–37, 39, 51)** are "commentary-rich but
  Leonov-annotation-thin" → the highest-yield first targets.

## 3. Build architecture (proposed)

Mirror the proven Phase-1 pattern: **deterministic segmentation + candidate generation → adversarial reject
gate → `review_required` merge**, many SMALL parallel agents (~3 sargas each), write-only, central merge.

1. `scripts/extract_yellow_sargas.py` (already queued in `.ai_state.md`) — segment each Sundara commentary
   file by `।। 5.s.v ।।` markers → per-verse bundles `{verse_id, tilaka?, bhusana?, siromani?, leonov_ru, sanskrit}`.
   Output `data/analysis/sundara_commentary_segmented.json` (deterministic, no LLM). Start with the 14 🟡 sargas.
2. **Candidate note generation** — per verse, decide whether the commentators add something the подстрочник
   can't give, and if so write a ЛП-register Russian note. **This step needs Sanskrit→Russian distillation**
   → not deterministic; see OPEN DECISION #4 (LLM backend is DeepSeek via the openai-compat pipeline, no
   Anthropic key). Every candidate `review_required: true`, `subtype: "commentator"`, Kazansky type per §4.
3. **Adversarial reject gate** — same discipline as lexical: reject notes that (a) merely restate the
   подстрочник, (b) are pure Sanskrit grammar invisible to a Russian reader, (c) duplicate an existing note
   (global lemma/verse dedup). Keep every rejection with `reject_reason` (the reject log IS the quality signal).
   Target reject rate ≥ 50 % — if it's padding, quality drops.
4. **Merge** — deterministic Python, global dedup keep-first, into `data/sundara_ch{N}_commentary_to_add.json`
   + rebuild `data/sundara_book_stats.json` + the report `leonov_sundara_corpus_enriched.html`.

**Density math:** 24.2 % → ~36 % over 2 859 verses ≈ **+340 accepted notes**. Do the 14 🟡 sargas first
(pilot + highest yield), measure, then decide whether to extend to 🔴/⚪.

## 4. ЛП (Литературные памятники) style contract — the notes must obey this

The register is the whole point; get it wrong and it isn't publishable. Grintser's Rāmāyaṇa is the model.
- **Terse, затекстовое.** One–three sentences. No essay. No block quotes of Sanskrit.
- **Russian scholarly voice**, not a translation of the commentator's syntax.
- **Realia → V, textological/what-the-text-says → Б** (Kazansky). Realia never go in Б.
- Sanskrit lemmas in **IAST**, sparingly (Grintser ≈12 % IAST — do not exceed the calibrated band).
- **«Парибка»** is the only correct oblique form; obey all `validate.py` hard rules.
- Never attribute a Leonov note to «М.: Наука 2022» (nonexistent volume).

## 5. OPEN DECISIONS (to confirm with M.G. before generating) — resolved values fill in here

- **[D-P2-1] First-build scope** — pending.
- **[D-P2-2] Commentator attribution in the reader-facing note** — pending. (ЛП house style tends to an
  anonymous scholarly voice; hard-rule #4 forbids naming the traditional commentators *in the article
  title* — unclear whether that sensitivity extends to the apparatus.)
- **[D-P2-3] Note rendering form** (distilled RU only · RU + IAST pratīka · short quoted Sanskrit + RU) — pending.
- **[D-P2-4] Generation method** (DeepSeek/openai-compat LLM distillation + gate · deterministic
  extract-only, human writes RU · hybrid) — pending.
- **[D-P2-5] Density target** — pending (default: ~36 %, Leonov parity).

## 6. Guardrails carried over

- Corpus is multi-actor: verify end-state on `origin/main`; prefer branch + PR; central merge only.
- `review_required: true` on every generated note — nothing is editor-approved until Leonov/Kostina sign off.
- CI corpus gate must stay green: `python scripts/validate.py` + `python scripts/derive_urn.py --check`.
- Attribution obligation: any deposit/redistribution carries the Gita Supersite permission string (CC BY 4.0).

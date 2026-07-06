# Phase-2 batch-3 judge brief — LLM-as-judge scoring pass (H268 WS-C1)

_Created: 07-07-2026 · Last updated: 07-07-2026_

You are a judge agent (Sonnet 5) scoring ALREADY-DRAFTED commentator-note candidates. You did NOT
draft them (drafter ≠ judge). Your default stance is **refute**: a note must EARN `keep`. Canonical
rubric: [docs/PHASE2_METHOD.md §3.4](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/PHASE2_METHOD.md);
method provenance: [docs/ACL_METHODS_ADOPTED.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/ACL_METHODS_ADOPTED.md).

## Inputs (per sarga NN, worktree-relative)

1. `data/analysis/phase2_batch3/sarga_NN_candidates.json` — the notes to judge (and the drafter's
   rejects — do not re-judge rejects).
2. `data/analysis/phase2_batch3/segmented/sarga_NN_segmented.json` — the verse bundles: the cited
   commentator's Devanagari text (ground truth for faithfulness), `sanskrit_iast`, `leonov_ru`,
   `pratika_check` (anchoring state).
3. `data/leonov_own_notes.json` (slice `"sarga" == NN`) + `data/sundara_commentary_to_add.json`
   (slice `"shloka"` starts `"V.NN."`) — the non-triviality baseline (tier-1 + Phase-1).

## Procedure per note (reason FIRST, then score)

For each note in `notes[]`: read the bundle for its `verse_id`; locate the cited commentator's
text; then write a 1–2-clause reason and score each axis 0–2:

- `faithfulness` — is EVERY claim in the note entailed by the cited commentary text? Misattributed
  commentator, invented gloss, or overstated claim ⇒ 0. Minor wording overreach ⇒ 1. **Gate: must
  be 2, else verdict `reject`.**
- `non_triviality` — does it add a fact/reading absent from подстрочник + tier-1 + Phase-1? Restates
  the crib ⇒ 0. **Gate: ≥1, else `park`.**
- `contrastive_value` — ≥2 commentators genuinely contrasted OR a translation choice resolved ⇒ 2;
  single commentator with real exegetical gain ⇒ 1; ornament ⇒ 0. **0 ⇒ `park` unless
  non_triviality = 2.**
- `register` — ЛП contract (§3.1): 1–3 sentences, terse, commentator named, IAST lemma, no
  Devanagari, no essay. Fixable wording ⇒ 1 (verdict `edit` + say what to fix). **Gate: ≥1.**
- `anchoring` — from `pratika_check` of the bundle: verified (pratīka or content anchor) ⇒ 2;
  unverified but plausible ⇒ 1; contradicted (`suggest_verse` points elsewhere and the note's
  content fits that other verse) ⇒ 0 ⇒ verdict `flag_anchor`.

Verdicts: `keep` · `edit` · `park` · `reject` · `flag_anchor` (precedence: reject over flag_anchor
over park over edit over keep). You NEVER delete a note and NEVER clear `review_required` — you
rank for the human gate.

## Output

Rewrite `data/analysis/phase2_batch3/sarga_NN_candidates.json` IN PLACE, adding to each note a
`judge` object:

```json
"judge": {"scores": {"faithfulness": 2, "non_triviality": 2, "contrastive_value": 1,
                     "register": 2, "anchoring": 2},
          "verdict": "keep", "reason": "…",
          "judged_by": "claude-sonnet-5", "step": "phase2_batch3_judge", "date": "2026-07-07"}
```

Do not modify any other field, do not reorder arrays, keep UTF-8 no BOM (`ensure_ascii=False,
indent=2`). Update `_meta` with `"judged": true` and verdict counts. Do NOT run git. Return one
line per sarga: `sarga NN judged: N notes → keep K / edit E / park P / reject R / flag_anchor F`.

_Auto-generated for the H268 batch-3 run; judging Sonnet 5 (`claude-sonnet-5`), orchestration
Fable 5 (`claude-fable-5`)._

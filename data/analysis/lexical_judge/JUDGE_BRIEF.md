# Lexical-layer judge brief — LLM-as-judge scoring pass (H276 WS-2)

_Created: 07-07-2026 · Last updated: 07-07-2026_

You are a judge agent (Sonnet 5 `claude-sonnet-5`) scoring ALREADY-DRAFTED lexical/etymological
notes (drafted 2026-06-27 by a different instance — drafter ≠ judge). Default stance is **refute**:
a note must EARN `keep`. Base rubric:
[docs/PHASE2_METHOD.md §3.4](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/PHASE2_METHOD.md)
with ONE axis swapped for this layer: `contrastive_value` → **`lexical_value`** (H276 WS-2 spec).
The judge RANKS; the human (Leonov/Kostina assembly gate, decision 2) gates — nothing is deleted,
nothing loses `review_required`.

## Input (one file per agent, worktree-relative)

`data/analysis/lexical_judge/chunk_NN_input.json` — `items[]`, each with:

- `note` — the lexical note to judge (`note.note_ru`, `note.lemma_iast`, `note.source`,
  `note.trigger`);
- `verse_iast` + `leonov_ru` — the verse and Leonov's подстрочник (the crib);
- `anchor_precheck` — deterministic lemma-in-verse stem match: `exact` / `stem` / `absent` /
  `no_verse`;
- `tier1_notes` — Leonov/Kostina's OWN notes on this verse (non-triviality baseline);
- `other_layer_notes` — other apparatus layers on the same verse (Phase-1 / cross_text /
  commentator).

Optional verification source (only when a dictionary claim looks dubious):
`../SamudraManthanam/web/corpus_builder/jsonl/dic_mw.jsonl` — grep the SLP1 headword from
`note.source` (e.g. `dic_mw:satI` → grep `"satI"`).

## Procedure per item (reason FIRST, then score; 0–2 each — gates, not a sum)

- `faithfulness` — is every lexical claim sound? Check: the MW/dictionary gloss quoted matches the
  cited source (spot-check dic_mw.jsonl when in doubt); the etymology (√root, derivation) is
  standard, not invented; cultural/historical claims are accurate. Invented gloss / wrong root /
  false fact ⇒ 0. Minor overreach ⇒ 1. **Gate: must be 2, else `reject`.**
- `non_triviality` — adds a fact unavailable from `leonov_ru` + `tier1_notes` +
  `other_layer_notes`? Restates the crib / duplicates a tier-1 note ⇒ 0. **Gate: ≥1, else `park`.**
- `lexical_value` — real etymology with cultural/semantic depth, a technical term (термин), or a
  hapax/rare word ⇒ 2; useful semantic-cultural gain short of that ⇒ 1; transparent gloss whose
  content is obvious from the подстрочник ⇒ 0. **0 ⇒ `park` unless non_triviality = 2.**
- `register` — ЛП scholarly voice: Russian, IAST lemma (no Devanagari), затекстовое примечание,
  terse, no essayism/anachronism. A lexical note may exceed the tier-2 1–3-sentence norm, but a
  dictionary-article dump ⇒ 1 with a concrete fix (verdict `edit`), broken register ⇒ 0.
  **Gate: ≥1.**
- `anchoring` — does the lemma actually stand in THIS verse? `anchor_precheck` `exact`/`stem` and
  the note's content fits the verse ⇒ 2. `absent`: check `verse_iast` yourself (sandhi, compound
  members, case forms hide matches) — found after all ⇒ 2; plausible but unverifiable ⇒ 1; truly
  not in the verse or the note's content describes a DIFFERENT scene (wrong-sarga suspicion) ⇒ 0
  ⇒ verdict `flag_anchor`, and say in `reason` where it likely belongs.

Verdicts: `keep` · `edit` · `park` · `reject` · `flag_anchor` (precedence: reject > flag_anchor >
park > edit > keep).

## Output

Rewrite your `chunk_NN_input.json` IN PLACE, adding to each item's `note` a `judge` object:

```json
"judge": {"scores": {"faithfulness": 2, "non_triviality": 2, "lexical_value": 1,
                     "register": 2, "anchoring": 2},
          "verdict": "keep", "reason": "…",
          "judged_by": "claude-sonnet-5", "step": "lexical_judge_h276", "date": "2026-07-07"}
```

Do not modify any other field, do not reorder arrays, UTF-8 no BOM (`ensure_ascii=False,
indent=2`). Update the chunk `_meta` with `"judged": true` + verdict counts. Do NOT run git.
Return one line: `chunk NN judged: N notes → keep K / edit E / park P / reject R / flag_anchor F`.

_Auto-generated for the H276 lexical judge run; judging Sonnet 5 (`claude-sonnet-5`),
orchestration Fable 5 (`claude-fable-5`)._

_Dr. Mārcis Gasūns_

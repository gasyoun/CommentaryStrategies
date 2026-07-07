# Sarga-12 re-draft brief — corrected sourcing protocol (H276 WS-3a)

_Created: 07-07-2026 · Last updated: 07-07-2026_

The 2026-07-07 batch-3 drafting of sarga 12 failed the judge pass 0/3: **every note cited a
commentator whose text is absent from that verse's bundle** (e.g. «по Тилаке» where the bundle has
only bhūṣaṇa + śiromaṇi), with content found in none of the present commentaries — fabricated
attribution. This re-draft replaces it under the same contract
([DRAFTING_BRIEF.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/analysis/phase2_batch3/DRAFTING_BRIEF.md),
[docs/PHASE2_METHOD.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/PHASE2_METHOD.md)
§3.1–3.3) with TWO hard additions:

1. **Quote-or-drop.** Every note MUST carry a `source_quote` field: the exact Devanagari span(s),
   copied verbatim from `commentary.<name>` of THAT verse's bundle in
   `segmented/sarga_12_segmented.json`, that entail every claim in the note. One quote per cited
   commentator. If you cannot paste a span that supports the claim — the note does not exist.
   Paraphrase-from-memory of what a ṭīkā "usually says" is the exact failure being corrected.
2. **Cited ⊆ present.** `source_commentary` may list only commentators with a non-empty text in
   the bundle for that verse_id. Sarga-12 coverage for orientation: bhūṣaṇa 24 verses,
   śiromaṇi 15, tilaka 13; 19 verses have ≥2 commentators (contrastive-first applies there).

Everything else per the original brief: dedup against Leonov/Kostina tier-1
(`data/leonov_own_notes.json`, sarga 12) + Phase-1 notes (`data/sundara_commentary_to_add.json`,
shloka `V.12.*`); ЛП register §3.1; `why_proposed`; every rejection logged with reason + bucket;
output schema identical to the other `sarga_NN_candidates.json` files (notes[] + rejected[] +
_meta), plus the new `source_quote` per note; all notes `review_required: true`.

Write to `data/analysis/phase2_batch3/sarga_12_candidates.json` (overwrite the failed set —
its 3 rejected notes are preserved by the judge log inside git history and the judge verdicts
were `reject` anyway; note the redraft in `_meta`: `"redraft": "H276 WS-3a, corrected sourcing
protocol"`). Do NOT run git.

_Auto-generated for the H276 sarga-12 re-draft; drafting Sonnet 5 (`claude-sonnet-5`),
orchestration Fable 5 (`claude-fable-5`)._

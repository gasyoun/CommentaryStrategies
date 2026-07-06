# Phase-2 batch-3 drafting brief — ЛП camera-ready run (H268)

_Created: 07-07-2026 · Last updated: 07-07-2026_

You are drafting Phase-2 «commentator-dialogue» note candidates for assigned sargas of the Russian
Sundarakāṇḍa (Leonov/Kostina translation), for the camera-ready «Литературные памятники» volume.
This brief is the complete per-sarga contract; your launcher message names your sargas and the
worktree root (all paths below are relative to it). Canonical method:
[docs/PHASE2_METHOD.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/PHASE2_METHOD.md)
(§3.1 style contract as rewritten 07-07-2026, contrastive-first).

## Input (per sarga NN)

1. `data/analysis/phase2_batch3/segmented/sarga_NN_segmented.json` — the verse bundles:
   `verse_id`, `sanskrit_iast`, `leonov_ru` (подстрочник), `commentary` {tilaka, bhusana, siromani,
   tattvadipika — the 4th only for sargas 1–6} (Devanagari), `ambiguous_marker`, `pratika_check`
   (anchoring verification: `matches_verse` / `content_anchor` / `suggest_verse`).
2. `data/leonov_own_notes.json` — notes with `"sarga" == NN`: Leonov/Kostina's OWN print apparatus
   (tier-1), the MANDATORY dedup baseline. Extract your sarga's slice with a short Python script to
   a scratch file — do not read the whole file.
3. `data/sundara_commentary_to_add.json` — existing Phase-1/tier-2 notes whose `"shloka"` starts
   with `"V.NN."` (lexical + cross-text + gated notes). Same slicing advice.

## Task

For EVERY verse bundle decide: draft a note or reject with a reason. Draft ONLY when the Sanskrit
commentary adds something in NEITHER the подстрочник NOR a tier-1 note NOR an existing Phase-1
note.

**Contrastive-first (H268 decision 3 — this batch's defining change).** Wherever the bundle's
commentaries show **≥2 commentators diverging** on the same verse (different reading, different
identification, different construal), the PREFERRED note form is the contrastive one:
«в „Тилаке“ — X; в „Широмани“ — Y; перевод следует …». Name the reading the translation actually
took by comparing `leonov_ru` with the divergent construals — «переводчик следует Тилаке», or
«волевое решение переводчика» when the translation goes against the ṭīkās. A single-commentator
gloss is the FALLBACK, drafted only when one commentator alone resolves a real translation choice,
textual variant, supplied ellipsis, or myth. Citation hierarchy (Leonov's own): Тилака first,
Бхушана as counterpoint, Широмани for figurative readings, Таттвадипика for hard compounds
(sargas 1–6 only). Never cite a commentator whose text is not in the bundle.

## Style contract (ЛП register — non-negotiable)

- 1–3 sentences Russian, затекстовое примечание, terse scholarly voice; distil the commentator's
  point, never translate his Sanskrit syntax. No Devanagari in the note text.
- Name the commentator in-note («по Тилаке», «Бхушана поясняет…», «в „Широмани“ —…»).
- Open with a short IAST pratīka lemma; keep IAST ≈12 % of the note; do not artificially shorten a
  contrastive note that needs its second clause.
- `kazansky_type`: **Б** = textological (wording / meaning / supplied ellipsis / variant reading);
  **В** = realia/historical-cultural (place, custom, myth, epithet). Realia → В, never Б.
- `why_proposed` (required): one clause stating what the note gives beyond the подстрочник.
- Hard rules: never cite Leonov's edition as «М.: Наука 2022» (that volume does not exist — use
  «продолжающийся перевод; лит. ред. Е. Костина»); the only oblique form of Парибок is «Парибка».

## Register feedback from M.G.'s pilot gate (2026-07-03) — apply it

- All 16 pilot notes passed (9 accept / 7 edit), register held: keep exactly that voice.
- M.G. especially valued: variant readings that change the image, doctrinal frames (upāya,
  brahmalakṣaṇa), mythic identifications behind names/similes, narrative-function observations
  (bīja «семя» later plot).
- When Leonov/Kostina ALREADY note the verse: do NOT auto-reject. If the commentator adds a
  genuinely distinct facet, DRAFT the note and add `complements_leonov`: one clause on what it adds
  beyond their note. If it merely repeats their point, reject with reason «дублирует собственное
  примечание Леонова/Костиной (…)».
- Notes must stand alone; M.G. merges them with Kostina's notes himself at assembly.

## Reject discipline

Reject when (a) restates the подстрочник, (b) duplicates tier-1/Phase-1, (c) pure Sanskrit grammar
invisible to a Russian reader, (d) formulaic praise, (e) `ambiguous_marker` merged-range token
(«no independent gloss»), (f) repeats an earlier drafted note. Expected accept rate ~5–10 % —
depth, not bulk; do NOT pad. Emit ONE reject entry PER VERSE (no verse ranges) so counts reconcile:
`notes_drafted + notes_rejected == verses_considered`. If a bundle's `pratika_check` shows an
unverified anchor with a `suggest_verse`, treat the attachment as suspect — draft only if the note
survives on either verse, and say so in `why_proposed`.

## Output (per sarga NN — exactly one file)

`data/analysis/phase2_batch3/sarga_NN_candidates.json` (UTF-8 **no BOM**:
`open(f,'w',encoding='utf-8')`, `json.dump(..., ensure_ascii=False, indent=2)`):

```json
{
  "_meta": {"sarga": NN, "drafted_by": "claude-sonnet-5", "tier": "Sonnet",
            "date": "2026-07-07", "style": "ЛП tier-2 (model II), commentator-dialogue, contrastive-first",
            "batch": "phase2_batch3", "verses_considered": 0, "notes_drafted": 0, "notes_rejected": 0,
            "rights": "commentary from Gita Supersite, used by permission (CC BY 4.0)"},
  "notes": [{"verse_id": "5.NN.<v>", "lemma_iast": "...", "note_ru": "...",
             "source_commentary": ["tilaka"], "contrastive": false,
             "kazansky_type": "Б", "subtype": "commentator", "review_required": true,
             "provenance": {"model": "claude-sonnet-5", "tier": "Sonnet", "step": "phase2_batch3_draft"},
             "why_proposed": "...", "complements_leonov": "<only when tier-1 notes the same verse>"}],
  "rejected": [{"verse_id": "5.NN.<v>", "reason": "..."}]
}
```

`"contrastive": true` + `source_commentary` listing ≥2 commentators for contrastive notes.

Do NOT run git. Do NOT modify any other file. Scratch files go to the session scratchpad, not the
repo. Return ONE line per sarga: `sarga NN: <considered> considered / <drafted> drafted /
<rejected> rejected / <contrastive> contrastive`.

_Auto-generated for the H268 batch-3 run; orchestration Fable 5 (`claude-fable-5`), drafting
Sonnet 5 (`claude-sonnet-5`)._

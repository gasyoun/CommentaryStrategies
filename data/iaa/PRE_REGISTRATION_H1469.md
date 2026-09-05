# Pre-registration — H1469 axis_2 / axis_4 blind second-annotator IAA

_Created: 24-07-2026 · Last updated: 24-07-2026_

**Status:** pre-registered **before** Pass B (blind LLM) runs on the five
translators lacking a second pass. Kalyanov already has a committed DeepSeek
Pass B (`data/kalyanov_full.json`); that artifact is re-used, not re-tuned.

**Handoff:** [H1469](https://github.com/gasyoun/Uprava/blob/main/handoffs/archive/H1469-Opus_CommentaryStrategies_commentarystrategies-axis2-axis4-blind-annotator-kappa_22.07.26.md)
**Protocol:** [PROTOCOL_BLIND_LLM_SECOND_ANNOTATOR_RELIABILITY_2026.md](https://github.com/gasyoun/Uprava/blob/main/docs/PROTOCOL_BLIND_LLM_SECOND_ANNOTATOR_RELIABILITY_2026.md)
(org C3 discipline; ruling D2 — agent-run blind LLM second annotator)

## Instrument

| Field | Value |
|---|---|
| Axes | `axis_2_kazansky` ∈ {A, B, V, G}; `axis_4_paribok` ∈ {P, K, D} |
| Codebook | [prompts/classify_note.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/prompts/classify_note.md) + human sheet [sources/B5_ANNOTATION_GUIDE.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/sources/B5_ANNOTATION_GUIDE.md) |
| Gold sample | 300 notes = 6 translators × 50 (`data/{translator}_markup_50.json`) |
| Scope reading | B5 roadmap text says "50 notes × 2 axes"; SUBMISSION_READINESS_A19 says 50-per-translator. **Full 300-note set is on disk and is the analysis frame** (documented here). |
| Pass A | Model-generated (synthetic) gold in `*_markup_50.json` — Gemini Flash, single commit `1c83044` (10-05-2026); the original "Human gold / hand-coded Year-1 sample" wording is retired as of 04-09-2026 (H3537 red-team row 5 — gold provenance; see Amendment below). Manuscript §2.3 restated. |
| Pass B | Blind LLM via `scripts/annotate_batch.py` reading `sources/{translator}_notes.json` (labels stripped — only `raw_text` + address). Model: **DeepSeek Chat** (`deepseek-chat`) via OpenAI-compatible endpoint `https://api.deepseek.com` (no Anthropic key on host; H1469 watch-out #2). |
| Blindness | Build-step: source files never contain gold labels; Pass B writes to `data/{translator}_full.json` joined only at scoring. |
| Bootstrap | Cohen's κ, 2 000 resamples, seed **20260724** |
| Gate (roadmap target) | κ ≥ 0.70 **or** raw agreement ≥ 85 % is the *target*; per D2/H453 a lower number **closes the gate as an honest finding**, not a blocker. |
| Granularity | L0 full labels; L1 axis_2 collapse {A} / {B} / {V,G} not pre-registered for gate (exploratory only if L0 fails). |
| Flip-rate | Optional under H1469 acceptance (not blocking); if run: 30-row subsample, seed 20260724, N=3. |
| Disagreement rule | Every disagree row categorized **protocol-ambiguity** vs **coder-error** against `classify_note.md`. |

## Backend substitution note

H453 used Opus 4.8 as Pass B. This host has `DEEPSEEK_API_KEY` only.
DeepSeek is a **different model family** from the original Haiku pipeline named in
the manuscript — that is a feature for independence (protocol §2.2), not a
defect. Quality implications are reported with the number, not hidden.

_Dr. Mārcis Gasūns_
_Executor this run: Grok 4.5 (session), model Pass B = deepseek-chat_

## Amendment 04-09-2026 — gold provenance corrected (H3537 red-team, review-sheet row 5)

The "Pass A — Human gold / hand-coded Year-1 sample" claim is **retired**. All six
`data/{translator}_markup_50.json` gold files were created wholesale in one commit
(`1c83044`, 10-05-2026, message «Gemini Flash»), with no sampling script, no
human-coding artifact and no adjudication commit anywhere in the repo; part of the
gold note texts are synthetic (paraphrases, not verbatim corpus records — 0/5 exact
corpus matches per translator spot-check). Pass A is therefore **model-generated
(synthetic) gold**. κ = 0.648/0.521 measures Gemini Flash × DeepSeek Chat
LLM×LLM consistency over partly synthetic inputs, not human inter-annotator
agreement. A genuine human coding pass over 300 verbatim corpus notes
(re-sampled by a committed script) with κ recomputation is required before these
numbers are read as human reliability. The instrument table below has been
restated accordingly; manuscript §2.1/§2.3/§7.5 carry the same correction.

_Dr. Mārcis Gasūns_

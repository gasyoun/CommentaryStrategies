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
| Pass A | Human gold in `*_markup_50.json` (hand-coded Year-1 sample; manuscript §2.3) |
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

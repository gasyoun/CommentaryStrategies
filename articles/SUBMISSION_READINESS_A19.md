---
paper_id: A19
title: "Концептуальная непереводимость как переводческая стратегия: санскритские ключевые термины в русских академических переводах"
venue: Вопросы языкознания (ВЯ)
byline: "М. Ю. Гасунс (sole author)"
orcid: 0000-0003-4513-884X
manuscript: article1_vya.md
readiness: 4/5
date: 2026-06-26
lang: ru
---

# A19 — Submission-readiness report (Вопросы языкознания)

Manuscript reviewed in full (484 lines): [article1_vya.md](article1_vya.md).
Handoff: [../../Uprava/handoffs/H005-Fable_CommentaryStrategies_untranslatability_26.06.26.md](../../Uprava/handoffs/H005-Fable_CommentaryStrategies_untranslatability_26.06.26.md).
This report is **additive** — no body text was rewritten. All edits below are proposals
for the author to apply.

Measured facts (this pass, not from the handoff):
- File: **64 528 characters** total incl. markup/apparatus; **112 017 bytes**; **no BOM** (clean UTF-8). 484 lines.
- Author's own running-text count in the header (line 30): **~52 000 зн.** — inside the ВЯ band of **45 000–80 000 зн.** Comfortable.
- RU abstract (Аннотация, lines 38–40): **1 979 зн. с пробелами / 1 760 без**.
- EN Summary (lines 46–48): **1 780 зн. с пробелами / 1 540 без**.
- RU keywords (line 42): **10 keywords**, 200 characters.

---

## What is done

- **Full body written.** §§1–5 and §7 are complete prose; §6 is complete prose plus four labelled, explicitly-flagged hypotheses H1–H4 (by design — verification deferred to Article 2/ВФ). Structure: Аннотация, Summary, §1–§7, Примечания, Список литературы.
- **Bilingual front matter.** RU Аннотация (lines 38–40) + EN Summary (lines 46–48), both with keyword lists. YAML frontmatter carries title, author, target venue, RU + EN keywords.
- **Empirical base stated and internally consistent** (re-checked 21-07-2026 after the H1377 corpus-composition repair; the earlier revision of this report wrongly certified "17 863 notes / 6 translators" as consistent). Corpus = 17 863 notes: five attributed sub-corpora summing to 17 622 (Кальянов 7 424 · Васильков–Невелева 5 574 · Эрман 758 · Гринцер 2 245 · Сыркин 1 621; Таблица in §2.1) plus 241 records not yet attributed to any of the five; Леонов (≈ 1 040) is a separate ongoing source, drawn on alongside but excluded from the 17 863. Quantitative claims rest on a 300-note hand-coded sample (50 per translator × six translators, Леонов included); lexicon = 25 terms (§2.2). The 50×6 = 300 arithmetic is consistent across §2.1, §2.3, Таблица 1 (every row sums to 50) and §7; canonical composition: [docs/CORPUS_COMPOSITION_17863.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/CORPUS_COMPOSITION_17863.md).
- **Method declared honestly.** *axis_4_paribok* (P/K/D) used as an *instrumental proxy* for the Т/К/Д strategies, not an identity (§2.3 line 109, §7.4 line 407). The LLM annotator (*claude-haiku-4-5*) and the ≥85% validation target are named (line 111).
- **Limitations section is candid (§7.5, lines 409–415):** sample size, un-verified inter-coder reliability, and the hypothetical status of §6 are all disclosed. This is what makes the 4/5→5/5 gates legitimate rather than hidden.
- **Bibliography present and split** into Источники (lines 439–467) and Литература (lines 473–483), ГОСТ 7.0.5-2008 base. Казанский 2025 carries a DOI (line 473).
- **Deliverables for this pass:** [cover_letter_A19.md](cover_letter_A19.md) (RU, ~300 words) written and staged; this report written.

---

## Proofread / house-style findings (concrete, with line refs)

### A. Table numbering — ✅ renumbered 24-07-2026 (agent follow-up)
Captioned tables now run in document order: **Таблица 1** (§3.5 levels) → **Таблица 2** (§5.1 axis_4 profile) → **Таблица 3** (§5.2 term×code). In-text «представляет» / «в Таблице N» updated. Residual (optional, not a gate): §2.1 corpus table, §2.3 P/K/D defs, and §4.4 strategy↔axis table remain un-captioned — may stay as such or get captions 4–6 if a human prefers the fuller sequence.

### B. Abstract / keyword house-style
- RU abstract (1 979 зн.) and EN Summary (1 780 зн.) are within typical journal abstract length but should be checked against ВЯ's current author guidelines, which usually cap the аннотация near **150–200 words / ~1 500 зн.** Both are slightly over a strict 200-word reading; trimming is low-risk (see Proposed edit 4).
- **Keyword count = 10** (line 42; same for EN line 50). ВЯ commonly expects **5–8 ключевых слов**. Consider trimming to ≤8 (see Proposed edit 5).
- Mixed-script keywords: the RU list mixes Cyrillic terms with italic IAST (*adhikārin*, *dharma*, *ātman*, *brahman*). Acceptable, but confirm ВЯ permits Latin-script keywords; if not, transliterate or drop them.

### C. Transliteration consistency
- The manuscript mixes **IAST** (*dharma*, *ātman*, *brahman*) with **Cyrillic practical transcription** («дхарма», «атман», «Брахман») — this is appropriate and consistent (IAST = object-language citation; Cyrillic = the rendered Russian word under discussion). No change needed, but state the convention once (Proposed edit 6) so a referee does not read it as inconsistency.
- ~~**Spelling error:** «Арааньяканда»~~ ✅ fixed 24-07-2026 → **«Араньяканда»**.

### D. Byline form — ✅ unified 2026-06-28
- Resolved: manuscript frontmatter (line 3) changed from «Гасунс М. Ю.» → **«М. Ю. Гасунс»**, now identical to the cover letter and the canonical RU form in `Uprava/AUTHOR.md` (given name + patronymic initials before surname, the ВЯ norm). All A19 artefacts now agree.

### E. Dev/status artefacts still embedded (must be stripped for submission)
- Lines 26–30: `<!-- СТАТУС … -->` HTML comment with the `[уточнить]` Петров flag.
- Lines 328–331: second `<!-- СТАТУС … -->` comment in §6.
- Lines 433–435: bibliography `<!-- ГОСТ … -->` comment.
These must not appear in the submitted copy. Produce a clean copy with all three removed, leaving **only** the Петров 1788 bracket (line 455) standing until the archival @DO check lands.

### F. Bibliography minutiae (ГОСТ 7.0.5-2008)
- Line 447 «Гринцер 2014» carries an editorial bracket `[Год и статус тома уточнить по выходным данным.]` — resolve and remove before submission (not a human gate; checkable against the volume).
- Line 453 «Леонов» has `URL: https://samskrtam.ru [дата обращения: уточнить.]` — ГОСТ requires a concrete access date; fill it.
- Line 441 «Васильков, Невелева» carries an inline note `[Кн. 10–13 выходили в 1990-е–2000-е; полный список — в корпусе …]` — acceptable as a source note, but confirm ВЯ tolerates the bracketed prose inside a reference; cleaner to move to a footnote.
- DOI line 473: confirm `10.30842/ielcp2306901529049` resolves (the prefix 10.30842 is ИЛИ РАН / Indo-European linguistics, which matches «Известия РАН. Серия литературы и языка» only loosely — verify the DOI actually points to the Казанский 2025 article, since §1 is the theoretical hinge that leans on it).

### G. Method/repo documentation drift (non-blocking, but keep consistent)
- ~~`docs/ARCHITECTURE.md` calls the axis "P/C/K" while the manuscript and data use P/K/D.~~ ✅ **RESOLVED** — `docs/ARCHITECTURE.md` uses the **P/K/D** letters (corrected 2026-06-13); no referee-visible letter mismatch via footnote [^1]. (A separate, non-blocking gloss discrepancy on the axis-4 **K/D semantics** between CLAUDE.md/GEMINI.md and ARCHITECTURE.md/ROADMAP_2026H2.md is logged in `.ai_state.md` for an author ruling; it does not touch the manuscript, which is internally consistent on P/K/D.)

---

## Remaining HUMAN GATES (@DO — these block 5/5; an agent cannot close them)

> Do not fabricate either result. Both must be supplied by a human and then stamped into the manuscript.

- **[@DO] Archival-verify Петров 1788.** Confirm attribution (is it «А. А. Петров»?), title, printer (Тип. Н. И. Новикова?), place, and year of the first Russian Bhagavadgītā (translated from Wilkins 1785) against the primary source. This releases the bracketed bibliography entry at **line 455** and the diachronic anchor prose in **§6.1 (line 337)** and **§1 (line 56)**. Until then the bracket stays. **PENDING — not done.**
- ~~**[@DO] axis_4 inter-coder reliability (≥85%).**~~ ✅ **RESOLVED 24-07-2026 (H1469)** — blind LLM second-annotator IAA (ruling D2) over the full 300-note gold (6×50), Pass B = DeepSeek Chat (`deepseek-chat`), codebook `prompts/classify_note.md`. **Measured (not invented):** axis_2 κ = **0.648** [0.571–0.719], raw agr **77.7 %**; axis_4 κ = **0.521** [0.430–0.608], raw agr **77.0 %**. Roadmap target κ≥0.7 / agr≥85 % **not met** — closed as an honest finding per D2/H453 (disagreements are 96–100 % protocol-ambiguity / policy-not-fact, not random coder noise). Full report: [`data/EVAL_RESULTS.md`](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/EVAL_RESULTS.md). ✅ **Measured numbers folded into manuscript §2.3 + §7.5 (24-07-2026 follow-up)** — no longer a pre-send prose debt.
- ~~**[@DO] Confirm ORCID for the byline.**~~ ✅ **RESOLVED 2026-06-28** — ORCID **0000-0003-4513-884X** (canonical source `Uprava/AUTHOR.md`) pasted into the manuscript frontmatter (`article1_vya.md`) and the cover letter (`cover_letter_A19.md`, line 43). No longer a gate; was mechanical, not a non-fabricable human action.

---

## Proposed manuscript edits (exact — for the author to apply; do NOT auto-apply)

1. ✅ **APPLIED 24-07-2026 (minimal sequence).** Captioned tables now 1→2→3 in document order; in-text refs updated. Optional fuller 1…6 captioning of unnumbered tables remains open.

2. **Caption the §4.4 strategy table (line 215).** Add a caption line immediately above it, e.g. `**Таблица N.** Соответствие стратегий Т/К/Д и оси axis_4_paribok` (N per the renumbering chosen in edit 1). The handoff already assumed this table is "Таблица 4".

3. ✅ **APPLIED 24-07-2026.** «Арааньяканда» → «Араньяканда».

4. **Trim the abstract toward ~200 words / ~1 500 зн.** The RU Аннотация (lines 38–40) runs two long paragraphs; the second (line 40) restates the diachronic programme. Consider compressing the last two sentences of line 40 into one. Mirror the cut in the EN Summary (line 48). Confirm against ВЯ's current word cap before cutting.

5. **Reduce keywords to ≤8** (lines 42 and 50). Suggested RU keep-set: концептуальная непереводимость; ложные друзья переводчика; санскрит; переводческая стратегия; параллельный корпус; читательский контракт; *adhikārin*. (Drop the per-term *dharma*/*ātman*/*brahman* trio from keywords — they recur in the title/abstract.)

6. ✅ **APPLIED 24-07-2026.** Transliteration convention sentence added to §2.2.

7. **Resolve the two non-gated bibliography brackets.** Line 447 «Гринцер 2014»: confirm year/volume status and delete the bracket. Line 453 «Леонов»: insert a concrete `дата обращения`.

8. **Strip dev artefacts in the clean submission copy** (do this in a *copy*, not the working draft, so the journal sees no comments): remove lines 26–30, 328–331, 433–435; remove the `[уточнить]/[проверить]` editorial markers; leave the Петров 1788 bracket (line 455) until the @DO archival check lands.

9. ✅ **APPLIED 2026-06-28.** Manuscript frontmatter (line 3) unified to «М. Ю. Гасунс», matching the cover letter and the canonical RU form in `Uprava/AUTHOR.md`. All three artefacts now agree.

---

## Verdict

**Current readiness: 4/5.** The manuscript is substantively complete, internally consistent on its arithmetic (300 = 50×6), bilingual, within the ВЯ length band (~52 000 зн.), and candid about its own limitations. It is staged for submission with a cover letter.

**What flips it to 5/5:** clearing the **one remaining @DO** human gate — Петров 1788 archival verification (releases the bibliography bracket + §6.1). _(ORCID resolved 2026-06-28; IAA measured + folded into §2.3/§7.5 24-07-2026 — [`data/EVAL_RESULTS.md`](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/EVAL_RESULTS.md).)_ Remaining agent-/author house-style items (abstract trim, keywords ≤8, optional table captions, strip dev comments in clean copy) do not block readiness.


---

## Verification pass — 02-07-2026 (Fable 5, `claude-fable-5`) — report & cover letter vs. manuscript

Gate question: do the readiness report and cover letter promise what the manuscript
delivers? **Verdict: yes — the report is substantively accurate and the cover letter's every
claim (17 863 notes, 300-note hand-coded sample, three strategies, reader-contract ↔
adhikārin, Kazansky lineage) is delivered by the manuscript.** Confirmed still-open, exactly
as reported: table numbering 3→1→2 (A), 10 keywords (B), «Арааньяканда» typo (C), all three
dev-comment blocks (E), the Гринцер-2014 / Леонов-URL brackets (F). Byline «М. Ю. Гасунс»
confirmed in frontmatter (D resolved). Deltas found:

1. **All line refs drifted +3** (frontmatter gained `orcid`/`affiliation`/`email` on
   2026-06-28 after this report was written): Таблица 3 now at line 172, Таблица 1 at 262,
   Таблица 2 at 287, typo at 450, Петров at 458, dev comments at 29–33 / 331–334 / 436–438.
   Recompute before applying the numbered edits.
2. **Item G under-calls the axis-4 issue.** The K/D semantics conflict *does* touch the
   manuscript: §2.2 uses «кодификатор направления деятельности» in Paribok's own sense
   (term-class, «Парибок 2011: 86») while §2.3 defines «К (K) Кодификатор» as a
   note-depth value «введенной А. В. Парибком (2011)» — two colliding senses of the same
   word, referee-visible at ВЯ. Per [docs/AXIS4_KD_DECISION.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/AXIS4_KD_DECISION.md)
   the fix is bounded rewording (§2.3 intro, §7.4, abstract's «П/К/Д по Парибку 2011» →
   provenance-honest phrasing); §2.2's usage is correct and stays. **This becomes a third
   @DO-adjacent gate**, shared with A21 and gated on the AXIS4 §5 source check.
3. **Казанский 2025 venue/DOI mismatch — upgrade from "verify" (item F) to "fix".** The
   bibliography names «Известия РАН. Серия литературы и языка. Т. 84. № 6», but the DOI
   prefix `10.30842/ielcp…` is ИЕЯКФ, and `docs/GEMINI.md` records the source as **ИЕЯКФ 29
   (2025)** (Tronsky proceedings, ИЛИ РАН). The theoretical hinge of §1 must cite its venue
   correctly; fix against the actual publication.
4. **Same defective Парибок 2011 entry as A21** («Шабдапракаша 2 / под ред. Парибка и
   Лелюхина» — externally the 2011 Шабдапракаша is Зографский сборник вып. 1, ред.
   Васильков/Пахомов, ЛЕМА; [academia.edu](https://www.academia.edu/8228180/)). Verify
   against the physical volume.
5. **Cover letter typo:** line 42 «Гасунс **Мāрцис** Юрьевич» mixes an IAST ā into a
   Cyrillic name — should be «Марцис».

**Addendum 16-08-2026 (H2872, Fable 5 `claude-fable-5`):** the bibliography entry
«Эрман 2009» is corrected from «СПб.: Наука, 2009» to **«М.: Ладомир, 2009»** — resolved
against the committed digitization header + meta imprint (see
[docs/CORPUS_TRUTH_RECONCILIATION_17863.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/CORPUS_TRUTH_RECONCILIATION_17863.md)).
The five sub-corpus figures cited above (7 424 … 1 621) are the published March-2026
composition per the canon; their source reconciliation (Кальянов confirmed exact; В–Н
5 574 includes «XII(б). Мокшадхарма»; остальные — snapshot values) is documented in the
same memo and guarded by `scripts/corpus_truth_census.py --check` in CI. The article's
own claims (17 863 = 17 622 + 241) remain canon-consistent and unchanged.

**Net readiness: stays 4/5.** Human gates after H1469 (24-07-2026): Петров 1788
(archival) and the Paribok attribution + bibliography fix (AXIS4_KD_DECISION §5).
The axis_4/axis_2 inter-coder number is no longer missing — measured κ reported in
[`data/EVAL_RESULTS.md`](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/EVAL_RESULTS.md)
(axis_2 κ=0.648, axis_4 κ=0.521; target ≥85 % raw not met; closed as honest finding).
The house-style fix list above remains agent-/author-doable in the clean submission copy.

---
paper_id: A19
title: "Концептуальная непереводимость как переводческая стратегия: санскритские ключевые термины в русских академических переводах"
venue: Вопросы языкознания (ВЯ)
byline: "М. Ю. Гасунс (sole author)"
orcid: TBC
manuscript: article1_vya.md
readiness: 4/5
date: 2026-06-26
lang: ru
---

# A19 — Submission-readiness report (Вопросы языкознания)

Manuscript reviewed in full (484 lines): [article1_vya.md](article1_vya.md).
Handoff: [../../Uprava/handoffs/A19_untranslatability.md](../../Uprava/handoffs/A19_untranslatability.md).
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
- **Empirical base stated and internally consistent.** Corpus = 17 863 notes / 6 translators (Таблица in §2.1, lines 80–87); quantitative claims rest on a 300-note hand-coded sample (50 per translator); lexicon = 25 terms (§2.2). The 50×6 = 300 arithmetic is consistent across §2.1, §2.3, Таблица 1 (lines 261–268, every row sums to 50) and §7.
- **Method declared honestly.** *axis_4_paribok* (P/K/D) used as an *instrumental proxy* for the Т/К/Д strategies, not an identity (§2.3 line 109, §7.4 line 407). The LLM annotator (*claude-haiku-4-5*) and the ≥85% validation target are named (line 111).
- **Limitations section is candid (§7.5, lines 409–415):** sample size, un-verified inter-coder reliability, and the hypothetical status of §6 are all disclosed. This is what makes the 4/5→5/5 gates legitimate rather than hidden.
- **Bibliography present and split** into Источники (lines 439–467) and Литература (lines 473–483), ГОСТ 7.0.5-2008 base. Казанский 2025 carries a DOI (line 473).
- **Deliverables for this pass:** [cover_letter_A19.md](cover_letter_A19.md) (RU, ~300 words) written and staged; this report written.

---

## Proofread / house-style findings (concrete, with line refs)

### A. Table numbering is out of sequence and incomplete (highest-priority house-style defect)
ВЯ requires tables numbered in order of first appearance, each with a caption.
Current state:
- Line 169: **«Таблица 3»** — but it is the *first* numbered table to appear in the text (in §3.5). Numbered 3 before 1 and 2.
- Line 259: **«Таблица 1»** (§5.1). Line 284: **«Таблица 2»** (§5.2). These appear *after* "Таблица 3".
- Line 103 (§2.3, P/K/D definitions) and line 215 (§4.4, strategy↔axis correlation) are **un-numbered tables with no caption**. The handoff refers to the line-215 table as "Таблица 4", but in the manuscript it has no caption at all.
- The §2.1 corpus table (lines 80–87) is also un-captioned.

Net: five tables, three of them captioned, and the captions run 3 → 1 → 2. A referee will flag this immediately.

### B. Abstract / keyword house-style
- RU abstract (1 979 зн.) and EN Summary (1 780 зн.) are within typical journal abstract length but should be checked against ВЯ's current author guidelines, which usually cap the аннотация near **150–200 words / ~1 500 зн.** Both are slightly over a strict 200-word reading; trimming is low-risk (see Proposed edit 4).
- **Keyword count = 10** (line 42; same for EN line 50). ВЯ commonly expects **5–8 ключевых слов**. Consider trimming to ≤8 (see Proposed edit 5).
- Mixed-script keywords: the RU list mixes Cyrillic terms with italic IAST (*adhikārin*, *dharma*, *ātman*, *brahman*). Acceptable, but confirm ВЯ permits Latin-script keywords; if not, transliterate or drop them.

### C. Transliteration consistency
- The manuscript mixes **IAST** (*dharma*, *ātman*, *brahman*) with **Cyrillic practical transcription** («дхарма», «атман», «Брахман») — this is appropriate and consistent (IAST = object-language citation; Cyrillic = the rendered Russian word under discussion). No change needed, but state the convention once (Proposed edit 6) so a referee does not read it as inconsistency.
- **Spelling error, line 447:** «Рамаяна. **Арааньяканда**» → should be **«Араньяканда»** (Araṇyakāṇḍa). Typo in a bibliography entry.

### D. Byline form is inconsistent across artefacts
- Manuscript frontmatter (line 3): **«Гасунс М. Ю.»**
- Handoff: **«М. Ю. Гасунс»**; task byline: **«M. Gasūns»**.
Pick one canonical Russian form for submission (recommend **«М. Ю. Гасунс»**, given name + patronymic initials before surname, the ВЯ norm) and use it identically in the manuscript, the cover letter, and the ORCID record. The cover letter as written uses «М. Ю. Гасунс».

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
- Per the handoff and `.ai_state.md`: `docs/ARCHITECTURE.md` in the repo calls the axis **"P/C/K"**, while the manuscript (§2.3, Таблица at line 103) and all data use **P/K/D**. If a referee follows the repo link in footnote [^1] (line 427), the mismatch is visible. Reconcile the repo doc to P/K/D; do not change the manuscript.

---

## Remaining HUMAN GATES (@DO — these block 5/5; an agent cannot close them)

> Do not fabricate either result. Both must be supplied by a human and then stamped into the manuscript.

- **[@DO] Archival-verify Петров 1788.** Confirm attribution (is it «А. А. Петров»?), title, printer (Тип. Н. И. Новикова?), place, and year of the first Russian Bhagavadgītā (translated from Wilkins 1785) against the primary source. This releases the bracketed bibliography entry at **line 455** and the diachronic anchor prose in **§6.1 (line 337)** and **§1 (line 56)**. Until then the bracket stays. **PENDING — not done.**
- **[@DO] axis_4 inter-coder reliability (≥85%).** Recruit a second coder, double-code the 50-note-per-translator gold sample on *axis_4_paribok*, and report inter-coder agreement reaching **≥85%**. Named as an open obligation in **§7.5 (line 413)**. If any P/K/D cell shifts, Таблицы 1–2 (lines 261–268, 286–302) and §5.3 may need an agreement footnote. **PENDING — no number exists yet; do not invent one.**
- **[@DO] Confirm ORCID for the byline** (the one used for the A25 / Письменные памятники Востока submission). Trivial but blocks the final byline line in both the manuscript and [cover_letter_A19.md](cover_letter_A19.md), which currently reads `[уточняется до подачи]`. **PENDING.**

---

## Proposed manuscript edits (exact — for the author to apply; do NOT auto-apply)

1. **Renumber tables in order of appearance.** Make line 169 **«Таблица 1»** (§3.5), line 259 **«Таблица 2»** (§5.1), line 284 **«Таблица 3»** (§5.2). Then update the in-text references: line 257 «Таблица 1 представляет…» → «Таблица 2 представляет…»; line 282 «Таблица 2 представляет…» → «Таблица 3 представляет…»; the §7 / §5 mentions of "Таблице 2" (e.g. line 411) → "Таблице 3". *Alternative* (if the author prefers): caption every table — give §2.1 corpus table, the §2.3 P/K/D table (line 103) and the §4.4 strategy table (line 215) their own numbers — then renumber the whole sequence 1…6 in document order. Either is acceptable to ВЯ; the current 3→1→2 is not.

2. **Caption the §4.4 strategy table (line 215).** Add a caption line immediately above it, e.g. `**Таблица N.** Соответствие стратегий Т/К/Д и оси axis_4_paribok` (N per the renumbering chosen in edit 1). The handoff already assumed this table is "Таблица 4".

3. **Fix the bibliography typo, line 447:** «Арааньяканда» → «Араньяканда».

4. **Trim the abstract toward ~200 words / ~1 500 зн.** The RU Аннотация (lines 38–40) runs two long paragraphs; the second (line 40) restates the diachronic programme. Consider compressing the last two sentences of line 40 into one. Mirror the cut in the EN Summary (line 48). Confirm against ВЯ's current word cap before cutting.

5. **Reduce keywords to ≤8** (lines 42 and 50). Suggested RU keep-set: концептуальная непереводимость; ложные друзья переводчика; санскрит; переводческая стратегия; параллельный корпус; читательский контракт; *adhikārin*. (Drop the per-term *dharma*/*ātman*/*brahman* trio from keywords — they recur in the title/abstract.)

6. **State the transliteration convention once.** Add a single sentence to §2.2 or a footnote: «Санскритские термины приводятся в IAST курсивом при цитировании языковой формы и в кириллической практической транскрипции при обсуждении русского эквивалента.» Pre-empts a referee reading the IAST/Cyrillic mix as inconsistency.

7. **Resolve the two non-gated bibliography brackets.** Line 447 «Гринцер 2014»: confirm year/volume status and delete the bracket. Line 453 «Леонов»: insert a concrete `дата обращения`.

8. **Strip dev artefacts in the clean submission copy** (do this in a *copy*, not the working draft, so the journal sees no comments): remove lines 26–30, 328–331, 433–435; remove the `[уточнить]/[проверить]` editorial markers; leave the Петров 1788 bracket (line 455) until the @DO archival check lands.

9. **Unify the byline** to «М. Ю. Гасунс» in the manuscript frontmatter (line 3 currently «Гасунс М. Ю.») to match the cover letter and the ВЯ surname-after-initials norm; or pick the journal's required order — but make all three artefacts agree.

---

## Verdict

**Current readiness: 4/5.** The manuscript is substantively complete, internally consistent on its arithmetic (300 = 50×6), bilingual, within the ВЯ length band (~52 000 зн.), and candid about its own limitations. It is staged for submission with a cover letter.

**What flips it to 5/5:** clearing the three **@DO** human gates — (1) Петров 1788 archival verification (releases line 455 + §6.1), (2) the ≥85% axis_4 inter-coder reliability number from a second coder (backs §5 Таблицы 1–2 and §7.5), and (3) the confirmed ORCID for the byline. The house-style and proofread items in §§A–G above are all agent-/author-doable and do not require external input; they should be applied in the clean submission copy alongside the gate resolutions. None of the agent-doable items, on its own, blocks 5/5 — but the three @DO gates each do, and two of them (Петров, IRR) are non-fabricable.

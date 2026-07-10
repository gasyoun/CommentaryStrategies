---
paper_id: A21
title: "Submission-readiness report — A21 Nīlakaṇṭha commentary traditions (RU)"
manuscript: "article3_nilakantha.md"
cover_letter: "cover_letter_A21.md"
venue: "Восток. Афро-Азиатские общества: история и современность (Oriens), ИВ РАН — ISSN 0869-1908 (resolved 10-07-2026; the earlier Scrinium/Indologica pair both failed — see Blocker 1)"
byline: "M. Gasūns (sole author)"
orcid: 0000-0003-4513-884X
readiness_now: 5/5
date: 2026-06-26
lang: en
---

# Submission-readiness report — A21

Manuscript: [`article3_nilakantha.md`](article3_nilakantha.md) (352 lines, ~5,266 words, UTF-8, no BOM — confirmed: first bytes `2d 2d 2d`).
Cover letter (this pass): [`cover_letter_A21.md`](cover_letter_A21.md).
Handoff of record: [`H006-Fable_CommentaryStrategies_nilakantha_ru_26.06.26.md`](../../Uprava/handoffs/H006-Fable_CommentaryStrategies_nilakantha_ru_26.06.26.md).

This is a Month-1 *confirmation* pass on a paper already at 5/5 (revising / ready-to-send). No body rewrite was performed; all proposed edits below are for the author to apply.

---

## What is done

- **All seven sections written** (§1–§7) plus Аннотация (RU), Summary (EN), Примечания (2 footnotes), and a full Список литературы (Источники + Литература). Confirmed by full read.
- **Both data tables present and internally complete.** Table 1 (lines 78–109) = 30 Nīlakaṇṭha loci with parallel V/N columns; Table 2 (lines 174–191) = 16 actual V/N notes. Two further comparison/typology tables in §3 (lines 155–160) and §5 (lines 231–236, 252–258).
- **Central result is stated consistently** in the abstract, §4.1, §7.1: typological convergence (Nīlakaṇṭha ≈43% P / 37% K / 17% D; V/N ≈63% P / 37% K / 0% D) with zero locus overlap ("selection divergence" / functional inversion).
- **Cover letter drafted** (English, ~330 words): title + one-paragraph contribution, fit-to-*Scrinium* rationale, originality / not-under-review statement, sole-author + ORCID line (0000-0003-4513-884X), contact.
- **No BOM**, encoding clean; Devanāgarī pratīkas in Table 1 render as expected in UTF-8.

---

## Proofread / house-style findings

Concrete, with manuscript line refs. Items P1–P2 are real defects; P3–P6 are house-style / consistency calls.

- **P1 — Orphaned footnote `[^1]` (definition at line 324, no anchor in body).** The footnote defining the project series and the "17 863 аннотированных примечания" figure is *defined* but its marker `[^1]` appears nowhere in the running text — only `[^2]` is anchored (line 70). A defined-but-unreferenced footnote will either be dropped silently or flagged by a copy-editor. Either anchor `[^1]` (natural home: §1, after the first mention of the *CommentaryStrategies* series at line 60, or in the abstract) or fold the content into the body / delete it.

- **P2 — `Минковски 2002` in-text characterization vs. bibliography title (line 316 vs. line 344).** §7.4 cites "ср. Минковски 2002 о Нилакантхе **как комментаторе разных традиций**." The bibliography entry (line 344) is Minkowski's JAOS article on the **Mantrakāśīkhaṇḍa**. Author/year resolve correctly (this was the subject of the last commit, `e0b6985`), but the parenthetical characterizes Minkowski's argument about Nīlakaṇṭha's cross-tradition profile, which is not the stated subject of the cited *Mantrakāśīkhaṇḍa* piece. Either (a) soften the parenthetical to match the actual article, or (b) add the more directly relevant Minkowski item if the author intends the "commentator across traditions" claim (see Optional references, below).

- **P3 — Byline form for an English/Latin venue (frontmatter line 3 + line 2 author field).** The frontmatter byline is Cyrillic **"Гасунс М. Ю."**. For *Scrinium* (Brill, English correspondence and Latin-script apparatus) the running byline should be the Latin **"M. Gasūns"** (matching keywords-en, the Summary, and the bibliography apparatus). This is partly a human gate (see below) but the manuscript-side change is mechanical once the form is confirmed.

- **P4 — Transliteration convention is applied uniformly and correctly** (verified, no defect): Cyrillic transcription in running RU prose (Нилакантха, Бхарата-бхавадипа, Налопакхьяна), IAST in the Latin apparatus (keywords-en lines 18–25; Summary lines 42–46; Список литературы Latin titles lines 338, 344), Devanāgarī pratīkas in Table 1. No mixed-script-within-a-token cases found. One worth a glance: the V/N transliterations inside Table 2 use IAST in an otherwise-Cyrillic table (e.g. `śucismitā` line 176, `satya-vāda` line 177, `tridaśālayāḥ` line 188) — this is internally consistent (technical Sanskrit terms in IAST) but confirm it is the intended house style for the venue.

- **P5 — Bibliography ↔ in-text citation match is complete** (verified): every in-text citation resolves to a Список литературы entry — Кальянов 1950–1996 (line 334), Васильков/Невелева 1987–2005 (line 336), Нилакантха 1929–1936 (line 338), Гасунс 2026 [= Article 1] (line 340; cross-referenced at lines 62, 266, 304), Минковски 2002 (line 344; cited line 316), Парибок 2011 (line 346; cited lines 60, 147). No dangling citations, no unused entries except the Minkowski characterization caveat in P2. Footnote [^2] (line 326) correctly names Kinjawadekar 1929–1936 and Krishnacharya 1906–1914; only Kinjawadekar appears as a Список литературы entry — Krishnacharya (Kumbakonam ed.) is mentioned in-note only, which is acceptable for a "consulted for variants" mention but could be promoted if the venue wants every named edition listed.

- **P6 — Tables render and are well-formed** (verified): Table 1 has 8 columns × 30 data rows, header/separator/rows column counts match; Table 2 has 5 columns × 16 data rows, likewise. The §4.1 percentages (line 195) match the §7.1 restatement (line 286): 43/37/17 and 63/37/0. Note the Table 1 caption claim "ни один из 30 локусов … не получает прямого параллельного примечания" is nuanced by two rows (#26 line 105, #29 line 108) that record a *near*-parallel V/N note in the same range on a *different* term — this is correctly worded ("нет прим." / "иная шлока"), but a referee may ask the author to surface that nuance in the §4.2 prose so it is not read as a contradiction of the absolute caption.

---

## Remaining HUMAN GATES

Bracketed `[@DO]` items that block 5/5 → submitted and that an agent cannot do:

- ~~**[@DO] Confirm ORCID for the sole byline (M. Gasūns).**~~ ✅ **RESOLVED 2026-06-28** — ORCID **0000-0003-4513-884X** (canonical source `Uprava/AUTHOR.md`) pasted into the cover letter (ORCID line + frontmatter); correspondence email unified to `gasyoun@ya.ru` (was `ai.chatgpt.ocr@gmail.com`). No longer a gate.
- ~~**[@DO] Confirm the final byline form** — Cyrillic "Гасунс М. Ю." vs. Latin "M. Gasūns"~~ ✅ **RESOLVED 10-07-2026 by the venue ruling.** «Восток» is a Russian-language journal → the **Cyrillic** form is primary. Frontmatter now reads `author: "М. Ю. Гасунс"` with `author-latin: "M. Gasūns"` preserved for the EN track (A22). P3 is therefore closed, not open.
- **[@DO] Scholarly call on the three optional references** (lines 348–352): keep, promote, or drop (see Proposed edits → Optional references). This is an editorial-judgment call reserved for the author.
- **[@DO] Final author sign-off + submission** to *Scrinium* (or *Indologica Taurinensia*): manuscript format, cover note, venue-specific style sheet, and (if Brill) the article-type / open-access selections.

---

## Proposed manuscript edits (for the author to apply — NOT applied here)

1. ✅ **APPLIED 2026-06-26 (fixes P1).** `[^1]` anchored at the first mention of the *CommentaryStrategies* corpus (line 60, after `…русских переводческих примечаний.`); the footnote is no longer orphaned. _Original guidance:_ add the marker at the first mention of the series. Suggested: at the end of line 60 (`…для корпусной аннотации русских переводческих примечаний.`) append `[^1]`, so the footnote attaches to the first reference to the *CommentaryStrategies* corpus. Alternatively attach it to the title of §1 or to the abstract's first sentence. No text of the footnote itself needs to change.

2. ✅ **APPLIED 2026-06-26 (fixes P2), option (a).** Line 316 parenthetical reworded to `(… ср. Минковски 2002 о ведийских и тантрических интересах Нилакантхи)`, matching the *Mantrakāśīkhaṇḍa* article actually cited. _Original options:_
   - (a) reword line 316's parenthetical to `(ср. Минковски 2002 о ведийских и тантрических интересах Нилакантхи)` so it matches the *Mantrakāśīkhaṇḍa* article actually cited; or
   - (b) keep the "комментатор разных традиций" claim and add the directly supporting item (Minkowski's "Nīlakaṇṭha's *Bhāratabhāvadīpa*" / "what makes a work classical" line of argument) to Литература, citing it at line 316.

3. **Byline (fixes P3), once the human gate resolves.** If the venue is *Scrinium*: change frontmatter line 3 `author: "Гасунс М. Ю."` → `author: "M. Gasūns"` and add an `author-ru: "Гасунс М. Ю."` field so the Cyrillic form is preserved for the *Indologica Taurinensia* fallback. Do **not** change the running RU prose, which correctly keeps Cyrillic transcription.

4. **Optional references decision (lines 348–352 comment) — RECOMMENDATION, not a silent edit.** The trailing HTML comment lists three candidates. My recommendation:
   - **Vassilkov 1995–1996** (*The Mahābhārata's Typological Definition Reconsidered*, **Indologica Taurinensia**) — **promote to Литература.** Strongly relevant (it is a Vassilkov methodological piece and is in the very alternate venue named on the title page); citing it strengthens the §1 framing of the V/N apparatus and signals fit to *Indologica Taurinensia*.
   - **Pollock 2006** (*The Language of the Gods in the World of Men*) — **optional/promote if space.** Directly supports the *adhikārin* / implied-reader argument of §6; a natural single citation at §6 if the author wants a canonical anchor.
   - **Bronkhorst 1996** (*Sanskrit and Reality*, in *Ideology and Status of Sanskrit*, Brill) — **lowest priority.** Tangential to the commentary-typology argument; promote only if the author engages the "what counts as a difficulty" framing explicitly. (Brill provenance is a minor plus for a *Scrinium* submission.)
   - In all cases: **delete the HTML comment block (lines 348–352) before submission** regardless of the keep/drop decision, so no editorial scaffolding ships in the manuscript.

5. **(Minor, P6) Surface the two near-parallel rows in §4.2 prose.** Optionally add one sentence in §4.2 noting that rows #26 and #29 (Table 1) carry a V/N note *in the same adhyāya range but on a different term*, so the "zero overlap" claim is read as "zero same-term overlap" rather than "zero notes in range." Not required, but pre-empts a likely referee question.

---

## Verdict

**Current readiness: 5/5 (revising, ready-to-send).** The paper is substantively complete, internally consistent, well-cited, and the data tables are well-formed. The agent-side confirmation pass found only one true defect (P1, orphaned footnote `[^1]`) and one wording reconciliation (P2, Minkowski characterization) — **both now applied 2026-06-26** (footnote anchored at line 60; Minkowski parenthetical reworded to match the cited *Mantrakāśīkhaṇḍa* article). The manuscript is now **fully ready bar sign-off**.

**What flips 5/5 → submitted:** the three remaining `[@DO]` human gates — (1) confirm the Latin byline form for *Scrinium*, (2) the optional-references scholarly call, (3) author sign-off and the venue upload. _(The former ORCID gate was resolved 2026-06-28: 0000-0003-4513-884X pasted into the cover letter.)_ None require further authoring. Recommend applying proposed edits 1–4 in the same pass as the byline confirmation, then submit.


---

## Hostile pre-send check — 02-07-2026 (Fable 5, `claude-fable-5`) — VERDICT: **HOLD**

Full adversarial read of the manuscript + external verification of venues and the
load-bearing citation. The argument itself is sound and the Russian scholarly register is
publication-grade; the internal arithmetic was re-verified against Tables 1–2 (13/11/5/1 →
43/37/17%; 10/6 → 63/37%; totals consistent in abstract, §4.1, §7.1). The P1/P2 edits from
this report are confirmed applied, and two report items are now stale: the Latin byline
(`author: "M. Gasūns"` + `author-ru`) and the three optional references (all promoted into
Литература AND cited in-text at §1, §6, §7.2) are already in the manuscript. What blocks
sending is none of that:

**Blocker 1 — RESOLVED 10-07-2026 (M.G. ruling).** The two named venues both failed: *Indologica
Taurinensia* ceased publication (last and final issue n. 45, 2019,
[asiainstitutetorino.it](https://www.asiainstitutetorino.it/indologica.html)); *Scrinium* (Brill)
is a journal of patrology / critical hagiography / ecclesiastical history —
ancient/medieval **Christian** Church ([brill.com](https://brill.com/view/journals/scri/scri-overview.xml)) —
categorically out of scope for a Sanskrit ṭīkā paper. **New venue chosen: «Восток.
Афро-Азиатские общества: история и современность» (Oriens), ИВ РАН, ISSN 0869-1908** —
a live, peer-reviewed Russian-language orientalist journal under the RAS Division of History
and Philology, six issues/year ([vostokoriens.ru](https://vostokoriens.ru/),
[new.ras.ru](https://new.ras.ru/work/publishing/journals/vostok-afro-aziatskie-obshchestva-istoriya-i-sovremennost/)).
The Russian manuscript needs no translation; the frontmatter `target` and the cover letter have been
switched to «Восток» (cover letter re-authored in Russian). The EN translation (A22,
`article3_nilakantha_en.md`) stays a separate 4/5 track for an English venue. Remaining gates:
Blockers 2 and 3 below.

**Blocker 2 — Paribok attribution (axis-4 K/D ruling).** §3 presents the operational
K/D glosses («кодификатор/системное позиционирование», «дискурсивное») as «Таксономия
Парибка (2011)», and §1/§4.1/§7.2 + both abstracts build the central universality claim on
that identity. Per [docs/AXIS4_KD_DECISION.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/AXIS4_KD_DECISION.md)
the scale is the project's own, derived from Paribok but classifying *notes*, not *terms*.
Likely referees are Russian indologists of Paribok's circle (Vasilkov — a subject of the
paper — co-edited the very Шабдапракаша volume). Required rewording is bounded (§3 intro +
definitions provenance, §1/§7.2 claim softening to «трехчастное различение, восходящее к
Парибку»; the I–IV↔P/K/D mapping, tables and percentages stand unchanged). Gated on the
[@DO] source check in AXIS4_KD_DECISION §5.

**Blocker 3 — the Парибок 2011 bibliography entry is defective.** The manuscript cites
«Шабдапракаша 2 / под ред. А. В. Парибка и Д. Н. Лелюхина. СПб., 2011. С. 77–98»; external
evidence documents the 2011 Шабдапракаша as **Зографский сборник. Вып. 1 / под ред.
Я. В. Василькова и С. В. Пахомова. СПб.: ЛЕМА, 2011**
([academia.edu](https://www.academia.edu/8228180/)); a «Шабдапракаша 2» edited by
Парибок/Лелюхин is not externally attested. Editors, issue, pages and the article title must
be verified against the physical volume (same [@DO] as Blocker 2). Note this entry was never
in the verified-bibliography list (.ai_state covers Кальянов/В-Н/Нилакантха/Минковски only);
P5 above verified citation *resolution*, not entry *content*.

**Minor (fix in the same pass):** (a) «Васильков 1995–1996» entry lacks volume and pages;
(b) Table 1 caption says «Рамопакхьяна, адхьяи 273–276» but its Rāma rows start at 274.9 —
align caption or note that adhyāya 273 yielded no Nīlakaṇṭha locus; (c) stray double blank
line after the Парибок 2011 entry.

**Consequence:** readiness 5/5 → **4/5 (revising / pre-submission)** until the three
blockers clear. Send is the wrong call today; the fix path is short and fully specified.

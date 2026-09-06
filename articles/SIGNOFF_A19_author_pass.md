# SIGNOFF A19 — author-voice pass

_Created: 06-09-2026 · Last updated: 06-09-2026_

## Scope

Manuscript: [articles/article1_vya.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/articles/article1_vya.md) — «Концептуальная непереводимость как переводческая стратегия: санскритские ключевые термины в русских академических переводах» (RU, target «Вопросы языкознания», status 4/5 submission-staged). Handoff: [H3857](https://github.com/gasyoun/Uprava/blob/main/handoffs/H3857-Fable_Uprava_all-articles-author-voice-pass-workflow_01.09.26.md). Pass by Fable 5.1 (`claude-fable-5-1`), 06-09-2026, branch `voice-pass/A19`.

Voice, register and framing only; no number, claim or citation altered; mechanical drift gate CLEAN (`voice_drift_check.py --git origin/main`: numbers 464/464, urls 2/2, dois 1/1, citations 5/5, IAST 108/108, headings 42/42, table rows 50/50). Byline kept as the paper already carries it in the front matter (`М. Ю. Гасунс`, ORCID, «независимый исследователь», gasyoun@ya.ru) — equivalent to the standing RU form. Authorial «мы» kept throughout: «Вопросы языкознания» house norm; only the one meta-sentence in §3.1 went to first person singular (see row 10) — revert it if the venue's style sheet objects.

## 1. Voice calls made — each may be vetoed

| # | Location | Call | Rationale |
|---|---|---|---|
| 1 | Header | `Last updated` 05-09-2026 → 06-09-2026 | pass stamp |
| 2 | §1 ¶1 | «Это несводимость не просто переводчески произвольная…» → «Эта несводимость не просто переводчески произвольная: она систематическая и воспроизводимая.» | reverted after adversarial verify: [substance] rewrite dropped «не просто переводчески» (the claim's scope); only the agreement fix «Это» → «Эта» kept |
| 3 | §1 ¶2 | «всё» → «все» | no ё |
| 4 | §1 ¶4 | «Что делает лексическую ошибку устранимой — это то, что она возникает…» → «Лексическая ошибка устранима потому, что возникает…» | «what makes X is that» calque; direct claim |
| 5 | §1 ¶5 | «Из этого следует важное следствие для диагностики:» → «Отсюда диагностический вывод:» | «следует… следствие» tautology + «важное» intensifier |
| 6 | §2.1 ¶4 | «неё» → «нее» | no ё |
| 7 | §2.2 ¶4 | «(Ведийская…) при данном исследовании не включается в анализ» → «(ведийская…) в анализ не включен» | bureaucratic «при данном исследовании»; lower-case adjective |
| 8 | §2.3 ¶1 | «регулярно-выраженный поиск» → «поиск по регулярным выражениям» | regex calque, not Russian |
| 9 | §2.3 ¶3 | «Принципиально: обе стороны согласия — языковые модели» → unchanged | reverted after adversarial verify: [meaning] the emphasis marker flags the paper's central caveat; original restored verbatim |
| 10 | §3.1 ¶1 | «важно уточнить природу самого феномена» → «уточним природу самого феномена» | empty opener dropped; corrected after adversarial verify: [voice] «уточню» was the only first-person singular in a «мы» paper → «уточним» |
| 11 | §4.6 last ¶ | «Что остается системным — это *направление смещения*» → «Системным остается *направление смещения*» | cleft-copula abuse |
| 12 | §5.1 profile Т | «Относительное прочтение: доля K…» → «В относительном выражении доля K…» | telegram label |
| 13 | §6.1 ¶1 | «примечания, обсуждающих выбор эквивалента, нет» → «примечаний, обсуждающих…» | genitive of negation |
| 14 | §6.1 ¶2 | «Важно понять, что это не неудача:» → «Это не неудача:» | empty opener |
| 15 | §6.4 ¶1 | «Существенно, что 2009 год дает два перевода…, вышедших практически одновременно, — Эрмана и Бурбы, — с…» → «В 2009 году практически одновременно выходят два перевода Бхагавадгиты — Эрмана и Бурбы — с…» | empty opener; dash clutter |
| 16 | §6.4 ¶1 | «в абсолютном выводе у него» → «в абсолютных числах у него» | «в абсолютном выводе» is not a phrase; §7.1 says «в абсолютном счете» — now consistent in sense |
| 17 | §7.1 ¶1 | «объединяемых традиционно под именем» → «традиционно объединяемых под именем» | word order |
| 18 | §7.1 ¶2 | «счёте» → «счете» | no ё |
| 19 | §7.3 ¶1 | «Одним из значимых результатов данного исследования является то, что описанная закономерность имеет имя в самой индийской традиции — задолго до…» → unchanged | reverted after adversarial verify: [meaning] the frame is the paper's contribution claim, not decoration; original restored verbatim |
| 20 | §7.5 ¶1 | «Необходимо указать на три методологических ограничения.» → «У исследования три методологических ограничения.» | empty opener |
| 21 | §7.5 ¶2 | «пересчёт» → «пересчет» | no ё |

Not changed on purpose: the recurring «не X, а Y» figure (≈9 instances: §1 «не четыре ошибки; … четыре ответа», §4.3 «не непоследовательность, а осознанная контекстуализация», §5.2 «не означает некомпетентности; … другой читательский контракт», etc.). In this paper it is the thesis (error vs. competence), not decoration; thinning it would touch argument, not voice. A human may still prune one or two.

## 2. Substance flags carried (not fixed)

1. §6.5 ¶2: «полемизировал с теософским пониманием *karmы*» — hybrid token (IAST stem + Cyrillic ending). Sanskrit token, left as is; should read *karma* or «кармы».
2. §7.3 ¶2: «обладает правом (лат. *adhikāra*)» — *adhikāra* is Sanskrit, not Latin; «лат.» is wrong.
3. §2.2 lexicon vs. «25 терминов»: the list at §2.2 has 24 entries unless *brahman* / *Brahmā* or *deva* / *asura* counts as two; *ākāśa* is in the lexicon but absent from Table 1 (§3.5); *āśrama* appears twice in Table 1 (meanings 1 and 2). The count 25 is stated in the abstract, Summary, §1, §2.2, §3.1, §7.4.
4. §5.3 ¶1: «Данные таблиц 1–2 позволяют…» — Table 1 is the incommensurability scale; the profile data are Tables 2–3. Figure reference, not changed.
5. §6.5 ¶2: «народной «кармой» Instagram» applied to Erman 2009 — Instagram launched in 2010; anachronism.
6. §6.1 vs. references: «Н. И. Петровым» in the text, «[А. А. Петрова]» in the reference entry «Петров 1788»; the entry itself is marked «требует верификации».
7. Footnote `[^1]` (project / samskrtam.ru / ИЛИ РАН acknowledgement) is defined under «Примечания» but never referenced in the body.
8. Summary (EN): «15,847 annotated notes» — only the 300-note sample is annotated (model labels); the RU abstract says «примечаний коммитнутого корпуса» without «annotated».
9. §2.3 and §7.5 lean on «синтетическое золото» (Gemini Flash first-pass labels, partly paraphrased note texts). The paper says so honestly and repeatedly; a reviewer for ВЯ may still ask why Tables 2–3 are presented before human annotation exists. Not a voice matter.
10. Front matter and two HTML status comments (`<!-- СТАТУС … -->`, §6 status, references note) remain in the `.md`; they are working metadata, not paper text, and were left untouched. Strip before submission pack.
11. References: «Гринцер 2014» carries «[Год и статус тома уточнить]»; «Леонов» carries «[дата обращения: уточнить]». Both pre-existing, unchanged.

## 3. Read-and-sign

Reading time for the human: about 30 minutes (the 21 rows above plus the 11 flags; the manuscript itself is ~9,200 words). Proposed readiness after this pass: stays 4/5 until flags 1–5 are ruled on (1, 2, 4 are one-word fixes; 3 needs a decision on how the 25 are counted). No venue change recommended: «Вопросы языкознания» remains the right home; the authorial «мы» was kept for that reason. No submission until 2026-11-01 (freeze).

_Dr. Mārcis Gasūns_

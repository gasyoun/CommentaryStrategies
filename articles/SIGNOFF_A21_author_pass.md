# SIGNOFF A21 — author-voice pass

_Created: 06-09-2026 · Last updated: 06-09-2026_

## Scope

Manuscript: [articles/article3_nilakantha.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/articles/article3_nilakantha.md) — «Индигенная и академическая комментаторские традиции: Бхарата-бхавадипа Нилакантхи и русские переводчики Махабхараты» (RU, target «Восток / Oriens», ИВ РАН; status 4/5 revising, pre-submission). Handoff: [H3857](https://github.com/gasyoun/Uprava/blob/main/handoffs/H3857-Fable_Uprava_all-articles-author-voice-pass-workflow_01.09.26.md). Pass 1, 06-09-2026, Fable 5.1 (`claude-fable-5-1`).

Voice, register and framing only; no number, claim or citation altered; mechanical drift gate CLEAN (`voice_drift_check.py --git origin/main`: numbers 374/374, urls 7/7, dois 0/0, citations 0/0, IAST 53/53, Devanagari 117/117, headings 26/26, table rows 69/69). Byline: the front matter carried `М. Ю. Гасунс` + ORCID only; `affiliation: "независимый исследователь"` and `email: "gasyoun@ya.ru"` were added there, so the block is now equivalent to the standing RU form. Authorial «мы» kept throughout: «Восток» house norm, same call as A19; the one place where the paper itself was the grammatical subject of an opinion («Настоящая статья считает») went to «Мы считаем». The English Summary was not touched.

## 1. Voice calls made — each may be vetoed

| # | Location | Call | Rationale |
|---|---|---|---|
| 1 | Header | `Last updated` 05-09-2026 → 06-09-2026 | pass stamp |
| 2 | Front matter | added `affiliation` and `email` lines under `orcid` | byline block per the standing RU form; YAML `author` left as the paper had it |
| 3 | Status comment (the hidden «СТАТУС» block after the front matter) | added one line: «Author-voice pass 06-09-2026 (SIGNOFF_A21_author_pass.md)» | required header note; the comment is the paragraph that lists prior passes |
| 4 | Аннотация, last sentence | «Делается вывод о том, что зона отбора является диагностикой…» → «Из этого следует, что зона отбора служит диагностикой…» | bureaucratic passive; same conclusion, same strength — **reverted after adversarial verify:** substance+meaning hit (conclusion reframed as entailment) |
| 5 | §1 ¶6 | «Настоящая статья предоставляет эмпирическую проверку этого тезиса: если…» → «Настоящая статья проверяет этот тезис эмпирически: если…» | «предоставляет проверку» is a calque; direct verb |
| 6 | §3 last ¶ | «Важное уточнение: тип IV (нарративная мотивация) не имеет…» → «Тип IV (нарративная мотивация), однако, не имеет…» | empty label-opener — **reverted after adversarial verify:** meaning+voice hit (the flag «важное уточнение» is load-bearing, «однако» adds a contrast the original does not make) |
| 7 | §4.2 ¶1 | «Вместе с тем нулевое пересечение … требует объяснения. Оно не случайно: каждый аппарат…» → «Нулевое пересечение …, однако, требует объяснения: каждый аппарат…» | «не случайно» occurred five times in the paper (§4.1, §4.2 ×2, §5.2, §7.4); this one carried nothing the colon does not — **reverted after adversarial verify:** voice hit (author's two-sentence cadence restored) |
| 8 | §5 ¶1 | «всё же» → «все же» | no ё (the only ё in the file) |
| 9 | §5.1 ¶1–2 | two paragraphs «Оба аппарата работают… Оба аппарата имеют доступ… Тем не менее… / Причина: каждый аппарат…» → one paragraph «Оба аппарата работают с одним и тем же текстом, с одними и теми же санскритскими словами, именами и реалиями — и тем не менее их зоны комментирования не пересекаются, потому что каждый комментирует то, что трудно для *его* читателя. Отсюда зеркальная структура непрозрачности:» | anaphoric «Оба аппарата… Оба аппарата…» run + telegram «Причина:»; the mirror-table still follows |
| 10 | §5.1 last ¶ | «Инверсия отбора не является несовпадением: это *комплементарность*. Взятые вместе,» → «Инверсия отбора — это *комплементарность*, а не несовпадение: взятые вместе,» | «not X: it is Y» punchline; the italic term stays |
| 11 | §5.2 last ¶ | «Это не случайное совпадение структурных форм. Оба аппарата отвечают…» → «Совпадение структурных форм здесь не случайно: оба аппарата отвечают…» | isolated «Это не …» punchline (second of the five «не случайно») |
| 12 | §6 ¶2 | «Настоящая статья предоставляет эмпирическую проверку этого сопоставления. Нилакантха является не просто примером … — он является *явным теоретиком*…» → «Изложенные выше данные позволяют проверить это сопоставление эмпирически. Нилакантха — не просто пример индигенного комментатора, но *явный теоретик*…» | the §1 sentence was repeated verbatim; double «является» |
| 13 | §7.2 ¶2 | «Настоящая статья считает вторую интерпретацию более вероятной, но подчеркивает статус этого суждения: … а не вывод, ими доказанный,» → «Мы считаем вторую интерпретацию более вероятной, но подчеркнем статус этого суждения: … а не доказанный ими вывод,» | a paper cannot hold an opinion; hedge («гипотеза, совместимая с нашими данными») kept word for word |
| 14 | §7.3 ¶2 | «предоставляет более тонкий инструмент» → «дает более тонкий инструмент» | third «предоставляет» |
| 15 | §7.4 ¶1 | «Несколько ограничений настоящего исследования требуют оговорки.» → «Ограничения исследования требуют оговорки.» | throat-clearing — **reverted after adversarial verify:** meaning hit («несколько» and «настоящего» are scope words) |

Not changed on purpose: the recurring «не X, а Y» figure where it states the thesis (§4.2 «не случайный разброс, а структурная инверсия», §5.2 «имманентную тексту, а не созданную переводом», §7.1 «не противоречат, а дополняют», §7.2 «не заимствование и не влияние», §7.4 «не случайный артефакт выборки, а принцип») — that is the argument, not decoration. «zona commentarii» (§7.1) is a Latin flourish next to the plain «зона комментирования» of §5.1; left as the author's coinage, a human may prefer one form. The authorial «мы» (§1 «мы защищаем», §4.1 «Подчеркнем», §4.2 «мы можем реконструировать», §7.2 «нашими данными», «в нашем случае», §7.4 «мы знаем») stays: switching a single-author «Восток» paper to «я» is a house-style decision a human should make, not a voice fix.

## 2. Substance flags carried (not fixed)

1. §4.2, В/Н list: «мифологические и культурные реалии (… ##3–5, 9, 11–14 в Табл. 2)» — the range 11–14 includes #13 (*tridaśālayāḥ*, coded Лексич. in Table 2), which is also listed under «грамматические и лексические явления (#8, 10, 13, 15, 16)». Should read «11–12, 14». Index reference, not changed.
2. §4.2 «редко — грамматические и лексические явления (#8, 10, 13, 15, 16)»: that is 5 of 16 (6 with #7, also Лексич.) against 7 mythological — «редко» is arguable at this sample size. Wording of a comparison, not changed.
3. §7.4 closing sentence «структурная гомология при функциональной инверсии — не случайный артефакт выборки, а принцип, определяемый природой самой герменевтической задачи» reads stronger than §7.2 («гипотеза, совместимая с нашими данными, а не доказанный ими вывод») and §4.1 («согласуется с гипотезой…, но само по себе ее не доказывает»). Hedging strength is a human call; a reviewer will notice the gap.
4. Citation keys for one edition come in three forms: «Nīlakaṇṭha 1929–1936» (§2.1 text), «Нилакантха 1929–1936» (reference entry), «Kinjawadekar 1929–1936» (footnote 2). Unify to the entry's key.
5. §2.1 «в составе стандартного издания Бхарата-бхавадипа» vs footnote 2 «Стандартное критическое издание Бхарата-бхавадипа не существует» — «стандартное» vs «стандартное критическое»; reconcile so a reviewer does not read it as a contradiction.
6. §6 ¶2: «в своих комментариях к Бхагавадгите и другим философским текстам он различает типы квалифицированных читателей» — no locus in Nīlakaṇṭha is cited; Pollock 2006 is general and Minkowski 2002 is about the Mantrakāśīkhaṇḍa. A reviewer will ask where Nīlakaṇṭha says this.
7. «Парибок 2011» bibliography entry: the book-check gate from the status comment (AXIS4_KD_DECISION §5 — volume not externally confirmed, do not «fix» from web sources) remains open; the entry was not touched.
8. «Гасунс 2026 [= Article 1]» series markers in §1, §3, §6, §7.3 and the reference entry «[= Article 1]», plus «[В печати.]» — internal cross-project tags to strip at camera-ready.
9. Keywords (RU and EN) list «Кальянов / Kalyanov», but Kalyanov appears only in §1 (background) and §7.4 (explicitly out of the comparison). Consider dropping from keywords or keeping for series continuity.
10. Footnote 1: «Корпус проекта включает 17 863 аннотированных примечания» — the A19 sibling paper states «15 847 коммитнутых примечаний по пяти корпусам» and its signoff flags that only the 300-note sample is annotated. The two papers of the series should quote one corpus size and one meaning of «аннотированных».
11. Front matter and the hidden «СТАТУС» status comment remain in the `.md`; working metadata, not paper text. Strip before the submission pack.
12. «Дополнительные материалы»: TEI files are cited by full blob URL and the rights decision «от 12.06.2026» is referenced; fine for the repo, but the venue will want a supplementary-data statement without GitHub paths.

## 3. Read-and-sign

Reading time for the human: about 30 minutes (15 rows above, 12 flags; the manuscript is ~6,150 words with two data tables). Proposed readiness after this pass: stays 4/5 until flags 1, 4, 5 and 6 are ruled on (1, 4 and 5 are one-line edits; 6 needs a locus or a softer sentence; 3 is a hedging decision). No venue change recommended: «Восток / Oriens» resolved 10-07-2026 stands; the authorial «мы» was kept for that reason. No submission until 2026-11-01 (freeze).

_Dr. Mārcis Gasūns_

# SIGNOFF A24 — author-voice pass (Комментаторские стратегии русских переводчиков санскритского эпоса)

_Created: 06-09-2026 · Last updated: 06-09-2026_

## Scope

Manuscript: [tronsky-XXX/article_current.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/tronsky-XXX/article_current.md) (Russian, ~6 000 words, Tronsky readings submission draft). Handoff: [H3857 — all-articles author-voice pass workflow](https://github.com/gasyoun/Uprava/blob/main/handoffs/H3857-Fable_Uprava_all-articles-author-voice-pass-workflow_01.09.26.md). Pass by Fable 5.1 (`claude-fable-5-1`), 06-09-2026. Voice, register and framing only; no number, claim or citation altered; mechanical drift gate ([voice_drift_check.py](https://github.com/gasyoun/Uprava/blob/main/tools/voice_drift_check.py) against `origin/main`) CLEAN — 276 numbers, 3 URLs, 100 IAST tokens, 14 headings, 23 table rows identical before and after. No letter yo (the seventh Cyrillic letter) in the text, checked before and after. No prior signoff existed; this is pass 1.

The manuscript already uses first-person plural («мы видели», «нас интересует») and the impersonal register standard for ИЛИ РАН proceedings; the pass did not force first-person singular. A contribution statement exists («Задача настоящей статьи — предложить параметры…»), the §1 question (which strategies, along which axes) is the question the Заключение answers, and title, аннотация and body agree. The pass therefore stayed light: openers, straight quotes, one typo, one paragraph split, the byline block.

## 1. Voice calls made — each may be vetoed

| # | Location | Call | Rationale |
|---|---|---|---|
| 1 | Header line | `Last updated` 05-09-2026 → 06-09-2026 | brief: bump on every pass |
| 2 | Сведения об авторе | added «(Mārcis Gasūns)» after the name and «ORCID [0000-0003-4513-884X](https://orcid.org/0000-0003-4513-884X)» after the affiliation; degree, affiliation and e-mail kept as they were | brief: author identity block (RU form) is added when absent; ORCID was absent. YAML `author: М. Ю. Гасунс` left untouched |
| 3 | Summary (EN), sentence 1 | «specifically focusing on» → «focusing on» | filler adverb |
| 4 | Summary (EN), last sentence | «serves as a vital environment for the coexistence of these diverse interpretive traditions» → «is the environment in which these interpretive traditions coexist» | «vital», «diverse» are decorative intensifiers; the claim (corpus = the shared environment) is unchanged |
| 5 | §1, para 4 | «Настоящая статья рассматривает переводческий комментарий…» → «Переводческий комментарий рассматривается здесь…» | third «настоящая статья» opener inside one section; the other two stay |
| 6 | §1, para 4 (end) | straight quotes → «Махабхаратой» / «Рамаяной» | typography consistency (the text uses guillemets everywhere else) |
| 7 | §1, para 7 | «"Литературных памятников"» → «Литературных памятников» in guillemets | same |
| 8 | §2, third parameter | «Дело в том, что «дискуссионный» слишком широко: под него подпадают…» → ««Дискуссионный» — характеристика слишком широкая: под нее подпадают…» | «Дело в том, что» is an empty opener |
| 9 | §2, third parameter | «Грубо говоря, *padārthokti* отвечает…» → «В самом общем виде *padārthokti* отвечает…» | colloquial hedge-opener; the simplification itself is kept |
| 10 | §3, para 1 | «Если сказать совсем коротко: стратегия — это…» → «В самом кратком виде стратегия — это…» | conversational opener |
| 11 | §3, para 1 (end) | straight quotes → «Наука» / «Восточная литература» | typography |
| 12 | §3, Кальянов | «Интересно, что это не выглядит как пробел на фоне тогдашней советской индологии:» → «На фоне тогдашней советской индологии это не выглядит как пробел:» | «Интересно, что» is an empty opener; the historical explanation is untouched |
| 13 | §3, second strategy, para 1 | «При этом профили внутри группы заметно различаются, что делает ее особенно интересной для наблюдения.» → «Профили внутри группы при этом заметно различаются.» | decorative tail («особенно интересной для наблюдения») |
| 14 | §3, second strategy | the single ~330-word paragraph split into three: Васильков–Невелева · Эрман · Гринцер + Сыркин | readability; no sentence removed, order unchanged |
| 15 | §3, Эрман reliability caveat | one three-clause semicolon sentence → three sentences («…наименьшем в основной выборке. При таком объеме… на расширенном материале. Перспективным контролем было бы… : оно позволило бы отделить…») | the hedge («ориентировочные, требующие проверки») is kept verbatim; only punctuation and one connector changed |
| 16 | §3, third strategy | «Примечательно, как при таком подходе меняется сама природа сноски:» → «При таком подходе меняется сама природа сноски:» | filler intensifier |
| 17 | §3, prediction para | «квантитивно проверяемо» → «количественно проверяемо» | non-standard calque; same meaning |
| 18 | §3, Эрман quotation (Erman 2009: 338) | inner straight quotes → „Дханурведа“ | Russian nested-quote convention inside «…»; the quoted wording is unchanged — veto if the source edition itself prints straight quotes and the author wants a diplomatic transcription |
| 19 | §4, para 3 | «Здесь следует еще раз подчеркнуть статус материала, относящегося к проекту М. В. Леонова (редактор Е. А. Костина).» → «Статус материала, относящегося к проекту М. В. Леонова (редактор Е. А. Костина), требует повторной оговорки.» | «следует подчеркнуть» opener |
| 20 | §4, paras 1–2 | trailing spaces removed | hygiene |
| 21 | Заключение | «аппарататом» → «аппаратом» | typo |

Not touched on purpose: «Примечание превратилось в небольшой диалог через эпохи … заговорили об одном месте вместе» (§1 opening image — it is the thread §4 picks up with «равноправных голосов»); «академический максимум русской санскритологии» and «самый системный пробел всей академической санскритологии» (§3 — evaluative claims, the author's, not decoration); the repeated «привлекаемыми здесь исключительно как контрастный фон» for Сыркин in §3 (a repeated hedge; removing a hedge is outside the pass).

## 2. Substance flags carried (not fixed)

1. **Кальянов textology share, two figures.** §3 says «категория „текстология“ достигает 3,4 % — втрое больше, чем у В. И. Кальянова (1,2 %)», but the prediction paragraph later says «4,3 % текстологии против почти нулевого показателя у Кальянова». 1,2 % is not «почти нулевой»; one of the two wordings should go.
2. **§3 table vs Приложение III disagree on several cells.** Гринцер: body table «текстология, нарратив, филология» as dominant rubric, appendix «Лексика (56 %)» and «текстология 15 %» in the body prose. Эрман type: body table «культурологический + филологический», appendix «Филолог.». Сыркин status: body table «понятие», appendix «Концепт». Васильков–Невелева status: body «понятие (без эксплицитной разметки)», appendix «Понятие». A reader who compares the two tables will find them inconsistent; a human must decide which is the source of record.
3. **Приложение III rows with no body support.** «Плотность (комм./шлока)» (56 % / 47 % / 37,9 % / 24,6 % / ≈ 36 %), «Доля IAST» for Эрман (50 %) and Гринцер (45 %), «Целевой читатель», «Диалог с традицией» (Васильков «Слабый») and Леонов «≈ 1 040» notes / «Диалог (38 %)» appear only in the appendix; the body never derives or cites them. Either point the body at them or mark them as repository-derived.
4. **Кальянов «до 80 % … по предварительным подсчетам» vs 51,5 %.** §3 gives 51,5 % for the «термин/перевод» rubric and then «до 80 % всех примечаний» for glosses to terms, toponyms, realia and characters — different denominators, but the second figure is called preliminary while the first is «надежно» in the table. Say which count the 80 % is.
5. **Footnote 5 cites a personal communication as «подробный разбор».** «См. подробный разбор истории перевода в: (Tolchelnikov, личное сообщение, 2026)» — a personal communication is not a published разбор and has no bibliography entry; venues in this series usually reject it in a footnote of this form.
6. **Bibliography key form.** Dasgupta and Schlegel entries lack the «Author Year —» key the other twelve entries carry, and are cited in footnotes 3 and 4 by name and year only. Also «Paribok 2011: 80–86» cites the full page range of the article as if it were a locus.
7. **Аннотация (RU) vs Summary (EN).** The EN summary names the «categorical gap» (codifiers vs concepts) as «a key theoretical finding»; the RU аннотация does not mention it at all. The Заключение calls it «фундаментальной чертой жанра». Aligning the RU abstract is a substance decision, not a voice one.
8. **17 622 vs 17 863.** Already acknowledged in §1 (241 unattributed records, «выверка … зафиксирована в репозитории как отдельная задача»); flagged only so that the number is reconciled before submission or the caveat survives into print.
9. **Four vs three parameters.** §3 itself concedes the scheme is «не вполне точно» four-parametric (parameters 1–2 correlate with 3); title of the model in the Заключение and the JSON schema still say «четырехпараметрическая» / «4 осям». Consistent framing wanted.
10. **Леонов data status.** §1 says the Сундараканда draft is «не входящий в основные 17 863 примечания»; Приложение III gives it ≈ 1 040 notes and a full row of ≈ figures on «Кн. V „Рамаяны“». Fine as flagged, but the reliability column already says «предварительно» — the two places should use the same word.
11. **YAML `date: 2026-05-10`** predates the header's `Last updated`; harmless for a draft, but the export pipeline (`article_fixed.md`, `.docx`) may read it as the manuscript date.

## 3. Read-and-sign

About 30 minutes: read §1 (byline block, para 4), the three new §3 paragraphs around Эрман, and the Эрман quotation with the nested quotes; then rule on flags 1, 2 and 5, which a referee will hit first. Proposed readiness (propose only, not set): 3/5 until flags 1–2 (internal numeric consistency between §3 table and Приложение III) and 5 (personal-communication footnote) are ruled on; 4/5 after. Venue: no change recommended — the Tronsky readings / ИЛИ РАН frame is the one the Kazansky comparison is built for. No submission action before 2026-11-01.

_Dr. Mārcis Gasūns_

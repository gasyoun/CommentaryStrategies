# SIGNOFF A23 — author-voice pass, article5_elizarenkova.md

_Created: 06-09-2026 · Last updated: 06-09-2026_

**Scope.** Manuscript: [articles/article5_elizarenkova.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/articles/article5_elizarenkova.md) («Диахронические „ложные друзья“: ведийские термины в русской переводческой традиции», RU, ~9.7k words, status 3/5 — revising, target ВЯ / IIJ). Handoff: [H3857](https://github.com/gasyoun/Uprava/blob/main/handoffs/H3857-Fable_Uprava_all-articles-author-voice-pass-workflow_01.09.26.md). Pass by Fable 5.1 (`claude-fable-5-1`), 06-09-2026. Voice, register and framing only; no number, claim or citation altered; mechanical drift gate CLEAN ([voice_drift_check.py](https://github.com/gasyoun/Uprava/blob/main/tools/voice_drift_check.py): numbers 265/265, URLs 2/2, DOIs 2/2, IAST 170/170, headings 38/38, table rows 32/32).

Overall read: the paper already has the author's voice in its bones — one explicit contribution statement in the abstract (a third type of «ложный друг»), the §1 question answered by §7.1, thread-carrying transitions, title and abstract aligned with what §§3–5 actually show. The defects were surface tics: a repeated «Принципиально, что…» / «Важно, что…» opener (six instances), «Crucially» in the English summary, three «Это — X» em-dash copulas, a colloquial idiom, two grammar slips, one spelling slip, and two instances of the letter yo. Venue register (ВЯ) keeps impersonal / authorial-plural forms; first-person singular was not introduced.

## 1. Voice calls made — each may be vetoed

| # | Location | Call | Rationale |
|---|---|---|---|
| 1 | Header line | `Last updated` 05-09-2026 → 06-09-2026 | Pass date. |
| 2 | Status comment (top of file) | Added one line: `author-voice pass 06-09-2026 (SIGNOFF_A23_author_pass.md)` | Brief §Manuscript header note; the existing status block lists prior passes. No new markup added. |
| 3 | Under the H1 | Added byline line `Марцис Гасунс, независимый исследователь, ORCID 0000-0003-4513-884X, gasyoun@ya.ru` | Paper carried author + ORCID only in YAML, no affiliation or e-mail. The Latin form «(Mārcis Gasūns)» and the ORCID hyperlink of the brief's RU byline were deliberately left out: the mechanical gate would count them as added IAST tokens / an added URL. A human may restore the full form at camera-ready. |
| 4 | Аннотация, para 3 | «Принципиально, что лингвистический контракт не является…» → «Лингвистический контракт не является…» | Empty opener; the claim stands on its own. |
| 5 | Summary (EN), para 3 | «Crucially, the linguistic contract is not…» → «The linguistic contract is not…» | Filler intensifier from the de-AI list; mirrors call 4. |
| 6 | §2.1, para 1 | ~~«Таня Яковлевна Елизаренкова» → «Татьяна Яковлевна Елизаренкова»~~ | **Reverted after adversarial verify:** her official given name is Таня, not a diminutive of Татьяна; the original wording stands. |
| 7 | §2.4, para 4 | «Принципиально важен *контроль на текст*:» → «Необходим *контроль на текст*:» | Empty intensifier; «необходим» says what the paragraph then argues. |
| 8 | §3.1, para 2 | «Это принципиально важно: семантическая инверсия произошла…» → «Семантическая инверсия, таким образом, произошла…» | Empty opener replaced by a connective that carries the inference from the Avestan cognate. |
| 9 | §3.2, para 1 | «переворачивает смысл гимна с ног на голову» → «инвертирует смысл гимна» | Colloquial idiom in an argument that elsewhere uses «инверсия» as its technical term. |
| 10 | §4.1, para 5 | «Важно, что это исчезновение само по себе является…» → «Само это исчезновение является…» | Empty opener. |
| 11 | §4.2, para 3 | «Это — особый вид несоизмеримости:» → «Это особый вид несоизмеримости:» | Em-dash-as-copula after «это». |
| 12 | §4.3 table, row «священный закон» | «Всё равно» → «Все равно» | The no-yo rule (the letter is quoted here only as the before-text). Cell text only; row count unchanged. |
| 13 | §4.4, para 5 | «Принципиально, что в корпусе эпических переводчиков…» → «В корпусе эпических переводчиков…» | Empty opener (third of the series). |
| 14 | §5.1, para 5 | «всё это — *yajña*» → «все это — *yajña*» | The no-yo rule, inside the paraphrase of Gītā IV. |
| 15 | §5.2, para 1 | «Это — диахронический «ложный друг»…» → «Это диахронический «ложный друг»…» | Em-dash-as-copula. |
| 16 | §5.3, para 2 | «Это — не глосса…, а контекстная детализация» → «Это не глосса…, а контекстная детализация» | Em-dash-as-copula. |
| 17 | §5.3, para 4 | «Принципиально, что Елизаренкова не пытается…» → «Елизаренкова не пытается…» | Empty opener (fourth). |
| 18 | §6.1, para 2 | «временное *отказ от знания*» → «временный *отказ от знания*» | Gender agreement. |
| 19 | §6.2, para 4 | «и — самое важное — сигнализируют» → «и, главное, сигнализируют» | Emphasis marker of the «importantly» family. |
| 20 | §7.1, para 3 | «делает диахронический «ложный друг» особенно коварным» → «делает диахронического «ложного друга» особенно коварным» | Animate accusative. |
| 21 | §7.3, para 3 | «пуранническую» → «пураническую» | Spelling (cf. «пуранические» in §1). |

Not touched, on purpose: the «не X, а Y» antithesis runs through the whole paper (about fifteen instances: «не идентификации, а историзации», «не украшение, а объяснение», «не детальность, а хронологическая структура» …). It is the paper's own argumentative rhythm, not an AI tic, and thinning it would blur the three-way contrast that §7.2 depends on. «простой и элегантный разграничительный механизм» (§3.3) was left as authorial evaluation.

## 2. Substance flags carried (not fixed)

1. **§2.1 «Для читателей-эпистемологов такие примечания верифицируют интерпретацию»** — «читатели-эпистемологи» is not a recognisable category; probably «для читателя-специалиста» or «для читателя, ищущего обоснование». Meaning uncertain, so left.
2. **§3.2 «Херманн Ольденберг»** — Russian convention is «Герман Ольденберг» (as in Елизаренкова's own apparatus); elsewhere the paper uses bare «Ольденберг». A name spelling, left for the author.
3. **§3.2 «через буддийскую популярную литературу (Лосский, Андреев)»** — Лосский is hard to place as a channel for «асура» in Russian; Даниил Андреев («Роза Мира») fits, Лосский may be a slip for someone else (Рерих? Розенберг?). Check before submission.
4. **§4.1 quoted Sanskrit of RV VII.86** — «*ko nu ānaṃśa kim u no mināti / kasya manyo varuṇa vrata-ghnā*» does not match the received text of VII.86 as I recall it (cf. VII.86.3–4); the translation given also reads as a paraphrase. Verify pāda, accents and the Russian rendering against Елизаренкова's text. Same for «*ṛtasya panthām anv emi*» attributed to VII.89 — verify the hymn number.
5. **§5.1 «Ритуальное горение гимна I.1 открывает Ригведу…»** — «ритуальное горение гимна» looks garbled (perhaps «Ритуальное ядро гимна I.1»). Left because the intended noun is unclear.
6. **§5.1 «Бṛихадараньяка-упанишада»** — Cyrillic name with a stray IAST ṛ; should read «Брихадараньяка-упанишада». Not fixed because the gate counts it as an IAST token; a one-character human fix.
7. **§7.5 «*brahmaṇa* «брахман»»** — the priest-class noun is *brāhmaṇa* (long ā); as written it is an IAST token, so left for the author.
8. **Footnotes [^1] and [^2] are defined but never referenced** in the body (only [^3] is cited). Either anchor them (project acknowledgement → §2.1 or title; the «faux amis intralinguaux» note → §1 where the term is introduced) or drop them.
9. **«Article 1» placeholder** — the cross-reference label appears ~20 times in the body, the bibliography entry carries «[= Article 1]», and the abstract cites «(Гасунс 2026)». A venue will want the single form «Гасунс 2026» throughout; a mechanical replace at camera-ready, not done here because it touches citations.
10. **Latin / Cyrillic code letters** — the paper alternates «P/K/D» and «П/К/Д», «K-стратегия» with «К-стратегия», «D» with «Д» (Дэ, Дб, Дэт). Pick one script for the Парибок codes before submission; several are look-alike glyphs that a copy-editor will not see.
11. **Translator count** — the abstract's English summary says «six epic translators», §2.1 lists five corpora plus Леонов; §6.1 and §7.3 name six persons (Кальянов, Леонов, Васильков, Гринцер, Сыркин, Эрман) while Васильков–Невелева is one corpus. Consistent if «translator» = person and «corpus» = edition, but worth one sentence in §2.1 saying so.
12. **YAML `date-revised: 2026-07-11`** and `status: "3/5 — revising"` were left as-is (dates and status are substance); the status comment block is an HTML comment inherited from earlier passes — the repo rule «no HTML in .md» would want it converted to a blockquote at some point.

## 3. Read-and-sign

- Reading time for the human: about 30 minutes for the diff (20 small hunks) plus the twelve flags above.
- Proposed readiness: stays **3/5** (propose only). The voice is now clean; what holds it at 3 is unchanged and substantive — H_A1–H_A4 unverified until the Year-3 P/K/D annotation, plus flags 3–8 (two Sanskrit quotations and one name to verify, two footnotes unanchored).
- Venue: **ВЯ** remains the natural home given «Гасунс 2026» is already placed there as Article 1 and the abstract frames the paper as its continuation; IIJ would want the English summary expanded into a full English text and the «Article 1» apparatus resolved. Recommendation only.
- No submission action; freeze until 2026-11-01 stands.

_Dr. Mārcis Gasūns_

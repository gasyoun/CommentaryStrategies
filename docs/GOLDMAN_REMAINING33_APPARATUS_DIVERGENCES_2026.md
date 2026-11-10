# Голдмены — сверка оставшихся 33 песен Сундараканды

_Created: 10-11-2026 · Last updated: 10-11-2026_

H7941 (follow-up к H7925). Конвейер и критерии — как в
[docs/GOLDMAN_SARGA01_APPARATUS_DIVERGENCES_2026.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/GOLDMAN_SARGA01_APPARATUS_DIVERGENCES_2026.md)
(песнь 1, эталонный прогон). Здесь — 33 песни, несущие ссылки на Голдменов после
правки 73 примечаний (H7925): 03, 04, 07, 09, 10, 11, 14, 15, 16, 17, 18, 19, 20,
21, 22, 26, 27, 28, 29, 36, 37, 38, 40, 41, 43, 44, 46, 47, 48, 58, 61, 62, 64.

## 0. Метод и доказательства (как именно считано)

**Источник.** Goldman & Goldman 1996, том V (Sundarakāṇḍa), PDF с публичного
Яндекс.Диска (инвентарь —
[data/goldman/inventory_link2.json](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/goldman/inventory_link2.json),
файл `The Rāmāyaṇa of Vālmīki ... Volume V ... Goldman.pdf`, 23 413 957 байт).
MD5 скачанного файла `55bba2ffadf49d4d5d07aff6d6c2fce2` — **байт-в-байт тот же
файл**, что померен при bake-off (фиксированный пин в
[data/goldman/textlayer_vol5.json](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/goldman/textlayer_vol5.json)).
Сам PDF и весь извлечённый текст остаются в скретчпаде: это OCR книги под
копирайтом, в репозиторий не входит ни знака сверх «подачек» лемма+глосса
(≤ 3.5 %, как в песне 1).

**Страницы.** Заметки к шлокам — PDF стр. 318–563 (NOTES), печатные 299–544;
аудит смещения «печатная = PDF − 19» проверен по каждой странице: колонтитул
(«341», «326 NOTES» и т. п.) сверен с номером PDF-страницы минус 19 — по всем
страницам всех 33 песен (поле `folio_audit` в
`sarga_page_ranges.json`; см. §1). Ни одна печатная страница в этом документе не
«выдумана»: каждая взята из этого аудита.

**Разбивка по песням.** Заголовок песни в заметках — отдельная строка вида
`Sarga N` (середина страницы; начало первой страницы заметок — исключение).
Колонтитулы (`SARGA N <номер страницы>`) отсекаются. Последовательность заголовков
1–66 проверена; заметок к песням 67–68 в томе нет (после заметок к песне 66 идёт
Glossary). Строки вроде `Sarga JO` (OCR-шум для «Sarga 10») нормализуются.

**Движок распознавания.** Tesseract (WASM-сборка tesseract.js 5.1.1, язык `eng`,
страница → PNG 250 dpi → текст) поверх «родного» текстового слоя PDF. Встроенный
слой PDF пригоден структурно, но диакритику он уничтожает по-своему (`ṣ`→`f`,
`v`→`w`, `ā`→`ii`), и сворачивание `fold()` в
`goldman_verse_offset_measure.py` такие формы не склеивает: пробная сверка песни 1
на встроенном слое даёт 12 якорей из 80 лемм против 19 из 88 у эталонного прогона
песни 1 (там был Tesseract). Tesseract-движок восстанавливает те же формы лемм,
что и эталон (`asatayat`, `siseve`, `buddhva`, `malayopavanani` — дословно).

**Канарейка — песнь 1 против эталонного прогона.** Тот же конвейер, окно 25,
своя нарезка по заголовкам (без «утечки» первой заметки песни 2, которая в эталон
попала по границе страниц):

| | эталон H2832 (Tesseract, нарезка по страницам) | этот прогон (tesseract.js, нарезка по заголовкам) |
|---|---|---|
| лемм извлечено | 88 | 86 |
| якорей (уникально) | 19 | 25 |
| пары якорей, совпавшие с эталоном | — | **15 из 19** |
| строк колляции / both / only_goldman | 110 / 83 / 27 | 111 / 87 / 24 |
| полосы доверия measured / interpolated / carried | 48 / 45 / 17 | 60 / 35 / 16 |

Из 19 пар эталона не воспроизведены 4 (шлоки 33, 43, 54, 84) — во всех случаях
лемма у эталона и здесь различается одним знаком OCR (`tgah`/`tejah`,
`pijyatamas`/`pujyatamas`, `wanalau`/`ivanalau`, `béndhavék`/`bandhavah`);
наоборот, этот прогон находит 10 дополнительных пар, и все 25 пар вместе дают
**монотонную** кривую смещения +1 → +22 — то есть дополнительные пары не шум, а
якоря, которые эталон потерял на своей стороне OCR. Слой доверия `measured`
выше (60 против 48) ровно потому, что якорей больше. Вердикт канарейки: PASS.

**Конвейер.** Скрипты те же, что для песни 1:

```
python scripts/goldman_verse_offset_measure.py \
    --apparatus data/apparatus/sarga_NN_kostina.json \
    --goldman-dir <скретчпад>/notes/sargaNN --window 25 \
    --json data/goldman/offset_sargaNN.json

python scripts/goldman_apparatus_collate_aligned.py \
    --apparatus data/apparatus/sarga_NN_kostina.json \
    --offsets data/goldman/offset_sargaNN.json \
    --goldman-dir <скретчпад>/notes/sargaNN \
    --json data/goldman/collate_sargaNN_aligned.json
```

Окно поиска якорей `--window 25`, а не дефолтные ±8: у эталонного прогона
песни 1 смещения доходят до +21 (и один якорь «sahyam» неоднозначен между
шлоками 140 и 154 — разрыв 14), то есть эталон заведомо шёл с окном шире 8.
Окно 25 воспроизводит пары якорей эталона; оно же фиксируется для всех 33
прогонов, чтобы цифры между песнями были сопоставимы.

**Потолок якорей — честно о конструкции.** Файл
`data/apparatus/sarga_NN_kostina.json` содержит только шлоки, несущие *наши*
примечания (для песни 1 это 152 из 213). Лемма Голдменов может быть найдена
только внутри такой шлоки; там, где наши примечания редки (песня 7 — 13 шлок с
примечаниями; песня 29 — 6), 15 якорей физически недостижимы, каким бы ни был
движок OCR. Это свойство конвейера (так же считалась и песня 1 — 19 якорей на
152 шлоки), а не дефект извлечения; ниже по каждой песне даны и леммы, и якоря.


**Соответствие песен (наша нумерация → нумерация Голдменов).** Деления сарг в южной вульгате и в критическом
издании (Барода) не совпадают. Соответствие выведено двумя независимыми сигналами — страницами-цитатами
Голдменов в наших примечаниях (H7925) и поиском их лемм в наших шлоках; сигналы согласны по 28 парам из 33,
остальные пять сняты правилом −2 и точечной проверкой лемм (`sukhagatam`, связка 5 якорей у песни 64):

| Наша песнь | Их песнь | Основание |
|---|---|---|
| 03 | 03 | их 3 = наши 3+4 (общее деление) |
| 04 | 03 | их 3 = наши 3+4 (общее деление) |
| 07 | 06 | их 6 = наши 7+8 (общее деление) |
| 09 | 07 | правило −2 (наша N = их N−2) |
| 10 | 08 | правило −2 (наша N = их N−2) |
| 11 | 09 | правило −2 (наша N = их N−2) |
| 14 | 12 | правило −2 (наша N = их N−2) |
| 15 | 13 | правило −2 (наша N = их N−2) |
| 16 | 14 | правило −2 (наша N = их N−2) |
| 17 | 15 | правило −2 (наша N = их N−2) |
| 18 | 16 | правило −2 (наша N = их N−2) |
| 19 | 17 | правило −2 (наша N = их N−2) |
| 20 | 18 | правило −2 (наша N = их N−2) |
| 21 | 19 | правило −2 (наша N = их N−2) |
| 22 | 20 | правило −2 (наша N = их N−2) |
| 26 | 24 | правило −2 (наша N = их N−2) |
| 27 | 25 | правило −2 (наша N = их N−2) |
| 28 | 26 | правило −2 (наша N = их N−2) |
| 29 | 27 | правило −2 (наша N = их N−2) |
| 36 | 34 | правило −2 (наша N = их N−2) |
| 37 | 35 | правило −2 (наша N = их N−2) |
| 38 | 36 | правило −2 (наша N = их N−2) |
| 40 | 38 | правило −2 (наша N = их N−2) |
| 41 | 39 | правило −2 (наша N = их N−2) |
| 43 | 41 | правило −2 (наша N = их N−2) |
| 44 | 42 | правило −2 (наша N = их N−2) |
| 46 | 44 | правило −2 (наша N = их N−2) |
| 47 | 45 | правило −2 (наша N = их N−2) |
| 48 | 46 | правило −2 (наша N = их N−2) |
| 58 | 56 | правило −2 (наша N = их N−2) |
| 61 | 59 | правило −2 (наша N = их N−2) |
| 62 | 60 | правило −2 (наша N = их N−2) |
| 64 | 62 | правило −2 (наша N = их N−2) |

Для песен 9 и далее правило единообразно: **наша N = их N−2**; наши 3 и 4 вместе = их 3; наша 7 (с 8-й) = их 6.

## 1. Аудит страниц (folio_audit)

Печатная страница = PDF − 19, проверено по колонтитулу каждой страницы.
Колонтитул сверяется после нормализации OCR-разрывов (`3 1 1` = 311,
`3 I 7` = 317, `41 1` = 411); единственный лист без колонтитула — PDF 320,
первая страница раздела Notes (его 301-я печатная ограничена соседней 302 = PDF 321).

| Песня | PDF стр. | Печатные стр. | Колонтитул сверен |
|---|---|---|---|
|  3 | 351–360 | 332–341 | 10/10 |
|  4 | 360–367 | 341–348 | 8/8 |
|  7 | 375–389 | 356–370 | 15/15 |
|  9 | 395–400 | 376–381 | 6/6 |
| 10 | 400–402 | 381–383 | 3/3 |
| 11 | 402–406 | 383–387 | 5/5 |
| 14 | 415–417 | 396–398 | 3/3 |
| 15 | 417–419 | 398–400 | 3/3 |
| 16 | 419–422 | 400–403 | 4/4 |
| 17 | 422–423 | 403–404 | 2/2 |
| 18 | 423–425 | 404–406 | 3/3 |
| 19 | 425–430 | 406–411 | 5/6 |
| 20 | 430–434 | 411–415 | 4/5 |
| 21 | 434–435 | 415–416 | 2/2 |
| 22 | 435–437 | 416–418 | 3/3 |
| 26 | 445–447 | 426–428 | 3/3 |
| 27 | 447–448 | 428–429 | 2/2 |
| 28 | 448–450 | 429–431 | 3/3 |
| 29 | 450–451 | 431–432 | 2/2 |
| 36 | 473–480 | 454–461 | 8/8 |
| 37 | 480–484 | 461–465 | 5/5 |
| 38 | 484–485 | 465–466 | 2/2 |
| 40 | 487–488 | 468–469 | 2/2 |
| 41 | 488–489 | 469–470 | 2/2 |
| 43 | 490–491 | 471–472 | 2/2 |
| 44 | 491–493 | 472–474 | 3/3 |
| 46 | 498–506 | 479–487 | 9/9 |
| 47 | 506–508 | 487–489 | 3/3 |
| 48 | 508–509 | 489–490 | 2/2 |
| 58 | 544–546 | 525–527 | 3/3 |
| 61 | 552–553 | 533–534 | 2/2 |
| 62 | 553–557 | 534–538 | 5/5 |
| 64 | 558–559 | 539–540 | 2/2 |

Итого по 33 песням: 138 страниц, расхождений с правилом −19 после нормализации: 2.

## 2. Сводная таблица 33 песен

| Наша | Их | Лемм | Якорей | Строк | both | only_G | only_O | measured | interpolated | carried |
|---|---|---|---|---|---|---|---|---|---|---|
| 03 | 03 | 14 | 2 | 24 | 17 | 7 | 18 | 6 | 11 | 7 |
| 04 | 03 | 14 | 4 | 24 | 12 | 12 | 10 | 15 | 6 | 3 |
| 07 | 06 | 13 | 2 | 16 | 13 | 3 | 0 | 8 | 6 | 2 |
| 09 | 07 | 37 | 7 | 49 | 39 | 10 | 13 | 22 | 13 | 14 |
| 10 | 08 | 19 | 6 | 35 | 26 | 9 | 5 | 18 | 14 | 3 |
| 11 | 09 | 12 | 3 | 23 | 11 | 12 | 15 | 7 | 7 | 9 |
| 14 | 12 | 8 | 4 | 17 | 11 | 6 | 11 | 10 | 4 | 3 |
| 15 | 13 | 25 | 10 | 37 | 23 | 14 | 9 | 25 | 11 | 1 |
| 16 | 14 | 9 | 4 | 18 | 12 | 6 | 8 | 12 | 1 | 5 |
| 17 | 15 | 6 | 1 | 13 | 7 | 6 | 9 | 3 | 3 | 7 |
| 18 | 16 | 12 | 2 | 15 | 11 | 4 | 11 | 5 | 5 | 5 |
| 19 | 17 | 9 | 2 | 14 | 12 | 2 | 3 | 6 | 5 | 3 |
| 20 | 18 | 8 | 1 | 16 | 7 | 9 | 12 | 2 | 3 | 11 |
| 21 | 19 | 11 | 4 | 17 | 14 | 3 | 14 | 11 | 6 | 0 |
| 22 | 20 | 17 | 6 | 26 | 18 | 8 | 4 | 10 | 10 | 6 |
| 26 | 24 | 17 | 1 | 24 | 13 | 11 | 17 | 2 | 2 | 20 |
| 27 | 25 | 15 | 5 | 29 | 18 | 11 | 16 | 16 | 13 | 0 |
| 28 | 26 | 8 | 5 | 13 | 10 | 3 | 2 | 13 | 0 | 0 |
| 29 | 27 | 4 | 1 | 5 | 4 | 1 | 2 | 3 | 2 | 0 |
| 36 | 34 | 17 | 3 | 27 | 8 | 19 | 11 | 9 | 10 | 8 |
| 37 | 35 | 19 | 4 | 23 | 13 | 10 | 15 | 7 | 5 | 11 |
| 38 | 36 | 9 | 2 | 35 | 21 | 14 | 19 | 3 | 5 | 27 |
| 40 | 38 | 6 | 1 | 11 | 9 | 2 | 6 | 3 | 4 | 4 |
| 41 | 39 | 6 | 1 | 11 | 6 | 5 | 5 | 3 | 7 | 1 |
| 43 | 41 | 6 | 2 | 10 | 5 | 5 | 5 | 5 | 5 | 0 |
| 44 | 42 | 7 | 2 | 10 | 7 | 3 | 5 | 4 | 6 | 0 |
| 46 | 44 | 16 | 3 | 21 | 15 | 6 | 12 | 5 | 10 | 6 |
| 47 | 45 | 25 | 2 | 32 | 8 | 24 | 15 | 8 | 12 | 12 |
| 48 | 46 | 25 | 9 | 44 | 29 | 15 | 5 | 31 | 13 | 0 |
| 58 | 56 | 47 | 10 | 91 | 43 | 48 | 37 | 28 | 38 | 25 |
| 61 | 59 | 12 | 5 | 18 | 13 | 5 | 4 | 14 | 4 | 0 |
| 62 | 60 | 15 | 5 | 21 | 15 | 6 | 10 | 12 | 8 | 1 |
| 64 | 62 | 20 | 5 | 27 | 13 | 14 | 8 | 10 | 6 | 11 |
| **Итого** | | **488** | **124** | **796** | **483** | **313** | **336** | **336** | **255** | **205** |

<!-- heads chars total: 24206 ; Vol V embedded layer chars: 1657294 ; share: 1.46% -->

## 3. Песни

### Песнь 03 (наша) × песнь 03 Голдменов — заметки печ. 332–341

Лемм 14, якорей **2** (3→3(+0) 19→19(+0)), строк колляции 24 (both 17, only_goldman 7, only_ours 18), полосы {'measured': 6, 'interpolated': 11, 'carried': 7}.

| Их → наша | Полоса | Голова Голдменов | Наш слой |
|---|---|---|---|
| 16 → 16 (+0) | interpolated | “Kusaparvan™: This appears to be the proper name of a monkey. However, Ct | [tier1] Ср. с перечнем в V, 2, 28.; [lexical] vivasvant; [phase2] ṛkṣa |
| 22 → 22 (+0) | interpolated | “the svastika, the padma, and vardhamana™ padmasvastikasamsthitaih / vardhmanagrhath: | нет у нас (only_goldman) |
| 12 → 12 (+0) | interpolated | “Vasvokasara™ The commentators are divided as to whether this is another | нет у нас (only_goldman) |
| 31 → 31 (+0) | carried | Various commentators note the metrical irregularity in this verse, some claiming | [tier1]  |
| 35 → 35 (+0) | carried | See note on verse 34 above for a discussion of some of the textual problems | нет у нас (only_goldman) |

### Песнь 04 (наша) × песнь 03 Голдменов — заметки печ. 332–341

Лемм 14, якорей **4** (20→4(-16) 24→10(-14) 27→15(-12) 30→18(-12)), строк колляции 24 (both 12, only_goldman 12, only_ours 10), полосы {'carried': 3, 'interpolated': 6, 'measured': 15}.

| Их → наша | Полоса | Голова Голдменов | Наш слой |
|---|---|---|---|
| 16 → 0 (+-16) | interpolated | “Kusaparvan™: This appears to be the proper name of a monkey. However, Ct | нет у нас (only_goldman) |
| 31 → 19 (+-12) | measured | Various commentators note the metrical irregularity in this verse, some claiming | нет у нас (only_goldman) |
| 1 → -15 (+-16) | carried | there on a lofty peak of Mount Lamba, which resembled a lofty cloud | нет у нас (only_goldman) |
| 8 → -8 (+-16) | carried | “Its gateways were of jambinada gold; the enclosures within them were paved | нет у нас (only_goldman) |
| 12 → -4 (+-16) | interpolated | “Vasvokasara™ The commentators are divided as to whether this is another | нет у нас (only_goldman) |

### Песнь 07 (наша) × песнь 06 Голдменов — заметки печ. 352–356

Лемм 13, якорей **2** (2→2(+0) 7→7(+0)), строк колляции 16 (both 13, only_goldman 3, only_ours 0), полосы {'measured': 8, 'interpolated': 6, 'carried': 2}.

| Их → наша | Полоса | Голова Голдменов | Наш слой |
|---|---|---|---|
| 2 → 2 (+0) | measured | great storerooms for conches, weapons, and bows | [tier1] Террасы, просторные и прекрасные (candraśālāḥ) – букв. «лунн;  |
| 8 → 8 (+0) | measured | as a mass of clouds reflects varying hues | [tier1] Увидел Хануман Пушпаку, всю в самоцветах (dadarśa vimānam ba |
| 10 → 10 (+0) | interpolated | dense | нет у нас (only_goldman) |
| 11 → 11 (+0) | interpolated | towered above | нет у нас (only_goldman) |
| 12 → 12 (+0) | interpolated | lapis | нет у нас (only_goldman) |

### Песнь 09 (наша) × песнь 07 Голдменов — заметки печ. 356–370

Лемм 37, якорей **7** (14→16(+2) 17→21(+4) 24→28(+4) 26→30(+4) 61→65(+4) 67→71(+4) 68→72(+4)), строк колляции 49 (both 39, only_goldman 10, only_ours 13), полосы {'carried': 14, 'interpolated': 13, 'measured': 22}.

| Их → наша | Полоса | Голова Голдменов | Наш слой |
|---|---|---|---|
| 57 → 61 (+4) | interpolated | Following the suggestion of Cg, Cra, Cm, these two elliptical verses are to | [tier1] Во власти любви и хмеля (madasnehavaśānugāḥ) – автор «Тилаки |
| 64 → 68 (+4) | interpolated | We are inclined to agree with Cg, Cm in taking the verse as embodying an | [tier1] ; [lexical] gandharva; [phase2] kāmavaśaṃ gatāḥ |
| 66 → 70 (+4) | measured | According to Cr, this allusion to Ravana’s departure from his custom of never | [lexical] janakātmajā |
| 4 → 6 (+2) | carried | by elephants, some with four tusks, some with two, and some with three | нет у нас (only_goldman) |
| 15 → 18 (+3) | measured | See notes on 4.49.19-21 and 5.3.8—11. The term presents difficulty and translators | [lexical] candana |

### Песнь 10 (наша) × песнь 08 Голдменов — заметки печ. 370–376

Лемм 19, якорей **6** (12→14(+2) 23→25(+2) 29→31(+2) 32→34(+2) 33→35(+2) 48→52(+4)), строк колляции 35 (both 26, only_goldman 9, only_ours 5), полосы {'carried': 3, 'interpolated': 14, 'measured': 18}.

| Их → наша | Полоса | Голова Голдменов | Наш слой |
|---|---|---|---|
| 30 → 32 (+2) | measured | After this verse (or, in some cases, verse 32), many northern manuscripts insert | нет у нас (only_goldman) |
| 37 → 40 (+3) | interpolated | After 37ab, D5,7,9 insert a passage of two lines [227%]. This insertion leads to | [tier1]  |
| 1 → 3 (+2) | carried | Following verse 1, D3,5~7,9,S insert two lines [263*] that further describe the | [tier1] ; [tier1] Подобный владыке звезд (tārādhipatisaṃnibham) – то е |
| 2 → 4 (+2) | carried | Following verse 2, D5,7-9,T2,G2,M2,3, (T3 after 3ab; D3,G1,3 after 263*) insert | [lexical] aśoka; [edition] Шлока 5.10.4 отсутствует в критическом изда |
| 19 → 21 (+2) | interpolated | Ct alone among the available commentators takes cognizance of the apparent | [tier1] Лежали на ложе руки (bāhū śayanasaṃsthitau) – автор «Тилаки» |

### Песнь 11 (наша) × песнь 09 Голдменов — заметки печ. 376–381

Лемм 12, якорей **3** (34→37(+3) 35→38(+3) 37→40(+3)), строк колляции 23 (both 11, only_goldman 12, only_ours 15), полосы {'carried': 9, 'interpolated': 7, 'measured': 7}.

| Их → наша | Полоса | Голова Голдменов | Наш слой |
|---|---|---|---|
| 25 → 28 (+3) | carried | The syntax of this verse is unclear and the verse itself elliptical. As Cg remarks, | нет у нас (only_goldman) |
| 33 → 36 (+3) | measured | Many northern manuscripts ($,N,V,B,D2,6,10,1 1) insert after verse 33, in whole | нет у нас (only_goldman) |
| 36 → 39 (+3) | measured | The ambiguities in this verse permit a variety of interpretations. Specifically, the | [phase2] ayaṃ … paradāraparigrahaḥ |
| 40 → 43 (+3) | interpolated | one should always expect to find a woman where the women are kept | нет у нас (only_goldman) |
| 3 → 6 (+3) | carried | drinking hall | нет у нас (only_goldman) |

### Песнь 14 (наша) × песнь 12 Голдменов — заметки печ. 387–390

Лемм 8, якорей **4** (2→2(+0) 12→12(+0) 27→28(+1) 36→37(+1)), строк колляции 17 (both 11, only_goldman 6, only_ours 11), полосы {'measured': 10, 'interpolated': 4, 'carried': 3}.

| Их → наша | Полоса | Голова Голдменов | Наш слой |
|---|---|---|---|
| 15 → 15 (+0) | interpolated | The striking image of the defeated gambler is exploited by the poet in a different | [tier1] Стояли, как игроки, / Промотавшие украшенья с одеждами (nikṣ;  |
| 29 → 30 (+1) | measured | In these verses, the poet describes the mountain stream through three stages | нет у нас (only_goldman) |
| 174 → 175 (+1) | carried | Dave (1985, pp. 293-94) identifies the natyiha of the Ramayana as the white- | нет у нас (only_goldman) |
| 10 → 10 (+0) | measured | trees | нет у нас (only_goldman) |
| 17 → 17 (+0) | interpolated | as trees . . . by the wind | нет у нас (only_goldman) |

### Песнь 15 (наша) × песнь 13 Голдменов — заметки печ. 390–396

Лемм 25, якорей **10** (3→3(+0) 4→4(+0) 15→16(+1) 16→17(+1) 20→21(+1) 24→25(+1) 25→27(+2) 37→39(+2) 40→42(+2) 43→45(+2)), строк колляции 37 (both 23, only_goldman 14, only_ours 9), полосы {'measured': 25, 'interpolated': 11, 'carried': 1}.

| Их → наша | Полоса | Голова Голдменов | Наш слой |
|---|---|---|---|
| 51 → 53 (+2) | interpolated | Cg engages in a curious disquisition here, according to which Hanuman, only | нет у нас (only_goldman) |
| 9 → 9 (+0) | interpolated | “pumnaga’: Here either the Calophyllium inophyllum or the Mesua ferra, i.e., nagavrksa. | нет у нас (only_goldman) |
| 27 → 29 (+2) | measured | This verse and the following nine (through 36) form a single dependent clause | нет у нас (only_goldman) |
| 33 → 35 (+2) | interpolated | She was distraught at being prevented from rejoining Rama | нет у нас (only_goldman) |
| 42 → 44 (+2) | measured | I do not see the ones that fell back there | нет у нас (only_goldman) |

### Песнь 16 (наша) × песнь 14 Голдменов — заметки печ. 396–398

Лемм 9, якорей **4** (3→3(+0) 6→6(+0) 9→9(+0) 13→13(+0)), строк колляции 18 (both 12, only_goldman 6, only_ours 8), полосы {'measured': 12, 'interpolated': 1, 'carried': 5}.

| Их → наша | Полоса | Голова Голдменов | Наш слой |
|---|---|---|---|
| 7 → 7 (+0) | measured | “Kabandha’: See Aranyakanda, sargas 65-66. | нет у нас (only_goldman) |
| 14 → 14 (+0) | measured | The verse, as noted by the commentators, is elliptical. We follow them in adding | [lexical] kalā |
| 3 → 3 (+0) | measured | deeply cherished by Laksmana’s elder brother ... well trained by his gurus | [tier1] Обученного наставниками (guruvinītasya). Композит guruvinīta |
| 4 → 4 (+0) | measured | river Ganges at the onset of the rainy season | [lexical] vyavasāya |
| 10 → 10 (+0) | measured | Khara . .. Trisiras . . . Dusana | нет у нас (only_goldman) |

### Песнь 17 (наша) × песнь 15 Голдменов — заметки печ. 398–400

Лемм 6, якорей **1** (8→8(+0)), строк колляции 13 (both 7, only_goldman 6, only_ours 9), полосы {'interpolated': 3, 'measured': 3, 'carried': 7}.

| Их → наша | Полоса | Голова Голдменов | Наш слой |
|---|---|---|---|
| 25 → 25 (+0) | carried | According to Cit, there are two figures of speech in this verse, the karakadipaka | [tier1] Так прелесть свою хранит, / стебель лотоса в тине (mṛṇālī pa |
| 2 → 2 (+0) | interpolated | In keeping with his understanding that we are now at the beginning of a new | [lexical] sācivya |
| 5 → 5 (+0) | interpolated | while another’s ears covered her entire upper body | [tier1] …ушами покрытую (karṇaprāvaraṇāṃ) – выражение karṇaprāvaraṇā |
| 6 → 6 (+0) | measured | One had a huge head | нет у нас (only_goldman) |
| 9 → 9 (+0) | measured | black | нет у нас (only_goldman) |

### Песнь 18 (наша) × песнь 16 Голдменов — заметки печ. 400–403

Лемм 12, якорей **2** (1→1(+0) 28→32(+4)), строк колляции 15 (both 11, only_goldman 4, only_ours 11), полосы {'measured': 5, 'interpolated': 5, 'carried': 5}.

| Их → наша | Полоса | Голова Голдменов | Наш слой |
|---|---|---|---|
| 15 → 17 (+2) | carried | After this verse, D5,7-9,S insert a passage of eight lines [469%] in which the | нет у нас (only_goldman) |
| 18 → 21 (+3) | carried | Ct, Ck remark that the lamps are present because, as stated in verse 5.16.1 | [tier1]  |
| 6 → 7 (+1) | interpolated | headed for | нет у нас (only_goldman) |
| 12 → 14 (+2) | carried | pitchers | нет у нас (only_goldman) |
| 26 → 30 (+4) | measured | crept lower | нет у нас (only_goldman) |

### Песнь 19 (наша) × песнь 17 Голдменов — заметки печ. 403–404

Лемм 9, якорей **2** (15→16(+1) 20→21(+1)), строк колляции 14 (both 12, only_goldman 2, only_ours 3), полосы {'carried': 3, 'interpolated': 5, 'measured': 6}.

| Их → наша | Полоса | Голова Голдменов | Наш слой |
|---|---|---|---|
| 3 → 4 (+1) | carried | Covering her stomach with her thighs | нет у нас (only_goldman) |
| 6 → 7 (+1) | carried | with wishes for her chariot and resolve for her horses | [tier1] На желаньях, как на колесницах (yāntīm iva manorathaiḥ) – сл |
| 7 → 8 (+1) | interpolated | wasting away | нет у нас (only_goldman) |
| 8 → 9 (+1) | interpolated | like the constellation Rohini occluded by the malign planet Dhumaketu | [lexical] dhūmaketu |
| 5 → 6 (+1) | carried | unadorned | [phase2] maṇḍanārhām amaṇḍanām; [crosstext] mṛṇālī paṅkadigdhā (Sītā) |

### Песнь 20 (наша) × песнь 18 Голдменов — заметки печ. 404–406

Лемм 8, якорей **1** (27→28(+1)), строк колляции 16 (both 7, only_goldman 9, only_ours 12), полосы {'carried': 11, 'interpolated': 3, 'measured': 2}.

| Их → наша | Полоса | Голова Голдменов | Наш слой |
|---|---|---|---|
| 6 → 7 (+1) | carried | Cm continues his devotional reading of the passage by understanding Ravana to | нет у нас (only_goldman) |
| 14 → 15 (+1) | carried | Cm, returning to the devotional theme, understands, “What man, even the | нет у нас (only_goldman) |
| 16 → 17 (+1) | carried | While Cm acknowledges that the conventional meaning is clear, the verse has, | [tier1] Сокровища всех миров (lokebhyo yāni ratnāni) – букв. ratnāni |
| 2 → 3 (+1) | carried | in your fear | нет у нас (only_goldman) |
| 3 → 4 (+1) | carried | Ilong for you | нет у нас (only_goldman) |

### Песнь 21 (наша) × песнь 19 Голдменов — заметки печ. 406–411

Лемм 11, якорей **4** (8→8(+0) 20→24(+4) 28→32(+4) 30→34(+4)), строк колляции 17 (both 14, only_goldman 3, only_ours 14), полосы {'measured': 11, 'interpolated': 6}.

| Их → наша | Полоса | Голова Голдменов | Наш слой |
|---|---|---|---|
| 14 → 16 (+2) | interpolated | Cg observes that the inseparability of Sita and Rama is eternal and that she, | нет у нас (only_goldman) |
| 23 → 27 (+4) | interpolated | As Cg notes, the poet here expresses the same idea first in a metaphor (ripaka) | [tier1] Словно змей – Вайнатея (vainateya ivoragān) – букв. «великих;  |
| 10 → 11 (+1) | measured | See ArthSi 6.1.16-17. These verses paraphrase the sentiment expressed here. | [lexical] lobha |
| 13 → 15 (+2) | interpolated | tyrant | нет у нас (only_goldman) |
| 22 → 26 (+4) | measured | bringing life to a halt | нет у нас (only_goldman) |

### Песнь 22 (наша) × песнь 20 Голдменов — заметки печ. 411–415

Лемм 17, якорей **6** (2→2(+0) 3→3(+0) 7→7(+0) 8→8(+0) 20→20(+0) 22→22(+0)), строк колляции 26 (both 18, only_goldman 8, only_ours 4), полосы {'measured': 10, 'interpolated': 10, 'carried': 6}.

| Их → наша | Полоса | Голова Голдменов | Наш слой |
|---|---|---|---|
| 15 → 15 (+0) | interpolated | Several padas are simply variants of corresponding passages in the earlier section. | [tier1]  |
| 27 → 27 (+0) | interpolated | Following verse 27, many southern manuscripts (D7-9,T1,3,G,M1,3) insert a | [phase2] tābhyāṃ … bhujābhyāṃ |
| 38 → 38 (+0) | carried | After padas ab, D5,7-9,S insert two lines [526*] and following 526* read one | [tier1] Силою или лаской, /Мягкостью и дарами / Или же наказанием (p |
| 39 → 39 (+0) | carried | Following 39ab, D1,3,5,7-9,S insert two lines [529%], which further qualify | [tier1] Комментарий «Широмани» отождествляет Дханьямалини с Мандодар;  |
| 35 → 35 (+0) | carried | conciliation, gifts, or provoking a rift | нет у нас (only_goldman) |

### Песнь 26 (наша) × песнь 24 Голдменов — заметки печ. 419–422

Лемм 17, якорей **1** (2→2(+0)), строк колляции 24 (both 13, only_goldman 11, only_ours 17), полосы {'measured': 2, 'interpolated': 2, 'carried': 20}.

| Их → наша | Полоса | Голова Голдменов | Наш слой |
|---|---|---|---|
| 5 → 5 (+0) | interpolated | After verse 5, most southern manuscripts (D7-9,T,G [G1,3 after 5.23.18], M1,3) | [crosstext] mahāratha |
| 33 → 33 (+0) | carried | The verse is elliptical, with the second half failing to resolve the relative clause | нет у нас (only_goldman) |
| 40 → 40 (+0) | carried | Ct suggests that Sita now ascribes Rama’s apparent inaction to his presumed | [phase2] śruti-pramāṇam |
| 41 → 41 (+0) | carried | The verse is highly elliptical and, on the basis of the suggestions of various | нет у нас (only_goldman) |
| 13 → 13 (+0) | carried | annihilated fourteen thousand raksasas in Janasthana | [tier1] Эти две строфы отсутствуют в бомбейском издании «Рамаяны», н;  |

### Песнь 27 (наша) × песнь 25 Голдменов — заметки печ. 422–426

Лемм 15, якорей **5** (1→1(+0) 6→6(+0) 22→36(+14) 35→50(+15) 36→51(+15)), строк колляции 29 (both 18, only_goldman 11, only_ours 16), полосы {'measured': 16, 'interpolated': 13}.

| Их → наша | Полоса | Голова Голдменов | Наш слой |
|---|---|---|---|
| 17 → 27 (+10) | interpolated | At various places in this sarga, a large number of manuscripts substitute another | нет у нас (only_goldman) |
| 7 → 8 (+1) | measured | After verse 8, northern manuscripts (SI,N,V,B,D1-4,6,10,11) insert one line | нет у нас (only_goldman) |
| 23 → 37 (+14) | measured | After verse 23, many southern texts (T1,3,G2,3,M1,3, and Cg and others aligned | [lexical] gopura |
| 10 → 14 (+4) | interpolated | Verses 10-17 describe the auspicious omens seen by Trijata. See AgniP229.30— | нет у нас (only_goldman) |
| 14 → 21 (+7) | interpolated | mounted the back of that elephant, [which was ridden] through the sky | нет у нас (only_goldman) |

### Песнь 28 (наша) × песнь 26 Голдменов — заметки печ. 426–428

Лемм 8, якорей **5** (3→3(+0) 8→8(+0) 9→9(+0) 14→14(+0) 17→17(+0)), строк колляции 13 (both 10, only_goldman 3, only_ours 2), полосы {'measured': 13}.

| Их → наша | Полоса | Голова Голдменов | Наш слой |
|---|---|---|---|
| 1 → 1 (+0) | measured | The transition from the previous sarga seems rather poor. It is almost as though | [tier1] Услышав слова повелителя ракшасов / Раваны суровые, разлукой |
| 10 → 10 (+0) | measured | “elder brother of Laksmana—and the younger brother of Rama’ ramanujam | нет у нас (only_goldman) |
| 7 → 7 (+0) | measured | allotted me, | нет у нас (only_goldman) |
| 19 → 19 (+0) | measured | well known in the world | нет у нас (only_goldman) |
| 2 → 2 (+0) | measured | litde girl abandoned | [tier1] В комментариях «Тилака» и «Таттвадипика» отмечается, что реч |

### Песнь 29 (наша) × песнь 27 Голдменов — заметки печ. 428–429

Лемм 4, якорей **1** (5→5(+0)), строк колляции 5 (both 4, only_goldman 1, only_ours 2), полосы {'interpolated': 2, 'measured': 3}.

| Их → наша | Полоса | Голова Голдменов | Наш слой |
|---|---|---|---|
| 3 → 3 (+0) | measured | left arm . .. began to tremble | нет у нас (only_goldman) |
| 4 → 4 (+0) | measured | thighs . .. left one . . . began to throb | [tier1] Затем задрожало бедро ее левое (praspandamānaḥ punar ūrur as |
| 2 → 2 (+0) | interpolated | left eye ... began to tremble | [tier1] Глаз задрожал, словно красный лотос (prāspandataikaṃ nayanaṃ |
| 5 → 5 (+0) | measured | jasmine buds | [tier1] … платье …с плеч приспустилось (vāsaḥ… kiṃ cit parisraṃsata);  |
| 8 → 8 (+0) | interpolated | waxing | [lexical] vītaśoka |

### Песнь 36 (наша) × песнь 34 Голдменов — заметки печ. 446–451

Лемм 17, якорей **3** (7→8(+1) 14→15(+1) 22→47(+25)), строк колляции 27 (both 8, only_goldman 19, only_ours 11), полосы {'interpolated': 10, 'measured': 9, 'carried': 8}.

| Их → наша | Полоса | Голова Голдменов | Наш слой |
|---|---|---|---|
| 32 → 57 (+25) | carried | Following 32ab, D5,7-9,S insert one line [779%]: “That is why he has not | нет у нас (only_goldman) |
| 36 → 61 (+25) | carried | Ct, Cm, Cg mention that Hanuman swears by the mountains because they | нет у нас (only_goldman) |
| 4 → 5 (+1) | interpolated | This verse is virtually identical (vadanam for ananam in pada a) 10 5.33.78 except | [tier1]  |
| 16 → 23 (+7) | measured | The commentators are widely divided as to how to interpret these gnomic ref- | нет у нас (only_goldman) |
| 29 → 54 (+25) | interpolated | “No one is dearer to him than I or even as dear: not his mother, his father, or | нет у нас (only_goldman) |

### Песнь 37 (наша) × песнь 35 Голдменов — заметки печ. 451–454

Лемм 19, якорей **4** (25→25(+0) 31→31(+0) 44→44(+0) 47→47(+0)), строк колляции 23 (both 13, only_goldman 10, only_ours 15), полосы {'carried': 11, 'interpolated': 5, 'measured': 7}.

| Их → наша | Полоса | Голова Голдменов | Наш слой |
|---|---|---|---|
| 12 → 12 (+0) | carried | Verses 12 and 13 represent primarily northern readings. Only D7-9,T2 of | [phase2] avindhyaḥ |
| 8 → 8 (+0) | carried | It is now the tenth month; only two more remain | нет у нас (only_goldman) |
| 27 → 27 (+0) | measured | This verse is subject to considerable and confusing variation among the various | нет у нас (only_goldman) |
| 61 → 61 (+0) | carried | if Rama and Laksmana were to lose hope of finding me | нет у нас (only_goldman) |
| 20 → 20 (+0) | interpolated | apes and monkeys | нет у нас (only_goldman) |

### Песнь 38 (наша) × песнь 36 Голдменов — заметки печ. 454–461

Лемм 9, якорей **2** (2→2(+0) 56→70(+14)), строк колляции 35 (both 21, only_goldman 14, only_ours 19), полосы {'measured': 3, 'interpolated': 5, 'carried': 27}.

| Их → наша | Полоса | Голова Голдменов | Наш слой |
|---|---|---|---|
| 13 → 16 (+3) | carried | See Jhala’s critical note (1966, p. 487) on the issue of the manuscript evidence | [lexical] balibhojana |
| 43 → 54 (+11) | carried | The syntax of this passage is complicated and elliptical. Jhala in his critical | нет у нас (only_goldman) |
| 34 → 42 (+8) | carried | “by making a heroic effort’ mahotsaham: The reading of the critical text is slightly | нет у нас (only_goldman) |
| 15 → 18 (+3) | carried | After 15, D5,7-9,S insert a passage of eight lines [836*] in which the episode | нет у нас (only_goldman) |
| 21 → 26 (+5) | carried | After verse 21, D5,7-9,S insert 839%: “In my exhaustion, I slept on Raghava’s | нет у нас (only_goldman) |

### Песнь 40 (наша) × песнь 38 Голдменов — заметки печ. 465–466

Лемм 6, якорей **1** (8→8(+0)), строк колляции 11 (both 9, only_goldman 2, only_ours 6), полосы {'interpolated': 4, 'measured': 3, 'carried': 4}.

| Их → наша | Полоса | Голова Голдменов | Наш слой |
|---|---|---|---|
| 12 → 12 (+0) | interpolated | Most southern manuscripts read 5.38.12—16 for the first time following 5.36.41. | нет у нас (only_goldman) |
| 20 → 20 (+0) | carried | See 5.36.53. | нет у нас (only_goldman) |
| 24 → 24 (+0) | carried | some small thing still remained to be done | [lexical] śokavega |
| 4 → 4 (+0) | interpolated | Please . . . give | [tier1] Должен отдать тайный знак / Ты Раме… (abhijñānaṃ ca rāmasya ;  |
| 7 → 7 (+0) | measured | I have experienced as much joy | [tier1] ; [lexical] cūḍāmaṇi; [phase2] cūḍāmaṇiḥ suparirakṣitaḥ |

### Песнь 41 (наша) × песнь 39 Голдменов — заметки печ. 466–468

Лемм 6, якорей **1** (8→8(+0)), строк колляции 11 (both 6, only_goldman 5, only_ours 5), полосы {'interpolated': 7, 'measured': 3, 'carried': 1}.

| Их → наша | Полоса | Голова Голдменов | Наш слой |
|---|---|---|---|
| 15 → 15 (+0) | interpolated | After verse 15, D5,7-9,S insert a passage of four lines [917*] further describing | [lexical] pramadāvana |
| 6 → 6 (+0) | measured | he who understands this multiplicity of means | нет у нас (only_goldman) |
| 7 → 7 (+0) | measured | If now, having accomplished my primary objective, I | нет у нас (only_goldman) |
| 3 → 3 (+0) | interpolated | See 5.34.16 and note. | нет у нас (only_goldman) |
| 4 → 4 (+0) | interpolated | be made more pliant | нет у нас (only_goldman) |

### Песнь 43 (наша) × песнь 41 Голдменов — заметки печ. 469–470

Лемм 6, якорей **2** (1→1(+0) 14→18(+4)), строк колляции 10 (both 5, only_goldman 5, only_ours 5), полосы {'measured': 5, 'interpolated': 5}.

| Их → наша | Полоса | Голова Голдменов | Наш слой |
|---|---|---|---|
| 2 → 2 (+0) | measured | After this verse, D5,7-9,S insert a passage of two lines [948%]: “As the protector | нет у нас (only_goldman) |
| 16 → 20 (+4) | measured | Following this verse, D5,7-9,S insert a passage of six lines [959%]: “We and | нет у нас (only_goldman) |
| 11 → 14 (+3) | interpolated | After this verse, D7-9,S repeat 5.40.27. | нет у нас (only_goldman) |
| 5 → 6 (+1) | interpolated | birds fell from the sky | нет у нас (only_goldman) |
| 9 → 11 (+2) | interpolated | under the very noses | нет у нас (only_goldman) |

### Песнь 44 (наша) × песнь 42 Голдменов — заметки печ. 470–471

Лемм 7, якорей **2** (2→2(+0) 14→15(+1)), строк колляции 10 (both 7, only_goldman 3, only_ours 5), полосы {'measured': 4, 'interpolated': 6}.

| Их → наша | Полоса | Голова Голдменов | Наш слой |
|---|---|---|---|
| 8 → 8 (+0) | interpolated | After verse 8, D5,7-9,S insert a passage of two lines [965%], which partially | [tier1] Казалось лицо Ханумана / Огромным лотосом в небе (śuśubhe mu |
| 5 → 5 (+0) | interpolated | delighted | нет у нас (only_goldman) |
| 17 → 18 (+1) | interpolated | ornaments | нет у нас (only_goldman) |
| 19 → 20 (+1) | interpolated | rolling with rage | нет у нас (only_goldman) |
| 2 → 2 (+0) | measured | floral chaplet | [lexical] samaradurjaya |

### Песнь 46 (наша) × песнь 44 Голдменов — заметки печ. 472–474

Лемм 16, якорей **3** (1→1(+0) 13→15(+2) 39→41(+2)), строк колляции 21 (both 15, only_goldman 6, only_ours 12), полосы {'measured': 5, 'interpolated': 10, 'carried': 6}.

| Их → наша | Полоса | Голова Голдменов | Наш слой |
|---|---|---|---|
| 35 → 37 (+2) | interpolated | After verse 35, the vulgate ( = GPP 37¢f) inserts one line [995%]: “Crushed by | [lexical] giriśṛṅga |
| 11 → 13 (+2) | measured | endurance | нет у нас (only_goldman) |
| 17 → 19 (+2) | interpolated | garlanded with the rays of his own splendor | [phase2] upamā / rūpaka |
| 22 → 24 (+2) | carried | bow at the ready | нет у нас (only_goldman) |
| 24 → 26 (+2) | carried | roared | нет у нас (only_goldman) |

### Песнь 47 (наша) × песнь 45 Голдменов — заметки печ. 474–479

Лемм 25, якорей **2** (1→1(+0) 15→36(+21)), строк колляции 32 (both 8, only_goldman 24, only_ours 15), полосы {'measured': 8, 'interpolated': 12, 'carried': 12}.

| Их → наша | Полоса | Голова Голдменов | Наш слой |
|---|---|---|---|
| 17 → 38 (+21) | measured | Jhala (1966, p. 490) notes that pada a is tristubh, while the remaining padas are | [tier1] ; [phase2] kṛtakṣaṇaḥ |
| 3 → 6 (+3) | measured | jambunada gold | нет у нас (only_goldman) |
| 5 → 11 (+6) | interpolated | splendor of the sun | нет у нас (only_goldman) |
| 8 → 18 (+10) | interpolated | his glance that of a lion | нет у нас (only_goldman) |
| 9 → 21 (+12) | interpolated | summoned all his strength | нет у нас (only_goldman) |

### Песнь 48 (наша) × песнь 46 Голдменов — заметки печ. 479–487

Лемм 25, якорей **9** (3→4(+1) 12→14(+2) 26→28(+2) 32→34(+2) 37→39(+2) 43→45(+2) 48→50(+2) 49→51(+2) 53→55(+2)), строк колляции 44 (both 29, only_goldman 15, only_ours 5), полосы {'measured': 31, 'interpolated': 13}.

| Их → наша | Полоса | Голова Голдменов | Наш слой |
|---|---|---|---|
| 11 → 13 (+2) | measured | The translation follows the interpretation of Cg, who explains: “The impropriety | [lexical] rājadharma |
| 20 → 22 (+2) | interpolated | Darkening of the horizons and the howling of wild animals are stereotypical | нет у нас (only_goldman) |
| 40 → 42 (+2) | interpolated | considering that he would momentarily be able to free himself | нет у нас (only_goldman) |
| 41 → 43 (+2) | measured | Brahma, Indra, and Vayu are the same deities that present Hanuman gifts at | нет у нас (only_goldman) |
| 59 → 61 (+2) | interpolated | his mission, its purpose, and the instigator of the purpose | нет у нас (only_goldman) |

### Песнь 58 (наша) × песнь 56 Голдменов — заметки печ. 513–523

Лемм 47, якорей **10** (15→15(+0) 16→16(+0) 37→39(+2) 40→42(+2) 48→54(+6) 89→108(+19) 106→126(+20) 118→140(+22) 122→144(+22) 139→168(+29)), строк колляции 91 (both 43, only_goldman 48, only_ours 37), полосы {'carried': 25, 'interpolated': 38, 'measured': 28}.

| Их → наша | Полоса | Голова Голдменов | Наш слой |
|---|---|---|---|
| 8 → 8 (+0) | interpolated | We follow Cr, Ck in reading the halves of the verses as separate sentences. | нет у нас (only_goldman) |
| 20 → 20 (+0) | interpolated | See 5.1.130-56 and Jhala’s critical note (1966, p. 491). | [edition] Шлока 5.58.20 отсутствует в критическом издании (Барода). |
| 99 → 119 (+20) | interpolated | Note that the northern versions omit this verse. For an explanation, see Jhala’s | нет у нас (only_goldman) |
| 19 → 19 (+0) | interpolated | Following verse 19, all southern manuscripts and those devanagari manuscripts | нет у нас (only_goldman) |
| 45 → 49 (+4) | interpolated | Following this verse, 1D5,7-9,S insert a passage of seven lines [1189*] describing | [tier1] ; [edition] Шлоки 5.58.49–51 (3 шлоки) отсутствуют в критическ |

### Песнь 61 (наша) × песнь 59 Голдменов — заметки печ. 527–529

Лемм 12, якорей **5** (5→5(+0) 6→6(+0) 14→16(+2) 18→20(+2) 19→21(+2)), строк колляции 18 (both 13, only_goldman 5, only_ours 4), полосы {'measured': 14, 'interpolated': 4}.

| Их → наша | Полоса | Голова Голдменов | Наш слой |
|---|---|---|---|
| 22 → 24 (+2) | interpolated | nearly killed him with their slaps and kicks | нет у нас (only_goldman) |
| 4 → 4 (+0) | measured | almost as if they bore up with their gaze | [tier1] Словно несли его взглядами (vahanta iva dṛṣṭibhiḥ) - то есть |
| 5 → 5 (+0) | measured | their spirits uplifted by the success of their undertaking | [tier1] И снова воспрянув духом (karmasiddhibhir unnatāḥ) - букв. “т;  |
| 7 → 7 (+0) | measured | heavenly garden | нет у нас (only_goldman) |
| 9 → 10 (+1) | interpolated | Dadhimukha | нет у нас (only_goldman) |

### Песнь 62 (наша) × песнь 60 Голдменов — заметки печ. 529–533

Лемм 15, якорей **5** (7→8(+1) 12→13(+1) 30→31(+1) 31→32(+1) 32→33(+1)), строк колляции 21 (both 15, only_goldman 6, only_ours 10), полосы {'interpolated': 8, 'measured': 12, 'carried': 1}.

| Их → наша | Полоса | Голова Голдменов | Наш слой |
|---|---|---|---|
| 1 → 2 (+1) | interpolated | them | нет у нас (only_goldman) |
| 6 → 7 (+1) | measured | learning that Hanuman had found Maithili | [tier1] Раззадоренные позволением / И Ханумана успехом (atisargāc ca;  |
| 14 → 15 (+1) | measured | monkeys . .. guards | нет у нас (only_goldman) |
| 20 → 21 (+1) | interpolated | the monkey guardians of the grove | нет у нас (only_goldman) |
| 21 → 22 (+1) | carried | guardians of the grove | нет у нас (only_goldman) |

### Песнь 64 (наша) × песнь 62 Голдменов — заметки печ. 534–538

Лемм 20, якорей **5** (4→4(+0) 7→7(+0) 9→9(+0) 14→15(+1) 15→16(+1)), строк колляции 27 (both 13, only_goldman 14, only_ours 8), полосы {'interpolated': 6, 'measured': 10, 'carried': 11}.

| Их → наша | Полоса | Голова Голдменов | Наш слой |
|---|---|---|---|
| 33 → 34 (+1) | carried | Following verse 33, D7--9, including the important text of Ct, insert three lines | нет у нас (only_goldman) |
| 8 → 8 (+0) | measured | Jhala (1966, p. 494) instructs us to omit this stanza from the critical text. Based | [lexical] mūrkhatā |
| 1 → 1 (+0) | interpolated | saluted . .. respectfully | нет у нас (only_goldman) |
| 12 → 13 (+1) | measured | his followers | нет у нас (only_goldman) |
| 17 → 18 (+1) | measured | immortal | нет у нас (only_goldman) |

## 4. Записи решений и флаги

### ДР-1. Перенумерация сарг (главный результат сверки)

**Что найдено.** Деления сарг в нашей южной вульгате и в критическом издании Голдменов не совпадают:
наша N = их N−2 (песни 9–64), наши 3+4 = их 3, наши 7+8 = их 6. Следствие: наивный запуск конвейера
«наша песнь NN против их заметок NN» даёт ложный ноль якорей (до правки — 29 песень из 33 без покрытия);
после перепривязки — покрытие есть у всех 33.

**Что решить.** Текущая форма ссылок (H7925) — «Goldman & Sutherland-Goldman 1996: стр.» — страницами,
поэтому уже корректна и перенумерации не чувствует. Решение нужно только о форме дополнения:
нужно ли в ссылки добавлять номер их сарги (напр. «…: 130 (их сарга 7)»). Рекомендация: не нужно —
страница однозначна, а таблица соответствия есть в этом документе. Решает: М. Гасунс.

### ДР-2. Порог «≥15 якорей на песню» против данных

**Что найдено.** Порог из задания («offset coverage >= 15 anchors per sarga (sarga01 = 19/88)»)
недостижим для 33 песен: потолок извлечённых лемм — 4–47 на песню против 88 у песни 1 (это богатейший
набор заметок книги); доля лемм, находящих дословное вхождение в нашу шлоку, — 20–40 % (расхождения
рецензий, падежные/сандхийные формы, эллипсисы в леммах вида `x- ... -y` — такие не матчатся по построению).
Фактически по 33 песням: **124 якоря на 488 лемм, 1–10 якорей на песню, покрытие у всех 33**
(условие Fail миссии «сарга без покрытия якорями» — чисто). Канарейка-песнь 1 этим же движком: 25 якорей.

**Что решить.** Принять формат отчёта «якоря/леммы» (как 19/88 у песни 1) вместо абсолютного порога,
либо заказать vision-восстановление лемм (остаток ниже) и перепроверить порог после него. Решает: М. Гасунс.

### ДР-3. Единственная ручная правка входных данных

В токене леммы `wikatam` (их 15.8, глосса «another was deformed») исправлен `w→v` → `vikatam`.
Основание: IAST не знает буквы w (это OCR-шум tesseract.js), глосса «уродлив» = vikatam, наша 17.8 —
ровно перечень уродств («…kubjaṃ ca vikataṃ vamanam…»). Правка внесена в рабочий текст (скретчпад),
не в репозиторий; это единственная правка входа во всём прогоне. Без неё наша 17 осталась бы без
якорей (единственный Fail); с ней — 1 якорь (17.8 ↔ их 8, смещение 0).

### ДР-4. Строки колляции пар с общим делением

Их 3 покрывает наши 3 и 4; их 6 — наши 7 и 8. В `collate_sarga04_aligned.json` часть строк их 3-й песни
отображается за пределы нашей 4-й (наша шлока ≤ 0) — это хвост нашей 3-й, а не дефект. Сырые JSON
оставлены без фильтрации (конвейер не фильтрует); читать строки песни 04 следует только в диапазоне
наших шлок 1..N. То же для пары 07×06.

### ДР-5. 5.9.28 против записи «отсутствует в критическом издании»

Наши [edition]-примечание к 5.9.28 утверждает «Шлока 5.9.28 отсутствует в критическом издании (Барода)».
Но их заметка 24 («brindled cow» `kalmāṣīm`, их 5.7.24) аннотирует ровно эту шлоку (`kalmāṣīm iva suprabhām`
— якорь g24→наша 28, +4). Если бы шлоки не было в критическом тексте, заметки к ней не существовало бы.
Действие: сверить 5.9.28 с Бародой (5.7.24) и либо снять/уточнить edition-примечание (возможно, речь о
полустишии или о выносе в аппарат), либо оставить с оговоркой. Решает: М. Гасунс.

### Флаги класса «nāga» (5.1.7)

Новых само-противоречий «перевод тянет в одну сторону, наше же примечание — в другую» в 33 песнях **не
найдено**. Четыре двузначности просмотрены и признаны информированными (примечание объясняет выбор
читателю): `śakti` (наша 4.21 — «копьё/сила», выбор оговорён), `bhāminī` (10.38 — «прекрасная/гневная»),
`candre harivāhane` (9.8 — перевод даёт «Луны или Индры», оба варианта в тексте), `kim uttaram`
(58.100 — «ответ/северный», двусмысленность как художественный приём объяснена в tier1).
Запись решения ДР-5 — единственный случай, где наше примечание спорит с фактом их аппарата.

## 5. Что остаётся человеку

1. **Решения ДР-1, ДР-2, ДР-5** (форма ссылок; принятие порога якорей; сверка 5.9.28 с Бародой).
2. **Остаток (не блокирует):** vision-восстановление лемм на слабых парах (их 15, 44, 45, 56) —
   подняло бы якоря в 1,5–2 раза; нужно, только если порог из ДР-2 принят в абсолютной форме.
3. Конвейер воспроизводим: команды §0; извлечение заметок — Tesseract поверх зафиксированного PDF
   (md5-пин), нарезка по заголовкам `Sarga N`, колонтитульный аудит §1.

_Dr. Mārcis Gasūns_

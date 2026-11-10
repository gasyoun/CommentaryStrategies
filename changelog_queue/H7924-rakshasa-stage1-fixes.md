_Created: 10-11-2026 · Last updated: 10-11-2026_

# H7924 — Stage 1 rakshasa print-blocking fixes (PR #280)

### Fixed

- **[articles/intro_article_lp5_draft.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/articles/intro_article_lp5_draft.md)** —
  дефект A-B: «почти все» → «почти половина» (31 из 65 в блоке стражей
  22–27); подпись и тело Table 2 state 79 mixed (31 f + 48 m/n); RV-проза
  точная: 94/90 (было ~95/~90). Princeton freeze: Pollock 1991 Vol III
  (ed. Goldman) [^11] + лит. 2; JAOS «Women at the Margins» 138.1:45–72
  [^12a] + лит. 5; Thompson & Payne, Monstrous Feminine, pp. 247–274 [^24]
  + лит. 6; осиротевшие сноски 3/4/6/7 занесены как [^22][^23][^24][^25].
  DH10: оговорка о метрике в S6 + substring-denominator caveats в
  микросекции.
- **[data/analysis/rakshasa_census_vulgate_2026-11-01.py](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/analysis/rakshasa_census_vulgate_2026-11-01.py)** —
  DH1: экспорт `sundara_tokens_by_sarga` (68) + `sundara_blocks`;
  DH2: пин DCS через `git rev-parse` (HEAD 450412c4), замороженный
  04e0778 отмечен.

### Added

- **[articles/intro_article_lp5_draft.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/articles/intro_article_lp5_draft.md)** —
  микросекция о гендере (без номера, после 1.4.2): split-таблица и карта
  65 (31/9/5/4/16), тезис 19.9% против 2.7%, движок Sutherland-Goldman
  [^12a][^24]; DH4: точные 0.888/0.964/0.945 в S6 (+оговорка); DH5:
  дословная атрибуция Gita Supersite в [^14]; DH7: ~67% paraphrase pilot
  rate в S6; DH9: containment (frozen RV preserved, unverified chunks
  unprinted).
- **[articles/intro_article_lp5_draft.meta.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/articles/intro_article_lp5_draft.meta.md)** —
  DH6: числовой журнал — каждое печатное число → источник (ключи
  `data/analysis/rakshasa_census_vulgate_2026-11-01.json`).
- **[data/analysis/README.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/analysis/README.md)** —
  DH3: README аналитического слоя.

### Verified

- Перепрогон (attempt 1): Table 2 == `sundara_blocks`, суммы 326/65/68.
- PR [#280](https://github.com/gasyoun/CommentaryStrategies/pull/280)
  merged 09-11-2026 (46d6bc9); строка кормит следующий `/cut-release`
  (residual закрытого H7924, GTD Y8I).

_к.ф.н. М.Ю. Гасунс_

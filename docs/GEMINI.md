# GEMINI.md — Agent Context for CommentaryStrategies

> This file is the **cold-start briefing** for any AI agent (Gemini, Claude, Codex)
> working on the CommentaryStrategies repository. Read this first.

---

## What this project is

A comparative study of **commentary strategies** used by Russian translators of Sanskrit classical texts. The core corpus contains **17 863+ scholarly annotations** across 6 translators working on the Mahābhārata, Rāmāyaṇa, and Upaniṣads.

**Repository:** <https://github.com/gasyoun/CommentaryStrategies>
**Parallel corpus:** <https://samskrtam.ru/parallel-corpus/>
**Conference target:** XXIX Tronsky Readings (ILI RAN, St. Petersburg, 2025)

---

## Quick orientation

| File | What it is | Read when |
|------|-----------|-----------|
| `docs/ROADMAP.md` | Phased project plan with task lists | Planning work |
| `docs/ARCHITECTURE.md` | Structure review + target architecture | Making structural changes |
| `tronsky-XXX/1_README.md` | **Deep meta-instruction** (33 KB) for the article | Working on the Tronsky article |
| `.ai_state.md` | Session state journal | Every session start |
| `README.md` | Universal prompt template for LLM analysis | Understanding the analytical method |
| `index.html` | Main comparative report (5 translators) | Understanding existing output |

---

## The 6 translators

| Translator | Text | Notes | Avg. length | IAST % |
|-----------|------|-------|-------------|--------|
| **Кальянов** (Kalyanov) | Mahābhārata I,II,IV,V,VII,IX | 7 424 | 160 chars | 66% |
| **Васильков** (Vasilkov) | Mahābhārata III,VIII,X–XVIII | 5 574 | 260 chars | 23% |
| **Эрман** (Erman) | Mahābhārata VI (Bhīṣmaparva) | 758 | 264 chars | 50% |
| **Гринцер** (Grintser) | Rāmāyaṇa I–III | 2 245 | 254 chars | ~45% |
| **Сыркин** (Syrkin) | 20 Upaniṣads | 1 621 | 316 chars | 64% |
| **Леонов** (Leonov) | Rāmāyaṇa V (Sundarakāṇḍa) | ~1 040 | ~310 chars | ~72% |

---

## The 4-axis analytical framework

Every annotation is classified along 4 axes:

### Axis 1 — Topic (8 empirical categories)
`sanskrit_term` · `myth` · `context` · `realia` · `geography` · `reference` · `textology` · `philosophy`

### Axis 2 — Commentary type (Kazansky 2025)
- **A** — Philological (lexical gloss, etymology)
- **B** — Realia (material/social culture)
- **V** — Historical (context, dating)
- **G** — Cultural-historical (broader interpretation)

### Axis 3 — Structural type of explanation (Lidova 2024)
Based on 5 *lakṣaṇa* from *Parāśara-upapurāṇa*:
- **L1** *pada-ccheda* — word segmentation
- **L2** *padārtha* — word meaning
- **L3** *vigraha* — compound analysis
- **L4** *vākya-yojanā* — sentence construction
- **L5** *ākṣepa-samādhāna* — objection-and-resolution

### Axis 4 — Categorical nature of term (Paribok 2011)
- **П (P)** — *ponyatie* (concept / notion)
- **К (K)** — *kontsept* (culturally loaded concept)
- **Д (D)** — *kodifikator* (direction-of-activity codifier: *dharma*, *karma*, *yoga*, etc.)

---

## Hard rules (NEVER violate)

1. **No «М.: Наука, 2022» for Leonov.** The 2022 volume **does not exist**. Use: «продолжающийся перевод; лит. ред. Е. Костина»
2. **«Парибка»** — the only correct genitive/accusative form. Not «Парибока».
3. **Do not add a 5th axis** without explicit user permission.
4. **Do not cite 5 traditional Rāmāyaṇa commentators** (Tilaka, Bhūṣaṇa, Śiromaṇi, Tattvadīpikā, Amṛta) without scan verification — current attributions are working hypotheses.
5. **Distinguish Princeton Goldman (1994/96) from CSL Goldman (2006).** Princeton = academic critical edition with footnotes. CSL = portable bilingual, no footnotes.
6. **Losev-as-editor ≠ Losev-as-monographer.** Only the editor role is relevant (Platonic eight-volume, 1968–1972).
7. **Do not use Kazansky's name in the article title** — he is the conference chair.

---

## Key theoretical sources

| Source | Year | What it provides |
|--------|------|-----------------|
| **Топоров** — «Текст и комментарий» (ed.) | 2006 | General philological framing of the commentary genre |
| **Парибок** — «Шабдапракаша» article | 2011 | Axis 4: П/К/Д distinction + canonical Д-term list |
| **Лидова** — «Комментарий в Древней Индии» (IMLI) | 2024 | Axis 3: five *lakṣaṇa* from *Parāśara-upapurāṇa* |
| **Казанский** — ИЕЯКФ 29 (DOI: 10.30842/ielcp2306901529049) | 2025 | Axis 2: A/B/V/G typology + 5 cross-cutting parameters |
| **Лелюхин** — «Шабдапракаша» article | 2011 | Parallel case: *adhyakṣa* in Arthaśāstra |
| **Скороходова** — «Шабдапракаша» article | 2011 | Bengali Renaissance as third commentary line |

---

## Central thesis

> Russian translators of Sanskrit texts inherit *two* commentary traditions simultaneously — the Indian (where commentary is a condition of text readability) and the European philological (where commentary is an auxiliary apparatus). The strategies of Russian Sanskritists are different configurations of this *double obligation*.

---

## Current article status

**File:** `tronsky-XXX/10_article_v_tronsky_v15.md` (67 KB)
**Sections:** Abstract + §§1–9 + Bibliography + 2 Appendices
**Word count:** ~12 000+

### Critical tasks before submission
1. Verify all Kazansky citations with page numbers
2. Verify 5 traditional commentator attributions
3. Verify Paribok 2007 thesis (currently cited via Lidova)
4. Remove all «М.: Наука, 2022» from Leonov materials
5. Translate abstract to English
6. Create 3000-word oral presentation version

---

## HTML analytics pages

Each translator has an individual analytics HTML page with:
- Commentary density statistics
- Thematic category distribution (bar charts)
- Stylistic formula patterns
- Example annotations
- IAST usage metrics

Shared design: PT Serif body / PT Sans labels / color-coded per translator.

### Color codes
| Translator | CSS var | Hex |
|-----------|---------|-----|
| Кальянов | `--k` | `#2a5a8b` |
| Васильков | `--v` | `#3a6b35` |
| Эрман | `--e` | `#5a2d82` |
| Гринцер | `--g` | `#8b4513` |
| Сыркин | `--s` | `#7a3b00` |
| Леонов | `--leonov` | `#7c4b2a` |

---

## Working with this project

### Before making any edit
1. Read this file
2. Check `.ai_state.md` for current session state
3. If working on the article → read `tronsky-XXX/1_README.md`

### After every edit
1. Run a verification pass: search for forbidden strings
2. Update `.ai_state.md` with what was done
3. Do not introduce new analytical axes without permission

### Forbidden strings (regex)
```
М\.\s*:\s*Наука,\s*2022    # Leonov volume does not exist
Парибок[аоу]                # Wrong declension
```

---

## Canonical Д-term list (Paribok 2011, p. 86)

*duḥkha*, *brahman*, *ātman*, *dharma*, *karma*, *bodhicitta*, *guru*,
*yoga*, *bhakti*, *mokṣa*, *māyā*, *śūnya*, *nirvāṇa*, *adhikāra*,
*śraddhā*, *jñāna*, *prakṛti*, *puruṣa*, *guṇa*, *avatāra*

Social-political (Lelyukhin 2011): *adhyakṣa*, *rājan*, *gaṇa*,
*saṃgha*, *daṇḍa*, *varṇa*, *jāti*

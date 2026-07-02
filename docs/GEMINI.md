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
| `index.html` | Main comparative report (6 translators) | Understanding existing output |

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

### Axis 1 — Topic (9 empirical categories)
`sanskrit_term` · `myth` · `context` · `realia` · `geography` · `reference` · `textology` · `philosophy` · `poetics`

### Axis 2 — Commentary type (Kazansky 2025)
> Canonical definitions: [`data/commentary_schema.json`](../data/commentary_schema.json) (`axis_2_kazansky`). **Realia belong to V, never B.**
- **A** — Philological / lexical: gloss, derivation, etymology of the Sanskrit form itself (literal sense, morphology, epithet rendering). *Not* realia.
- **B** — Textological (*not* "realia"): metatext on the state of the source or the act of translation — omission in the translation, manuscript/commentator variant, interpolation verdict.
- **V** — Historical-cultural / realia: in-world identification + realia — deity, demon class, sage, king, caste, river, mountain, city, people, weapon, battle formation, plot scene. **Realia go here, never in B.**
- **G** — Cultural / interpretive: abstract concepts (dharma, mokṣa, yuga, puruṣārthas) and interpretive moves — cross-traditional comparisons, symbolic/allegorical readings, concept-development.

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

1. **No «М.: Наука (2022)» for Leonov.** The volume does not exist. Use: «продолжающийся перевод; лит. ред. Е. Костина»
2. **«Парибка»** — the only correct genitive/accusative form. Not «Парибо-ка».
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

**File:** `tronsky-XXX/article_current.md` (75 KB, v16+)
**Sections:** Abstract + §§1–9 + Bibliography + 2 Appendices (III, IV)
**Word count:** ~12 000+

### Completed tasks before submission
1. [x] Verify all Kazansky citations with page numbers
2. [x] Verify 5 traditional commentator attributions
3. [x] Verify Paribok 2007 thesis (now cited directly)
4. [x] Remove all «М.: Наука (2022)» from Leonov materials
5. [x] Translate abstract to English
6. [x] Create 3000-word oral presentation version

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
М\.\s*:\s*Наука,\s*2022    # Leonov volume does not exist (string masked in docs)
Парибок[аоу]                # Wrong declension (string masked in docs)
```

---

## Mapping to agent-roadmap-2026

> Reference: <https://github.com/codejunkie99/agent-roadmap-2026>
>
> That roadmap is a **6-phase, 17-week AI agent engineering curriculum**
> (harness → context → LangGraph → evals → production).
> This project is a *running domain application* — a scholarly corpus that
> drives concrete agent engineering tasks at each phase.

### How the phases map

| agent-roadmap-2026 phase | Harness concept taught | Where it appears in CommentaryStrategies |
|--------------------------|------------------------|------------------------------------------|
| **Phase 0** — Mental models | Workflow vs. agent; context engineering (Write / Select / Compress / Isolate) | `.ai_state.md` + `docs/GEMINI.md` implement the **Write** primitive. This file *is* the system-prompt context for the agent. |
| **Phase 1** — Tool-using agent | 100-line loop; Claude Agent SDK; Skills / hooks | `nilakantha_parser.py` is a tool. A Phase 1 project: wrap it as an `@tool`, add `read_file` / `write_file`, run it against the Mahābhārata HTML. |
| **Phase 2** — LangGraph deep agent | Orchestrator-worker; sub-agent fan-out; PostgresSaver durability | **Micro-markup task** (Phase 2.1 of the roadmap): lead agent reads 50 annotations per translator, fans out to 6 annotation sub-agents (one per translator), each classifies by 4 axes, returns compressed JSON. Lead merges into `data/`. |
| **Phase 3** — Custom harness | Loop + tool dispatch + context compression + sub-agents | `build_docx.py` + `validate.py` are early harness fragments. A Phase 3 deliverable: 1 500-line harness that ingests any HTML analysis page, runs regex validation, spawns sub-agents to verify citations, and writes the corrected Markdown. |
| **Phase 4** — Evals & CI | Golden datasets; trajectory evals; CI gates | **Validation CI** (Architecture issue C3): a `make eval` target that runs `validate.py` (forbidden-string check), graders on Leonov date attribution, and blocks merge if errors appear. The 14-item checklist in article §9 is the golden rubric. |
| **Phase 5** — Production | Cost discipline; sandboxing; drift alerts | Once corpus annotation is automated: prompt-caching the 4-axis system prompt; model routing (Haiku for Axis 1 classification, Opus for Axis 2–4 judgment); nightly drift check on LLM-as-judge scores on the micro-markup dataset. |

### The key insight

The agent-roadmap-2026 says: *same model, different harness, 78% vs 42% on CORE*.

For CommentaryStrategies the equivalent is: *same annotation corpus, different agent harness, manual classification vs. automated 4-axis micro-markup at scale*. The bottleneck is not the model — it is the harness that correctly **selects** (which annotations to classify), **writes** (JSON to `data/`), **isolates** (per-translator sub-agents), and **compresses** (returns only axis labels, not raw text, to the parent).

### Skills this project develops

Following the agent-roadmap-2026 `AGENT.md` protocol, the project profile is:

```
Level:    built simple agents / shipping scholarly ones
Goal:     ship at current job (scholarly publication + corpus platform)
Stack:    Python + Anthropic (Gemini for planning, Claude for harness work)
Hours:    variable — research schedule
```

Adjusted plan per `AGENT.md` rules:
- Phase 0–1: **SPEEDRUN** — existing `nilakantha_parser.py` and HTML pipeline count as Phase 1 evidence
- Phase 2: **NORMAL** — micro-markup task is the canonical Phase 2 project
- Phase 3: **SPEEDRUN** — use Deep Agents middleware; write harness only for `validate.py` + docx builder
- Phase 4: **DEEP** — eval quality is the core bottleneck (architecture issue C3)
- Phase 5: **ONGOING** — cost and drift matter when annotation scales to 300+ translators

### Deliverables mapped to ROADMAP.md phases

| ROADMAP.md phase | agent-roadmap-2026 deliverable produced |
|------------------|-----------------------------------------|
| Phase 1 (article submission) | Phase 0 mental-model doc: write the 2-page doc that explains the 4-axis framework as a context-engineering artifact |
| Phase 2 (micro-markup) | Phase 2 project: research-analyst deep agent classifying 300 annotations; LangSmith trace URL in README |
| Phase 3 (corpus expansion) | Phase 1 rebuild: `nilakantha_parser.py` as a Claude Agent SDK Skill with SKILL.md metadata |
| Phase 4 (CLR integration) | Phase 4 eval: CI gate blocking merge if axis classification drift > 3 points |
| Phase 5 (publication platform) | Phase 5 hardening: prompt caching, model routing, sandbox for code execution |

---

## Canonical Д-term list (Paribok 2011, p. 86)

*duḥkha*, *brahman*, *ātman*, *dharma*, *karma*, *bodhicitta*, *guru*,
*yoga*, *bhakti*, *mokṣa*, *māyā*, *śūnya*, *nirvāṇa*, *adhikāra*,
*śraddhā*, *jñāna*, *prakṛti*, *puruṣa*, *guṇa*, *avatāra*

Social-political (Lelyukhin 2011): *adhyakṣa*, *rājan*, *gaṇa*,
*saṃgha*, *daṇḍa*, *varṇa*, *jāti*

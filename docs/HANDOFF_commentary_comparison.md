# Handoff — Compare Sundarakāṇḍa commentaries (generated + Leonov-real) vs the 5 analyzed translators

> **For:** a new **Opus** chat in `GitHub/CommentaryStrategies`.
> **Goal:** extend `index.html`'s 5-way summary matrix into a 7-way comparison that places the
> **Sundarakāṇḍa** commentary — in **two forms** (our corpus-**generated** 788-note apparatus *and*
> Leonov's **real** published profile) — against the five already-analyzed translators, answering
> **both** "how does it compare in quality & quantity" **and** "did the generated apparatus reach
> human quality?" (method-validation).
> Per the user's standing rule: **report the model tier (Opus/Sonnet/Haiku) at every step.**

---

## 1. Decisions already made (don't re-ask)

| Decision | Answer |
|---|---|
| Subject | **Both** — the generated 788-note apparatus AND Leonov's real ~1040-note commentary |
| Compare against | The **5 in `index.html`**: Kalyanov · Vassilkov · Erman · Grintser · Syrkin |
| Deliverable | **Extend the existing `index.html` summary matrix** (add Leonov-real + Sundara-generated columns + quality/quantity rows) — do NOT build a new page |
| Angle | **Quality + method-validation** (scholarly profile *and* "is the generated apparatus as good as the human ones?") |

---

## 2. Check prior art FIRST — the comparison is ~70% already computed

Read these before computing anything (most numbers exist):

- **[index.html](../index.html)** — the **5-way summary matrix** + per-translator badge stats (notes, mean length, IAST%, density, leading category, target reader, stylistic formulas). This is the table you EXTEND.
- **[leonov_kostina_commentary_analysis.html](../leonov_kostina_commentary_analysis.html)** §10 "Параметры для сводного документа" — **already has a Leonov-real + Kostina comparison row** against Kalyanov/Vassilkov/Grintser. Lift Leonov's real numbers from here (they are marked `≈`, awaiting a final machine count — flag that).
- **[data/*_markup_50.json](../data/)** — the 4-axis **gold samples** (6×50 notes) for the human translators; `scripts/profile_translator.py` computes axis profiles from them.
- **[data/sundara_commentary_to_add.json](../data/sundara_commentary_to_add.json)** — the **generated 788-note apparatus** (the new subject). **[data/sundara_book_stats.json](../data/sundara_book_stats.json)** — its aggregate stats.
- **[SUNDARA_COMMENTARY_RATIONALE.md](../SUNDARA_COMMENTARY_RATIONALE.md)** — how the 788 were built (3 regimes + Г), the adversarial gate, the dedup. Essential for the method-validation angle.
- **[CLAUDE.md](../CLAUDE.md)** §"4-axis annotation framework" — Kazansky A/B/V/G ↔ the Cyrillic А/Б/В/Г used in the Sundara `type` field. **Note the mapping subtlety**: the gold-sample `axis_2_kazansky` uses A/B/V/G (V = hist-cultural+realia, G = cultural); the Sundara apparatus `type` uses the report's А/Б/В/Г (А philol, Б textol, В realia, Г hist-cultural). Reconcile carefully when comparing.

---

## 3. The hard numbers (already computed — embed these)

| Параметр | Кальянов | Васильков | Эрман | Гринцер | Сыркин | **Леонов (реальный)** | **Сундара (генерир.)** |
|---|---|---|---|---|---|---|---|
| Примечаний | 7 424 | 5 574 | 758 | 2 245 | 1 621 | **≈1 040** | **788** |
| Текст | МБх 1,2,4,5,7,9 | МБх 3,8,10–18 | МБх 6 | Рам I–III | 20 упаниш. | Рам V (Сундара) | Рам V (Сундара) |
| Плотность | 56,4 % | ~47 % | 37,9 % | 24,6 % | перем. | **≈36 %** | **24,2 %** (692/2859) |
| Ср. длина (зн.) | 160 | 260 | 264 | 254 | 316 | **≈310** | **521** (медиана 550) |
| С IAST | 66 % | 23 % | 50 % | ~45 % | 64 % | **≈72 %** | **100 %** |
| Ведущая категория | термин 52 % | контекст 26 % | термин 40 % | лексика 34 % | текстол. 34 % | **диалог комм. 38 %** | **лексика/А 78 %** |
| Ведущий тип Казанского | A филол. | V ист.-культ. | A филол. | A филол. | B текстол. | **B текстол.** | **A филол.** |
| Целевой читатель | широкий+спец. | гуманитарий | индолог | образ. гуманит. | спец./философ | индолог | *(кандидатный слой)* |

**Generated apparatus internal profile** (from `sundara_commentary_to_add.json`):
- By Kazansky type: **А 617 (78 %) · В 122 (15 %) · Б 38 (5 %) · Г 11 (1 %)**.
- By layer (`subtype`): base 95 · lexical 611 · cross_text 71 · hist_cultural 11.
- Top triggers: realia 206 · etymology 190 · gloss 138 · compound 119 · crosstext 61.
- Grintser cross-refs: 45. All notes `review_required: true`.

---

## 4. The analytical thesis to test & write up

The headline (verify, sharpen, don't just restate):

1. **Quantity / density: the generated apparatus reaches the human Rāmāyaṇa benchmark.** 24.2 % ≈ Grintser's 24.6 % — but well below the dense MBh commentators (Kalyanov 56 %, Vassilkov 47 %). Density-normalize so big-corpus translators don't win on raw count alone.
2. **Quality profile is *inverted* from Leonov's own.** The generated apparatus is **А-led (78 % philological/lexical)**; Leonov's *real* commentary is **Б-led (38 % commentator-dialogue, текстологический)** — his signature. The generated layer is a strong **lexical backbone** that is **missing exactly the Б layer that defines Leonov** (the 5-commentator dialogue) — which is **Phase 2**, gated on OCR of the commentaries.
3. **Two generation artifacts to name honestly:** (a) **100 % IAST** vs human ≤72 % — every generated note is lemma-keyed; (b) **521-char mean** ≫ every human (≤316) — candidate notes over-explain; an editor would trim. So "generated" ≠ "publishable as-is."
4. **Method-validation verdict (the deliverable's punchline):** the corpus method produces *human-comparable density and an unusually complete lexical/etymological + realia + historico-cultural apparatus*, but a *distinct, machine-flavored profile* (verbose, exhaustively transliterated, philology-heavy) and *cannot yet supply the textological dialogue* that is the human commentator's scholarly core. Quantity: yes. Quality: a strong scaffold, not a substitute — pending Phase 2.

---

## 5. Deliverable spec

Edit **`index.html`** (it is hand-authored, NOT generated — safe to edit directly; the CI corpus job leaves root `*_commentary_analysis.html` / `index.html` alone, but run `python scripts/validate.py` after — it checks forbidden strings + that every `.html` keeps `css/commentary.css` + breadcrumb + `<main class="container">`).

1. **Extend the summary matrix** (the `.summary-matrix` / `.compare-table` near the bottom of `index.html`) to **7 columns** — add **Леонов (реальный)** and **Сундара (генерир.)**. Reuse the existing CSS classes/colors; pick two new accent colors consistent with the palette (Leonov already has a `--leo`/leonov color in the css; use a distinct shade for the generated column).
2. **Add quality/quantity rows** if missing: density (normalized), mean length, IAST%, leading Kazansky type, and a **"генерир. vs реальный"** delta row or note.
3. **Add a short "Method validation" prose block** stating thesis §4 (esp. points 2–4): density reached, profile inverted, Б layer absent, generated ≠ publishable.
4. Update the header note (`17 863+ примечаний · 7 переводчиков`) if you add Sundara as an 8th/9th column — keep the count honest (the generated 788 are *candidates*, not part of the analyzed human corpus; label them as such so they're not conflated).
5. **Forbidden-string rule (hard, CLAUDE.md rule #1):** never cite Leonov with the fabricated «Наука 2022» imprint (that volume does not exist) — use "продолжающийся перевод; лит. ред. Е. Костина". `validate.py` enforces this.

---

## 6. Caveats to surface in the writeup (don't bury)

- **Apples vs oranges, stated openly:** the 788 are **machine-generated, `review_required` candidates** for a parallel-reader; the five others are **published human commentaries**. The comparison is legitimate *only* if this is foregrounded — it measures whether the corpus method approximates human output, not a like-for-like scholarly contest.
- **Leonov-real numbers are `≈`** (from `leonov_kostina_commentary_analysis.html`, "требуют финального машинного подсчёта"). If you can get Leonov's real note file (`ramayana-leonov/` HTML / `sources/leonov_notes.json`), compute exact figures; otherwise keep the `≈` and say so.
- **Gold samples are 50-note samples**, not full corpora — the human per-translator type profiles in `*_markup_50.json` are samples; `index.html`'s totals (7424 etc.) are full-corpus counts. Don't mix the two scales silently.
- **Kazansky axis mapping** A/B/V/G (gold) vs А/Б/В/Г (Sundara) — reconcile before cross-tabulating (see §2 / CLAUDE.md).

---

## 7. Suggested first moves for the new chat

1. (Opus) Read §2 sources; lift the human numbers from `index.html` + the Leonov row from `leonov_kostina` §10.
2. (Opus or a Sonnet sub-agent) Recompute/confirm the generated metrics from `sundara_commentary_to_add.json` (density, length, IAST%, type profile) — §3 already has them; verify.
3. (Opus) Write the matrix extension + method-validation block into `index.html`; `python scripts/validate.py`; commit on a branch → PR (repo uses PRs + a parallel automation on `main`; verify end-state on `origin/main`, don't trust a single push).
4. Update `changelog.md` (SemVer — next is likely **v1.3.0** or a PATCH), `.ai_state.md`, and the `Uprava/GTD_NEXT_ACTIONS.md` hub.

**Current repo state (2026-06-29):** apparatus = 788 notes, all 4 Kazansky levels, on `main`; releases v1.0.0/v1.1.0/v1.2.0 cut; report `leonov_sundara_corpus_enriched.html` refreshed to 788; `validate.py` green. Phase 2 (Б commentator-dialogue, gated on Gemini-OCR of the 5 commentaries) deferred.

# EVAL_RESULTS — axis_2 / axis_4 inter-annotator agreement (H1469)

_Created: 24-07-2026 · Last updated: 24-07-2026_

**Status:** complete. Cohen's κ measured on the full 300-note gold sample
(6 translators × 50). Gate closed as an **honest reliability report**, not by
tuning toward the roadmap target.

| Field | Value |
|---|---|
| Handoff | [H1469](https://github.com/gasyoun/Uprava/blob/main/handoffs/archive/H1469-Opus_CommentaryStrategies_commentarystrategies-axis2-axis4-blind-annotator-kappa_22.07.26.md) |
| Pre-registration | [data/iaa/PRE_REGISTRATION_H1469.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/iaa/PRE_REGISTRATION_H1469.md) (committed **before** the five missing Pass-B runs) |
| Codebook | [prompts/classify_note.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/prompts/classify_note.md), human sheet [sources/B5_ANNOTATION_GUIDE.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/sources/B5_ANNOTATION_GUIDE.md) |
| Pass A | Human gold `data/{translator}_markup_50.json` |
| Pass B | Blind LLM — **DeepSeek Chat** (`deepseek-chat`) via OpenAI-compatible API; `scripts/annotate_batch.py` reading label-free `sources/{translator}_notes.json` |
| Scoring | `scripts/compute_iaa_kappa.py` (stdlib Cohen's κ + 2 000-bootstrap CI, seed **20260724**) |
| Machine artifacts | [data/iaa/iaa_kappa_stats.json](iaa/iaa_kappa_stats.json), [disagreement_adjudication.json](iaa/disagreement_adjudication.json) |

**Scope reading (H1469 watch-out #1):** B5 roadmap text says «50 примечаний × 2 оси»;
SUBMISSION_READINESS_A19 says 50-per-translator. The **full 300-note set** is on
disk and is the analysis frame. Per-translator rows are also reported.

**Backend note (H1469 watch-out #2):** no Anthropic key on the host. Pass B is
DeepSeek (non-Anthropic family), not Opus as in H453. Independence is stronger
than a same-family double pass; quality is reported, not assumed.

**Limitation (protocol §3):** this is **human × LLM** agreement (Pass A human,
Pass B model). It measures codebook executability and gold stability under a
blind second coder, **not** human–human IRR. Report it as such in the manuscript.

---

## Headline numbers (pooled n = 300)

| Axis | Cohen's κ | 95 % bootstrap CI | Raw agreement |
|---|---:|---|---:|
| **axis_2_kazansky** (A/B/V/G) | **0.648** | [0.571 – 0.719] | **77.7 %** (233/300) |
| **axis_4_paribok** (P/K/D) | **0.521** | [0.430 – 0.608] | **77.0 %** (231/300) |

Roadmap target (B5): κ ≥ 0.70 **or** raw agreement ≥ 85 %.
**Neither axis clears that target** on the pooled sample.

Per ruling **D2** and the H453/A44 precedent: a measured κ **below** target is a
**reportable finding that closes the IRR gate**, not a defect to fix by
re-prompting until the number rises. The number goes into §7.5 of Article 1 as
the measured reliability of the instrument.

---

## Per-translator breakdown

| Translator | axis_2 κ [CI] | axis_2 agr | axis_4 κ [CI] | axis_4 agr |
|---|---|---:|---|---:|
| kalyanov | 0.928 [0.813–1.000] | 96 % | 0.732 [0.502–0.935] | 90 % |
| erman | 0.775 [0.601–0.925] | 88 % | 0.607 [0.419–0.788] | 78 % |
| syrkin | 0.616 [0.242–0.882] | 90 % | 0.362 [0.151–0.567] | 62 % |
| leonov | 0.498 [0.306–0.676] | 68 % | 0.000 [0.000–0.000]¹ | 82 % |
| vassilkov | 0.352 [0.136–0.580] | 66 % | 0.239 [−0.003–0.471] | 64 % |
| grintser | 0.210 [0.010–0.409] | 58 % | −0.048 [−0.087–0.000]¹ | 86 % |

¹ **κ paradox under extreme base rates.** Gold axis_4 is **208/300 = P**. On
grintser and leonov the gold is almost all P; high raw agreement with near-zero
(or negative) κ is expected when chance agreement is already high. Do not read
κ = 0 as "zero reliability" on those slices — report raw agreement alongside κ.

Kalyanov alone would clear both the κ and agreement targets; the **pooled**
instrument does not, driven by V/G boundary failures on vassilkov/grintser and
P/K/D depth boundaries on discursive translators (vassilkov, syrkin, erman).

---

## Confusion matrices (pooled)

### axis_2 — gold rows × Pass B columns

| gold \ pred | A | B | V | G |
|---|---:|---:|---:|---:|
| A | 31 | 0 | 1 | 0 |
| B | 0 | 7 | 2 | 0 |
| V | 9 | 0 | 91 | 7 |
| G | 6 | 0 | 42 | 104 |

Dominant off-diagonal: **G → V (42)**. Pass B systematically under-assigns G.

### axis_4 — gold rows × Pass B columns

| gold \ pred | P | K | D |
|---|---:|---:|---:|
| P | 180 | 10 | 18 |
| K | 11 | 13 | 16 |
| D | 11 | 3 | 38 |

Off-diagonals spread across all six directed P/K/D pairs — depth scale is
the soft boundary, not a single confusable pair.

---

## Disagreement adjudication (every row categorized)

Full machine list: [data/iaa/disagreement_adjudication.json](iaa/disagreement_adjudication.json).
Rule: **protocol-ambiguity** = both codes defensible under the frozen codebook
or the boundary is underspecified; **coder-error** = one side clearly violates
`classify_note.md`.

### axis_2 — 67 disagreements

| n | Category | Reading |
|---:|---|---|
| 42 | protocol-ambiguity: V/G interpretive boundary | Gold marks ethnographic/comparative "analysis" notes as G; Pass B treats them as V realia/narrative. Codebook's G cues ("анализирует", "сопоставляет") are present in many gold-G texts, but Pass B still defaults to V — **codebook executability gap**, not random noise. |
| 9 | protocol-ambiguity: A/V word-vs-thing | Epithets, botanical Latin, situational adjectives — gold V, Pass B A (or vice versa). Protocol has worked examples; residual edge cases remain. |
| 7 | protocol-ambiguity: V/G (Pass B over-interprets) | Inverse of the dominant class — Pass B lifts a realia note to G. |
| 4 | protocol-ambiguity: G-as-crossref vs A-as-epithet | Leonov «см. примеч. к …» epithet pointers coded G in gold, A in Pass B. |
| 2 | protocol-ambiguity: G/A system-concept | Rite / dharma-epithet boundary. |
| 2 | coder-error (gold suspect): B vs realia | Erman measure notes (yojana, muhūrta) coded B in gold; B is reserved for textology. Pass B V is codebook-correct. |
| 1 | coder-error (Pass B): A→V | One epithet misread as realia. |

**Net:** **64/67 = 96 % protocol-ambiguity**, **3/67 = 4 % coder-error**.
This is the same structural finding as H453/A44 (κ low / disagreements
**policy-not-fact**): the multi-class label set's *boundaries* are contested
even where substance is shared.

### axis_4 — 69 disagreements

| n | Category |
|---:|---|
| 18 | protocol-ambiguity: P/D multi-sentence narrative vs term-discourse |
| 16 | protocol-ambiguity: K/D system-place vs historical/comparative elaboration |
| 11 | protocol-ambiguity: K/P missing explicit system-placement cue |
| 11 | protocol-ambiguity: D/P interpretive narrative without term focus |
| 10 | protocol-ambiguity: P/K rite/system-concept default (axis_2 G override tension) |
| 3 | protocol-ambiguity: D/K depth boundary |

**Net:** **69/69 = 100 % protocol-ambiguity.** No pure factual misread of the
note text. The P/K/D scale is a **depth / framing instrument**, not a crisp
ontology — disagreements concentrate exactly where the length heuristic and the
content rule pull apart (protocol lines 99–102 of `classify_note.md`).

---

## Gate verdict

| Question | Answer |
|---|---|
| Is κ reported for both axes? | **Yes** — 0.648 and 0.521 with CIs |
| Does either axis clear κ ≥ 0.70 **and** agr ≥ 85 % pooled? | **No** |
| Does that block A19? | **No** — D2/H453: publish the measured number; do not invent ≥85 % |
| Every disagreement categorized? | **Yes** — 67 + 69 rows |
| What the manuscript may claim | Cross-coder (human × blind-LLM) agreement of **~78 % raw / κ ≈ 0.65 (axis_2) and κ ≈ 0.52 (axis_4)** on the 300-note gold; reliability is **moderate**; residual error is **boundary policy**, not random mislabeling. The ≥85 % validation *target* in §2.3 remains an **aspiration**, not a measured result — §7.5 must state the measured numbers. |
| Protocol revision (non-blocking follow-up) | Tighten V↔G decision rule for "ethnographic analysis of a concrete scene"; clarify that bare «см. примеч.» epithet pointers are **A** (or a dedicated reference type), not G; restate that axis_4 applies only when a Sanskrit term is the note's subject (not multi-sentence narrative realia). Optional: re-run Pass B after a frozen codebook patch — that is a **new** pre-registered study, not a silent re-tune of this one. |

---

## Reproduce

```powershell
# Pass B already written to data/{translator}_full.json (DeepSeek, 2026-07-24).
# Re-score only:
python scripts/compute_iaa_kappa.py --write

# Full re-run of Pass B (costs API calls; do not re-tune prompts to chase κ):
# requires DEEPSEEK_API_KEY in .env
python scripts/run_blind_iaa_pass.py --skip-existing
```

---

## Provenance

| Role | Actor |
|---|---|
| Pass A (gold) | Human Year-1 hand sample (manuscript §2.3) |
| Pass B | `deepseek-chat` @ `https://api.deepseek.com`, temperature 0, `prompts/classify_note.md` |
| Orchestration / adjudication write-up | Grok 4.5 (H1469 session, 24-07-2026); handoff intended executor was Opus 4.8 — session ran on explicit user launch |
| Kalyanov Pass B | Reused committed `data/kalyanov_full.json` (byte-identical DeepSeek run already on main; not re-tuned) |

_Dr. Mārcis Gasūns_

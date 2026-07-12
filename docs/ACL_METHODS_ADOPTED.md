# ACL / DH methods adopted for the Sundarakāṇḍa apparatus (H268 WS-C)

_Created: 07-07-2026 · Last updated: 07-07-2026_

> **What this is.** The bounded "focused scan → concrete adoption" record required by
> [H268](https://github.com/gasyoun/Uprava/blob/main/handoffs/archive/H268-Fable_CommentaryStrategies_sundara_LP_camera_ready_07.07.26.md)
> decision 4: which method families from the ACL Anthology / DH literature were **taken** into the
> camera-ready pipeline, which were **considered and skipped**, and where each adoption landed in
> code. This is an engineering adoption memo, not a survey; the eventual method paper (see §4)
> owns the full related-work treatment. Scan by Fable 5 (`claude-fable-5`), 07-07-2026; sibling
> baseline reused from
> [H265's ACL/DH compatibility analysis](https://github.com/gasyoun/SanskritLexicography/blob/master/ReverseDictionary/ACL_DH_COMPATIBILITY_ANALYSIS.md)
> (SanskritLexicography, PR [#207](https://github.com/gasyoun/SanskritLexicography/pull/207)).

## 1. Note quality / filtering — LLM-as-judge (WS-C1)

**Problem.** The Phase-2 reject taxonomy shows ~67 % of drafter rejects are «restates the
подстрочник» ([pilot_rejected.json](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/analysis/phase2_pilot/pilot_rejected.json));
the same failure mode passes *into* candidates at an unmeasured rate, and the filter was heuristic
(substring buckets). A ЛП volume needs every printed note to be *earned*.

**Adopted** (implementation:
[PHASE2_METHOD.md §3.4](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/PHASE2_METHOD.md)
— the scored judge rubric run as STEP 2b):

| Method family (representative work) | What we took | Where it landed |
|---|---|---|
| Rubric-anchored, reason-then-score evaluation — G-Eval (Liu et al., EMNLP 2023) | pointwise 0–2 anchors per axis, judge writes the reason before the score | §3.4 rubric table |
| LLM-judge bias analyses — MT-Bench/Chatbot Arena (Zheng et al., 2023); Wang et al. 2023 on position bias | **pointwise, never pairwise** (no position bias); refute-framing against leniency/verbosity bias | §3.4 "refute-framed", default verdict `park` |
| Self-preference bias — LLM evaluators favor their own generations (Panickssery et al., 2024) | **drafter ≠ judge**: a fresh agent instance scores, never the one that drafted | batch-3 run discipline |
| Faithfulness/consistency evaluation — SummaC (Laban et al., TACL 2022), AlignScore (Zha et al., ACL 2023), FActScore (Min et al., EMNLP 2023) | entailment framing: *every claim in the note must be entailed by the cited commentary chunk*; faithfulness is a **veto axis**, not a summand | §3.4 `faithfulness` gate («must be 2») |
| Content selection / salience — pyramid method lineage (Nenkova & Passonneau, NAACL 2004); "Citation Needed" annotation-worthiness (Redi et al., WWW 2019) | note-worthiness as its own scored axis: what does the note give beyond подстрочник + tier-1 + Phase-1 | §3.4 `non_triviality` + the drafters' `why_proposed` label |

**Considered and skipped:** multi-judge self-consistency voting (Wang et al., ICLR 2023) — ×3–5
judge calls per note across ~2,700 batch-3 verses is not affordable inside the 1-month window;
single refute-framed pass + human gate covers the risk (the human gate is the final arbiter
anyway). Prometheus-style fine-tuned judge models — no training loop in this repo, and the repo's
no-API-key policy limits us to in-session agents. Pairwise tournaments — position-bias mitigation
cost with no ranking need (the gate is absolute, not relative).

## 2. Alignment / anchoring precision (WS-C2)

**Problem.** A ṭīkā note attached to the wrong verse is a hard defect in print. Marker-based
segmentation + pratīka (catchword) prefix-matching reached 0.889–0.896 precision; the residual
~10 % = pronominal pratīkas («sa», «te») and paraphrasing ṭīkās that quote no verse word.

**Adopted:**

| Method family (representative work) | What we took | Where it landed |
|---|---|---|
| Quotation/text-reuse linking — passim (Smith et al., 2014), TRACER (Büchler), and the Sanskrit intertextuality line (BuddhaNexus; ByT5-Sanskrit, Nehrdich et al., 2024) | treat ṭīkā→verse attachment as **quotation linking with two independent signals**: exact catchword (pratīka) + lexical-overlap fallback | [`extract_yellow_sargas.py`](https://github.com/gasyoun/CommentaryStrategies/blob/main/scripts/extract_yellow_sargas.py) reassignment + verification passes |
| Overlap scoring for noisy reuse (containment vs Jaccard, text-reuse practice) | **containment** — \|chunk ∩ verse\| / \|verse\| over `sanskrit_util`-canonicalized tokens; asymmetric so chunk length can't dilute the score | [`sa_align.containment`](https://github.com/gasyoun/CommentaryStrategies/blob/main/scripts/sa_align.py) |
| Windowed local alignment (sentence-alignment practice, Vecalign-style locality) | candidates restricted to a ±3-verse window around the marker; moves need a margin (≥0.20 containment, ≥0.08 over incumbent) — no global re-shuffling | `CONTENT_*` thresholds in the segmenter |

**Measured result (07-07-2026):** strict pratīka precision unchanged **0.888** (definition kept for
honesty); **verified precision (pratīka ∪ content anchor) = 0.964** on the 10 gated sargas,
**0.945** across the 58 batch-3 sargas — H268's >0.90 target cleared. Chunks failing both signals
carry `suggest_verse`, get judge verdict `flag_anchor`, and cannot print without a human fix.

**Considered and skipped:** neural word aligners — SimAlign (Jalili Sabet et al., Findings EMNLP
2020), awesome-align (Dou & Neubig, EACL 2021), fast_align (Dyer et al., NAACL 2013) — these align
*parallel bitext* word-to-word; ṭīkā→verse attachment is quotation linking between a text and its
commentary, not translation alignment, and the multilingual-embedding aligners add a heavy
dependency for a residual of ~40 hard chunks (11 of which are bare pronouns no aligner can anchor).
Embedding-based semantic matching for the paraphrase tail — deferred: the org's `sanskrit-util`
canon + containment already reaches the target, and any embedding stack would violate the repo's
stdlib-only default. Prior-art rule honored: canonicalization reused from `sanskrit_util`
(SHARED_CODE §1–2), no new transcoder written.

## 3. DH data-publication baseline (inherited from H265 — not re-derived)

H265's analysis (same day, sibling repo) already ruled the org baseline: data statements
(Bender & Friedman 2018, schema v3), `CITATION.cff` 1.2.0, the ARR Responsible NLP checklist §B
(cite artifacts, machine-readable license, provenance, use-restriction disclosure), and the
pragmatic "documented schema now, TEI as optional interoperability layer later" stance
(TEI Lex-0 for lexicographic data). This repo already carries CITATION.cff, RIGHTS.md,
per-note provenance stamps and CC BY 4.0 attribution for the ṭīkā corpus
([data/valmiki_PERMISSION.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/valmiki_PERMISSION.md));
TEI P5 export exists for the gold sample (`scripts/export_tei.py`). Nothing further is adopted
here inside the 1-month window; the critical-apparatus TEI encoding of the *book* apparatus is
flagged as a post-camera-ready enhancement.

## 4. Noted for the method paper, not chased now (H268 §WS-C boundary)

Digital critical editions / TEI critical-apparatus / standoff annotation / computational
commentary as venue framing for the pipeline's method paper (candidate A-paper, see
[Uprava/ARTICLES.md](https://github.com/gasyoun/Uprava/blob/main/ARTICLES.md)): the natural venues
are the ACL workshop circuit (LaTeCH-CLfL, ML4AL) and DH journals; the H265 venue table
(WSC/COLING/LREC line) transfers. The judge rubric + two-signal anchoring + human-gate discipline
is itself the paper's method core. Parked deliberately — no further tokens spent this pass.

_Dr. Mārcis Gasūns_

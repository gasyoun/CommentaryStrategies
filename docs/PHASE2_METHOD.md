# Phase-2 method manual — Sundarakāṇḍa commentator-dialogue layer

_Created: 01-07-2026 · Last updated: 04-07-2026_

> **What this is:** the complete, reproducible procedure for generating the Type-Б/В
> "commentator-dialogue" note layer for the Russian Sundarakāṇḍa — every step, *when* it runs, *how* to
> run it, and *why* it is done that way. Written so M.G./Kostina can review and correct the method **before
> it is scaled** past the 2026-07-01 pilot (sargas 35/36/37).
>
> Companion docs: [`docs/PHASE2_SUNDARA_HANDOFF.md`](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/PHASE2_SUNDARA_HANDOFF.md)
> (scope + decisions) · [`SUNDARA_COMMENTARY_RATIONALE.md`](https://github.com/gasyoun/CommentaryStrategies/blob/main/SUNDARA_COMMENTARY_RATIONALE.md)
> (Phase-1 ledger) · [`data/valmiki_PERMISSION.md`](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/valmiki_PERMISSION.md) (rights).

## 0. Why this layer exists

Phase-1 reached ~24 % density (Grintser level) using **dictionary** glosses. Phase-2 adds what a dictionary
cannot: what the **traditional Sanskrit commentators** (Tilaka, Bhūṣaṇa, Śiromaṇi) actually *say* about a
verse — a disambiguation, a supplied ellipsis, a textual variant, a myth behind a simile, a doctrinal
frame. The goal is to put Leonov's translation into dialogue with the ṭīkā tradition, in the register of
the «Литературные памятники» series (Grintser's Rāmāyaṇa is the benchmark), moving toward Leonov's own
~36 % density. **Depth, not bulk** — see §6 on why the accept rate is deliberately low.

## 1. Pipeline at a glance

```
data/valmiki_commentaries/kanda_5_sundarakanda/{tilaka,bhusana,siromani}_sarga_NN.txt   (licensed source)
        │  STEP 1 — deterministic segmentation (Opus-written Python, no LLM)
        ▼
data/analysis/sundara_commentary_segmented.json   (per-verse: verse + подстрочник + 3 commentaries)
        │  STEP 2 — candidate drafting (Sonnet subagents, 1 per sarga, parallel, write-only)
        ▼
data/analysis/phase2_pilot/sarga_NN_candidates.json   ({notes[], rejected[]}, all review_required)
        │  STEP 3 — deterministic merge + reject taxonomy (Opus-written Python)
        ▼
data/analysis/phase2_pilot/pilot_candidates.json  +  pilot_rejected.json  +  PILOT_REVIEW.md
        │  STEP 4 — HUMAN GATE (Leonov/Kostina): accept / edit / reject each note
        ▼
data/sundara_ch{NN}_commentary_to_add.json (accepted, stamped)  +  *.rejected.json (with reason)
```

**Model division (reported per project convention — tier AND version):**
- Orchestration + all deterministic code + this manual: **Opus 4.8** (`claude-opus-4-8`).
- Sanskrit→Russian note drafting: **Sonnet 5** (`claude-sonnet-5`), one subagent per sarga.
- The human gate: M.G. + E. Kostina. Nothing reaches the book without it.

## 2. STEP 1 — deterministic segmentation

**When:** first, once per batch of sargas. **Why deterministic:** splitting commentary by verse is
mechanical and must be reproducible/auditable — no LLM judgment belongs here.

**How:**
```sh
python scripts/extract_yellow_sargas.py            # pilot sargas 35 36 37
python scripts/extract_yellow_sargas.py 22 24 26   # any sargas
```
[`scripts/extract_yellow_sargas.py`](https://github.com/gasyoun/CommentaryStrategies/blob/main/scripts/extract_yellow_sargas.py)
splits each commentary file on its `।। 5.<sarga>.<verse> ।।` markers (text *before* a marker glosses that
verse), aligns each verse with the IAST verse text and Leonov's подстрочник from the sibling
`SamudraManthanam` corpus, and writes per-verse bundles.

**Pilot output:** 253 verse-bundles (70 with all three commentaries, 204 corpus-aligned, 48 merged-range
markers).

**Known caveats (carry into the gate):**
- **Merged-range markers**: the source sometimes emits one marker for a verse range, scraped as a single
  token (e.g. `5.35.810` = vv. 8–10). These are flagged `ambiguous_marker: true` and don't align to a
  single passage; almost all are rejected in Step 2.
- **Marker offset glitch**: at least one verse (5.36.45) had its Bhūṣaṇa chunk actually belonging to v. 4.
  Isolated, and it produced no accepted note — but it is why **verse_ids must be verified against print**.

## 3. STEP 2 — candidate drafting (Sonnet subagents)

**When:** after Step 1, once the segmented JSON exists. **Why an LLM:** distilling Devanagari commentary
prose into a terse Russian ЛП note is a translation/judgment task, not a lookup. **Why Sonnet:** strong at
Sanskrit→Russian; and driven *inside Claude Code* it needs no API key (this sidesteps the repo's
"no-Anthropic-key" constraint, which governs only the standalone `scripts/annotate_batch.py` pipeline —
see §8). **Why one small agent per sarga, write-only:** the host process cycles and kills long agents;
small parallel agents each writing one file avoid git-index races and are resumable. This mirrors the
Phase-1 lesson.

**How:** the orchestrator (Opus) spawns N Sonnet subagents, each given the style contract below, the
resolved decisions, the input path, and an output schema; each writes exactly
`data/analysis/phase2_pilot/sarga_NN_candidates.json` and returns a count summary. No agent runs git.

### 3.1 Style contract (the ЛП register — non-negotiable)
- 1–3 sentences, затекстовое примечание. Terse. No essay, no Devanagari, no block quotes.
- Russian scholarly voice — *distil* the commentator, do not translate his Sanskrit syntax.
- **Name the commentator in-note** («по Тилаке», «Бхушана поясняет…») — decision [D-P2-2]; this is tier-2
  of model II. (Hard-rule #4 forbids naming them in the *article title* only — not in the apparatus.)
- Short **IAST pratīka** lemma; keep IAST ≈12 % of the note (Grintser calibration) — decision [D-P2-3].
- Kazansky type per note: **Б** = textological (wording / meaning / ellipsis / variant); **В** =
  realia/historical-cultural (place, custom, myth, epithet). Realia → В, never Б.
- **`why_proposed`** (required label): one clause stating *why this note earns a place* — what it gives
  beyond the подстрочник (the acceptance rationale, mirror image of a reject reason). The reviewer sees
  this label first. Pilot notes were back-filled by Opus (`scripts/backfill_why_proposed.py`); future
  agents emit it natively.
- Obey `validate.py` hard rules: never «М.: Наука 2022» for Leonov; «Парибка» is the only oblique form.

### 3.2 What to draft vs. skip — the reject discipline
Draft a note **only** when the commentary adds something **neither the подстрочник NOR Leonov/Kostina's
own note** already gives. **Reject** when it (a) restates the подстрочник, (b) duplicates a Leonov/Kostina
own note on the same verse+point (see §3.3), (c) is pure Sanskrit grammar/parsing invisible to a Russian
reader, (d) is formulaic praise, (e) is a non-independent merged-range marker, or (f) duplicates an
earlier note. Every rejection is **kept with its reason** (§6).

### 3.3 Dedup baseline — Leonov/Kostina's OWN apparatus (model II tier-1)
Leonov/Kostina already wrote **1,058 notes** across all 68 sargas (their print apparatus — this *is* the
~36 % density benchmark, and model II tier-1). Digitized by
[`scripts/extract_leonov_notes.py`](https://github.com/gasyoun/CommentaryStrategies/blob/main/scripts/extract_leonov_notes.py)
from `ramayana-leonov/Рамаяна. Книга 5. Сундараканда 2026.html` →
[`data/leonov_own_notes.json`](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/leonov_own_notes.json)
(442 attributed to Kostina, 616 unattributed = Leonov; ~1,022 verses covered).
**Every Phase-2 candidate must be checked against this file** — a commentator note that repeats a point
Leonov/Kostina already made is a duplicate. **The 2026-07-01 pilot did NOT have this baseline** (agents
deduped only against the подстрочник): 9 of the 16 candidates landed on verses Leonov already comments on,
and several (e.g. 5.37.25 nāgarājasya, 5.35.82 Śambasādana, 5.36.17 upāya, 5.36.33 Śachī) are effective
duplicates. The interactive review page now shows Leonov's own note per verse in red so the reviewer sees
the overlap; when scaling, the drafting prompt must include the sarga's Leonov notes as dedup context.

## 4. STEP 3 — merge + reject taxonomy

**When:** after all sargas in the batch are drafted. **How:**
```sh
python scripts/merge_phase2_pilot.py
```
[`scripts/merge_phase2_pilot.py`](https://github.com/gasyoun/CommentaryStrategies/blob/main/scripts/merge_phase2_pilot.py)
combines the per-sarga files into
[`pilot_candidates.json`](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/analysis/phase2_pilot/pilot_candidates.json)
(all notes) and
[`pilot_rejected.json`](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/analysis/phase2_pilot/pilot_rejected.json)
(all rejections, each tagged with a reason **bucket**), and asserts every note is `review_required`.

## 5. STEP 4 — the human gate (this is where you come in)

**When:** now, before any scale-up. **Interactive — no printing.** Build and open the review page:
```sh
python scripts/build_pilot_review_html.py     # -> data/analysis/phase2_pilot/review.html
```
Open [`data/analysis/phase2_pilot/review.html`](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/analysis/phase2_pilot/review.html)
in a browser. Each card shows: the verse (IAST + Leonov подстрочник), the **`why_proposed`** label,
the proposed note, the **Sanskrit source** (all three commentators at that verse; the cited one
highlighted), **neighbouring verses ±2** (so you see what else is commented nearby), and any existing
Phase-1 note on the verse. Click **✅ принять / ✏️ править / ❌ отклонить** per card (edit box and
reject-reason field appear as needed). Choices persist in `localStorage`; **⬇ Скачать decisions.json**
exports them (or ⧉ copy). The static markdown sheet `PILOT_REVIEW.md` remains as a read-only fallback.

**Caveat shown in the page:** the per-verse "source" is the segmenter's alignment; because of marker
offsets/merged ranges it can differ from where the drafter actually found the cited text (e.g. 5.35.45
cites Tilaka but Tilaka's chunk aligned to a neighbour) — the neighbours panel is there to cover this.

**After you send `decisions.json` back:** an apply step (to be written) grafts `accept`/`edit` notes into
`data/sundara_ch{NN}_commentary_to_add.json` with a `gated_by`/`gated_date` stamp and the (possibly edited)
text; `reject` entries go to a `.rejected.json` with your reason. Only once you approve the **register** do
we scale.

## 6. Why the accept rate is ~6 % (and why that is correct)

Pilot: **16 accepted of 253 considered (6.3 %); 138 rejections.** Reject taxonomy:

| bucket | count | meaning |
|---|---:|---|
| restates_podstrochnik | 92 | commentary just re-says what Leonov already conveys |
| merged_range_marker | 25 | non-independent verse-range token, no single-verse gloss |
| pure_grammar | 12 | Sanskrit parsing invisible/irrelevant to a Russian reader |
| overlaps_other_note | 4 | point already made in a drafted note for a nearby verse |
| other | 3 | paraphrase-only / variant-without-gloss / speech-marker |
| formulaic_panegyric | 1 | ornamental praise, no exegesis |
| data_misalignment | 1 | the 5.36.45 marker-offset glitch |

The headline finding: **two-thirds of all commentary simply restates the подстрочник.** That is expected —
a commentator-dialogue layer is inherently sparse, because most verses are not textually contested. This
layer is for **depth on the hard verses**, not density. The bulk of the ~36 % target will come from the
already-built lexical layer, not from this one. A *high* accept rate here would be the warning sign (it
would mean padding), exactly as the Phase-1 lexical gate proved.

## 7. Count reconciliation (honesty note)

`notes (16) + reject-entries (138) = 154 ≠ 253 verses considered`. The gap is because the drafters grouped
some rejects (e.g. one entry `5.35.17-20` covers four verses) and some considered bundles were
merged-range markers counted once. This is bookkeeping fuzz, **not** dropped data. When scaling, prefer
per-verse reject entries so the arithmetic closes.

## 8. Provenance, rights & reproducibility

- **Provenance:** every note carries `provenance: {model: "claude-sonnet-5", tier: "Sonnet", step:
  "phase2_pilot_draft"}` and `review_required: true`. The reject log records the drafter's reason.
- **Reproducibility caveat:** because the pilot was drafted by Sonnet *inside Claude Code*, the committed
  standalone `scripts/` cannot reproduce the exact note texts without Claude Code. Steps 1, 3 (Python) are
  fully deterministic and reproducible; Step 2 (drafting) is model-mediated and human-gated, so the record
  is the committed candidate files + this manual, not a re-runnable keyless script. Anyone without Claude
  Code can reproduce the drafting via the repo's openai-compat backend (`scripts/annotate_batch.py`,
  DeepSeek etc.) — the "no Anthropic key" rule applies to that path.
- **Rights:** commentary source is the Gita Supersite corpus, used by permission (CC BY 4.0). Any
  redistribution carries the attribution string from [`data/valmiki_PERMISSION.md`](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/valmiki_PERMISSION.md).

## 9. Scaling plan (only after the pilot register is approved)

1. Run Step 1 on the next batch — the 14 🟡 sargas first (22, 24, 26, 30, 34, 35–37, 39, 51), then 🔴/⚪.
2. Fold any register corrections from the gate into the Step-2 style contract before drafting more.
3. Draft (Sonnet, ≤3–4 parallel agents), merge, gate — same loop.
4. Track cumulative density in `data/sundara_book_stats.json`; stop the *commentator* layer when its
   marginal accept rate collapses (dry signal), not at a fixed count.
5. Switch to per-verse reject entries (§7) so counts reconcile at scale.

## 11. Alignment accuracy — current state & preprocessing plan

**Current (marker-only) accuracy.** Step 1 aligns commentary to verses solely by the `।। 5.s.v ।।`
markers. Pilot: **204/253 (~81 %) of bundles corpus-aligned**; 48 merged-range markers. Per-commentator
alignment is weaker — e.g. 5.35.45 cites Tilaka, but Tilaka's chunk aligned to a neighbour/merged token.
Two failure modes: (a) **merged-range tokens** (`5.35.810` = vv. 8–10) don't map to one verse; (b)
**marker offsets** (a chunk sits before the wrong marker, e.g. 5.36.45 held v. 4's text).

**Yes — accuracy can be materially improved, mostly by preprocessing** (documented now, to implement before
scaling):
1. **Merged-range reconstruction.** Parse tokens like `810` using sequence context (prev marker 7, next 11
   ⇒ 8–10); attribute the chunk to each verse in the range and tag `verse_range`. Repairs most of the 48.
2. **Sequence validation + offset repair.** Cross-check the marker sequence against the canonical verse
   count per sarga (e.g. 90 for sarga 35); flag out-of-order/duplicate markers and snap them to the
   expected position. Catches the 5.36.45-type offset.
3. **Pratīka anchoring (strongest signal).** Every traditional gloss opens with a *pratīka* — the verse
   catchword it comments (e.g. `yānīti` = yāni + iti). Match the pratīka against the verse's own words
   (transliteration-normalized, via the org `sanskrit-util` toolkit — do not re-implement transcoding) to
   align **by content**, independent of the `।।` marker. This would have placed Tilaka on 5.35.45
   correctly. Define **alignment precision = fraction of chunks whose pratīka matches the assigned verse**;
   target > 95 %.
4. **Keep multi-glosses.** A verse can carry several sub-glosses (bhūṣaṇa emitted 131 markers for 90
   verses) — preserve all, don't collapse.

Until this lands, the mitigation is the review page's **neighbours ±2** panel and the honest per-page
caveat. Recommended order: implement (1)+(2) as a cheap `extract_yellow_sargas.py` preprocessing pass,
then (3) as a validation/repair step reported alongside the segmented output.

**IMPLEMENTED 2026-07-01 (partial):** shared canon module `scripts/sa_align.py` (wraps `sanskrit_util`
`nfold` + `difflib`; SHARED_CODE §1-2). Wired into `compare_editions.py` (principled canon; identical
1006→1065; transposition detection; true-vs-apparent absence split — but `critical_only` stayed ~399,
needs fuzzy global assignment, not done) and into `extract_yellow_sargas.py` as pratīka anchoring: each
gloss's leading pratīka is deva→iast→canon'd and prefix-matched to the verse; the run now reports
`alignment_precision`. **Measured: 0.432** (197/456) with prefix matching — well below the >95% target,
and 138/259 mismatches carry a `suggest_verse` (a nearby verse the pratīka fits) → the marker-based
segmentation has a systematic offset recoverable by a **reassignment pass (item 3, NOT yet done)**. So
p.1 delivered the shared canon + honest metrics + edition correctness, but neither aspirational target
(critical_only <50, precision >95%) is met yet.

**Item 1a (fuzzy assigner) 2026-07-01 — done, corrected conclusion.** Token-set Jaccard pass pairing
mutually-unmatched verses recovered only 22 clean pairs (critical_only 399→377). A sample diagnostic
showed the residual is NOT artifact: those critical verses map to nearby southern verses at Jaccard
0.27–0.44 — the **same shlokas heavily reworded** between Baroda critical and southern vulgate. The "<50"
premise was wrong (the recensions rephrase pervasively). The useful output instead **partitions the 742
southern-only into `structural_absence` (307, best Jaccard vs any critical verse < 0.25 → real absence,
safe footnote) vs `reworded` (435, 0.25–0.5 → variant reading, NOT an absence)** — the real accuracy win
for footnotes (item 4): only the 307 + whole extra sargas are truly "absent in critical."

**Item 1b (segmenter reassignment) 2026-07-01 — done.** `extract_yellow_sargas.py` now re-anchors each
commentary chunk to the verse its leading pratīka actually matches (nearest in the sarga), fixing the
systematic marker offset instead of only flagging it. **179 chunks reassigned; pratīka alignment precision
0.432 → 0.799 → 0.896** (353/394) after adding **iti-stemming** to the matcher (a pratīka is quoted fused
with *iti*: `rakṣitā+iti`→`raksiteti`; stripping `-iti/-eti/-ti` yields a stem that prefix-matches the
verse word). The residual ~10% (41 chunks) is the genuinely-hard set and is left as-is (diminishing
returns): 11 bare-pronoun pratīkas ("sa"/"te") and ~30 Tilaka/Śiromaṇi *paraphrases* that don't quote a
verse word. Reassignment is heuristic; all downstream notes stay `review_required`.

## 10. Decision & change record

- 2026-07-01 — C0/D2 = model II (two-tier hybrid); D-P2-1 pilot 35/36/37; D-P2-2 name commentator in-note;
  D-P2-3 RU + IAST pratīka; D-P2-4 hybrid (Sonnet drafts, human gates); D-P2-5 ~36 % post-approval.
- 2026-07-01 — pilot drafted (16 notes), reject log consolidated + taxonomy added; awaiting human gate.
- 2026-07-03 — **pilot gated by M.G.: 16/16 passed** (9 accept / 7 edit / 0 reject). Edit-directives
  («объединить с комментарием Костиной») preserved as `gate.mg_comment`, note text kept clean.
- 2026-07-04 — decisions applied by [`scripts/apply_phase2_decisions.py`](https://github.com/gasyoun/CommentaryStrategies/blob/main/scripts/apply_phase2_decisions.py)
  (the §5 apply step, now written): grafted into ch35/36/37 + book aggregate with `gate` stamps,
  `review_required` stays true until the Leonov/Kostina assembly gate. **Scale batch 2 drafted**
  (H142): sargas 22/24/26/30/34/39/51, 38 candidates / 350 verses (10.9%), per-verse rejects (§7
  fixed — counts reconcile exactly), tier-1 dedup context in every drafting prompt (§3.3 satisfied;
  41 rejects bucketed `duplicate_of_tier1`), pratīka precision 0.889 across all 10 yellow sargas.
  Review page: [`data/analysis/phase2_batch2/review.html`](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/analysis/phase2_batch2/review.html).
  Drafting Sonnet 5 (`claude-sonnet-5`), orchestration Fable 5 (`claude-fable-5`).

_Dr. Mārcis Gasūns_

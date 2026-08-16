# The Nīlakaṇṭha licence register — 151 tradition-attested Pāṇini deviations from the *Bhāratabhāvadīpa*

_Created: 16-08-2026 · Last updated: 16-08-2026_

Build report for [H2860](https://github.com/gasyoun/Uprava/blob/main/handoffs/H2860-Opus_CommentaryStrategies_commentary-licence-register-build-nilakantha_15.08.26.md),
executed 16-08-2026 by Opus 5 (`claude-opus-5`) on the GO verdict of
[H1324](https://github.com/gasyoun/Uprava/blob/main/handoffs/H1324-Opus_CommentaryStrategies_mbh-ramayana-commentary-parsing-feasibility_19.07.26.md).
Predecessor and premise:
[COMMENTARY_LICENCE_REGISTER_FEASIBILITY_2026.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/reports/COMMENTARY_LICENCE_REGISTER_FEASIBILITY_2026.md).

**The register exists.** 151 rows, every one carrying locus, commentator, `defense_term`,
a `deviation_type`, and a quotation; 149 of the types derived mechanically, 2 assigned by
hand, 14 further hits rejected as the *ārṣa* homonym with a written reason each. Precision
of the word-anchored sweep, hand-checked over **all 165 hits rather than a sample**:
**91.5 %**.

## 1. What changed under the feasibility report

Three of the probe's conclusions survive intact, and three need correcting. The
corrections are the useful part of this report.

| Probe said | Build measured |
|---|---|
| Narrow vocabulary (`ārṣa`, `chāndasa`) is right; `pramāda` is 0/56 | **Confirmed at 60× the sample.** `प्रमाद` occurs **79 times** in the ṭīkā and licenses nothing: 76 carry the moral sense (heedlessness — "one of the fourteen royal vices", "the eight *pramāda*s of the senses"), and the remaining 3 are `लेखकप्रमादः` "a scribe's slip" (MBh 2.49.26, 3.119.13, 4.46.20), which is the **opposite** of a licence — it says the reading is wrong, not that it is defensible |
| Nīlakaṇṭha is machine-readable; one re-run of the scraper restores it | **Was true, then stopped being true, now true again** — §2 |
| Locus alignment is free | **Confirmed.** Every row's locus is the scrape's own P/U/A/S id; no alignment step was written |
| The homonym *ārṣa vivāha* "never fired" (0 hits in the Gītā) | **Wrong at MBh scale.** It fires **6 times**, all in the dharma sections (Ādi 1.13/1.102/1.113, Anuśāsana 13.19 ×2, 13.44) — §5 |
| An unanchored grep is the precision trap | **Not in Devanāgarī.** The script anchors `आर्ष` for free; two *different*, smaller traps replace it — §4 |
| "High hundreds to low thousands" of rows | **151.** The order-of-magnitude estimate was 3–6× high — §6 |

## 2. Step 1: the scrape had to be repaired, not just re-run

The handoff costed step 1 as "scripted, one run". It was not. Between the 11-07-2026 scrape
and today, [sanatana.in](https://sanatana.in/mahabharata/) moved its text off the endpoint
[`nilakantha_parser.py`](https://github.com/gasyoun/CommentaryStrategies/blob/main/mahabharata-nilakantha/nilakantha_parser.py)
was written against, and did so in the worst possible way:

> `GET /mahabharata/listing/getParvaByPage/{parva}?page={N}` still exists, still returns
> **HTTP 200**, and now returns a body of exactly one byte — a newline.

The parser's `scrape_parva()` reads an empty page as "end of parvan" and stops. A re-run
would therefore have written a **valid, empty, silent** JSONL and reported success. This is
the failure mode a `raise_for_status()` cannot catch and a row-count assertion can.

The live path is a JSON window endpoint, one call per **upaparvan**:

```
GET /mahabharata/listing/getUpaparvaWindow/{parva}?center={P##_U##}&before=0&after=0
 -> {"upaparvas":[{"id","upaParvaName","html"}],"hasPrevious","hasNext","centerId"}
```

with the upaparvan ids enumerated from the index page `/mahabharata/Moola/`. The HTML inside
the window is unchanged — the same `<div class="shloka" id="P/U/A/S">` + `<p class="shloka_text">`
+ `<p class="bhavadeepa">`, so `parse_page()` was reused untouched. 107 requests at the
parser's own 1 s pacing replace the old ~1 700.

**The restored scrape reproduces the 11-07-2026 census exactly** — 83,971 shlokas, 24,694
carrying ṭīkā (29.4 %), and every one of the 18 per-parvan pairs identical to the numbers in
[NILAKANTHA_VULGATE_CENSUS.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/mahabharata-nilakantha/NILAKANTHA_VULGATE_CENSUS.md).
That equality is the evidence that the new endpoint serves the same corpus, not a subset.

The old path is kept behind `--legacy-endpoint`, documented as dead, so the census of
11-07-2026 stays reproducible in principle and nobody re-derives the diagnosis.

## 3. Step 2: the per-parvan density census

Measured over all 24,694 ṭīkā-bearing shlokas.
Machine-readable:
[data/licence_register/nilakantha_parvan_density.tsv](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/licence_register/nilakantha_parvan_density.tsv).

| # | Parvan | ṭīkā shlokas | ṭīkā chars | raw hits | per 1 000 ṭīkā shlokas | per 100 k ṭīkā chars |
|---|---|---:|---:|---:|---:|---:|
| 1 | ādi | 3 177 | 324 258 | 24 | 7.55 | 7.40 |
| 2 | sabhā | 1 107 | 137 815 | 5 | 4.52 | 3.63 |
| 3 | vana | 3 592 | 344 562 | 26 | 7.24 | 7.55 |
| 4 | virāṭa | 857 | 77 915 | 8 | 9.33 | 10.27 |
| 5 | udyoga | 2 391 | 255 384 | 18 | 7.53 | 7.05 |
| 6 | bhīṣma | 1 393 | 416 619 | 10 | 7.18 | 2.40 |
| 7 | droṇa | 1 249 | 68 509 | 4 | 3.20 | 5.84 |
| 8 | karṇa | 736 | 44 277 | 9 | 12.23 | 20.33 |
| 9 | śalya | 254 | 14 091 | 3 | 11.81 | 21.29 |
| 10 | sauptika | 132 | 10 224 | **0** | 0.00 | 0.00 |
| 11 | strī | 162 | 8 654 | 2 | 12.35 | 23.11 |
| 12 | śānti | 6 600 | 980 669 | 41 | 6.21 | 4.18 |
| 13 | anuśāsana | 2 080 | 186 103 | 15 | 7.21 | 8.06 |
| 14 | āśvamedhika | 732 | 102 164 | **0** | 0.00 | 0.00 |
| 15 | āśramavāsika | 149 | 12 494 | **0** | 0.00 | 0.00 |
| 16 | mausala | 46 | 3 223 | **0** | 0.00 | 0.00 |
| 17 | mahāprasthānika | 31 | 1 865 | **0** | 0.00 | 0.00 |
| 18 | svargārohaṇa | 6 | 499 | **0** | 0.00 | 0.00 |
| — | **all 18** | **24 694** | **2 989 325** | **165** | **6.68** | **5.52** |

Read the last two columns together, and never quote either alone.

- **Six parvans return zero.** Per the handoff's own instruction this is a **finding, not a
  bug**: it is the same result the probe got on Rāmopākhyāna (0 over 77,508 chars), now at
  book scale. Five of the six are the short closing books, where the whole ṭīkā is 499–12,494
  characters; sauptika and āśvamedhika are large enough (10k and 102k chars) that zero is a
  real property of Nīlakaṇṭha's attention there, not a sampling artefact.
- **The two rates disagree, and the disagreement is informative.** Bhīṣma is mid-pack per
  shloka (7.18) and near the bottom per character (2.40) — its ṭīkā is the Gītā commentary,
  enormous per verse and philosophical rather than grammatical. Karṇa, śalya and strī invert
  it: few, short, dense glosses.
- **Any density figure must name the parvans it averages over.** The corpus mean of 6.68 per
  1 000 ṭīkā shlokas is an average over eighteen books of which a third contribute nothing.

## 4. The pattern: what anchoring means in Devanāgarī

The feasibility report's central methodological warning — that an unanchored `ārṣ\w*` matches
inside `pārṣada`, `kārṣīr`, `vārṣika` and drags precision from 100 % to 37 % — **does not
transfer to the Devanāgarī corpus**, for a reason worth writing down once:

> `आ` is an *independent* vowel sign. Inside a word, ā is written with the dependent mātrā
> `ा`, so a compound-internal *ārṣa* (…सार्ष…) simply is not the same character sequence.
> **The script anchors the term for free**, and the IAST trap cannot occur.

What replaces it is smaller and different in kind: unrelated *stems* that genuinely begin
आर्ष. Five hits, all excluded by one negative lookahead, none by hand:

| Stem | What it is | Hits |
|---|---|---:|
| आर्ष्टिषेण | Ārṣṭiṣeṇa, a sage's name | 2 |
| आर्ष्यशृङ्गि | Ārṣyaśṛṅgi, patronymic of Ṛṣyaśṛṅga | 1 |
| आर्षभ | *ārṣabha* "of the bull", from ṛṣabha | 1 |
| आर्षेय | *ārṣeya*, the gotra term | 1* |

\* *ārṣeya* occurs once, unfused (`सतां ग्रहणम् आर्षेयं वरणं`, MBh 12.296.18), so only the
lookahead catches it; the आ-anchor would have passed it through.

For `छान्दस` **no anchor is used, deliberately.** It is consonant-initial, so no equivalent
guard exists — and none is wanted: 30 of 30 occurrences are licence-claims, and two thirds of
them sit at a sandhi junction (…नुमभावच्छान्दसः, …सुपो डादेशश्छान्दसः) or inside a solid
compound (…असन्धिप्रछान्दसः) where a "no preceding Devanāgarī letter" lookbehind destroys
them. Measured cost of adding that lookbehind: **16 of 30 rows lost, 0 false positives
prevented.** This is the Devanāgarī form of the report's own note that a licence term
legitimately follows a hyphen in IAST.

### 4.1 The trap that actually bit: sandhi hides the *grammatical* noun too

The same orthography that anchors `आर्ष` also **erases the initial vowel of the technical
term Nīlakaṇṭha names beside it**. `अडभाव` appears as …इत्यडभाव and …त्राडभाव; `आडभाव` as
ङितामाडभाव; `अन्तादेश` as आकारोन्तादेश; `अडागम` behind an avagraha as …पूर्वोऽडागम. Matching
the citation form alone drops those rows silently into the hand queue — a recall bug that
*looks* like philological difficulty. Every vowel-initial trigger in the lexicon is therefore
written with its initial vowel optional.

Two of these were not recall bugs but **sign inversions**, and they are the ones to remember:

- `…ासन्धिप्रछान्दसः` — the negating अ- of *asandhi* is fused into the preceding ā, so a plain
  `सन्धि` pattern types the row as *sandhi* when the claim is the **absence** of sandhi.
- `सुलोपाभाव`, `इतोलोपाभाव` — matching the substring `…लोप` first types an **absence** of
  elision as an elision.

Both now have their negative patterns ordered ahead of their positive ones, with the reason in
a comment beside them.

## 5. Precision — measured on every hit, not on a sample

165 word-anchored hits, **all 165 read in context** — the corpus is small enough that
sampling would have been a needless loss of information. 151 are licence-claims, 14 are not.

| | Rows | Share |
|---|---:|---:|
| Licence-claims kept, type derived automatically | 149 | 90.3 % |
| Licence-claims kept, type assigned by hand | 2 | 1.2 % |
| **Register total** | **151** | **91.5 %** |
| Rejected — *ārṣa* as a marriage rite (dharmaśāstra) | 6 | 3.6 % |
| Rejected — *ārṣa* glossed in its ordinary sense | 8 | 4.8 % |

Against the handoff's fail condition — "precision on a fresh 30-row hand sample below ~90 %"
— 91.5 % passes, and the exhaustive check is stronger evidence than the sample it replaces.
The 30-row sample was still drawn (uniform, seed 2860, over the auto-typed rows), verified,
and put on the review sheet for a second pair of eyes: **30 of 30 correct**.

### 5.1 What the exhaustive check caught that a 30-row sample would have missed

Reading all 165 was not ceremony. The first automatic pass scored **150 / 151 on membership
and 148 / 151 on type**, and every one of the three defects sat outside any plausible sample:

| Locus | Defect | Cause | Fix |
|---|---|---|---|
| MBh 5.70.7 | **False positive** — *ārṣam* glossed as "the Veda" admitted as a licence-claim | `svārthe taddhitaḥ` two characters upstream belongs to the *previous* derivation (`sattvataḥ > sātvataḥ`) and has nothing to do with the *ārṣa* | hand override, rejected |
| MBh 12.342.77 | *bha-stem treatment* typed as *kṛtya suffix `tvan`* | a bare `त्वन्` pattern matched inside `सत्त्वन्तः` "possessing *sat*" | pattern tightened to the two contexts where *tvan* is actually named |
| MBh 5.141.47 | *upapada government* typed as *vowel lengthening* | "first lexicon entry that matches anywhere in ±120 chars" reached a `दीर्घश्च` forty characters downstream, in the next clause | selection changed to the operation **nearest** the licence word, lexicon order as tie-break |

The second and third are one bug wearing two hats: a ±120-char window routinely spans two
sentences, and *first match* is not the same question as *which operation is being licensed*.
Proximity answers the right question and is what the shipped script does.

There is also one thing no rule can decide, now handled by declaring it rather than guessing:
after sandhi, **`aḍ-abhāva` and `āḍ-abhāva` are orthographically identical** — इत्यत्र +
अडभाव and ङिताम् + आडभाव both surface as …ाडभाव. The `āḍ` reading is therefore claimed only
on the unfused word-initial form; fused hits default to the far commoner `aḍ`; and the one
genuine fused `āḍ` (MBh 1.32.24, decided by its `ङिताम्` → Pāṇini 7.3.112 *ṅiti āṭ*) is a
hand ruling with that reasoning written down.

### 5.2 The discriminator that does hold

**A named grammatical operation standing beside the licence word is very nearly a perfect
discriminator on this corpus** — 150 of the 151 rows where a rule found one are genuine, and
13 of the 14 rejects are rows where no rule found one. The single exception in each direction
is MBh 5.70.7, and it is instructive: the term was there, it just belonged to a neighbouring
sentence. The automatic pass is not "75 % of the work at 75 % accuracy" as the handoff
budgeted; it is a clean partition with one seam, and the hand queue is the ambiguous residue
rather than a quarter of the corpus.

### 5.3 The homonym the probe cleared does fire

H1324 §5 warned that *ārṣa* as one of the eight marriage rites "will pollute every grep"; the
probe found **zero** and concluded the guard "turns out not to bind for this corpus". At full
MBh scale it binds: six hits, every one in a dharma passage, four of them quoting Āśvalāyana's
list verbatim (`गोमिथुनं दत्वोपयच्छेत स आर्षः`). The probe's corpus — the Gītā and two
upākhyānas — contained no dharmaśāstra, which is why it saw none. A vocabulary guard cleared on
a narrative sample is not cleared for the Anuśāsanaparvan.

Eight further rejects are *ārṣa* in its plain sense, glossing the commented verse's own word:
"beneficial to the ṛṣis" (12.12.17), "the Veda" (12.268.10 and 5.70.7), "composed by the
ṛṣis" (1.77.18), "by the ṛṣi-like vision of non-difference" (3.91.24). One (12.132.17) is a
ṭīkā truncated in the source to the two characters `आर्षं -`.

Every rejection carries its reason and its quotation in
[nilakantha_licence_rejected.tsv](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/licence_register/nilakantha_licence_rejected.tsv),
and the ruling that produced it in
[nilakantha_hand_rulings.json](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/licence_register/nilakantha_hand_rulings.json).

## 6. Scale — the probe's estimate was 3–6× high, and the better predictor was already visible

The feasibility report put the full register in the "high hundreds to low thousands". It is
**151**. Both of its own numbers were in the report; only one of them extrapolated:

| Basis | Nala rate | × corpus | Predicted | Actual |
|---|---|---|---:|---:|
| per ṭīkā **character** | 4 / 111 861 chars | × 2 989 325 chars | **107** | 165 raw / 151 kept |
| per ṭīkā **shloka** (implicit) | 4 / ~300 shlokas | × 24 694 shlokas | ~330 → "high hundreds" | 151 |

The character-rate prediction was within a factor of 1.5; the shloka-rate one was 2× high and
the prose around it stretched further. **Quote densities per character, not per verse, when
verse-length varies by a factor of thirty across a corpus** — bhīṣma's ṭīkā averages 299
characters per glossed shloka, śalya's 55.

This is a correction to an estimate, not to the project: 151 rows is a usable dataset, and the
inter-commentator agreement in §7 is what makes it citable.

## 7. Step 5: the Gītā rows and the agreement column

The 27 rows of the H1324 probe are folded into
[commentary_licence_register_combined.tsv](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/licence_register/commentary_licence_register_combined.tsv)
(**178 rows**) keeping the multi-commentator agreement signal: `agreement_n` and
`agreement_commentators` per row. Eight of the 27 Gītā rows are attested by two or three
commentators at the same verse — three at BhG 11.41, three at 11.48, two each at 10.24, 11.35,
11.37, 11.44, 14.23, 16.1.

`agreement_n` is **1 for every Nīlakaṇṭha row, by construction and not by measurement**: the
vulgate has one commentator. The column is not a quality score and must not be read as one —
it says "how many independent commentators flagged this deviation", and a single-commentator
corpus can only ever say one. Corroboration remains the Gītā slice's contribution to the
combined table.

## 8. What is in the register

[commentary_licence_register_nilakantha.tsv](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/licence_register/commentary_licence_register_nilakantha.tsv)
· `.jsonl`. Columns: `row_id, source, work, locus, locus_id, parva, commentator, term_family,
defense_term, deviation_type, deviation_term_sa, classification, agreement_n,
agreement_commentators, quote`.

`locus` is the human form (`MBh 12.284.141`), `locus_id` the scrape's addressable
`P12_U03_A284_S141` — the two are kept separate because only the second round-trips to the
source.

Term split: **121 `ārṣa` · 30 `chāndasa`**. The commonest deviation types:

| Rows | `deviation_type` |
|---:|---|
| 21 | absence of the *aṭ* augment (`aḍ-abhāva`) — the augmentless imperfect, the single commonest epicism |
| 12 | elision — segment/affix |
| 9 | elision — case ending (`vibhakti-lopa`) |
| 7 | voice — ātmanepada for parasmaipada (`taṅ-bhāva`) |
| 6 | elision — segment/syllable (`varṇa-lopa`) |
| 5 | transfer — gender (`liṅga-vyatyaya`) |
| 5 | elision (unspecified) |
| 4 | elision — reduplication syllable (`abhyāsa-lopa`) |
| 4 | sandhi |
| 3 | absence of an expected elision (`lopa-abhāva`) |

59 distinct types over 151 rows: the tail is long, and that is the shape of the phenomenon, not
of the method. Five rows carry a deliberately coarse "elision" where Nīlakaṇṭha names *lopa*
without saying of what; sharpening those means reading the two forms he contrasts, which is the
same work as §10's sūtra layer.

## 9. Human gating

46 cards, Russian, generated with the shared
[csl-pyutil](https://github.com/sanskrit-lexicon/csl-pyutil) emitter:
`review/commentarystrategies-nilakantha-licence_h2860_review.html` (gitignored — a working
artifact, not a deliverable). 16 hand rulings + the 30-row auto-typed sample; each card states
what approving and rejecting will actually do to the register and to the precision figure, and
its header links to the verse on sanatana.in.

Nothing in this report waits on that vote. The register is committed and usable now; the sheet
decides whether 14 rejected rows come back and whether the two hand-assigned types stand.

## 10. Open questions this build did NOT answer

Both are the handoff's own, and both remain open because they are scope calls, not measurements:

- **Who is the consumer** (H1324 §6 Q4). A human should decide. The register as built serves
  the first two answers — a labelled evals slice and a citable dataset — at full completeness.
  It does **not** serve the third: no row is tied to a Pāṇini sūtra number. That work is real
  and was deliberately not started; `deviation_term_sa` (`aḍ-abhāva`, `supāṃ suluk`,
  `liṅga-vyatyaya`) is the join key a sūtra layer would use, and 56 distinct terms is the size
  of that job.
- **Both epics or one** (Q1). MBh is done; Govindarāja on the Rāmāyaṇa is still scan-only and
  still deferred.

## 11. Reproduce

```sh
python mahabharata-nilakantha/nilakantha_parser.py scrape      # ~107 requests, 1 s apart
python scripts/build_licence_register_nilakantha.py
python scripts/build_licence_register_review_sheet.py
```

The scrape output (58.9 MB) stays gitignored on rights grounds, unchanged from the posture set
on 11-07-2026: derived rows are the release-eligible artifact, bulk source text is not, and any
publication goes through
[/publish-safety-check](https://github.com/gasyoun/claude-config/blob/main/commands/publish-safety-check.md).
The build fails loudly if the scrape is absent rather than emitting an empty register — the
lesson of §2 applied to this repo's own tooling.

_Dr. Mārcis Gasūns_

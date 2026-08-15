# Feasibility — a register of tradition-attested Pāṇini deviations from epic commentaries

_Created: 15-08-2026 · Last updated: 15-08-2026_

**Verdict: GO**, with a scope correction that matters more than the verdict.

Probe report for [H1324](https://github.com/gasyoun/Uprava/blob/main/handoffs/H1324-Opus_CommentaryStrategies_mbh-ramayana-commentary-parsing-feasibility_19.07.26.md)
§5 — can the Mahābhārata / Rāmāyaṇa commentaries be parsed into a base of the cases where a
traditional commentator himself licenses a deviation from Pāṇini (*ārṣa prayoga*)? Run
15-08-2026, Opus 5 (`claude-opus-5`). Origin: MG's note on the
`review-vedic-r02-adjudication` sheet, 19-07-2026; hypothesis `R2607-05` in
[QUESTIONS_LOG.md](https://github.com/gasyoun/Uprava/blob/main/QUESTIONS_LOG.md).

## The headline, in one paragraph

The probe was expected to be a narrow, low-precision sounding on a slice of the corpus. It
came back at **100 % precision on 31 of 31 hand-checked hits**, across two independent
sources and two scripts, with **locus alignment costing nothing** — and the handoff's single
worst finding, that Nīlakaṇṭha exists only as page scans, turns out to be **false**. What the
probe actually found is that this dataset is not a research programme; it is roughly a week
of careful work.

## 1. What was measured

| | Source | Format | Commentators | Size probed |
|---|---|---|---|---|
| A | [GRETIL `sa_bhagavadgItA-4comm`](https://gretil.sub.uni-goettingen.de/gretil/corpustei/sa_bhagavadgItA-4comm.xml) | TEI XML, IAST | Śrīdhara, Madhusūdana, Viśvanātha, Baladeva | 1,741,192 chars |
| B | [`mahabharata-nilakantha/MBh-Nalopakhyanam-Nilakantha.md`](https://github.com/gasyoun/CommentaryStrategies/blob/main/mahabharata-nilakantha/MBh-Nalopakhyanam-Nilakantha.md) | Markdown, Devanāgarī | **Nīlakaṇṭha** (*Bhāratabhāvadīpa*) | 111,861 chars |
| B′ | [`MBh-Ramopakhyanam-Nilakantha.md`](https://github.com/gasyoun/CommentaryStrategies/blob/main/mahabharata-nilakantha/MBh-Ramopakhyanam-Nilakantha.md) | Markdown, Devanāgarī | Nīlakaṇṭha | 77,508 chars |

## 2. Precision — the number the GO/NO-GO rests on

### 2.1 The pattern defect that must not be mistaken for a finding

A naïve `ārṣ\w*` grep returns 43 hits on source A. Twenty-seven of them are **substring
noise** — `pārṣada` (attendant), `mā kārṣīr` (aorist of √kṛ), `dvādaśa-vārṣika`
(twelve-yearly). That is a defect of the regex, not a property of the corpus, and any
precision figure quoted from an unanchored grep is meaningless. Anchoring the match to a word
or compound boundary (start-of-string, whitespace, or a hyphen — Sanskrit compounds mean a
licence term legitimately follows a hyphen) removes all 27.

### 2.2 Hand-classified results, word-anchored

| Term | Source | Raw hits | Genuine licence-claims | Precision |
|---|---|---:|---:|---:|
| `ārṣa` | A (Gītā, 4 comm.) | 16 | **16** | **100 %** |
| `chāndasa` | A | 11 | **11** | **100 %** |
| `pramāda` | A | 56 | **0** | **0 %** |
| `आर्ष` | B (Nīlakaṇṭha, Nala) | 3 | **3** | **100 %** |
| `छान्दस` | B | 1 | **1** | **100 %** |
| `प्रमाद` | B | 0 | — | — |
| any | B′ (Nīlakaṇṭha, Rāma) | 0 | — | — |
| **total classified** | | **31** | **31** | **100 %** |

Against the §5 threshold — "if precision is under ~30 %, the answer is NO-GO-as-specified" —
this is not a marginal pass.

### 2.3 The two vocabulary findings

**`pramāda` must be dropped from the licence vocabulary.** All 56 hits in the Gītā
commentaries carry the *moral* sense — heedlessness, negligence, the `pramāda` of
[YogaS 1.30]'s list of obstacles, `apramādinam` "attentive". Not one is a claim about a
grammatical form. Keeping `pramāda` in the grep would have dragged aggregate precision from
100 % to 36 % and buried the real signal in devotional prose. This directly answers §6 Q2
with data instead of authority: **the narrow closed set (`ārṣa`, `chāndasa`) is the right
vocabulary**, and the broad set is not a trade-off between precision and recall — it is
simply worse.

**The homonym the handoff flagged up front never fired.** §5 warned that *ārṣa vivāha*, ārṣa
as a marriage type, "will pollute every grep". It produced **zero** hits in either source,
because that sense lives in dharmaśāstra, not in epic or Gītā commentary. The guard was
correct to state, and turns out not to bind for this corpus — worth knowing before anyone
budgets for filtering it.

## 3. §3a is wrong — Nīlakaṇṭha is machine-readable and already in this repo

The handoff's §3a calls this "the headline finding" and "bad news that reshapes the whole
project":

> **Nīlakaṇṭha's *Bhāratabhāvadīpa* — the flagship Mahābhārata commentary, the single richest
> source of ārṣa-defenses — exists ONLY as page scans.** … any MBh-commentary corpus work
> means **OCR from the Chitrashala plates**, not grepping.

That was already false when it was written. Eight days earlier, on **11-07-2026**, a session
in this same repository scraped the entire Nīlakaṇṭha vulgate — mūla **plus** ṭīkā — from
[sanatana.in/mahabharata](https://sanatana.in/mahabharata/) via
[`nilakantha_parser.py`](https://github.com/gasyoun/CommentaryStrategies/blob/main/mahabharata-nilakantha/nilakantha_parser.py),
and recorded the result in
[`NILAKANTHA_VULGATE_CENSUS.md`](https://github.com/gasyoun/CommentaryStrategies/blob/main/mahabharata-nilakantha/NILAKANTHA_VULGATE_CENSUS.md):

> **83,971 shlokas** across all 18 parvans, **24,694 of them carrying ṭīkā** (29.4 %), 2,110
> adhyāyas, per-verse P/U/A/S addressing, deduplicated clean.

The bulk text (`nilakantha_vulgate_full.jsonl`, 58.9 MB) is gitignored for rights and is not
currently on disk, so it needs one re-run of the scraper — but that is a scripted afternoon,
not an OCR programme, and the census proves the endpoint and the parser both work. The two
committed upakhyāna extracts were enough to probe the commentator directly, which is what
§5 step 1 actually asked for ("whichever … is genuinely available as plain text").

**Consequence:** the §6 Q3 fork — "(a) stop with NO-GO, (b) run the SamudraManthanam OCR
pipeline, (c) narrow to machine-readable and declare coverage incomplete" — **dissolves**.
None of the three applies. The flagship source is machine-readable, so the project can be
built at full MBh scope without OCR and without a coverage apology.

## 4. Locus alignment costs nothing — the feared tax is not there

§4.2 named locus alignment, not parsing, as "the real tax … where an unbudgeted project
dies", because Nīlakaṇṭha follows the vulgate while the machine-readable MBh is the BORI
critical edition.

For the two sources probed, that tax is **zero**, for the same structural reason in both
cases: **the commentary is stored interleaved with the verse it comments on**. In source A
the TEI carries inline `BhG 11.41` markers, so every hit's locus is the nearest preceding
marker. In source B the ṭīkā follows its verse and the verse number sits in the `॥३४॥`
marker, and the scrape's own P/U/A/S addressing is per-verse by construction. No alignment
step, no fuzzy pratīka matching, no edition crosswalk.

The vulgate-vs-critical problem is real, but it is a **different** problem: it only appears
if the register must be *joined to the BORI critical edition*, which is a downstream
consumer's requirement, not the register's own. The register is internally consistent in its
own recension. That reframing is the single biggest cost change the probe produced.

## 5. The dataset the probe actually produced

Not one row end-to-end, as §5 step 4 asked — all 27 rows from source A, in the §2 shape:
[`data/licence_register/commentary_licence_register_bhagavadgita_probe.tsv`](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/licence_register/commentary_licence_register_bhagavadgita_probe.tsv)
(+ `.jsonl`).

| # | locus | commentator | defense_term | deviation_type |
|---|---|---|---|---|
| 1 | BhG 4.24 | Baladeva | `chāndasaḥ` | elision (`ṇi-kāra-lopa`) |
| 2 | BhG 6.25 | Madhusūdana | `cchāndasaṃ` | vowel lengthening (`dairghya`) |
| 3 | BhG 6.39 | Baladeva | `ārṣam` | gender (neuter, `klībatvam`) |
| 4 | BhG 9.3 | Baladeva | `ārṣī` | case (objective genitive, `karmaṇi ṣaṣṭhī`) |
| 5 | BhG 10.24 | Viśvanātha | `ārṣam` | form of `senānīnām` |
| 6 | BhG 10.24 | Baladeva | `ārṣaḥ` | augment (`nuḍāgama`) |
| 7 | BhG 10.29 | Baladeva | `ārṣaḥ` | absence of the `ch`-substitution |
| 8 | BhG 11.8 | Madhusūdana | `chāndas` | class-transfer of `√śak` |
| 9 | BhG 11.35 | Viśvanātha | `ārṣam` | absolutive `namaskṛtvā` |
| 10 | BhG 11.35 | Baladeva | `ārṣam` | absolutive `namaskṛtvā` |
| 11 | BhG 11.37 | Viśvanātha | `ārṣam` | voice (ātmanepada) |
| 12 | BhG 11.37 | Baladeva | `chāndasam` | voice (ātmanepada) |
| 13 | BhG 11.41 | Śrīdhara | `ārṣam` | sandhi |
| 14 | BhG 11.41 | Viśvanātha | `ārṣaḥ` | sandhi |
| 15 | BhG 11.41 | Baladeva | `chāndasaḥ` | sandhi |
| 16 | BhG 11.44 | Madhusūdana | `chāndasaḥ` | sandhi + `iva`-elision |
| 17 | BhG 11.44 | Viśvanātha | `ārṣaḥ` | sandhi |
| 18 | BhG 11.48 | Madhusūdana | `chāndasaḥ` | visarga elision |
| 19 | BhG 11.48 | Viśvanātha | `ārṣau` | two elisions |
| 20 | BhG 11.48 | Baladeva | `chāndasaḥ` | visarga elision |
| 21 | BhG 12.8 | Baladeva | `chāndasam` | form of `nivasiṣyasi` |
| 22 | BhG 13.12 | Śrīdhara | `chāndasaḥ` | suffix (`matup` after a bahuvrīhi) |
| 23 | BhG 14.22 | Viśvanātha | `ārṣam` | gender (neuter ending) |
| 24 | BhG 14.23 | Śrīdhara | `ārṣam` | voice (parasmaipada) |
| 25 | BhG 14.23 | Viśvanātha | `ārṣam` | voice (parasmaipada) |
| 26 | BhG 16.1 | Śrīdhara | `ārṣaḥ` | elision (`avarṇa-lopa`) |
| 27 | BhG 16.1 | Baladeva | `chāndasaḥ` | elision (`pa-lopa`) |

Plus the four Nīlakaṇṭha rows from source B: `आर्षः संधिः` (Nala ॥३॥, sandhi),
`णिजभाव आर्षः` (॥३४॥, absence of the causative `ṇic`), `अभ्यासलोप आर्षः` (॥११४॥,
reduplication-syllable elision), `छान्दसं टाबन्तत्वम्` (॥१४॥, the `ṭāp` ending).

`deviation_type` is proposed mechanically from the grammatical noun the commentator himself
names beside the licence word; 20 of 27 classify automatically and 7 need a philologist's
eye. That ratio is the honest division of labour for the build.

### 5.1 The finding nobody asked for: independent corroboration is free

Because source A carries **four commentators over one text**, the same deviation gets flagged
by more than one of them at the same verse: three at BhG 11.41, three at 11.48, two each at
10.24, 11.35, 11.37, 11.44, 14.23 and 16.1. **Eight of the 27 rows are multiply attested.**
The register therefore ships with an inter-commentator agreement signal at no extra cost —
which is exactly the evidence a reviewer will demand, and exactly what a single-commentator
corpus could never provide. It also shows the vocabulary is genuinely interchangeable in
practice: at BhG 11.41 Śrīdhara and Viśvanātha say `ārṣa` where Baladeva says `chāndasa` for
the same sandhi, and at 11.44 the pair swaps round.

## 6. Scale

Measured density in Nīlakaṇṭha's Nala ṭīkā: 4 claims in 111,861 chars. Against the census's
**24,694 ṭīkā-bearing shlokas**, a claim rate of this order puts the full Nīlakaṇṭha register
in the **high hundreds to low thousands** of rows. State that as an order of magnitude, not a
forecast: source B′ (Rāmopākhyāna) returned **zero** hits over 77,508 chars, so density
varies by parvan and by how grammatical Nīlakaṇṭha is feeling — a real property, and a
per-parvan census is the first thing the build should measure rather than assume.

## 7. Rights

- Source A, GRETIL: licence "not stated" (per the handoff's own §3a table). The register
  stores derived rows plus short quotations for citation, which is ordinary scholarly use.
- Source B, sanatana.in / Sanatana Sampatti: the 11-07-2026 scrape already treats bulk text
  as **gitignored, publication-gated** — that posture carries over unchanged and this report
  does not widen it.
- Per org standing policy, rights **uncertainty is not a stop** and no `@DECIDE` is opened for
  greyness. Any *publication* of the register goes through
  [`/publish-safety-check`](https://github.com/gasyoun/claude-config/blob/main/commands/publish-safety-check.md)
  at release time. The derived-rows-only bundle is the publishable artifact; bulk source text
  is not.
- The BORI critical edition and its apparatus stay local-only per
  [`BORI_CRITICAL_SOURCE.md`](https://github.com/gasyoun/CommentaryStrategies/blob/main/mahabharata-nilakantha/BORI_CRITICAL_SOURCE.md)
  — untouched by this probe, and another reason §4's alignment problem should be treated as a
  downstream join rather than a core requirement.

## 8. Costed plan

| Step | What | Cost |
|---|---|---|
| 1 | Re-run `nilakantha_parser.py scrape` to restore `nilakantha_vulgate_full.jsonl` | scripted, one run |
| 2 | Word-anchored `आर्ष`/`छान्दस` sweep over all 24,694 ṭīkā shlokas; per-parvan density census | hours |
| 3 | Auto-fill `locus` (P/U/A/S, free) + `commentator` (Nīlakaṇṭha, constant) + `defense_term` | mechanical |
| 4 | `deviation_type`: ~75 % auto from the named grammatical noun, ~25 % by hand | the real work |
| 5 | Fold in source A's 27 Gītā rows, keeping the multi-commentator agreement column | trivial |
| 6 | Extend to Govindarāja on the Rāmāyaṇa | **scan-only — deferred, not blocking** |
| 7 | `/review-sheet` over the hand-classified rows; publish-safety-check; release | standard |

Step 6 is where the original OCR fear survives, and it now scopes down to one commentator on
one epic instead of gating the entire project.

## 9. What still needs a human

The §6 questions were framed as blocking the build. Three are now answered by measurement,
and the remaining two are genuine scope calls:

| Q | Question | Status |
|---|---|---|
| 1 | Both epics or one? | **A human should decide.** The probe makes MBh/Nīlakaṇṭha clearly the cheaper and richer lane; Rāmāyaṇa/Govindarāja is still scan-only. Recommended: MBh first, Rāmāyaṇa as a later wave. |
| 2 | Narrow or broad licence vocabulary? | **Answered by §2.3** — narrow (`ārṣa`, `chāndasa`). `pramāda` is 0/56. |
| 3 | What if only scans? | **Dissolved by §3.** Nīlakaṇṭha is machine-readable. |
| 4 | Who is the consumer? | **A human should decide.** This one still drives the shape: a RuWritingStyles evals slice wants a small labelled set, a `CommentaryStrategies` dataset/paper wants completeness and citability, a `SanGram` reference layer wants each row tied to a Pāṇini sūtra — and only the third makes step 4 expensive. |
| 5 | Which edition for page-level citation? | Partly answered: source A cites by BhG verse and source B by vulgate P/U/A/S, both verifiable without page numbers. A print edition is still wanted for a journal submission. |

Nothing above blocks starting steps 1–3, which is why the build handoff is minted rather than
parked.

## 10. Reproduce

```
python scripts/probe_licence_vocabulary.py <source> <hits.json>
```

Fetch of source A: `https://gretil.sub.uni-goettingen.de/gretil/corpustei/sa_bhagavadgItA-4comm.xml`
(200, 2,056,476 bytes, 15-08-2026). Whole probe — fetch, grep, hand-classify 31 hits, emit the
27-row table — ran inside a single session.

_Dr. Mārcis Gasūns_

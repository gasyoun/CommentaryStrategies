# H4738 — Samsaadhanii Sundarakāṇḍa treebank ingest parity report

_Created: 2026-09-16 · tier: OxAlpha (opencode/z-ai/glm-5.3-flash) · VALIDATION-ONLY · RELABELED 2026-09-16 (MG ruling а)_

## Inputs (provenance)

| input | sha256 (first 12) | note |
|---|---|---|
| SCL `samsaadhanii/datasets` `Annotated-data/Sundarakanda.csv` (no LICENSE upstream) | `eed7e126b86b` | 38126 word rows, tab-separated, 14 cols, WX notation |

## Result — sentence-count parity (DoD gate, anvaya_no basis)

Sentence identity is the upstream `anvaya_no` column (`N.M` = sentence.word):
one sentence = (book, chaptno, N).

| metric | value |
|---|---|
| word rows (csv-module walk) | 38126 |
| unannotated rows (anvaya_no='-': punctuation/interpolations) | 5 (lines 14, 723, 7514, 18841, 18855) |
| total non-header lines (raw census) | 38131 |
| **sentences (anvaya_no → book, chaptno, N)** | **1742** |
| verse pairs (chaptno × slokano) | 2198 |
| distinct slokano labels | 576 |
| sargas | 62 |
| rows per sarga (min–max) | 155–2864 |
| ingested layer emitted | yes (local-only, outside repo) |
| layer record recount | 1742 |
| layer token sum | 38126 |

**Relabel note (2026-09-16, MG ruling а on verifier DISAGREE).** The
previously reported «92 sentences» counted (book, chaptno, sentno) buckets.
`sentno` is a chapter-level constant, not a sentence id: 44
of 62 chapters carry `sentno=1` on every row, and the
largest single bucket holds 2864 words.
Those buckets are recorded below only as a labeled artifact; the DoD metric
is the anvaya_no sentence count.

| degenerate sentno artifact | value |
|---|---|
| (book, chaptno, sentno) buckets | 92 (= 62 chapters + 30 extra sentno buckets) |
| chapters with sentno always 1 | 44 / 62 |
| max tokens in one bucket | 2864 |

**Parity verdict: PASS** — three non-vacuous cross-checks: word rows +
unannotated rows == raw line census (38126 + 5 == 38131);
emitted-layer record count == distinct source anvaya sentences
(1742 == 1742);
emitted-layer token sum == word rows (38126 == 38126).
Every row passed the 14-column schema and identity checks; malformed rows
abort with a loud FAIL (none fired).

## Rosette (aggregate-only, first words ≤5 per sentence, 3 sentences)

⚠️ WX `f` is ambiguous in this dataset: standard vocalic ṛ AND pre-stop
nasal. Derived census (all 38131 data
rows): substring `lafk` in any cell — 139 rows
(incl. `alafkArAm` = alaṅkāram, unrelated to Laṅkā); exact word `lafkAm` —
55 rows (= **laṅkām**, lemma `lafkA` tagged
`swrI` feminine); word cells containing `lafkA` —
117 rows; zero `laMk` spellings. The literal table
renders it ṛ — word-level IAST below is indicative, not authoritative; any
future WX layer needs a context-resolved converter (sanskrit_util + WX
mode), not this table.

| sarga.anvaya | slokano | first words (WX) | IAST |
|---|---|---|---|
| 001.1 | 001 | AnupUrvyeNa ApAwe Asye BImam BUyaH | ānupūrvyeṇa āpāte āsye bhīmam bhūyaḥ |
| 001.2 | 001 | AkASa- Alokayan AviRtam BakRyaH SEla- | ākāśa- ālokayan āviṣṭam bhakṣyaḥ śaila- |
| 001.3 | 001 | AsAxiwaH AsWAya AvixXam AyawA BakRyAn | āsāditaḥ āsthāya āviddham āyatā bhakṣyān |

## Residue

- Upstream carries **no LICENSE**: the row-level layer is deliberately NOT
  committed — regenerable via this script + a fresh clone of
  samsaadhanii/datasets. Rights follow-up belongs to the estate
  license-gated-ingest discipline (ask upstream before any redistribution).
- 5 upstream quirk rows carry `anvaya_no='-'` (4 punctuation '.'-word rows,
  1 annotated interpolation `(xaxarSa)` with real morphology, lines listed
  above); excluded from token counts, included in the line census.
- Two merged-verse `slokano` forms (`002-003`, `026_2_027_1`) kept as-is —
  verse stats use upstream labels verbatim.
- Morphology/kāraka columns validated structurally only (non-empty,
  well-formed identity fields); semantic gold-quality judgement is out of
  scope for this pilot.

## Reproduce

```
git clone --depth 1 https://github.com/samsaadhanii/datasets /tmp/h4738-samsaa
python3 scripts/ingest_samsaadhanii_sundara_treebank.py \
    --datasets-dir /tmp/h4738-samsaa \
    --outdir data/analysis/samsaadhanii_sundara_treebank \
    --emit-layer /tmp/h4738-layer
```

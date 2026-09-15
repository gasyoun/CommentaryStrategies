# H4738 — Samsaadhanii Sundarakāṇḍa treebank ingest parity report

_Created: 2026-09-15 · tier: OxAlpha (opencode/z-ai/glm-5.3-flash) · VALIDATION-ONLY_

## Inputs (provenance)

| input | sha256 (first 12) | note |
|---|---|---|
| SCL `samsaadhanii/datasets` `Annotated-data/Sundarakanda.csv` (no LICENSE upstream) | `eed7e126b86b` | 38126 word rows, tab-separated, 14 cols, WX notation |

## Result — sentence-count parity (DoD gate)

| metric | value |
|---|---|
| word rows (csv-module walk) | 38126 |
| unannotated rows (anvaya\_no='-': punctuation/interpolations) | 5 (lines 14, 723, 7514, 18841, 18855) |
| total non-header lines (raw census) | 38131 |
| **sentences (book, chaptno, sentno)** | **92** |
| verses (ślokas) | 85 |
| sargas | 62 |
| rows per sarga (min–max) | 155–2864 |
| ingested layer emitted | yes (local-only, outside repo) |
| layer sentence recount | 92 |

**Parity verdict: PASS** — word rows + unannotated rows == raw line
census, sentence groups recount identically, and the emitted layer (when
emitted) recounts to the same sentence count. Every row passed the 14-column schema and identity checks;
malformed rows abort with a loud FAIL (none fired).

## Rosette (aggregate-only, rosette words ≤5 per sentence, 3 sentences)

⚠️ WX `f` is ambiguous in this dataset: standard vocalic ṛ AND, 139×,
pre-stop nasal (lafkAm = **laṅkām**, lemma `lafkA` tagged `swrI` feminine;
zero `laMk` spellings). The literal table renders it ṛ — word-level IAST
below is indicative, not authoritative; any future WX layer needs a
context-resolved converter (sanskrit_util + WX mode), not this table.

| sarga.śloka | first words (WX) | IAST |
|---|---|---|
| 001.001 | wawaH rAvaNa- nIwAyAH sIwAyAH Sawru- | tataḥ rāvaṇa- nītāyāḥ sītāyāḥ śatru- |
| 002.001 | saH svasWaH xaxarSa ha sAgaram | saḥ svasthaḥ dadarśa ha sāgaram |
| 003.001-002.1 | saH niSi lafkAm mahA- sawwvaH | saḥ niśi laṛkām mahā- sattvaḥ |

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

# H2677 — unlabeled CS notes inventory

_Created: 14-08-2026 · Last updated: 14-08-2026_

W1-CS inventory for [H2677 (Grok 4.6) — W1 Flash IAA on unlabeled CS notes](https://github.com/gasyoun/Uprava/blob/main/handoffs/H2677-Grok_CommentaryStrategies_deepseek-w1-cs-unlabeled-axes_13.08.26.md).
Gold 300 is skipped. IAA `sources/{tr}_notes.json` is already the gold sample.

## IAA pipeline (sources → data/*_full.json)

| translator | source n | already in *_full.json | unlabeled |
|---|---:|---:|---:|
| kalyanov | 50 | 50 | 0 |
| vassilkov | 50 | 50 | 0 |
| erman | 50 | 50 | 0 |
| grintser | 50 | 50 | 0 |
| syrkin | 50 | 50 | 0 |
| leonov | 50 | 50 | 0 |

Total source=300; already labelled=300; unlabeled in this format=0.

## Unlabeled remainder (this pass)

Machine-readable translator notes with `raw_text` and **no** `axis_2`/`axis_4`, not in the gold 300:

| pile | n |
|---|---:|
| [data/leonov_own_notes.json](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/leonov_own_notes.json) notes | 1058 |
| already had axes | 0 |
| gold-text overlap (skipped) | 0 |
| empty raw_text | 0 |
| **Flash worklist** | **1058** |

Year-1 pending source files (no file on disk — parked, D21): `sementsov_notes.json`, `burba_notes.json`, `petrov_notes.json`, `smirnov_notes.json`, `blinderman_notes.json`.

Already-typed layers (not unlabeled; not this pass): data/sundara_ch*_commentary_to_add.json (type А/В/…); data/hist_cultural/ch*.json (type Г); data/lexical/ch*.json (lexical layer).

## Gold 300 SHA-256 (must stay unchanged)

| file | sha256 |
|---|---|
| `kalyanov_full.json` | `187ea18b8f7439f58790ec736f5bbf8ff109b95c26a1a4bb798e902d2a1808c3` |
| `vassilkov_full.json` | `efc353188c21324eff88eb83e872d9de9940ae571a73ba2b8b2f62d42af92838` |
| `erman_full.json` | `870b9e0f3fa8bc0f587a5884267e72a739fc256eb7eb2fe6a148651a576c78cb` |
| `grintser_full.json` | `6c8af7aca863e540cbfc4fb8169d45740fa951e2d13455ac7457c729277cefbc` |
| `syrkin_full.json` | `3285ac7ed06c17d5acee63f09d43ba9c6aa21a4b1b91cfde358090cdbe319b86` |
| `leonov_full.json` | `73bdca02533b847168e9e95a00ad0e1ea1cbf0aba7d5c1ddecbcc29ece3649e1` |
| `kalyanov_markup_50.json` | `da3c11b6bd0f16f2c1d3f508dec0e03af7e88a7803fb01baf3b2dee11ff6d441` |
| `vassilkov_markup_50.json` | `529dd2f7a29cc88171d5428d06e090cd5e396e8ef94f7878dd6325a58036b439` |
| `erman_markup_50.json` | `9b3e19cbcc73eaae9f1aa0e02a02dfbb4a1b5662de4f8c1e15970f3c91c2d709` |
| `grintser_markup_50.json` | `0d16caa89ff351c2ed01831458d1d5c731a60943708a0d53f9669635c698a3ca` |
| `syrkin_markup_50.json` | `9ef317c4b36398dab55ace387e7712631d80ee6b86cd10c88abc494e3e176991` |
| `leonov_markup_50.json` | `4a824b1cb239684a3f346e84273743b9aaa39143217504a49cf4b2cc232f9a0c` |

_Dr. Mārcis Gasūns_

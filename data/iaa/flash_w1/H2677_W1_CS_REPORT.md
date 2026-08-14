# H2677 — W1 Flash IAA unlabeled CS notes

_Created: 14-08-2026 · Last updated: 14-08-2026_

Run UTC: 2026-08-14 00:04Z. Model `deepseek-v4-flash` @ `https://api.deepseek.com`. Executor Grok 4.6 (`grok-4.6`).

## Counts

| item | n |
|---|---:|
| IAA source notes (gold sample) | 300 |
| already in DeepSeek/IAA `*_full.json` | 300 |
| unlabeled in IAA sources | 0 |
| leonov_own worklist | 1058 |
| labelled this file | 1058 |
| schema-valid | 1058 |
| schema-invalid | 0 |
| API calls | 1059 |
| API errors | 1 |
| error rate | 0.0009 |
| prompt tokens | 3803187 |
| completion tokens | 94771 |
| reasoning tokens | 512 |
| **cost USD** (pre-16-08 Flash card) | **0.5590** |

Schema-valid %: 100.0%

The one API error is the first smoke call (`max_tokens=512` with default-on thinking, empty `content`). The job then pinned `thinking: disabled` + `json_object` and labelled all 1058 with 0 errors.

## Axis distribution (this remainder, n=1058)

| axis | value | n | share |
|---|---|---:|---:|
| axis_2 | A | 468 | 44.2% |
| axis_2 | B | 444 | 42.0% |
| axis_2 | V | 136 | 12.9% |
| axis_2 | G | 10 | 0.9% |
| axis_4 | P | 1045 | 98.8% |
| axis_4 | K | 9 | 0.9% |
| axis_4 | D | 4 | 0.4% |

Not a κ re-gate. Sidecar only — do not fold into the gold 300.

## Gold 300 hashes

Unchanged: **yes**

| file | sha256 after |
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

Gold `data/{tr}_full.json` / `{tr}_markup_50.json` were not opened for write.
Anthropic `annotate_batch.py --backend anthropic` was not used.

_Dr. Mārcis Gasūns_

# Sundara apparatus — vendored, canonical home moved

_Created: 16-09-2026 · Last updated: 16-09-2026_

The Sundarakāṇḍa commentary apparatus family in this directory (and in
`data/apparatus/`, `data/valmiki_shlokas/kanda_5_sundarakanda/`) is now a
**vendored read-only copy**. The canonical source of truth moved to
[`gasyoun/Sundara-commentaries`](https://github.com/gasyoun/Sundara-commentaries)
(H4849, MG ruling 14-09-2026, census B4).

## Why the copy stays here

~70 scripts under [`scripts/`](https://github.com/gasyoun/CommentaryStrategies/tree/main/scripts)
and [`tests/`](https://github.com/gasyoun/CommentaryStrategies/tree/main/tests) have hard build
dependencies on these exact `data/` paths (`sundara_ch*_commentary_to_add.json`,
`apparatus/sarga_*.json`, `valmiki_shlokas/kanda_5_sundarakanda/*`, etc.). Repointing
every reader to the new repo in one pass was out of scope for H4849's time budget and
too risky to do unverified. Per the handoff's own escape clause — "only if a hard
build dependency blocks, vendored read-only copy marked vendored" — this directory
stays as the working copy CommentaryStrategies' pipeline actually reads.

## Files covered by this marker

- `sundara_ch*_commentary_to_add.json` (68 files, ch1–ch68)
- `sundara_commentary_to_add.json`
- `leonov_sundara_ch1_candidates.json`
- `sundara1_pilot_c3_20.json`
- `sundara_book_stats.json`
- `typed_link_sundara_concordance.*`
- `apparatus/` (sarga reviewer manifests, `gate_ledger.json`, `gate_disagreements.*`, `adjudication_policy.json`)
- `valmiki_shlokas/kanda_5_sundarakanda/`

Verified byte-identical (sha256 parity, 428/428 files) against
[`Sundara-commentaries` `data/`](https://github.com/gasyoun/Sundara-commentaries/tree/main/data)
at move time (16-09-2026). Edge registered in
[Uprava interlinks_edges.tsv](https://github.com/gasyoun/Uprava/blob/main/interlinks_edges.tsv)
(`Sundara-commentaries` → `CommentaryStrategies`, kind `feeds`, status `vendored`).

## Rule going forward

**Edit the canonical copy in `Sundara-commentaries`, not this one.** A future session
that repoints the ~70 readers to the new repo should delete this vendored copy and this
marker in the same pass.

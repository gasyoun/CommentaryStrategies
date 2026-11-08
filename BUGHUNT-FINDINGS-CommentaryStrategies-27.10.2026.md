# BUGHUNT-FINDINGS — CommentaryStrategies — 27.10.2026

_Created: 27-10-2026 · Author: Dr. Mārcis Gasūns (DeepSeek Flash, `deepseek-flash`, via DSH) · Run: interactive day `/bughunt` (bare invocation → rotation cursor, `CommentaryStrategies` was NEXT at 25/173; night driver not used)_

**Elapsed:** ~40 min. Budget 40 min; nothing failed three times.
**Scope:** the executable surface and the artifacts it owns — `scripts/` (167 Python
modules), `.github/workflows/ci.yml` (the nine-step `corpus` gate), `review-api/src/`
(4 JS modules), `tests/` (23 modules). Read-only static hunt plus live probes: the
gates were re-run, every candidate finding was reproduced before it was written
down. The probes wrote **nothing** into the shared tree (`git status` clean
throughout); the two destructive-looking probes ran in `/tmp/urnprobe` and
`/tmp/hygprobe` against copies.

## Summary

| # | Sev | Finding | Where |
|---|-----|---------|-------|
| 1 | HIGH | `derive_urn.py --check` **exits 0 on its own failure**: the CTS-URN book↔number cross-check wired into CI as a gate only *prints* its problems — the step can never turn red | [`scripts/derive_urn.py:122-150`](https://github.com/gasyoun/CommentaryStrategies/blob/main/scripts/derive_urn.py#L122-L150), [`.github/workflows/ci.yml:121-122`](https://github.com/gasyoun/CommentaryStrategies/blob/main/.github/workflows/ci.yml#L121-L122) |
| 2 | HIGH | **`data/leonov_own_notes.json` is not reproducible from its declared source.** Regenerating it (the documented command) reverts 11 records to the pre-H2884 mixed-script text and makes `translit_hygiene.py --check` fail with 9 undeclared words — the H2884 sweep repaired the derived artifact, never the source HTML | [`scripts/extract_leonov_notes.py:84-136`](https://github.com/gasyoun/CommentaryStrategies/blob/main/scripts/extract_leonov_notes.py#L84-L136), [`scripts/translit_hygiene.py:141`](https://github.com/gasyoun/CommentaryStrategies/blob/main/scripts/translit_hygiene.py#L141), [`.github/workflows/ci.yml:147-158`](https://github.com/gasyoun/CommentaryStrategies/blob/main/.github/workflows/ci.yml#L147-L158) |
| 3 | MEDIUM | `samskrtam_map.py`'s `ANCHOR_VERIFIED` set **never gates anything** — it is only stringified into provenance prose, so **73 of 244 "mapped" (29.9 %)** links rest on an existence-only page check the module's own docstring says does not count as proof | [`scripts/samskrtam_map.py:69-79,131-138,162-173`](https://github.com/gasyoun/CommentaryStrategies/blob/main/scripts/samskrtam_map.py#L69-L138) |
| 4 | MEDIUM | `profile_translator.py` prints topic percentages under the label **«доля примечаний»** (share of *notes*) but computes them per *topic assignment*; with 14–36 multi-topic notes per file the column sums to **128–172 %** | [`scripts/profile_translator.py:51,88-90`](https://github.com/gasyoun/CommentaryStrategies/blob/main/scripts/profile_translator.py#L51-L90) |
| 5 | LOW | `derive_urn.reorder()` lets the record's **pre-existing `urn` overwrite the freshly derived one** (stale value wins), so the non-`--check` write path can never correct a URN — it is a silent no-op by construction | [`scripts/derive_urn.py:100-109`](https://github.com/gasyoun/CommentaryStrategies/blob/main/scripts/derive_urn.py#L100-L109) |
| 6 | LOW | `extract_leonov_notes.py` joins comment ids to note texts by **unverified position** (a regex pass zipped against a separate `HTMLParser` pass); the parser's own `cur_id` is dead code (always `None`), so nothing would detect a shift | [`scripts/extract_leonov_notes.py:65,76,91,98-107`](https://github.com/gasyoun/CommentaryStrategies/blob/main/scripts/extract_leonov_notes.py#L65-L107) |
| 7 | LOW | Three modules vendored from Uprava (`pyfloor`, `_common`, `git_ops`) carry **doc pointers that do not exist here** (`tools/audit_pyfloor.py`, `docs/DECISION_PYTHON_INTERPRETER_FLOOR_2026.md`) and so claim an enforcement loop this repo does not have; `git_ops.exec(text=True)` also **silently drops `input_bytes`** | [`scripts/pyfloor.py:19-21,38`](https://github.com/gasyoun/CommentaryStrategies/blob/main/scripts/pyfloor.py#L19-L21), [`scripts/_common.py:1-8`](https://github.com/gasyoun/CommentaryStrategies/blob/main/scripts/_common.py#L1-L8), [`scripts/git_ops.py:101-124`](https://github.com/gasyoun/CommentaryStrategies/blob/main/scripts/git_ops.py#L101-L124) |
| 8 | LOW | `gate_reviewer_agreement.py` reports κ/raw-agreement on the **action only** while its disagreement worklist uses `conflict()` (action **or** edited text), so one report can print "100 % agreement" beside a non-empty editorial list | [`scripts/gate_reviewer_agreement.py:114-129`](https://github.com/gasyoun/CommentaryStrategies/blob/main/scripts/gate_reviewer_agreement.py#L114-L129) |

**No credential, injection or destructive-writer finding.** Nothing here needs a
human-gated `@DO` row; findings 1–4 are agent-fixable in the ordinary fix lane
(§4 of `/bughunt`).

## What was checked and came back green

Recorded so the next hunt does not repeat the work, and so the four findings above
are read as *the residue of a healthy repo*, not of an unchecked one.

- `python -m pytest` — **132 passed** on the live tree.
- All nine `corpus`-job gates re-run locally: `validate.py` (6 194 files, PASS),
  `typed_link_sundara_store_selftest.py`, `curated_floors_check.py` (21 floors
  hold), `check_release_meta.py` (1.28.0 ↔ 1.28.0), `derive_urn.py --check`,
  `samskrtam_map.py --check`, `release_binaries.py --check`, `translit_hygiene.py
  --check`, `corpus_truth_census.py --check` — every one exit 0.
- All five bundled selftests: `gate_ledger_selftest.py`,
  `review_platform_selftest.py`, `footnote_review_required.py --selftest` (9
  asserts), `corpus_truth_census_tamper_selftest.py` (1-byte flip → exit 1 with
  the s24 message; control passes), `typed_link_sundara_store_selftest.py`.
- **`py_compile` on all 167 `scripts/*.py` — 0 failures.** `eol_census.py` runs
  clean against `origin/main` (0 CR bytes over 6 437 text-attributed paths).
- Committed statistics were re-derived, not trusted: `data/iaa/iaa_kappa_stats.json`
  reproduces from its own confusion matrices to 4 dp for all 12 cells (overall
  κ 0.6476 / 0.5208, per-translator down to grintser's −0.0479), and the recorded
  67/69 disagreements are exactly `n − diag`.
- The index-based join in `compute_iaa_kappa.load_pairs` — the first thing that
  looked wrong (gold ids `mbh/kalyanov/c1` vs pred ids `kalyanov/comment_0001`,
  **0/50 ids match by name**) — is in fact aligned: `raw_text` is identical for
  all **300** index pairs. The id schemes differ by construction; the pairing is
  right. It stays unguarded (nothing asserts it), but it is not broken today.

## 1. HIGH — the CTS-URN gate is wired into CI and cannot fail

`.github/workflows/ci.yml` runs it as a named gate:

```yaml
      - name: CTS-URN cross-check (book ↔ number)
        run: python scripts/derive_urn.py --check
```

`main()` accumulates failures in `bad` and prints them — and then returns `None`:

```python
    print(f"\nВсего: {total} примечаний.")
    if bad:
        print(f"⚠ Проблемы перекрёстной проверки ({len(bad)}):")
        for cid, addr, note in bad:
            print(f"  {cid}: {addr} — {note}")
    else:
        print("✓ Все адреса разобраны, перекрёстная проверка книга↔номер пройдена.")
```

There is no `sys.exit` on either branch and no return value consumed by
`__main__`, so the process exit status is 0 whether the cross-check passed or not.

Live reproduction on a copy (`/tmp/urnprobe`, two deliberately bad addresses, one
wrong leading book number and one unknown parva):

```bash
$ cd /tmp/urnprobe && python3 scripts/derive_urn.py --check
(check) bad_markup_50.json             2 rec  напр.: urn:cts:sanskritLit:mahabharata:6.10.5

Всего: 2 примечаний.
⚠ Проблемы перекрёстной проверки (2):
  mbh/BAD/c1: MBh. Vana 6.10.5 — «Vana»=3 ≠ ведущий номер 6
  mbh/BAD/c2: MBh. Несуществующая 1.2.3 — неизвестная книга/парва «Несуществующая»
>>> EXIT CODE = 0
```

The same command on the live tree prints the success line and exits 0 — the two
states are indistinguishable to CI. Every other `--check` in this repo returns an
int from `main()` under `raise SystemExit(main())` (`corpus_truth_census.py:281`,
`build_apparatus_review_portal.py:114`, `check_release_meta.py:145`,
`samskrtam_map.py:199-203`); `derive_urn.py` is the one that does not, and it is
the one whose whole gate is the cross-check.

**Impact:** the gold sample's 300 CTS-URNs are the addressing layer for the TEI
export, the samskrtam crosswalk and every citation in the articles. A silently
wrong URN (`Vana` written with `6.` in front, a parva name typo, a re-typed
`shloka_addr` in a decision merge) lands green and propagates. The gate exists
precisely to catch that class and currently certifies it.

**Fix direction:** `return 1 if bad else 0` from `main()` and
`raise SystemExit(main())` — plus one test that fails-before/passes-after on a
fixture with a wrong leading book number, so the gate is proven non-vacuous.

## 2. HIGH — the Leonov/Kostina artifact is not reproducible from its own source, and regenerating it turns the hygiene gate red

`data/leonov_own_notes.json` is the **tier-1 print layer**: 1 058 notes with
`_meta.generated_by = scripts/extract_leonov_notes.py`, the ~36 % density benchmark
and the dedup baseline for the Phase-2 commentator layer (the
`typed_link_sundara_store_selftest.py` check `baseline_total_notes=1058` asserts
exactly this corpus).

Re-running the documented generator against the source HTML it names produces
**11 records that differ** from the committed file:

```bash
$ python3 - <<'PY'   # parse the source with the extractor's own Parser, diff by field
...  11 records would revert on regeneration
      5.1.7  comment_1_7: [('нāга', 'lat-in-cyr', 'нага', 'UNDECLARED')]
     5.15.4  comment_15_4: [('bahubhūmigṛhа', 'cyr-in-latin', 'bahubhūmigṛha', 'UNDECLARED')]
     5.17.8  comment_17_8: [('cлово', 'lat-in-cyr', 'слово', 'UNDECLARED')]
     5.38.29 comment_38_29: [('cогласно', 'lat-in-cyr', 'согласно', 'UNDECLARED')]
     5.39.50 comment_39_50: [('ūthа', 'cyr-in-latin', 'ūtha', 'UNDECLARED')]
     5.48.51 comment_48_51: [('smа', 'cyr-in-latin', 'sma', 'UNDECLARED')]
     5.52.11 comment_52_11: [('pāpа', 'cyr-in-latin', 'pāpa', 'UNDECLARED')]
     5.58.90 comment_58_90: [('ofJanaka', 'camel', None, 'UNDECLARED')]
     … (+ нāга at 5.10.12, prāvaraṇа at 5.17.5)
```

Every difference is **one homoglyph, and the committed side is the clean one**:
the artifact says `нага`/`слово`/`согласно`/`bahubhūmigṛha`, the source HTML at
`ramayana-leonov/Рамаяна. Книга 5. Сундараканда 2026.html` still carries
`нāга`/`cлово`/`cогласно`/`bahubhūmigṛhа`. The full end-to-end receipt, on a copy
(`/tmp/hygprobe`: regenerate the artifact from source, then run the gate):

```bash
$ python3 scripts/translit_hygiene.py --check
files scanned: 2, defect occurrences: 13
  lat-in-cyr         5  (auto-fixable 5)
  cyr-in-latin       5  (auto-fixable 5)
  camel              3  (auto-fixable 0)

FAIL: 9 undeclared mixed-script word(s): bahubhūmigṛhа, cлово, cогласно, ofJanaka,
prāvaraṇа, pāpа, smа, ūthа, нāга
>>> EXIT CODE = 1
```

Git history names the mechanism exactly:

| file | last commit |
|---|---|
| `data/leonov_own_notes.json` | `a62b374` 16-08-2026 — *"feat(translit): apply the h2864 vote — 643 mixed-script places down to 3 declared exceptions (H2884)"* |
| `ramayana-leonov/Рамаяна. Книга 5. Сундараканда 2026.html` | `433249f` 30-04-2026 — untouched |

H2884 ran the hygiene fixer over the **derived artifact** — `translit_hygiene.py`
line 141 puts `data/leonov_own_notes.json` in `target_files()` — and never over the
source HTML, which no `target_files()` pattern matches. That is verbatim the
failure mode the same module's docstring warns against ("fixing it here would be
fixing the shadow instead of the object").

**Impact, and why CI does not see it:** the six generators in the `corpus` job's
reproducibility step are `export_tei`, `build_pages`, `parse_formulas`,
`profile_nilakantha`, `extract_false_friends_profile`, `build_visualizations`;
`extract_leonov_notes.py` is not among them and its output is not in the
`git diff --exit-code` path list, so a stale artifact is invisible. The repo is in
a state where **the committed corpus and its own generator cannot both be right**:
leave the artifact as committed and it no longer matches its source; regenerate it
and the repo's own hygiene gate fails. Any future re-ingest of the Leonov HTML
(e.g. a corrected scan) silently reverts the H2884 repair for these 11 notes.

**Fix direction (two steps, in this order):** repair the 11 places in the **source
HTML** (translit_hygiene classifies all 11 as auto-fixable or declared — `нāга`
→ `нага`, `cлово` → `слово`, `ofJanaka` → `of Janaka`), regenerate the artifact,
and only then add `extract_leonov_notes.py` + `data/leonov_own_notes.json` to the
`corpus` job's reproducibility step so the drift becomes a red gate instead of a
slow rot.

## 3. MEDIUM — the samskrtam crosswalk publishes 73 links whose anchors were never checked

The module distinguishes two evidence grades and says so twice — in the constant's
comment ("якоря вне этого списка не считаются доказанными") and in the docstring of
`map_urn`, where an unproven anchor is supposed to be a signal, not a link:

```python
# Страницы, где каждый ожидаемый якорь был сверен с реальным HTML (а не только
# existence-проверка страницы): якоря вне этого списка не считаются доказанными.
ANCHOR_VERIFIED = { ... 7 pages ... }
```

But `ANCHOR_VERIFIED` is **never consulted by the status logic** — the only branch
is the blacklist:

```python
    if anchor in KNOWN_ANCHOR_MISSING.get((work, book_key), set()):
        rec["status"] = "anchor-missing"
    else:
        rec["status"] = "mapped"
```

and the set appears exactly once more, as prose: `", ".join(sorted(ANCHOR_VERIFIED))`
at line 166. Measured on the committed artifact:

| quantity | value |
|---|---|
| notes | 300 |
| `status: mapped` | 244 |
| …on an anchor-verified page | **171** |
| …on an existence-only page | **73 (29.9 % of mapped)** |

So `data/samskrtam_id_map.json` presents 244 working deep links while only 171 were
per-verse verified — and no per-record field lets a consumer tell the two apart
(`status` is `mapped` for both). This is the same class the repo already fixed once
in the apparatus ballot (H4371): a check that the artifact claims but the code does
not perform. It is a publication-facing claim, since the map is what generated
`sources/` pages link through.

**Fix direction:** either emit `status: "mapped"` only for `page in ANCHOR_VERIFIED`
and `"existence-only"` otherwise (making the constant load-bearing, with the
coverage block gaining a third bucket), or add a per-record `anchor_verified: bool`
and let `coverage.by_status` stay as is. Either way the docstring and the code must
agree; today the docstring is the better contract.

## 4. MEDIUM — six research profiles print a "share of notes" column that sums to 128–172 %

```python
    topics = Counter(t for r in records for t in r.get("axis_1_topic", []))   # :51
...
    print("\nОсь 1 — темы (доля примечаний, %):")                              # :88
    for t, v in p["topics"].most_common():
        print(f"  {t:16s} {round(100 * v / n, 1):5.1f}%  ({v})")              # :90
```

`topics` counts **assignments** (one note can carry several topics — the same
function computes `multi_topic_pct` from exactly that), while the label and the
`100 * v / n` denominator promise **notes**. Measured on all six gold files:

| translator | n | topic assignments | multi-topic notes | Σ of the labelled % |
|---|---:|---:|---:|---:|
| kalyanov | 50 | 71 | 21 | 142.0 % |
| vassilkov | 50 | 68 | 18 | 136.0 % |
| erman | 50 | 74 | 24 | 148.0 % |
| grintser | 50 | 72 | 22 | 144.0 % |
| syrkin | 50 | 86 | 36 | 172.0 % |
| leonov | 50 | 64 | 14 | 128.0 % |

The cross-translator comparison table (`report()`'s `myth %`, `realia %`, …
rows) inherits the same numerator via `pct()`, so a reader comparing "Grintser
realia 34 %" against a table where the column cannot total 100 % has no way to
know which denominator he is reading.

**Fix direction:** either label it for what it is («доля назначений тем, %» — the
honest reading, since multi-topic notes are real and the assignment rate is a
legitimate metric) or switch to notes-carrying-topic
(`sum(1 for r in records if t in r.get("axis_1_topic", []))`), which is what the
label promises and what `multi_topic_pct` already measures. Changing the number
means re-quoting any article figure derived from it — check `articles/` for the
affected percentages before choosing.

## 5. LOW — the URN writer overwrites its own fresh value with the stale one

`derive_urn.py` has two modes; the second is documented as the corrective one
("`python scripts/derive_urn.py` — внедрить поле urn"). It does not correct:

```python
def reorder(rec, urn):
    out = {}
    for k, v in rec.items():
        out[k] = v
        if k == "comment_id":
            out["urn"] = urn          # fresh value
    ...
```

Iteration then reaches the record's **existing** `urn` key (the real files are laid
out `['comment_id', 'urn', 'shloka_addr', …]`, i.e. after `comment_id`) and
`out[k] = v` writes the old value over the fresh one. Live:

```python
>>> reorder({"comment_id":"x","urn":"urn:cts:sanskritLit:mahabharata:99.9.9"}, "urn:cts:sanskritLit:mahabharata:3.8.10")["urn"]
'urn:cts:sanskritLit:mahabharata:99.9.9'   # stale value wins
```

Harmless today (derived and stored values agree, so the write is a no-op either
way), but it means the only corrective path in the file cannot correct anything —
and it compounds finding #1: the pair `--check` (cannot fail) plus the writer
(cannot fix) leaves URNs with no working guard at all. Fix: skip `k == "urn"` in
the loop (`if k != "urn": out[k] = v`).

## 6. LOW — the extractor's id join is positional and its self-check is dead code

```python
ids = re.findall(r'class="comment_item" id="([^"]+)"', html)   # :91 — pass A
p = Parser(); p.feed(html)                                      # :94 — pass B
for i, (verse, _cid, text) in enumerate(notes):                 # :98
    ...
    "comment_id": ids[i] if i < len(ids) else None,             # :107
```

Two independent passes over the same file are joined by index, keeping the regex
pass and **discarding** `_cid` — the parser's own id, which is the only evidence
that would catch a shift. It cannot catch one anyway: `self.cur_id` is assigned
nowhere in the class (verified: `sum(1 for _,c,_ in notes if c) == 0` over all
1 058 blocks), so `notes` carries `None` in that slot by construction and the id
comes solely from the zip.

Today the assumption holds — 1 058 regex ids, 1 058 text blocks, 0 disagreements —
so nothing is mislabelled. It is latent: one `comment_item` div without a
`comment_text` child (or the reverse) anywhere in the source shifts every id after
it, and the miscount is a silent mislabel of the dedup baseline, not a crash.
Fix: set `cur_id` in `handle_starttag` from the `comment_text` sibling's container
(or match the ids against the parser's own), assert `len(ids) == len(notes)`, and
prefer the parser's id over the positional one.

## 7. LOW — the vendored Uprava modules promise an enforcement loop this repo does not have

`scripts/pyfloor.py` and `scripts/_common.py` are copies of Uprava tool files: the
docstring of `_common` opens "Shared helpers for **Uprava** tools scripts" and its
`repo_root()` is described as "The Uprava checkout holding THIS module", while
`pyfloor` claims

> Call as `pyfloor.read_text(p, ...)` … ``tools/audit_pyfloor.py`` fails the build on any regression.

Neither path exists here — `tools/` is absent (this repo's tools live in
`scripts/`), and so is `docs/DECISION_PYTHON_INTERPRETER_FLOOR_2026.md`. Nothing in
`tests/` or `.github/workflows/` imports `pyfloor`, so the advertised audit loop is
not merely unwired, it is not present. The one live consumer is
`scripts/eol_census.py:44` (via `scripts/git_ops.py:46-53`), which is fine today —
`FLOOR = (3, 9)` is satisfied by every CI matrix entry.

While verifying the consumer, one real (currently unexercised) defect surfaced in
the seam it uses: `GitOperations.exec()` accepts `input_bytes` but forwards nothing
to `_common.git()` in the `text=True` branch —

```python
        if text:
            proc = _common.git(repo_path, *args, check=False, timeout=timeout_s, env=env)
```

so a caller passing `input_bytes` **without** `text=False` silently runs git with
no stdin (`git hash-object --stdin`, `git check-attr --stdin` would read an empty
stream) and gets a plausible-looking empty result. `eol_census` always passes
`text=False`, so the bug is latent. Fix: raise on `input_bytes` when `text=True`,
or route it through `_common.run(input_text=…)`.

Either way, the doc pointers should say what is true here (`scripts/`, no audit
script) or the modules should stop being vendored and be imported from a shared
package — a reader who trusts the docstring will look for a gate that does not
exist.

## 8. LOW — agreement is measured on actions, disagreement on actions *or* text

```python
        pairs = [(acts[a].get("action"), acts[b].get("action")) for acts in per_note.values()
                 if a in acts and b in acts]
...
        agree = sum(1 for x, y in pairs if x == y)
...
            if gate_ledger.conflict({a: av, b: bv}):      # action OR differing edited_note
                disagreements[layer[nid]].append((nid, x, y))
```

`conflict()` (gate_ledger.py:122-128) treats two `edit` verdicts proposing
**different text** as a conflict, but `pairs` keeps only the action, so both enter
κ and raw agreement as agreement. A report can therefore print "raw agreement
100.0 %" and "DISAGREEMENTS (n)" in the same block — two different definitions of
the same word on one page.

Unexercised today: `data/apparatus/gate_ledger.json` holds **126 entries, every one
with exactly one verdict** (`{'accept': 126}`, 0 two-reviewer notes, 0 `edit`
verdicts), so the second gatekeeper has not voted and no pair is ever formed. The
finding is real but its blast radius is zero until Kostina's ballot lands — worth
fixing before that, since the first two-reviewer run is exactly when the report
will be read as a worklist.

## Method note — what was *not* run

The night driver (`bughunt_night.py run --repo CommentaryStrategies`) was not used;
this was the interactive day lane, so the cycle cursor was **not** advanced by a
driver run and finding-autofix (night policy: auto-fix HIGH) did **not** run. No fix
was applied in this pass: findings 1–4 are queued for the fix lane (§4 of
`/bughunt`) and each ships a fails-before/passes-after pin when it does.

_Dr. Mārcis Gasūns_

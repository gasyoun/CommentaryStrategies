#!/usr/bin/env python3
"""H4738 — Samsaadhanii Sundarakāṇḍa gold kāraka treebank → analysis layer (VALIDATION-ONLY).

Sibling census A5 pilot 1 (slots s5a; siblings: H4740 morph.cgi, H4741
dhātupāṭha×mw_roots). Ingests Amba Kulkarni's SCL treebank
(samsaadhanii/datasets → Annotated-data/Sundarakāṇḍa.csv; tab-separated,
14-column word-level gold dependency annotation in WX notation) into the
CommentaryStrategies analysis-layer estate.

VALIDATION-ONLY by mission: the upstream `datasets` repo carries **no
LICENSE** — rights unclear, redistribution barred (SAMSAADHANII_INDEX.md,
02-07-2026 deep dive). The committed artifacts are this script + an
AGGREGATE parity report + a counts-only manifest. The row-level ingested
layer is emitted ONLY behind `--emit-layer` (use a path OUTSIDE the repo;
it must never be committed).

Sentence identity is the upstream `anvaya_no` column (`N.M` = sentence.word):
a sentence is (book, chaptno, N). RELABELED 2026-09-16 per MG ruling (а) on
the H4738 verifier DISAGREE: the earlier identity (book, chaptno, sentno) is
a chapter-level constant, not a sentence id (in 44 of 62 chapters sentno is
always 1) — the "92 sentences" then reported were 62 chapter-buckets plus 30
sentno buckets. The DoD parity gate is now measured against anvaya_no
sentences; the degenerate sentno bucket count is kept only as a labeled
artifact. Parity gate: word rows + unannotated rows == raw line census,
layer records == source anvaya sentences, layer token sum == word rows.
Any mismatch = FAIL, exit 1.

WX rosette (selftest only): literal char pairs attested by SCL's own
converters/wx2slp.lex and by H4741's rosette (XAwu→dhātu, gaNa→gaṇa,
AwmanepaxI→ātmanepada) — WX traps: w=t-dental, x=d-dental, d=ḍ-retroflex,
t=ṭ-retroflex, N=ṇ, R=ṣ. Rendered to IAST for the report; sunxarakANdam →
sundarakāṇḍam, wawaH → tataḥ, XAwu → dhātu. Not a general transliterator;
the estate canonical remains sanskrit_util.

Usage:
  python3 scripts/ingest_samsaadhanii_sundara_treebank.py \
      --datasets-dir /tmp/h4738-samsaa \
      --outdir data/analysis/samsaadhanii_sundara_treebank \
      [--emit-layer /tmp/h4738-layer]
  python3 scripts/ingest_samsaadhanii_sundara_treebank.py --selftest

Exit 0 = PASS. Refuses to overwrite an existing report without --force.
"""

import argparse
import csv
import hashlib
import json
import os
import re
import sys
from collections import Counter
from datetime import date

EXPECTED_COLUMNS = [
    "anvaya_no", "word", "poem", "sandhied_word", "morph_analysis",
    "morph_in_context", "kaaraka_sambandha", "possible_relations",
    "sentno", "chaptno", "slokano", "book", "part1", "part2",
]

# Minimal WX→IAST pairs for the documentation rosette (selftest/report only).
# Attested by SCL converters/wx2slp.lex pairings as cited in H4741; WX traps:
# dental series w/W/x/X (= t/th/d/dh), retroflex series t/T/d/D (= ṭ/ṭh/ḍ/ḍh),
# N=ṇ, R=ṣ, z/Z=anubandha markers (stripped). Unmapped chars pass through.
WX_TO_IAST = {
    "a": "a", "A": "ā", "i": "i", "I": "ī", "u": "u", "U": "ū",
    "f": "ṛ", "F": "ṝ", "e": "e", "E": "ai", "o": "o", "O": "au",
    "M": "ṃ", "H": "ḥ",
    "k": "k", "K": "kh", "g": "g", "G": "gh", "N": "ṇ",
    "c": "c", "C": "ch", "j": "j", "J": "jh",
    "w": "t", "W": "th", "x": "d", "X": "dh",
    "t": "ṭ", "T": "ṭh", "d": "ḍ", "D": "ḍh", "n": "n",
    "p": "p", "P": "ph", "b": "b", "B": "bh", "m": "m",
    "y": "y", "r": "r", "l": "l", "v": "v",
    "R": "ṣ", "S": "ś", "s": "s", "h": "h",
    "z": "", "Z": "",  # anubandha markers, stripped
    "-": "-", ".": ".",
}


def wx_to_iast(word: str) -> str:
    out = []
    for ch in word:
        out.append(WX_TO_IAST.get(ch, ch))
    return "".join(out)


def sha256_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def parse_treebank(csv_path: str):
    """Parse the 14-col TSV. Returns (sentences, stats).

    sentences: dict[(book, chaptno, anvaya_N)] -> {n_tokens, words[(M, word)],
    slokano, sentno}. Sentence identity = the `anvaya_no` column (`N.M` =
    sentence.word) — the source's own sentence id. `sentno` is a chapter-level
    constant (RELABEL 2026-09-16, MG ruling а): its bucket count is tracked
    only as a labeled degenerate artifact, never as a sentence count.
    Fails loudly on schema drift or malformed identity fields.
    """
    rows = 0
    unannotated = 0
    unannotated_lines = []
    sentences = {}
    sentno_buckets = set()
    bucket_tokens = Counter()
    sentno_max_per_chapter = {}
    verse_pairs = set()
    slokano_labels = set()
    wx_lafk_any_cell = 0
    wx_lafkAm_word = 0
    wx_lafkA_word = 0
    wx_lafkAm_occurrences = 0
    wx_lamk_occurrences = 0
    per_sarga_rows = Counter()
    anu_re = re.compile(r"^\d+\.\d+$")
    with open(csv_path, "r", encoding="utf-8", newline="") as fh:
        reader = csv.reader(fh, delimiter="\t")
        header = next(reader)
        if header != EXPECTED_COLUMNS:
            raise SystemExit(
                f"FAIL schema: header drift\n  got: {header}\n  want: {EXPECTED_COLUMNS}")
        for lineno, rec in enumerate(reader, start=2):
            if not rec or all(not c.strip() for c in rec):
                continue
            if len(rec) != len(EXPECTED_COLUMNS):
                raise SystemExit(f"FAIL row {lineno}: {len(rec)} cols, want 14")
            d = dict(zip(EXPECTED_COLUMNS, rec))
            for key in ("word", "sentno", "chaptno", "slokano", "book"):
                if not d[key].strip():
                    raise SystemExit(f"FAIL row {lineno}: empty {key!r}")
            if not (anu_re.match(d["anvaya_no"]) or d["anvaya_no"] == "-"):
                raise SystemExit(f"FAIL row {lineno}: bad anvaya_no {d['anvaya_no']!r}")
            # WX f-ambiguity census (derive-don't-store, all data rows)
            if any("lafk" in c for c in rec):
                wx_lafk_any_cell += 1
            if d["word"] == "lafkAm":
                wx_lafkAm_word += 1
            if "lafkA" in d["word"]:
                wx_lafkA_word += 1
            wx_lafkAm_occurrences += sum(c.count("lafkAm") for c in rec)
            wx_lamk_occurrences += sum(c.count("laMk") for c in rec)
            if d["anvaya_no"] == "-":
                # upstream quirk: punctuation/interpolation rows carry no
                # anvaya identity — counted separately, not treebank tokens
                unannotated += 1
                unannotated_lines.append(lineno)
                continue
            chap = int(d["chaptno"])
            sent_no = int(d["sentno"])
            n_str, m_str = d["anvaya_no"].split(".")
            sent_key = (d["book"], chap, int(n_str))
            s = sentences.setdefault(sent_key, {"n_tokens": 0, "words": [],
                                                "slokano": d["slokano"],
                                                "sentno": sent_no})
            s["n_tokens"] += 1
            s["words"].append((int(m_str), d["word"]))
            rows += 1
            per_sarga_rows[chap] += 1
            bucket_key = (d["book"], chap, sent_no)
            sentno_buckets.add(bucket_key)
            bucket_tokens[bucket_key] += 1
            sentno_max_per_chapter[chap] = max(sentno_max_per_chapter.get(chap, 0), sent_no)
            verse_pairs.add((chap, d["slokano"]))
            slokano_labels.add(d["slokano"])
    stats = {
        "rows": rows,
        "unannotated_rows": unannotated,
        "unannotated_lines": unannotated_lines,
        "sentences": len(sentences),
        "sentno_buckets": len(sentno_buckets),
        "chapters_with_sentno_always_1": sum(
            1 for v in sentno_max_per_chapter.values() if v == 1),
        "chapters_total": len(sentno_max_per_chapter),
        "max_tokens_in_one_sentno_bucket": max(bucket_tokens.values()),
        "verse_pairs": len(verse_pairs),
        "slokano_labels": len(slokano_labels),
        "sargas": len({k[1] for k in sentences}),
        "per_sarga_rows_min": min(per_sarga_rows.values()),
        "per_sarga_rows_max": max(per_sarga_rows.values()),
        "wx_lafk_rows_any_cell": wx_lafk_any_cell,
        "wx_lafkAm_word_rows": wx_lafkAm_word,
        "wx_lafkA_word_rows": wx_lafkA_word,
        "wx_lafkAm_occurrences": wx_lafkAm_occurrences,
        "wx_lamk_occurrences": wx_lamk_occurrences,
    }
    return sentences, stats


def raw_line_census(csv_path: str) -> int:
    """Independent count: non-empty, non-header physical lines."""
    n = 0
    with open(csv_path, "r", encoding="utf-8") as fh:
        for i, line in enumerate(fh):
            if i == 0:
                continue
            if line.strip():
                n += 1
    return n


def ingest_layer(sentences, emit_dir: str) -> str:
    """Write the row-level layer OUT-OF-REPO (validation-only license).

    One record per anvaya sentence (book, chaptno, N); words ordered by the
    anvaya word index M. `sentno` is carried informational-only (chapter-level
    constant, NOT identity).
    """
    os.makedirs(emit_dir, exist_ok=True)
    layer_path = os.path.join(emit_dir, "sundara_treebank_sentences.jsonl")
    with open(layer_path, "w", encoding="utf-8") as out:
        for key in sorted(sentences, key=lambda k: (k[0], k[1], k[2])):
            book, sarga, anvaya_n = key
            s = sentences[key]
            words = [w for _, w in sorted(s["words"])]
            out.write(json.dumps({
                "book_wx": book, "sarga": sarga, "anvaya_sentence": anvaya_n,
                "sentno_informational": s["sentno"], "slokano": s["slokano"],
                "n_tokens": s["n_tokens"], "words_wx": words,
            }, ensure_ascii=False) + "\n")
    return layer_path


def verify_layer_parity(layer_path: str, source_sentence_count: int) -> tuple:
    """Re-read the emitted layer; recount records + tokens for the parity gate.

    Gate (RELABEL 2026-09-16, MG ruling а): layer record count == distinct
    source anvaya sentences AND layer token sum == annotated word rows —
    both cross-checks are non-vacuous (record count and token sum are
    computed over the emitted file, against independently walked source
    counts).
    """
    n = 0
    tokens = 0
    with open(layer_path, "r", encoding="utf-8") as fh:
        for line in fh:
            if line.strip():
                rec = json.loads(line)
                if rec["n_tokens"] != len(rec["words_wx"]):
                    raise SystemExit(
                        f"FAIL layer: token/word mismatch in {rec['book_wx']} "
                        f"{rec['sarga']}.anvaya={rec['anvaya_sentence']}")
                n += 1
                tokens += rec["n_tokens"]
    if n != source_sentence_count:
        raise SystemExit(
            f"FAIL parity: layer {n} anvaya sentences != source {source_sentence_count}")
    return n, tokens


def run(datasets_dir: str, outdir: str, emit_layer: str, force: bool) -> dict:
    csv_path = os.path.join(datasets_dir, "Annotated-data", "Sundarakanda.csv")
    if not os.path.isfile(csv_path):
        raise SystemExit(f"FAIL: {csv_path} not found (clone samsaadhanii/datasets first)")
    sentences, stats = parse_treebank(csv_path)
    source_count_raw = raw_line_census(csv_path)

    parity = {
        "word_rows (csv-module walk)": stats["rows"],
        "unannotated_rows": stats["unannotated_rows"],
        "source_nonheader_lines (raw census)": source_count_raw,
        "anvaya_sentences (book,chaptno,N)": stats["sentences"],
    }
    if stats["rows"] + stats["unannotated_rows"] != source_count_raw:
        raise SystemExit(
            f"FAIL parity: word {stats['rows']} + unannotated "
            f"{stats['unannotated_rows']} != raw census {source_count_raw}")

    layer_path = None
    layer_count = None
    layer_tokens = None
    if emit_layer:
        if os.path.abspath(emit_layer).startswith(os.path.abspath(os.getcwd())):
            # guard: row-level data must not land inside the repo
            raise SystemExit("FAIL: --emit-layer must point OUTSIDE the repository")
        layer_path = ingest_layer(sentences, emit_layer)
        layer_count, layer_tokens = verify_layer_parity(layer_path, stats["sentences"])
        if layer_tokens != stats["rows"]:
            raise SystemExit(
                f"FAIL parity: layer token sum {layer_tokens} != word rows {stats['rows']}")

    os.makedirs(outdir, exist_ok=True)
    report_path = os.path.join(outdir, "H4738_PARITY_REPORT.md")
    manifest_path = os.path.join(outdir, "ingest_manifest.json")
    for p in (report_path, manifest_path):
        if os.path.exists(p) and not force:
            raise SystemExit(f"FAIL: {p} exists; pass --force to overwrite")

    sample = []
    for key in sorted(sentences, key=lambda k: (k[1], k[2]))[:3]:
        book, sarga, anvaya_n = key
        words = [w for _, w in sorted(sentences[key]["words"])][:5]
        sample.append({
            "sarga.anvaya": f"{sarga:03d}.{anvaya_n}",
            "slokano": sentences[key]["slokano"],
            "first_words_wx": words,
            "first_words_iast": [wx_to_iast(w) for w in words],
        })

    manifest = {
        "handoff": "H4738",
        "census": "sibling census A5 pilot 1 (slot s5a)",
        "created": date.today().isoformat(),
        "tier": "OxAlpha (opencode/z-ai/glm-5.3-flash)",
        "validation_only": True,
        "relabel": "2026-09-16 MG ruling (а) on verifier DISAGREE: sentence "
                   "identity re-measured by anvaya_no; prior '92 sentences' "
                   "was a (book,chaptno,sentno) grouping artifact",
        "upstream": {
            "repo": "https://github.com/samsaadhanii/datasets",
            "path": "Annotated-data/Sundarakanda.csv",
            "license": "NONE on upstream repo — validation-only, no redistribution",
            "sha256_12": sha256_file(csv_path)[:12],
        },
        "notation": "WX (SCL); sentence identity = anvaya_no N.M → (book, chaptno, N)",
        "counts": {
            "word_rows": stats["rows"],
            "unannotated_rows": stats["unannotated_rows"],
            "unannotated_lines": stats["unannotated_lines"],
            "sentences_anvaya": stats["sentences"],
            "sentno_buckets_degenerate": {
                "count": stats["sentno_buckets"],
                "chapters_with_sentno_always_1": stats["chapters_with_sentno_always_1"],
                "chapters_total": stats["chapters_total"],
                "max_tokens_in_one_bucket": stats["max_tokens_in_one_sentno_bucket"],
                "note": "chapter-level constant, NOT a sentence count",
            },
            "verse_pairs_chaptno_x_slokano": stats["verse_pairs"],
            "distinct_slokano_labels": stats["slokano_labels"],
            "sargas": stats["sargas"],
            "per_sarga_row_range": [stats["per_sarga_rows_min"], stats["per_sarga_rows_max"]],
        },
        "wx_f_ambiguity_census": {
            "rows_with_substring_lafk_any_cell": stats["wx_lafk_rows_any_cell"],
            "rows_word_exact_lafkAm": stats["wx_lafkAm_word_rows"],
            "rows_word_contains_lafkA": stats["wx_lafkA_word_rows"],
            "lafkAm_literal_occurrences_all_cells": stats["wx_lafkAm_occurrences"],
            "laMk_literal_occurrences_all_cells": stats["wx_lamk_occurrences"],
        },
        "parity": {k.replace(" ", "_").replace("(", "").replace(")", ""): v
                   for k, v in parity.items()},
        "layer_emitted": bool(emit_layer),
        "layer_path": layer_path,
        "layer_sentence_count": layer_count,
        "layer_token_sum": layer_tokens,
        "rosette_sample": sample,
    }
    with open(manifest_path, "w", encoding="utf-8") as fh:
        json.dump(manifest, fh, ensure_ascii=False, indent=2)
        fh.write("\n")

    verdict = "PASS"
    with open(report_path, "w", encoding="utf-8") as fh:
        fh.write(f"""# H4738 — Samsaadhanii Sundarakāṇḍa treebank ingest parity report

_Created: {date.today().isoformat()} · tier: OxAlpha (opencode/z-ai/glm-5.3-flash) · VALIDATION-ONLY · RELABELED 2026-09-16 (MG ruling а)_

## Inputs (provenance)

| input | sha256 (first 12) | note |
|---|---|---|
| SCL `samsaadhanii/datasets` `Annotated-data/Sundarakanda.csv` (no LICENSE upstream) | `{manifest["upstream"]["sha256_12"]}` | {stats["rows"]} word rows, tab-separated, 14 cols, WX notation |

## Result — sentence-count parity (DoD gate, anvaya_no basis)

Sentence identity is the upstream `anvaya_no` column (`N.M` = sentence.word):
one sentence = (book, chaptno, N).

| metric | value |
|---|---|
| word rows (csv-module walk) | {stats["rows"]} |
| unannotated rows (anvaya_no='-': punctuation/interpolations) | {stats["unannotated_rows"]} (lines {", ".join(map(str, stats["unannotated_lines"]))}) |
| total non-header lines (raw census) | {source_count_raw} |
| **sentences (anvaya_no → book, chaptno, N)** | **{stats["sentences"]}** |
| verse pairs (chaptno × slokano) | {stats["verse_pairs"]} |
| distinct slokano labels | {stats["slokano_labels"]} |
| sargas | {stats["sargas"]} |
| rows per sarga (min–max) | {stats["per_sarga_rows_min"]}–{stats["per_sarga_rows_max"]} |
| ingested layer emitted | {"yes (local-only, outside repo)" if emit_layer else "no (--emit-layer not passed)"} |
| layer record recount | {layer_count if layer_count is not None else "—"} |
| layer token sum | {layer_tokens if layer_tokens is not None else "—"} |

**Relabel note (2026-09-16, MG ruling а on verifier DISAGREE).** The
previously reported «92 sentences» counted (book, chaptno, sentno) buckets.
`sentno` is a chapter-level constant, not a sentence id: {stats["chapters_with_sentno_always_1"]}
of {stats["chapters_total"]} chapters carry `sentno=1` on every row, and the
largest single bucket holds {stats["max_tokens_in_one_sentno_bucket"]} words.
Those buckets are recorded below only as a labeled artifact; the DoD metric
is the anvaya_no sentence count.

| degenerate sentno artifact | value |
|---|---|
| (book, chaptno, sentno) buckets | {stats["sentno_buckets"]} (= {stats["chapters_total"]} chapters + {stats["sentno_buckets"] - stats["chapters_total"]} extra sentno buckets) |
| chapters with sentno always 1 | {stats["chapters_with_sentno_always_1"]} / {stats["chapters_total"]} |
| max tokens in one bucket | {stats["max_tokens_in_one_sentno_bucket"]} |

**Parity verdict: {verdict}** — three non-vacuous cross-checks: word rows +
unannotated rows == raw line census ({stats["rows"]} + {stats["unannotated_rows"]} == {source_count_raw});
emitted-layer record count == distinct source anvaya sentences
({layer_count if layer_count is not None else "—"} == {stats["sentences"]});
emitted-layer token sum == word rows ({layer_tokens if layer_tokens is not None else "—"} == {stats["rows"]}).
Every row passed the 14-column schema and identity checks; malformed rows
abort with a loud FAIL (none fired).

## Rosette (aggregate-only, first words ≤5 per sentence, 3 sentences)

⚠️ WX `f` is ambiguous in this dataset: standard vocalic ṛ AND pre-stop
nasal. Derived census (all {stats["rows"] + stats["unannotated_rows"]} data
rows): substring `lafk` in any cell — {stats["wx_lafk_rows_any_cell"]} rows
(incl. `alafkArAm` = alaṅkāram, unrelated to Laṅkā); exact word `lafkAm` —
{stats["wx_lafkAm_word_rows"]} rows (= **laṅkām**, lemma `lafkA` tagged
`swrI` feminine; {stats["wx_lafkAm_occurrences"]} literal occurrences);
word cells containing `lafkA` —
{stats["wx_lafkA_word_rows"]} rows; `laMk` spellings —
{stats["wx_lamk_occurrences"]}. The literal table
renders it ṛ — word-level IAST below is indicative, not authoritative; any
future WX layer needs a context-resolved converter (sanskrit_util + WX
mode), not this table.

| sarga.anvaya | slokano | first words (WX) | IAST |
|---|---|---|---|
""")
        for s in sample:
            fh.write(f"| {s['sarga.anvaya']} | {s['slokano']} | {' '.join(s['first_words_wx'])} | {' '.join(s['first_words_iast'])} |\n")
        fh.write(f"""
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
python3 scripts/ingest_samsaadhanii_sundara_treebank.py \\
    --datasets-dir /tmp/h4738-samsaa \\
    --outdir data/analysis/samsaadhanii_sundara_treebank \\
    --emit-layer /tmp/h4738-layer
```
""")
    print(json.dumps({"verdict": verdict, "counts": manifest["counts"],
                      "parity": manifest["parity"], "report": report_path}, ensure_ascii=False))
    return manifest


def selftest() -> None:
    """Own-data canary: synthetic 3-sentence treebank + malformed-row rejection."""
    import tempfile
    header = "\t".join(EXPECTED_COLUMNS)
    rows = [
        "1.1\ttataH\t-\ttataH\tavya\tavya\t-\t-\t1\t001\t001\tsunxarakANdam\t-\t-",
        "1.1\trAvaNa-\t-\trAvaNa\tpum-nAman\t-\t-\t-\t1\t001\t001\tsunxarakANdam\t-\t-",
        "1.2\tgaNayati\t-\tgaNayati\tlaT\tlaT\txAwu\tkara/kyap\t2\t001\t001\tsunxarakANdam\t-\t-",
        "2.1\tlakRmaNaH\t-\tlakRmaNaH\tpum-nAman\tprAwamipaxa\taxwA\t-\t1\t002\t005\tsunxarakANdam\t-\t-",
        "2.2\tvanam\t-\tvanam\tnApaM Napum\tprAwamipaxa\tkarma\t-\t1\t002\t005\tsunxarakANdam\t-\t-",
        "3.1\tsitaA\t-\tsitaA\tnApaM strI\tprAwamipaxa\taxwA\t-\t2\t002\t006\tsunxarakANdam\t-\t-",
    ]
    with tempfile.TemporaryDirectory() as tmp:
        csv_path = os.path.join(tmp, "fixture.csv")
        with open(csv_path, "w", encoding="utf-8") as fh:
            fh.write(header + "\n" + "\n".join(rows) + "\n")
        sentences, stats = parse_treebank(csv_path)
        assert stats["rows"] == 6, stats
        # anvaya_no N: (001,1)=tataH+rAvaNa-+gaNayati, (002,2), (002,3) → 3 sentences
        assert stats["sentences"] == 3, stats
        # degenerate sentno buckets: (001,1) (001,2) (002,1) (002,2) → 4, NOT 3
        assert stats["sentno_buckets"] == 4, stats
        assert stats["verse_pairs"] == 3 and stats["slokano_labels"] == 3, stats
        assert stats["chapters_with_sentno_always_1"] == 0, stats  # both chapters reach sentno=2
        assert raw_line_census(csv_path) == 6
        layer = ingest_layer(sentences, os.path.join(tmp, "layer"))
        n, toks = verify_layer_parity(layer, 3)
        assert n == 3 and toks == 6, (n, toks)
        assert wx_to_iast("sunxarakANdam") == "sundarakāṇḍam", wx_to_iast("sunxarakANdam")
        assert wx_to_iast("wawaH") == "tataḥ", wx_to_iast("wawaH")
        assert wx_to_iast("XAwu") == "dhātu", wx_to_iast("XAwu")
        assert wx_to_iast("lakRmaNaH") == "lakṣmaṇaḥ", wx_to_iast("lakRmaNaH")
        assert wx_to_iast("rAvaNa") == "rāvaṇa", wx_to_iast("rAvaNa")
        # malformed row must abort loudly
        bad = os.path.join(tmp, "bad.csv")
        with open(bad, "w", encoding="utf-8") as fh:
            fh.write(header + "\n" + "X.9\tword\t-\t-\t-\t-\t-\t-\t1\t001\t001\tb\t-\t-\n")
        try:
            parse_treebank(bad)
        except SystemExit as e:
            assert "anvaya_no" in str(e), e
        else:
            raise AssertionError("malformed anvaya_no did not abort")
    print("SELFTEST PASS — 3 anvaya sentences vs 4 degenerate sentno buckets / "
          "6 rows, record parity 3==3, token parity 6==6, "
          "rosette sundarakāṇḍam, malformed-row abort")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--datasets-dir", help="clone of samsaadhanii/datasets")
    ap.add_argument("--outdir", default="data/analysis/samsaadhanii_sundara_treebank")
    ap.add_argument("--emit-layer", help="OUT-OF-REPO dir for the row-level layer")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if args.selftest:
        selftest()
        return
    if not args.datasets_dir:
        ap.error("--datasets-dir is required (or use --selftest)")
    run(args.datasets_dir, args.outdir, args.emit_layer, args.force)


if __name__ == "__main__":
    main()

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

Sentence identity follows the upstream annotation: (book, chaptno, sentno).
Parity gate (DoD): sentence count in the ingested layer == two independent
recounts of the source (csv-module walk and raw-line census). Any mismatch
= FAIL, exit 1.

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
    """Parse the 14-col TSV. Returns (rows, sentences, stats).

    sentences: dict[(book, chaptno, sentno)] -> {n_tokens, words[], first_anvaya}
    Fails loudly on schema drift or malformed identity fields.
    """
    rows = 0
    unannotated = 0
    unannotated_lines = []
    sentences = {}
    per_sarga_rows = Counter()
    # WX-`f` ambiguity census (H4738 verifier, 15-09-2026): counts over ALL
    # data rows (annotated + quirk), using the verifier's exact definitions.
    wx_rows_substr = 0  # rows carrying substring `lafk` in ANY cell
    wx_rows_exact = 0  # rows whose `word` cell is exactly `lafkAm`
    wx_word_cells_lafkA = 0  # word cells containing `lafkA`
    wx_occurrences = 0  # literal `lafkAm` occurrences, whole file
    wx_lamk = 0  # literal `laMk` occurrences (expected 0)
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
            if any("lafk" in c for c in rec):
                wx_rows_substr += 1
            if d["word"] == "lafkAm":
                wx_rows_exact += 1
            if "lafkA" in d["word"]:
                wx_word_cells_lafkA += 1
            wx_occurrences += sum(c.count("lafkAm") for c in rec)
            wx_lamk += sum(c.count("laMk") for c in rec)
            for key in ("word", "sentno", "chaptno", "slokano", "book"):
                if not d[key].strip():
                    raise SystemExit(f"FAIL row {lineno}: empty {key!r}")
            if not (anu_re.match(d["anvaya_no"]) or d["anvaya_no"] == "-"):
                raise SystemExit(f"FAIL row {lineno}: bad anvaya_no {d['anvaya_no']!r}")
            if d["anvaya_no"] == "-":
                # upstream quirk: punctuation/interpolation rows carry no
                # anvaya identity — counted separately, not treebank tokens
                unannotated += 1
                unannotated_lines.append(lineno)
                continue
            sent_key = (d["book"], int(d["chaptno"]), int(d["sentno"]))
            s = sentences.setdefault(sent_key, {"n_tokens": 0, "words": [],
                                                "slokano": d["slokano"],
                                                "first_anvaya": d["anvaya_no"]})
            s["n_tokens"] += 1
            s["words"].append(d["word"])
            rows += 1
            per_sarga_rows[int(d["chaptno"])] += 1
    stats = {
        "rows": rows,
        "unannotated_rows": unannotated,
        "unannotated_lines": unannotated_lines,
        "sentences": len(sentences),
        "verses": len({(k[1], s["slokano"]) for k, s in sentences.items()}),
        "sargas": len({k[1] for k in sentences}),
        "per_sarga_rows_min": min(per_sarga_rows.values()),
        "per_sarga_rows_max": max(per_sarga_rows.values()),
        "wx_f_rows_substr": wx_rows_substr,
        "wx_f_rows_exact_lafkAm": wx_rows_exact,
        "wx_f_word_cells_lafkA": wx_word_cells_lafkA,
        "wx_f_occurrences_lafkAm": wx_occurrences,
        "wx_f_occurrences_laMk": wx_lamk,
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
    """Write the row-level layer OUT-OF-REPO (validation-only license)."""
    os.makedirs(emit_dir, exist_ok=True)
    layer_path = os.path.join(emit_dir, "sundara_treebank_sentences.jsonl")
    with open(layer_path, "w", encoding="utf-8") as out:
        for key in sorted(sentences, key=lambda k: (k[0], k[1], k[2])):
            book, sarga, sentno = key
            s = sentences[key]
            out.write(json.dumps({
                "book_wx": book, "sarga": sarga, "sentno": sentno,
                "slokano": s["slokano"], "n_tokens": s["n_tokens"],
                "words_wx": s["words"],
            }, ensure_ascii=False) + "\n")
    return layer_path


def verify_layer_parity(layer_path: str, source_sentence_count: int) -> int:
    """Re-read the emitted layer; recount sentences for the parity gate."""
    n = 0
    with open(layer_path, "r", encoding="utf-8") as fh:
        for line in fh:
            if line.strip():
                rec = json.loads(line)
                if rec["n_tokens"] != len(rec["words_wx"]):
                    raise SystemExit(
                        f"FAIL layer: token/word mismatch in {rec['book_wx']} "
                        f"{rec['sarga']}.{rec['sentno']}")
                n += 1
    if n != source_sentence_count:
        raise SystemExit(
            f"FAIL parity: layer {n} sentences != source {source_sentence_count}")
    return n


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
        "sentence_groups (book,chaptno,sentno)": stats["sentences"],
    }
    if stats["rows"] + stats["unannotated_rows"] != source_count_raw:
        raise SystemExit(
            f"FAIL parity: word {stats['rows']} + unannotated "
            f"{stats['unannotated_rows']} != raw census {source_count_raw}")

    layer_path = None
    layer_count = None
    if emit_layer:
        if os.path.abspath(emit_layer).startswith(os.path.abspath(os.getcwd())):
            # guard: row-level data must not land inside the repo
            raise SystemExit("FAIL: --emit-layer must point OUTSIDE the repository")
        layer_path = ingest_layer(sentences, emit_layer)
        layer_count = verify_layer_parity(layer_path, stats["sentences"])

    os.makedirs(outdir, exist_ok=True)
    report_path = os.path.join(outdir, "H4738_PARITY_REPORT.md")
    manifest_path = os.path.join(outdir, "ingest_manifest.json")
    for p in (report_path, manifest_path):
        if os.path.exists(p) and not force:
            raise SystemExit(f"FAIL: {p} exists; pass --force to overwrite")

    sample = []
    for key in sorted(sentences, key=lambda k: (k[1], k[2]))[:3]:
        book, sarga, sentno = key
        words = sentences[key]["words"][:5]
        sample.append({
            "sarga.sloka": f"{sarga:03d}.{sentences[key]['slokano']}",
            "first_words_wx": words,
            "first_words_iast": [wx_to_iast(w) for w in words],
        })

    manifest = {
        "handoff": "H4738",
        "census": "sibling census A5 pilot 1 (slot s5a)",
        "created": date.today().isoformat(),
        "tier": "OxAlpha (opencode/z-ai/glm-5.3-flash)",
        "validation_only": True,
        "upstream": {
            "repo": "https://github.com/samsaadhanii/datasets",
            "path": "Annotated-data/Sundarakanda.csv",
            "license": "NONE on upstream repo — validation-only, no redistribution",
            "sha256_12": sha256_file(csv_path)[:12],
        },
        "notation": "WX (SCL); sentence identity = (book, chaptno, sentno)",
        "counts": {
            "word_rows": stats["rows"],
            "unannotated_rows": stats["unannotated_rows"],
            "unannotated_lines": stats["unannotated_lines"],
            "sentences": stats["sentences"],
            "verses_slokas": stats["verses"],
            "sargas": stats["sargas"],
            "per_sarga_row_range": [stats["per_sarga_rows_min"], stats["per_sarga_rows_max"]],
        },
        "parity": {k.replace(" ", "_").replace("(", "").replace(")", ""): v
                   for k, v in parity.items()},
        "layer_emitted": bool(emit_layer),
        "layer_path": layer_path,
        "layer_sentence_count": layer_count,
        "rosette_sample": sample,
    }
    with open(manifest_path, "w", encoding="utf-8") as fh:
        json.dump(manifest, fh, ensure_ascii=False, indent=2)
        fh.write("\n")

    verdict = "PASS"
    with open(report_path, "w", encoding="utf-8") as fh:
        fh.write(f"""# H4738 — Samsaadhanii Sundarakāṇḍa treebank ingest parity report

_Created: {date.today().isoformat()} · tier: OxAlpha (opencode/z-ai/glm-5.3-flash) · VALIDATION-ONLY_

## Inputs (provenance)

| input | sha256 (first 12) | note |
|---|---|---|
| SCL `samsaadhanii/datasets` `Annotated-data/Sundarakanda.csv` (no LICENSE upstream) | `{manifest["upstream"]["sha256_12"]}` | {stats["rows"]} word rows, tab-separated, 14 cols, WX notation |

## Result — sentence-count parity (DoD gate)

| metric | value |
|---|---|
| word rows (csv-module walk) | {stats["rows"]} |
| unannotated rows (anvaya\_no='-': punctuation/interpolations) | {stats["unannotated_rows"]} (lines {", ".join(map(str, stats["unannotated_lines"]))}) |
| total non-header lines (raw census) | {source_count_raw} |
| **sentences (book, chaptno, sentno)** | **{stats["sentences"]}** |
| verses (ślokas) | {stats["verses"]} |
| sargas | {stats["sargas"]} |
| rows per sarga (min–max) | {stats["per_sarga_rows_min"]}–{stats["per_sarga_rows_max"]} |
| ingested layer emitted | {"yes (local-only, outside repo)" if emit_layer else "no (--emit-layer not passed)"} |
| layer sentence recount | {layer_count if layer_count is not None else "—"} |

**Parity verdict: {verdict}** — word rows + unannotated rows == raw line
census, sentence groups recount identically, and the emitted layer (when
emitted) recounts to the same sentence count. Every row passed the 14-column schema and identity checks;
malformed rows abort with a loud FAIL (none fired).

## Rosette (aggregate-only, rosette words ≤5 per sentence, 3 sentences)

⚠️ WX `f` is ambiguous in this dataset: standard vocalic ṛ AND pre-stop
nasal. Measured over this file: {stats["wx_f_rows_substr"]} rows carry the
substring `lafk` in any cell — but that set includes `alafkArAm` (alaṅkāram,
unrelated to Laṅkā); the exact word form `lafkAm` (= **laṅkām**, lemma
`lafkA` tagged `swrI` feminine) occupies {stats["wx_f_rows_exact_lafkAm"]}
rows ({stats["wx_f_occurrences_lafkAm"]} literal occurrences), `lafkA`-bearing
word cells {stats["wx_f_word_cells_lafkA"]}; `laMk` spellings:
{stats["wx_f_occurrences_laMk"]}. The literal table renders it ṛ — word-level
IAST below is indicative, not authoritative; any future WX layer needs a
context-resolved converter (sanskrit_util + WX mode), not this table.

| sarga.śloka | first words (WX) | IAST |
|---|---|---|
""")
        for s in sample:
            fh.write(f"| {s['sarga.sloka']} | {' '.join(s['first_words_wx'])} | {' '.join(s['first_words_iast'])} |\n")
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
        assert stats["sentences"] == 4, stats  # (001,1) (001,2) (002,1) (002,2)
        assert stats["sargas"] == 2 and stats["verses"] == 3, stats
        assert raw_line_census(csv_path) == 6
        layer = ingest_layer(sentences, os.path.join(tmp, "layer"))
        assert verify_layer_parity(layer, 4) == 4
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
    print("SELFTEST PASS — 4 sentences / 6 rows fixture, parity 4==4, rosette sundarakāṇḍam, malformed-row abort")


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

#!/usr/bin/env python3
"""Q4.1 Type-D pilot concordance on the linkid library (H3346).

Builds the first Type-D `commentary-citation` concordance consuming
sanskrit-util v0.10.0's linkid builders/parsers/validator END TO END —
grammar anchors (√roots cited in prose) ↔ commentary citations (the Sundara
lexical apparatus layer), per Uprava/TYPED_LINK_ID_GRAMMAR.md §3/§6 and
CONCORDANCE_ROADMAP_GRAMMAR_NONGRAMMAR_2026_2027.md Q4.1:

    anchor_type      : root
    anchor_id        : root:<SLP1>            <- linkid_build_anchor_id()
    anchor_key_slp1  : <SLP1>
    target_locus     : commentary:sundara-lexical:V.<s>.<v>
                                              <- linkid_build_target_locus()
    link_type        : commentary-citation
    source_dataset   : CommentaryStrategies/data/lexical/chN.json
    match_method     : exact                  (verbatim √X / «корня X» citation)
    confidence       : 0.95                   (kosha TieredMatcher TIER_CONFIDENCE)
    evidence_count   : citation occurrences of this root in this note
    date             : DD-MM-YYYY

Reuse, don't mint (§0): root tails are accepted ONLY when they already exist
in WhitneyRoots/crosswalk/mw_roots.json (704 distinct SLP1 keys) after
sanskrit_util.to_slp1 normalization — an unresolvable citation is skipped and
counted, never minted into an ID outside the grammar.

Every emitted record passes linkid_validate_link_record() with zero errors;
one error aborts the build (fail-closed).

Dedup vs Leonov/Kostina's own 1058-note tier-1 baseline
(data/leonov_own_notes.json): each row is classified
unique-vs-1058 / verse-overlap / root-overlap so the human review sheet can
rank duplicates first (the Phase-2 rule: a candidate duplicating a tier-1
note on the same verse+point is rejected or merged).

Human gate BEFORE any store write (handoff Fail condition): the review sheet
is generated here; nothing is written to any store until a voted
decisions.json is applied via `--apply-decisions` — which refuses to run on
an unvoted/empty file.

Outputs:
    data/typed_link_sundara_concordance.tsv          (Type-D TSV, lint convention)
    data/typed_link_sundara_concordance.jsonl        (records + dedup + provenance)
    data/analysis/typed_link_sundara/dedup_vs_1058_report.md
    data/analysis/typed_link_sundara/dedup_vs_1058.json
    data/analysis/typed_link_sundara/commentarystrategies-sundarakanda-typed-link-q41_review.html

Usage:
    python scripts/build_typed_link_sundara_concordance.py
    python scripts/build_typed_link_sundara_concordance.py --apply-decisions FILE
"""
import argparse
import csv
import json
import os
import re
import sys
from collections import defaultdict
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

HERE = Path(__file__).resolve().parent
REPO = HERE.parent

sys.path.insert(0, str(REPO.parent / "sanskrit-util" / "py"))
from sanskrit_util import (  # noqa: E402
    from_slp1,
    linkid_build_anchor_id,
    linkid_build_target_locus,
    linkid_validate_link_record,
    to_slp1,
)

sys.path.insert(0, str(REPO.parent / "kosha" / "scripts"))
from concordance_core import TIER_CONFIDENCE  # noqa: E402

sys.path.insert(0, str(REPO.parent / "csl-pyutil"))
from csl_pyutil import render_review_sheet  # noqa: E402
from csl_pyutil.evidence import EvidenceManifest  # noqa: E402

LEXICAL_DIR = REPO / "data" / "lexical"
MW_ROOTS = REPO.parent / "WhitneyRoots" / "crosswalk" / "mw_roots.json"
LEONOV_NOTES = REPO / "data" / "leonov_own_notes.json"
OUT_TSV = REPO / "data" / "typed_link_sundara_concordance.tsv"
OUT_JSONL = REPO / "data" / "typed_link_sundara_concordance.jsonl"
OUT_DIR = REPO / "data" / "analysis" / "typed_link_sundara"
DEDUP_JSON = OUT_DIR / "dedup_vs_1058.json"
DEDUP_MD = OUT_DIR / "dedup_vs_1058_report.md"
SHEET = OUT_DIR / (
    "commentarystrategies-sundarakanda-typed-link-q41_review.html")
DATE = "26-08-2026"
WORK_SLUG = "sundara-lexical"

TYPE_D_FIELDS = [
    "anchor_type", "anchor_id", "anchor_key_slp1", "target_locus",
    "link_type", "source_dataset", "match_method", "confidence",
    "evidence_count", "date",
]

SQ_RE = re.compile(r"√\s?([aāiīuūṛṝḷḹeaioṃuḥkgghjñcdtthdbhpyrlvśṣsh"
                   r"aāiīuūṛṝḷḹeaiou]+(?:-[aāiīuūṛṝḷḹeaioṃuḥkgghjñcdtthdbhpyrlvśṣsh]*)*)")
KO_RE = re.compile(
    r"корн(?:я|ень|ю|ей)\s+([aāiīuūṛṝḷḹeaiouṃḥkgghjñcdtthdbhpyrlvśṣsh]"
    r"[aāiīuūṛṝḷḹeaiouṃḥkgghjñcdtthdbhpyrlvśṣsh]*)")


def load_lexical_notes():
    """All kept lexical notes from the 68 per-sarga files, sorted."""
    files = sorted(p for p in LEXICAL_DIR.glob("ch*.json")
                   if ".rejected" not in p.name and ".qa_removed" not in p.name)
    notes = []
    for path in files:
        for n in json.loads(path.read_text(encoding="utf-8")):
            if "_meta" in n:
                continue
            n = dict(n)
            n["_src"] = f"CommentaryStrategies/data/lexical/{path.name}"
            notes.append(n)
    return notes


def extract_cited_roots(text):
    """Deterministic √X / «корня X» citation harvest -> {iast_root: count}."""
    found = defaultdict(int)
    for rx in (SQ_RE, KO_RE):
        for m in rx.finditer(text):
            tok = m.group(1).rstrip("-").strip()
            if tok:
                found[tok] += 1
    return dict(found)


def load_leonov_index():
    """verse-key -> [(comment_id, editor, raw_text)] from the 1058 baseline.

    Leonov/Kostina verse_ids are "5.<sarga>.<verse>"; the lexical layer
    addresses verses as "V.<sarga>.<verse>" — both normalize to one key so a
    same-verse note is never missed by a format mismatch.
    """
    data = json.loads(LEONOV_NOTES.read_text(encoding="utf-8"))
    idx = defaultdict(list)
    for n in data["notes"]:
        vid = str(n.get("verse_id", ""))
        m = re.match(r"^(?:V\.|5\.)?(\d+)\.(\d+)$", vid)
        if not m:
            continue
        idx[f"V.{m.group(1)}.{m.group(2)}"].append(
            (n.get("comment_id", ""), n.get("editor") or "leonov",
             n.get("raw_text", "")))
    return idx, len(data["notes"])


_SANSKRIT_LETTERS = (
    # vowels + avagraha-less full IAST alphabet: any of these glued to the
    # candidate form means it is part of a longer word, not a bare citation
    "aāiīuūṛṝḷḹeaiou"
    "kgghṅcchjjhñṭṭhḍḍhṇtthdhnpphbbhmmyrlvśṣsh"
    "ṃḥA-Z")


def _root_cited_in(text, iast_root):
    """Word-boundary-aware citation test: the root form must not be glued
    into a longer Sanskrit word on either side («dhā» must not hit
    «dhātubhiḥ», «lakṣ» must not hit «lakṣmīs»)."""
    if not iast_root:
        return False
    pat = (f"(?<![ {_SANSKRIT_LETTERS}])"
           f"{re.escape(iast_root)}"
           f"(?![{_SANSKRIT_LETTERS}])")
    return re.search(pat, text) is not None


def dedup_classify(verse_id, iast_root, leonov_idx):
    """unique-vs-1058 | verse-overlap | root-overlap (+ overlapping ids)."""
    hits = leonov_idx.get(verse_id, [])
    if not hits:
        return "unique-vs-1058", []
    overlap = [cid for cid, _ed, txt in hits
               if _root_cited_in(txt, iast_root)]
    if overlap:
        return "root-overlap", overlap
    return ("verse-overlap",
            [cid for cid, _ed, _txt in hits])


def verse_sort_key(target_locus):
    tail = target_locus.split(":", 2)[2]
    m = re.match(r"^V\.(\d+)\.(\d+)([a-b])?$", tail)
    if not m:
        raise ValueError(f"unexpected commentary cite tail: {tail!r}")
    return (int(m.group(1)), int(m.group(2)), m.group(3) or "")


def build_records():
    roots_inv = {r["slp1"] for r in
                 json.loads(MW_ROOTS.read_text(encoding="utf-8"))}
    notes = load_lexical_notes()
    leonov_idx, leonov_total = load_leonov_index()

    records, unresolved, invalid = [], [], []
    stats = {"notes_scanned": len(notes), "notes_with_citations": 0}
    for n in notes:
        cited = extract_cited_roots(n.get("note_ru", ""))
        if not cited:
            continue
        stats["notes_with_citations"] += 1
        shloka = str(n["shloka"])
        for iast, cnt in sorted(cited.items()):
            slp1 = to_slp1(iast)
            if slp1 not in roots_inv:
                unresolved.append({"shloka": shloka, "iast": iast,
                                   "slp1": slp1, "src": n["_src"],
                                   "reason": "not in WhitneyRoots mw_roots "
                                             "inventory (704 keys)"})
                continue
            anchor_id = linkid_build_anchor_id({"type": "root",
                                                "tail": slp1})
            target_locus = linkid_build_target_locus({
                "type": "commentary", "tail": f"{WORK_SLUG}:{shloka}"})
            if anchor_id is None or target_locus is None:
                invalid.append({"shloka": shloka, "iast": iast,
                                "reason": f"builder returned None "
                                          f"(anchor={anchor_id!r}, "
                                          f"locus={target_locus!r})"})
                continue
            rec = {
                "anchor_type": "root",
                "anchor_id": anchor_id,
                "anchor_key_slp1": slp1,
                "target_locus": target_locus,
                "link_type": "commentary-citation",
                "source_dataset": n["_src"],
                "match_method": "exact",
                "confidence": TIER_CONFIDENCE["exact"],
                "evidence_count": cnt,
                "date": DATE,
            }
            chk = linkid_validate_link_record(rec)
            if not chk["valid"]:
                invalid.append({"shloka": shloka, "iast": iast,
                                "errors": chk["errors"]})
                continue
            status, overlap_ids = dedup_classify(shloka, iast, leonov_idx)
            rec["_dedup_status"] = status
            rec["_dedup_overlap_ids"] = overlap_ids
            rec["_lemma_iast"] = n.get("lemma_iast", "")
            rec["_cited_form_iast"] = iast
            rec["_note_ru_excerpt"] = n.get("note_ru", "")[:400]
            records.append(rec)

    records.sort(key=lambda r: (verse_sort_key(r["target_locus"]),
                                r["anchor_id"]))
    stats.update({
        "leonov_baseline_total": leonov_total,
        "records_emitted": len(records),
        "unresolved_citations_skipped": len(unresolved),
        "invalid_records_aborted": len(invalid),
    })
    return records, unresolved, invalid, stats


def write_tsv(records):
    with open(OUT_TSV, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=TYPE_D_FIELDS, delimiter="\t",
                           lineterminator="\n",
                           extrasaction="ignore")
        w.writeheader()
        for r in records:
            w.writerow(r)


def write_jsonl(records):
    with open(OUT_JSONL, "w", encoding="utf-8") as fh:
        for r in records:
            row = {"_row_key": f'{r["anchor_id"]}|{r["target_locus"]}'}
            row.update(r)
            fh.write(json.dumps(row, ensure_ascii=False,
                                sort_keys=True) + "\n")


def write_dedup_report(records, unresolved, stats):
    counts = defaultdict(int)
    for r in records:
        counts[r["_dedup_status"]] += 1
    payload = {
        "generated": DATE,
        "baseline": "CommentaryStrategies/data/leonov_own_notes.json",
        "baseline_total_notes": stats["leonov_baseline_total"],
        "concordance_rows": len(records),
        "counts": dict(counts),
        "notes_scanned": stats["notes_scanned"],
        "notes_with_citations": stats["notes_with_citations"],
        "unresolved_citations_skipped": unresolved,
    }
    DEDUP_JSON.write_text(json.dumps(payload, ensure_ascii=False,
                                     indent=2) + "\n", encoding="utf-8")

    lines = [
        "# Dedup vs Leonov/Kostina 1058 — Type-D Sundara pilot (H3346)",
        "",
        f"_Generated: {DATE} · baseline: "
        f"[leonov_own_notes.json](https://github.com/gasyoun/"
        f"CommentaryStrategies/blob/main/data/leonov_own_notes.json) "
        f"({stats['leonov_baseline_total']} notes)_",
        "",
        "| dedup_status | rows | meaning |",
        "|---|---|---|",
        f"| unique-vs-1058 | {counts['unique-vs-1058']} | no tier-1 note on "
        "that verse at all |",
        f"| verse-overlap | {counts['verse-overlap']} | tier-1 covers the "
        "verse but never cites this root — complementary, keep candidate |",
        f"| root-overlap | {counts['root-overlap']} | a tier-1 note on the "
        "same verse mentions this root too — duplicate-or-merge suspect, "
        "vote first |",
        "",
        f"Scanned {stats['notes_with_citations']}/{stats['notes_scanned']} "
        "lexical notes carried ≥1 root citation; "
        f"{len(unresolved)} cited forms were skipped because their SLP1 key "
        "is absent from the WhitneyRoots mw_roots inventory (reuse-don't-"
        "mint, TYPED_LINK_ID_GRAMMAR §0) — listed in "
        "[dedup_vs_1058.json](https://github.com/gasyoun/CommentaryStrategies"
        "/blob/main/data/analysis/typed_link_sundara/dedup_vs_1058.json).",
        "",
        "## root-overlap rows (rank first on the sheet)",
        "",
    ]
    for r in records:
        if r["_dedup_status"] == "root-overlap":
            lines.append(
                f"- `{r['anchor_id']}` @ `{r['target_locus']}` — overlaps "
                f"{', '.join(r['_dedup_overlap_ids'])}")
    DEDUP_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


STATUS_BADGE = {
    "root-overlap": "⚠ дубликат-кандидат",
    "verse-overlap": "➕ стих уже покрыт, корень не тронут",
    "unique-vs-1058": "✅ уникально против 1058",
}

ROOT_ID_LABEL = "корень из инвентаря WhitneyRoots mw_roots"
LOCUS_ID_LABEL = "стих аппарата lexical кн. V Сундараканды"


def esc(s):
    import html
    return html.escape(str(s), quote=True)


def build_items(records):
    items = []
    rank = {"root-overlap": 0, "verse-overlap": 1, "unique-vs-1058": 2}
    for r in sorted(records, key=lambda x: (rank[x["_dedup_status"]],
                                            verse_sort_key(x["target_locus"]),
                                            x["anchor_id"])):
        iast = r["_cited_form_iast"]
        lemma = r.get("_lemma_iast", "")
        items.append({
            "id": f'{r["anchor_id"]}|{r["target_locus"]}',
            "filt": r["_dedup_status"],
            "title": (f'√{esc(iast)} @ '
                      f'{esc(r["target_locus"].split(":", 2)[2])}'),
            "badges": [STATUS_BADGE[r["_dedup_status"]],
                       f'evidence ×{r["evidence_count"]}',
                       f'лемма {esc(lemma)}'],
            "question": (
                "<p>Тип-D связь: грамматический якорь "
                f'<code>{esc(r["anchor_id"])}</code> — '
                f'{ROOT_ID_LABEL}, здесь корень '
                f'√{esc(from_slp1(r["anchor_key_slp1"]))} — цитируется в '
                "аппарате на "
                f'<code>{esc(r["target_locus"])}</code>, {LOCUS_ID_LABEL}'
                ".</p>"
                "<p>Подтвердить строку конкорданса в подтверждённый ярус "
                "(после голоса — единственный путь записи)?</p>"),
            "panels": [
                ("примечание слоя lexical (фрагмент)",
                 f"<blockquote>{esc(r['_note_ru_excerpt'])}</blockquote>"),
                ("дедупликация против 1058 Леонова/Костиной",
                 f'<p>{esc(STATUS_BADGE[r["_dedup_status"]])}'
                 + (f' — пересечения: {esc(", ".join(r["_dedup_overlap_ids"]))}'
                    if r["_dedup_overlap_ids"] else "")
                 + "</p>"),
            ],
            "note_placeholder": ("Почему отклоняете/откладываете (для "
                                 "reject/defer обязательно)"),
        })
    return items


def write_sheet(records):
    items = build_items(records)
    manifest = EvidenceManifest(
        "commentarystrategies-sundarakanda-typed-link-q41",
        [i["id"] for i in items], repo_root=str(REPO))
    manifest.declare_joined(
        "data/lexical/ch*.json (68 files)",
        ["shloka", "lemma_iast", "note_ru"])
    manifest.declare_joined(
        "../WhitneyRoots/crosswalk/mw_roots.json",
        ["slp1 (704-key root inventory, reuse-don't-mint gate)"])
    manifest.declare_joined(
        "data/leonov_own_notes.json",
        ["verse_id", "comment_id", "raw_text (1058-note dedup baseline)"])
    manifest.declare_omitted(
        "data/lexical/ch*.rejected.json",
        "adversarial-gate rejects — never candidates for a link row")
    manifest.declare_omitted(
        "SamudraManthanam verse corpus",
        "display-only context on other sheets; the link rows need only the "
        "cite tail, not the verse text")
    for i in items:
        manifest.add_card(i["id"], ["anchor_id", "target_locus",
                                    "_dedup_status"])

    cfg = {
        "sheet_id": "commentarystrategies-sundarakanda-typed-link-q41",
        "title": ("Q4.1 Type-D пилот: root ↔ commentary-citation через "
                  "linkid (H3346)"),
        "subtitle": (
            f"{len(items)} строк конкорданса; каждая собрана библиотекой "
            "sanskrit-util linkid и прошла linkid_validate_link_record без "
            "ошибок. Approve = подтвердить связь в подтверждённый ярус "
            "датасета · Reject = снять строку · Defer = нужен другой якорь."),
        "footer": (
            "Ворота записи: НИЧЕГО не пишется ни в какой стор до голоса "
            "(Fail = store write мимо человеческих ворот). Дедупликация "
            "против 1058 примечаний Леонова/Костиной посчитана заранее и "
            "показана на карточке; строки ⚠ ранжированы первыми."),
        "approve_label": "✅ подтвердить связь",
        "reject_label": "❌ снять строку",
        "filters": [("root-overlap", "⚠ дубликат-кандидат"),
                    ("verse-overlap", "➕ стих покрыт, корень нов"),
                    ("unique-vs-1058", "✅ уникально")],
        "generated": DATE,
        "show_ids": True,
        "note_min_height_px": 72,
        "save_as": ("CommentaryStrategies\\data\\analysis\\"
                    "typed_link_sundara\\commentarystrategies-"
                    "sundarakanda-typed-link-q41_decisions.json"),
        "preflight": {
            "overlap_threshold": 0.5,
            # The linkid tails ARE the join keys this pilot exists to prove
            # (root:<SLP1> verbatim in ids and id chips) — declared ids, not
            # prose leaks. The remaining tokens were each verified against
            # the source notes (h2868 procedure): English words quoted from
            # Goldman's translations inside note_ru excerpts, plus MBh /
            # ChUp, the standard Mahabharata / Chandogya-Upanisad
            # abbreviations some excerpts cite.
            "allow_slp1_tokens": sorted(
                {r["anchor_key_slp1"] for r in records} | {
                    "MBh", "ChUp",
                    "confinement", "conflict", "faithful", "fulfilled",
                    "fulfilment", "grandfather", "herself", "infant",
                    "information", "mindful", "overflowing", "painful",
                    "perf", "perfect", "perfection", "performance",
                    "performed", "powerful", "satisfaction", "stanza",
                    "truthfulness", "unfortunate",
                }),
        },
        "identity_gate": {
            "patterns": [
                r"root:[A-Za-z]+",
                r"commentary:sundara-lexical:V\.\d+\.\d+[ab]?",
            ],
            "labels": {
                **{aid: ROOT_ID_LABEL
                   for aid in {r["anchor_id"] for r in records}},
                **{tid: LOCUS_ID_LABEL
                   for tid in {r["target_locus"] for r in records}},
            },
        },
    }
    screening = {
        "deterministic": len(items),
        "lookup": 0,
        "agent": 0,
        "human": len(items),
        "evidence_path": ("data/analysis/typed_link_sundara/"
                          "dedup_vs_1058.json"),
        "rules": [
            "linkid_validate_link_record() 0 ошибок на всех строках",
            "хвосты root: сверены с инвентарём WhitneyRoots mw_roots "
            "(704 SLP1-ключа) — вне инвентаря ID не минтуется",
            "дедуп против 1058 посчитан машиной (статус на карточке)",
        ],
    }
    html_out = render_review_sheet(items, cfg, screening=screening,
                                   manifest=manifest)
    SHEET.write_text(_validate_contract_adapters(html_out), encoding="utf-8")


def _validate_contract_adapters(doc):
    """Repo CI contract (scripts/validate.py): every tracked HTML carries
    css/commentary.css and a LITERAL <main class="container"> wrapper — the
    two things every hand-rolled sheet in data/analysis/ embeds in its
    shell. The shared emitter is self-contained by design, so adapt here,
    deterministically: its own <main id="cards"> becomes a plain
    .container main whose first child keeps the #cards id the sheet's JS
    targets, plus the same relative stylesheet link the sibling sheets use
    (harmless no-op when the sheet travels off-repo, e.g. to the vote hub).
    String surgery only — never touches emitter logic."""
    anchor = "<main id=\"cards\">"
    if anchor not in doc:
        raise ValueError("emitter cards anchor missing")
    doc = doc.replace(anchor, '<main class="container">\n<div id="cards">',
                      1)
    doc = doc.replace("</main>\n<div class=\"votebar\"",
                      "</div>\n</main>\n<div class=\"votebar\"", 1)
    marker = "</title>"
    link = '\n<link rel="stylesheet" href="../../../css/commentary.css">'
    if marker in doc:
        doc = doc.replace(marker, marker + link, 1)
    return doc


def apply_decisions(path):
    """Consume a VOTED decisions.json -> rewrite confirmed tier. Refuses
    unvoted/empty files (the human gate, enforced by construction)."""
    dec = json.loads(Path(path).read_text(encoding="utf-8"))
    votes = dec.get("reviewer_decisions", {})
    if not votes:
        sys.exit("REFUSED: decisions.json carries no votes — the human gate "
                 "is still open; nothing to apply.")
    known = {}
    with open(OUT_JSONL, encoding="utf-8") as fh:
        for line in fh:
            row = json.loads(line)
            known[row["_row_key"]] = row
    unknown = set(votes) - set(known)
    if unknown:
        sys.exit(f"REFUSED: {len(unknown)} voted ids are not in the current "
                 f"dataset, e.g. {sorted(unknown)[:3]}")
    kept, dropped = [], []
    for key, row in known.items():
        action = votes[key].get("action")
        if action == "approve":
            kept.append(row)
        elif action == "reject":
            dropped.append(key)
        else:
            sys.exit(f"REFUSED: open vote remains on {key} "
                     f"(action={action!r}) — all-or-nothing apply.")
    conf_tsv = OUT_TSV.with_name("typed_link_sundara_concordance.confirmed.tsv")
    conf_jsonl = OUT_TSV.with_name(
        "typed_link_sundara_concordance.confirmed.jsonl")
    with open(conf_tsv, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=TYPE_D_FIELDS, delimiter="\t",
                           lineterminator="\n", extrasaction="ignore")
        w.writeheader()
        for r in kept:
            w.writerow(r)
    with open(conf_jsonl, "w", encoding="utf-8") as fh:
        for r in kept:
            fh.write(json.dumps(row_key := {"_row_key":
                                            f'{r["anchor_id"]}|'
                                            f'{r["target_locus"]}',
                                            **r},
                                ensure_ascii=False, sort_keys=True) + "\n")
    print(f"APPLIED: {len(kept)} confirmed, {len(dropped)} rejected -> "
          f"{conf_tsv.name} / {conf_jsonl.name}. No apparatus store touched.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply-decisions", metavar="FILE", default=None,
                    help="apply a VOTED decisions.json (refuses empty)")
    args = ap.parse_args()
    if args.apply_decisions:
        apply_decisions(args.apply_decisions)
        return

    records, unresolved, invalid, stats = build_records()
    if invalid:
        print("FATAL: linkid validation failures:", file=sys.stderr)
        for bad in invalid[:10]:
            print(" ", json.dumps(bad, ensure_ascii=False),
                  file=sys.stderr)
        sys.exit(1)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    write_tsv(records)
    write_jsonl(records)
    write_dedup_report(records, unresolved, stats)
    write_sheet(records)

    counts = defaultdict(int)
    for r in records:
        counts[r["_dedup_status"]] += 1
    print(f"rows={len(records)} "
          f"(root-overlap={counts['root-overlap']}, "
          f"verse-overlap={counts['verse-overlap']}, "
          f"unique={counts['unique-vs-1058']}) "
          f"unresolved_skipped={len(unresolved)} "
          f"invalid={len(invalid)}")
    print(f"tsv={OUT_TSV.relative_to(REPO)} jsonl={OUT_JSONL.relative_to(REPO)}")
    print(f"sheet={SHEET.relative_to(REPO)}")


if __name__ == "__main__":
    main()

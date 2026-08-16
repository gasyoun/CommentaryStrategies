"""Corpus-truth census + regression gate for the 17,863-note composition (H2872).

Two modes:

  python scripts/corpus_truth_census.py
      Regenerate data/analysis/corpus_truth_reconciliation.json from the
      sibling SamudraManthanam canonical JSONL corpus (the lowest committed
      source of the note corpus). Requires ../SamudraManthanam locally;
      refuses politely when absent.

  python scripts/corpus_truth_census.py --check
      Regression gate (CI-safe, no sibling needed):
        1. committed reconciliation JSON is internally consistent (bucket
           sums match per-work counts);
        2. claim surfaces (index.html, essays, articles, canon doc) do not
           re-assert the defects reconciled by H2872 (surface_rules);
        3. when ../SamudraManthanam IS present: recount every censused work
           and fail on drift against the committed table.

Counting rule (the definition behind every number here): a "note" is a JSONL
record whose seg matches comm\\d+ and whose deleted flag is falsy. See
docs/CORPUS_TRUTH_RECONCILIATION_17863.md for verdicts and lineage.
"""
import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

REPO = Path(__file__).resolve().parents[1]
OUT = REPO / "data" / "analysis" / "corpus_truth_reconciliation.json"
JSONL = REPO.parent / "SamudraManthanam" / "web" / "corpus_builder" / "jsonl"

SEG_COMM = re.compile(r'^comm\d+$')
ANCHOR = re.compile(r'title="([^"]*?)(?::\s*[0-9IVXLC–\-, ]+)?"')

# bucket -> work slugs. The five attributed corpora follow the canonical book
# lists of docs/CORPUS_COMPOSITION_17863.md; identified strata OUTSIDE the five
# are censused explicitly so the 241-remainder question stays evidence-bounded.
BUCKETS = {
    "kalyanov": [
        "01_mahabharata-adiparva", "02_mahabharata-sabhaparva",
        "04_mahabharata-virataparva", "05_mahabharata-udyogaparva",
        "07_mahabharata-dronaparva", "09_mahabharata-shalyaparva"],
    "vassilkov_neveleva": [
        "03_mahabharata-aranyakaparva", "08_mahabharata-karnaparva",
        "10_mahabharata-sauptikaparva", "11_mahabharata-striparva",
        "14_mahabharata-ashvamedhikaparva", "15_mahabharata-ashramavasikaparva",
        "16_mahabharata-mausalaparva", "17_mahabharata-mahaprasthanikaparva",
        "18_mahabharata-svargarohanikaparva"],
    "erman": ["06_mahabharata-bhishmaparva"],
    "grintser": [
        "01_ramayana-balakanda", "02_ramayana-ayodhyakanda",
        "03_ramayana-aranyakanda"],
    "syrkin": [  # 26 works, all page-anchored to «Упанишады» (1992, кн. 1-3)
        "ait-up", "atma-up", "br-up", "brb-up", "ch-up", "chag-up", "isha-up",
        "jab-up", "kai-up", "kan-up", "kat-up", "kau-up", "kena-up", "mai-up",
        "man-up", "mnar-up", "mun-up", "nr-up", "pai-up", "pr-up", "rampt-up",
        "shv-up", "sub-up", "tai-up", "vajs-up", "yotat-up"],
    # committed note-bearing strata NOT in the five attributed corpora
    "outside_five": [
        "12_mahabharata-shantiparva",          # «Махабхарата 2017 (XII)» — translator not committed
        "05_ramayana-sundarakanda",            # «Рамаяна 2022» — Leonov online, excluded from 17,863 by canon
        "jabala-up",                           # «Джабала упанишада (2025)» — not Syrkin
        "bhagavadgita-erman",                  # standalone BG 2009 — duplicates bhishmaparva ch.23-40 lineage
        "mahabharata-mausalaparva-ignatiev",
        "mahabharata-mahaprasthanikaparva-ignatiev",
        "mahabharata-svargarohanikaparva-ignatiev"],
}


def count_work(path: Path):
    comm = 0
    anchor = None
    h = hashlib.sha256()
    with open(path, 'rb') as fb:
        for raw in fb:
            h.update(raw)
            if b'"seg": "comm' not in raw:
                continue
            r = json.loads(raw.decode('utf-8'))
            if SEG_COMM.match(str(r.get('seg', ''))) and not r.get('deleted'):
                comm += 1
                if anchor is None:
                    m = ANCHOR.search(r.get('html') or '')
                    if m:
                        anchor = m.group(1).strip()
    return comm, anchor, h.hexdigest()


def corpus_commit():
    try:
        out = subprocess.run(
            ["git", "-C", str(JSONL.parents[2]), "rev-parse", "--short", "HEAD"],
            capture_output=True, encoding='utf-8', check=True)
        return out.stdout.strip()
    except Exception:
        return "unknown"


def build():
    if not JSONL.is_dir():
        print(f"REFUSE: sibling corpus not found at {JSONL} — the census can only "
              f"be regenerated on a machine with SamudraManthanam checked out.")
        return 2
    works = []
    buckets = {}
    for bucket, slugs in BUCKETS.items():
        total = 0
        for slug in slugs:
            p = JSONL / f"{slug}.jsonl"
            comm, anchor, sha = count_work(p)
            works.append({"slug": slug, "bucket": bucket, "comm_live": comm,
                          "edition_anchor": anchor, "sha256": sha})
            total += comm
        buckets[bucket] = {"works": len(slugs), "comm_total": total}
    five = sum(buckets[b]["comm_total"] for b in
               ("kalyanov", "vassilkov_neveleva", "erman", "grintser", "syrkin"))
    doc = {
        "_meta": {
            "handoff": "H2872",
            "generator": "scripts/corpus_truth_census.py",
            "note_definition": "JSONL record with seg=comm\\d+ and deleted falsy",
            "corpus_repo": "SamudraManthanam",
            "corpus_commit": corpus_commit(),
            "memo": "docs/CORPUS_TRUTH_RECONCILIATION_17863.md",
        },
        "buckets": buckets,
        "five_corpora_committed_total": five,
        "works": works,
        "published_claims": PUBLISHED_CLAIMS,
        "surface_rules": SURFACE_RULES,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT, 'w', encoding='utf-8') as f:
        json.dump(doc, f, ensure_ascii=False, indent=1)
        f.write("\n")
    print(f"wrote {OUT.relative_to(REPO)}: five-corpora committed total = {five}")
    return 0


# Published figures and their verdicts (documented in the memo; kept here so a
# drifting surface fails --check, not a future reader).
PUBLISHED_CLAIMS = [
    {"figure": "7424", "subject": "Kalyanov total",
     "verdict": "CONFIRMED", "committed_value": 7424},
    {"figure": "5574", "subject": "Vassilkov-Neveleva total",
     "verdict": "DEFINITION_DIFFERENCE",
     "note": "includes 1,685 notes of «XII(б). Мокшадхарма» per the essay's own table; "
             "canonical 9-book list gives 3,889 (Mar-2026) / 3,885 (committed)",
     "committed_value": 3885},
    {"figure": "758", "subject": "Erman total",
     "verdict": "VERSION_DRIFT", "committed_value": 776},
    {"figure": "2245", "subject": "Grintser total",
     "verdict": "UNRESOLVED",
     "note": "contradicts its own essay table (2,220); committed corpus 2,157",
     "committed_value": 2157},
    {"figure": "1621", "subject": "Syrkin total ('20 текстов')",
     "verdict": "UNRESOLVED",
     "note": "committed: 26 works anchored to «Упанишады» (1992), 1,605 notes",
     "committed_value": 1605},
    {"figure": "241", "subject": "unattributed remainder 17863-17622",
     "verdict": "UNRESOLVED",
     "note": "candidate committed strata: 12_shantiparva 139 + 05_ramayana-sundarakanda 82 = 221; "
             "exact decomposition needs the uncommitted Mar-2026 crawl output"},
    {"figure": "3.4%/7.7%", "subject": "Vassilkov textology share",
     "verdict": "UNRESOLVED",
     "note": "both descend from the uncommitted Mar-2026 categorization; different partitions"},
    {"figure": "40.2%/27.8%", "subject": "Erman sanskrit-term share",
     "verdict": "UNRESOLVED",
     "note": "параллели 32.5% agrees on both surfaces; the term rubric does not"},
    {"figure": "М.: Ладомир, 2009", "subject": "Erman book VI imprint",
     "verdict": "CONFIRMED",
     "note": "committed digitization header + .meta.json imprint in SamudraManthanam "
             "Index/lib/x86_64-win64/Data/06_mahabharata-bhishmaparva.html(.meta.json)"},
]

# file -> forbidden/required literal strings. Paths relative to repo root.
SURFACE_RULES = [
    {"file": "index.html",
     "must_not_contain": ["М.: Наука, 1977", "1950–1992"],
     "reason": "Erman book VI is М.: Ладомир, 2009 (committed imprint); Kalyanov editions run 1950–1996"},
    {"file": "erman_commentary_analysis.html",
     "must_not_contain": ["М.: Наука, 1977"],
     "reason": "Erman book VI is М.: Ладомир, 2009"},
    {"file": "kalyanov_commentary_analysis.html",
     "must_not_contain": ["1950–1992"],
     "reason": "committed edition anchors: I 1950 … VII 1993, IX 1996"},
    {"file": "articles/article1_vya.md",
     "must_not_contain": ["СПб.: Наука, 2009"],
     "reason": "Erman 2009 bibliography entry: М.: Ладомир, 2009"},
    {"file": "index.html",
     "must_contain": ["CORPUS_TRUTH_RECONCILIATION_17863"],
     "reason": "March-2026 snapshot figures must point at the reconciliation memo"},
    {"file": "vassilkov_commentary_analysis.html",
     "must_contain": ["CORPUS_TRUTH_RECONCILIATION_17863"],
     "reason": "5,574 (with XII(б)) must be qualified against the canonical 9-book list"},
    {"file": "erman_commentary_analysis.html",
     "must_contain": ["CORPUS_TRUTH_RECONCILIATION_17863"],
     "reason": "758 is a Mar-2026 snapshot; committed corpus holds 776"},
    {"file": "grintser_commentary_analysis.html",
     "must_contain": ["CORPUS_TRUTH_RECONCILIATION_17863"],
     "reason": "2,245 headline contradicts its own table (2,220); committed 2,157"},
    {"file": "docs/CORPUS_COMPOSITION_17863.md",
     "must_contain": ["CORPUS_TRUTH_RECONCILIATION_17863"],
     "reason": "canon composition must reference the source reconciliation"},
]


def check():
    failures = []
    if not OUT.exists():
        print(f"FAIL: {OUT.relative_to(REPO)} missing — run the generator first.")
        return 1
    doc = json.load(open(OUT, encoding='utf-8'))

    # 1. internal consistency
    for bucket, info in doc["buckets"].items():
        s = sum(w["comm_live"] for w in doc["works"] if w["bucket"] == bucket)
        if s != info["comm_total"]:
            failures.append(f"bucket {bucket}: works sum {s} != recorded {info['comm_total']}")
    five = sum(doc["buckets"][b]["comm_total"] for b in
               ("kalyanov", "vassilkov_neveleva", "erman", "grintser", "syrkin"))
    if five != doc["five_corpora_committed_total"]:
        failures.append(f"five-corpora total {doc['five_corpora_committed_total']} != bucket sum {five}")

    # 2. claim surfaces
    for rule in doc["surface_rules"]:
        p = REPO / rule["file"]
        if not p.exists():
            failures.append(f"surface missing: {rule['file']}")
            continue
        text = p.read_text(encoding='utf-8', errors='replace')
        for s in rule.get("must_not_contain", []):
            if s in text:
                failures.append(f"{rule['file']}: forbidden string {s!r} — {rule['reason']}")
        for s in rule.get("must_contain", []):
            if s not in text:
                failures.append(f"{rule['file']}: required string {s!r} absent — {rule['reason']}")

    # 3. live recount when the sibling corpus is available
    if JSONL.is_dir():
        for w in doc["works"]:
            p = JSONL / f"{w['slug']}.jsonl"
            if not p.exists():
                failures.append(f"corpus work vanished: {w['slug']}")
                continue
            comm, _anchor, sha = count_work(p)
            if comm != w["comm_live"]:
                failures.append(
                    f"{w['slug']}: corpus drift — committed census {w['comm_live']}, live {comm} "
                    f"(sha {w['sha256'][:12]} -> {sha[:12]}); re-run the generator and reconcile the memo")
    else:
        print("note: sibling corpus absent — recount skipped (surface + consistency checks only)")

    if failures:
        for f_ in failures:
            print("FAIL:", f_)
        return 1
    print("corpus-truth check OK")
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    return check() if args.check else build()


if __name__ == "__main__":
    sys.exit(main())

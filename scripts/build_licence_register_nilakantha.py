"""H2860 — tradition-attested Pāṇini-deviation register from Nīlakaṇṭha's Bhāratabhāvadīpa.

Word-anchored आर्ष / छान्दस sweep over the whole Nīlakaṇṭha vulgate ṭīkā, plus a
per-parvan density census, plus the register itself (locus, commentator,
defense_term, deviation_type, quote), plus the fold-in of the 27 Bhagavadgītā
probe rows with their multi-commentator agreement column.

Input (gitignored, rights-gated — see mahabharata-nilakantha/NILAKANTHA_VULGATE_CENSUS.md):
    mahabharata-nilakantha/nilakantha_vulgate_full.jsonl
Restore it with:
    python mahabharata-nilakantha/nilakantha_parser.py scrape

Outputs (all under data/licence_register/):
    nilakantha_parvan_density.tsv                    per-parvan density census
    commentary_licence_register_nilakantha.tsv/.jsonl  the register
    nilakantha_licence_rejected.tsv                  every rejected hit + reason
    commentary_licence_register_combined.tsv/.jsonl    Nīlakaṇṭha + Gītā probe rows

Hand rulings (the ~25 % the machine cannot classify) are NOT recomputed here — they
are read from the committed nilakantha_hand_rulings.json so the build stays
deterministic and the philology stays reviewable.

Usage:
    python scripts/build_licence_register_nilakantha.py
    python scripts/build_licence_register_nilakantha.py --emit-hand-queue   # for a re-ruling pass
"""
import argparse
import csv
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "mahabharata-nilakantha", "nilakantha_vulgate_full.jsonl")
OUTDIR = os.path.join(ROOT, "data", "licence_register")
RULINGS = os.path.join(OUTDIR, "nilakantha_hand_rulings.json")
GITA_TSV = os.path.join(OUTDIR, "commentary_licence_register_bhagavadgita_probe.tsv")

COMMENTATOR = "nīlakaṇṭhaḥ"
WORK = "Mahābhārata (vulgate, Nīlakaṇṭha recension)"

PARVA_ORDER = [
    "adiparva", "sabhaparva", "vanaparva", "virataparva", "udyogaparva",
    "bhishmaparva", "dronaparva", "karnaparva", "shalyaparva", "sauptikaparva",
    "striparva", "shantiparva", "anushasanaparva", "ashwamedhikaparva",
    "ashramavasikaparva", "mausalaparva", "mahaprasthanikaparva", "swargarohanaparva",
]

# ---------------------------------------------------------------------------
# 1. The word-anchored pattern
# ---------------------------------------------------------------------------
# In Devanagari the IAST substring trap (pārṣada / kārṣīr / vārṣika dragging
# precision from 100 % to 37 %) does NOT exist: आ is an INDEPENDENT vowel sign, so
# "आर्ष" can only stand at the head of a word — a compound-internal ārṣa is written
# with the dependent ा (…सार्ष…) and never matches. The script does the anchoring.
#
# What DOES bite in Devanagari is a different, smaller class: unrelated *stems* that
# happen to begin आर्ष — the patronymics आर्ष्टिषेण (Ārṣṭiṣeṇa) and आर्ष्यशृङ्गि
# (Ārṣyaśṛṅgi), the bull-adjective आर्षभ (ārṣabha < ṛṣabha), and the gotra-term
# आर्षेय (ārṣeya). Those are excluded by a negative lookahead, not by hand.
#
# छान्दस is CONSONANT-initial, so no such anchor is available — and none is needed.
# Measured on this corpus: 30 of 30 occurrences are licence-claims. Two thirds of them
# sit at a sandhi junction (…नुमभावच्छान्दसः, …सुपो डादेशश्छान्दसः) or inside a solid
# compound (…असन्धिप्रछान्दसः), exactly where a lookbehind on "no preceding Devanagari
# letter" would have destroyed them — the Devanagari twin of the report's own note that
# a licence term legitimately follows a hyphen in IAST. The five-akṣara sequence
# छ + ा + न् + द + स is not a substring of any unrelated Sanskrit stem, so the term
# needs no anchor; the recall cost of adding one is 16 of 30 rows.
ARSA = r"आर्ष(?!्ट|्य|भ|ेय)"
CHANDASA = r"छान्दस"
HIT_RE = re.compile(rf"(?:(?<![ऀ-ॿ])(?P<a>{ARSA})|(?P<c>{CHANDASA}))")
# Token: the whole inflected word carrying the licence term — letters only, so a
# clause-final "आर्षः॥१॥" yields the word, not the daṇḍa and the verse number.
TOKEN_RE = re.compile(r"[ऀ-ॣॱ-ॿ]+")
# The scrape carries stray ZWNJ/ZWJ inside words (…त‌ङ्भाव…); they are invisible
# to a reader and fatal to a regex, so they are stripped before any matching.
ZW_RE = re.compile("[​‌‍]")

# ---------------------------------------------------------------------------
# 2. deviation_type — auto-derived from the grammatical noun Nīlakaṇṭha names
#    beside the licence word. Longest / most specific first.
# ---------------------------------------------------------------------------
# NOTE on the patterns below. Nīlakaṇṭha names the grammatical operation in running
# sandhi, so a VOWEL-INITIAL technical term loses its initial vowel to the orthography:
# अडभाव appears as …इत्यडभाव / …त्राडभाव, आडभाव as ङितामाडभाव, अन्तादेश as आकारोन्तादेश,
# अडागम as …पूर्वोऽडागम (behind an avagraha). Matching the citation form alone silently
# drops those rows into the hand queue, so vowel-initial triggers are written with the
# initial vowel optional — `[अआा]?डभाव` — with the more specific variants ordered first.
LEXICON = [
    # (Sanskrit trigger, deviation_type, the Sanskrit technical term as printed)
    (r"अभ्यासलोप",              "elision — reduplication syllable", "abhyāsa-lopa"),
    (r"सम्प्रसारणाभाव|संप्रसारणाभाव", "absence of saṃprasāraṇa", "saṃprasāraṇa-abhāva"),
    (r"पदविकरणव्यत्यय",         "transfer — stem-class (vikaraṇa)", "pada-vikaraṇa-vyatyaya"),
    (r"आर्द्धधातुकत्वाभाव|आर्धधातुकत्वाभाव", "absence of ārdhadhātuka status", "ārdhadhātukatva-abhāva"),
    (r"प्रगृह्यत्वाभाव",         "absence of pragṛhya status", "pragṛhyatva-abhāva"),
    (r"पुंवद्भावाभाव",           "absence of puṃvadbhāva", "puṃvadbhāva-abhāva"),
    (r"व्यवहितत्वम्|व्यवधानम्|व्यवहिताश्चेति", "preverb–verb separation", "vyavahita"),
    (r"णिजभाव",                 "absence of the causative ṇic", "ṇij-abhāva"),
    (r"टाबन्तत्व",              "feminine ṭāp ending", "ṭāb-antatva"),
    (r"नुमभाव",                 "absence of the num augment", "num-abhāva"),
    (r"नुडभाव",                 "absence of the nuṭ augment", "nuḍ-abhāva"),
    (r"मुमागम",                 "mum augment", "mum-āgama"),
    (r"इडभाव",                  "absence of the iṭ augment", "iḍ-abhāva"),
    (r"आर्ष\s*इट्|आर्षमिट्",     "iṭ augment", "iṭ"),
    # āḍ- vs aḍ-abhāva is UNDECIDABLE once sandhi has run: …इत्यत्र + अडभाव and
    # …ङिताम् + आडभाव both surface as …ाडभाव. So āḍ is claimed only on the unfused
    # word-initial form; the fused ones default to the far commoner aḍ below, and the
    # one real āḍ that arrives fused (MBh 1.32.24, decided by its ङिताम्) is a hand
    # ruling. Better one documented override than a rule that guesses.
    (r"(?<![ऀ-ॿ])आडभाव",        "absence of the āṭ augment", "āḍ-abhāva"),
    (r"[अआा]?डभाव|[अआा]?डाभाव|[अआा]?डाहम", "absence of the aṭ augment", "aḍ-abhāva"),
    (r"[अआा]?डागम",             "aṭ augment", "aḍ-āgama"),
    (r"तङ्भाव|तङभाव|आर्षस्तङ्|आर्षमात्मनेपद",
                                "voice — ātmanepada for parasmaipada", "taṅ-bhāva"),
    (r"लकारव्यत्यय",            "transfer — tense/mood (lakāra)", "lakāra-vyatyaya"),
    (r"लिङ्गव्यत्यय",            "transfer — gender", "liṅga-vyatyaya"),
    (r"वचनव्यत्यय",             "transfer — number", "vacana-vyatyaya"),
    (r"विभक्तिव्यत्यय",          "transfer — case", "vibhakti-vyatyaya"),
    (r"पदव्यत्यय",              "transfer — pada (voice/ending)", "pada-vyatyaya"),
    # …लोपाभाव must precede every plain …लोप pattern: "sulopābhāva" is the ABSENCE of
    # an elision, and matching the substring "sulopa" first inverts the finding.
    (r"लोपाभाव",                "absence of an expected elision", "lopa-abhāva"),
    (r"विभक्तिलोप|विभक्त्यलोप|विभक्तेर्लोप", "elision — case ending", "vibhakti-lopa"),
    (r"विभक्त्यलुक्|विभक्तिलुक्", "non-elision of the case ending", "vibhakti-aluk"),
    (r"तद्धितलुक्|तद्धितलोप",    "elision — taddhita suffix", "taddhita-luk"),
    (r"सुपां\s*सुलु|सुपो\s*लुक्|सुपो\s*डादेश|सुपश्छान्दसोऽडादेश|डादेश",
                                "case ending — luk / ḍa-substitution", "supāṃ suluk"),
    (r"तृतीयाया\s*आर्षोऽलुक्|आर्षोऽलुक्|आर्षो\s*लुक्", "case ending — (a)luk", "aluk / luk"),
    (r"अनुस्वारलोप",            "elision — anusvāra", "anusvāra-lopa"),
    (r"विसर्गलोप",              "elision — visarga", "visarga-lopa"),
    (r"वर्णलोप|अक्षरलोप|प्रथमाक्षरलोप", "elision — segment/syllable", "varṇa-lopa"),
    (r"तकारलोप|नकारलोप|सलोप|सुलोप|वलोप|इतोलोप|आकारलोप|मतुब्लोप|तृतीयालोप|द्वितीयालोप|स\s*लोप",
                                "elision — segment/affix", "lopa"),
    (r"अक्षराधिक्य",            "extra syllable", "akṣara-ādhikya"),
    (r"दैर्घ्य|दैर्ध्य|दीर्घश्च", "vowel lengthening", "dairghya"),
    (r"दैर्ध्याभाव|दैर्घ्याभाव",  "absence of expected lengthening", "dairghya-abhāva"),
    (r"गुणाभाव|एति\s*गुणाभाव",  "absence of guṇa", "guṇa-abhāva"),
    (r"उत्वाभाव|उत्वाद्यभाव",    "absence of the u-substitution", "utva-abhāva"),
    (r"रोरुत्वाभाव",            "absence of ru-substitution", "ru-tva-abhāva"),
    (r"रुत्वम्",                "ru-substitution", "rutva"),
    (r"क्लीबत्व",               "gender — neuter", "klībatva"),
    (r"पुंस्त्व",               "gender — masculine", "puṃstva"),
    (r"स्त्रीत्व",              "gender — feminine", "strītva"),
    (r"[अा]?कारान्तत्म्|[अा]?कारान्तत्व|[अा]?दन्तत्व", "stem-final vowel (a-stem)", "adantatva"),
    # NOT a bare त्वन्: it is a substring of सत्त्वन्तः "possessing sat", which stands
    # beside a different licence-claim at MBh 12.342.77 and stole its type.
    (r"कृत्यार्थे\s*तवैकेन्|छान्दसस्त्वन्|आर्षस्त्वन्", "kṛtya suffix (tvan)", "tvan"),
    (r"[अाो]?न्तादेश",          "final-segment substitution", "antādeśa"),
    (r"भत्वम्|’भत्वम्’",         "bha-stem treatment", "bhatva"),
    # …ासन्धि, not …असन्धि: "atra asandhiḥ" is written अत्रासन्धि, so the negating अ-
    # is invisible and the plain सन्धि pattern below would invert the finding.
    (r"[अा]सन्धि|[अा]संधि",     "absence of sandhi", "asandhi"),
    (r"सन्धिः|संधिः|सन्धिश्|संधिश्|सन्धिर्|संधिर्|सन्धिः|सन्धि",
                                "sandhi", "sandhi"),
    (r"पूर्वनिपात",             "compound — member order", "pūrva-nipāta"),
    (r"असमास",                  "absence of compounding", "asamāsa"),
    (r"समासान्त|अच्प्रत्यय|ष्टच्|टच्", "compound-final / ṭac suffix", "samāsānta"),
    (r"मत्वर्थीय|मट्प्रत्यय",     "matup-sense suffix", "matvarthīya"),
    (r"क्त्वो\s*यक्|क्त्वोल्यबादेश", "absolutive suffix", "ktvā / lyap"),
    (r"क्त्वाप्रत्यय",           "absolutive suffix", "ktvā"),
    (r"गर्हायां\s*लट्|लट्",      "tense — laṭ", "laṭ"),
    (r"अन्तादेश",               "final-segment substitution", "antādeśa"),
    (r"स्वार्थे\s*तद्धित|तद्धित", "taddhita suffix", "taddhita"),
    (r"क्यप्",                  "kyap suffix", "kyap"),
    (r"पूर्वसवर्ण",             "pūrvasavarṇa (case-ending fusion)", "pūrvasavarṇa"),
    (r"द्वित्वम्",               "gemination", "dvitva"),
    (r"शत्रन्त",                "śatṛ participle", "śatṛ"),
    (r"उपपदयोग",                "upapada government", "upapada-yoga"),
    # --- generic fallbacks: reached only when no specific operation matched ---
    (r"[अा]?दिलोप",             "elision — initial segment", "ādi-lopa"),
    (r"लोप|लुप्त|लुक्",          "elision", "lopa"),
    (r"व्यत्यय",                "transfer (vyatyaya)", "vyatyaya"),
    # A generic …भाव fallback is deliberately NOT here: "इति भावः" ("that is the sense")
    # is the commonest phrase in the whole ṭīkā and would auto-type the noise rows.
]
LEXICON = [(re.compile(p), en, sa) for p, en, sa in LEXICON]
WINDOW = 120          # chars either side searched for the grammatical noun
QUOTE = 170           # chars either side kept as the quote window


def clean(s):
    return re.sub(r"\s+", " ", s or "").strip()


def human_locus(rec):
    return f"MBh {rec['parva_no']}.{rec['adhyaya']}.{rec['shloka']}"


def nearest_operation(ctx, hit_start, hit_end):
    """The grammatical operation NEAREST the licence word, not the first rule that fires.

    A ±120-char window routinely holds two technical terms belonging to two different
    sentences. Taking the first lexicon entry that matched anywhere in it mis-typed
    MBh 5.141.47 (`upapada-yoga … ārṣo vā` typed from a `dīrghaś ca` forty characters
    downstream in the NEXT clause). Distance to the licence word settles it, with
    lexicon order — i.e. specificity — as the tie-break.
    """
    best = None
    for rank, (rx, en, sa) in enumerate(LEXICON):
        for m in rx.finditer(ctx):
            if m.end() <= hit_start:
                d = hit_start - m.end()
            elif m.start() >= hit_end:
                d = m.start() - hit_end
            else:
                d = 0
            if best is None or (d, rank) < best[0]:
                best = ((d, rank), en, sa)
    return (best[1], best[2]) if best else ("", "")


def sweep(src):
    """Every word-anchored licence hit, with its auto-derived deviation_type."""
    hits = []
    per_parva = {p: {"shlokas": 0, "tika": 0, "hits": 0, "tika_chars": 0} for p in PARVA_ORDER}
    for line in open(src, encoding="utf-8"):
        rec = json.loads(line)
        p = rec["parva"]
        if p not in per_parva:
            continue
        per_parva[p]["shlokas"] += 1
        tikas = rec.get("tika_dev") or []
        if tikas:
            per_parva[p]["tika"] += 1
        for ti, t in enumerate(tikas):
            t = ZW_RE.sub("", t)
            per_parva[p]["tika_chars"] += len(t)
            for m in HIT_RE.finditer(t):
                per_parva[p]["hits"] += 1
                tok = ""
                for tm in TOKEN_RE.finditer(t):
                    if tm.start() <= m.start() < tm.end():
                        tok = tm.group(0)
                        break
                lo, hi = max(0, m.start() - WINDOW), m.end() + WINDOW
                ctx = t[lo:hi]
                dev_en, dev_sa = nearest_operation(ctx, m.start() - lo, m.end() - lo)
                hits.append({
                    "hit_id": f"{rec['id']}#{ti}@{m.start()}",
                    "id": rec["id"], "parva": p, "parva_no": rec["parva_no"],
                    "locus": human_locus(rec),
                    "term_family": "ārṣa" if m.group("a") else "chāndasa",
                    "defense_term": tok or m.group(0),
                    "deviation_type": dev_en,
                    "deviation_term_sa": dev_sa,
                    "classification": "auto" if dev_en else "",
                    "quote": clean(t[max(0, m.start() - QUOTE):m.end() + QUOTE]),
                })
    return hits, per_parva


def write_census(per_parva, path):
    tot = {"shlokas": 0, "tika": 0, "hits": 0, "tika_chars": 0}
    rows = []
    for i, p in enumerate(PARVA_ORDER, 1):
        d = per_parva[p]
        for k in tot:
            tot[k] += d[k]
        rows.append([
            i, p, d["shlokas"], d["tika"],
            f"{100 * d['tika'] / d['shlokas']:.1f}" if d["shlokas"] else "0.0",
            d["tika_chars"], d["hits"],
            f"{1000 * d['hits'] / d['tika']:.2f}" if d["tika"] else "0.00",
            f"{100000 * d['hits'] / d['tika_chars']:.2f}" if d["tika_chars"] else "0.00",
        ])
    rows.append([
        "—", "TOTAL", tot["shlokas"], tot["tika"],
        f"{100 * tot['tika'] / tot['shlokas']:.1f}", tot["tika_chars"], tot["hits"],
        f"{1000 * tot['hits'] / tot['tika']:.2f}",
        f"{100000 * tot['hits'] / tot['tika_chars']:.2f}",
    ])
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(["n", "parva", "shlokas", "tika_shlokas", "tika_pct",
                    "tika_chars", "raw_hits", "hits_per_1000_tika_shlokas",
                    "hits_per_100k_tika_chars"])
        w.writerows(rows)
    return tot


def load_gita_rows():
    """The 27 probe rows from source A, with the multi-commentator agreement column."""
    rows = list(csv.DictReader(open(GITA_TSV, encoding="utf-8"), delimiter="\t"))
    by_locus = {}
    for r in rows:
        by_locus.setdefault(r["locus"], []).append(r["commentator"])
    out = []
    for i, r in enumerate(rows, 1):
        agree = by_locus[r["locus"]]
        out.append({
            "row_id": f"GITA-{i:03d}",
            "source": "GRETIL sa_bhagavadgItA-4comm (TEI, IAST)",
            "work": "Bhagavadgītā with four commentaries",
            "locus": r["locus"], "locus_id": r["locus"],
            "parva": "", "commentator": r["commentator"],
            "term_family": r["term_family"], "defense_term": r["defense_term"],
            "deviation_type": r["deviation_type"], "deviation_term_sa": "",
            "classification": "probe",
            "agreement_n": len(agree),
            "agreement_commentators": "; ".join(sorted(set(agree))),
            "quote": clean(r["quote_window"]),
        })
    return out


FIELDS = ["row_id", "source", "work", "locus", "locus_id", "parva", "commentator",
          "term_family", "defense_term", "deviation_type", "deviation_term_sa",
          "classification", "agreement_n", "agreement_commentators", "quote"]


def write_table(rows, stem, fields=FIELDS):
    with open(stem + ".tsv", "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter="\t",
                           lineterminator="\n", extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)
    # newline="\n" explicitly: on Windows the default translates to CRLF, git
    # normalises it back to LF, and the repo's "every generator reproduces its
    # artifact with no git diff" CI gate then fails on a phantom change.
    with open(stem + ".jsonl", "w", encoding="utf-8", newline="\n") as f:
        for r in rows:
            f.write(json.dumps({k: r.get(k, "") for k in fields}, ensure_ascii=False) + "\n")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--src", default=SRC)
    ap.add_argument("--emit-hand-queue", action="store_true",
                    help="dump the un-auto-classifiable hits for a fresh hand pass")
    args = ap.parse_args()

    if not os.path.exists(args.src):
        sys.exit(f"MISSING {args.src}\n"
                 "Restore it: python mahabharata-nilakantha/nilakantha_parser.py scrape")
    os.makedirs(OUTDIR, exist_ok=True)

    hits, per_parva = sweep(args.src)
    tot = write_census(per_parva, os.path.join(OUTDIR, "nilakantha_parvan_density.tsv"))
    print(f"raw word-anchored hits: {len(hits)} over {tot['tika']} ṭīkā-bearing shlokas")

    unresolved = [h for h in hits if not h["deviation_type"]]
    print(f"auto-classified: {len(hits) - len(unresolved)}  |  needs a hand ruling: {len(unresolved)}")

    if args.emit_hand_queue:
        qp = os.path.join(OUTDIR, "nilakantha_hand_queue.json")
        with open(qp, "w", encoding="utf-8") as f:
            json.dump(unresolved, f, ensure_ascii=False, indent=1)
        print("hand queue ->", qp)
        return

    rulings = json.load(open(RULINGS, encoding="utf-8")) if os.path.exists(RULINGS) else {}
    missing = [h["hit_id"] for h in unresolved if h["hit_id"] not in rulings]
    if missing:
        sys.exit(f"{len(missing)} hits have no hand ruling in {RULINGS}: {missing[:5]}")

    kept, rejected = [], []
    for h in hits:
        r = rulings.get(h["hit_id"])
        if r:
            if r["verdict"] != "licence_claim":
                h = dict(h, reject_reason=r["verdict"], reject_note=r.get("note", ""))
                rejected.append(h)
                continue
            h = dict(h, deviation_type=r["deviation_type"],
                     deviation_term_sa=r.get("deviation_term_sa", ""),
                     classification="hand")
        kept.append(h)

    nil_rows = []
    for i, h in enumerate(sorted(kept, key=lambda x: (x["parva_no"], x["id"])), 1):
        nil_rows.append({
            "row_id": f"NIL-{i:03d}",
            "source": "sanatana.in Nīlakaṇṭha vulgate scrape (Devanāgarī)",
            "work": WORK,
            "locus": h["locus"], "locus_id": h["id"], "parva": h["parva"],
            "commentator": COMMENTATOR,
            "term_family": h["term_family"], "defense_term": h["defense_term"],
            "deviation_type": h["deviation_type"],
            "deviation_term_sa": h["deviation_term_sa"],
            "classification": h["classification"],
            "agreement_n": 1, "agreement_commentators": COMMENTATOR,
            "quote": h["quote"],
        })
    write_table(nil_rows, os.path.join(OUTDIR, "commentary_licence_register_nilakantha"))

    with open(os.path.join(OUTDIR, "nilakantha_licence_rejected.tsv"),
              "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, delimiter="\t", lineterminator="\n", extrasaction="ignore",
                           fieldnames=["hit_id", "locus", "parva", "term_family",
                                       "defense_term", "reject_reason", "reject_note", "quote"])
        w.writeheader()
        w.writerows(sorted(rejected, key=lambda x: (x["parva_no"], x["id"])))

    gita = load_gita_rows()
    write_table(nil_rows + gita, os.path.join(OUTDIR, "commentary_licence_register_combined"))

    print(f"register rows: {len(nil_rows)} Nīlakaṇṭha + {len(gita)} Gītā "
          f"= {len(nil_rows) + len(gita)} combined")
    print(f"rejected (not a grammatical licence-claim): {len(rejected)}")
    print(f"precision on the word-anchored sweep: "
          f"{100 * len(nil_rows) / len(hits):.1f} % ({len(nil_rows)}/{len(hits)})")


if __name__ == "__main__":
    main()

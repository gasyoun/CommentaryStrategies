"""
crosstext_upanishads.py -- Upaniṣad cross-text pass for Sundarakāṇḍa.

EXPECTED VERY LOW YIELD: epic adventure narrative shares little register
with gnomic Upaniṣadic prose/verse. Only confirm a note for a genuine
locus classicus of a philosophical term Sundara actually uses.

Works: br-up, ch-up, kat-up, isha-up, mun-up, shv-up, kena-up, tai-up, pr-up, man-up.

Qualifying terms: ātman, brahman, māyā, tapas, satya, ṛta, prāṇa (as cosmic force),
akṣara, karma. These MUST appear in a philosophically relevant Sundara context
(not just any casual mention of prāṇa = breath or satya = truth).
"""
import sys, json, re
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

CS_DIR     = Path(r"C:\Users\user\Documents\GitHub\CommentaryStrategies")
OUT_DIR    = CS_DIR / "data" / "crosstext"
CORPUS_DIR = Path(r"C:\Users\user\Documents\GitHub\SamudraManthanam\web\corpus_builder\jsonl")
SUNDARA    = CORPUS_DIR / "05_ramayana-sundarakanda.jsonl"

UPANISHAD_WORKS = {
    "Bṛhad.Up":   "br-up.jsonl",
    "Chānd.Up":   "ch-up.jsonl",
    "Kaṭha Up":   "kat-up.jsonl",
    "Īśā Up":     "isha-up.jsonl",
    "Muṇḍaka Up": "mun-up.jsonl",
    "Śvetāśv.Up": "shv-up.jsonl",
    "Kena Up":    "kena-up.jsonl",
    "Taitt.Up":   "tai-up.jsonl",
    "Praśna Up":  "pr-up.jsonl",
    "Māṇḍūkya":  "man-up.jsonl",
}

def load_pairs(path):
    out = {}
    with open(path, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            o = json.loads(line)
            if o.get("deleted"):
                continue
            if o.get("seg") not in ("sa", "ru"):
                continue
            p = o["passage"]
            rec = out.setdefault(p, {"chapter": o.get("chapter")})
            seg = o["seg"]
            if seg == "sa":
                slp1 = o.get("slp1", "")
                if "{no sanskrit" in slp1 or not slp1:
                    continue
                rec["sa"] = o.get("text", "")
                rec["slp1"] = slp1
            elif seg == "ru":
                rec["ru"] = o.get("text", "")
    return {p: r for p, r in out.items() if r.get("slp1")}

_TOK = re.compile(r'[A-Za-z]+')

def strip_punct(s):
    return s.replace("।", " ").replace("॥", " ")

def tokens(slp1):
    return [t for t in _TOK.findall(strip_punct(slp1)) if len(t) >= 3]

# Tight Upaniṣadic lexicon: only terms where Sundara genuinely uses the
# philosophical sense (not just incidental verbal coincidence).
UPANISHAD_STEMS = {
    # ātman -- self, soul (not "himself" as reflexive)
    "AtmA":     ("ātman",    "Атман (ātman) -- индивидуальная душа",               "atman"),
    "paramAtm": ("paramātman","Высший Атман (paramātman)",                           "atman"),
    # brahman -- absolute (not brāhmaṇa the caste)
    "brahman":  ("brahman",  "Брахман (brahman) -- абсолют, не жрец",              "brahman"),
    "brahmAnand":("brahmānanda","блаженство Брахмана (brahmānanda)",                "brahman"),
    # māyā -- cosmic illusion (rarely in epic, but Sundara has illusion/magic context)
    "mAyA":     ("māyā",     "майя (māyā) -- иллюзия, волшебство",                 "maya"),
    # tapas -- austerity as cosmic power (shared with Veda & epic, but UP defines it)
    "tapas":    ("tapas",    "тапас (tapas) -- аскетический жар как космическая сила","tapas"),
    # satya / ṛta -- cosmic truth (Sundara: Rāma as satyavāc, satyavrata)
    "satya":    ("satya",    "истина (satya) -- абсолютная, как в Упанишадах",       "satya"),
    "satyakAm": ("satyakāma","любящий истину (satyakāma) -- Упанишадский термин",   "satya"),
    # prāṇa as cosmic life-force (not mere breath)
    "prARa":    ("prāṇa",    "прана (prāṇa) -- жизненная сила, космос",             "prana"),
    "apAna":    ("apāna",    "апана (apāna) -- выдох, нижний вздох",               "prana"),
    # karma -- action and retribution
    "karma":    ("karma",    "карма (karma) -- действие и воздаяние",               "karma"),
    "karmaphala":("karmaphala","плод кармы (karmaphala)",                           "karma"),
    # akṣara -- imperishable (Upaniṣadic term for the Absolute)
    "akzar":    ("akṣara",   "Нетленное (akṣara) -- термин Упанишад для Абсолюта", "aksara"),
    # mokṣa / mukti -- liberation
    "mokz":     ("mokṣa",    "мокша (mokṣa) -- освобождение",                      "moksha"),
    "mukti":    ("mukti",    "мукти (mukti) -- освобождение",                      "moksha"),
}

def find_stem(toks):
    hits = set()
    for t in toks:
        for key in UPANISHAD_STEMS:
            if key in t:
                hits.add(key)
    return hits

def main():
    sund = load_pairs(SUNDARA)
    print(f"Sundara verses: {len(sund)}", file=sys.stderr)

    sund_idx = {}
    for p, rec in sund.items():
        toks = tokens(rec.get("slp1", ""))
        rec["_toks"] = toks
        for s in find_stem(toks):
            sund_idx.setdefault(s, []).append((p, rec))

    up_data = {}
    for wn, fn in UPANISHAD_WORKS.items():
        path = CORPUS_DIR / fn
        if path.exists():
            data = load_pairs(path)
            up_data[wn] = data
            print(f"  {wn}: {len(data)} verses", file=sys.stderr)
        else:
            print(f"  MISSING: {fn}", file=sys.stderr)

    src_idx = {}
    for wn, data in up_data.items():
        for p, rec in data.items():
            toks = tokens(rec.get("slp1", ""))
            rec["_toks"] = toks
            for s in find_stem(toks):
                src_idx.setdefault(s, []).append((wn, p, rec))

    shared = sorted(set(sund_idx) & set(src_idx))
    print(f"\nShared Upanishad stems: {len(shared)}", file=sys.stderr)
    for s in shared:
        print(f"  {s:14s}  {UPANISHAD_STEMS[s][0]:22s}  sund={len(sund_idx[s]):3d}  src={len(src_idx[s]):4d}", file=sys.stderr)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    dump = {}
    for s in shared:
        dump[s] = {
            "lemma": UPANISHAD_STEMS[s][0],
            "gloss": UPANISHAD_STEMS[s][1],
            "cat":   UPANISHAD_STEMS[s][2],
            "sund_n": len(sund_idx[s]),
            "src_n":  len(src_idx[s]),
            "sundara": [
                {"passage": p, "chapter": rec.get("chapter"),
                 "sa": rec.get("sa",""), "ru": rec.get("ru","")}
                for p, rec in sund_idx[s][:25]
            ],
            "source": [
                {"work": wn, "passage": p,
                 "sa": rec.get("sa",""), "ru": rec.get("ru","")}
                for wn, p, rec in src_idx[s][:25]
            ],
        }
    raw_path = OUT_DIR / "_upanishads_raw_index.json"
    raw_path.write_text(json.dumps(dump, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"\nWrote {raw_path}", file=sys.stderr)

if __name__ == "__main__":
    main()

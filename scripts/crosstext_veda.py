"""
crosstext_veda.py -- Vedic cross-text pass for Sundarakāṇḍa.

Selectively targets Rigveda + Atharvaveda. Does NOT brute-force all 29 files.
Instead, targets 5 RV books + 4 AV books with the richest Sundara-relevant hymns:
- Vāyu/Marut complex (Hanumān = mārutātmaja = son of Vāyu)
- Indra as cosmic champion
- Varuṇa as lord of the ocean
- Ocean-crossing (sāgara, sindhu)
- Agni (pāvaka, hutāśana) -- the Agni-test motif
- Tapas (cosmological power underlying the leap)
- Sundara-specific: Hanumān as wind-son, Lanka as demon fortress

Method: curated Vedic stem lexicon. Only a genuine ANCHOR (Vedic locus for a
Sundara epithet or divine name) passes. Coincidental stem collision rejected.
"""
import sys, json, re
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

CS_DIR     = Path(r"C:\Users\user\Documents\GitHub\CommentaryStrategies")
OUT_DIR    = CS_DIR / "data" / "crosstext"
CORPUS_DIR = Path(r"C:\Users\user\Documents\GitHub\SamudraManthanam\web\corpus_builder\jsonl")
SUNDARA    = CORPUS_DIR / "05_ramayana-sundarakanda.jsonl"

# Selective: only the most productive books (Vāyu/Marut-rich RV books + AV high hymns)
VEDA_FILES = {
    "RV.1":  "01_rigveda.jsonl",
    "RV.2":  "02_rigveda.jsonl",
    "RV.5":  "05_rigveda.jsonl",  # Marut hymns: 5.54-61
    "RV.7":  "07_rigveda.jsonl",  # Varuṇa hymns: 7.86-89
    "RV.8":  "08_rigveda.jsonl",  # Indra: 8.1-15
    "RV.10": "10_rigveda.jsonl",  # cosmogony (Puruṣa, Nāsadīya)
    "AV.1":  "01_atharvaveda.jsonl",
    "AV.4":  "04_atharvaveda.jsonl",
    "AV.11": "11_atharvaveda.jsonl",  # tapas hymn 11.5
    "AV.19": "19_atharvaveda.jsonl",
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

# Vedic stem lexicon: only high-signal terms that are genuine Vedic anchors for Sundara.
VEDIC_STEMS = {
    # Vāyu / Marut complex -- the theological anchor of Hanumān = mārutātmaja
    "mArut":    ("māruta/marut",  "Маруты / Ваю -- боги ветра (предки Ханумана)", "vayu"),
    "mArutAtm": ("mārutātmaja",   "сын Маруты (mārutātmaja) = Хануман",           "vayu"),
    "vAyu":     ("vāyu",          "Ваю -- бог ветра, отец Ханумана (vāyu)",        "vayu"),
    "pavamAn":  ("pavamāna",      "Очищающий / эпитет Сомы и Ваю (pavamāna)",     "vayu"),
    "pavanAtm": ("pavanātmaja",   "сын Ветра = Хануман (pavanātmaja)",             "vayu"),
    # Indra -- king of gods, cosmic champion
    "indra":    ("indra",         "Индра (indra) -- царь богов",                   "indra"),
    "SAkr":     ("śakra",         "Шакра (śakra) -- могучий, эпитет Индры",       "indra"),
    "vajrapARi":("vajrapāṇi",     "ваджроносный (vajrapāṇi) -- Индра",            "indra"),
    "SAcIpat":  ("śacīpati",      "супруг Шачи -- Индра (śacīpati)",              "indra"),
    "maghav":   ("maghavan",      "щедрый -- эпитет Индры (maghavan)",            "indra"),
    # Varuṇa -- lord of the ocean (Sundara: crossing the ocean ruled by Varuṇa)
    "varuR":    ("varuṇa",        "Варуна (varuṇa) -- владыка океана",            "varuna"),
    "varuRAlaya":("varuṇālaya",   "обитель Варуны = океан (varuṇālaya)",          "varuna"),
    # Ocean / crossing terms
    "sAgar":    ("sāgara",        "океан (sāgara)",                                "ocean"),
    "samudra":  ("samudra",       "море (samudra)",                                "ocean"),
    "sindhu":   ("sindhu",        "Синдху / поток (sindhu)",                      "ocean"),
    "mahodaDi": ("mahodadhi",     "великий океан (mahodadhi)",                    "ocean"),
    # Agni -- fire-god; Sītā's fire-ordeal (Agni-test)
    "agni":     ("agni",          "Агни (agni) -- бог огня",                     "agni"),
    "pAvak":    ("pāvaka",        "Очиститель (pāvaka) -- эпитет Агни",          "agni"),
    "hutASan":  ("hutāśana",      "Пожиратель жертв (hutāśana) -- Агни",         "agni"),
    "jAtaved":  ("jātaveda",      "Знаток рождённых (jātaveda) -- Агни",         "agni"),
    # Tapas -- cosmic power; Sītā's tapas, the leap as tapas
    "tapas":    ("tapas",         "аскетический жар (tapas)",                     "tapas"),
    "tapasv":   ("tapasvin",      "подвижник (tapasvin)",                         "tapas"),
    # Cosmological: sun, divine order
    "sUrya":    ("sūrya",         "Сурья -- бог солнца (sūrya)",                 "cosmic"),
    "savitf":   ("savitṛ",        "Савитар -- животворящий (savitṛ)",            "cosmic"),
    "vizvede":  ("viśvadeva",     "Всебоги (viśvedeva)",                         "cosmic"),
    "Rtav":     ("ṛtāvan",        "причастный к Порядку-Rta (ṛtāvan)",           "cosmic"),
    "satyav":   ("satyavant",     "обладающий истиной (satyavant)",              "cosmic"),
}

def find_stem(toks):
    hits = set()
    for t in toks:
        for key in VEDIC_STEMS:
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

    veda_data = {}
    for bk, fn in VEDA_FILES.items():
        path = CORPUS_DIR / fn
        if path.exists():
            data = load_pairs(path)
            veda_data[bk] = data
            print(f"  {bk}: {len(data)} verses", file=sys.stderr)
        else:
            print(f"  MISSING: {fn}", file=sys.stderr)

    src_idx = {}
    for bk, data in veda_data.items():
        for p, rec in data.items():
            toks = tokens(rec.get("slp1", ""))
            rec["_toks"] = toks
            for s in find_stem(toks):
                src_idx.setdefault(s, []).append((bk, p, rec))

    shared = sorted(set(sund_idx) & set(src_idx))
    print(f"\nShared Vedic stems: {len(shared)}", file=sys.stderr)
    for s in shared:
        print(f"  {s:14s}  {VEDIC_STEMS[s][0]:22s}  sund={len(sund_idx[s]):3d}  src={len(src_idx[s]):4d}", file=sys.stderr)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    dump = {}
    for s in shared:
        dump[s] = {
            "lemma": VEDIC_STEMS[s][0],
            "gloss": VEDIC_STEMS[s][1],
            "cat":   VEDIC_STEMS[s][2],
            "sund_n": len(sund_idx[s]),
            "src_n":  len(src_idx[s]),
            "sundara": [
                {"passage": p, "chapter": rec.get("chapter"),
                 "sa": rec.get("sa",""), "ru": rec.get("ru","")}
                for p, rec in sund_idx[s][:30]
            ],
            "source": [
                {"book": bk, "passage": p,
                 "sa": rec.get("sa",""), "ru": rec.get("ru","")}
                for bk, p, rec in src_idx[s][:30]
            ],
        }
    raw_path = OUT_DIR / "_veda_raw_index.json"
    raw_path.write_text(json.dumps(dump, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"\nWrote {raw_path}", file=sys.stderr)

if __name__ == "__main__":
    main()

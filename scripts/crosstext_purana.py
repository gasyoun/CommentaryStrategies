"""
crosstext_purana.py -- Purāṇa cross-text pass for Sundarakāṇḍa.

Primary: vishnu-purana (Rāma avatāra, cosmology, divine genealogies).
Optional: devi-gita (Goddess aspect relevant to Sītā's divine status).

Focus: Rāma as Viṣṇu's avatāra (theological anchor), divine genealogies of
Hanumān, Rāvaṇa's Purāṇic backstory, cosmological terms in Sundara.

Method: curated-lexicon substring (same as dharmashastra.py).
"""
import sys, json, re
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

CS_DIR     = Path(r"C:\Users\user\Documents\GitHub\CommentaryStrategies")
OUT_DIR    = CS_DIR / "data" / "crosstext"
CORPUS_DIR = Path(r"C:\Users\user\Documents\GitHub\SamudraManthanam\web\corpus_builder\jsonl")
SUNDARA    = CORPUS_DIR / "05_ramayana-sundarakanda.jsonl"

PURANA_WORKS = {
    "Viṣṇupurāṇa": "vishnu-purana.jsonl",
    "Devīgītā":    "devi-gita.jsonl",
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

PURANA_STEMS = {
    # Rāma as Viṣṇu avatāra -- the Purāṇic theological anchor
    "viZRu":    ("viṣṇu",        "Вишну (viṣṇu) -- как Рама есть авататара Вишну",  "avatara"),
    "nArAyaR":  ("nārāyaṇa",     "Нараяна (nārāyaṇa) -- космический Вишну",          "avatara"),
    "avatAr":   ("avatāra",      "аватара (avatāra) -- нисхождение бога",             "avatara"),
    "jagannAT": ("jagannātha",   "Владыка мира (jagannātha)",                         "avatara"),
    "puruZott": ("puruṣottama",  "Высший Пуруша (puruṣottama) -- эпитет Рамы/Вишну", "avatara"),
    # Rāvaṇa's Purāṇic backstory
    "rAvaR":    ("rāvaṇa",       "Равана (rāvaṇa) -- его история в Вишну-пуране",    "ravana"),
    "kubera":   ("kubera",       "Кубера -- владыка богатств, брат Рагваны",          "ravana"),
    "pulasty":  ("pulastya",     "Пуластья -- дед Раваны (pulastya)",                "ravana"),
    "trikUw":   ("trikūṭa",      "Трикута -- гора Ланки (trikūṭa)",                  "ravana"),
    # Hanumān's divine genealogy
    "mArut":    ("māruta",       "Марут/Ваю -- отец Ханумана",                       "hanuman"),
    "vAyu":     ("vāyu",         "Ваю (vāyu) -- бог ветра",                          "hanuman"),
    "anjana":   ("añjanā",       "Анджана -- мать Ханумана (añjanā)",                "hanuman"),
    "kesarin":  ("kesarin",      "Кесарин -- отчим Ханумана (kesarin)",              "hanuman"),
    # Cosmological / divine order
    "brahmA":   ("brahmā",       "Брахма (brahmā) -- бог-творец",                    "cosmic"),
    "prajAp":   ("prajāpati",    "Праджапати -- Владыка существ (prajāpati)",        "cosmic"),
    "dakza":    ("dakṣa",        "Дакша (dakṣa) -- праотец богов",                  "cosmic"),
    "devAsurasaMgram":("devāsurasaṃgrāma","война богов и демонов",                  "cosmic"),
    "yuga":     ("yuga",         "юга (yuga) -- мировой период",                    "cosmic"),
    "manvant":  ("manvantara",   "манвантара (manvantara)",                          "cosmic"),
    "kalp":     ("kalpa",        "кальпа (kalpa)",                                   "cosmic"),
    "pralaya":  ("pralaya",      "пралая -- растворение мира (pralaya)",            "cosmic"),
    # Sacred geography
    "meru":     ("meru",         "Меру (meru) -- мировая гора",                     "sacred"),
    "mandar":   ("mandara",      "Мандара (mandara) -- гора пахтания",              "sacred"),
    "mahendra": ("mahendra",     "Махендра (mahendra) -- священная гора",           "sacred"),
    "mainAk":   ("maināka",      "Майнака -- гора в океане (maināka)",              "sacred"),
    # Divine weapons / power
    "sudarSan": ("sudarśana",    "Сударшана (sudarśana) -- диск Вишну",            "divine"),
    "GAMgA":    ("gaṅgā",        "Ганга (gaṅgā) -- священная река",               "divine"),
    "lakzmI":   ("lakṣmī",       "Лакшми (lakṣmī) -- супруга Вишну",             "divine"),
    "SrI":      ("śrī",          "Шри (śrī) -- Лакшми, богиня процветания",       "divine"),
}

def find_stem(toks):
    hits = set()
    for t in toks:
        for key in PURANA_STEMS:
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

    purana_data = {}
    for wn, fn in PURANA_WORKS.items():
        path = CORPUS_DIR / fn
        if path.exists():
            data = load_pairs(path)
            purana_data[wn] = data
            print(f"  {wn}: {len(data)} verses", file=sys.stderr)
        else:
            print(f"  MISSING: {fn}", file=sys.stderr)

    src_idx = {}
    for wn, data in purana_data.items():
        for p, rec in data.items():
            toks = tokens(rec.get("slp1", ""))
            rec["_toks"] = toks
            for s in find_stem(toks):
                src_idx.setdefault(s, []).append((wn, p, rec))

    shared = sorted(set(sund_idx) & set(src_idx))
    print(f"\nShared Purana stems: {len(shared)}", file=sys.stderr)
    for s in shared:
        print(f"  {s:14s}  {PURANA_STEMS[s][0]:22s}  sund={len(sund_idx[s]):3d}  src={len(src_idx[s]):4d}", file=sys.stderr)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    dump = {}
    for s in shared:
        dump[s] = {
            "lemma": PURANA_STEMS[s][0],
            "gloss": PURANA_STEMS[s][1],
            "cat":   PURANA_STEMS[s][2],
            "sund_n": len(sund_idx[s]),
            "src_n":  len(src_idx[s]),
            "sundara": [
                {"passage": p, "chapter": rec.get("chapter"),
                 "sa": rec.get("sa",""), "ru": rec.get("ru","")}
                for p, rec in sund_idx[s][:30]
            ],
            "source": [
                {"work": wn, "passage": p,
                 "sa": rec.get("sa",""), "ru": rec.get("ru","")}
                for wn, p, rec in src_idx[s][:30]
            ],
        }
    raw_path = OUT_DIR / "_purana_raw_index.json"
    raw_path.write_text(json.dumps(dump, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"\nWrote {raw_path}", file=sys.stderr)

if __name__ == "__main__":
    main()

"""
crosstext_kavya.py -- deep kāvya cross-text pass for Sundarakāṇḍa.

Works: raghuvamsha (deep pass), kumarasambhava, megha-duta, gitagovinda,
amaru-shataka, shatakatrayam, chaurapanchashika, shukasaptati.

Method: curated-lexicon substring approach (same as dharmashastra.py).
Dumps _kavya_deep_index.json then the curation step writes kavya.json.
"""
import sys, json, re
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

CS_DIR     = Path(r"C:\Users\user\Documents\GitHub\CommentaryStrategies")
OUT_DIR    = CS_DIR / "data" / "crosstext"
CORPUS_DIR = Path(r"C:\Users\user\Documents\GitHub\SamudraManthanam\web\corpus_builder\jsonl")
SUNDARA    = CORPUS_DIR / "05_ramayana-sundarakanda.jsonl"

KAVYA_WORKS = {
    "Raghuvaṃśa":     "raghuvamsha.jsonl",
    "Kumārasambhava": "kumarasambhava.jsonl",
    "Meghadūta":      "megha-duta.jsonl",
    "Gītagovinda":    "gitagovinda.jsonl",
    "Amaruśataka":    "amaru-shataka.jsonl",
    "Śatakatrayam":   "shatakatrayam.jsonl",
    "Caurapañcāśikā": "chaurapanchashika.jsonl",
    "Śukasaptati":    "shukasaptati.jsonl",
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

KAVYA_STEMS = {
    "rAGav":    ("rāghava",     "потомок Рагху = Рама (rāghava)",   "dynasty"),
    "dASaraT":  ("dāśarathi",   "сын Дашаратхи = Рама",             "dynasty"),
    "raghu":    ("raghu",       "Рагху -- предок Рамы",              "dynasty"),
    "ikzvAk":   ("ikṣvāku",    "Икшваку -- прародитель рода Рамы",  "dynasty"),
    "kakutsTa": ("kakutstha",   "Какутстха -- предок Рамы",          "dynasty"),
    "kosala":   ("kosala",      "Кошала -- царство Рамы",            "dynasty"),
    "mArut":    ("māruta",      "Марут/Ваю (ветер; отец Ханумана)", "hanuman"),
    "mArutAtm": ("mārutātmaja", "сын Ваю = Хануман",               "hanuman"),
    "vAyuput":  ("vāyuputra",   "сын Ваю = Хануман",               "hanuman"),
    "kapi":     ("kapi",        "обезьяна (kapi)",                  "hanuman"),
    "vaideh":   ("vaidehī",     "Видехийка = Сита",                 "sita"),
    "maITil":   ("maithilī",    "Митхилийка = Сита",                "sita"),
    "janak":    ("janaka",      "Джанака (отец Ситы)",              "sita"),
    "virah":    ("viraha",      "разлука (viraha)",                  "viraha"),
    "sAgar":    ("sāgara",      "океан (sāgara)",                   "ocean"),
    "samudra":  ("samudra",     "море (samudra)",                   "ocean"),
    "laNkA":    ("laṅkā",       "Ланка",                            "lanka"),
    "rAvaR":    ("rāvaṇa",      "Равана",                           "lanka"),
    "tapas":    ("tapas",       "аскеза (tapas)",                   "tapas"),
    "tapasv":   ("tapasvin",    "подвижник/ница (tapasvin/i)",      "tapas"),
    "padma":    ("padma",       "лотос (padma)",                    "simile"),
    "kamala":   ("kamala",      "лотос (kamala)",                   "simile"),
    "candra":   ("candra",      "луна (candra)",                    "simile"),
    "mfRAl":    ("mṛṇāla",      "стебель лотоса (mṛṇāla)",         "simile"),
    "aSok":     ("aśoka",       "ашока (дерево заточения Ситы)",    "simile"),
    "rudant":   ("rudantī",     "плачущая (rudantī)",               "lament"),
    "vilap":    ("vilāpa",      "причитание (vilāpa)",              "lament"),
    "kfS":      ("kṛśa",        "исхудавшая -- о Сите (kṛśa)",      "lament"),
    "dIna":     ("dīna",        "несчастная, удручённая (dīna)",    "lament"),
    "siMha":    ("siṃha",       "лев (siṃha -- воинское сравнение)","hero"),
    "garuq":    ("garuḍa",      "Гаруда (garuḍa)",                 "hero"),
    "vajra":    ("vajra",       "ваджра (vajra)",                   "hero"),
    "mahAbAh":  ("mahābāhu",    "длиннорукий (mahābāhu)",           "hero"),
    "parAkram": ("parākrama",   "доблесть (parākrama)",             "hero"),
    "pAvak":    ("pāvaka",      "Агни/огонь (pāvaka)",             "divine"),
    "mahend":   ("mahendra",    "Махендра (Индра)",                 "divine"),
    "varuR":    ("varuṇa",      "Варуна (бог океана)",             "divine"),
}

def find_stem(toks):
    hits = set()
    for t in toks:
        for key in KAVYA_STEMS:
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

    kavya_data = {}
    for wn, fn in KAVYA_WORKS.items():
        path = CORPUS_DIR / fn
        if path.exists():
            data = load_pairs(path)
            kavya_data[wn] = data
            print(f"  {wn}: {len(data)} verses", file=sys.stderr)
        else:
            print(f"  MISSING: {fn}", file=sys.stderr)

    src_idx = {}
    for wn, data in kavya_data.items():
        for p, rec in data.items():
            toks = tokens(rec.get("slp1", ""))
            rec["_toks"] = toks
            for s in find_stem(toks):
                src_idx.setdefault(s, []).append((wn, p, rec))

    shared = sorted(set(sund_idx) & set(src_idx))
    print(f"\nShared kavya stems: {len(shared)}", file=sys.stderr)
    for s in shared:
        print(f"  {s:14s}  {KAVYA_STEMS[s][0]:20s}  sund={len(sund_idx[s]):3d}  src={len(src_idx[s]):4d}", file=sys.stderr)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    dump = {}
    for s in shared:
        dump[s] = {
            "lemma": KAVYA_STEMS[s][0],
            "gloss": KAVYA_STEMS[s][1],
            "cat":   KAVYA_STEMS[s][2],
            "sund_n": len(sund_idx[s]),
            "src_n":  len(src_idx[s]),
            "sundara": [
                {"passage": p, "chapter": rec.get("chapter"),
                 "sa": rec.get("sa",""), "ru": rec.get("ru","")}
                for p, rec in sund_idx[s][:40]
            ],
            "source": [
                {"work": wn, "passage": p,
                 "sa": rec.get("sa",""), "ru": rec.get("ru","")}
                for wn, p, rec in src_idx[s][:40]
            ],
        }
    raw_path = OUT_DIR / "_kavya_deep_index.json"
    raw_path.write_text(json.dumps(dump, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"\nWrote {raw_path}", file=sys.stderr)

if __name__ == "__main__":
    main()

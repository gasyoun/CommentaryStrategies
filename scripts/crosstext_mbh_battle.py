"""
crosstext_mbh_battle.py

Mine the five MBh battle parvans (Bhishma/Drona/Karna/Shalya/Sauptika) for
cross-text commentary parallels to the WHOLE Sundarakanda, with editorial
focus on MILITARY REALIA: weapons, army formations, warrior epithets,
heroic-combat formulae (relevant to Sundara battle chapters 42-55).

Output: data/crosstext/mbh_battle.json  (list of candidate notes, review_required)

Method:
  1. Build SLP1 content-stem index of the 5 source parvans and of every
     Sundara verse. Intersect on RARE shared stems (drop function words and
     ultra-common epic vocabulary).
  2. For a curated set of military-realia stems, find the BEST source verse
     (one where the stem is salient + the verse is a clean exemplar) and the
     Sundara verse(s) carrying it. Emit a note quoting both #sa and #ru.
"""
import sys, json, re, collections
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

CS_DIR     = Path(r"C:\Users\user\Documents\GitHub\CommentaryStrategies")
OUT_DIR    = CS_DIR / "data" / "crosstext"
CORPUS_DIR = Path(r"C:\Users\user\Documents\GitHub\SamudraManthanam\web\corpus_builder\jsonl")
SUNDARA    = CORPUS_DIR / "05_ramayana-sundarakanda.jsonl"
PARVANS = {
    "Bhīṣmaparva":   "06_mahabharata-bhishmaparva.jsonl",
    "Droṇaparva":    "07_mahabharata-dronaparva.jsonl",
    "Karṇaparva":    "08_mahabharata-karnaparva.jsonl",
    "Śalyaparva":    "09_mahabharata-shalyaparva.jsonl",
    "Sauptikaparva": "10_mahabharata-sauptikaparva.jsonl",
}

def load_pairs(path):
    """Return dict passage -> {'sa':..., 'ru':..., 'slp1':..., 'chapter':...}"""
    out = {}
    with open(path, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            o = json.loads(line)
            if o.get("deleted"):
                continue
            p = o["passage"]
            rec = out.setdefault(p, {"chapter": o.get("chapter")})
            seg = o["seg"]
            if seg == "sa":
                rec["sa"] = o.get("text", "")
                rec["slp1"] = o.get("slp1", "")
            elif seg == "ru":
                rec["ru"] = o.get("text", "")
    return out

_TOK = re.compile(r'[A-Za-z]+')

def strip_punct(slp1):
    return slp1.replace("।", " ").replace("॥", " ")

def tokens(slp1):
    return [t for t in _TOK.findall(strip_punct(slp1).lower()) if len(t) >= 3]

# ---- militaria stem lexicon: SLP1 substring -> (IAST lemma, gloss-ru, gloss-cat) ----
# We match by SUBSTRING on lowercased slp1 tokens so inflected/compounded forms
# are caught (e.g. 'gadayA', 'gadAm', 'gadApARiH' all hit 'gad').
MILITARIA = {
    # weapons
    "gad":    ("gadā", "палица", "weapon"),
    "parig":  ("parigha", "палица-таран (parigha)", "weapon"),
    "tomar":  ("tomara", "дротик (tomara)", "weapon"),
    "prAs":   ("prāsa", "копьё (prāsa)", "weapon"),
    "Sakti":  ("śakti", "копьё-щакти", "weapon"),
    "Sara":   ("śara", "стрела", "weapon"),
    "Balla":  ("bhalla", "стрела-бхалла", "weapon"),
    "nArAc":  ("nārāca", "цельножелезная стрела (nārāca)", "weapon"),
    "cakra":  ("cakra", "диск-чакра", "weapon"),
    "Kaqg":   ("khaḍga", "меч", "weapon"),
    "asipa":  ("asi", "меч (asi)", "weapon"),
    "muSal":  ("musala", "палица-мушала", "weapon"),
    "paraSv": ("paraśvadha", "боевой топор", "weapon"),
    "Cakra":  ("cakra", "диск", "weapon"),
    "DanuZ":  ("dhanus", "лук", "weapon"),
    "Danur":  ("dhanus", "лук", "weapon"),
    "kArmuk": ("kārmuka", "лук (kārmuka)", "weapon"),
    "cAp":    ("cāpa", "лук (cāpa)", "weapon"),
    "kuMt":   ("kunta", "пика (kunta)", "weapon"),
    # armour / equipment
    "kavac":  ("kavaca", "панцирь", "armour"),
    "varman": ("varman", "доспех (varman)", "armour"),
    "carman": ("carman", "щит (carman)", "armour"),
    "puNK":   ("puṅkha", "оперение стрелы", "armour"),
    "tUR":    ("tūṇa", "колчан (tūṇa)", "armour"),
    "raTa":   ("ratha", "колесница", "formation"),
    # formations / host
    "vyUh":   ("vyūha", "боевой строй (vyūha)", "formation"),
    "senA":   ("senā", "войско (senā)", "formation"),
    "anIk":   ("anīka", "войсковой строй (anīka)", "formation"),
    "vAhin":  ("vāhinī", "войско (vāhinī)", "formation"),
    "DvajA":  ("dhvaja", "знамя", "formation"),
    "Dvaja":  ("dhvaja", "знамя (dhvaja)", "formation"),
    "patAk":  ("patākā", "стяг (patākā)", "formation"),
    "samar":  ("samara", "битва (samara)", "combat"),
    "raRa":   ("raṇa", "битва (raṇa)", "combat"),
    "saMgrAm":("saṃgrāma", "сражение (saṃgrāma)", "combat"),
    "AhavA":  ("āhava", "битва (āhava)", "combat"),
    "yudDa":  ("yuddha", "бой (yuddha)", "combat"),
    # warrior epithets / formulae
    "vIra":   ("vīra", "герой (vīra)", "epithet"),
    "SUra":   ("śūra", "храбрец (śūra)", "epithet"),
    "mahAraT":("mahāratha", "великий колесничный воин (mahāratha)", "epithet"),
    "raTina": ("rathin", "колесничный боец (rathin)", "epithet"),
    "durAdar":("durādharṣa", "неодолимый (durādharṣa)", "epithet"),
    "durjay": ("durjaya", "непобедимый (durjaya)", "epithet"),
    "Satrun": ("śatrunāśana", "губитель врагов", "epithet"),
    "ripuG":  ("ripughna", "сокрушитель недругов", "epithet"),
    "parAkram":("parākrama", "доблесть (parākrama)", "epithet"),
    "vikram": ("vikrama", "натиск, доблесть (vikrama)", "epithet"),
    "ojas":   ("ojas", "мощь (ojas)", "epithet"),
    "tejas":  ("tejas", "пыл, мощь (tejas)", "epithet"),
    "siMha":  ("siṃha", "лев (как воинское сравнение)", "simile"),
    "garj":   ("garj", "рык (рёв воина/льва)", "simile"),
    "nadant": ("nad", "рык в бою", "simile"),
    "krudD":  ("kruddha", "разъярённый (kruddha)", "combat"),
    "amarZa": ("amarṣa", "боевая ярость (amarṣa)", "combat"),
    "vegena": ("vega", "стремительность (vega)", "combat"),
    "praharZ":("praharṣa", "боевой задор", "combat"),
    "abhyaDAv":("abhyadhāv", "ринуться в атаку", "combat"),
    "samAsAd":("samāsādya", "сойтись (в бою)", "combat"),
}

def find_stem(slp1_toks):
    hits = set()
    for t in slp1_toks:
        for key in MILITARIA:
            if key.lower() in t:
                hits.add(key)
    return hits

def main():
    sund = load_pairs(SUNDARA)
    # restrict candidate Sundara verses to those carrying militaria; focus weight on 42-55
    sund_idx = {}  # stem -> list of (passage, rec, tokset)
    for p, rec in sund.items():
        toks = tokens(rec.get("slp1", ""))
        rec["_toks"] = toks
        for s in find_stem(toks):
            sund_idx.setdefault(s, []).append((p, rec))

    # source index: stem -> list of (parvan, passage, rec) ; also global stem freq
    src = {name: load_pairs(p := CORPUS_DIR / fn) for name, fn in PARVANS.items()}
    src_idx = {}
    for name, d in src.items():
        for p, rec in d.items():
            toks = tokens(rec.get("slp1", ""))
            rec["_toks"] = toks
            for s in find_stem(toks):
                src_idx.setdefault(s, []).append((name, p, rec))

    print("== militaria stems present in BOTH Sundara and battle parvans ==", file=sys.stderr)
    shared = sorted(set(sund_idx) & set(src_idx))
    for s in shared:
        print(f"  {s:10s} sund={len(sund_idx[s]):4d}  src={len(src_idx[s]):5d}", file=sys.stderr)

    # dump raw indices for the curation step
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    dump = {}
    for s in shared:
        dump[s] = {
            "lemma": MILITARIA[s][0],
            "gloss": MILITARIA[s][1],
            "cat": MILITARIA[s][2],
            "sundara": [
                {"passage": p, "chapter": rec.get("chapter"),
                 "sa": rec.get("sa", ""), "ru": rec.get("ru", "")}
                for p, rec in sund_idx[s]
            ],
            "source": [
                {"parvan": name, "passage": p,
                 "sa": rec.get("sa", ""), "ru": rec.get("ru", "")}
                for name, p, rec in src_idx[s]
            ],
        }
    (OUT_DIR / "_mbh_battle_raw_index.json").write_text(
        json.dumps(dump, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"\nwrote raw index: {OUT_DIR/'_mbh_battle_raw_index.json'}", file=sys.stderr)
    print(f"shared stems: {len(shared)}", file=sys.stderr)

if __name__ == "__main__":
    main()

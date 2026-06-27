"""
crosstext_dharmashastra.py

Mine the Mānavadharmaśāstra (Laws of Manu, Elmanovich/Ilyin Russian ed. in the
SamudraManthanam corpus) for cross-text commentary parallels to the WHOLE
Sundarakāṇḍa, with editorial focus on the DHARMAŚĀSTRA cluster: dharma, varṇa,
the rākṣasa category, yuga, ritual/legal termini — Manu being the locus
classicus for normative definitions an indologist reaches for when these terms
surface in the epic.

Output: data/crosstext/dharmashastra.json (list of candidate notes, review_required)

Method (mirrors crosstext_mbh_battle.py):
  1. Build SLP1 content-stem index of Manu and of every Sundara verse.
     Intersect on a CURATED set of dharmaśāstric stems (substring match so
     inflected/compounded forms are caught), dropping function words.
  2. Dump a raw index (manu verses x sundara verses per stem) for curation.
  3. (curation done by the agent reading the raw index, then notes written.)
"""
import sys, json, re, collections
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

CS_DIR     = Path(r"C:\Users\user\Documents\GitHub\CommentaryStrategies")
OUT_DIR    = CS_DIR / "data" / "crosstext"
CORPUS_DIR = Path(r"C:\Users\user\Documents\GitHub\SamudraManthanam\web\corpus_builder\jsonl")
SUNDARA    = CORPUS_DIR / "05_ramayana-sundarakanda.jsonl"
MANU       = CORPUS_DIR / "manavadharmashastra.jsonl"

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
                continue  # skip comm entries
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
    # drop verses without real sanskrit
    return {p: r for p, r in out.items() if r.get("slp1")}

_TOK = re.compile(r'[A-Za-z]+')

def strip_punct(slp1):
    return slp1.replace("।", " ").replace("॥", " ")

def tokens(slp1):
    return [t for t in _TOK.findall(strip_punct(slp1)) if len(t) >= 3]

# ---- dharmaśāstra stem lexicon: SLP1 substring -> (IAST lemma, gloss-ru, cat) ----
# Matched by SUBSTRING (case-sensitive on SLP1) against Sundara tokens, so only
# Sundara verses that actually carry the term are candidate-flagged.
DHARMA = {
    # --- dharma / law / norm ---
    "Darm":    ("dharma", "дхарма (закон, долг, праведность)", "dharma"),
    "aDarm":   ("adharma", "адхарма (беззаконие)", "dharma"),
    "nyAy":    ("nyāya", "правило, должный порядок (nyāya)", "dharma"),
    "satya":   ("satya", "истина, верность слову (satya)", "dharma"),
    "anfta":   ("anṛta", "ложь (anṛta)", "dharma"),
    "vrat":    ("vrata", "обет (vrata)", "vow"),
    "vid":     None,  # too common; placeholder excluded below
    # --- varṇa / āśrama / social order ---
    "varRa":   ("varṇa", "варна (сословие)", "varna"),
    "brAhmaR": ("brāhmaṇa", "брахман (жрец)", "varna"),
    "kzatr":   ("kṣatra", "кшатра (воинское сословие)", "varna"),
    "rAjaDarm":("rājadharma", "царская дхарма (rājadharma)", "varna"),
    "Asram":   ("āśrama", "ашрама (стадия жизни)", "ashrama"),
    "gfhasT":  ("gṛhastha", "домохозяин (gṛhastha)", "ashrama"),
    "tapasv":  ("tapasvin", "подвижник (tapasvin)", "ashrama"),
    "tapas":   ("tapas", "тапас (подвижнический жар)", "tapas"),
    "brahmacar":("brahmacārin", "брахмачарин (ученик)", "ashrama"),
    # --- pativratā / marriage / woman's dharma ---
    "pativrat":("pativratā", "верная мужу жена (pativratā)", "stridharma"),
    "patnI":   ("patnī", "законная супруга (patnī)", "stridharma"),
    "BAryA":   ("bhāryā", "жена (bhāryā)", "stridharma"),
    "vivAh":   ("vivāha", "брак (vivāha)", "stridharma"),
    "kanyA":   ("kanyā", "дева, незамужняя (kanyā)", "stridharma"),
    "rakzaR":  ("rakṣaṇa", "охрана (женщины) (rakṣaṇa)", "stridharma"),
    # --- rākṣasa-category / classes of beings ---
    "rAkzas":  ("rākṣasa", "ракшас (демон-людоед)", "rakshasa"),
    "piSAc":   ("piśāca", "пишача (демон-трупоед)", "rakshasa"),
    "yakz":    ("yakṣa", "якша (полубог-страж богатств)", "rakshasa"),
    "gandArv": ("gandharva", "гандхарва (небесный музыкант)", "rakshasa"),
    "asur":    ("asura", "асур (демон, противник богов)", "rakshasa"),
    "piSit":   ("piśita", "сырое мясо (piśita)", "rakshasa"),
    # --- yuga / cosmic time ---
    "yug":     ("yuga", "юга (мировой период)", "yuga"),
    "kalp":    ("kalpa", "кальпа (мировой цикл)", "yuga"),
    "manvant": ("manvantara", "манвантара (период Ману)", "yuga"),
    # --- sin / merit / retribution / pātaka ---
    "pApa":    ("pāpa", "грех, зло (pāpa)", "karma"),
    "puRya":   ("puṇya", "заслуга, благочестие (puṇya)", "karma"),
    "pAtak":   ("pātaka", "тяжкий грех (pātaka)", "karma"),
    "prAyaScit":("prāyaścitta", "искупление (prāyaścitta)", "karma"),
    "narak":   ("naraka", "ад (naraka)", "karma"),
    "svarg":   ("svarga", "небеса, рай (svarga)", "karma"),
    "pretya":  ("pretya", "в посмертии (pretya)", "karma"),
    "daRq":    ("daṇḍa", "наказание, кара (daṇḍa)", "danda"),
    "vaD":     ("vadha", "убийство, казнь (vadha)", "danda"),
    # --- ritual / purity ---
    "yajY":    ("yajña", "жертвоприношение (yajña)", "ritual"),
    "havi":    ("havis", "жертвенное возлияние (havis)", "ritual"),
    "homa":    ("homa", "возлияние в огонь (homa)", "ritual"),
    "Saoc":    ("śauca", "ритуальная чистота (śauca)", "ritual"),
    "Suci":    ("śuci", "чистый (śuci)", "ritual"),
    "aSuci":   ("aśuci", "нечистый (aśuci)", "ritual"),
    "dAna":    ("dāna", "дарение, щедрость (dāna)", "ritual"),
    "atiTi":   ("atithi", "гость (atithi)", "ritual"),
    "Sapt":    ("śapatha", "клятва (śapatha)", "ritual"),
    "SApa":    ("śāpa", "проклятие (śāpa)", "ritual"),
    "guru":    ("guru", "наставник, старший (guru)", "ritual"),
    # --- guṇa / temperament termini Manu defines ---
    "krUr":    ("krūra", "жестокий (krūra)", "ethos"),
    "lobh":    ("lobha", "алчность (lobha)", "ethos"),
    "kAma":    ("kāma", "вожделение, желание (kāma)", "ethos"),
    "kroD":    ("krodha", "гнев (krodha)", "ethos"),
    "ahiMs":   ("ahiṃsā", "невреждение (ahiṃsā)", "ethos"),
    "hiMs":    ("hiṃsā", "насилие (hiṃsā)", "ethos"),
}
# strip out placeholders
DHARMA = {k: v for k, v in DHARMA.items() if v is not None}

def find_stem(slp1_toks):
    hits = set()
    for t in slp1_toks:
        for key in DHARMA:
            if key in t:
                hits.add(key)
    return hits

def main():
    sund = load_pairs(SUNDARA)
    manu = load_pairs(MANU)
    print(f"Sundara verses w/ sa: {len(sund)}", file=sys.stderr)
    print(f"Manu verses w/ sa:    {len(manu)}", file=sys.stderr)

    sund_idx = {}
    for p, rec in sund.items():
        toks = tokens(rec.get("slp1", ""))
        rec["_toks"] = toks
        for s in find_stem(toks):
            sund_idx.setdefault(s, []).append((p, rec))

    manu_idx = {}
    for p, rec in manu.items():
        toks = tokens(rec.get("slp1", ""))
        rec["_toks"] = toks
        for s in find_stem(toks):
            manu_idx.setdefault(s, []).append((p, rec))

    print("\n== dharmaśāstra stems present in BOTH Sundara and Manu ==", file=sys.stderr)
    shared = sorted(set(sund_idx) & set(manu_idx))
    for s in shared:
        print(f"  {s:10s} {DHARMA[s][0]:14s} sund={len(sund_idx[s]):4d}  manu={len(manu_idx[s]):4d}", file=sys.stderr)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    dump = {}
    for s in shared:
        dump[s] = {
            "lemma": DHARMA[s][0],
            "gloss": DHARMA[s][1],
            "cat": DHARMA[s][2],
            "sundara": [
                {"passage": p, "chapter": rec.get("chapter"),
                 "sa": rec.get("sa", ""), "ru": rec.get("ru", "")}
                for p, rec in sund_idx[s]
            ],
            "manu": [
                {"passage": p, "chapter": rec.get("chapter"),
                 "sa": rec.get("sa", ""), "ru": rec.get("ru", "")}
                for p, rec in manu_idx[s]
            ],
        }
    (OUT_DIR / "_dharmashastra_raw_index.json").write_text(
        json.dumps(dump, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"\nwrote raw index: {OUT_DIR/'_dharmashastra_raw_index.json'}", file=sys.stderr)
    print(f"shared stems: {len(shared)}", file=sys.stderr)

if __name__ == "__main__":
    main()

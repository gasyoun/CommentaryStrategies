"""
crosstext_lexica.py

LEXICA cluster: mine MW, Apte, Kochergina dictionary entries for AUTHORITATIVE
GLOSS SUPPORT to terms in the WHOLE Sundarakanda where Leonov's podstrochnik
under-specifies. The "parallel" here is a dictionary HEADWORD ENTRY, not a verse.

Method:
  1. Build a headword lookup per dict: slp1 headword stem -> {gloss text}.
     (each dict line is one head entry; slp1 field = headword in SLP1, may carry
      a leading '-' or '°' for bound forms -> strip.)
  2. Build SLP1 content-stem multiset of every Sundara verse, with global freq.
  3. For a CURATED set of technical / rare termini that actually occur in Sundara
     (kavya, rakshasa-lore, flora/fauna, realia, ethically loaded words), pull
     the matching headword entry from each dict.
  4. Dump a raw index for agent curation -> data/crosstext/_lexica_raw_index.json
"""
import sys, json, re, collections
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

CS_DIR     = Path(r"C:\Users\user\Documents\GitHub\CommentaryStrategies")
OUT_DIR    = CS_DIR / "data" / "crosstext"
CORPUS_DIR = Path(r"C:\Users\user\Documents\GitHub\SamudraManthanam\web\corpus_builder\jsonl")
SUNDARA    = CORPUS_DIR / "05_ramayana-sundarakanda.jsonl"
MW         = CORPUS_DIR / "dic_mw.jsonl"
APTE       = CORPUS_DIR / "dic_apte.jsonl"
KOCH       = CORPUS_DIR / "kochergina.jsonl"

_TOK = re.compile(r'[A-Za-z]+')

def strip_punct(slp1):
    return slp1.replace("।", " ").replace("॥", " ")

def tokens(slp1):
    return [t for t in _TOK.findall(strip_punct(slp1)) if len(t) >= 3]

# ---------------- Sundara ----------------
def load_sundara():
    out = {}
    with open(SUNDARA, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line: continue
            o = json.loads(line)
            if o.get("deleted"): continue
            if o.get("seg") not in ("sa", "ru"): continue
            p = o["passage"]
            rec = out.setdefault(p, {"chapter": o.get("chapter")})
            if o["seg"] == "sa":
                slp1 = o.get("slp1", "")
                if not slp1 or "{no sanskrit" in slp1: continue
                rec["sa"] = o.get("text", ""); rec["slp1"] = slp1
            else:
                rec["ru"] = o.get("text", "")
    return {p: r for p, r in out.items() if r.get("slp1")}

# ---------------- dict headword lookup ----------------
def clean_head(slp1):
    return slp1.lstrip("-°").strip()

def load_dict(path):
    """slp1 headword -> gloss text (first entry wins for dup heads)."""
    lut = {}
    with open(path, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line: continue
            o = json.loads(line)
            if o.get("deleted"): continue
            h = clean_head(o.get("slp1", ""))
            if not h: continue
            if h not in lut:
                lut[h] = {
                    "text": o.get("text", ""),
                    "iast": (o.get("forms", {}) or {}).get("iast", ""),
                    "id": o.get("id", ""),
                }
    return lut

def main():
    sund = load_sundara()
    print(f"Sundara verses w/ sa: {len(sund)}", file=sys.stderr)

    # global Sundara stem freq
    freq = collections.Counter()
    sund_toks = {}
    for p, rec in sund.items():
        t = tokens(rec["slp1"])
        sund_toks[p] = t
        for w in set(t):  # count verses, not occurrences
            freq[w] += 1

    mw   = load_dict(MW);   print(f"MW heads:   {len(mw)}", file=sys.stderr)
    apte = load_dict(APTE); print(f"Apte heads: {len(apte)}", file=sys.stderr)
    koch = load_dict(KOCH); print(f"Koch heads: {len(koch)}", file=sys.stderr)

    # ---- curated technical termini that occur in Sundara & merit a gloss ----
    # key = SLP1 headword to look up in the dicts; we match Sundara verses whose
    # tokens CONTAIN this key as a substring (so inflected/compound forms hit).
    TERMS = {
        # rakshasa-lore / classes of beings
        "rAkzasa":   ("rākṣasa", "класс существ"),
        "piSAca":    ("piśāca", "класс существ"),
        "yAtu":      ("yātu", "класс существ"),
        "kiMnara":   ("kiṃnara", "класс существ"),
        "gandarva":  ("gandharva", "класс существ"),
        "vidyADara": ("vidyādhara", "класс существ"),
        "apsaras":   ("apsaras", "класс существ"),
        "yakza":     ("yakṣa", "класс существ"),
        "pannaga":   ("pannaga", "класс существ"),
        "uraga":     ("uraga", "класс существ"),
        # vanara / fauna realia
        "plavaga":   ("plavaṅga", "обезьяна (эпич. эпитет)"),
        "plavaMga":  ("plavaṅgama", "обезьяна (эпич. эпитет)"),
        "hari":      ("hari", "обезьяна / конь / эпитет"),
        "SAKAmfga":  ("śākhāmṛga", "обезьяна (\"ветвезверь\")"),
        "kapi":      ("kapi", "обезьяна"),
        # flora / realia of Lanka's gardens
        "aSoka":     ("aśoka", "дерево ашока"),
        "SiMSapA":   ("śiṃśapā", "дерево шиншапа"),
        "campaka":   ("campaka", "дерево чампака"),
        "karRikAra": ("karṇikāra", "дерево карникара"),
        "kiMSuka":   ("kiṃśuka", "дерево кимшука (палаша)"),
        "punnAga":   ("punnāga", "дерево пуннага"),
        "saptaparRa":("saptaparṇa", "дерево саптапарна"),
        "candana":   ("candana", "сандал"),
        # kavya / aesthetic-emotional termini that podstrochnik flattens
        "viraha":    ("viraha", "разлука (как эстет. состояние)"),
        "Soka":      ("śoka", "скорбь"),
        "kAma":      ("kāma", "желание / страсть"),
        "lajjA":     ("lajjā", "стыдливость"),
        "tejas":     ("tejas", "пыл / блеск / мощь"),
        "ojas":      ("ojas", "жизненная сила"),
        "sattva":    ("sattva", "существо / стойкость"),
        "Dfti":      ("dhṛti", "стойкость"),
        "lakzmI":    ("lakṣmī", "краса / благая доля"),
        "SrI":       ("śrī", "блеск / благоденствие"),
        "kAnti":     ("kānti", "сияющая прелесть"),
        # realia: city, palace, vehicles, weapons
        "puzpaka":   ("puṣpaka", "воздушная колесница Куберы"),
        "vimAna":    ("vimāna", "дворец-колесница"),
        "toraRa":    ("toraṇa", "арочные ворота"),
        "prAkAra":   ("prākāra", "крепостная стена"),
        "parigHa":   ("parigha", "засов / палица"),
        "antaHpura": ("antaḥpura", "женские покои"),
        # ascetic / religious termini
        "tapasvin":  ("tapasvin", "подвижник"),
        "mahezvAsa": ("maheṣvāsa", "великий лучник (эпитет)"),
        "durDarza":  ("durdharṣa", "неодолимый (эпитет)"),
        "duranta":   ("duranta", "неодолимый / без конца"),
        # natural-omen / cosmic
        "muhUrta":   ("muhūrta", "мухурта (мера времени)"),
        "lagna":     ("lagna", "благоприятный момент"),
        "nimitta":   ("nimitta", "примета / знамение"),
        "utpAta":    ("utpāta", "зловещее знамение"),
    }

    # index Sundara verses by term (substring on tokens)
    term_hits = {}
    for key in TERMS:
        hits = []
        for p, toks in sund_toks.items():
            if any(key in t for t in toks):
                hits.append(p)
        if hits:
            term_hits[key] = hits

    dump = {}
    for key, hits in term_hits.items():
        iast, cat = TERMS[key]
        entry = {
            "lemma": iast, "cat": cat,
            "n_sundara_verses": len(hits),
            "mw":   mw.get(key, {}).get("text", ""),
            "apte": apte.get(key, {}).get("text", ""),
            "koch": koch.get(key, {}).get("text", ""),
            "sundara": [
                {"passage": p, "chapter": sund[p].get("chapter"),
                 "sa": sund[p].get("sa", ""), "ru": sund[p].get("ru", "")}
                for p in sorted(hits, key=lambda x: (int(x.split('.')[0]), int(x.split('.')[1])))
            ],
        }
        dump[key] = entry

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "_lexica_raw_index.json").write_text(
        json.dumps(dump, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"\nwrote raw index: {OUT_DIR/'_lexica_raw_index.json'}", file=sys.stderr)
    print(f"terms with Sundara hits: {len(term_hits)}", file=sys.stderr)
    for key in sorted(term_hits, key=lambda k: -len(term_hits[k])):
        haveg = []
        if mw.get(key): haveg.append("MW")
        if apte.get(key): haveg.append("Ap")
        if koch.get(key): haveg.append("Ko")
        print(f"  {key:12s} {TERMS[key][0]:14s} n={len(term_hits[key]):3d}  dicts={','.join(haveg) or 'NONE'}", file=sys.stderr)

if __name__ == "__main__":
    main()

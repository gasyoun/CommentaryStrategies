#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mine rare shared SLP1 content stems between Sundarakanda (kn. V) and
Ramayana I-III (Bala/Ayodhya/Aranya) for genuine intratextual parallels.

Outputs a raw candidate index (rare-stem -> sundara verses + earliest source
verse) to data/crosstext/_grintser_raw_index.json. The final curated notes are
authored by hand from this index.
"""
import json, sys, re, os
from collections import defaultdict, Counter

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

JSONL_DIR = r"C:\Users\user\Documents\GitHub\SamudraManthanam\web\corpus_builder\jsonl"
SRC_FILES = {
    "I": ("01_ramayana-balakanda.jsonl",   "Rām. Bāla"),
    "II": ("02_ramayana-ayodhyakanda.jsonl", "Rām. Ayodhyā"),
    "III": ("03_ramayana-aranyakanda.jsonl", "Rām. Araṇya"),
}
SUNDARA = "05_ramayana-sundarakanda.jsonl"
OUT = r"C:\Users\user\Documents\GitHub\CommentaryStrategies\data\crosstext\_grintser_raw_index.json"

# very common SLP1 stems / function words to drop (not content)
STOP = set("""
ca tu hi vA eva iva tataH tato tatra atha api na no mA sa saH tat tad tasya tasmin
te tAH tAn tAni yaH yat ye yA yan yena yasya sma kim ko kaH kaSca iti asya enam enaM
ayaM idaM ezaH eza asti AsIt aBavat babhUva tathA evaM yathA punaH punar saH tAm imAM
aham ahaM mAm mama me tvam tvAm tava nas vas saMnidhO ataH tu ha vai nu khalu uta cet
 advaitam SrI atra kvacit param paraM sarva sarve sarvam sarvAn sarvaM kaScid kaScit
mahA mahat mahAn mahatI mahatA bhUya bhUyas saMprati sAmprata loka bhU bhUmi nara nR
naraH dina rAtri kAla samaya gam Agam pratiyA yA i gaM gata gatvA gacCati
asmin teza yathA tathA yad yataH sma uvAca abravIt vacaH vAkya gira Aha procya uktvA
dfS dfzwa dfzwvA paSya paSyati apaSyat dadarSa ICa kf kfta karma kftvA karoti cakAra
bhU babhUva bhavati bhUtvA as Asa AsIt sTita sTA sTitaH dA dadO datta gfh gfhIta
han hatvA hata yA yAti gata ev tat saH sa tasmAt tena
""".split())

VERSE_RE = re.compile(r'[।॥|\d०-९॰\.\-]')

def slp1_tokens(slp1):
    # strip danda/numbers, split on space
    s = re.sub(r'[।॥|]', ' ', slp1)
    s = re.sub(r'[0-9]', ' ', s)
    toks = [t.strip() for t in s.split() if t.strip()]
    return toks

def crude_stem(tok):
    """Very rough stemming: strip a handful of common inflectional endings so
    that e.g. 'vAnaraH','vAnaram','vAnareRa' collapse. Conservative."""
    t = tok
    # long compound: keep last member if hyphen-like; we treat whole token though
    for suf in ['eByaH','AByAm','Anam','AnAm','ezu','ENaH','eRa','asya','AyAH','AyAm',
                'ABiH','ezAm','ABiH','asya','ebhyaH','Asu','Ani','ANi','ena','eza',
                'asaH','iByaH','uByaH','iBiH','uBiH','ayaH','avaH','InAm','UnAm',
                'AH','aH','am','aM','As','an','At','Ai','O','O','Ena','sya','os',
                'I','U','iH','uH','iM','uM','iB','uB','e','A','aiH']:
        if t.endswith(suf) and len(t) - len(suf) >= 3:
            return t[:-len(suf)]
    return t

def load_verses(path):
    """Return dict passage -> {'sa','ru','slp1','chapter'}"""
    out = {}
    with open(path, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line: continue
            o = json.loads(line)
            if o.get('deleted'): continue
            p = o['passage']; seg = o['seg']
            d = out.setdefault(p, {'sa':'','ru':'','slp1':'','chapter':o.get('chapter','')})
            if seg == 'sa':
                d['sa'] = o.get('text',''); d['slp1'] = o.get('slp1','')
            elif seg == 'ru':
                d['ru'] = o.get('text','')
    return out

# --- build source stem -> earliest (book, passage) index ---
src_stem_first = {}   # stem -> (book, passage)
src_stem_count = Counter()
src_verses = {}       # (book,passage) -> verse dict
for book, (fn, label) in SRC_FILES.items():
    vs = load_verses(os.path.join(JSONL_DIR, fn))
    for p, d in vs.items():
        src_verses[(book, p)] = d
        seen_in_v = set()
        for tok in slp1_tokens(d['slp1']):
            st = crude_stem(tok)
            if st in STOP or len(st) < 4: continue
            src_stem_count[st] += 1
            if st not in seen_in_v:
                seen_in_v.add(st)
            if st not in src_stem_first:
                src_stem_first[st] = (book, p, label)

# --- sundara stems ---
sun = load_verses(os.path.join(JSONL_DIR, SUNDARA))
sun_stem_verses = defaultdict(list)
sun_stem_count = Counter()
for p, d in sun.items():
    seen = set()
    for tok in slp1_tokens(d['slp1']):
        st = crude_stem(tok)
        if st in STOP or len(st) < 4: continue
        if st not in seen:
            seen.add(st)
            sun_stem_verses[st].append(p)
        sun_stem_count[st] += 1

# --- intersect on RARE shared stems ---
# rare = appears few times in source AND in sundara (content-bearing, not formulaic filler)
shared = []
for st, srcfirst in src_stem_first.items():
    if st not in sun_stem_verses: continue
    sc = src_stem_count[st]
    uc = sun_stem_count[st]
    # rare band: not ultra-frequent. Keep stems that are distinctive.
    if sc > 220 or uc > 160:   # drop very high-frequency stems
        continue
    shared.append((st, sc, uc, srcfirst, sun_stem_verses[st]))

# sort: prefer genuinely rare (low source count), then moderate sundara presence
shared.sort(key=lambda x: (x[1] + x[2]))

index = {}
for st, sc, uc, srcfirst, sunps in shared:
    book, p, label = srcfirst
    sv = src_verses[(book, p)]
    # limit sundara verse list size
    def passkey(pp):
        a,b = pp.split('.'); return (int(a), int(b))
    sunps_sorted = sorted(set(sunps), key=passkey)
    index[st] = {
        "stem": st,
        "src_count": sc,
        "sun_count": uc,
        "src_book": book,
        "src_label": label,
        "src_passage": p,
        "src_addr": f"{label} {book.replace('I','').replace('V','') or ''}".strip(),
        "src_sa": sv['sa'],
        "src_ru": sv['ru'],
        "sundara_passages": sunps_sorted[:40],
    }

with open(OUT, 'w', encoding='utf-8') as f:
    json.dump(index, f, ensure_ascii=False, indent=1)

print(f"source verses I-III: {len(src_verses)}")
print(f"sundara verses: {len(sun)}")
print(f"distinct sundara content stems: {len(sun_stem_verses)}")
print(f"rare shared stems: {len(index)}")
print(f"wrote {OUT}")
# print a digest of the rarest 60 for hand-curation
print("\n=== rarest shared content stems (st | srcCount | sunCount | srcBook.passage) ===")
for st, sc, uc, srcfirst, sunps in shared[:120]:
    print(f"{st:18s} {sc:4d} {uc:4d}  {srcfirst[0]}.{srcfirst[1]:8s}  sun:{','.join(sorted(set(sunps),key=lambda pp:(int(pp.split('.')[0]),int(pp.split('.')[1])))[:6])}")

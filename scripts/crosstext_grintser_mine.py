"""
crosstext_grintser_mine.py — CANDIDATE MINER for the cluster
"Рамаяна I-III (Гринцер) — углубление" (ramayana_grintser).

INTRATEXTUAL parallels: build SLP1 content-stem sets of the source kāṇḍas
(I Bālakāṇḍa, II Ayodhyākāṇḍa, III Araṇyakāṇḍa) and intersect with each
Sundarakāṇḍa (kn. V) verse on RARE shared stems. For each promising stem,
locate the real parallel verse in the source, pull its #sa (IAST) + #ru
(Гринцер-школа подстрочник), so a human can judge genuine illumination.

UTF-8, no BOM.
"""
import sys, json, re, collections
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

CORPUS = Path(r"C:\Users\user\Documents\GitHub\SamudraManthanam\web\corpus_builder\jsonl")
SUND   = CORPUS / "05_ramayana-sundarakanda.jsonl"
SOURCES = {
    "balakanda":    CORPUS / "01_ramayana-balakanda.jsonl",
    "ayodhyakanda": CORPUS / "02_ramayana-ayodhyakanda.jsonl",
    "aranyakanda":  CORPUS / "03_ramayana-aranyakanda.jsonl",
}
ROMAN = {"balakanda": "I", "ayodhyakanda": "II", "aranyakanda": "III"}

def load_jsonl(p):
    rows = []
    with open(p, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                try: rows.append(json.loads(line))
                except json.JSONDecodeError: pass
    return rows

_TOK = re.compile(r'[A-Za-z][A-Za-z]{2,}')
# very common epic function/connective stems + ubiquitous epithet words
STOP = set("""tat tato tata tatas iva ca cha tu iti eva api hi na sa se te tam sma vai yat
kim yad tad idam asya tasya atra tatra yatra puna atha atah ata ha svam tena yena anu upa
pra sam pari nis nir dur sus abhi avi ava ati adhi aha ima para param asmin tasmAt yasmin
enam etat etad ayam imAn aham mama tvam mAm me uta vA yaTA taTA sarva sarve sarvam asti
bhU bhUta kf kfta gata yA gam gacCati gatA tasmin tasmAd tAni tasya tasyA tAM tAn
naras nara narA mahat mahA mahAn rAma rAmas rAmaM rAmasya sItA sItAM sItAyAH evam tadA
yadA kfTA kftvA tAvat yAvat sarvataH samantAt ucyate uvAca abravIt vAkyam vacanam
gatvA dfzwvA SrutvA prApya tasyAH tasyAm itara tena""".split())

def stems(slp1):
    toks = _TOK.findall(slp1.lower())
    out = set()
    for t in toks:
        if len(t) < 4: continue
        if t in STOP: continue
        out.add(t)
    return out

# ---- load sources ----
stem_locus = collections.defaultdict(list)   # stem -> [(work, passage, text)]
stem_df = collections.Counter()              # in how many of the 3 kandas
src_rows = {}
for work, path in SOURCES.items():
    rows = [r for r in load_jsonl(path) if r.get("seg") == "sa"]
    src_rows[work] = {r["passage"]: r for r in rows}
    work_stems = set()
    for r in rows:
        s = stems(r.get("slp1", ""))
        for st in s:
            stem_locus[st].append((work, r["passage"], r.get("text")))
        work_stems |= s
    for st in work_stems:
        stem_df[st] += 1

src_freq = collections.Counter({st: len(loci) for st, loci in stem_locus.items()})

# ---- Sundara ----
sund = [r for r in load_jsonl(SUND) if r.get("seg") == "sa"]
sund_freq = collections.Counter()
sund_stems = {}
for r in sund:
    s = stems(r.get("slp1", ""))
    sund_stems[r["passage"]] = s
    for st in s: sund_freq[st] += 1

# ---- rare shared stems ----
MIN_LEN  = 6
SRC_MAX  = 18    # not ubiquitous across the 3 source kandas
SUND_MAX = 14    # not ubiquitous in Sundara
shared = set(sund_freq) & set(src_freq)
ranked = []
for st in shared:
    if len(st) < MIN_LEN: continue
    if src_freq[st] > SRC_MAX: continue
    if sund_freq[st] > SUND_MAX: continue
    sund_pass = [r["passage"] for r in sund if st in sund_stems[r["passage"]]]
    ranked.append((st, sund_pass))

ranked.sort(key=lambda kv: (src_freq[kv[0]] + sund_freq[kv[0]]))

print(f"# rare shared stems: {len(ranked)} (MIN_LEN={MIN_LEN} SRC_MAX={SRC_MAX} SUND_MAX={SUND_MAX})")
for st, sund_pass in ranked:
    loci = stem_locus[st]
    print(f"\n=== STEM {st}  src_freq={src_freq[st]} sund_freq={sund_freq[st]} kandas={stem_df[st]}")
    print(f"    Sundara V.: {sund_pass[:14]}")
    for w, p, t in loci[:8]:
        print(f"    [{ROMAN[w]}.{p} {w}] {t[:95]}")

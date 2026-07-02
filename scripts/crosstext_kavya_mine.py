"""
crosstext_kavya_mine.py  — CANDIDATE MINER (not the writer)

Build SLP1 content-stem sets for the kāvya cluster
(Raghuvaṃśa, Kumārasambhava, Meghadūta, Buddhacarita, Gītagovinda, Śatakatraya)
and intersect with each Sundarakāṇḍa verse on RARE shared stems.
Print, per Sundara verse, the rare shared stems plus the located source loci,
so a human can judge genuine illumination.

UTF-8, no BOM.
"""
import sys, json, re, collections
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

CORPUS = Path(r"C:\Users\user\Documents\GitHub\SamudraManthanam\web\corpus_builder\jsonl")
SUND   = CORPUS / "05_ramayana-sundarakanda.jsonl"
SOURCES = {
    "raghuvamsha":   CORPUS / "raghuvamsha.jsonl",
    "kumarasambhava":CORPUS / "kumarasambhava.jsonl",
    "megha-duta":    CORPUS / "megha-duta.jsonl",
    "buddhacharita": CORPUS / "buddhacharita.jsonl",
    "gitagovinda":   CORPUS / "gitagovinda.jsonl",
    "shatakatrayam": CORPUS / "shatakatrayam.jsonl",
}

def load_jsonl(p):
    rows=[]
    with open(p, encoding='utf-8') as f:
        for line in f:
            line=line.strip()
            if line:
                try: rows.append(json.loads(line))
                except json.JSONDecodeError: pass
    return rows

_TOK = re.compile(r'[A-Za-z][A-Za-z]{2,}')
STOP = set("""tat tato tata tatas iva ca cha tu iti eva api hi na sa se te tam sma vai yat
kim yad tad idam asya tasya atra tatra yatra puna atha atah ata ha svam tena yena anu upa
pra sam pari nis nir dur sus abhi avi ava ati adhi aha ima para param asmin tasmAt yasmin
enam etat etad ayam imAn aham mama tvam mAm me tu uta vA yaTA taTA sarva sarve sarvam asti
bhU bhUta kf kfta gata yA gam gacCati gatA ca""".split())

def stems(slp1):
    toks=_TOK.findall(slp1.lower())
    out=set()
    for t in toks:
        if len(t)<4: continue
        if t in STOP: continue
        out.add(t)
    return out

# load sources, build per-stem -> list of (work, passage)
src_rows={}
stem_locus=collections.defaultdict(list)   # stem -> [(work,passage,text)]
stem_df=collections.Counter()              # how many works contain the stem
for work,path in SOURCES.items():
    rows=[r for r in load_jsonl(path) if r.get("seg")=="sa"]
    src_rows[work]=rows
    work_stems=set()
    for r in rows:
        s=stems(r.get("slp1",""))
        for st in s:
            stem_locus[st].append((work, r.get("passage"), r.get("text")))
        work_stems|=s
    for st in work_stems:
        stem_df[st]+=1

# global source frequency (how many source verses contain stem)
src_freq=collections.Counter()
for st,loci in stem_locus.items():
    src_freq[st]=len(loci)

# Sundara stem frequency
sund=[r for r in load_jsonl(SUND) if r.get("seg")=="sa"]
sund_freq=collections.Counter()
sund_stems={}
for r in sund:
    s=stems(r.get("slp1",""))
    sund_stems[r["passage"]]=s
    for st in s: sund_freq[st]+=1

# RARE shared stems: appears in sources but with bounded freq, and rare-ish in Sundara
MIN_LEN=5
SRC_MAX=40     # not ubiquitous in kavya cluster
SUND_MAX=25    # not ubiquitous in Sundara
candidates=collections.defaultdict(list)  # stem -> list of sundara passages
shared=set(sund_freq)&set(src_freq)
for st in shared:
    if len(st)<MIN_LEN: continue
    if src_freq[st]>SRC_MAX: continue
    if sund_freq[st]>SUND_MAX: continue
    # which sundara verses
    for r in sund:
        if st in sund_stems[r["passage"]]:
            candidates[st].append(r["passage"])

# rank stems by rarity (low combined freq, present in source)
ranked=sorted(candidates.items(), key=lambda kv:(src_freq[kv[0]]+sund_freq[kv[0]]))

print(f"# shared rare stems: {len(ranked)}")
for st, sund_pass in ranked:
    if src_freq[st] < 1: continue
    loci=stem_locus[st]
    # show
    print(f"\n=== STEM {st}  src_freq={src_freq[st]} sund_freq={sund_freq[st]} works={stem_df[st]}")
    print(f"    Sundara verses: {sund_pass[:12]}")
    seen=set()
    for w,p,t in loci[:6]:
        print(f"    [{w} {p}] {t[:90]}")

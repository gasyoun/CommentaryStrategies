"""
kavya_lookup.py  — verse fetcher for curating kavya cross-text notes.
Usage:
  python kavya_lookup.py sund 1.1 1.2 ...           # fetch Sundara verses (sa+ru)
  python kavya_lookup.py SRC raghuvamsha 1.1 ...     # fetch source verses (sa+ru)
  python kavya_lookup.py grep SRC <substr>          # grep a source for a slp1/text substr
UTF-8 no BOM.
"""
import sys, json
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

CORPUS = Path(r"C:\Users\user\Documents\GitHub\SamudraManthanam\web\corpus_builder\jsonl")
FILES = {
 "sund":"05_ramayana-sundarakanda.jsonl",
 "raghuvamsha":"raghuvamsha.jsonl","kumarasambhava":"kumarasambhava.jsonl",
 "megha-duta":"megha-duta.jsonl","buddhacharita":"buddhacharita.jsonl",
 "gitagovinda":"gitagovinda.jsonl","shatakatrayam":"shatakatrayam.jsonl",
}
def load(key):
    rows=[]
    with open(CORPUS/FILES[key],encoding='utf-8') as f:
        for line in f:
            line=line.strip()
            if line:
                try: rows.append(json.loads(line))
                except: pass
    return rows

def show(rows, passages):
    idx={}
    for r in rows:
        idx.setdefault(r["passage"],{})[r["seg"]]=r["text"]
    for p in passages:
        d=idx.get(p)
        if not d:
            # fuzzy: find passages containing p
            cand=[k for k in idx if k==p or k.startswith(p) or p in k]
            print(f"--- {p}: NOT FOUND exact; near={cand[:5]}")
            continue
        print(f"=== {p}")
        if "sa" in d: print("  SA:", d["sa"])
        if "ru" in d: print("  RU:", d["ru"])

cmd=sys.argv[1]
if cmd=="sund":
    show(load("sund"), sys.argv[2:])
elif cmd=="SRC":
    show(load(sys.argv[2]), sys.argv[3:])
elif cmd=="grep":
    rows=load(sys.argv[2]); sub=sys.argv[3].lower()
    for r in rows:
        if r.get("seg")=="sa" and (sub in r.get("slp1","").lower() or sub in r.get("text","").lower()):
            print(f"[{r['passage']}] {r['text'][:140]}")

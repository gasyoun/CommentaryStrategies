#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Targeted lookup helper: given a list of SLP1 substrings, find in Books I-III
the BEST (earliest / most salient) exemplar verse and the Sundara verses that
share it. Used to author the curated grintser cross-text notes by hand.
"""
import json, sys, re, os
sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

JSONL_DIR = r"C:\Users\user\Documents\GitHub\SamudraManthanam\web\corpus_builder\jsonl"
SRC = [("01_ramayana-balakanda.jsonl","Rām. Bāla","I"),
       ("02_ramayana-ayodhyakanda.jsonl","Rām. Ayodhyā","II"),
       ("03_ramayana-aranyakanda.jsonl","Rām. Araṇya","III")]
SUNDARA = "05_ramayana-sundarakanda.jsonl"

def load(path):
    out={}
    for line in open(path,encoding='utf-8'):
        line=line.strip()
        if not line: continue
        o=json.loads(line)
        if o.get('deleted'): continue
        p=o['passage']; d=out.setdefault(p,{'sa':'','ru':'','slp1':'','ch':o.get('chapter','')})
        if o['seg']=='sa': d['sa']=o.get('text',''); d['slp1']=o.get('slp1','')
        elif o['seg']=='ru': d['ru']=o.get('text','')
    return out

src=[]
for fn,label,bk in SRC:
    src.append((label,bk,load(os.path.join(JSONL_DIR,fn))))
sun=load(os.path.join(JSONL_DIR,SUNDARA))

def _num(x):
    m=re.match(r'\d+', x); return int(m.group()) if m else 0
def pk(p):
    parts=p.split('.'); a=parts[0]; b=parts[1] if len(parts)>1 else '0'
    return (_num(a), _num(b))

# query terms passed on argv
terms = sys.argv[1:]
for term in terms:
    t=term.lower()
    print("="*70)
    print("TERM:", term)
    # source hits, earliest per book
    for label,bk,vs in src:
        hits=[p for p,d in vs.items() if t in d['slp1'].lower()]
        if not hits: continue
        hits.sort(key=pk)
        p=hits[0]; d=vs[p]
        print(f"  [{label} {bk}.{p}]  (n={len(hits)})")
        print("   SA:", d['sa'])
        print("   RU:", d['ru'])
    # sundara hits
    shits=[(p,d) for p,d in sun.items() if t in d['slp1'].lower()]
    shits.sort(key=lambda x: pk(x[0]))
    print(f"  -- Sundara hits: {len(shits)} -> {','.join('V.'+p for p,_ in shits[:12])}")
    for p,d in shits[:6]:
        print(f"   [V.{p}] SA:", d['sa'])
        print(f"          RU:", d['ru'])

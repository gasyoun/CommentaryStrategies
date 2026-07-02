#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Locator helper: for given (stem, work) print the matching source verses
and the matching Sundara verses, so the curator can pick the best parallel."""
import sys, json, re
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

CORPUS_DIR = Path(r"C:\Users\user\Documents\GitHub\SamudraManthanam\web\corpus_builder\jsonl")
SUNDARA = CORPUS_DIR / "05_ramayana-sundarakanda.jsonl"
WORKS = {
    "Raghuvaṃśa":"raghuvamsha.jsonl","Kumārasambhava":"kumarasambhava.jsonl",
    "Meghadūta":"megha-duta.jsonl","Gītagovinda":"gitagovinda.jsonl",
    "Buddhacarita":"buddhacharita.jsonl","Amaruśataka":"amaru-shataka.jsonl",
    "Śatakatraya":"shatakatrayam.jsonl",
}
def load_pairs(path):
    out={}
    for line in open(path,encoding='utf-8'):
        line=line.strip()
        if not line: continue
        o=json.loads(line)
        if o.get("deleted"): continue
        seg=o.get("seg")
        if seg not in("sa","ru"): continue
        p=o["passage"]; rec=out.setdefault(p,{"chapter":o.get("chapter")})
        if seg=="sa": rec["sa"]=o.get("text","");rec["slp1"]=o.get("slp1","")
        else: rec["ru"]=o.get("text","")
    return out

def search(d, sub):
    res=[]
    for p,rec in d.items():
        if sub in rec.get("slp1",""):
            res.append((p,rec))
    return res

if __name__=="__main__":
    sub=sys.argv[1]          # SLP1 substring
    work=sys.argv[2] if len(sys.argv)>2 else None
    sund=load_pairs(SUNDARA)
    print(f"=== SUNDARA matches for '{sub}' ===")
    for p,rec in search(sund,sub):
        print(f"[V.{p}] SA: {rec.get('sa','')}")
        print(f"        RU: {rec.get('ru','')}")
    if work:
        d=load_pairs(CORPUS_DIR/WORKS[work])
        print(f"\n=== {work} matches for '{sub}' ===")
        for p,rec in search(d,sub):
            print(f"[{work} {p}] SA: {rec.get('sa','')}")
            print(f"        RU: {rec.get('ru','')}")

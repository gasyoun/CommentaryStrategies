"""Inspect specific candidate stems: print the full sa+ru parallel pairs so the
judge (LLM) can author notes. Reads the candidate dump; filters by a watchlist of
cluster-relevant stems (epic formulae, similes, divine beings, epithets)."""
import sys, json
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

CAND = Path(r"C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\e26123ee-a72f-4004-8cfb-8f040c528361\scratchpad\mbh_candidates.json")
d = json.load(open(CAND, encoding='utf-8'))
top = d['top']

# Watchlist: cluster-relevant roots (substring match on stem). Epic formulae,
# similes (upamāna: simha/mahendra/meru/garuda/uraga/ulkā), divine beings,
# stock epithets, gnomic terms.
WATCH = sys.argv[1:] if len(sys.argv) > 1 else [
    'mahorag','BujaNg','pannag','nAgA','kUrm','garuq','suparR','uraga',
    'aprameya','mArutAtmaja','devarAw','ulkA','meru','mandara','mahendra',
    'siMha','vyAGr','gaja','mAtaNga','vfzaB','SArdUl','airAvat','vAsavi',
    'aYjali','atiTi','pUjArh','satkriyA','sammAn','kftAYjali',
    'manyu','amarz','tejas','pratApa','ojas','vikrama','parAkrama',
    'aSani','vajra','kAla','antaka','yama','mftyu','kftAnt',
    'ratnamay','jAtarUpa','hAwak','kAYcan','tapanIya',
    'cAraR','gandharv','yakza','kinnar','vidyADar','apsaras',
    'aMSumat','divAkar','BAskar','candram','SaSaN','rAhu',
]

def matches(stem):
    s = stem.lower()
    return any(w.lower() in s for w in WATCH)

picked = [c for c in top if matches(c['stem'])]
print(f"# {len(picked)} watch-matched candidates\n")
for c in picked:
    print("="*90)
    print(f"STEM {c['stem']}  | {c['work']}  sun={c['sun_count']} src={c['src_count']} spread={c['spread']} score={c['score']}")
    seen=set()
    for s in c['samples']:
        key=(s['sun_addr'], s['src_addr'])
        if key in seen: continue
        seen.add(key)
        print(f"  SUN {s['sun_addr']}: {s['sun_sa']}")
        print(f"      RU: {s['sun_ru']}")
        print(f"  SRC {s['src_addr']}: {s['src_sa']}")
        print(f"      RU: {s['src_ru']}")
        print()

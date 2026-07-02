"""
sundara_mbh_narrative_mine.py — candidate extractor for cluster mbh_narrative.

Mine rare shared SLP1 content-stems between the WHOLE Sundarakāṇḍa and the five
Mahābhārata narrative parvas (Ādi / Sabhā / Āraṇyaka / Virāṭa / Udyoga). For each
rare shared stem, locate the best parallel verse on each side and dump #sa + #ru so
a human/LLM judge can decide whether the parallel genuinely illuminates the Sundara
verse (shared formula/epithet, simile upamāna, mythological cross-ref, divine being,
gnomic parallel).

Output: scratchpad/mbh_candidates.json (ranked candidate pairs, NOT final notes).
"""
import sys, json, re, collections
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

CORPUS = Path(r"C:\Users\user\Documents\GitHub\SamudraManthanam\web\corpus_builder\jsonl")
OUT    = Path(r"C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\e26123ee-a72f-4004-8cfb-8f040c528361\scratchpad\mbh_candidates.json")

SUNDARA = "05_ramayana-sundarakanda.jsonl"
SOURCES = [
    "01_mahabharata-adiparva.jsonl",
    "02_mahabharata-sabhaparva.jsonl",
    "03_mahabharata-aranyakaparva.jsonl",
    "04_mahabharata-virataparva.jsonl",
    "05_mahabharata-udyogaparva.jsonl",
]
LABELS = {
    "01_mahabharata-adiparva":   "Mahābhārata, Ādiparva",
    "02_mahabharata-sabhaparva": "Mahābhārata, Sabhāparva",
    "03_mahabharata-aranyakaparva": "Mahābhārata, Āraṇyaka(Vana)parva",
    "04_mahabharata-virataparva":"Mahābhārata, Virāṭaparva",
    "05_mahabharata-udyogaparva":"Mahābhārata, Udyogaparva",
}

# Ultra-common epic function words / particles / pronouns / ubiquitous verbs+stems.
STOP = set("""
tat tato tatas tatra tada tadā iva ca tu iti eva api hi na sa te tam tan sma vai
yat kim yad tad idam asya tasya atra yatra yatha tathā tatha puna punar atha
atah ata ha svam tena yena cha anu upa pra sam pari nis nir dur sus abhi avi ava
ati adhi aha ima maha mahA para param asmin tasmAt yasmin enam etat etad ayam imAn
aham mama me tvam tava te vā va so 'sya 'pi 'tha 'bhavat 'bravIt evam tāḥ tān tāṃ
yaḥ yā ye yān yām sā taiḥ tair tais kaḥ kā ke nara naram nareṣu rājan rājā rājñaḥ
abravIt uvāca bravIti bhavati babhūva āsīt āsa gata gatā prāpya kṛtvā tasmin
ubha ubhau sarva sarve sarvān sarvāḥ kāma artha bahu mahat mahā tasyāḥ tāsāṃ
naḥ vaḥ asmākam yuṣmākam tataḥ kaścit kecit kasya kasmin
nfpa nfpati BUmi loka jagat sthita sthitā vacana vAkya uvac
abravIt provAca sūta vāsudeva
""".split())

# Pure-SLP1 STOP variants (the slp1 field uses A I U f x E O M H etc.)
STOP_SLP1 = set("""
tato tatas tatra tadA iva ca tu iti eva api hi na sa te tam tan sma vE yat kim yad
tad idam asya tasya atra yatra yaTA taTA tatha punar aTa ataH ata ha svam tena yena
ca anu upa pra sam pari nis nir dur sus aBi avi ava ati aDi aha ima mahA para param
asmin tasmAt yasmin enam etat etad ayam imAn aham mama me tvam tava vA so api aTa
evam yaH yA ye yAn yAm sA tEH tEs kaH kA ke nara naram narezu rAjan rAjA rAjYaH
abravIt uvAca BavataH Bavati baBUva AsIt Asa gata gatA prApya kftvA tasmin uBa uBO
sarva sarve sarvAn sarvAH kAma arTa bahu mahat mahA tasyAH tAsAM naH vaH asmAkam
yuzmAkam kaScit kecit kasya kasmin nfpa nfpati BUmi loka jagat sTita sTitA vacana
vAkya provAca sUta vAsudeva BavAn BAryA putra putraH rAjaputra nAma nAmnA gacCati
""".split())

_TOK = re.compile(r'[A-Za-z]{4,}')   # require length >=4 in slp1 to cut tiny words

def load(path):
    sa, ru = {}, {}
    with open(path, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            o = json.loads(line)
            if o.get('deleted'):
                continue
            p = o['passage']; seg = o['seg']
            if seg == 'sa':
                sa[p] = o
            elif seg == 'ru':
                ru[p] = o
    return sa, ru

def stems(slp1):
    out = set()
    for t in _TOK.findall(slp1):
        if t in STOP_SLP1:
            continue
        # crude stemming: drop common nominal/verbal endings to merge inflections
        base = t
        for suf in ('asya','AnAm','AByAm','ezu','ena','Aya','asya','AH','An','Am',
                    'aH','am','At','os','oH','A','I','U','as','is','us','e','o','M','H'):
            if base.endswith(suf) and len(base)-len(suf) >= 4:
                base = base[:-len(suf)]
                break
        if len(base) >= 4 and base not in STOP_SLP1:
            out.add(base)
    return out

def main():
    sun_sa, sun_ru = load(CORPUS / SUNDARA)
    # stem -> set of sundara passages
    sun_idx = collections.defaultdict(set)
    for p, o in sun_sa.items():
        for s in stems(o['slp1']):
            sun_idx[s].add(p)
    sun_stem_count = {s: len(ps) for s, ps in sun_idx.items()}

    # load all sources, build a combined source index + per-work index
    src_sa = {}      # work -> {passage: obj}
    src_ru = {}
    src_idx = {}     # work -> {stem: set(passages)}
    global_stem_works = collections.defaultdict(set)
    for fn in SOURCES:
        work = fn[:-6]
        sa, ru = load(CORPUS / fn)
        src_sa[work] = sa; src_ru[work] = ru
        idx = collections.defaultdict(set)
        for p, o in sa.items():
            for s in stems(o['slp1']):
                idx[s].add(p)
                global_stem_works[s].add(work)
        src_idx[work] = idx

    # candidate stems: shared, RARE on the Sundara side, and not omnipresent across MBh.
    candidates = []
    for s, sun_ps in sun_idx.items():
        sc = len(sun_ps)
        if sc == 0 or sc > 25:        # too common in Sundara -> drop
            continue
        for work, idx in src_idx.items():
            if s not in idx:
                continue
            src_ps = idx[s]
            mc = len(src_ps)
            if mc == 0 or mc > 40:     # too common in this parva -> drop
                continue
            # rarity score: rarer on both sides + appearing in fewer of the 5 parvas = better
            spread = len(global_stem_works[s])
            score = 1.0/(sc) + 1.0/(mc) + 1.0/spread
            candidates.append({
                'stem': s, 'work': work, 'sun_count': sc, 'src_count': mc,
                'spread': spread, 'score': round(score,4),
                'sun_passages': sorted(sun_ps)[:6],
                'src_passages': sorted(src_ps)[:6],
            })

    candidates.sort(key=lambda c: -c['score'])

    # attach actual verse text for the top N for judging
    top = candidates[:400]
    for c in top:
        work = c['work']
        c['samples'] = []
        # pick first sundara passage + first source passage as exemplar pair;
        # include up to 3 source passages so judge can pick the closest formula
        for sp in c['sun_passages'][:2]:
            sun = sun_sa.get(sp); sru = sun_ru.get(sp)
            for xp in c['src_passages'][:3]:
                so = src_sa[work].get(xp); sro = src_ru[work].get(xp)
                if sun and so:
                    c['samples'].append({
                        'sun_addr': sp,
                        'sun_sa': sun['text'],
                        'sun_slp1': sun['slp1'],
                        'sun_ru': sru['text'] if sru else '',
                        'src_addr': xp,
                        'src_sa': so['text'],
                        'src_ru': sro['text'] if sro else '',
                    })
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT, 'w', encoding='utf-8') as f:
        json.dump({'n_candidates': len(candidates), 'top': top}, f, ensure_ascii=False, indent=1)
    print('candidates', len(candidates), '-> wrote top', len(top), 'to', OUT)
    # quick console digest of the rarest 60
    for c in candidates[:60]:
        print(f"{c['score']:.3f}  {c['stem']:16s} sun={c['sun_count']:2d} {c['work'][3:]:28s} src={c['src_count']:2d} spread={c['spread']}")

if __name__ == '__main__':
    main()

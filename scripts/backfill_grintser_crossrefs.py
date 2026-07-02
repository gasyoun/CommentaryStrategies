"""Idempotent corpus-driven Grintser cross-ref backfill for Sundara В-realia notes.
Only entities CONFIRMED in Grintser's glossary (Books I-II) AND found as a proper
inflected form in Books I-III text. Coordinate = first appearance (corpus-derived);
review_required so the editor confirms against Grintser's printed apparatus."""
import json,sys,re,unicodedata
sys.stdout.reconfigure(encoding='utf-8'); sys.stderr.reconfigure(encoding='utf-8')
S='C:/Users/user/Documents/GitHub/SamudraManthanam/web/corpus_builder/jsonl/'
M=[('ā','A'),('ī','I'),('ū','U'),('ṝ','F'),('ṛ','f'),('ḹ','X'),('ḷ','x'),('ṅ','N'),('ñ','Y'),
   ('ṭ','w'),('ḍ','q'),('ṇ','R'),('ś','S'),('ṣ','z'),('ṃ','M'),('ḥ','H'),('ch','C'),('kh','K'),
   ('gh','G'),('jh','J'),('th','T'),('dh','D'),('ph','P'),('bh','B'),('ai','E'),('au','O')]
def i2s(s):
    s=s.lower().split('(')[0].split('/')[0].strip(); s=s.split()[0] if s.split() else s
    for a,b in sorted(M,key=lambda x:-len(x[0])): s=s.replace(a,b)
    return re.sub(r'[^A-Za-z]','',s)
def norm(s):
    s=''.join(c for c in unicodedata.normalize('NFD',s.lower()) if unicodedata.category(c)!='Mn')
    return re.sub(r'[^a-z]','',s.split('(')[0].split()[0]) if s.split() else ''
GLOSS=set()
for l in open(S+'slovar-grintsera-iz-ramayany-1-2.jsonl',encoding='utf-8'):
    m=re.search(r'\(([A-Za-zāīūṛṝḷṅñṭḍṇśṣṃḥ-]+)', json.loads(l).get('text',''))
    if m: GLOSS.add(norm(m.group(1)))
# Books I-III verses IN ORDER: (coord, token-set)
verses=[]
for f,rom in [('01_ramayana-balakanda','I'),('02_ramayana-ayodhyakanda','II'),('03_ramayana-aranyakanda','III')]:
    for l in open(S+f+'.jsonl',encoding='utf-8'):
        o=json.loads(l)
        if o.get('seg')!='sa': continue
        toks={re.sub(r'[^A-Za-z]','',w) for w in re.split(r'[ ।॥|]+',o.get('slp1',''))}
        verses.append((f"{rom}.{o.get('passage')}", toks))
def first_coord(slp):
    # proper inflected-form match: token startswith stem and not a longer compound (len<=stem+2)
    for coord,toks in verses:
        for t in toks:
            if t.startswith(slp) and len(t)<=len(slp)+1 and len(t)>=len(slp):
                return coord
    return None
F='data/sundara_commentary_to_add.json'
d=json.load(open(F,encoding='utf-8'))
def hasref(x):
    t=str(x.get('note_ru',''))+str(x.get('cross_ref',''))+str(x.get('source',''))
    return 'ринцер' in t or 'примеч. к I' in t or x.get('trigger')=='crossref' or str(x.get('cross_ref','')).strip()
applied=[]
for x in d:
    if 'shloka' not in x or x.get('type')!='В' or hasref(x): continue
    lem=str(x.get('lemma_iast','')); k=norm(lem); slp=i2s(lem)
    if k not in GLOSS or len(slp)<4 or slp in {'akza'}: continue
    coord=first_coord(slp)
    if not coord: continue
    x['cross_ref']=f"Рам. {coord} (Гринцер)"; x['cross_ref_method']="corpus_first_appearance"; x['review_required']=True
    nr=str(x.get('note_ru','')).rstrip();  nr=nr+('' if nr.endswith('.') else '.')
    x['note_ru']=nr+f" См. примеч. к {coord} (Гринцер; первое вхождение в кн. I–III, уточнить по примеч.)."
    applied.append((x.get('shloka'),lem,coord))
json.dump(d,open(F,'w',encoding='utf-8'),ensure_ascii=False,indent=2)
print(f"backfilled {len(applied)} Grintser cross-refs")
for s,l,c in applied: print(f"   {s:9} {l[:22]:22} -> Рам. {c}")

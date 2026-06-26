"""
Sundara ch.1 corpus enrichment pipeline.
Steps 0-3: provenance, relevance survey, per-verse candidates, aggregate stats.
Output files:
  data/sundara_ch1_corpus_relevance.json
  data/leonov_sundara_ch1_candidates.json
"""
import sys, os, json, re, collections, math
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

CORPUS_DIR = Path(r"C:\Users\user\Documents\GitHub\SamudraManthanam\web\corpus_builder\jsonl")
CS_DIR     = Path(r"C:\Users\user\Documents\GitHub\CommentaryStrategies")
SUNDARA    = CORPUS_DIR / "05_ramayana-sundarakanda.jsonl"
DATA_DIR   = CS_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

# ── helpers ──────────────────────────────────────────────────────────────────

def load_jsonl(path):
    """Load a JSONL file; skip malformed lines silently."""
    rows = []
    try:
        with open(path, encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    rows.append(json.loads(line))
                except json.JSONDecodeError:
                    pass
    except Exception as e:
        print(f"  WARN: cannot read {path}: {e}", file=sys.stderr)
    return rows

# SLP1 tokeniser — split on non-alphanumeric, keep tokens ≥3 chars
_TOKEN_RE = re.compile(r'[A-Za-z][A-Za-z]{2,}')

def slp1_tokens(text: str) -> list[str]:
    """Return lower-cased SLP1 word-tokens (≥3 chars)."""
    return _TOKEN_RE.findall(text.lower())

# Stop-set: ultra-common SLP1 words (function words, particles, copula etc.)
STOP_SLP1 = {
    'tat','tato','iva','ca','tu','iti','eva','api','hi','na','sa','te','tam',
    'sma','vai','vai','yat','kim','yad','tad','idam','asya','tasya','atra',
    'tatra','yatra','atra','puna','atha','tatah','tatas','tatHA','yathA',
    'atah','ata','sma','ha','svam','tat','tat','iti','yena','yasya',
    'asmin','tasmAt','yasmin','enam','etat','etad','ayam','imAn',
    'mahA','maha','para','param','tena','yena','cha','cha',
    # short noise
    'anu','upa','pra','sam','pari','nis','nir','dur','sus','abhi',
    'avi','ava','ati','adhi','aha','ima','ima',
}

def content_tokens(slp1: str) -> set[str]:
    toks = slp1_tokens(slp1)
    return {t for t in toks if t not in STOP_SLP1 and len(t) >= 3}

# ── STEP 0: #ru provenance ───────────────────────────────────────────────────
print("STEP 0 — #ru provenance")
# The HTML saved from samskrtam.ru states:
#   «Подстрочник подготовил М.В. Леонов»
# The JSONL #ru text is Leonov's own literal interlinear (подстрочник),
# NOT an independent translation — confirmed by matching the HTML parallel corpus.
# Attribution: М.В. Леонов, «Рамаяна. Книга 5. Сундараканда» (М.: Наука, 2022).
PROVENANCE = {
    "translator": "М.В. Леонов",
    "source": "Рамаяна. Книга 5. Сундараканда (М.: Наука, 2022)",
    "note": "Параллельный #ru-текст в корпусе samskrtam.ru — подстрочный перевод, "
            "подготовленный М.В. Леоновым. Он совпадает с буквальным слоем "
            "параллельного корпуса (не является независимым переводом). "
            "Сравнение «Леонов литературный» vs «Леонов подстрочник» — "
            "инструмент для выявления переводческих трансформаций (тип Б по Казанскому).",
    "status": "resolved"
}
print(f"  #ru translator: {PROVENANCE['translator']}")

# ── Load Sundara ch.1 ────────────────────────────────────────────────────────
print("Loading Sundara ch.1 …")
sundara_rows = load_jsonl(SUNDARA)
ch1_sa = [r for r in sundara_rows if r.get('chapter') == '1' and r.get('seg') == 'sa']
ch1_ru = {r['passage']: r for r in sundara_rows if r.get('chapter') == '1' and r.get('seg') == 'ru'}
print(f"  ch.1 Sanskrit verses: {len(ch1_sa)}")

# Build SLP1 token set for ch.1 content words
ch1_content: set[str] = set()
ch1_verse_tokens: dict[str, set[str]] = {}  # passage → token set
for r in ch1_sa:
    slp = r.get('slp1', '') or r.get('text', '')
    toks = content_tokens(slp)
    ch1_verse_tokens[r['passage']] = toks
    ch1_content.update(toks)
print(f"  ch.1 content SLP1 stems: {len(ch1_content)}")

# ── STEP 1: Build I–III + Grintser index, then survey all 148 ───────────────
print("\nSTEP 1 — Corpus-relevance survey")

# Priority files: Ramayana I–III + Grintser glossary (Grintser cross-ref base)
GRINTSER_FILES = [
    "01_ramayana-balakanda.jsonl",
    "02_ramayana-ayodhyakanda.jsonl",
    "03_ramayana-aranyakanda.jsonl",
    "slovar-grintsera-iz-ramayany-1-2.jsonl",
]

# Build lemma→[address] index for Books I–III + Grintser
print("  Building I–III + Grintser lemma index …")
grintser_index: dict[str, list[str]] = collections.defaultdict(list)
for fname in GRINTSER_FILES:
    fpath = CORPUS_DIR / fname
    rows = load_jsonl(fpath)
    sa_rows = [r for r in rows if r.get('seg') == 'sa' or r.get('lang') == 'sa'
               or (r.get('seg') is None and r.get('slp1'))]
    # for glossaries, all rows may be relevant
    if not sa_rows:
        sa_rows = rows
    for r in sa_rows:
        slp = r.get('slp1', '') or r.get('text', '')
        passage = r.get('passage', r.get('id', ''))
        addr = f"{fname.replace('.jsonl','')}:{passage}"
        for tok in content_tokens(slp):
            if tok in ch1_content:
                grintser_index[tok].append(addr)
# Deduplicate per token (keep up to 3 examples)
for tok in grintser_index:
    grintser_index[tok] = list(dict.fromkeys(grintser_index[tok]))[:3]

print(f"  Grintser-index tokens matching ch.1: {len(grintser_index)}")

# Survey ALL 148 works
print("  Surveying all 148 works …")
all_jsonl = sorted(CORPUS_DIR.glob("*.jsonl"))
relevance_results = []

for fpath in all_jsonl:
    fname = fpath.name
    if fname == "05_ramayana-sundarakanda.jsonl":
        continue  # skip self
    rows = load_jsonl(fpath)
    # collect all sa-side tokens (or all tokens for glossaries)
    sa_rows = [r for r in rows if r.get('seg') == 'sa' or r.get('lang') == 'sa']
    if not sa_rows:
        sa_rows = rows

    work_tokens: set[str] = set()
    passage_index: dict[str, set[str]] = collections.defaultdict(set)
    for r in sa_rows:
        slp = r.get('slp1', '') or r.get('text', '')
        passage = r.get('passage', r.get('id', ''))
        toks = content_tokens(slp)
        work_tokens.update(toks)
        for t in toks:
            if t in ch1_content:
                passage_index[t].add(passage)

    shared = ch1_content & work_tokens
    n_shared = len(shared)
    if n_shared == 0:
        continue

    # Collect example verses: for each shared token find a ch.1 verse that has it
    examples = []
    # pick tokens that appear in fewest ch.1 verses (rarer = more interesting)
    token_freq = {t: len([v for v,ts in ch1_verse_tokens.items() if t in ts]) for t in shared}
    rare_shared = sorted(shared, key=lambda t: token_freq.get(t, 999))[:5]
    for tok in rare_shared:
        ch1_vv = [v for v,ts in ch1_verse_tokens.items() if tok in ts]
        other_vv = list(passage_index.get(tok, set()))[:2]
        if ch1_vv and other_vv:
            examples.append({
                "stem": tok,
                "ch1_verse": ch1_vv[0],
                "other_verses": other_vv[:2]
            })
        if len(examples) >= 3:
            break

    # Classify work type
    if 'rigveda' in fname or 'atharvaveda' in fname:
        work_type = 'vedic'
    elif 'mahabharata' in fname or 'adiparva' in fname:
        work_type = 'mahabharata'
    elif 'ramayana' in fname:
        work_type = 'ramayana'
    elif 'bhagavadgita' in fname or 'gita' in fname.lower():
        work_type = 'gita'
    elif fname.endswith('-up.jsonl') or 'up.jsonl' in fname:
        work_type = 'upanishad'
    elif 'slovar' in fname or 'dic_' in fname or 'kewa' in fname or 'warnemyr' in fname:
        work_type = 'lexicon'
    elif 'purana' in fname or 'vishnu' in fname:
        work_type = 'purana'
    elif 'yoga' in fname or 'sankhya' in fname or 'nyaya' in fname:
        work_type = 'philosophy'
    else:
        work_type = 'other'

    relevance_results.append({
        "file": fname,
        "work_type": work_type,
        "shared_stems": n_shared,
        "total_work_tokens": len(work_tokens),
        "ch1_content_size": len(ch1_content),
        "overlap_pct": round(100 * n_shared / len(ch1_content), 1),
        "examples": examples
    })

# Sort by shared stems descending
relevance_results.sort(key=lambda x: x['shared_stems'], reverse=True)
print(f"  Works with shared stems: {len(relevance_results)}")
print(f"  Top-10:")
for r in relevance_results[:10]:
    print(f"    {r['file']:50s}  shared={r['shared_stems']:4d}  ({r['overlap_pct']}%)")

# Save relevance JSON
rel_out = {
    "meta": {
        "description": "Relevance of 148 corpus works to Sundara-kāṇḍa ch.1 content stems",
        "ch1_content_stems": len(ch1_content),
        "ch1_verses": len(ch1_sa),
        "generated": "2026-06-26",
        "note": "Stem-overlap counting only (SLP1 3-gram+). Evidence is verse-level (soft). "
                "All candidates require editorial review."
    },
    "provenance": PROVENANCE,
    "grintser_index_tokens": len(grintser_index),
    "results": relevance_results
}
rel_path = DATA_DIR / "sundara_ch1_corpus_relevance.json"
with open(rel_path, 'w', encoding='utf-8') as f:
    json.dump(rel_out, f, ensure_ascii=False, indent=2)
print(f"\nSaved: {rel_path}")

# ── STEP 2: Per-verse candidate generation ───────────────────────────────────
print("\nSTEP 2 — Per-verse candidate generation")

# Load existing Leonov markup (the 50 golden notes for ch.1)
markup_path = DATA_DIR / "leonov_markup_50.json"
leonov_markup: list[dict] = []
if markup_path.exists():
    with open(markup_path, encoding='utf-8') as f:
        leonov_markup = json.load(f)
# Index existing notes by passage
existing_by_passage: dict[str, list[dict]] = collections.defaultdict(list)
for note in leonov_markup:
    # shloka_addr like "Rām. Sundara 5.1.1" → extract "1.1"
    m = re.search(r'5\.(\d+\.\d+)', note.get('shloka_addr',''))
    if m:
        existing_by_passage[m.group(1)].append(note)

# Load ramayana epithets JSON
epithet_path = DATA_DIR / "ramayana_epithets.json"
epithets_db: dict = {}
if epithet_path.exists():
    with open(epithet_path, encoding='utf-8') as f:
        epithets_db = json.load(f)
    # could be list or dict
    if isinstance(epithets_db, list):
        # index by key/name field
        epithets_db = {e.get('name','') or e.get('term','') or str(i): e
                       for i, e in enumerate(epithets_db)}

# Load formulas md file — extract epithet names and their first shloka refs
formulas_path = CS_DIR / "ramayana-leonov" / "ramayana-formulas_1-2.md"
formula_index: dict[str, str] = {}  # epithet_name → first_shloka ref
if formulas_path.exists():
    formula_text = formulas_path.read_text(encoding='utf-8')
    # Lines like: **Хануман** — (epithets...)  or standalone lines
    # Extract **Name** entries
    for m in re.finditer(r'\*\*([^*]+)\*\*\s*[—-]\s*([^\n]+)', formula_text):
        name = m.group(1).strip()
        val  = m.group(2).strip()
        # Look for IAST terms
        iast_m = re.search(r'([a-zāīūṛḷṃḥṅñṭḍṇśṣ]{3,})', val)
        formula_index[name.lower()] = iast_m.group(1) if iast_m else val[:40]

# Key epithets/names in ch.1 (known from the golden markup)
KEY_EPITHETS_SLP1 = {
    # Hanuman epithets
    'SatrukarSana': ('śatrukarśana', 'Губитель врагов'),
    'mahAbala': ('mahābala', 'Обладающий великой силой'),
    'DIra': ('dhīra', 'Стойкий'),
    'DImat': ('dhīmān', 'Мудрый'),
    'kAmarUpa': ('kāmarūpa', 'Принимающий любой облик'),
    'kapivara': ('kapivara', 'Лучший из обезьян'),
    'plavaGapravara': ('plavaṃgapravara', 'Лучший из прыгунов'),
    'vAnarazrezWa': ('vānaraśreṣṭha', 'Лучший из ванаров'),
    'kapikuYjara': ('kapikuñjara', 'Слон среди обезьян'),
    'mAruti': ('māruti', 'Марути'),
    'mArutAtmaja': ('mārutātmaja', 'Сын бога ветра'),
    'vAyuputra': ('vāyuputra', 'Сын Ваю'),
    'mahAkAya': ('mahākāya', 'Огромный'),
    # Sita epithets
    'janakAtmajA': ('janakātmajā', 'Дочь Джанаки'),
    'vEdehI': ('vaidehī', 'Вайдехи'),
    'mEtalI': ('maithilī', 'Майтхили'),
    # Rama epithets
    'rAGava': ('rāghava', 'Потомок Рагху'),
    'dASaraTi': ('dāśarathi', 'Сын Дашаратхи'),
    # Ravana
    'rAvaNa': ('rāvaṇa', 'Равана'),
    # Beings
    'cAraRa': ('cāraṇa', 'Чаран'),
    'vAnara': ('vānara', 'Ванара'),
    'nAga': ('nāga', 'Наг/слон'),
    # Mountains/geography
    'mEnAka': ('maināka', 'Майнака'),
    'surAsA': ('surasā', 'Сурасса'),
    'siMhikA': ('siṃhikā', 'Симхика'),
    # Minerals/flora
    'vEdUrya': ('vaidūrya', 'Вайдурья (минерал)'),
    'SAdvala': ('śādvala', 'Луг'),
}

# Colour classification rules
def classify_fill(note: dict, verse_tokens: set, is_first_occurrence: bool) -> str:
    topic = note.get('axis_1_topic', [])
    if isinstance(topic, str):
        topic = [topic]
    if 'sanskrit_term' in topic and is_first_occurrence:
        return 'yellow'
    if any(t in topic for t in ['geography', 'realia']) and is_first_occurrence:
        return 'green'  # flora/fauna/geography first appearance
    if 'reference' in topic:
        return 'blue'
    if any(t in topic for t in ['poetics']) or note.get('axis_2_kazansky') == 'G':
        return 'orange'  # formula/epithet
    return 'none'

# Track first occurrences of IAST terms
seen_terms: set[str] = set()

# Generate candidates
candidates = []
comment_counter = 0

# Seen epithets for formula tracking
first_formula: dict[str, str] = {}  # iast_term → verse address

for r in ch1_sa:
    passage = r['passage']
    sa_text = r.get('text', '')
    slp1_text = r.get('slp1', '') or ''
    verse_toks = ch1_verse_tokens.get(passage, set())
    ru_r = ch1_ru.get(passage)
    ru_text = ru_r['text'] if ru_r else ''

    # Check existing markup for this passage
    existing = existing_by_passage.get(passage, [])

    # ── A: Epithet/formula candidates ──────────────────────────────────────
    for slp_key, (iast_form, ru_gloss) in KEY_EPITHETS_SLP1.items():
        slp_lower = slp_key.lower()
        if slp_lower not in slp1_text.lower():
            continue
        is_first = iast_form not in seen_terms
        if is_first:
            seen_terms.add(iast_form)

        # Check if already covered by existing markup
        already = any(iast_form in (n.get('raw_text','')) for n in existing)
        if already:
            continue

        # Find Grintser cross-refs (Books I–III)
        grintser_refs = grintser_index.get(slp_lower, [])

        # Build provenance from top corpus hits
        prov_works = []
        for rel in relevance_results[:20]:
            wf = rel['file']
            for ex in rel.get('examples', []):
                if ex['stem'] == slp_lower:
                    prov_works.append({
                        "work": wf,
                        "verses": ex['other_verses']
                    })
                    break

        # Determine fill color
        if is_first and iast_form not in first_formula:
            first_formula[iast_form] = passage
            fill = 'orange'  # first appearance of formula/epithet
        elif grintser_refs:
            fill = 'blue'  # Grintser cross-ref
        elif is_first:
            fill = 'yellow'  # first appearance of term
        else:
            fill = 'none'

        comment_counter += 1
        comment_id = f"ram/leonov/candidate_5.{passage}.ep{comment_counter}"

        # Compose candidate text
        if grintser_refs:
            ref_str = f" Ср. {grintser_refs[0]}."
        else:
            ref_str = ""

        if is_first:
            raw = (f"{ru_gloss} ({iast_form}) — первое вхождение эпитета в гл. 1.{ref_str} "
                   f"[Корпус: {prov_works[0]['work'] if prov_works else 'нет данных'}]")
        else:
            raw = (f"{ru_gloss} ({iast_form}).{ref_str} "
                   f"[Корпус: {prov_works[0]['work'] if prov_works else 'нет данных'}]")

        cand = {
            "comment_id": comment_id,
            "urn": f"urn:cts:sanskritLit:ramayana:5.{passage}",
            "shloka_addr": f"Rām. Sundara 5.{passage}",
            "translator": "leonov",
            "editor": "kostina",
            "raw_text": raw,
            "char_count": len(raw),
            "has_iast": True,
            "axis_1_topic": ["sanskrit_term"],
            "axis_2_kazansky": "A" if is_first else "G",
            "axis_3_lakshana": ["L2"],
            "axis_4_paribok": "P",
            "cited_indian_commentators": [],
            "cited_western_sources": [],
            # Extended fields
            "fill_color": fill,
            "candidate": True,
            "review_required": True,
            "evidence_type": "verse-level (soft)",
            "provenance": {
                "iast_form": iast_form,
                "slp1_stem": slp_lower,
                "first_occurrence": is_first,
                "grintser_cross_refs": grintser_refs,
                "corpus_parallels": prov_works[:3]
            }
        }
        candidates.append(cand)

    # ── B: Parallel #ru divergence candidates (Kostina-style «Опущено») ───
    # Compare literal substrings from slp1 that appear in ru_text
    # Simple heuristic: find IAST words in sa_text not reflected in ru_text
    # We look for key Sanskrit terms present in sa_text but absent from ru
    if ru_text:
        for slp_key, (iast_form, ru_gloss) in KEY_EPITHETS_SLP1.items():
            if slp_key.lower() not in slp1_text.lower():
                continue
            # Check if the Russian gloss or a close equivalent is in ru_text
            # Simple: look for the first 4 chars of ru_gloss
            short = ru_gloss[:5].lower()
            if short not in ru_text.lower() and len(ru_text) > 0:
                # Potential omission
                already = any(iast_form in (n.get('raw_text','')) and 'Опущено' in n.get('raw_text','')
                              for n in existing)
                if already:
                    continue
                comment_counter += 1
                raw2 = (f"{ru_gloss} ({iast_form}). [Е. Костина — кандидат]: «{iast_form}» "
                        f"возможно опущено в подстрочнике Леонова. "
                        f"Подстрочник: «{ru_text[:80]}…». Требует проверки.")
                cand2 = {
                    "comment_id": f"ram/leonov/candidate_5.{passage}.om{comment_counter}",
                    "urn": f"urn:cts:sanskritLit:ramayana:5.{passage}",
                    "shloka_addr": f"Rām. Sundara 5.{passage}",
                    "translator": "leonov",
                    "editor": "kostina",
                    "raw_text": raw2,
                    "char_count": len(raw2),
                    "has_iast": True,
                    "axis_1_topic": ["textology"],
                    "axis_2_kazansky": "B",
                    "axis_3_lakshana": ["L1"],
                    "axis_4_paribok": "P",
                    "cited_indian_commentators": [],
                    "cited_western_sources": [],
                    "fill_color": "none",
                    "candidate": True,
                    "review_required": True,
                    "evidence_type": "parallel-text divergence (soft)",
                    "provenance": {
                        "iast_form": iast_form,
                        "slp1_stem": slp_key.lower(),
                        "parallel_ru_text": ru_text[:120],
                        "divergence_type": "potential_omission"
                    }
                }
                candidates.append(cand2)

    # ── C: Intertextual cross-refs from top corpus works ──────────────────
    # For every rare ch.1 token that appears in a non-Ramayana work, flag once
    for rel in relevance_results[:15]:
        if rel['work_type'] in ('ramayana',):
            continue  # skip same-epic; already handled by Grintser index
        for ex in rel.get('examples', []):
            tok = ex['stem']
            if tok not in verse_toks:
                continue
            # Only generate one intertextual note per verse per work
            already_gen = any(
                c.get('provenance', {}).get('slp1_stem') == tok
                and rel['file'] in str(c.get('provenance', {}))
                for c in candidates
                if c['shloka_addr'] == f"Rām. Sundara 5.{passage}"
            )
            if already_gen:
                continue
            comment_counter += 1
            work_label = rel['file'].replace('.jsonl','').replace('_',' ')
            other_vv = ", ".join(ex.get('other_verses', [])[:2])
            raw3 = (f"Стебель «{tok}» (SLP1) присутствует также в «{work_label}» "
                    f"(ср. {other_vv}). Возможная межтекстовая параллель — "
                    f"требует проверки редактором. [Доказательство: уровень шлоки, мягкое]")
            cand3 = {
                "comment_id": f"ram/leonov/candidate_5.{passage}.ix{comment_counter}",
                "urn": f"urn:cts:sanskritLit:ramayana:5.{passage}",
                "shloka_addr": f"Rām. Sundara 5.{passage}",
                "translator": "leonov",
                "editor": "kostina",
                "raw_text": raw3,
                "char_count": len(raw3),
                "has_iast": False,
                "axis_1_topic": ["reference"],
                "axis_2_kazansky": "G",
                "axis_3_lakshana": [],
                "axis_4_paribok": "P",
                "cited_indian_commentators": [],
                "cited_western_sources": [],
                "fill_color": "blue",
                "candidate": True,
                "review_required": True,
                "evidence_type": "verse-level stem overlap (soft)",
                "provenance": {
                    "slp1_stem": tok,
                    "corpus_work": rel['file'],
                    "other_verses": ex.get('other_verses', []),
                    "ch1_verse": passage
                }
            }
            candidates.append(cand3)
            break  # one intertextual note per work per verse

print(f"  Generated {len(candidates)} candidate annotations")

# Color distribution
color_counts = collections.Counter(c['fill_color'] for c in candidates)
print(f"  Color distribution: {dict(color_counts)}")

# Save candidates
cand_path = DATA_DIR / "leonov_sundara_ch1_candidates.json"
with open(cand_path, 'w', encoding='utf-8') as f:
    json.dump(candidates, f, ensure_ascii=False, indent=2)
print(f"Saved: {cand_path}")

# ── STEP 3: Aggregate real numbers ──────────────────────────────────────────
print("\nSTEP 3 — Aggregate stats")

# From existing golden markup (leonov_markup_50)
ch1_existing = [n for n in leonov_markup
                if re.search(r'5\.1\.', n.get('shloka_addr',''))]
ch1_existing_count = len(ch1_existing)
ch1_existing_chars = [n['char_count'] for n in ch1_existing]
ch1_mean_len = round(sum(ch1_existing_chars)/len(ch1_existing_chars), 0) if ch1_existing_chars else 0
ch1_iast_count = sum(1 for n in ch1_existing if n.get('has_iast'))
ch1_iast_pct = round(100*ch1_iast_count/ch1_existing_count, 0) if ch1_existing_count else 0

# Topic distribution
topic_counter = collections.Counter()
for n in ch1_existing:
    for t in (n.get('axis_1_topic') or []):
        topic_counter[t] += 1

# Kostina «Опущено» count
kostina_omit = [n for n in ch1_existing if 'Опущено' in n.get('raw_text','')]

# Candidate stats
cand_color_dist = dict(color_counts)

stats = {
    "ch1_verses": len(ch1_sa),
    "existing_notes_in_markup_50": ch1_existing_count,
    "existing_notes_mean_len_chars": ch1_mean_len,
    "existing_notes_iast_pct": ch1_iast_pct,
    "existing_kostina_omissions": len(kostina_omit),
    "existing_topic_distribution": dict(topic_counter),
    "candidate_notes_generated": len(candidates),
    "candidate_color_distribution": cand_color_dist,
    "corpus_works_with_shared_stems": len(relevance_results),
    "grintser_index_tokens": len(grintser_index),
    "top_10_enriching_works": [
        {"file": r['file'], "shared_stems": r['shared_stems'],
         "work_type": r['work_type'], "overlap_pct": r['overlap_pct']}
        for r in relevance_results[:10]
    ]
}

stats_path = DATA_DIR / "sundara_ch1_stats.json"
with open(stats_path, 'w', encoding='utf-8') as f:
    json.dump(stats, f, ensure_ascii=False, indent=2)
print(f"Saved: {stats_path}")
print("\nKey stats:")
for k, v in stats.items():
    if not isinstance(v, (list, dict)):
        print(f"  {k}: {v}")

print("\n✓ Pipeline complete — Steps 0–3 done.")
print(f"  Deliverables:")
print(f"    {rel_path}")
print(f"    {cand_path}")
print(f"    {stats_path}")

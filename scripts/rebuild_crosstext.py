#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Idempotent full rebuild: BASE + deduped CROSS -> commentary, stats, ledger, rationale.

Safe to run repeatedly. Reads sources fresh each time; full rewrite (no append).
"""
import json, sys, glob, os, re
from collections import Counter, defaultdict, OrderedDict

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, 'data')
CT = os.path.join(DATA, 'crosstext')

def load(p):
    with open(p, encoding='utf-8') as f:
        return json.load(f)

def dump(p, obj):
    # utf-8 NO BOM
    with open(p, 'w', encoding='utf-8') as f:
        json.dump(obj, f, ensure_ascii=False, indent=1)
        f.write('\n')

# ---------------------------------------------------------------------------
# 1. BASE notes (subtype != cross_text) from current commentary file
# ---------------------------------------------------------------------------
COMM = os.path.join(DATA, 'sundara_commentary_to_add.json')
comm = load(COMM)
meta_entry = next((x for x in comm if isinstance(x, dict) and '_meta' in x), None)
all_notes = [x for x in comm if isinstance(x, dict) and '_meta' not in x]
base = [x for x in all_notes if x.get('subtype') != 'cross_text']
# Ensure base notes carry subtype 'base' explicitly (idempotent normalisation)
for b in base:
    if b.get('subtype') is None:
        b['subtype'] = 'base'
print(f'BASE notes: {len(base)}')

# ---------------------------------------------------------------------------
# 2. CROSS candidates: every verified note across crosstext/*.json
#    (ignore *.rejected.json). gita + mbh_gnomic treated as confirmed.
# ---------------------------------------------------------------------------
CONFIRMED_NO_FLAG = {'gita', 'mbh_gnomic', 'ramayana_grintser'}  # merged earlier, lack verified flag
# ramayana_grintser added 2026-07-02 (PR #42 reconciliation): main's 22-entry file is a
# non-underscore "confirmed" file by the same naming convention as every other category,
# but never carries the verified flag (unlike main's own dharmashastra/kavya/mbh_narrative,
# which are 100% flagged) -- an oversight in whichever pass wrote that one file, not a
# deliberate unconfirmed marker.
cluster_meta = {}   # cluster -> _meta dict
cross_candidates = []  # accepted-into-merge candidates (verified or confirmed)

def chapter_of(shloka):
    # shloka like "V.20.5" -> 20
    m = re.match(r'V\.(\d+)\.', str(shloka))
    return int(m.group(1)) if m else None

for f in sorted(glob.glob(os.path.join(CT, '*.json'))):
    if f.endswith('.rejected.json'):
        continue
    d = load(f)
    m = next((x['_meta'] for x in d if isinstance(x, dict) and '_meta' in x), {})
    notes = [x for x in d if isinstance(x, dict) and '_meta' not in x]
    cl = m.get('cluster') or (notes[0].get('cluster') if notes else None)
    cluster_meta[cl] = m
    for n in notes:
        ncl = n.get('cluster', cl)
        is_conf = (n.get('verified') is True) or (ncl in CONFIRMED_NO_FLAG)
        if not is_conf:
            # any non-verified, non-confirmed note is skipped from merge
            continue
        n = dict(n)
        n['subtype'] = 'cross_text'
        n.setdefault('trigger', 'crosstext')
        n.setdefault('review_required', True)
        cross_candidates.append(n)

print(f'CROSS candidates (verified/confirmed): {len(cross_candidates)}')

# ---------------------------------------------------------------------------
# 3. DEDUP by (shloka, lemma_iast, source). Identical -> keep one.
#    Same shloka+lemma from DIFFERENT works -> keep both, cross-link via 'also'.
# ---------------------------------------------------------------------------
def norm(s):
    return (str(s) if s is not None else '').strip()

# exact-triple dedup
seen_triple = {}
deduped = []
dup_dropped = []  # exact (shloka,lemma,source) duplicates removed
for n in cross_candidates:
    key = (norm(n.get('shloka')), norm(n.get('lemma_iast')), norm(n.get('source')))
    if key in seen_triple:
        dup_dropped.append(n)
        continue
    seen_triple[key] = n
    deduped.append(n)

print(f'After exact-triple dedup: {len(deduped)} (dropped {len(dup_dropped)})')

# cross-link same shloka+lemma across DIFFERENT works via 'also'
by_pair = defaultdict(list)
for n in deduped:
    by_pair[(norm(n.get('shloka')), norm(n.get('lemma_iast')))].append(n)

for pair, group in by_pair.items():
    if len(group) < 2:
        continue
    for n in group:
        also = []
        for other in group:
            if other is n:
                continue
            also.append({
                'cluster': other.get('cluster'),
                'source': other.get('source'),
                'parallel_addr': other.get('parallel_addr'),
            })
        # merge with any pre-existing 'also' authored in source data, dedup by source
        existing = n.get('also') or []
        merged = []
        seen_src = set()
        for a in (existing + also):
            s = norm(a.get('source'))
            if s in seen_src:
                continue
            seen_src.add(s)
            merged.append(a)
        if merged:
            n['also'] = merged

cross_final = deduped
print(f'CROSS final (merged): {len(cross_final)}')

# ---------------------------------------------------------------------------
# 4. WRITE commentary fresh = BASE + deduped CROSS
# ---------------------------------------------------------------------------
cluster_counts = Counter(n.get('cluster') for n in cross_final)
merged_total = len(base) + len(cross_final)

# rebuild _meta
new_meta = dict(meta_entry['_meta']) if meta_entry else {}
# per-chapter note counts (base+cross)
all_final_notes = base + cross_final
per_chapter = Counter()
noted_verses = defaultdict(set)
for n in all_final_notes:
    ch = chapter_of(n.get('shloka'))
    if ch is not None:
        per_chapter[ch] += 1
        noted_verses[ch].add(norm(n.get('shloka')))

chapter_verse_counts = new_meta.get('chapter_verse_counts', {})
total_verses = new_meta.get('total_verses', sum(int(v) for v in chapter_verse_counts.values()))
verses_with_note = len(set(norm(n.get('shloka')) for n in all_final_notes))

new_meta.update({
    'generated': '2026-06-27',
    'total_notes': merged_total,
    'verses_with_note': verses_with_note,
    'verses_without_note': total_verses - verses_with_note,
    'by_type': dict(Counter(n.get('type') for n in all_final_notes if n.get('type'))),
    'by_trigger': dict(Counter(n.get('trigger') for n in all_final_notes if n.get('trigger'))),
    'by_priority': dict(Counter(n.get('priority') for n in all_final_notes if n.get('priority'))),
    'per_chapter_notes': {str(c): per_chapter.get(c, 0) for c in sorted(chapter_verse_counts.keys(), key=lambda x: int(x))} if chapter_verse_counts else {str(c): per_chapter[c] for c in sorted(per_chapter)},
    'by_subtype': {'base': len(base), 'cross_text': len(cross_final)},
    'cross_text_total': len(cross_final),
    'cross_text_by_cluster': dict(cluster_counts),
    'crosstext_expansion': 'book-wide multi-perspective cross-text run recovered from data/crosstext/*.json (all 6 verified/confirmed works: dharmashastra, gita, kavya, mbh_gnomic, mbh_narrative, ramayana_grintser). Idempotent full rebuild.',
})
out_comm = [{'_meta': new_meta}] + base + cross_final
dump(COMM, out_comm)
print(f'WROTE commentary: {merged_total} notes')

# ---------------------------------------------------------------------------
# Cluster display labels (prompt grouping) -> ordered
# ---------------------------------------------------------------------------
CLUSTER_LABELS = OrderedDict([
    ('dharmashastra', 'Ману'),
    ('mbh_narrative', 'МБх-нарратив'),
    ('ramayana_grintser', 'Гринцер'),
    ('gita', 'Гита'),
    ('mbh_gnomic', 'Шанти'),
    ('kavya', 'кавья'),
])
CLUSTER_FULL = {cl: (cluster_meta.get(cl, {}).get('cluster_label') or lbl)
                for cl, lbl in CLUSTER_LABELS.items()}

# ---------------------------------------------------------------------------
# 5. REBUILD decision ledger: keep base entries, rebuild cross_text entries
#    from all 6 sources (accepted) + 4 rejected files (rejected-with-reason).
# ---------------------------------------------------------------------------
LEDGER = os.path.join(DATA, 'sundara_decision_ledger.json')
ledger = load(LEDGER)
old_entries = ledger['entries']
base_entries = [e for e in old_entries if e.get('subtype') != 'cross_text']
# base accepted should equal len(base); base rejected preserved as-is
base_accepted = [e for e in base_entries if e.get('decision') == 'accepted']
base_rejected = [e for e in base_entries if e.get('decision') == 'rejected']
print(f'Ledger base entries: {len(base_entries)} (acc {len(base_accepted)}, rej {len(base_rejected)})')

# build cross_text accepted entries from cross_final
ct_accept_entries = []
for n in cross_final:
    ct_accept_entries.append({
        'shloka': n.get('shloka'),
        'lemma_iast': n.get('lemma_iast'),
        'trigger': 'crosstext',
        'subtype': 'cross_text',
        'cluster': n.get('cluster'),
        'source': n.get('source'),
        'decision': 'accepted',
        'reason': 'accepted_cross_text',
        'chapter': chapter_of(n.get('shloka')),
    })

# exact-triple duplicates dropped during merge -> ledger rejected_duplicate
ct_dup_entries = []
for n in dup_dropped:
    ct_dup_entries.append({
        'shloka': n.get('shloka'),
        'lemma_iast': n.get('lemma_iast'),
        'trigger': 'crosstext',
        'subtype': 'cross_text',
        'cluster': n.get('cluster'),
        'source': n.get('source'),
        'decision': 'rejected',
        'reason': 'rejected_duplicate',
        'reject_detail': 'exact (shloka, lemma_iast, source) duplicate of an already-accepted cross-text note',
        'chapter': chapter_of(n.get('shloka')),
    })

# rejected files -> rejected-with-reason entries
ct_reject_entries = []
rejected_by_cluster = Counter()
for f in sorted(glob.glob(os.path.join(CT, '*.rejected.json'))):
    d = load(f)
    notes = [x for x in d if isinstance(x, dict) and '_meta' not in x]
    for n in notes:
        cl = n.get('cluster')
        rejected_by_cluster[cl] += 1
        ct_reject_entries.append({
            'shloka': n.get('shloka'),
            'lemma_iast': n.get('lemma_iast'),
            'trigger': 'crosstext',
            'subtype': 'cross_text',
            'cluster': cl,
            'source': n.get('source'),
            'decision': 'rejected',
            'reason': 'rejected_crosstext_trivial',
            'reject_detail': n.get('reject_reason') or n.get('reason'),
            'chapter': chapter_of(n.get('shloka')),
        })

ct_entries = ct_accept_entries + ct_dup_entries + ct_reject_entries
print(f'Ledger cross_text entries: acc {len(ct_accept_entries)}, dup {len(ct_dup_entries)}, rej-file {len(ct_reject_entries)}')

new_entries = base_entries + ct_entries
total_candidates = len(new_entries)
accepted_total = sum(1 for e in new_entries if e['decision'] == 'accepted')
rejected_total = sum(1 for e in new_entries if e['decision'] == 'rejected')

# accepted must equal final note count
assert accepted_total == merged_total, f'accepted {accepted_total} != notes {merged_total}'

# accepted-by-bucket
acc_buckets = Counter(e['reason'] for e in new_entries if e['decision'] == 'accepted')
rej_buckets = Counter(e['reason'] for e in new_entries if e['decision'] == 'rejected')

# per-work contribution map
per_work = OrderedDict()
for cl, lbl in CLUSTER_LABELS.items():
    m = cluster_meta.get(cl, {})
    conf = sum(1 for n in cross_final if n.get('cluster') == cl)
    rej = rejected_by_cluster.get(cl, 0)
    dup = sum(1 for n in dup_dropped if n.get('cluster') == cl)
    stems = sorted(set(n.get('stem') for n in cross_final if n.get('cluster') == cl and n.get('stem')))
    example_loci = []
    for n in cross_final:
        if n.get('cluster') == cl and len(example_loci) < 4:
            example_loci.append(f"{n.get('shloka')} -> {n.get('parallel_addr')}")
    per_work[cl] = {
        'cluster': cl,
        'label': CLUSTER_FULL[cl],
        'short_label': lbl,
        'source_files': m.get('source_files') or m.get('source_corpus'),
        'stems_overlapped': len(stems),
        'stem_list': stems,
        'candidates': conf + rej + dup,
        'notes_confirmed': conf,
        'rejected_as_trivial': rej,
        'rejected_as_duplicate': dup,
        'example_loci': example_loci,
    }

new_ledger_meta = dict(ledger['meta'])
new_ledger_meta.update({
    'generated': '2026-06-27',
    'total_candidates': total_candidates,
    'accepted': accepted_total,
    'rejected': rejected_total,
    'accepted_by_bucket': dict(acc_buckets),
    'rejected_by_bucket': dict(rej_buckets),
    'note': f'Rebuilt 2026-06-27 (idempotent): accepted == note count in sundara_commentary_to_add.json ({merged_total}). Cross-text from all 6 verified/confirmed works in data/crosstext/*.json; rejected-with-reason from *.rejected.json. per_work_cross_text_map covers all 6 works.',
})
# extend reason glossary
new_ledger_meta.setdefault('reason_glossary', {})
new_ledger_meta['reason_glossary']['rejected_crosstext_trivial'] = 'отклонено — межтекстовый кандидат: тривиальное/фабрикованное/мисатрибутированное пересечение (см. reject_detail)'

new_ledger = OrderedDict()
new_ledger['meta'] = new_ledger_meta
new_ledger['per_work_cross_text_map'] = per_work
new_ledger['entries'] = new_entries
dump(LEDGER, new_ledger)
print(f'WROTE ledger: cand {total_candidates}, acc {accepted_total}, rej {rejected_total}')

# ---------------------------------------------------------------------------
# Regenerate book stats
# ---------------------------------------------------------------------------
STATS = os.path.join(DATA, 'sundara_book_stats.json')
verses_noted_per_ch = {}
for c in sorted(chapter_verse_counts.keys(), key=lambda x: int(x)) if chapter_verse_counts else sorted(per_chapter):
    ci = int(c)
    vc = int(chapter_verse_counts.get(str(c), 0)) if chapter_verse_counts else 0
    noted = len(noted_verses.get(ci, set()))
    verses_noted_per_ch[str(c)] = {
        'verses': vc,
        'verses_noted': noted,
        'verses_unnoted': vc - noted,
        'notes': per_chapter.get(ci, 0),
    }

stats = OrderedDict()
stats['_meta'] = {
    'description': 'Агрегированная статистика примечаний по всей кн. V (гл. 1–68)',
    'generated': '2026-06-27',
    'source': 'sundara_commentary_to_add.json (idempotent rebuild)',
}
stats['total_verses'] = total_verses
stats['total_notes'] = merged_total
stats['verses_with_note'] = verses_with_note
stats['verses_without_note'] = total_verses - verses_with_note
stats['by_type'] = dict(Counter(n.get('type') for n in all_final_notes if n.get('type')))
stats['by_trigger'] = dict(Counter(n.get('trigger') for n in all_final_notes if n.get('trigger')))
stats['by_subtype'] = {'base': len(base), 'cross_text': len(cross_final)}
stats['by_priority'] = dict(Counter(n.get('priority') for n in all_final_notes if n.get('priority')))
stats['cross_text_by_cluster'] = dict(cluster_counts)
stats['per_chapter'] = verses_noted_per_ch
dump(STATS, stats)
print(f'WROTE stats')

# emit machine-readable summary for the orchestrator
summary = {
    'base_count': len(base),
    'cross_text_count': len(cross_final),
    'merged_total': merged_total,
    'ledger_total_candidates': total_candidates,
    'ledger_accepted': accepted_total,
    'ledger_rejected': rejected_total,
    'by_cluster': dict(cluster_counts),
    'dup_dropped': len(dup_dropped),
    'rejected_files_total': len(ct_reject_entries),
    'per_work': {cl: {'confirmed': v['notes_confirmed'], 'rejected': v['rejected_as_trivial'], 'dup': v['rejected_as_duplicate']} for cl, v in per_work.items()},
}
dump(os.path.join(ROOT, 'scripts', '_rebuild_summary.json'), summary)
print('SUMMARY', json.dumps(summary, ensure_ascii=False))

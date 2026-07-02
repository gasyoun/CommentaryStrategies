#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Idempotent patch of the 'Межтекстовый слой' section in the enriched HTML.

Replaces the pilot ch.1 section with a book-wide per-perspective table grouped
by cluster, and rebuilds the ctData JS array from the merged commentary file.
Safe to run repeatedly (replaces by stable markers).
"""
import json, sys, os, re
from collections import OrderedDict, Counter

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HTML = os.path.join(ROOT, 'leonov_sundara_corpus_enriched.html')
COMM = os.path.join(ROOT, 'data', 'sundara_commentary_to_add.json')
LEDGER = os.path.join(ROOT, 'data', 'sundara_decision_ledger.json')

comm = json.load(open(COMM, encoding='utf-8'))
ledger = json.load(open(LEDGER, encoding='utf-8'))
ct = [x for x in comm if isinstance(x, dict) and '_meta' not in x and x.get('subtype') == 'cross_text']
per_work = ledger['per_work_cross_text_map']

# cluster order + display labels (prompt grouping)
CLUSTER_ORDER = OrderedDict([
    ('dharmashastra', 'Ману'),
    ('mbh_narrative', 'МБх-нарратив'),
    ('mbh_gnomic', 'Шанти'),
    ('ramayana_grintser', 'Гринцер'),
    ('gita', 'Гита'),
    ('kavya', 'кавья'),
])
# note: prompt lists Ману/МБх-нарратив/МБх-батальные/Гринцер/Гита/Шанти/кавья/упанишады/пураны;
# only the 6 clusters above exist in the recovered data — батальные/упанишады/пураны empty, omitted.

BADGE = {
    'dharmashastra': ('bt-other', 'дхармашастра'),
    'mbh_narrative': ('bt-maha', 'МБх-нарратив'),
    'mbh_gnomic': ('bt-maha', 'МБх-Шанти'),
    'ramayana_grintser': ('bt-other', 'Рам. I–III'),
    'gita': ('bt-gita', 'Гита'),
    'kavya': ('bt-other', 'кавья'),
}

def shloka_key(s):
    m = re.match(r'V\.(\d+)\.(\d+)', str(s))
    return (int(m.group(1)), int(m.group(2))) if m else (999, 999)

# build JS ctData rows grouped by cluster order, then by shloka
rows = []
for cl in CLUSTER_ORDER:
    grp = sorted([n for n in ct if n.get('cluster') == cl], key=lambda n: shloka_key(n.get('shloka')))
    for n in grp:
        pr = n.get('priority') or 'med'
        also = n.get('also') or []
        also_txt = '; '.join(f"{a.get('source','')}".split('(')[0].strip() for a in also) if also else ''
        rows.append({
            'cl': cl,
            'cll': CLUSTER_ORDER[cl],
            'sh': n.get('shloka'),
            'lem': n.get('lemma_iast'),
            'wl': (n.get('source') or '').split('(')[0].strip(),
            'va': n.get('parallel_addr') or '',
            'tx': (n.get('note_ru') or '').replace('\n', ' '),
            'pr': pr,
            'also': also_txt,
        })

def jss(s):
    return json.dumps(s, ensure_ascii=False)

js_lines = ['const ctData = [']
for r in rows:
    js_lines.append('  {cl:%s,cll:%s,sh:%s,lem:%s,wl:%s,va:%s,pr:%s,also:%s,tx:%s},' % (
        jss(r['cl']), jss(r['cll']), jss(r['sh']), jss(r['lem']), jss(r['wl']),
        jss(r['va']), jss(r['pr']), jss(r['also']), jss(r['tx'])))
js_lines.append('];')
js_array = '\n'.join(js_lines)

# cluster badge map for JS
badge_js = 'const ctBadge = ' + json.dumps(
    {cl: list(BADGE[cl]) for cl in CLUSTER_ORDER}, ensure_ascii=False) + ';'

# ---- new JS block (between markers) ----
js_block = f"""// ── Межтекстовый слой (§07 cross_text · книжный охват, 6 источников) ──
{js_array}
{badge_js}
const ctClusterLabel = {json.dumps({cl: lbl for cl, lbl in CLUSTER_ORDER.items()}, ensure_ascii=False)};
const ctbody = document.getElementById('ctBody');
if (ctbody) {{
  const prioBadge2 = {{"high":["#c23b22","выс."],"med":["#e08020","сред."],"low":["#888","низ."]}};
  let curCl = null;
  ctData.forEach(n=>{{
    if (n.cl !== curCl) {{
      curCl = n.cl;
      const cnt = ctData.filter(x=>x.cl===curCl).length;
      const [bc,bl] = ctBadge[curCl]||["bt-other",curCl];
      const hr = document.createElement('tr');
      hr.innerHTML = `<td colspan="5" style="background:#f3efe6;padding:8px 10px;font-family:'PT Serif',serif;font-weight:700;font-size:14px;color:var(--leo);">`
        + `<span class="badge-type ${{bc}}" style="margin-right:8px;">${{bl}}</span>${{ctClusterLabel[curCl]||curCl}} · ${{cnt}} примеч.</td>`;
      ctbody.appendChild(hr);
    }}
    const [pc,pl] = prioBadge2[n.pr]||["#888",n.pr];
    const tr = document.createElement('tr');
    const alsoHtml = n.also ? `<br><span style="font-size:10.5px;color:var(--muted);">также: ${{n.also}}</span>` : '';
    tr.innerHTML = `
      <td style="font-family:'PT Sans',sans-serif;font-weight:700;color:var(--leo);white-space:nowrap;">${{n.sh}}</td>
      <td><iast style="font-weight:700;">${{n.lem}}</iast><br><span class="example-addr" style="font-size:11px;">${{n.wl}}</span>${{alsoHtml}}</td>
      <td style="font-size:12px;color:var(--muted);">${{n.va}}</td>
      <td style="font-family:'PT Serif',serif;font-size:12.5px;line-height:1.5;">${{(n.tx||'').slice(0,260)}}…</td>
      <td><span style="display:inline-block;padding:2px 8px;border-radius:2px;font-size:11px;font-weight:700;color:#fff;background:${{pc}};">${{pl}}</span></td>`;
    ctbody.appendChild(tr);
  }});
}}
"""

# ---- contribution map table rows (book-wide) ----
contrib_rows = []
for cl, lbl in CLUSTER_ORDER.items():
    w = per_work.get(cl, {})
    bc, bl = BADGE[cl]
    contrib_rows.append(
        f'      <tr>\n'
        f'        <td style="font-weight:700;">{w.get("label", lbl)}</td>\n'
        f'        <td><span class="badge-type {bc}">{bl}</span></td>\n'
        f'        <td>{w.get("stems_overlapped", 0)}</td>\n'
        f'        <td>{w.get("notes_confirmed", 0)}</td>\n'
        f'        <td>{w.get("rejected_as_trivial", 0)}</td>\n'
        f'      </tr>')
contrib_tbody = '\n'.join(contrib_rows)

total_conf = sum(per_work.get(cl, {}).get('notes_confirmed', 0) for cl in CLUSTER_ORDER)
total_rej = sum(per_work.get(cl, {}).get('rejected_as_trivial', 0) for cl in CLUSTER_ORDER)

# ---- new section markup ----
section = f'''<!-- § МЕЖТЕКСТОВЫЙ СЛОЙ (книжный охват) -->
<section class="section" id="cross_text">
  <div class="section-eyebrow">§ 07 · Межтекстовый слой · книжный охват · 6 источников</div>
  <h2>Межтекстовый слой — примечания из параллельных текстов (вся кн. V, по перспективам)</h2>

  <p style="font-family:'PT Sans',sans-serif; font-size:14px; line-height:1.7; margin-bottom:12px;">
    Помимо 95 базовых примечаний (Тип А/Б/В), по всей <strong>книге V</strong> добавлен
    слой межтекстовых параллелей (<code>subtype: "cross_text"</code>): {total_conf} подтверждённых
    локусов из <strong>шести</strong> нераямаянских/рамаянских перспектив корпуса, подлинно
    освещающих шлок Сундараканды. Критерий допуска: <em>не</em> тривиальное пересечение стеблей,
    а конкретный смысловой вклад — locus classicus термина, гномический/этический параллелизм,
    дхарма-норма, нарративный мотив-двойник или кāвья-переосмысление. Каждое примечание —
    <code>review_required: true</code>; свидетельство — уровень шлоки (мягкое). При совпадении
    шлока+лемма между разными works обе перспективы сохранены и связаны полем <code>also</code>.
  </p>

  <div class="soft-note" style="margin-bottom:20px;">
    <strong>Сгруппировано по кластеру-перспективе:</strong> Ману (дхарма-норма) · МБх-нарратив
    (мотивы-двойники) · Шанти (гномика, царская нити) · Гринцер (углубление рамаянского фона) ·
    Гита (этика долга, бхакти) · кāвья (переосмысление эпитета). Каждый блок открывается строкой-заголовком.
  </div>

  <!-- Таблица cross_text примечаний (книжный охват, по кластерам) -->
  <table class="rel-table" style="margin-bottom:28px;">
    <thead>
      <tr>
        <th style="width:64px;">Шлока</th>
        <th style="width:150px;">Стержень (IAST)</th>
        <th style="width:120px;">Источник · локус</th>
        <th>Текст примечания (фрагмент)</th>
        <th style="width:52px;">Приор.</th>
      </tr>
    </thead>
    <tbody id="ctBody"><!-- filled by script: grouped by cluster --></tbody>
  </table>

  <!-- Карта вклада по источникам (книжный охват) -->
  <h3 style="font-family:'PT Serif',serif; font-size:16px; margin:24px 0 10px;">
    Вклад источников (пересечение стеблей → подтверждено в примечание / отклонено)
  </h3>
  <table class="rel-table">
    <thead>
      <tr>
        <th>Источник / кластер</th>
        <th>Тип</th>
        <th>Стеблей пересечено</th>
        <th>Подтверждено</th>
        <th>Отклонено</th>
      </tr>
    </thead>
    <tbody>
{contrib_tbody}
      <tr style="font-weight:700;background:#f3efe6;">
        <td>Итого</td><td></td><td></td><td>{total_conf}</td><td>{total_rej}</td>
      </tr>
    </tbody>
  </table>

  <p style="font-family:'PT Sans',sans-serif; font-size:13px; color:var(--muted); margin-top:8px;">
    Отклонено {total_rej} межтекстовых кандидата — тривиальные стем-коллизии, фабрикованные
    или мисатрибутированные локусы (полная причина по каждому — в «Решебнике»). —
    Полный реестр: <a href="data/sundara_decision_ledger.json" style="color:var(--leo);">data/sundara_decision_ledger.json</a>
    · <a href="SUNDARA_COMMENTARY_RATIONALE.md" style="color:var(--leo);">SUNDARA_COMMENTARY_RATIONALE.md</a>
  </p>
</section>'''

# ---------------------------------------------------------------------------
html = open(HTML, encoding='utf-8').read()

# Replace the whole section (from the comment marker to the matching </section>)
sec_pat = re.compile(
    r'<!-- § МЕЖТЕКСТОВЫЙ СЛОЙ.*?-->\s*<section class="section" id="cross_text">.*?</section>',
    re.DOTALL)
html, ns = sec_pat.subn(lambda m: section, html, count=1)
assert ns == 1, f'section replace count={ns}'

# Replace the JS block: from '// ── Межтекстовый слой' up to the next '// ── ' comment
js_pat = re.compile(
    r'// ── Межтекстовый слой.*?(?=\n// ── Плотность примечаний)',
    re.DOTALL)
html, nj = js_pat.subn(lambda m: js_block, html, count=1)
assert nj == 1, f'js replace count={nj}'

# Fix stale ledger-section count "итоговые 105 примечаний (включая 10 cross_text)"
html = html.replace('итоговые 105 примечаний (включая 10 cross_text)',
                    'итоговые 202 примечания (включая 107 cross_text из 6 источников)')
html = re.sub(r'105 примечаний', '202 примечания', html)

with open(HTML, 'w', encoding='utf-8') as f:
    f.write(html)
print('PATCHED HTML: section + js + counts')
print('BOM' if html.encode('utf-8')[:3] == b'\xef\xbb\xbf' else 'no-BOM')
print('ct rows:', len(rows), 'clusters:', dict(Counter(r['cl'] for r in rows)))

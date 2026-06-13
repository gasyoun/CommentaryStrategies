#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Генератор data-driven визуализаций (visualizations.html).

Считает РЕАЛЬНЫЙ профиль шести переводчиков из data/*_markup_50.json и встраивает
его в visualizations.html (Chart.js). Заменяет прежнюю версию с приблизительными
захардкоженными числами — теперь графики строятся из источника истины.

Панели: пузырьки (IAST×длина), тепловая карта (темы×переводчики), столбцы по
Казанскому (A/B/V/G), радар-профиль, scatter «читательский контракт» (IAST×
дискурсивность) с контрастом Нилакантхи.

Запуск:  python scripts/build_visualizations.py
Зависимости: только stdlib. Цвета — токены дизайн-системы (css/commentary.css).
"""

import json
import statistics
import sys
import pathlib
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8")

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
OUT = ROOT / "visualizations.html"

# Переводчик → (отображаемое имя, цвет из дизайн-системы)
TR = [
    ("kalyanov", "Кальянов", "#2a5a8b"),
    ("vassilkov", "Васильков", "#3a6b35"),
    ("erman", "Эрман", "#5a2d82"),
    ("grintser", "Гринцер", "#8b4513"),
    ("syrkin", "Сыркин", "#7a3b00"),
    ("leonov", "Леонов", "#7c4b2a"),
]
TOPICS = ["sanskrit_term", "myth", "context", "realia", "geography",
          "reference", "textology", "philosophy", "poetics"]
TOPIC_RU = {"sanskrit_term": "санскр. термин", "myth": "миф/персонаж",
            "context": "контекст", "realia": "реалия", "geography": "география",
            "reference": "отсылка", "textology": "текстология",
            "philosophy": "философия", "poetics": "поэтика"}

# Нилакантха — индигенная база (из data/nilakantha_profile.json, PR #7; здесь как
# встроенная константа, т.к. файл приходит с тем PR).
NILAKANTHA = {"verses": 1800, "with_tika": 373, "coverage_pct": 20.7,
              "median_gloss": 30, "substantive": 90}


def compute():
    rows = []
    for slug, name, color in TR:
        recs = json.loads((DATA / f"{slug}_markup_50.json").read_text(encoding="utf-8"))
        n = len(recs)
        lengths = [len(r["raw_text"]) for r in recs]
        kaz = Counter(r["axis_2_kazansky"] for r in recs)
        par = Counter(r.get("axis_4_paribok") for r in recs)
        top = Counter(t for r in recs for t in r.get("axis_1_topic", []))
        rows.append({
            "slug": slug, "name": name, "color": color, "n": n,
            "iast": round(100 * sum(1 for r in recs if r.get("has_iast")) / n),
            "mean_len": round(statistics.mean(lengths)),
            "median_len": round(statistics.median(lengths)),
            "multitopic": round(100 * sum(1 for r in recs if len(r.get("axis_1_topic", [])) > 1) / n),
            "kazansky": {c: kaz.get(c, 0) for c in "ABVG"},
            "paribok": {c: round(100 * par.get(c, 0) / n) for c in "PKD"},
            "topics": {t: round(100 * top.get(t, 0) / n, 1) for t in TOPICS},
        })
    return rows


HTML = """<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Визуализация стратегий комментирования</title>
<link rel="stylesheet" href="css/commentary.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.js"></script>
<style>
  .chart-container{background:var(--paper);border:1px solid var(--rule);padding:2rem;margin-bottom:3rem}
  .chart-wrap{position:relative;width:100%}
  .legend{display:flex;flex-wrap:wrap;gap:1.2rem;margin-top:1.2rem;font-family:'JetBrains Mono',monospace;font-size:.68rem;text-transform:uppercase;letter-spacing:.05em;color:var(--muted)}
  .legend span{display:flex;align-items:center;gap:.4rem}
  .legend-dot{width:.7rem;height:.7rem;border-radius:2px;display:inline-block}
  .gen-note{font-size:.78rem;color:var(--muted);font-style:italic}
  .panel-note{font-size:.85rem;color:var(--muted);margin-top:1rem}
</style>
</head>
<body>
<header>
  <div class="breadcrumb"><a href="index.html">&larr; Аналитика</a> / Визуализации</div>
  <h1>Визуализация стратегий</h1>
  <div class="subtitle">Шесть переводчиков по 4-осной сетке + Нилакантха как индигенная база</div>
</header>
<main class="container">
<p class="gen-note">Графики построены из данных автоматически (scripts/build_visualizations.py);
золотая выборка — 50 примечаний на переводчика.</p>

<section><h2 class="section-title">01. IAST &times; длина примечания</h2>
  <div class="chart-container"><div class="chart-wrap" style="height:420px;"><canvas id="bubble"></canvas></div>
  <div id="leg1" class="legend"></div>
  <p class="panel-note">Размер пузыря — многотемность. Филологический полюс (Кальянов/Леонов)
  при 100&nbsp;% IAST; гуманитарный (Гринцер) — слева внизу при 12&nbsp;%.</p></div></section>

<section><h2 class="section-title">02. Темы &times; переводчики</h2>
  <div class="chart-container"><div id="heat"></div></div></section>

<section><h2 class="section-title">03. Тип комментария (Казанский A/B/V/G)</h2>
  <div class="chart-container"><div class="chart-wrap" style="height:340px;"><canvas id="kaz"></canvas></div>
  <div id="leg3" class="legend"></div></div></section>

<section><h2 class="section-title">04. Радар: нормированный профиль</h2>
  <div class="chart-container"><div class="chart-wrap" style="height:520px;"><canvas id="radar"></canvas></div>
  <div id="leg4" class="legend" style="justify-content:center;"></div></div></section>

<section><h2 class="section-title">05. Читательский контракт: IAST &times; дискурсивность</h2>
  <div class="chart-container"><div class="chart-wrap" style="height:440px;"><canvas id="scatter"></canvas></div>
  <p class="panel-note">Ось X — IAST&nbsp;%, ось Y — доля дискурсивных примечаний (Парибок&nbsp;D).
  Три контракта расходятся: филологический (низ-право), гуманитарный (низ-лево),
  философский (верх). Нилакантха (adhikārin) несоизмерим: покрытие лишь
  __NK_COV__&nbsp;% строф, терсная глосса ~__NK_MED__ знаков — на этой плоскости он
  был бы вырожденной точкой у нуля по обеим осям.</p></div></section>
</main>
<footer>CommentaryStrategies &copy; 2026 &middot; Визуальный анализ</footer>

<script>
const D = __DATA__;
const css = getComputedStyle(document.documentElement);
const RULE = css.getPropertyValue('--rule') || '#c9bfaf';
const fade = (hex,a)=>{const n=parseInt(hex.slice(1),16);return `rgba(${n>>16&255},${n>>8&255},${n&255},${a})`;};

// 01 bubble
new Chart(bubble,{type:'bubble',data:{datasets:D.map(t=>({label:t.name,
  data:[{x:t.iast,y:t.mean_len,r:6+t.multitopic/4}],backgroundColor:fade(t.color,.18),borderColor:t.color,borderWidth:1.5}))},
  options:{responsive:true,maintainAspectRatio:false,layout:{padding:18},plugins:{legend:{display:false}},
  scales:{x:{min:0,max:105,title:{display:true,text:'IAST, %'}},y:{min:55,max:140,title:{display:true,text:'Ср. длина, знаков'}}}}});
mkleg('leg1',D.map(t=>[t.name,t.color]));

// 02 heatmap (SVG)
const TOP=__TOPICS__, TRU=__TOPIC_RU__;
const cW=86,cH=34,lW=150,tH=28,W=lW+cW*D.length+8,H=tH+cH*TOP.length+6;
let s=`<svg viewBox="0 0 ${W} ${H}" width="100%" xmlns="http://www.w3.org/2000/svg" style="display:block;font-family:'Source Serif 4',serif">`;
D.forEach((t,j)=>s+=`<text x="${lW+j*cW+cW/2}" y="${tH-8}" text-anchor="middle" font-size="11" fill="var(--muted)">${t.name}</text>`);
TOP.forEach((tk,i)=>{const y=tH+i*cH;s+=`<text x="${lW-8}" y="${y+cH/2+4}" text-anchor="end" font-size="11" fill="var(--ink)">${TRU[tk]}</text>`;
  D.forEach((t,j)=>{const v=t.topics[tk]||0,x=lW+j*cW,a=Math.min(.85,v/55+.04);
    s+=`<rect x="${x+1}" y="${y+1}" width="${cW-2}" height="${cH-2}" rx="3" fill="${t.color}" fill-opacity="${a}"/>`;
    s+=`<text x="${x+cW/2}" y="${y+cH/2+4}" text-anchor="middle" font-size="10.5" font-weight="500" fill="${a>.4?'#fff':'var(--ink)'}">${v>0?v+'%':'—'}</text>`;});});
heat.innerHTML=s+'</svg>';

// 03 Kazansky stacked
const KZ=[['A','филологический'],['B','текстологический'],['V','историко-культурный'],['G','культурологический']];
const KC={A:'#2a5a8b',B:'#5a2d82',V:'#8b4513',G:'#7a3b00'};
new Chart(kaz,{type:'bar',data:{labels:D.map(t=>t.name),datasets:KZ.map(([c,lab])=>({label:lab,
  data:D.map(t=>Math.round(100*t.kazansky[c]/t.n)),backgroundColor:KC[c],borderWidth:0}))},
  options:{responsive:true,maintainAspectRatio:false,plugins:{legend:{display:false}},
  scales:{x:{stacked:true},y:{stacked:true,max:100,ticks:{callback:v=>v+'%'}}}}});
mkleg('leg3',KZ.map(([c,lab])=>[lab,KC[c]]));

// 04 radar (normalized across translators per axis)
const AX=[['Длина',t=>t.mean_len],['IAST %',t=>t.iast],['Понятие P',t=>t.paribok.P],
  ['Кодиф. K',t=>t.paribok.K],['Дискурс D',t=>t.paribok.D],['Философия',t=>t.topics.philosophy||0]];
const raw=AX.map(([,f])=>D.map(f)),norm=raw.map(a=>{const mn=Math.min(...a),mx=Math.max(...a),d=mx-mn||1;return a.map(v=>Math.round((v-mn)/d*100));});
new Chart(radar,{type:'radar',data:{labels:AX.map(a=>a[0]),datasets:D.map((t,j)=>({label:t.name,
  data:norm.map(ax=>ax[j]),borderColor:t.color,backgroundColor:fade(t.color,.12),borderWidth:1.5,pointRadius:3}))},
  options:{responsive:true,maintainAspectRatio:false,plugins:{legend:{display:false}},
  scales:{r:{min:0,max:100,ticks:{display:false},grid:{color:RULE},angleLines:{color:RULE}}}}});
mkleg('leg4',D.map(t=>[t.name,t.color]));

// 05 contract scatter
new Chart(scatter,{type:'scatter',data:{datasets:D.map(t=>({label:t.name,
  data:[{x:t.iast,y:t.paribok.D}],backgroundColor:t.color,borderColor:t.color,pointRadius:8,pointHoverRadius:10}))},
  options:{responsive:true,maintainAspectRatio:false,layout:{padding:18},
  plugins:{legend:{display:false},tooltip:{callbacks:{label:c=>c.dataset.label+` (IAST ${c.parsed.x}%, D ${c.parsed.y}%)`}}},
  scales:{x:{min:0,max:105,title:{display:true,text:'IAST, %'}},y:{min:-2,max:50,title:{display:true,text:'Дискурсивность (Парибок D), %'}}}}});

function mkleg(id,pairs){const el=document.getElementById(id);pairs.forEach(([n,c])=>{const sp=document.createElement('span');sp.innerHTML=`<span class="legend-dot" style="background:${c}"></span>${n}`;el.appendChild(sp);});}
</script>
</body>
</html>
"""


def main():
    rows = compute()
    html = (HTML
            .replace("__DATA__", json.dumps(rows, ensure_ascii=False))
            .replace("__TOPICS__", json.dumps(TOPICS))
            .replace("__TOPIC_RU__", json.dumps(TOPIC_RU, ensure_ascii=False))
            .replace("__NK_COV__", str(NILAKANTHA["coverage_pct"]))
            .replace("__NK_MED__", str(NILAKANTHA["median_gloss"])))
    OUT.write_text(html, encoding="utf-8", newline="\n")
    print(f"Записано: {OUT.relative_to(ROOT)} ({len(html)} знаков, {len(rows)} переводчиков)")
    for r in rows:
        print(f"  {r['name']:10s} IAST {r['iast']:>3}%  ср.длина {r['mean_len']:>3}  "
              f"P/K/D {r['paribok']['P']}/{r['paribok']['K']}/{r['paribok']['D']}")


if __name__ == "__main__":
    main()

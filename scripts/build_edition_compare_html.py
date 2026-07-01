#!/usr/bin/env python3
"""Build a self-contained HTML report for the critical↔southern edition comparison.

Joins data/edition_comparison/{book_summary,concordance,significant_absences,
critical_only_and_variants}.json into one browsable page (inline JSON + JS) with
tabs: overview + per-sarga table, structural absences (footnote candidates),
reworded verses, word-variants, critical-only. No external deps; open locally.

Usage: python scripts/build_edition_compare_html.py
Output: data/edition_comparison/report.html
"""
import sys
import os
import json

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
CD = os.path.join(REPO, "data", "edition_comparison")
OUT = os.path.join(CD, "report.html")


def load(name):
    return json.load(open(os.path.join(CD, name), encoding="utf-8"))


def main():
    bs = load("book_summary.json")
    sa = load("significant_absences.json")
    cv = load("critical_only_and_variants.json")

    structural = sa.get("structural_absence", [])
    reworded = sa.get("reworded", [])
    runs = sa.get("runs", [])
    div = {r["southern"]: r.get("divergence") for r in structural + reworded}
    # annotate runs with structural/reworded composition
    for run in runs:
        ids = [f"5.{run['sarga']}.{v}" for v in run["verses"]]
        run["structural"] = sum(1 for i in ids if div.get(i) == "structural_absence")
        run["reworded"] = sum(1 for i in ids if div.get(i) == "reworded")

    data = {
        "totals": bs["book_totals"],
        "per_sarga": bs.get("per_sarga_aligned", []),
        "extra_sargas": bs.get("southern_extra_sargas", []),
        "runs": sorted(runs, key=lambda r: -r["count"]),
        "structural": structural,
        "reworded": reworded,
        "critical_only": cv.get("critical_only", []),
        "variants": cv.get("variants", []),
        "meta": bs.get("_meta", {}),
    }
    html = PAGE.replace("/*DATA*/null", json.dumps(data, ensure_ascii=False))
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write(html)
    print(f"wrote {OUT}  (runs {len(runs)}, structural {len(structural)}, "
          f"reworded {len(reworded)}, variants {len(data['variants'])}, "
          f"critical_only {len(data['critical_only'])})")


PAGE = r"""<!DOCTYPE html>
<html lang="ru"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Критическое (Барода) ↔ южное (Леонов) — сравнение изданий, Сундараканда</title>
<link rel="stylesheet" href="../../css/commentary.css">
<style>
:root{--bg:#faf8f4;--card:#fff;--ink:#222;--mut:#777;--line:#e4ddd0;--acc:#5a4a7a;
--abs:#2e7d32;--rew:#b8860b;--crit:#b23b3b;--var:#3a6ea5;}
*{box-sizing:border-box}
body{font:15px/1.5 Georgia,serif;margin:0;background:var(--bg);color:var(--ink)}
header{position:sticky;top:0;background:#fff;border-bottom:2px solid var(--acc);padding:10px 18px;z-index:10;box-shadow:0 2px 6px rgba(0,0,0,.06)}
h1{font-size:17px;margin:0 0 6px}
.badges{display:flex;gap:8px;flex-wrap:wrap;font:12px system-ui,sans-serif;margin-bottom:6px}
.b{background:#efe9dd;border-radius:10px;padding:2px 9px;color:var(--acc)}
.tabs{display:flex;gap:6px;flex-wrap:wrap}
.tab{font:13px system-ui,sans-serif;padding:5px 12px;border:1px solid var(--acc);background:#fff;color:var(--acc);border-radius:5px;cursor:pointer}
.tab.on{background:var(--acc);color:#fff}
input#q{font:13px system-ui,sans-serif;padding:5px 10px;border:1px solid var(--line);border-radius:5px;margin-left:auto;min-width:200px}
main{max-width:960px;margin:0 auto;padding:16px}
table{border-collapse:collapse;width:100%;font:13px system-ui,sans-serif}
th,td{border:1px solid var(--line);padding:4px 8px;text-align:left}
th{background:#f2ecdd}
tr.extra{background:#eaf6ea}
.row{background:var(--card);border:1px solid var(--line);border-radius:7px;padding:8px 12px;margin:7px 0}
.row.abs{border-left:4px solid var(--abs)}
.row.rew{border-left:4px solid var(--rew)}
.row.crit{border-left:4px solid var(--crit)}
.row.var{border-left:4px solid var(--var)}
.vid{font:12px system-ui,sans-serif;color:var(--mut)}
.tag{font:11px system-ui,sans-serif;padding:1px 7px;border-radius:9px;margin-left:6px}
.tag.abs{background:#e5f3e5;color:var(--abs)} .tag.rew{background:#f6eede;color:var(--rew)}
.sa{font-style:italic;color:#3a3020;margin-top:3px}
.two{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:4px}
.two .c{background:#f7f2e8;border-radius:5px;padding:5px 8px}
.two .lbl{font:11px system-ui,sans-serif;color:var(--mut)}
.hint{font:12px system-ui,sans-serif;color:var(--mut);margin:6px 0 12px}
section{display:none} section.on{display:block}
.run{font:13px system-ui,sans-serif}
</style></head><body>
<header>
<h1>Сундараканда · критическое (GRETIL/Барода) ↔ южное (перевод Леонова)</h1>
<div class="badges" id="badges"></div>
<div class="tabs">
<button class="tab on" data-s="overview">Обзор</button>
<button class="tab" data-s="absence">Отсутствия (сноски)</button>
<button class="tab" data-s="reworded">Переформулировки</button>
<button class="tab" data-s="variants">Разночтения слов</button>
<button class="tab" data-s="critonly">Только в критическом</button>
<input id="q" placeholder="фильтр по стиху / тексту…">
</div></header>
<main class="container">
<section id="overview" class="on"></section>
<section id="absence"></section>
<section id="reworded"></section>
<section id="variants"></section>
<section id="critonly"></section>
</main>
<script>
const D=/*DATA*/null;
function esc(s){return (s||"").replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;");}
const t=D.totals;
document.getElementById("badges").innerHTML=[
 `песни <b>${t.critical_sargas}</b> vs <b>${t.southern_sargas}</b> (+${t.southern_sargas-t.critical_sargas})`,
 `шлоки <b>${t.critical_verses}</b> vs <b>${t.southern_verses}</b> (+${t.delta_southern_minus_critical})`,
 `идентичных ${t.identical_verses}`,`вариантных ${t.variant_verses}`,
 `отсутствий ${t.southern_structural_absence}`,`переформ. ${t.southern_reworded}`,
 `только крит. ${t.critical_only_verses}`
].map(x=>`<span class="b">${x}</span>`).join("");

// Overview
(function(){
 let h=`<div class="hint">Сарги сопоставлены по содержанию. Зелёным — южные сарги без критического аналога (${D.extra_sargas.join(", ")||"—"}).</div>`;
 h+=`<table><tr><th>крит. песнь</th><th>→ южн.</th><th>шлок крит.</th><th>шлок южн.</th><th>Δ</th></tr>`;
 D.per_sarga.forEach(r=>{const ex=D.extra_sargas.includes(r.southern_sarga);
   h+=`<tr class="${ex?'extra':''}"><td>${r.critical_sarga}</td><td>${r.southern_sarga??'—'}</td><td>${r.critical_verses}</td><td>${r.southern_verses}</td><td>${r.delta_southern_minus_critical}</td></tr>`;});
 h+=`</table>`;
 document.getElementById("overview").innerHTML=h;
})();

// Absence (runs, filterable)
function renderAbsence(q){
 let h=`<div class="hint">Кандидаты в сноски «в критическом издании (Барода) отсутствует». Каждый пассаж помечен: <b style="color:var(--abs)">структурное отсутствие</b> (безопасно) / <b style="color:var(--rew)">переформулировка</b> (разночтение, не сноска). Плюс целые южные сарги ${D.extra_sargas.join(", ")}.</div>`;
 D.runs.filter(r=>!q||(`5.${r.sarga}.`+r.verses.join(" ")).includes(q)).forEach(r=>{
   const pure=r.reworded===0;
   h+=`<div class="row ${pure?'abs':'rew'}"><span class="run"><b>${r.range}</b> — ${r.count} шлок`+
      `<span class="tag abs">структ. ${r.structural}</span><span class="tag rew">переформ. ${r.reworded}</span>`+
      (pure?' — чистое отсутствие':'')+`</span></div>`;});
 return h;
}
// generic list renderer
function renderList(arr,cls,fmt,q){
 return arr.filter(x=>!q||JSON.stringify(x).toLowerCase().includes(q)).slice(0,1200).map(fmt).join("")
   ||`<div class="hint">нет записей</div>`;
}
function draw(q){
 q=(q||"").toLowerCase().trim();
 document.getElementById("absence").innerHTML=renderAbsence(q);
 document.getElementById("reworded").innerHTML=
  `<div class="hint">Та же шлока присутствует в критическом, но сильно переписана (Jaccard 0.25–0.5) — это разночтение, НЕ отсутствие.</div>`+
  renderList(D.reworded,"rew",x=>`<div class="row rew"><span class="vid">${x.southern} · Jaccard ${x.best_crit_jaccard??''}</span><div class="sa">${esc(x.text)}</div></div>`,q);
 document.getElementById("variants").innerHTML=
  `<div class="hint">Пары шлок, признанные вариантами (в т.ч. fuzzy). Слева критическое, справа южное.</div>`+
  renderList(D.variants,"var",x=>`<div class="row var"><span class="vid">${x.critical} ↔ ${x.southern} · сходство ${x.similarity??''}${x.kind?' · '+x.kind:''}</span><div class="two"><div class="c"><span class="lbl">критическое</span><div class="sa">${esc(x.critical_text||'')}</div></div><div class="c"><span class="lbl">южное</span><div class="sa">${esc(x.southern_text||'')}</div></div></div></div>`,q);
 document.getElementById("critonly").innerHTML=
  `<div class="hint">Шлоки, найденные только в критическом издании (нет близкого южного аналога). В Рамаяне таких мало — в основном сильно переписанные места.</div>`+
  renderList(D.critical_only,"crit",x=>`<div class="row crit"><span class="vid">${x.critical}</span><div class="sa">${esc(x.text)}</div></div>`,q);
}
draw("");
document.querySelectorAll(".tab").forEach(b=>b.onclick=()=>{
 document.querySelectorAll(".tab").forEach(x=>x.classList.remove("on"));b.classList.add("on");
 document.querySelectorAll("section").forEach(s=>s.classList.remove("on"));
 document.getElementById(b.dataset.s).classList.add("on");});
document.getElementById("q").oninput=e=>draw(e.target.value);
</script></body></html>"""


if __name__ == "__main__":
    main()

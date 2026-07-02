#!/usr/bin/env python3
"""Interactive review gate for the edition-difference footnote candidates.

Reads data/edition_footnotes/candidates.json and emits footnotes_review.html:
one принять/править/отклонить control per candidate, choices persisted in
localStorage, "Скачать decisions.json" export. This is the standard review
artifact (CLAUDE.md "Human review / gating artifacts") — NOT a checkbox markdown.

Usage: python scripts/build_footnotes_review_html.py
Output: data/edition_footnotes/footnotes_review.html
"""
import sys
import os
import json

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
DIR = os.path.join(REPO, "data", "edition_footnotes")
OUT = os.path.join(DIR, "footnotes_review.html")


def main():
    d = json.load(open(os.path.join(DIR, "candidates.json"), encoding="utf-8"))
    items = d.get("candidates", []) + d.get("single_verse_absences", [])
    payload = {"meta": d.get("_meta", {}), "items": items}
    html = PAGE.replace("/*DATA*/null", json.dumps(payload, ensure_ascii=False))
    os.makedirs(DIR, exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write(html)
    print(f"wrote {OUT} ({len(items)} candidates)")


PAGE = r"""<!DOCTYPE html>
<html lang="ru"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Сноски о расхождениях изданий — сверка</title>
<link rel="stylesheet" href="../../css/commentary.css">
<style>
:root{--bg:#faf8f4;--card:#fff;--ink:#222;--mut:#777;--line:#e4ddd0;--acc:#5a4a7a;--ok:#2e7d32;--edit:#b8860b;--no:#b23b3b;}
*{box-sizing:border-box}
body{font:15px/1.5 Georgia,serif;margin:0;background:var(--bg);color:var(--ink)}
header{position:sticky;top:0;background:#fff;border-bottom:2px solid var(--acc);padding:10px 18px;z-index:10;box-shadow:0 2px 6px rgba(0,0,0,.06)}
h1{font-size:17px;margin:0 0 6px}
.bar{display:flex;gap:14px;align-items:center;flex-wrap:wrap;font:13px system-ui,sans-serif;color:var(--mut)}
button{font:13px system-ui,sans-serif;padding:6px 12px;border:1px solid var(--acc);background:#fff;color:var(--acc);border-radius:5px;cursor:pointer}
button:hover{background:var(--acc);color:#fff}
main.container{max-width:920px;margin:0 auto;padding:16px}
.card{background:var(--card);border:1px solid var(--line);border-left:5px solid var(--acc);border-radius:8px;padding:12px 16px;margin:0 0 14px}
.card.d-accept{border-left-color:var(--ok)} .card.d-edit{border-left-color:var(--edit)} .card.d-reject{border-left-color:var(--no);opacity:.75}
.vid{font:12px system-ui,sans-serif;color:var(--mut)}
.badge{font:11px system-ui,sans-serif;padding:1px 7px;border-radius:10px;background:#eee5d3;color:var(--acc);margin-left:6px}
.dup{font:12px system-ui,sans-serif;background:#fff0f0;border:1px solid var(--no);border-radius:5px;padding:4px 8px;margin:6px 0;color:var(--no)}
.note{font-size:16px;margin:8px 0;padding:6px 0;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.absent{background:#f7f2e8;border-radius:6px;padding:6px 10px;margin:6px 0}
.absent .lbl{font:11px system-ui,sans-serif;color:var(--mut)}
.absent .v{font-style:italic;color:#3a3020;margin:2px 0}
.absent .vn{font-style:normal;color:var(--mut);font:11px system-ui,sans-serif;margin-right:6px}
.controls{margin-top:10px;display:flex;gap:8px;flex-wrap:wrap;font:13px system-ui,sans-serif}
.controls label{display:inline-flex;gap:4px;align-items:center;padding:5px 10px;border:1px solid var(--line);border-radius:20px;cursor:pointer}
textarea{width:100%;font:14px Georgia,serif;padding:8px;border:1px solid var(--line);border-radius:5px;margin-top:8px}
.hidden{display:none}
</style></head><body>
<header>
<h1>Сундараканда · сноски о расхождениях изданий — сверка</h1>
<div class="bar">
<span id="prog">—</span>
<button onclick="dl()">⬇ Скачать decisions.json</button>
<button onclick="cp()">⧉ Копировать</button>
<button onclick="rs()">↺ Сброс</button>
<span class="vid">Формат сноски и порог — [на ратификацию]. Координаты корпусные — сверить с печатным критич. аппаратом. Выбор хранится в браузере.</span>
</div></header>
<main class="container"><div id="app"></div></main>
<script>
const D=/*DATA*/null;
const KEY="edition_footnotes_decisions_v1";
const dec=JSON.parse(localStorage.getItem(KEY)||"{}");
function esc(s){return (s||"").replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;");}
function render(){
 const app=document.getElementById("app");app.innerHTML="";
 D.items.forEach((c,i)=>{
  const id=c.anchor||("#"+i); const d=dec[id]||{};
  const dup=c.leonov_edition_note_here?`<div class="dup">⚠ Леонов уже отмечает редакцию на этих стихах (${c.leonov_edition_note_here.join(", ")}) — возможно дубль</div>`
    :(c.leonov_note_here?`<div class="vid">у Леонова есть примечание на этих стихах: ${c.leonov_note_here.join(", ")}</div>`:"");
  const card=document.createElement("div");
  card.className="card"+(d.action?" d-"+d.action:"");card.id="c"+i;
  card.innerHTML=`<div class="vid">${c.range}<span class="badge">${c.kind}</span><span class="badge">${c.count} шлок</span></div>
   ${dup}
   <div class="note">${esc(c.note_ru)}</div>
   <div class="absent"><span class="lbl">Отсутствующий текст (IAST):</span>${
     (c.verses_iast||[]).map(v=>`<div class="v"><span class="vn">${v.verse_id}</span>${esc(v.iast)||'<span class="vn">—</span>'}</div>`).join("")
   }</div>
   <div class="controls">
     <label><input type="radio" name="a${i}" value="accept"> ✅ принять</label>
     <label><input type="radio" name="a${i}" value="edit"> ✏️ править</label>
     <label><input type="radio" name="a${i}" value="reject"> ❌ отклонить</label>
   </div>
   <textarea class="hidden" id="e${i}" rows="2">${esc(d.edited_note||c.note_ru)}</textarea>
   <input class="hidden" id="r${i}" placeholder="Причина отклонения…" value="${esc(d.reject_reason||'')}"
     style="width:100%;font:13px system-ui;padding:6px;border:1px solid var(--line);border-radius:5px;margin-top:6px">`;
  app.appendChild(card);
  card.querySelectorAll(`input[name=a${i}]`).forEach(r=>{if(d.action===r.value)r.checked=true;r.onchange=()=>set(i,id,r.value);});
  tog(i,d.action);
 });
 prog();
}
function tog(i,a){document.getElementById("e"+i).classList.toggle("hidden",a!=="edit");document.getElementById("r"+i).classList.toggle("hidden",a!=="reject");}
function set(i,id,a){const r=dec[id]||{};r.action=a;r.edited_note=document.getElementById("e"+i).value;r.reject_reason=document.getElementById("r"+i).value;r.range=D.items[i].range;dec[id]=r;
 document.getElementById("e"+i).oninput=()=>{r.edited_note=document.getElementById("e"+i).value;save();};
 document.getElementById("r"+i).oninput=()=>{r.reject_reason=document.getElementById("r"+i).value;save();};
 document.getElementById("c"+i).className="card d-"+a;tog(i,a);save();prog();}
function save(){localStorage.setItem(KEY,JSON.stringify(dec));}
function prog(){const n=D.items.length;const done=D.items.filter((c,i)=>dec[c.anchor||("#"+i)]&&dec[c.anchor||("#"+i)].action).length;
 const a=Object.values(dec).filter(x=>x.action==="accept").length,e=Object.values(dec).filter(x=>x.action==="edit").length,j=Object.values(dec).filter(x=>x.action==="reject").length;
 document.getElementById("prog").innerHTML=`<b>${done}/${n}</b> решено · ✅ ${a} · ✏️ ${e} · ❌ ${j}`;}
function payload(){return JSON.stringify({source:"edition_footnotes",reviewed_at:new Date().toISOString(),decisions:dec},null,2);}
function dl(){const b=new Blob([payload()],{type:"application/json"});const u=URL.createObjectURL(b);const a=document.createElement("a");a.href=u;a.download="decisions.json";a.click();URL.revokeObjectURL(u);}
function cp(){navigator.clipboard.writeText(payload()).then(()=>alert("JSON скопирован"));}
function rs(){if(confirm("Сбросить все решения?")){localStorage.removeItem(KEY);for(const k in dec)delete dec[k];render();}}
render();
</script></body></html>"""


if __name__ == "__main__":
    main()

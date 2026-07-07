#!/usr/bin/env python3
"""Interactive review sheet for the judged lexical layer (H276 WS-2).

Reads the book aggregate's `subtype == "lexical"` notes (AFTER
lexical_judge_merge.py + fix_ch11_lexical_anchors.py), joins each with its
verse (IAST + Leonov подстрочник, SamudraManthanam corpus) and the tier-1
baseline, and emits a self-contained voting page ranked for the assembly gate:
problem verdicts first (flag_anchor → reject → park → edit), then `keep`
weakest-first (ascending rubric score sum). The 7 notes parked by WS-3b
(ch11.qa_removed.json, H276 pass) appear in a final overrideable section —
nothing is invisible to the human gate.

Votes persist in localStorage; «⬇ Скачать decisions.json» exports
{reviewer_decisions: {"<shloka>|<lemma>": {action, edited_note, reject_reason}}}.

Output: data/analysis/lexical_judge/
        commentarystrategies-sundarakanda-lexical_all68_review.html

Usage: python scripts/build_lexical_review_html.py
"""
import sys
import os
import re
import json
from collections import defaultdict

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
DATA = os.path.join(REPO, "data")
BOOK = os.path.join(DATA, "sundara_commentary_to_add.json")
LEONOV = os.path.join(DATA, "leonov_own_notes.json")
QA11 = os.path.join(DATA, "lexical", "ch11.qa_removed.json")
CORPUS = os.path.join(os.path.dirname(REPO), "SamudraManthanam", "web",
                      "corpus_builder", "jsonl", "05_ramayana-sundarakanda.jsonl")
OUT = os.path.join(DATA, "analysis", "lexical_judge",
                   "commentarystrategies-sundarakanda-lexical_all68_review.html")

GROUP_ORDER = ["flag_anchor", "reject", "park", "edit", "keep"]
GROUP_TITLE = {
    "flag_anchor": "⚓ flag_anchor — лемма не подтверждена в стихе (правьте якорь или отклоняйте)",
    "reject": "❌ reject — судья нашёл фактическую/лексикографическую ошибку",
    "park": "🅿 park — тривиально или без лексической ценности (по судье)",
    "edit": "✏️ edit — исправимая формулировка (по судье)",
    "keep": "✅ keep — судья оставил (слабые первыми)",
}


def load(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def main():
    verses = defaultdict(dict)
    with open(CORPUS, encoding="utf-8") as fh:
        for line in fh:
            r = json.loads(line)
            if r.get("seg") in ("sa", "ru") and not r.get("deleted"):
                verses[r["passage"]][r["seg"]] = r["text"]

    tier1 = defaultdict(list)
    for n in load(LEONOV)["notes"]:
        tier1[n["verse_id"]].append({"editor": n.get("editor"),
                                     "note": n.get("raw_text", "")})

    book = load(BOOK)
    lex = [n for n in book if "_meta" not in n and n.get("subtype") == "lexical"]
    missing_judge = [n["shloka"] for n in lex if "judge" not in n]
    if missing_judge:
        sys.exit(f"ERROR: unjudged lexical notes (run lexical_judge_merge.py "
                 f"first): {missing_judge[:5]}…")

    def record(n, parked=False):
        key9 = re.sub(r"^V\.", "", str(n.get("qa_removed", {}).get(
            "original_shloka") if parked else n["shloka"]))
        vv = verses.get(re.sub(r"[ab]$", "", key9), {})
        return {
            "key": f"{n['shloka']}|{n.get('lemma_iast')}",
            "shloka": n["shloka"],
            "lemma": n.get("lemma_iast"),
            "note_ru": n.get("note_ru"),
            "source": n.get("source"),
            "trigger": n.get("trigger"),
            "type": n.get("type"),
            "judge": n.get("judge"),
            "reanchored": n.get("reanchored"),
            "qa_removed": n.get("qa_removed"),
            "verse_iast": vv.get("sa", ""),
            "leonov_ru": vv.get("ru", ""),
            "tier1": tier1.get(f"5.{key9}", [])[:3],
        }

    def score_sum(n):
        return sum(n.get("judge", {}).get("scores", {}).values())

    groups = defaultdict(list)
    for n in lex:
        groups[n["judge"]["verdict"]].append(n)
    ordered, sections = [], []
    for g in GROUP_ORDER:
        items = sorted(groups.get(g, []), key=score_sum)
        if items:
            sections.append({"id": g, "title": GROUP_TITLE[g],
                             "count": len(items)})
            ordered.extend((g, n) for n in items)

    parked = []
    if os.path.exists(QA11):
        parked = [n for n in load(QA11) if "_meta" not in n
                  and n.get("qa_removed", {}).get("handoff") == "H276"]

    data = {
        "generated": "2026-07-07",
        "counts": {g: len(groups.get(g, [])) for g in GROUP_ORDER},
        "total": len(lex),
        "sections": sections,
        "notes": [{**record(n), "group": g} for g, n in ordered],
        "parked": [record(n, parked=True) for n in parked],
    }
    title = (f"Сундараканда · лексический слой ({len(lex)} примечаний, все 68 "
             f"песней) — вердикты судьи и сверка")
    html = (PAGE.replace("/*DATA*/null", json.dumps(data, ensure_ascii=False))
                .replace("__TITLE__", title)
                .replace("__KEY__", "sundara_lexical_judge_decisions_v1"))
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write(html)
    print(f"wrote {OUT} ({len(lex)} notes + {len(parked)} parked)")


PAGE = r"""<!DOCTYPE html>
<html lang="ru"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>__TITLE__</title>
<link rel="stylesheet" href="../../../css/commentary.css">
<style>
:root{--bg:#faf8f4;--card:#fff;--ink:#222;--mut:#777;--line:#e4ddd0;--acc:#7a5c2e;
--ok:#2e7d32;--edit:#b8860b;--no:#b23b3b;--flag:#7b1fa2;}
*{box-sizing:border-box}
body{font:16px/1.55 Georgia,serif;margin:0;background:var(--bg);color:var(--ink)}
header{position:sticky;top:0;background:#fff;border-bottom:2px solid var(--acc);
padding:10px 18px;z-index:5}
h1{font-size:18px;margin:0 0 6px}
.bar{display:flex;gap:16px;align-items:center;flex-wrap:wrap;font:13px/1.4 system-ui,sans-serif;color:var(--mut)}
.bar b{color:var(--ink)}
button{font:13px system-ui,sans-serif;padding:6px 12px;border:1px solid var(--acc);
background:#fff;color:var(--acc);border-radius:5px;cursor:pointer}
button:hover{background:var(--acc);color:#fff}
.container{max-width:900px;margin:0 auto;padding:14px}
.sec{font:15px system-ui,sans-serif;background:#f2ecdd;border:1px solid var(--line);
border-left:5px solid var(--acc);border-radius:6px;padding:8px 12px;margin:22px 0 10px}
.card{background:var(--card);border:1px solid var(--line);border-left:5px solid var(--acc);
border-radius:8px;padding:12px 16px;margin:12px 0}
.card.g-flag_anchor{border-left-color:var(--flag)}
.card.g-reject{border-left-color:var(--no)}
.card.g-park{border-left-color:#607d8b}
.card.g-edit{border-left-color:var(--edit)}
.card.d-accept{border-left-color:var(--ok)}
.card.d-edit{border-left-color:var(--edit)}
.card.d-reject{border-left-color:var(--no);opacity:.75}
.vid{font:12px system-ui,sans-serif;color:var(--mut)}
.badge{font:11px system-ui,sans-serif;padding:1px 7px;border-radius:10px;background:#eee5d3;color:var(--acc)}
.verse{margin:8px 0;font-size:14px}
.verse .sa{color:#333;font-style:italic}
.verse .ru{color:#555}
.why{background:#fff8e6;border:1px dashed var(--edit);border-radius:6px;padding:6px 10px;
font:13px/1.5 system-ui,sans-serif;margin:8px 0}
.why b{color:var(--edit)}
.leo{font-size:13px;background:#fff0f0;border:1px solid var(--no);border-left:4px solid var(--no);
border-radius:6px;padding:6px 10px;margin:8px 0}
.leo .who{font:11px system-ui,sans-serif;color:var(--mut)}
.note{font-size:16px;margin:10px 0;padding:8px 0;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.controls{margin-top:8px}
.controls label{display:inline-flex;gap:4px;align-items:center;padding:5px 10px;border:1px solid var(--line);
border-radius:20px;cursor:pointer;font:13px system-ui,sans-serif;margin-right:6px}
.controls input[type=radio]{accent-color:var(--acc)}
textarea,.rr{width:100%;font:14px Georgia,serif;padding:8px;border:1px solid var(--line);border-radius:5px;margin-top:8px}
.hidden{display:none}
</style></head><body>
<header>
<nav class="breadcrumb" style="font:12px system-ui,sans-serif;margin-bottom:4px"><a href="../../../index.html">Главная</a> › <a href="../../../data/apparatus/">Аппарат Сундараканды</a> › Лексический слой — вердикты судьи</nav>
<h1>__TITLE__</h1>
<div class="bar">
<span id="progress">—</span>
<button onclick="dl()">⬇ Скачать decisions.json</button>
<button onclick="cp()">⧉ Копировать JSON</button>
<button onclick="reset()">↺ Сброс</button>
<span class="vid">Судья РАНЖИРУЕТ, человек ГЕЙТИТ (решение 2: слой в печати). Карточки отсортированы: проблемные вердикты выше, keep — слабые первыми. Оси: Ф достоверность · Н нетривиальность · Л лекс. ценность · Р регистр · А якорь (0–2). Выбор хранится в localStorage.</span>
</div></header>
<main class="container"><div id="app"></div></main>
<script>
const D = /*DATA*/null;
const KEY = "__KEY__";
const dec = JSON.parse(localStorage.getItem(KEY) || "{}");
const $ = (h)=>{const t=document.createElement("template");t.innerHTML=h.trim();return t.content.firstChild;};
function esc(s){return (s||"").replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;");}
function scoreBadge(j){
  if(!j||!j.scores) return "";
  const s=j.scores;
  return `<span class="badge">Ф${s.faithfulness}·Н${s.non_triviality}·Л${s.lexical_value}·Р${s.register}·А${s.anchoring}</span>`;
}
function card(n,i,extra){
  const d=dec[n.key]||{};
  const el=$(`<div class="card g-${n.group||'parked'} ${d.action?('d-'+d.action):''}" id="c${i}"></div>`);
  el.innerHTML=`
    <div class="vid">${esc(n.shloka)} · <b>${esc(n.lemma)}</b>
      <span class="badge">${esc(n.type||'')}</span>
      <span class="badge">${esc(n.source||'')}</span></div>
    <div class="verse">
      <div class="sa">${esc(n.verse_iast)||'<i>стих не найден</i>'}</div>
      <div class="ru">${esc(n.leonov_ru)||''}</div>
    </div>
    ${extra||''}
    ${n.judge?`<div class="why"><b>Судья:</b> вердикт <b>${esc(n.judge.verdict)}</b> ${scoreBadge(n.judge)} — ${esc(n.judge.reason||'')}</div>`:''}
    ${n.reanchored?`<div class="why"><b>Переякорено (H276):</b> ${esc(n.reanchored.from)} → ${esc(n.reanchored.to)}. ${esc(n.reanchored.evidence)}</div>`:''}
    ${n.qa_removed?`<div class="leo"><b>Запарковано (H276 WS-3b):</b> ${esc(n.qa_removed.reason)} (исходный якорь ${esc(n.qa_removed.original_shloka)})</div>`:''}
    ${(n.tier1||[]).length?`<div class="leo"><b>⚠ Леонов/Костина уже комментируют этот стих:</b>${
      n.tier1.map(l=>`<div><span class="who">${esc(l.editor||'Леонов')}:</span> ${esc(l.note).slice(0,220)}</div>`).join("")
    }</div>`:''}
    <div class="note">${esc(n.note_ru)}</div>
    <div class="controls">
      <label><input type="radio" name="a${i}" value="accept"> ✅ принять</label>
      <label><input type="radio" name="a${i}" value="edit"> ✏️ править</label>
      <label><input type="radio" name="a${i}" value="reject"> ❌ отклонить</label>
    </div>
    <textarea class="hidden" id="e${i}" rows="4">${esc(d.edited_note||n.note_ru)}</textarea>
    <input class="rr hidden" id="r${i}" placeholder="Причина отклонения / замечание…" value="${esc(d.reject_reason||'')}">
  `;
  el.querySelectorAll(`input[name=a${i}]`).forEach(r=>{
    if(d.action===r.value) r.checked=true;
    r.onchange=()=>set(i,n.key,r.value);
  });
  return el;
}
let ALL=[];
function render(){
  const app=document.getElementById("app");
  app.innerHTML="";
  ALL=[...D.notes,...D.parked];
  app.appendChild($(`<div class="sec"><b>Итог судьи (Sonnet 5, рубрика §3.4 c осью Л lexical_value):</b> из ${D.total} примечаний — keep ${D.counts.keep} · edit ${D.counts.edit} · park ${D.counts.park} · reject ${D.counts.reject} · flag_anchor ${D.counts.flag_anchor}${D.parked.length?` · отдельно запарковано WS-3b: ${D.parked.length}`:''}</div>`));
  let i=0, lastGroup=null;
  D.notes.forEach(n=>{
    if(n.group!==lastGroup){
      const s=D.sections.find(x=>x.id===n.group);
      if(s) app.appendChild($(`<div class="sec">${s.title} — <b>${s.count}</b></div>`));
      lastGroup=n.group;
    }
    app.appendChild(card(n,i)); wire(i,n); i++;
  });
  if(D.parked.length){
    app.appendChild($(`<div class="sec">🗄 Запарковано WS-3b (фантомные якоря сарги 11) — <b>${D.parked.length}</b>. По умолчанию НЕ в книге; голос «принять» = вернуть с новым якорем (укажите стих в правке).</div>`));
    D.parked.forEach(n=>{app.appendChild(card(n,i)); wire(i,n); i++;});
  }
  prog();
}
function wire(i,n){
  const d=dec[n.key]||{};
  toggle(i,d.action);
}
function toggle(i,action){
  document.getElementById("e"+i).classList.toggle("hidden",action!=="edit");
  document.getElementById("r"+i).classList.toggle("hidden",action!=="reject");
}
function set(i,key,action){
  const rec=dec[key]||{};
  rec.action=action;
  rec.edited_note=document.getElementById("e"+i).value;
  rec.reject_reason=document.getElementById("r"+i).value;
  rec.ts=new Date().toISOString();
  dec[key]=rec;
  document.getElementById("e"+i).oninput=()=>{rec.edited_note=document.getElementById("e"+i).value;save();};
  document.getElementById("r"+i).oninput=()=>{rec.reject_reason=document.getElementById("r"+i).value;save();};
  document.getElementById("c"+i).classList.add("d-"+action);
  toggle(i,action);save();prog();
}
function save(){localStorage.setItem(KEY,JSON.stringify(dec));}
function prog(){
  const done=ALL.filter(n=>dec[n.key]&&dec[n.key].action).length;
  const a=ALL.filter(n=>(dec[n.key]||{}).action==="accept").length;
  const e=ALL.filter(n=>(dec[n.key]||{}).action==="edit").length;
  const r=ALL.filter(n=>(dec[n.key]||{}).action==="reject").length;
  document.getElementById("progress").innerHTML=`<b>${done}/${ALL.length}</b> решено · ✅ ${a} · ✏️ ${e} · ❌ ${r}`;
}
function payload(){return JSON.stringify({generated:D.generated,layer:"lexical",
  reviewer_decisions:dec,reviewed_at:new Date().toISOString()},null,2);}
function dl(){const b=new Blob([payload()],{type:"application/json"});const u=URL.createObjectURL(b);
  const a=document.createElement("a");a.href=u;a.download="lexical_decisions.json";a.click();URL.revokeObjectURL(u);}
function cp(){navigator.clipboard.writeText(payload()).then(()=>alert("JSON скопирован в буфер обмена"));}
function reset(){if(confirm("Сбросить все решения?")){localStorage.removeItem(KEY);for(const k in dec)delete dec[k];render();}}
render();
</script></body></html>"""


if __name__ == "__main__":
    main()

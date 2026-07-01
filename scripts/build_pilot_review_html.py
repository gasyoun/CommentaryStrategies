#!/usr/bin/env python3
"""Build an interactive HTML review page for the Phase-2 pilot notes.

Joins each candidate note with its verse (IAST + Leonov подстрочник), the FULL
commentary at that verse (all three commentators, not only the cited ones),
neighbouring verses' commentary (±2, so the reviewer sees what else is nearby),
and any existing Phase-1 note on the same verse. Emits a self-contained page
(inline JSON + JS) that lets M.G./Kostina click принять / править / отклонить,
persists choices in localStorage, and exports decisions.json — no printing.

Usage: python scripts/build_pilot_review_html.py
Output: data/analysis/phase2_pilot/review.html
"""
import sys
import os
import re
import json

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
PILOT_DIR = os.path.join(REPO, "data", "analysis", "phase2_pilot")
SEG = os.path.join(REPO, "data", "analysis", "sundara_commentary_segmented.json")
BOOK = os.path.join(REPO, "data", "sundara_commentary_to_add.json")
OUT = os.path.join(PILOT_DIR, "review.html")

COMM_LABEL = {"tilaka": "Тилака", "bhusana": "Бхушана", "siromani": "Широмани"}


def vnum(verse):
    return int(verse) if str(verse).isdigit() else None


def parse_vid(vid):
    """'5.35.3' -> (35, '3'); tolerant of merged tokens like '5.35.810'."""
    m = re.match(r"5\.(\d+)\.(.+)", str(vid))
    return (int(m.group(1)), m.group(2)) if m else (None, None)


def main():
    cand = json.load(open(os.path.join(PILOT_DIR, "pilot_candidates.json"), encoding="utf-8"))
    notes = cand["notes"]
    seg = json.load(open(SEG, encoding="utf-8"))
    seg_idx = {b["verse_id"]: b for b in seg["verses"]}

    # Phase-1 existing notes indexed by "5.s.v"
    book = json.load(open(BOOK, encoding="utf-8"))
    bnotes = book["notes"] if isinstance(book, dict) and "notes" in book else book
    p1 = {}
    for n in bnotes:
        m = re.match(r"V\.(\d+)\.(\d+)", str(n.get("shloka", "")))
        if m:
            p1.setdefault(f"5.{int(m.group(1))}.{int(m.group(2))}", []).append(
                {"lemma": n.get("lemma_iast", ""), "note": n.get("note_ru", ""),
                 "type": n.get("type", "")})

    # per-sarga context stats
    stats = {}
    for b in seg["verses"]:
        s = b["sarga"]
        st = stats.setdefault(s, {"verses": 0, "with_commentary": 0})
        st["verses"] += 1
        if b["commentary"]:
            st["with_commentary"] += 1
    for s in stats:
        stats[s]["phase1_notes"] = sum(len(v) for k, v in p1.items() if k.startswith(f"5.{s}."))
        stats[s]["proposed"] = sum(1 for n in notes if parse_vid(n["verse_id"])[0] == s)

    # build review records
    review = []
    for n in notes:
        vid = n["verse_id"]
        s, v = parse_vid(vid)
        bundle = seg_idx.get(vid, {})
        neighbours = []
        base = vnum(v)
        if base is not None:
            for d in (-2, -1, 1, 2):
                nb = seg_idx.get(f"5.{s}.{base + d}")
                if nb and nb.get("commentary"):
                    neighbours.append({
                        "verse_id": nb["verse_id"],
                        "leonov_ru": nb.get("leonov_ru", ""),
                        "commentary": nb.get("commentary", {}),
                    })
        review.append({
            **n,
            "sanskrit_iast": bundle.get("sanskrit_iast", ""),
            "leonov_ru": bundle.get("leonov_ru", ""),
            "commentary_at_verse": bundle.get("commentary", {}),
            "neighbours": neighbours,
            "phase1_here": p1.get(vid, []),
        })

    data = {"generated": cand["_meta"].get("date"), "stats": stats, "notes": review,
            "labels": COMM_LABEL}
    html = PAGE.replace("/*DATA*/null", json.dumps(data, ensure_ascii=False))
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write(html)
    print(f"wrote {OUT} ({len(review)} notes)")


PAGE = r"""<!DOCTYPE html>
<html lang="ru"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Пилот Сундараканды — интерактивная сверка примечаний</title>
<style>
:root{--bg:#faf8f4;--card:#fff;--ink:#222;--mut:#777;--line:#e4ddd0;--acc:#7a5c2e;
--ok:#2e7d32;--edit:#b8860b;--no:#b23b3b;}
*{box-sizing:border-box}
body{font:16px/1.55 Georgia,serif;margin:0;background:var(--bg);color:var(--ink)}
header{position:sticky;top:0;background:#fff;border-bottom:2px solid var(--acc);
padding:12px 20px;z-index:10;box-shadow:0 2px 6px rgba(0,0,0,.06)}
h1{font-size:19px;margin:0 0 4px}
.bar{display:flex;gap:16px;align-items:center;flex-wrap:wrap;font:13px/1.4 system-ui,sans-serif;color:var(--mut)}
.bar b{color:var(--ink)}
button{font:13px system-ui,sans-serif;padding:6px 12px;border:1px solid var(--acc);
background:#fff;color:var(--acc);border-radius:5px;cursor:pointer}
button:hover{background:var(--acc);color:#fff}
main{max-width:920px;margin:0 auto;padding:18px}
.stat{font:12px system-ui,sans-serif;background:#f2ecdd;border:1px solid var(--line);
border-radius:6px;padding:8px 12px;margin:0 0 14px}
.card{background:var(--card);border:1px solid var(--line);border-left:5px solid var(--acc);
border-radius:8px;padding:16px 18px;margin:0 0 18px;box-shadow:0 1px 3px rgba(0,0,0,.05)}
.card.d-accept{border-left-color:var(--ok)}
.card.d-edit{border-left-color:var(--edit)}
.card.d-reject{border-left-color:var(--no);opacity:.75}
.vid{font:12px system-ui,sans-serif;color:var(--mut)}
.badges{display:inline-flex;gap:6px;margin-left:8px}
.badge{font:11px system-ui,sans-serif;padding:1px 7px;border-radius:10px;background:#eee5d3;color:var(--acc)}
.verse{background:#f7f2e8;border-radius:6px;padding:8px 12px;margin:8px 0}
.verse .sa{font-style:italic;color:#4a3f2c}
.verse .ru{color:#333}
.why{background:#fff8e6;border:1px dashed var(--edit);border-radius:6px;padding:6px 10px;
margin:8px 0;font:14px/1.5 system-ui,sans-serif}
.why b{color:var(--edit)}
.note{font-size:17px;margin:10px 0;padding:8px 0;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
details{margin:8px 0;font-size:14px}
summary{cursor:pointer;color:var(--acc);font:13px system-ui,sans-serif}
.comm{margin:6px 0;padding:6px 10px;background:#f6f6f2;border-radius:5px;font-size:13px;line-height:1.5}
.comm.cited{background:#eef6ee;border-left:3px solid var(--ok)}
.comm .who{font:11px system-ui,sans-serif;color:var(--mut);display:block;margin-bottom:2px}
.dev{font-family:"Nirmala UI","Noto Sans Devanagari",serif}
.p1{font-size:13px;color:#555;background:#fbf0f0;border-radius:5px;padding:6px 10px;margin:6px 0}
.controls{margin-top:12px;display:flex;gap:8px;align-items:center;flex-wrap:wrap;
font:13px system-ui,sans-serif}
.controls label{display:inline-flex;gap:4px;align-items:center;padding:5px 10px;border:1px solid var(--line);
border-radius:20px;cursor:pointer}
.controls input[type=radio]{accent-color:var(--acc)}
textarea,.rr{width:100%;font:14px Georgia,serif;padding:8px;border:1px solid var(--line);border-radius:5px;margin-top:8px}
.hidden{display:none}
</style></head><body>
<header>
<h1>Сундараканда · пилот примечаний (песни 35–37) — интерактивная сверка</h1>
<div class="bar">
<span id="progress">—</span>
<button onclick="dl()">⬇ Скачать decisions.json</button>
<button onclick="cp()">⧉ Копировать JSON</button>
<button onclick="reset()">↺ Сброс</button>
<span class="vid">Выбор сохраняется в браузере (localStorage). Каждая карточка: стих · подстрочник · <b>зачем предложено</b> · примечание · санскр. источник (зелёным — использованный) · соседние комментарии · существующие примечания фазы 1.</span>
</div></header>
<main id="app"></main>
<script>
const D = /*DATA*/null;
const KEY = "sundara_pilot_decisions_v1";
const dec = JSON.parse(localStorage.getItem(KEY) || "{}");
const $ = (h)=>{const t=document.createElement("template");t.innerHTML=h.trim();return t.content.firstChild;};
function esc(s){return (s||"").replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;");}

function commBlock(comm, cited){
  return Object.keys(comm||{}).map(c=>{
    const isC = (cited||[]).includes(c);
    return `<div class="comm ${isC?'cited':''}"><span class="who">${D.labels[c]||c}${isC?' · использован':''}</span><span class="dev">${esc(comm[c])}</span></div>`;
  }).join("");
}

function render(){
  const app=document.getElementById("app");
  app.innerHTML="";
  // per-sarga stat header
  Object.keys(D.stats).sort((a,b)=>a-b).forEach(s=>{
    const st=D.stats[s];
    app.appendChild($(`<div class="stat">Песнь ${s}: стихов ${st.verses} · с санскр. комментарием ${st.with_commentary} · существующих примечаний (фаза 1) ${st.phase1_notes} · <b>предложено сейчас ${st.proposed}</b></div>`));
  });
  D.notes.forEach((n,i)=>{
    const d=dec[n.verse_id]||{};
    const card=$(`<div class="card ${d.action?('d-'+d.action):''}" id="c${i}"></div>`);
    card.innerHTML=`
      <div class="vid">${n.verse_id}
        <span class="badges"><span class="badge">${n.kazansky_type}</span>
        <span class="badge">${(n.source_commentary||[]).map(c=>D.labels[c]||c).join(', ')}</span></span></div>
      <div class="verse">
        <div class="sa dev">${esc(n.sanskrit_iast)||'<i>—</i>'}</div>
        <div class="ru">${esc(n.leonov_ru)||'<i>подстрочник не найден</i>'}</div>
      </div>
      <div class="why"><b>Зачем предложено:</b> ${esc(n.why_proposed)}</div>
      <div class="note" contenteditable="false">${esc(n.note_ru)}</div>
      <details><summary>Санскритский источник (все комментаторы к этому стиху)</summary>${commBlock(n.commentary_at_verse,n.source_commentary)}</details>
      ${n.neighbours.length?`<details><summary>Соседние стихи (±2) — что рядом комментируется</summary>${
        n.neighbours.map(nb=>`<div class="p1"><b>${nb.verse_id}</b> ${esc(nb.leonov_ru).slice(0,140)}</div>${commBlock(nb.commentary,[])}`).join("")
      }</details>`:''}
      ${n.phase1_here.length?`<div class="p1"><b>Уже есть (фаза 1) на этом стихе:</b> ${n.phase1_here.map(p=>esc(p.lemma)+' — '+esc(p.note).slice(0,120)).join(' · ')}</div>`:''}
      <div class="controls">
        <label><input type="radio" name="a${i}" value="accept"> ✅ принять</label>
        <label><input type="radio" name="a${i}" value="edit"> ✏️ править</label>
        <label><input type="radio" name="a${i}" value="reject"> ❌ отклонить</label>
      </div>
      <textarea class="hidden" id="e${i}" rows="3">${esc(d.edited_note||n.note_ru)}</textarea>
      <input class="rr hidden" id="r${i}" placeholder="Причина отклонения / замечание…" value="${esc(d.reject_reason||'')}">
    `;
    app.appendChild(card);
    // wire
    card.querySelectorAll(`input[name=a${i}]`).forEach(r=>{
      if(d.action===r.value) r.checked=true;
      r.onchange=()=>set(i,n.verse_id,r.value);
    });
    toggle(i,d.action);
  });
  prog();
}
function toggle(i,action){
  document.getElementById("e"+i).classList.toggle("hidden",action!=="edit");
  document.getElementById("r"+i).classList.toggle("hidden",action!=="reject");
}
function set(i,vid,action){
  const rec=dec[vid]||{};
  rec.action=action;
  rec.edited_note=document.getElementById("e"+i).value;
  rec.reject_reason=document.getElementById("r"+i).value;
  rec.ts=new Date().toISOString();
  dec[vid]=rec;
  document.getElementById("e"+i).oninput=()=>{rec.edited_note=document.getElementById("e"+i).value;save();};
  document.getElementById("r"+i).oninput=()=>{rec.reject_reason=document.getElementById("r"+i).value;save();};
  document.getElementById("c"+i).className="card d-"+action;
  toggle(i,action);save();prog();
}
function save(){localStorage.setItem(KEY,JSON.stringify(dec));}
function prog(){
  const done=D.notes.filter(n=>dec[n.verse_id]&&dec[n.verse_id].action).length;
  const a=D.notes.filter(n=>(dec[n.verse_id]||{}).action==="accept").length;
  const e=D.notes.filter(n=>(dec[n.verse_id]||{}).action==="edit").length;
  const r=D.notes.filter(n=>(dec[n.verse_id]||{}).action==="reject").length;
  document.getElementById("progress").innerHTML=`<b>${done}/${D.notes.length}</b> решено · ✅ ${a} · ✏️ ${e} · ❌ ${r}`;
}
function payload(){return JSON.stringify({generated:D.generated,reviewer_decisions:dec,
  reviewed_at:new Date().toISOString()},null,2);}
function dl(){const b=new Blob([payload()],{type:"application/json"});const u=URL.createObjectURL(b);
  const a=document.createElement("a");a.href=u;a.download="decisions.json";a.click();URL.revokeObjectURL(u);}
function cp(){navigator.clipboard.writeText(payload()).then(()=>alert("JSON скопирован в буфер обмена"));}
function reset(){if(confirm("Сбросить все решения?")){localStorage.removeItem(KEY);for(const k in dec)delete dec[k];render();}}
render();
</script></body></html>"""


if __name__ == "__main__":
    main()

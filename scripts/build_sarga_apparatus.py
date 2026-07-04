#!/usr/bin/env python3
"""Build the unified per-sarga apparatus view (H141, ruling R3, roadmap §5 п.6).

One interactive HTML page per sarga merging all FIVE note sources per verse,
with provenance badges and review-status badges:

  1. tier1     — Leonov/Kostina own notes (data/leonov_own_notes.json) —
                 authoritative, display-only, NO vote control;
  2. lexical   — Phase-1 lexical layer: book-level data/sundara_commentary_to_add.json
                 (subtype != cross_text) ∪ data/lexical/ch{N}.json, deduped on
                 (shloka, lemma_iast);
  3. phase2    — Phase-2 pilot candidates (data/analysis/phase2_pilot/pilot_candidates.json),
                 «ожидает гейта М.Г.» until H142 applies decisions.json;
  4. edition   — edition-footnote candidates (data/edition_footnotes/candidates.json,
                 candidates + single_verse_absences), gate-pending;
  5. crosstext — hand-curated clusters (data/crosstext/*.json) ∪ the DCS archive layer
                 REMAPPED to the vulgate (data/crosstext/archive_parallels_vulgate.json —
                 run scripts/remap_archive_parallels.py first).

Where a candidate collides with a tier-1 note on the same verse the tier-1 note is
shown adjacent and the collision is flagged (pattern from phase2_pilot/review.html).
Vote controls on all non-tier-1 items, persisted in localStorage, exported via
«Скачать decisions.json».

Usage:  python scripts/build_sarga_apparatus.py [sarga ...]     (default: 35 36 37)
Output: data/apparatus/sarga_{NN}.html + sarga_{NN}.json
"""
import sys
import os
import re
import json
import glob

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
DATA = os.path.join(REPO, "data")
OUTDIR = os.path.join(DATA, "apparatus")

SEG = os.path.join(DATA, "analysis", "sundara_commentary_segmented.json")
LEONOV = os.path.join(DATA, "leonov_own_notes.json")
BOOK = os.path.join(DATA, "sundara_commentary_to_add.json")
PILOT = os.path.join(DATA, "analysis", "phase2_pilot", "pilot_candidates.json")
FOOTNOTES = os.path.join(DATA, "edition_footnotes", "candidates.json")
ARCHIVE_V = os.path.join(DATA, "crosstext", "archive_parallels_vulgate.json")

LAYER_LABEL = {
    "tier1": "ярус 1 · Леонов/Костина",
    "lexical": "Фаза 1 · лексич.",
    "phase2": "Фаза 2 · комментаторы",
    "edition": "издания · сноска",
    "crosstext": "cross-text",
}
LAYER_ORDER = ["tier1", "lexical", "phase2", "edition", "crosstext"]
COMM_LABEL = {"tilaka": "Тилака", "bhusana": "Бхушана", "siromani": "Широмани"}


def shloka_to_vid(shloka):
    """'V.35.8' -> '5.35.8' (single-verse refs only, else None)."""
    m = re.match(r"^V\.(\d+)\.(\d+)$", str(shloka).strip())
    return f"5.{int(m.group(1))}.{int(m.group(2))}" if m else None


def shloka_sarga_first_verse(shloka):
    """Any 'V.35.8,10' / 'V.35.3–7' ref -> (sarga, first_verse) or (None, None)."""
    m = re.match(r"^V\.(\d+)\.(\d+)", str(shloka).strip())
    return (int(m.group(1)), int(m.group(2))) if m else (None, None)


def load_sources():
    seg = json.load(open(SEG, encoding="utf-8"))
    seg_idx = {v["verse_id"]: v for v in seg["verses"]}

    leonov = {}
    for n in json.load(open(LEONOV, encoding="utf-8"))["notes"]:
        leonov.setdefault(n["verse_id"], []).append(n)

    # Phase-1 lexical: book aggregate (minus its cross_text slice) ∪ per-chapter files
    book = json.load(open(BOOK, encoding="utf-8"))
    bnotes = book["notes"] if isinstance(book, dict) and "notes" in book else book
    lexical, seen_lex = {}, set()
    for n in bnotes:
        # commentator-subtype notes are the gated Phase-2 layer (they enter the
        # book aggregate via apply_phase2_decisions.py) — shown in the phase2
        # layer, not duplicated here
        if "_meta" in n or n.get("subtype") in ("cross_text", "commentator"):
            continue
        vid = shloka_to_vid(n.get("shloka", ""))
        if not vid:
            continue
        key = (n.get("shloka"), n.get("lemma_iast"))
        seen_lex.add(key)
        lexical.setdefault(vid, []).append(n)
    for path in sorted(glob.glob(os.path.join(DATA, "lexical", "ch*.json"))):
        if ".rejected" in path:
            continue
        for n in json.load(open(path, encoding="utf-8")):
            if "_meta" in n:
                continue
            key = (n.get("shloka"), n.get("lemma_iast"))
            vid = shloka_to_vid(n.get("shloka", ""))
            if vid and key not in seen_lex:
                seen_lex.add(key)
                lexical.setdefault(vid, []).append(n)

    pilot = {}
    phase2_files = [PILOT] + sorted(
        glob.glob(os.path.join(DATA, "analysis", "phase2_batch*", "batch*_candidates.json")))
    for path in phase2_files:
        if not os.path.exists(path):
            continue
        doc = json.load(open(path, encoding="utf-8"))
        for n in doc.get("notes", []):
            pilot.setdefault(n["verse_id"], []).append(n)

    fd = json.load(open(FOOTNOTES, encoding="utf-8"))
    edition = {}
    for n in fd.get("candidates", []) + fd.get("single_verse_absences", []):
        edition.setdefault(n["anchor"], []).append(n)

    # cross-text: hand-curated clusters (vulgate numbering) + remapped archive layer
    crosstext, seen_ct = {}, set()
    for path in sorted(glob.glob(os.path.join(DATA, "crosstext", "*.json"))):
        base = os.path.basename(path)
        if (".rejected" in base or base.startswith("_")
                or base.startswith("archive_parallels")):
            continue
        d = json.load(open(path, encoding="utf-8"))
        items = d if isinstance(d, list) else d.get("notes", [])
        cluster_label = ""
        for e in items:
            if "_meta" in e:
                cluster_label = e["_meta"].get("cluster_label", "")
                continue
            s, v = shloka_sarga_first_verse(e.get("shloka", ""))
            if s is None:
                continue
            key = (e.get("shloka"), e.get("lemma_iast"))
            seen_ct.add(key)
            rec = dict(e)
            rec["_cluster"] = base.replace(".json", "")
            rec["_cluster_label"] = cluster_label
            crosstext.setdefault(f"5.{s}.{v}", []).append(rec)
    if os.path.exists(ARCHIVE_V):
        for e in json.load(open(ARCHIVE_V, encoding="utf-8")):
            if "_meta" in e:
                continue
            s, v = shloka_sarga_first_verse(e.get("shloka", ""))
            if s is None:
                continue
            key = (e.get("shloka"), e.get("lemma_iast"))
            if key in seen_ct:
                continue
            rec = dict(e)
            rec["_cluster"] = "archive_parallels"
            rec["_cluster_label"] = "DCS parallel-search (archive.sqlite)"
            crosstext.setdefault(f"5.{s}.{v}", []).append(rec)
    else:
        print("WARN: run scripts/remap_archive_parallels.py first — archive layer skipped")

    return seg, seg_idx, leonov, lexical, pilot, edition, crosstext


def mk_note(layer, vid, idx, src):
    """Normalize a source record to the apparatus note schema."""
    n = {
        "id": f"{layer}:{vid}:{idx}",
        "layer": layer,
        "layer_label": LAYER_LABEL[layer],
        "votable": layer != "tier1",
    }
    if layer == "tier1":
        n.update({
            "status": "принято (печать)",
            "editor": src.get("editor") or "Леонов",
            "note_ru": src.get("raw_text", ""),
        })
    elif layer == "lexical":
        n.update({
            "status": "review_required" if src.get("review_required") else "принято",
            "lemma_iast": src.get("lemma_iast", ""),
            "note_ru": src.get("note_ru", ""),
            "type": src.get("type", ""),
            "subtype": src.get("subtype", ""),
            "trigger": src.get("trigger", ""),
            "source": src.get("source", ""),
        })
    elif layer == "phase2":
        gate = src.get("gate") or {}
        if gate.get("action") in ("accept", "edit"):
            status = f"принято гейтом М.Г. ({gate.get('gated_date', '')})"
        elif gate.get("action") == "reject":
            status = f"отклонено М.Г.: {gate.get('reject_reason', '')}"
        else:
            status = "ожидает гейта М.Г."
        n.update({
            "status": status,
            "mg_comment": gate.get("mg_comment", ""),
            "lemma_iast": src.get("lemma_iast", ""),
            "note_ru": src.get("note_ru", ""),
            "type": src.get("kazansky_type", ""),
            "source_commentary": src.get("source_commentary", []),
            "why_proposed": src.get("why_proposed", ""),
            "provenance": src.get("provenance", {}),
        })
        if gate.get("action"):          # already gated — no second vote control
            n["votable"] = False
    elif layer == "edition":
        n.update({
            "status": "ожидает гейта М.Г.",
            "note_ru": src.get("note_ru", ""),
            "kind": src.get("kind", ""),
            "range": src.get("range", ""),
            "confidence": src.get("confidence", ""),
            "verses_iast": src.get("verses_iast", []),
        })
    elif layer == "crosstext":
        n.update({
            "status": "review_required" if src.get("review_required", True)
                      else "принято",
            "lemma_iast": src.get("lemma_iast", ""),
            "note_ru": src.get("note_ru", ""),
            "type": src.get("type", ""),
            "cluster": src.get("_cluster", ""),
            "cluster_label": src.get("_cluster_label", ""),
            "shloka_ref": src.get("shloka", ""),
            "work_label": src.get("work_label", ""),
            "verse_address": src.get("verse_address", ""),
            "parallel_sa_iast": src.get("parallel_sa_iast", ""),
            "sundara_sa_iast": src.get("sundara_sa_iast", ""),
            "quality": src.get("quality", ""),
            "source": src.get("source", ""),
        })
        if src.get("_cluster") == "archive_parallels":
            n["edition_flag"] = src.get("edition", "")
            n["shloka_critical"] = src.get("shloka_critical", "")
            n["verse_address_vulgate"] = src.get("verse_address_vulgate", "")
    return n


def coverage_map(verses):
    """verse-number -> verse record, understanding merged tokens like '4347' (=43–47).

    The segmented corpus merges some verse bundles into concatenated ids
    ('5.35.7072' covers 70–72); a note anchored at 5.35.70 must attach there,
    not vanish. Exact single-number tokens always win over merged ranges.
    """
    cov = {}
    # pass 1: exact numeric tokens
    for v in verses:
        tok = str(v["verse"])
        if tok.isdigit() and len(tok) <= 3:
            cov.setdefault(int(tok), v)
    # pass 2: merged even-length tokens split into (start, end)
    for v in verses:
        tok = str(v["verse"])
        if tok.isdigit() and len(tok) >= 4 and len(tok) % 2 == 0:
            half = len(tok) // 2
            a, b = int(tok[:half]), int(tok[half:])
            if a < b and b - a < 20:
                for n in range(a, b + 1):
                    cov.setdefault(n, v)
    return cov


def build_sarga(sarga, seg, seg_idx, leonov, lexical, pilot, edition, crosstext):
    verses = sorted((v for v in seg["verses"] if v["sarga"] == sarga),
                    key=lambda v: int(v["verse"]) if str(v["verse"]).isdigit() else 0)
    cov = coverage_map(verses)
    sources = {"tier1": leonov, "lexical": lexical, "phase2": pilot,
               "edition": edition, "crosstext": crosstext}

    # attach every note of this sarga to its verse record — exact id, then
    # numeric coverage (merged bundles), then a synthetic card (never drop)
    attached = {}   # display verse_id -> {layer: [(anchor_vid, src), ...]}
    synthetic = {}  # display verse_id -> verse number (for ordering)
    prefix = f"5.{sarga}."
    for layer, pool in sources.items():
        for vid, items in pool.items():
            if not vid.startswith(prefix):
                continue
            if vid in seg_idx and seg_idx[vid]["sarga"] == sarga:
                disp = vid
            else:
                num = vid[len(prefix):]
                hit = cov.get(int(num)) if num.isdigit() else None
                if hit is not None:
                    disp = hit["verse_id"]
                else:
                    disp = vid
                    synthetic[vid] = int(num) if num.isdigit() else 0
            for src in items:
                attached.setdefault(disp, {}).setdefault(layer, []).append((vid, src))

    display = list(verses)
    for vid, num in sorted(synthetic.items(), key=lambda kv: kv[1]):
        display.append({"verse_id": vid, "verse": num, "sarga": sarga,
                        "sanskrit_iast": "", "leonov_ru": "", "commentary": {},
                        "_synthetic": True})
    display.sort(key=lambda v: int(v["verse"]) if str(v["verse"]).isdigit()
                 and len(str(v["verse"])) <= 3 else int(str(v["verse"])[:2]))

    out_verses, stats = [], {k: 0 for k in LAYER_ORDER}
    for v in display:
        vid = v["verse_id"]
        pools = attached.get(vid, {})
        notes = []
        for layer in LAYER_ORDER:
            for i, (anchor, src) in enumerate(pools.get(layer, [])):
                note = mk_note(layer, vid, i, src)
                if anchor != vid:
                    note["anchor_verse_id"] = anchor
                notes.append(note)
                stats[layer] += 1
        if not notes:
            continue
        has_tier1 = bool(pools.get("tier1"))
        for n in notes:
            if n["votable"] and has_tier1:
                n["collision_tier1"] = True
        rec = {
            "verse_id": vid,
            "verse": v["verse"],
            "sanskrit_iast": v.get("sanskrit_iast", ""),
            "leonov_ru": v.get("leonov_ru", ""),
            "commentary": v.get("commentary", {}),
            "has_tier1": has_tier1,
            "notes": notes,
        }
        if v.get("_synthetic"):
            rec["verse_not_segmented"] = True
        out_verses.append(rec)
    return {
        "_meta": {
            "generated_by": "scripts/build_sarga_apparatus.py",
            "handoff": "H141 — сводный per-sarga аппарат (roadmap §5 п.6, ruling R3)",
            "sarga": sarga,
            "numbering": "southern vulgate (Leonov); archive cross-text layer remapped "
                         "from critical via scripts/remap_archive_parallels.py",
            "sources": {k: LAYER_LABEL[k] for k in LAYER_ORDER},
            "verses_total": len(verses),
            "verses_with_notes": len(out_verses),
            "notes_by_layer": stats,
        },
        "sarga": sarga,
        "verses": out_verses,
    }


def main():
    args = [int(a) for a in sys.argv[1:]] or [35, 36, 37]
    os.makedirs(OUTDIR, exist_ok=True)
    seg, seg_idx, leonov, lexical, pilot, edition, crosstext = load_sources()
    for sarga in args:
        data = build_sarga(sarga, seg, seg_idx, leonov, lexical, pilot,
                           edition, crosstext)
        jpath = os.path.join(OUTDIR, f"sarga_{sarga:02d}.json")
        with open(jpath, "w", encoding="utf-8") as fh:
            json.dump(data, fh, ensure_ascii=False, indent=2)
        payload = dict(data)
        payload["labels"] = COMM_LABEL
        blob = json.dumps(payload, ensure_ascii=False).replace("</", "<\\/")
        html = (PAGE.replace("/*DATA*/null", blob)
                    .replace("{SARGA}", str(sarga)))
        hpath = os.path.join(OUTDIR, f"sarga_{sarga:02d}.html")
        with open(hpath, "w", encoding="utf-8") as fh:
            fh.write(html)
        m = data["_meta"]
        print(f"sarga {sarga}: {m['verses_with_notes']}/{m['verses_total']} verses "
              f"with notes, by layer {m['notes_by_layer']} -> {hpath}")


PAGE = r"""<!DOCTYPE html>
<html lang="ru"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Сундараканда · песнь {SARGA} — сводный аппарат (5 источников)</title>
<link rel="stylesheet" href="../../css/commentary.css">
<style>
:root{--bg:#faf8f4;--card:#fff;--ink:#222;--mut:#777;--line:#e4ddd0;--acc:#7a5c2e;
--ok:#2e7d32;--edit:#b8860b;--no:#b23b3b;--t1:#8b2f2f;--lex:#2e5d7d;--p2:#6a4fa0;
--ed:#8a6d1f;--ct:#3e7d5c;}
*{box-sizing:border-box}
body{font:16px/1.55 Georgia,serif;margin:0;background:var(--bg);color:var(--ink)}
header{position:sticky;top:0;background:#fff;border-bottom:2px solid var(--acc);
padding:12px 20px;z-index:10;box-shadow:0 2px 6px rgba(0,0,0,.06)}
h1{font-size:19px;margin:0 0 4px}
.breadcrumb{font:12px system-ui,sans-serif;color:var(--mut);margin:0 0 4px}
.breadcrumb a{color:var(--acc)}
.bar{display:flex;gap:14px;align-items:center;flex-wrap:wrap;font:13px/1.4 system-ui,sans-serif;color:var(--mut)}
.bar b{color:var(--ink)}
button{font:13px system-ui,sans-serif;padding:6px 12px;border:1px solid var(--acc);
background:#fff;color:var(--acc);border-radius:5px;cursor:pointer}
button:hover{background:var(--acc);color:#fff}
main{max-width:960px;margin:0 auto;padding:18px}
.legend{font:12px system-ui,sans-serif;background:#f2ecdd;border:1px solid var(--line);
border-radius:6px;padding:8px 12px;margin:0 0 14px;line-height:2}
.vcard{background:var(--card);border:1px solid var(--line);border-radius:8px;
padding:14px 18px;margin:0 0 20px;box-shadow:0 1px 3px rgba(0,0,0,.05)}
.vhead{font:13px system-ui,sans-serif;color:var(--mut);margin-bottom:6px}
.vhead b{font-size:15px;color:var(--ink)}
.verse{background:#f7f2e8;border-radius:6px;padding:8px 12px;margin:6px 0 10px}
.verse .sa{font-style:italic;color:#4a3f2c}
.verse .ru{color:#333}
.note{border:1px solid var(--line);border-left:5px solid var(--acc);border-radius:6px;
padding:10px 12px;margin:10px 0}
.note.l-tier1{border-left-color:var(--t1);background:#fdf6f6}
.note.l-lexical{border-left-color:var(--lex)}
.note.l-phase2{border-left-color:var(--p2)}
.note.l-edition{border-left-color:var(--ed);background:#fbf8ef}
.note.l-crosstext{border-left-color:var(--ct)}
.note.d-accept{outline:2px solid var(--ok)}
.note.d-edit{outline:2px solid var(--edit)}
.note.d-reject{opacity:.6;outline:2px solid var(--no)}
.badge{font:11px system-ui,sans-serif;padding:1px 8px;border-radius:10px;
background:#eee5d3;color:var(--acc);margin-right:5px;white-space:nowrap}
.badge.b-tier1{background:var(--t1);color:#fff}
.badge.b-lexical{background:var(--lex);color:#fff}
.badge.b-phase2{background:var(--p2);color:#fff}
.badge.b-edition{background:var(--ed);color:#fff}
.badge.b-crosstext{background:var(--ct);color:#fff}
.badge.b-status{background:#fff;border:1px solid var(--line);color:var(--mut)}
.badge.b-gate{background:#fff3cd;border:1px solid var(--edit);color:#7a5c00}
.badge.b-crit{background:#f8d7da;border:1px solid var(--no);color:#842029}
.lemma{font-style:italic;color:var(--acc)}
.ntext{margin:6px 0 0;font-size:15px}
.collide{font:12px system-ui,sans-serif;background:#fff0f0;border:1px dashed var(--no);
color:var(--no);border-radius:5px;padding:3px 8px;margin:6px 0 0;display:inline-block}
.meta{font:12px system-ui,sans-serif;color:var(--mut);margin-top:4px}
.par{background:#f2f7f4;border-radius:5px;padding:6px 10px;margin:6px 0 0;font-size:13px}
.par .sa{font-style:italic}
details{margin:6px 0 0;font-size:13px}
summary{cursor:pointer;color:var(--acc);font:12px system-ui,sans-serif}
.comm{margin:5px 0;padding:5px 9px;background:#f6f6f2;border-radius:5px;font-size:13px}
.comm .who{font:11px system-ui,sans-serif;color:var(--mut);display:block}
.dev{font-family:"Nirmala UI","Noto Sans Devanagari",serif}
.controls{margin-top:8px;display:flex;gap:8px;align-items:center;flex-wrap:wrap;
font:13px system-ui,sans-serif}
.controls label{display:inline-flex;gap:4px;align-items:center;padding:4px 10px;
border:1px solid var(--line);border-radius:20px;cursor:pointer}
.controls input[type=radio]{accent-color:var(--acc)}
textarea,.rr{width:100%;font:14px Georgia,serif;padding:8px;border:1px solid var(--line);
border-radius:5px;margin-top:6px}
.hidden{display:none}
</style></head><body>
<header>
<div class="breadcrumb"><a href="../../index.html">Commentary Strategies</a> › Сундараканда · сводный аппарат</div>
<h1>Песнь {SARGA} — сводный аппарат из 5 источников (пилот H141)</h1>
<div class="bar">
<span id="progress">—</span>
<button onclick="dl()">⬇ Скачать decisions.json</button>
<button onclick="cp()">⧉ Копировать JSON</button>
<button onclick="reset()">↺ Сброс</button>
<span>Нумерация — южная вульгата (перевод М. Леонова). Голосование сохраняется в браузере (localStorage); ярус 1 — только показ, без голосования.</span>
</div></header>
<main class="container"><div id="app"></div></main>
<script>
const D = /*DATA*/null;
const KEY = "sundara_apparatus_s{SARGA}_v1";
const dec = JSON.parse(localStorage.getItem(KEY) || "{}");
const $ = (h)=>{const t=document.createElement("template");t.innerHTML=h.trim();return t.content.firstChild;};
function esc(s){return (s||"").replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;");}
const STATUS_CLS = s => s==="ожидает гейта М.Г." ? "b-gate" : "b-status";

function commBlock(comm){
  return Object.keys(comm||{}).map(c=>`<div class="comm"><span class="who">${D.labels[c]||c}</span><span class="dev">${esc(comm[c])}</span></div>`).join("");
}

function noteHtml(n,vi,ni){
  const d=dec[n.id]||{};
  const badges=[`<span class="badge b-${n.layer}">${esc(n.layer_label)}</span>`,
    `<span class="badge ${STATUS_CLS(n.status)}">${esc(n.status)}</span>`];
  if(n.layer==="tier1"&&n.editor) badges.push(`<span class="badge b-status">${esc(n.editor)}</span>`);
  if(n.type) badges.push(`<span class="badge b-status">тип ${esc(n.type)}</span>`);
  if(n.cluster_label) badges.push(`<span class="badge b-status">${esc(n.cluster_label)}</span>`);
  if(n.quality) badges.push(`<span class="badge b-status">${esc(n.quality)}</span>`);
  if(n.edition_flag && n.edition_flag!=="vulgate")
    badges.push(`<span class="badge b-crit">⚠ нумерация: ${esc(n.edition_flag)} (${esc(n.shloka_critical)})</span>`);
  let body="";
  if(n.lemma_iast) body+=`<span class="lemma">${esc(n.lemma_iast)}</span> — `;
  body+=esc(n.note_ru||"");
  let extra="";
  if(n.why_proposed) extra+=`<div class="meta"><b>Зачем предложено:</b> ${esc(n.why_proposed)}</div>`;
  if(n.mg_comment) extra+=`<div class="meta"><b>Ремарка М.Г.:</b> ${esc(n.mg_comment)}</div>`;
  if(n.layer==="crosstext"&&n.parallel_sa_iast){
    extra+=`<div class="par"><b>${esc(n.work_label||"")}</b> ${esc(n.verse_address||"")}${n.verse_address_vulgate?` · ${esc(n.verse_address_vulgate)}`:""}<br><span class="sa">${esc(n.parallel_sa_iast)}</span></div>`;
  }
  if(n.layer==="edition"&&(n.verses_iast||[]).length){
    extra+=`<details><summary>Текст отсутствующих в критическом издании шлок</summary>${
      n.verses_iast.map(v=>`<div class="par"><b>${esc(v.verse_id)}</b> <span class="sa">${esc(v.iast)}</span></div>`).join("")}</details>`;
  }
  if(n.source) extra+=`<div class="meta">Источник: ${esc(n.source)}</div>`;
  if((n.source_commentary||[]).length) extra+=`<div class="meta">Комментаторы: ${n.source_commentary.map(c=>D.labels[c]||c).join(", ")}</div>`;
  const collide=n.collision_tier1?`<div class="collide">⚠ на этом стихе уже есть примечание яруса 1 (Леонов/Костина) — см. выше, проверьте на дублирование</div>`:"";
  const controls=n.votable?`
    <div class="controls">
      <label><input type="radio" name="a_${n.id}" value="accept"> ✅ принять</label>
      <label><input type="radio" name="a_${n.id}" value="edit"> ✏️ править</label>
      <label><input type="radio" name="a_${n.id}" value="reject"> ❌ отклонить</label>
    </div>
    <textarea class="hidden" id="e_${n.id}" rows="3">${esc(d.edited_note||n.note_ru||"")}</textarea>
    <input class="rr hidden" id="r_${n.id}" placeholder="Причина отклонения / замечание…" value="${esc(d.reject_reason||"")}">`:"";
  return `<div class="note l-${n.layer} ${d.action?("d-"+d.action):""}" id="n_${n.id}">
    <div>${badges.join("")}</div>
    <div class="ntext">${body}</div>${extra}${collide}${controls}</div>`;
}

function render(){
  const app=document.getElementById("app");
  app.innerHTML="";
  const m=D._meta, bl=m.notes_by_layer, L=m.sources;
  app.appendChild($(`<div class="legend"><b>Песнь ${D.sarga}</b>: стихов ${m.verses_total}, с примечаниями ${m.verses_with_notes}. Слои: <span class="badge b-tier1">${L.tier1}</span> ${bl.tier1} (без голосования) · <span class="badge b-lexical">${L.lexical}</span> ${bl.lexical} · <span class="badge b-phase2">${L.phase2}</span> ${bl.phase2} · <span class="badge b-edition">${L.edition}</span> ${bl.edition} · <span class="badge b-crosstext">${L.crosstext}</span> ${bl.crosstext}. Статус <span class="badge b-gate">ожидает гейта М.Г.</span> — решение по пилоту (H142) ещё не применено.</div>`));
  D.verses.forEach((v,vi)=>{
    const card=$(`<div class="vcard"></div>`);
    card.innerHTML=`
      <div class="vhead"><b>${v.verse_id}</b>${v.has_tier1?' · <span class="badge b-tier1">есть примечание яруса 1</span>':''}</div>
      <div class="verse">
        <div class="sa dev">${esc(v.sanskrit_iast)||'<i>—</i>'}</div>
        <div class="ru">${esc(v.leonov_ru)||'<i>подстрочник не найден</i>'}</div>
      </div>
      ${Object.keys(v.commentary||{}).length?`<details><summary>Санскритские комментаторы к стиху</summary>${commBlock(v.commentary)}</details>`:''}
      ${v.notes.map((n,ni)=>noteHtml(n,vi,ni)).join("")}`;
    app.appendChild(card);
    v.notes.filter(n=>n.votable).forEach(n=>{
      const d=dec[n.id]||{};
      card.querySelectorAll(`input[name="a_${CSS.escape(n.id)}"]`).forEach(r=>{
        if(d.action===r.value) r.checked=true;
        r.onchange=()=>set(n,r.value);
      });
      toggle(n.id,d.action);
    });
  });
  prog();
}
function toggle(id,action){
  const e=document.getElementById("e_"+id),r=document.getElementById("r_"+id);
  if(e)e.classList.toggle("hidden",action!=="edit");
  if(r)r.classList.toggle("hidden",action!=="reject");
}
function set(n,action){
  const id=n.id,rec=dec[id]||{};
  rec.action=action;
  rec.verse_id=n.verse_id||id.split(":")[1];
  rec.layer=n.layer;
  if(n.lemma_iast)rec.lemma_iast=n.lemma_iast;
  const e=document.getElementById("e_"+id),r=document.getElementById("r_"+id);
  rec.edited_note=e?e.value:"";
  rec.reject_reason=r?r.value:"";
  rec.ts=new Date().toISOString();
  dec[id]=rec;
  if(e)e.oninput=()=>{rec.edited_note=e.value;save();};
  if(r)r.oninput=()=>{rec.reject_reason=r.value;save();};
  const el=document.getElementById("n_"+id);
  el.className=el.className.replace(/\bd-(accept|edit|reject)\b/g,"").trim()+" d-"+action;
  toggle(id,action);save();prog();
}
function allVotable(){const a=[];D.verses.forEach(v=>v.notes.forEach(n=>{if(n.votable)a.push(n);}));return a;}
function save(){localStorage.setItem(KEY,JSON.stringify(dec));}
function prog(){
  const all=allVotable();
  const done=all.filter(n=>dec[n.id]&&dec[n.id].action).length;
  const a=all.filter(n=>(dec[n.id]||{}).action==="accept").length;
  const e=all.filter(n=>(dec[n.id]||{}).action==="edit").length;
  const r=all.filter(n=>(dec[n.id]||{}).action==="reject").length;
  document.getElementById("progress").innerHTML=`<b>${done}/${all.length}</b> решено · ✅ ${a} · ✏️ ${e} · ❌ ${r}`;
}
function payload(){
  return JSON.stringify({sarga:D.sarga,generated_by:D._meta.generated_by,
    decisions:dec,reviewed_at:new Date().toISOString()},null,2);
}
function dl(){const b=new Blob([payload()],{type:"application/json"});const u=URL.createObjectURL(b);
  const a=document.createElement("a");a.href=u;a.download="decisions_sarga_"+D.sarga+".json";a.click();URL.revokeObjectURL(u);}
function cp(){navigator.clipboard.writeText(payload()).then(()=>alert("JSON скопирован в буфер обмена"));}
function reset(){if(confirm("Сбросить все решения по этой песни?")){localStorage.removeItem(KEY);for(const k in dec)delete dec[k];render();}}
// verse_id onto each note for the export
D.verses.forEach(v=>v.notes.forEach(n=>n.verse_id=v.verse_id));
render();
</script></body></html>"""


if __name__ == "__main__":
    main()

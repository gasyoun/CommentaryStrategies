#!/usr/bin/env python3
"""H1685 step 5 — the human's blind spot-check of the ADJUDICATOR.

Ruling В2 spends the human's minutes on verifying the adjudicator rather than
re-deciding 1 889 cards. So this sheet does not show what the adjudicator (or
the earlier Sonnet judge) decided: it shows the card and the evidence, asks the
reviewer for their own verdict in the same vocabulary, and only afterwards is
the comparison computed (scripts/h1685_score_spotcheck.py). A sheet that
displayed the verdict would measure agreement-under-anchoring, not precision.

SIZING — derived, not chosen. For a stratum checked clean (k = n), the Wilson
95 % lower bound on precision is exactly n / (n + z²), z = 1.96. So

    n = 16  ->  lower bound 0.806        n = 10  ->  0.722
    n = 20  ->  0.839                    n = 30  ->  0.887

16 is the smallest n whose clean sweep certifies a stratum at ≥ 0.80, which is
the bar this queue's downstream use (a printed critical apparatus) needs. Every
stratum of ≥ 16 cards therefore gets 16; a stratum smaller than that is
censused in full. Nothing is rounded toward a nicer total.

STRATA — one per way the adjudicator could be wrong, not per queue:
  A rule/FN-ABS-OK    absence confirmed by the global critical re-search
  B rule/FN-VAR-OK    variant confirmed by locating both readings
  C rule/NOTE-KEEP    accepted on judge-keep + three clean independent checks
                      (the rubber-stamp risk: the largest rule stratum)
  D opus/accept       read individually and accepted
  E opus/reject       read and rejected — destroys content, so it is measured
  F opus/edit         read and sent back for a named fix
  G opus/park         read and held (non-triviality, or a key collision)
  H opus/flag_anchor  read and blocked pending re-anchoring
  I rule/FN-VAR-NULL  rejected as an orthographic non-difference

Sampling is seeded (1685) and reproducible.

Output: data/analysis/h1685_adjudication/
        commentarystrategies-h1685-adjudication-spotcheck_review.html
Usage: python scripts/build_h1685_spotcheck_sheet.py
"""
import sys
import os
import re
import math
import json
import random
from collections import defaultdict, Counter

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
DATA = os.path.join(REPO, "data")
AD = os.path.join(DATA, "analysis", "h1685_adjudication")
OUT = os.path.join(AD, "commentarystrategies-h1685-adjudication-spotcheck_review.html")
SEED = 1685
Z2 = 1.96 ** 2
TARGET_LB = 0.80

sys.path.insert(0, HERE)
from compare_editions import load_southern  # noqa: E402

STRATA = [
    ("A", "Отсутствие в критическом издании — подтверждено глобальным перепоиском",
     lambda r: r.get("rule_id") == "FN-ABS-OK"),
    ("B", "Разночтение — оба чтения найдены в своих изданиях",
     lambda r: r.get("rule_id") == "FN-VAR-OK"),
    ("C", "Заметка принята по правилу: судья keep + три независимые проверки чисты",
     lambda r: r.get("rule_id") == "NOTE-KEEP-CLEAN"),
    ("D", "Прочитано адъюдикатором и принято", lambda r: r["tier"] == "opus" and r["verdict"] == "accept"),
    ("E", "Прочитано и ОТКЛОНЕНО", lambda r: r["tier"] == "opus" and r["verdict"] == "reject"),
    ("F", "Прочитано и отправлено на правку", lambda r: r["tier"] == "opus" and r["verdict"] == "edit"),
    ("G", "Прочитано и припарковано", lambda r: r["tier"] == "opus" and r["verdict"] == "park"),
    ("H", "Прочитано и заблокировано до перепривязки якоря",
     lambda r: r["tier"] == "opus" and r["verdict"] == "flag_anchor"),
    ("I", "Отклонено по правилу: различия нет после снятия орфографии",
     lambda r: r.get("rule_id") == "FN-VAR-NULL"),
]


def load(p):
    with open(p, encoding="utf-8") as fh:
        return json.load(fh)


def wilson_lb_clean(n):
    return round(n / (n + Z2), 3)


def derived_n(pop):
    """Smallest n whose clean sweep clears TARGET_LB; censused if too small.

    n/(n+z²) >= T  <=>  n >= z²T/(1-T). It must be a CEILING: z²·0.8/0.2 = 15.37,
    and n=15 yields 0.796 — under the bar this sheet claims to certify.
    """
    need = math.ceil(Z2 * TARGET_LB / (1 - TARGET_LB))      # = 16 for T = 0.80
    return min(pop, need)


def main():
    ledger = load(os.path.join(AD, "ledger_final.json"))["verdicts"]
    ev = {c["card_id"]: c for c in load(os.path.join(AD, "evidence.json"))["cards"]}
    south = {f"5.{s}.{v}": t for s, v, t in load_southern()}

    buckets = defaultdict(list)
    for r in ledger:
        for sid, _title, pred in STRATA:
            if pred(r):
                buckets[sid].append(r)
                break

    rng = random.Random(SEED)
    plan, items = [], []
    for sid, title, _ in STRATA:
        pop = buckets.get(sid, [])
        n = derived_n(len(pop))
        pick = pop if n >= len(pop) else rng.sample(pop, n)
        plan.append({"stratum": sid, "title": title, "population": len(pop),
                     "sampled": len(pick), "censused": n >= len(pop),
                     "wilson_lb_if_clean": wilson_lb_clean(len(pick))})
        for r in pick:
            c = ev[r["card_id"]]
            e = c["evidence"]
            vid = re.sub(r"[ab]$", "", c["verse_id"] or "")
            ec = e.get("evidence_cited")
            shown = {
                "id": r["card_id"], "stratum": sid, "queue": r["queue"],
                "key": r["key"], "verse_id": c["verse_id"],
                "verse": south.get(vid, ""),
                "lemma": c["lemma"], "note": c["note_ru"],
                # the evidence the adjudicator used — NOT its conclusion
                "evidence": {k: v for k, v in e.items()
                             if k not in ("per_verse", "reading_checks", "top3")},
            }
            if e.get("kind") in ("single", "verse_range", "sarga_absence"):
                shown["absence"] = [
                    {"southern_id": p["southern_id"], "best_crit_id": p["best_crit_id"],
                     "best_jaccard": p["best_jaccard"]} for p in e.get("per_verse", [])]
            if e.get("kind") == "variant_reading":
                shown["readings"] = e.get("reading_checks", [])
            items.append(shown)

    rng.shuffle(items)              # strata interleaved: no positional tell
    total = len(items)
    payload = {"meta": {
        "handoff": "H1685", "seed": SEED, "target_lower_bound": TARGET_LB,
        "z2": round(Z2, 4), "total": total, "plan": plan,
        "blind": True,
        "adjudicator": "Opus 5 1M (claude-opus-5[1m])",
        "instruction": ("Вы проверяете АДЪЮДИКАТОРА, а не заметки. Его вердикт "
                        "и вердикт прежнего судьи скрыты намеренно. Вынесите "
                        "свой — сравнение считает h1685_score_spotcheck.py."),
    }, "items": items}

    html = PAGE.replace("/*DATA*/null", json.dumps(payload, ensure_ascii=False))
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write(html)

    print(f"wrote {OUT}")
    print(f"{'str':<4}{'население':>10}{'выборка':>9}{'ценз':>6}{'LB при чистом':>15}  описание")
    for p in plan:
        print(f"{p['stratum']:<4}{p['population']:>10}{p['sampled']:>9}"
              f"{'да' if p['censused'] else '—':>6}{p['wilson_lb_if_clean']:>15}  {p['title'][:44]}")
    print(f"\nчеловеку предъявлено {total} карт вместо {len(ledger)} "
          f"({100 - 100*total/len(ledger):.1f}% сокращение)")


PAGE = r"""<!DOCTYPE html>
<html lang="ru"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>H1685 — слепая выборочная проверка адъюдикатора</title>
<link rel="stylesheet" href="../../../css/commentary.css">
<style>
:root{--bg:#faf8f4;--card:#fff;--ink:#222;--mut:#777;--line:#e4ddd0;--acc:#5a4a7a;
      --ok:#2e7d32;--edit:#b8860b;--no:#b23b3b;--park:#4a6b8a;--anch:#8a4a6b;}
*{box-sizing:border-box}
body{font:15px/1.55 Georgia,serif;margin:0;background:var(--bg);color:var(--ink)}
header{position:sticky;top:0;background:#fff;border-bottom:2px solid var(--acc);
       padding:10px 18px;z-index:10;box-shadow:0 2px 6px rgba(0,0,0,.06)}
h1{font-size:17px;margin:0 0 6px}
.bar{display:flex;gap:14px;align-items:center;flex-wrap:wrap;
     font:13px system-ui,sans-serif;color:var(--mut)}
button{font:13px system-ui,sans-serif;padding:6px 12px;border:1px solid var(--acc);
       background:#fff;color:var(--acc);border-radius:5px;cursor:pointer}
button:hover{background:var(--acc);color:#fff}
main.container{max-width:940px;margin:0 auto;padding:16px}
.intro{background:#fff;border:1px solid var(--line);border-left:5px solid var(--acc);
       border-radius:8px;padding:12px 16px;margin:0 0 16px;font-size:14px}
.card{background:var(--card);border:1px solid var(--line);border-left:5px solid var(--acc);
      border-radius:8px;padding:12px 16px;margin:0 0 14px}
.card.d-accept{border-left-color:var(--ok)} .card.d-edit{border-left-color:var(--edit)}
.card.d-reject{border-left-color:var(--no)} .card.d-park{border-left-color:var(--park)}
.card.d-flag_anchor{border-left-color:var(--anch)}
.vid{font:12px system-ui,sans-serif;color:var(--mut)}
.badge{font:11px system-ui,sans-serif;padding:1px 7px;border-radius:10px;
       background:#eee5d3;color:var(--acc);margin-left:6px}
.verse{font-style:italic;color:#3a3020;background:#f7f2e8;border-radius:6px;
       padding:6px 10px;margin:6px 0}
.note{font-size:16px;margin:8px 0;padding:6px 0;border-top:1px solid var(--line);
      border-bottom:1px solid var(--line)}
.ev{font:12px ui-monospace,monospace;background:#f2f4f7;border-radius:6px;
    padding:6px 10px;margin:6px 0;white-space:pre-wrap;word-break:break-word;color:#334}
.ev b{color:#5a4a7a}
.controls{margin-top:10px;display:flex;gap:8px;flex-wrap:wrap;font:13px system-ui,sans-serif}
.controls label{display:inline-flex;gap:4px;align-items:center;padding:5px 10px;
                border:1px solid var(--line);border-radius:20px;cursor:pointer;background:#fff}
.controls label:hover{background:#f3efe6}
textarea{width:100%;font:14px Georgia,serif;padding:8px;border:1px solid var(--line);
         border-radius:5px;margin-top:8px}
.hidden{display:none}
</style></head><body>
<header>
  <h1>H1685 — слепая выборочная проверка адъюдикатора</h1>
  <div class="bar">
    <span id="prog">0 / 0</span>
    <button id="dl">⬇ Скачать decisions.json</button>
    <button id="clr">Сбросить</button>
    <label><input type="checkbox" id="onlyleft"> только неотвеченные</label>
  </div>
</header>
<main class="container">
  <div class="intro" id="intro"></div>
  <div id="list"></div>
</main>
<script>
const D = /*DATA*/null;
const KEY = "h1685_spotcheck_decisions_v1";
const ACTIONS = [["accept","принять"],["edit","на правку"],["reject","отклонить"],
                 ["park","припарковать"],["flag_anchor","якорь неверен"]];
let votes = JSON.parse(localStorage.getItem(KEY) || "{}");
const save = () => localStorage.setItem(KEY, JSON.stringify(votes));

document.getElementById("intro").innerHTML =
  "<b>Вы проверяете адъюдикатора, а не заметки.</b> Его вердикт и вердикт прежнего "
  + "судьи (Sonnet 5) на карточках намеренно НЕ показаны — иначе измерялось бы "
  + "согласие с подсказкой, а не точность. Вынесите собственный вердикт; сравнение "
  + "посчитает <code>scripts/h1685_score_spotcheck.py</code>.<br><br>"
  + "Выборка: <b>" + D.meta.total + "</b> карт из 1889, 9 страт, seed " + D.meta.seed
  + ". Размер страты выведен, а не выбран: при полностью чистой страте нижняя "
  + "граница Уилсона 95% равна n/(n+3.84), поэтому n=16 — минимум, дающий ≥ "
  + D.meta.target_lower_bound + ".<br><br>"
  + D.meta.plan.map(p => "<code>" + p.stratum + "</code> " + p.title
      + " — " + p.sampled + " из " + p.population
      + (p.censused ? " (сплошь)" : "") + ", LB " + p.wilson_lb_if_clean).join("<br>");

function evLines(it){
  const e = it.evidence || {};
  const keep = ["kind","anchor","anchor_detail","commentators_named","commentators_attested",
    "commentators_missing","note_in_podstrochnik","note_in_tier1","tier1_notes_here",
    "mw_headwords_cited","mw_headwords_missing","gloss_check","duplicate_in_book",
    "max_global_jaccard","verses_checked","leonov_edition_note_here",
    "readings_checked","n_readings_distinct","n_omission_markers","all_readings_located",
    "generator_confidence","parked_ws3b","reanchored"];
  let out = keep.filter(k => e[k] !== undefined && e[k] !== null && e[k] !== "" &&
                             !(Array.isArray(e[k]) && !e[k].length))
                .map(k => "<b>"+k+"</b>: "+JSON.stringify(e[k])).join("\n");
  if (it.absence) out += "\n<b>глобальный перепоиск</b>: " + it.absence.map(a =>
      a.southern_id+" ~ "+a.best_crit_id+" j="+a.best_jaccard).join("; ");
  if (it.readings) out += "\n<b>чтения</b>: " + it.readings.map(r =>
      r.crit+" ] "+r.southern+" [крит:"+(r.crit_located?"✓":"✗")
      +" южн:"+(r.southern_located?"✓":"✗")+(r.omission?" ∅":"")+"]").join("; ");
  return out;
}

function render(){
  const only = document.getElementById("onlyleft").checked;
  const list = document.getElementById("list");
  list.innerHTML = "";
  let done = 0;
  D.items.forEach(it => {
    const v = votes[it.id];
    if (v) done++;
    if (only && v) return;
    const div = document.createElement("div");
    div.className = "card" + (v ? " d-" + v.action : "");
    div.innerHTML =
      '<div class="vid">' + it.verse_id + ' · ' + it.queue
      + '<span class="badge">страта ' + it.stratum + '</span>'
      + (it.lemma ? '<span class="badge">' + it.lemma + '</span>' : '') + '</div>'
      + (it.verse ? '<div class="verse">' + it.verse + '</div>' : '')
      + '<div class="note">' + it.note + '</div>'
      + '<div class="ev">' + evLines(it) + '</div>'
      + '<div class="controls">'
      + ACTIONS.map(([a, ru]) =>
          '<label><input type="radio" name="r_' + it.id + '" value="' + a + '"'
          + (v && v.action === a ? ' checked' : '') + '>' + ru + '</label>').join('')
      + '</div>'
      + '<textarea rows="2" placeholder="почему (обязательно при расхождении)">'
      + (v && v.comment ? v.comment : '') + '</textarea>';
    div.querySelectorAll('input[type=radio]').forEach(r => r.onchange = () => {
      votes[it.id] = {action: r.value,
                      comment: div.querySelector('textarea').value,
                      stratum: it.stratum, queue: it.queue, key: it.key};
      save(); render();
    });
    div.querySelector('textarea').onblur = e => {
      if (votes[it.id]) { votes[it.id].comment = e.target.value; save(); }
    };
    list.appendChild(div);
  });
  document.getElementById("prog").textContent = done + " / " + D.items.length;
}
document.getElementById("onlyleft").onchange = render;
document.getElementById("clr").onclick = () => {
  if (confirm("Сбросить все голоса?")) { votes = {}; save(); render(); }
};
document.getElementById("dl").onclick = () => {
  const blob = new Blob([JSON.stringify({
    sheet_id: "commentarystrategies-h1685-adjudication-spotcheck",
    handoff: "H1685", reviewed_at: new Date().toISOString(),
    meta: D.meta, reviewer_decisions: votes}, null, 1)],
    {type: "application/json"});
  const a = document.createElement("a");
  a.href = URL.createObjectURL(blob);
  a.download = "h1685_spotcheck_decisions.json";
  a.click();
};
render();
</script></body></html>
"""


if __name__ == "__main__":
    main()

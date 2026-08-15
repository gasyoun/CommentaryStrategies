/* Apparatus ballot renderer.
 *
 * Rebuilt under H2830 against votes/sarga.md — Kostina's and MG's 19-point read
 * of the sarga-1 ballot. Numbers in comments below are that document's items.
 */
(function(){"use strict";
const D=window.APPARATUS_DATA;const C=window.REVIEW_CONFIG||{};if(!D)return;
const reviewer=C.reviewer||"";const revision=C.manifestRevision||"unmanifested";const key=`sundara-review:${reviewer}:${revision}:${D.sarga}`;
let decisions={};try{decisions=JSON.parse(localStorage.getItem(key)||"{}");}catch(_){decisions={};}
const root=document.getElementById("app");const status=document.getElementById("sync-status");
function esc(value){return String(value==null?"":value).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;").replace(/'/g,"&#39;");}

/* п.1 «весь санскрит всегда надо курсивом — cāraṇācarite pathi».
 * Sanskrit inside a Russian sentence is only ever recognisable by its
 * diacritics, so that is what marks it: a run of Latin letters where at least
 * one carries an IAST diacritic. A plain Latin word (MW, Goldman, N. of) has
 * none and stays upright, which is what keeps «MW: amarāvatī» reading correctly
 * — siglum roman, headword italic. Runs on the ESCAPED string, so it can never
 * introduce markup: the pattern matches letters only. */
const IAST_DIA="āīūṛṝḷḹṅñṭḍṇśṣḥṃĀĪŪṚṜḶḸṄÑṬḌṆŚṢḤṂ";
const SA_RUN=new RegExp("[A-Za-z"+IAST_DIA+"][A-Za-z"+IAST_DIA+"'’-]*(?:[  ][A-Za-z"+IAST_DIA+"][A-Za-z"+IAST_DIA+"'’-]*)*","g");
const HAS_DIA=new RegExp("["+IAST_DIA+"]");
function sa(html){return String(html==null?"":html).replace(SA_RUN,m=>HAS_DIA.test(m)?`<i class="sa">${m}</i>`:m);}
function escSa(value){return sa(esc(value));}

function setState(name,detail){status.className=`status-pill status-${name}`;status.textContent={local:"черновик",syncing:"синхронизация…",synced:"сохранено",offline:"офлайн (черновик)",conflict:"конфликт",submitted:"отправлено",error:"ошибка синхронизации"}[name]||name;status.setAttribute("role","status");document.getElementById("sync-detail").textContent=detail||"";}
const sync=new ReviewSync({base:C.apiBase||"",revision,sarga:D.sarga,onState:setState});
function votable(){return D.verses.flatMap(v=>v.notes).filter(n=>n.votable);}
/* A comment is optional everywhere (п.11), so it never gates completeness; a
 * rejection still owes a reason and an edit still owes text. */
function validRecord(n,rec){if(!rec||!["accept","edit","reject"].includes(rec.action))return false;if(rec.action==="edit"&&!String(rec.edited_note||"").trim())return false;if(rec.action==="reject"&&!String(rec.reject_reason||"").trim())return false;return true;}
function persist(){localStorage.setItem(key,JSON.stringify(decisions));setState(navigator.onLine?"local":"offline","Черновик сохранён на этом устройстве.");progress();window.dispatchEvent(new CustomEvent("review-draft-change",{detail:{sarga:D.sarga}}));}
function progress(){const all=votable();const done=all.filter(n=>validRecord(n,decisions[n.id])).length;document.getElementById("progress").textContent=`${done} из ${all.length} решено`;}

/* п.8: the badge carries the state, this block carries who/when/why — the two
 * no longer print the same fact in two notations. */
const ACT_RU={accept:"принял",edit:"правил",reject:"отклонил"};
function ruDate(iso){const m=/^(\d{4})-(\d{2})-(\d{2})/.exec(iso||"");return m?`${m[3]}.${m[2]}.${m[1]}`:(iso||"");}
function verdicts(n){return Object.keys(n.gate_verdicts||{}).sort().map(r=>{const v=n.gate_verdicts[r];const mine=r===reviewer;
  const when=v.gated_date?` · ${esc(ruDate(v.gated_date))}`:"";
  const why=v.reject_reason?`<span class="was">причина: ${escSa(v.reject_reason)}</span>`:"";
  const was=v.edited_note?`<span class="was">его редакция: ${escSa(v.edited_note)}</span>`:"";
  if(mine)return `<div class="mine">Ваш голос учтён: ${esc(ACT_RU[v.action]||v.action)}${when}${why}${was}</div>`;
  return `<div class="colleague"><b>${esc(r)}</b> ${esc(ACT_RU[v.action]||v.action)}${when}${reviewer?" — ваш голос нужен независимо":""}${why}${was}</div>`;}).join("");}

/* п.5: «надо выделить [Е. Костина] — потому что в печатном тексте этого не
 * будет, это для пока служебной заметки». The editor's own reminders are lifted
 * out of the prose by the generator and printed here as a separate, plainly
 * labelled block that says it is not for print. */
function serviceBlock(n){return (n.service||[]).map(s=>`<aside class="service"><span class="service-tag">служебная заметка · ${esc(s.author)} · не идёт в печать</span>${s.lemma_iast?`<i class="sa">${esc(s.lemma_iast)}</i> — `:""}${escSa(s.text)}</aside>`).join("");}

/* п.17: «Комм.[Claude.AI — желательно] ? [кат.5 — текстология] — убрать»,
 * «почему не завершено и не стоит точка в конце?». The `Комм.` and the stray
 * `?` are gone with the parse; an unfinished template is now labelled as one
 * instead of being printed as if it were a finished sentence. */
function suggestionBlock(n){return (n.suggestions||[]).map(s=>{
  const tags=[`<span class="badge b-machine">предложение машины${s.strength?" · "+esc(s.strength):""}</span>`];
  if(s.kind)tags.push(`<span class="badge b-status">${esc(s.kind)}</span>`);
  if(s.accounted)tags.push(`<span class="badge b-status">${esc(s.accounted)}</span>`);
  if(s.incomplete)tags.push(`<span class="badge b-crit">заготовка не заполнена</span>`);
  const body=s.incomplete
    ?`<span class="stub">Ссылка на первое вхождение не подставлена — заготовку нужно либо дописать, либо снять.</span>`
    :escSa(s.text);
  return `<aside class="suggestion${s.incomplete?" incomplete":""}"><div>${tags.join("")}</div>${body}</aside>`;}).join("");}

/* п.18: «почему не кликабельно на Cologne? amarāvatī на MW и Apte» */
function sourceBlock(n){
  if(!n.source&&!(n.source_links||[]).length)return "";
  const links=(n.source_links||[]).map(l=>`<a href="${esc(l.url)}" target="_blank" rel="noopener">${escSa(l.label)}</a>`).join(" · ");
  return `<div class="meta">Источник: ${links||escSa(n.source)}${links&&n.source_links.length?` <span class="hint">(Cologne)</span>`:""}</div>`;}

function noteHtml(n){const rec=decisions[n.id]||{};
  const badges=[`<span class="badge b-${esc(n.layer)}">${esc(n.layer_label)}</span>`,
                `<span class="badge b-status">${esc(n.status)}</span>`];
  if(n.provenance)badges.push(`<span class="badge b-status" title="${esc(n.provenance)}">происхождение</span>`);
  if(n.scope)badges.push(`<span class="badge b-status">объём: ${esc(n.scope)}</span>`);
  /* п.12: a running number per sarga plus the stable id, so a reviewer can name
   * one note in an e-mail and everyone lands on the same card. */
  const anchor=`n-${n.id}`;
  const head=`<div class="nhead"><a class="seq" href="#${esc(anchor)}" title="${esc(n.id)}">№&nbsp;${esc(n.seq)}</a>${badges.join("")}</div>`;
  const body=`<p class="ntext">${n.lemma_iast?`<i class="sa lemma">${esc(n.lemma_iast)}</i> — `:""}${escSa(n.note_ru||"")}</p>`;
  /* п.11: «почему нет окна для комментариев? Хотя бы одной строчки» — one is
   * always open, on every votable card, whatever the verdict. */
  const controls=n.votable?`<div class="controls" role="group" aria-label="Решение по примечанию ${esc(n.seq)}">${
    ["accept","edit","reject"].map(a=>`<label><input type="radio" name="a_${esc(n.id)}" value="${a}" ${rec.action===a?"checked":""}>${{accept:"✅ принять",edit:"✏️ править",reject:"❌ отклонить"}[a]}</label>`).join("")}</div>
    <textarea data-edit="${esc(n.id)}" class="${rec.action==="edit"?"":"hidden"}" rows="3" aria-label="Исправленный текст">${esc(rec.edited_note||n.note_ru||"")}</textarea>
    <input data-reject="${esc(n.id)}" class="reject-reason ${rec.action==="reject"?"":"hidden"}" aria-label="Причина отклонения" placeholder="Причина отклонения…" value="${esc(rec.reject_reason||"")}">
    <input data-comment="${esc(n.id)}" class="comment" aria-label="Комментарий" placeholder="Комментарий (необязательно)…" value="${esc(rec.comment||"")}">`:"";
  const collide=n.collision_tier1?`<div class="collide">⚠ на этом стихе уже есть примечание яруса 1 — проверьте на дублирование</div>`:"";
  return `<article class="note l-${esc(n.layer)} ${rec.action?`d-${esc(rec.action)}`:""}" id="${esc(anchor)}" data-note="${esc(n.id)}">${head}${body}${serviceBlock(n)}${suggestionBlock(n)}${sourceBlock(n)}${verdicts(n)}${collide}${controls}</article>`;}

/* п.3 «что значит ярус 1? где легенда?» and п.7 «а сколько всего фаз?» — the
 * glossary travels with the data (see LAYER_GLOSSARY in the generator) so it can
 * never drift away from the labels printed on the badges. */
function legendHtml(){const g=D._meta.glossary||{};const order=["tier1","lexical","phase2","edition","crosstext"];
  const rows=order.filter(k=>g[k]).map(k=>`<div class="legend-row"><span class="badge b-${k}">${esc((D._meta.sources||{})[k]||k)}</span><b>${esc(g[k].title)}</b><span>${escSa(g[k].what)}</span><span class="legend-vote">${esc(g[k].vote)}</span><span class="legend-prov">${escSa(g[k].provenance)}</span></div>`).join("");
  return `<details class="legend" open><summary>Условные обозначения — пять слоёв аппарата</summary>
    <p class="legend-phase">${escSa(D._meta.phase_note||"")}</p>${rows}
    <p class="legend-foot">Номер стиха ведёт к полному тексту песни; № примечания — постоянный адрес карточки, на него можно ссылаться.</p></details>`;}

function render(){root.textContent="";
  root.insertAdjacentHTML("beforeend",legendHtml());
  D.verses.forEach(v=>{const card=document.createElement("section");card.className="vcard";
    const ref=v.verse_ref?`<a href="${esc(v.verse_ref)}" target="_blank" rel="noopener">${esc(v.verse_id)}</a>`:esc(v.verse_id);
    /* п.16: an empty card now says why it is empty. */
    const versePane=v.empty_reason
      ?`<div class="verse empty"><span class="empty-why">${escSa(v.empty_reason)}</span></div>`
      :`<div class="verse"><div class="sa">${escSa(v.sanskrit_iast)||"—"}</div><div class="ru">${escSa(v.leonov_ru)||"—"}</div></div>`;
    card.innerHTML=`<div class="vhead"><b>${ref}</b></div>${versePane}${v.notes.map(noteHtml).join("")}`;
    root.appendChild(card);});
  bind();progress();}

function bind(){
  root.querySelectorAll("input[type=radio]").forEach(input=>input.addEventListener("change",()=>{const article=input.closest("[data-note]");const id=article.dataset.note;const note=votable().find(n=>n.id===id);const rec=decisions[id]||{verse_id:note.verse_id,layer:note.layer,lemma_iast:note.lemma_iast||"",seq:note.seq};rec.action=input.value;rec.ts=new Date().toISOString();const edit=article.querySelector("[data-edit]");const reject=article.querySelector("[data-reject]");const comment=article.querySelector("[data-comment]");edit.classList.toggle("hidden",rec.action!=="edit");reject.classList.toggle("hidden",rec.action!=="reject");rec.edited_note=edit.value;rec.reject_reason=reject.value;rec.comment=comment?comment.value:"";decisions[id]=rec;article.className=article.className.replace(/\bd-(accept|edit|reject)\b/g,"").trim()+` d-${rec.action}`;persist();}));
  root.querySelectorAll("[data-edit],[data-reject],[data-comment]").forEach(input=>input.addEventListener("input",()=>{const id=input.dataset.edit||input.dataset.reject||input.dataset.comment;const rec=decisions[id]||{};if(input.dataset.edit)rec.edited_note=input.value;else if(input.dataset.reject)rec.reject_reason=input.value;else rec.comment=input.value;decisions[id]=rec;persist();}));}

function aggregate(){return {schema_version:1,reviewer,manifest_hash:C.manifestHash||"",source_hash:C.sourceHash||"",client_timestamp:new Date().toISOString(),sargas:[{sarga:D.sarga,source_hash:D._meta.source_hash||"",decisions}]};}
function download(){const body=JSON.stringify(aggregate(),null,2);const url=URL.createObjectURL(new Blob([body],{type:"application/json"}));const a=document.createElement("a");a.href=url;a.download=`decisions_sarga_${D.sarga}_kostina.json`;a.click();URL.revokeObjectURL(url);}
document.getElementById("download").addEventListener("click",download);
document.getElementById("remote-save").addEventListener("click",()=>sync.save(decisions).catch(()=>{}));
document.getElementById("submit").addEventListener("click",async()=>{const missing=votable().filter(n=>!validRecord(n,decisions[n.id]));if(missing.length){setState("error",`Не заполнено решений: ${missing.length}. Окончательная отправка не выполнена.`);return;}if(!confirm("Окончательная отправка необратима. Продолжить?"))return;await sync.submit(aggregate()).catch(()=>{});});
window.addEventListener("online",()=>setState("local","Сеть есть; доступна удалённая синхронизация."));
window.addEventListener("offline",()=>setState("offline","Черновик сохранён локально."));
window.reviewPlatform={aggregate,validRecord,key};
setState(navigator.onLine?"local":"offline","Черновик готов.");render();
})();

// DOM verification of the cross-text section via a minimal DOM shim that runs
// the page's actual inline ctData -> ctBody script.
import { readFileSync } from 'fs';

const HTML = 'C:/Users/user/Documents/GitHub/CommentaryStrategies-crosstext/leonov_sundara_corpus_enriched.html';
const html = readFileSync(HTML, 'utf-8');

// --- extract the ctData script block (from the marker to the next // ── comment) ---
const start = html.indexOf('// ── Межтекстовый слой');
const end = html.indexOf('// ── Плотность примечаний', start);
if (start < 0 || end < 0) { console.error('MARKERS NOT FOUND'); process.exit(2); }
const script = html.slice(start, end);

// --- minimal DOM shim ---
const rows = [];
function makeEl(tag) {
  return {
    tagName: tag, _html: '', children: [],
    set innerHTML(v) { this._html = v; },
    get innerHTML() { return this._html; },
    appendChild(c) { this.children.push(c); },
    querySelector() { return null; },
  };
}
const ctBody = { children: [], appendChild(c){ this.children.push(c); rows.push(c); } };
const document = {
  getElementById(id){ return id === 'ctBody' ? ctBody : null; },
  createElement(tag){ return makeEl(tag); },
};
// run the script
const fn = new Function('document', script + '\nreturn (typeof ctData!=="undefined")?ctData:[];');
const ctData = fn(document);

// --- assertions ---
const headerRows = rows.filter(r => /colspan=/.test(r._html));
const noteRows = rows.filter(r => !/colspan=/.test(r._html));
const clusters = {};
ctData.forEach(d => clusters[d.cl] = (clusters[d.cl]||0)+1);
const clusterHeaders = headerRows.map(r => (r._html.match(/· (\d+) примеч/)||[])[0]);

const result = {
  ctDataLen: ctData.length,
  domRowsTotal: rows.length,
  clusterHeaderRows: headerRows.length,
  noteRows: noteRows.length,
  clusterCounts: clusters,
  clusterOrder: [...new Set(ctData.map(d=>d.cl))],
  sampleHeader: headerRows[0]?._html?.replace(/<[^>]+>/g,' ').replace(/\s+/g,' ').trim(),
  alsoRows: noteRows.filter(r=>/также:/.test(r._html)).length,
  firstNote: noteRows[0]?._html?.replace(/<[^>]+>/g,' ').replace(/\s+/g,' ').trim().slice(0,90),
};
console.log(JSON.stringify(result, null, 1));
// hard checks (updated 2026-07-02, crosstext-expansion PR #42 reconciliation: 107->170 notes,
// 6->9 clusters after unioning with parallel direct-to-main cross-text work; ramayana_grintser
// promoted 11->33 confirmed once its missing 'verified' flag was treated like gita/mbh_gnomic)
const ok = ctData.length === 170
  && headerRows.length === 9
  && noteRows.length === 170
  && JSON.stringify(Object.keys(clusters).sort()) === JSON.stringify(['dharmashastra','gita','kavya','mbh_battle','mbh_gnomic','mbh_narrative','ramayana_grintser','upanishads','veda']);
console.log('DOM_VERIFY', ok ? 'PASS' : 'FAIL');
process.exit(ok ? 0 : 1);

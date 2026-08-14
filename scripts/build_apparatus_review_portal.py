#!/usr/bin/env python3
"""Build/check the deterministic 68-sarga Kostina review portal."""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "apparatus"
MANIFEST = OUT / "reviewer_manifest.json"
INDEX = OUT / "index.html"
WEBMANIFEST = OUT / "review.webmanifest"
SW = OUT / "review-sw.js"
REVIEWER = "Костина"


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def source_revision() -> tuple[str, str]:
    paths = ["scripts/build_sarga_apparatus.py", "scripts/build_apparatus_review_portal.py",
             "js/apparatus-review.js", "js/review-portal.js", "js/review-sync.js",
             "css/apparatus-review.css", "data/apparatus/gate_ledger.json",
             "data/analysis/sundara_commentary_segmented.json"]
    commit = subprocess.run(["git", "log", "-1", "--format=%H", "--", *paths],
                            cwd=ROOT, check=True, capture_output=True,
                            encoding="utf-8").stdout.strip()
    stamp = subprocess.run(["git", "show", "-s", "--format=%cI", commit], cwd=ROOT,
                           check=True, capture_output=True, encoding="utf-8").stdout.strip()
    return commit, stamp


def build_manifest() -> dict:
    entries = []
    combined = hashlib.sha256()
    for sarga in range(1, 69):
        jp = OUT / f"sarga_{sarga:02d}_kostina.json"
        hp = OUT / f"sarga_{sarga:02d}_kostina.html"
        if not jp.exists() or not hp.exists():
            raise ValueError(f"missing generated ballot for sarga {sarga}")
        raw = jp.read_bytes()
        doc = json.loads(raw)
        if doc.get("sarga") != sarga or doc.get("_meta", {}).get("built_for_reviewer") != REVIEWER:
            raise ValueError(f"sarga {sarga}: wrong identity")
        notes = [n for verse in doc.get("verses", []) for n in verse.get("notes", [])]
        source_hash = doc.get("_meta", {}).get("source_hash")
        if not source_hash:
            raise ValueError(f"sarga {sarga}: missing source hash")
        combined.update(bytes.fromhex(source_hash))
        entries.append({"sarga": sarga, "url": f"sarga_{sarga:02d}_kostina.html",
                        "data_url": f"sarga_{sarga:02d}_kostina.json",
                        "note_count": len(notes),
                        "votable_count": sum(bool(n.get("votable")) for n in notes),
                        "ballot_hash": sha(hp.read_bytes()), "source_hash": source_hash})
    revision, stamp = source_revision()
    return {"schema_version": 1, "reviewer": REVIEWER, "repo_revision": revision,
            "generated_at": stamp, "source_hash": combined.hexdigest(), "sargas": entries}


def with_manifest_hash(doc: dict) -> dict:
    unsigned = json.dumps(doc, ensure_ascii=False, sort_keys=True,
                          separators=(",", ":")).encode("utf-8")
    out = dict(doc)
    out["manifest_hash"] = sha(unsigned)
    return out


def index_html(doc: dict) -> str:
    blob = json.dumps(doc, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    return f'''<!doctype html>
<html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'; connect-src 'self' https:; object-src 'none'; base-uri 'none'">
<title>Сундараканда — рецензирование Костиной</title><link rel="manifest" href="review.webmanifest"><link rel="stylesheet" href="../../css/commentary.css"><link rel="stylesheet" href="../../css/apparatus-review.css"></head>
<body><header class="review-header"><div class="breadcrumb"><a href="../../index.html">CommentaryStrategies</a> › официальный портал</div><h1>Рецензирование Сундараканды · Е. Костина</h1><div class="toolbar"><strong id="portal-status" role="status" aria-live="polite">Загрузка…</strong></div></header>
<main class="container"><div class="review-shell"><section class="recovery"><b>Работа сохраняется локально на этом устройстве.</b> Можно продолжить после перезагрузки и скачать один JSON по всем 68 песням. Удалённая синхронизация доступна только после входа; окончательная отправка всегда отдельна и необратима.</section><div class="portal-actions"><button id="aggregate-download">Скачать общий JSON</button><button id="final-submit">Отправить окончательно</button></div><p class="warning">Нажатие «сохранить» не отправляет бюллетень. Перед окончательной отправкой сохраните общий JSON как резервную копию.</p><section id="sarga-grid" class="portal-grid" aria-label="Песни 1–68"></section></div></main>
<script>window.REVIEW_MANIFEST={blob};</script><script src="../../js/review-portal.js" defer></script></body></html>'''


def webmanifest() -> str:
    return json.dumps({"name": "Сундараканда — рецензирование Костиной",
                       "short_name": "Sundara review", "start_url": "./",
                       "display": "standalone", "background_color": "#f6f2ea",
                       "theme_color": "#73562c"}, ensure_ascii=False, indent=2) + "\n"


def service_worker(doc: dict) -> str:
    version = doc["manifest_hash"][:16]
    shell = ["./", "index.html", "reviewer_manifest.json", "review.webmanifest",
             "../../css/commentary.css", "../../css/apparatus-review.css",
             "../../js/review-portal.js", "../../js/review-sync.js", "../../js/apparatus-review.js"]
    return f'''"use strict";const CACHE="sundara-review-{version}";const SHELL={json.dumps(shell)};
self.addEventListener("install",event=>event.waitUntil(caches.open(CACHE).then(cache=>cache.addAll(SHELL))));
self.addEventListener("activate",event=>event.waitUntil(caches.keys().then(keys=>Promise.all(keys.filter(k=>k!==CACHE).map(k=>caches.delete(k))))));
self.addEventListener("fetch",event=>{{if(event.request.method!=="GET")return;event.respondWith(fetch(event.request).then(response=>{{const copy=response.clone();caches.open(CACHE).then(cache=>cache.put(event.request,copy));return response;}}).catch(()=>caches.match(event.request)));}});\n'''


def expected() -> dict[Path, str]:
    doc = with_manifest_hash(build_manifest())
    return {MANIFEST: json.dumps(doc, ensure_ascii=False, indent=2) + "\n",
            INDEX: index_html(doc), WEBMANIFEST: webmanifest(), SW: service_worker(doc)}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    outputs = expected()
    if args.check:
        errors = [str(path.relative_to(ROOT)) for path, content in outputs.items()
                  if not path.exists() or path.read_text(encoding="utf-8") != content]
        if errors:
            print("FAIL: stale/missing portal outputs: " + ", ".join(errors))
            return 1
    else:
        for path, content in outputs.items():
            path.write_text(content, encoding="utf-8")
    manifest = json.loads(outputs[MANIFEST])
    sargas = [row["sarga"] for row in manifest["sargas"]]
    if sargas != list(range(1, 69)) or len(set(sargas)) != 68:
        print("FAIL: manifest must contain exactly unique sargas 1–68")
        return 1
    print(f"PASS: 68 Kostina ballots; manifest {manifest['manifest_hash']}; check={args.check}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

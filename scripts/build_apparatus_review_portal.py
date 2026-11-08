#!/usr/bin/env python3
"""Build/check the deterministic 68-sarga reviewer portal (Kostina or Leonov).

Kostina keeps her legacy single-instance filenames (index.html,
reviewer_manifest.json, review.webmanifest, review-sw.js) — structure and
filenames stable, existing links keep working. Provenance-only deltas to her
artifacts after source commits are the established H4742 heal recipe (commit
5264bbd precedent): the repo_revision pin makes any commit touching the pinned
source paths invalidate both portals' committed provenance, and the follow-up
regen commit (which touches no pinned path) restores --check green.
Every other reviewer gets slug-suffixed filenames (index_<slug>.html, ...),
derived from the same REVIEWER_SLUG map the ballot builder uses.
"""
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

# Cyrillic reviewer name -> ASCII slug for filenames (same map as
# build_sarga_apparatus.py; keep the two in sync).
REVIEWER_SLUG = {"Костина": "kostina", "Леонов": "leonov", "Гасунс": "gasuns"}
# Genitive of the reviewer for the <title> («рецензирование Костиной»).
REVIEWER_GEN = {"Костина": "Костиной", "Леонов": "Леоновым", "Гасунс": "Гасунсом"}
# Display name in the h1.
REVIEWER_DISPLAY = {"Костина": "Е. Костина", "Леонов": "М. Леонов", "Гасунс": "М. Гасунс"}


def paths_for(slug: str) -> dict:
    """Portal output paths for a reviewer slug; kostina keeps legacy names."""
    if slug == "kostina":
        return {"manifest": OUT / "reviewer_manifest.json", "index": OUT / "index.html",
                "webmanifest": OUT / "review.webmanifest", "sw": OUT / "review-sw.js"}
    return {"manifest": OUT / f"reviewer_manifest_{slug}.json",
            "index": OUT / f"index_{slug}.html",
            "webmanifest": OUT / f"review_{slug}.webmanifest",
            "sw": OUT / f"review-sw-{slug}.js"}


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


def build_manifest(reviewer: str, slug: str) -> dict:
    entries = []
    combined = hashlib.sha256()
    for sarga in range(1, 69):
        jp = OUT / f"sarga_{sarga:02d}_{slug}.json"
        hp = OUT / f"sarga_{sarga:02d}_{slug}.html"
        if not jp.exists() or not hp.exists():
            raise ValueError(f"missing generated ballot for sarga {sarga} ({slug})")
        raw = jp.read_bytes()
        doc = json.loads(raw)
        if doc.get("sarga") != sarga or doc.get("_meta", {}).get("built_for_reviewer") != reviewer:
            raise ValueError(f"sarga {sarga}: wrong identity")
        notes = [n for verse in doc.get("verses", []) for n in verse.get("notes", [])]
        source_hash = doc.get("_meta", {}).get("source_hash")
        if not source_hash:
            raise ValueError(f"sarga {sarga}: missing source hash")
        combined.update(bytes.fromhex(source_hash))
        entries.append({"sarga": sarga, "url": f"sarga_{sarga:02d}_{slug}.html",
                        "data_url": f"sarga_{sarga:02d}_{slug}.json",
                        "note_count": len(notes),
                        "votable_count": sum(bool(n.get("votable")) for n in notes),
                        "ballot_hash": sha(hp.read_text(encoding="utf-8").encode("utf-8")),
                        "source_hash": source_hash})
    revision, stamp = source_revision()
    return {"schema_version": 1, "reviewer": reviewer, "repo_revision": revision,
            "generated_at": stamp, "source_hash": combined.hexdigest(), "sargas": entries}


def with_manifest_hash(doc: dict) -> dict:
    unsigned = json.dumps(doc, ensure_ascii=False, sort_keys=True,
                          separators=(",", ":")).encode("utf-8")
    out = dict(doc)
    out["manifest_hash"] = sha(unsigned)
    return out


def index_html(doc: dict, reviewer: str, slug: str) -> str:
    blob = json.dumps(doc, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    gen = REVIEWER_GEN.get(reviewer, reviewer)
    display = REVIEWER_DISPLAY.get(reviewer, reviewer)
    return f'''<!doctype html>
<html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; font-src 'self' https://fonts.gstatic.com; connect-src 'self' https:; object-src 'none'; base-uri 'none'">
<title>Сундараканда — рецензирование {gen}</title><link rel="manifest" href="review{"_" + slug if slug != "kostina" else ""}.webmanifest"><link rel="stylesheet" href="../../css/commentary.css"><link rel="stylesheet" href="../../css/apparatus-review.css"></head>
<body><header class="review-header"><div class="breadcrumb"><a href="../../index.html">CommentaryStrategies</a> › официальный портал</div><h1>Рецензирование Сундараканды · {display}</h1><div class="toolbar"><strong id="portal-status" role="status" aria-live="polite">Загрузка…</strong></div></header>
<main class="container"><div class="review-shell"><section class="recovery"><b>Работа сохраняется локально на этом устройстве.</b> Можно продолжить после перезагрузки и скачать один JSON по всем 68 песням. Удалённая синхронизация доступна только после входа; окончательная отправка всегда отдельна и необратима.</section><div class="portal-actions"><button id="aggregate-download">Скачать общий JSON</button><button id="final-submit">Отправить окончательно</button></div><p class="warning">Нажатие «сохранить» не отправляет бюллетень. Перед окончательной отправкой сохраните общий JSON как резервную копию.</p><section id="sarga-grid" class="portal-grid" aria-label="Песни 1–68"></section></div></main>
<script>window.REVIEW_MANIFEST={blob};</script><script src="../../js/review-portal.js" defer></script></body></html>'''


def webmanifest(reviewer: str) -> str:
    gen = REVIEWER_GEN.get(reviewer, reviewer)
    return json.dumps({"name": f"Сундараканда — рецензирование {gen}",
                       "short_name": "Sundara review", "start_url": "./",
                       "display": "standalone", "background_color": "#f6f2ea",
                       "theme_color": "#73562c"}, ensure_ascii=False, indent=2) + "\n"


def service_worker(doc: dict, slug: str) -> str:
    version = doc["manifest_hash"][:16]
    # kostina keeps the legacy cache name (saved PWA states must survive);
    # other reviewers namespace by slug so caches never collide.
    cache = "sundara-review-" + (version if slug == "kostina" else f"{slug}-{version}")
    index_name = "index.html" if slug == "kostina" else f"index_{slug}.html"
    webmanifest_name = "review.webmanifest" if slug == "kostina" else f"review_{slug}.webmanifest"
    manifest_name = "reviewer_manifest.json" if slug == "kostina" else f"reviewer_manifest_{slug}.json"
    shell = ["./", index_name, manifest_name, webmanifest_name,
             "../../css/commentary.css", "../../css/apparatus-review.css",
             "../../js/review-portal.js", "../../js/review-sync.js", "../../js/apparatus-review.js"]
    return f'''"use strict";const CACHE="{cache}";const SHELL={json.dumps(shell)};
self.addEventListener("install",event=>event.waitUntil(caches.open(CACHE).then(cache=>cache.addAll(SHELL))));
self.addEventListener("activate",event=>event.waitUntil(caches.keys().then(keys=>Promise.all(keys.filter(k=>k!==CACHE).map(k=>caches.delete(k))))));
self.addEventListener("fetch",event=>{{if(event.request.method!=="GET")return;event.respondWith(fetch(event.request).then(response=>{{const copy=response.clone();caches.open(CACHE).then(cache=>cache.put(event.request,copy));return response;}}).catch(()=>caches.match(event.request)));}});\n'''


def expected(reviewer: str, slug: str) -> dict[Path, str]:
    paths = paths_for(slug)
    doc = with_manifest_hash(build_manifest(reviewer, slug))
    return {paths["manifest"]: json.dumps(doc, ensure_ascii=False, indent=2) + "\n",
            paths["index"]: index_html(doc, reviewer, slug),
            paths["webmanifest"]: webmanifest(reviewer),
            paths["sw"]: service_worker(doc, slug)}


def drift_check() -> int:
    # H4371: each reviewer ballot (sarga_NN_<slug>.json) and its view-only twin
    # (sarga_NN.json) are built from the same sources by the same generator, so
    # they must carry the same notes. They diverged once, silently (kostina,
    # 25 QA-parked cards). Nothing in CI noticed. This is that missing check,
    # run for every reviewer slug whose ballots are on disk.
    failures = 0
    for slug in sorted(set(REVIEWER_SLUG.values())):
        missing = [f"sarga_{n:02d}_{slug}" for n in range(1, 69)
                   if not (OUT / f"sarga_{n:02d}_{slug}.json").exists()]
        if len(missing) == 68:
            continue  # no ballots for this reviewer at all — nothing to check
        if missing:
            print(f"FAIL: incomplete {slug} ballot set, first missing: {missing[0]}")
            failures += 1
            continue
        drift = []
        for n in range(1, 69):
            view = OUT / f"sarga_{n:02d}.json"
            ballot = OUT / f"sarga_{n:02d}_{slug}.json"
            if not view.exists():
                drift.append(f"sarga_{n:02d}: missing view-only twin")
                continue
            ids = lambda f: [x["id"] for v in json.loads(
                f.read_text(encoding="utf-8"))["verses"] for x in v["notes"]]
            if ids(view) != ids(ballot):
                drift.append(f"sarga_{n:02d}")
        if drift:
            print(f"FAIL: {slug} ballot and view-only twin disagree: "
                  + ", ".join(drift)
                  + f"\n      rebuild BOTH: build_sarga_apparatus.py <NN> and "
                    f"build_sarga_apparatus.py --reviewer "
                  + next(k for k, v in REVIEWER_SLUG.items() if v == slug)
                  + f" <NN>")
            failures += 1
    return failures


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--reviewer", default="Костина",
                    help="reviewer to build/check the portal for: "
                         + ", ".join(REVIEWER_SLUG) + " (default: Костина)")
    args = ap.parse_args()
    if args.reviewer not in REVIEWER_SLUG:
        print(f"FAIL: unknown reviewer {args.reviewer!r}; known: {', '.join(REVIEWER_SLUG)}")
        return 1
    slug = REVIEWER_SLUG[args.reviewer]
    outputs = expected(args.reviewer, slug)
    if args.check:
        errors = [str(path.relative_to(ROOT)) for path, content in outputs.items()
                  if not path.exists() or path.read_text(encoding="utf-8") != content]
        if errors:
            print("FAIL: stale/missing portal outputs: " + ", ".join(errors))
            return 1
    else:
        for path, content in outputs.items():
            path.write_text(content, encoding="utf-8")
    manifest = json.loads(outputs[paths_for(slug)["manifest"]])
    sargas = [row["sarga"] for row in manifest["sargas"]]
    if sargas != list(range(1, 69)) or len(set(sargas)) != 68:
        print("FAIL: manifest must contain exactly unique sargas 1–68")
        return 1

    failures = drift_check()
    if failures:
        return 1
    print(f"PASS: 68 {args.reviewer} ballots; manifest {manifest['manifest_hash']}; check={args.check}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

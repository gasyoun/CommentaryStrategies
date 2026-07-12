#!/usr/bin/env python3
"""Driver for the H784/H802/H804 MBh edition-apparatus rollout: runs
compare_editions_mbh.py + build_edition_apparatus.py for every parva number
given on the command line, then writes a per-parva README.md (mirroring the
Vanaparva/Virataparva prose pattern) and a top-level rollout summary.

Usage: python scripts/run_all_mbh_parvas.py 1 2 5 6 7 8 9 10 11 12 13 14 15 16 17 18
"""
import sys
import os
import json
import subprocess

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)

PARVA_NAMES = {
    1: "adiparva", 2: "sabhaparva", 3: "vanaparva", 4: "virataparva",
    5: "udyogaparva", 6: "bhishmaparva", 7: "dronaparva", 8: "karnaparva",
    9: "shalyaparva", 10: "sauptikaparva", 11: "striparva", 12: "shantiparva",
    13: "anushasanaparva", 14: "ashwamedhikaparva", 15: "ashramavasikaparva",
    16: "mausalaparva", 17: "mahaprasthanikaparva", 18: "swargarohanaparva",
}

GITIGNORE = """# These embed near-complete verbatim text from rights-restricted sources
# (BORI critical edition: "do not provide copies to others"; Nilakantha
# vulgate: rights-gated per mahabharata-nilakantha/NILAKANTHA_VULGATE_CENSUS.md).
# Local-only, regenerable via scripts/run_all_mbh_parvas.py -- never commit.
critical_only_and_variants.json
significant_absences.json
"""

README_TMPL = """# BORI/Poona критическое издание ↔ Нīлакантха-вульгата — {title_ru} (кн. {parva})

_Created: 12-07-2026 · Last updated: 12-07-2026_

> Часть [H804](https://github.com/gasyoun/Uprava/blob/main/handoffs/H804-Sonnet_CommentaryStrategies_mbh-edition-apparatus-remaining-parvas_12.07.26.md)
> (продолжение [H784](https://github.com/gasyoun/Uprava/blob/main/handoffs/H784-Sonnet_CommentaryStrategies_mahabharata_nilakantha_vs_critical_apparatus_12.07.26.md)/[H802](https://github.com/gasyoun/Uprava/blob/main/handoffs/H802-Sonnet_CommentaryStrategies_mbh-edition-apparatus-virataparva_12.07.26.md)) —
> тот же пайплайн, без изменений в скриптах. Источники и метод —
> [`../vanaparva/README.md`](../vanaparva/README.md).

## Итог по книге

| | Критическое (BORI) | Вульгата (Нилакантха) | Δ |
|---|---:|---:|---:|
| **Адхьяй** | **{crit_adhy}** | **{vulg_adhy}** | **{delta_adhy:+d}** |
| **Шлок** | **{crit_v}** | **{vulg_v}** (= перепись census) | **{delta_v:+d}** |

- Вульгата содержит **{n_extra} целых адхьяй без критического аналога**{extra_list} — не сверено построфно.
- Выравнивание: идентичных **{identical}** · вариантных **{variant}** (вкл. {fuzzy} fuzzy-пар) ·
  «только в критическом» **{crit_only}** · транспозиций {trans_v}/{trans_c}.
- Вульгатные шлоки без выравнивания = {vulg_only}: **{struct_abs} — истинное отсутствие**,
  **{reworded} — переформулировка**.
- Крупнейшие вульгата-only пассажи ({n_runs} runs): {top_runs}.

## Вариантный аппарат (helayo-Gotoh)

[`apparatus_mbh-{slug}_variants.json`](apparatus_mbh-{slug}_variants.json) /
[`APPARATUS_MBH-{SLUG}_VARIANTS.md`](APPARATUS_MBH-{SLUG}_VARIANTS.md) —
**{clean_variants} чистых вариантных пары** (из {input_pairs} difflib-«variant», {routed} слишком
переформулированы → в слой отсутствий, {cyr} кириллических загрязнений) → **{loci} позиционных
loci** по всем {n_adhy} адхьяям.

## Файлы

Та же четвёрка, что у Ванапарвы: `book_summary.json`, `concordance.json`,
`significant_absences.json` (gitignored), `critical_only_and_variants.json` (gitignored),
плюс апарат `apparatus_mbh-{slug}_variants.json`/`.md` (committed — короткие loci).

_Dr. Mārcis Gasūns_
"""

RU_NAMES = {
    "adiparva": "Ādипарва", "sabhaparva": "Сабхāпарва",
    "udyogaparva": "Удьйогапарва", "bhishmaparva": "Бхӣшмапарва",
    "dronaparva": "Дроṇапарва", "karnaparva": "Карṇапарва",
    "shalyaparva": "Шальяпарва", "sauptikaparva": "Саупатикапарва",
    "striparva": "Стрӣпарва", "shantiparva": "Шāнтипарва",
    "anushasanaparva": "Анушāсанапарва", "ashwamedhikaparva": "Ашвамедхикапарва",
    "ashramavasikaparva": "Āшрамавāсикапарва", "mausalaparva": "Маусалапарва",
    "mahaprasthanikaparva": "Махāпрастхāникапарва", "swargarohanaparva": "Сваргарохаṇапарва",
}


def run(cmd, **kw):
    print("+", " ".join(cmd), flush=True)
    r = subprocess.run(cmd, cwd=REPO, encoding="utf-8", **kw)
    if r.returncode != 0:
        raise SystemExit(f"FAILED: {' '.join(cmd)}")


def write_readme(parva_no, slug, outdir):
    bs = json.load(open(os.path.join(outdir, "book_summary.json"), encoding="utf-8"))
    sa = json.load(open(os.path.join(outdir, "significant_absences.json"), encoding="utf-8"))
    ap = json.load(open(os.path.join(outdir, f"apparatus_mbh-{slug}_variants.json"), encoding="utf-8"))
    bt = bs["book_totals"]
    runs = sorted(sa["runs"], key=lambda r: -r["count"])[:6]
    top_runs = " · ".join(f"{r['range']} ({r['count']})" for r in runs) or "нет"
    extra = bt["vulgate_extra_adhyayas"]
    extra_list = f" ({', '.join(str(x) for x in extra)})" if extra else ""
    text = README_TMPL.format(
        title_ru=RU_NAMES.get(slug, slug), parva=parva_no, slug=slug, SLUG=slug.upper(),
        crit_adhy=bt["critical_adhyayas"], vulg_adhy=bt["vulgate_adhyayas"],
        delta_adhy=bt["vulgate_adhyayas"] - bt["critical_adhyayas"],
        crit_v=bt["critical_verses"], vulg_v=bt["vulgate_verses"],
        delta_v=bt["delta_vulgate_minus_critical"],
        n_extra=len(extra), extra_list=extra_list,
        identical=bt["identical_verses"], variant=bt["variant_verses"],
        fuzzy=bt["fuzzy_paired_verses"], crit_only=bt["critical_only_verses"],
        trans_v=bt["transposed_vulgate_verses"], trans_c=bt["transposed_critical_verses"],
        vulg_only=bt["vulgate_only_verses"], struct_abs=bt["vulgate_structural_absence"],
        reworded=bt["vulgate_reworded"], n_runs=bt["vulgate_only_runs"], top_runs=top_runs,
        clean_variants=ap["totals"]["clean_variant_verses"],
        input_pairs=ap["totals"]["input_variant_pairs"],
        routed=ap["totals"]["reworded_verses_routed_to_footnote_layer"],
        cyr=ap["totals"]["cyrillic_contaminated_verses"],
        loci=ap["totals"]["apparatus_loci"], n_adhy=ap["totals"]["chapters"],
    )
    open(os.path.join(outdir, "README.md"), "w", encoding="utf-8").write(text)
    open(os.path.join(outdir, ".gitignore"), "w", encoding="utf-8").write(GITIGNORE)
    return bt, ap["totals"]


def main():
    parvas = [int(a) for a in sys.argv[1:]]
    if not parvas:
        raise SystemExit("usage: run_all_mbh_parvas.py PARVA_NO [PARVA_NO ...]")
    summary = []
    for n in parvas:
        slug = PARVA_NAMES[n]
        outdir = os.path.join(REPO, "data", "edition_comparison_mbh", slug)
        print(f"\n===== parva {n} ({slug}) =====", flush=True)
        run([sys.executable, "scripts/compare_editions_mbh.py", str(n)])
        run([sys.executable, "scripts/build_edition_apparatus.py",
             "--input", os.path.join(outdir, "critical_only_and_variants.json"),
             "--outdir", outdir,
             "--title", f"{RU_NAMES.get(slug, slug)} — BORI critical <-> Nilakantha vulgate variant apparatus",
             "--work-label", f"MBh-{slug.capitalize()}",
             "--other-key", "vulgate", "--chapter-label", "adhyaya"])
        bt, apt = write_readme(n, slug, outdir)
        summary.append((n, slug, bt, apt))

    print("\n\n===== ROLLOUT SUMMARY =====")
    for n, slug, bt, apt in summary:
        print(f"parva {n:2d} {slug:22s} crit={bt['critical_verses']:6d} vulg={bt['vulgate_verses']:6d} "
              f"loci={apt['apparatus_loci']:6d}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Сборка data-derived HTML-страниц из размеченного корпуса (шаг B4).

Единый источник истины: страница генерируется ИЗ data/<name>_markup_50.json по
шаблону templates/translator_template.html. Выход — pages/<translator>.html.

⚠️ Это НЕ заменяет рукописные *_commentary_analysis.html в корне репозитория:
те — развёрнутые аналитические эссе, содержательно богаче 50-нотной выборки.
Сгенерированные страницы — воспроизводимое табличное представление данных
(оси, URN, IAST), которое CI может пересобирать при изменении JSON.

Переиспользует scripts/profile_translator.py (без дублирования статистики).

Запуск:
    python scripts/build_pages.py
"""

import sys
import pathlib
from html import escape

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from profile_translator import load, profile, AXIS2_LABELS  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

ROOT = pathlib.Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "templates" / "translator_template.html"
OUT = ROOT / "pages"

# Метаданные переводчиков: полное имя, токен цвета (из css/commentary.css), корпус.
# Цвет — единый источник истины: токен --c-* в дизайн-системе, не дублируется здесь.
# Все --c-* достаточно тёмные для белого текста (контраст ≥ AA на заголовке таблицы).
TRANSLATORS = {
    "kalyanov":  ("В. И. Кальянов", "c-kal", "Махабхарата (полный академический перевод)"),
    "vassilkov": ("Я. В. Васильков, С. Л. Невелева", "c-vas", "Махабхарата (книги Вана, Карна и др.)"),
    "erman":     ("В. Г. Эрман", "c-erm", "Махабхарата, Бхишмапарва (с Бхагавадгитой)"),
    "grintser":  ("П. А. Гринцер", "c-gri", "Рамаяна (книги 1–4)"),
    "syrkin":    ("А. Я. Сыркин", "c-syr", "Упанишады"),
    "leonov":    ("М. А. Леонов, ред. Е. Костина", "c-leo", "Рамаяна, книга 5 (Сундараканда) — продолжающийся перевод"),
}


def summary(p):
    topics = ", ".join(f"{t} ({v})" for t, v in p["topics"].most_common(3))
    a2 = p["axis2"].most_common(1)[0][0]
    a4 = p["axis4"].most_common(1)[0][0]
    return (f"Золотая выборка из {p['n']} примечаний. "
            f"Медиана длины {p['len_median']} знаков, IAST в {p['iast_pct']}% примечаний, "
            f"многотемность {p['multi_topic_pct']}%. "
            f"Темы-лидеры: {topics}. "
            f"По номенклатуре Казанского преобладает «{AXIS2_LABELS.get(a2, a2)}»; "
            f"по Парибку — преимущественно «{a4}».")


def strategy(p):
    a2 = AXIS2_LABELS.get(p["axis2"].most_common(1)[0][0], "")
    top = p["topics"].most_common(1)[0][0]
    return f"{a2}; {top}-доминанта; IAST {p['iast_pct']}%"


def notes_table(records):
    rows = []
    for r in records:
        axes = " · ".join([
            r["axis_2_kazansky"], r["axis_4_paribok"],
            "+".join(r.get("axis_3_lakshana", [])) or "—",
            "+".join(r.get("axis_1_topic", [])),
        ])
        iast = "✓" if r.get("has_iast") else "—"
        rows.append(
            f'    <tr><td class="urn">{escape(r.get("urn",""))}</td>'
            f'<td>{escape(r["shloka_addr"])}</td>'
            f'<td class="axes">{escape(axes)}</td>'
            f'<td class="iast">{iast}</td>'
            f'<td>{escape(r.get("raw_text",""))}</td></tr>'
        )
    style = (
        "<style>"
        ".data-table{width:100%;border-collapse:collapse;font-size:.85rem;margin-top:1rem}"
        ".data-table th,.data-table td{border-bottom:1px solid var(--tr-bg,#eee);"
        "padding:.45rem .5rem;text-align:left;vertical-align:top}"
        ".data-table th{position:sticky;top:0;background:var(--tr-color,#333);color:#fff}"
        ".data-table .urn{font-family:monospace;font-size:.72rem;white-space:nowrap;color:#666}"
        ".data-table .axes{white-space:nowrap;font-size:.78rem;color:var(--tr-color,#333)}"
        ".data-table .iast{text-align:center}"
        ".gen-note{font-size:.8rem;color:#777;font-style:italic}"
        ".table-scroll{overflow-x:auto;-webkit-overflow-scrolling:touch}"
        "</style>"
    )
    return (style +
            '\n    <p class="gen-note">Таблица сгенерирована из данных автоматически '
            '(scripts/build_pages.py). Полная аналитика — в рукописной странице '
            '*_commentary_analysis.html.</p>\n'
            '    <div class="table-scroll">\n'
            '    <table class="data-table">\n'
            '      <thead><tr><th>URN</th><th>Адрес</th><th>Оси (Каз.·Париб.·lakṣ.·темы)</th>'
            '<th>IAST</th><th>Текст примечания</th></tr></thead>\n'
            '      <tbody>\n' + "\n".join(rows) + '\n      </tbody>\n    </table>\n    </div>')


def build(name, template):
    records = load(name)
    p = profile(name, records)
    full, token, desc = TRANSLATORS[name]
    color = f"var(--{token})"      # ссылка на токен дизайн-системы
    light = "var(--card)"           # светлый нейтральный фон/граница из дизайн-системы
    repl = {
        "{{TRANSLATOR_NAME}}": escape(full.split(",")[0]),
        "{{TRANSLATOR_FULL_NAME}}": escape(full),
        "{{PROJECT_DESCRIPTION}}": escape(desc),
        "{{COLOR_HEX}}": color,
        "{{COLOR_LIGHT_HEX}}": light,
        "{{TOTAL_NOTES}}": str(p["n"]),
        "{{IAST_PCT}}": str(p["iast_pct"]),
        "{{AVG_LENGTH}}": str(int(p["len_mean"])),
        "{{ANALYTICAL_SUMMARY}}": escape(summary(p)),
        "{{STRATEGY_TYPE}}": escape(strategy(p)),
        "{{EXAMPLES_HTML}}": notes_table(records),
    }
    html = template
    for k, v in repl.items():
        html = html.replace(k, v)
    return html


def main():
    OUT.mkdir(exist_ok=True)
    template = TEMPLATE.read_text(encoding="utf-8")
    for name in sorted(TRANSLATORS):
        dest = OUT / f"{name}.html"
        dest.write_text(build(name, template), encoding="utf-8")
        print(f"✓ {dest.relative_to(ROOT)}")
    print(f"\nСобрано {len(TRANSLATORS)} страниц из data/*_markup_50.json.")


if __name__ == "__main__":
    main()

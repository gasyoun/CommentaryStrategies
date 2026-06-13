#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Единый источник истины для кодов 4-осной таксономии — читается ИЗ схемы.

Коды осей (A/B/V/G, P/K/D, L1–L5, темы axis_1) и список переводчиков берутся
напрямую из data/commentary_schema.json, чтобы они НЕ МОГЛИ разойтись со схемой.
Именно расхождение дублированных копий породило баги, найденные в код-ревью
(translator-enum «vasilkov» vs данные «vassilkov»; пропуск «poetics» в enum).

Подписи (человекочитаемые labels) намеренно остаются в скриптах-потребителях:
у export_tei (TEI <catDesc>) и profile_translator (отчёт) разный стиль подписей.
Но КОДЫ — единые, отсюда; а `assert_covers()` ловит дрейф любой карты подписей.
"""

import json
import pathlib

SCHEMA_PATH = pathlib.Path(__file__).resolve().parent.parent / "data" / "commentary_schema.json"
_SCHEMA = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
_PROPS = _SCHEMA["properties"]

# Коды — из схемы (единый источник истины)
TRANSLATORS    = _PROPS["translator"]["enum"]
AXIS1_TOPICS   = _PROPS["axis_1_topic"]["items"]["enum"]
AXIS2_KAZANSKY = _PROPS["axis_2_kazansky"]["enum"]
AXIS3_LAKSHANA = _PROPS["axis_3_lakshana"]["items"]["enum"]
AXIS4_PARIBOK  = _PROPS["axis_4_paribok"]["enum"]
REQUIRED       = _SCHEMA.get("required", [])
URN_PREFIX     = "urn:cts:sanskritLit:"


def assert_covers(label_map, codes, name):
    """Карта подписей потребителя должна покрывать РОВНО коды схемы.

    Падает при дрейфе (схема получила/потеряла код, а карта подписей — нет),
    превращая молчаливое расхождение в громкую ошибку на импорте/в CI.
    """
    missing = set(codes) - set(label_map)
    extra = set(label_map) - set(codes)
    if missing or extra:
        raise ValueError(
            f"{name}: подписи разошлись со схемой — "
            f"нет подписи для {sorted(missing)}; лишние {sorted(extra)}")

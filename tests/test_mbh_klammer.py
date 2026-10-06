"""mbh_klammer.py — H6055 full-Mahābhāṣya Klammeranalyse, hermetic unit tests.

No network, no live data/: the module's parse/tokenize/segment/κ primitives
are exercised on synthetic fixtures only (the build itself needs the
gitignored source mirror, which CI never fetches).
"""
import importlib.util
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SPEC = importlib.util.spec_from_file_location("mbh_klammer", REPO / "scripts" / "mbh_klammer.py")
assert SPEC is not None and SPEC.loader is not None
mod = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(mod)

VOCAB = {"समास", "अन्त", "वृद्धि", "आदैच्", "इति", "दोष", "भाष्यम्", "प्रत्यय", "लक्षणेन"}


def test_parse_layer_both_upstream_shapes():
    bhashya_json = '{"11001": "वृद्धिरादैच् ॥[[1.1.1]] ॥ ऽकारः"}'
    rows = mod.parse_layer("bhashya", bhashya_json)
    assert rows[0]["sutra"] == "1.1.1"
    assert "[[" not in rows[0]["text"] and "ऽ" not in rows[0]["text"]
    vartika_json = '{"name": "vartika", "data": [{"sutra": "1.1.9", "vartika": "ऋऌवर्णयोर्मिथः सावर्ण्यं वाच्यम् ।"}]}'
    rows = mod.parse_layer("vartika", vartika_json)
    assert rows[0]["sutra"] == "1.1.9" and "वाच्यम्" in rows[0]["text"]


def test_tokenize_keeps_devanagari_drops_noise():
    toks = mod.tokenize("कुत्वं कस्मान्न भवति ॥ 1.1.1 (a)")
    assert toks == ["कुत्वं", "कस्मान्न", "भवति"]


def test_tokenize_danda_digits_are_separators_not_word_chars():
    # verifier finding (cou-2): U+0964/0965 daṇḍa and Devanagari digits must
    # never end up inside a token — they inflated the census as प्राप्नोति।
    toks = mod.tokenize("प्राप्नोति। प्राप्नोति॥ वक्तव्यम्। १२३कर्तव्यम्")
    assert toks == ["प्राप्नोति", "प्राप्नोति", "वक्तव्यम्", "कर्तव्यम्"], toks


def test_segmenters_split_true_compound_both_directions():
    assert mod.seg_left("दोषभाष्यम्", VOCAB) == ["दोष", "भाष्यम्"]
    assert mod.seg_right("दोषभाष्यम्", VOCAB) == ["दोष", "भाष्यम्"]
    assert mod.seg_left("प्रत्ययलक्षणेन", VOCAB) == ["प्रत्यय", "लक्षणेन"]


def test_segmenters_fail_loud_on_unknown_residue():
    assert mod.seg_left("दोषqqqq", VOCAB) is None
    assert mod.seg_right("qqqqदोष", VOCAB) is None


def test_directional_greed_converges_on_short_ambiguous_form():
    # अन्तइति: both directions resolve to the same two members — the
    # short-form convergence case (divergence lives in the long tail, which
    # the κ sample + disagreement bank capture).
    assert mod.seg_left("अन्तइति", VOCAB) == ["अन्त", "इति"]
    assert mod.seg_right("अन्तइति", VOCAB) == ["अन्त", "इति"]


def test_kappa_reference_properties():
    assert mod.cohen_kappa(["a", "b"], ["a", "b"]) == 1.0
    # pure disagreement beyond chance -> negative
    k = mod.cohen_kappa(["a", "a", "b", "b"], ["b", "b", "a", "a"])
    assert k < 0
    # symmetric chance-alignment ~ 0
    k = mod.cohen_kappa(["a", "a", "b", "b"], ["a", "b", "a", "b"])
    assert abs(k) < 0.01


def test_boundary_labels_codepoint_offsets():
    assert mod.boundary_labels("दोषभाष्यम्", ["दोष", "भाष्यम्"]) == {3}


def test_selftest_entrypoint_runs_green(capsys):
    mod.selftest()
    assert "SELFTEST PASS" in capsys.readouterr().out


def test_cli_surface():
    # build/check/selftest are the three documented modes; no mode prints help
    assert hasattr(mod, "build") and hasattr(mod, "check") and hasattr(mod, "selftest")

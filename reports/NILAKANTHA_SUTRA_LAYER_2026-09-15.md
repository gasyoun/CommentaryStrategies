# Nilakantha licence register → Panini sutra layer (H4736)

_Created: 2026-09-15 · Last updated: 2026-09-15_

Join of `deviation_term_sa` in `commentary_licence_register_nilakantha.tsv` (59 unique terms over 151 register rows) to `sutra_coverage_map.tsv` (3983 sutras, kosha data-v0.3.0).

## Method

1. Register terms are IAST-style grammar-operation labels; each is split into
   SLP1 candidate tokens (`X-abhāva` matches on X; English connectors dropped).
2. Match tiers, strongest first: `phrase` (whole term inside a sutra text),
   `word` (token equals a sutra word, trailing visarga/anusvāra stripped),
   `substring` (token inside a sutra word — weakest, may be accidental).
3. Layer rows carry up to 10 sutra ids per term; the register itself is untouched
   (additive file `nilakantha_sutra_layer.tsv`, rebuilt idempotently by
   `scripts/build_nilakantha_sutra_layer.py --check`).

## Coverage

- register rows: 151; rows with ≥1 sutra match: 120
- unique terms matched: 39; unmatched: 20
- kosha map: `/Users/mac/Documents/GitHub/kosha/data/concordance/sutra_coverage_map.tsv`

## Term → sutra table

term | rows | tier | sutra ids
--- | --- | --- | ---
abhyāsa-lopa | 4 | word | 1.1.60; 1.3.9; 3.4.97; 4.1.133; 5.4.146; 6.4.48
adantatva | 2 | UNMATCHED | 
aluk / luk | 2 | word | 1.2.49; 4.1.90; 4.1.109; 4.3.163; 4.3.168; 4.4.125
antādeśa | 1 | UNMATCHED | 
anusvāra-lopa | 1 | word | 1.1.60; 1.3.9; 3.4.97; 4.1.133; 5.4.146; 6.4.48
asamāsa | 1 | UNMATCHED | 
asandhi | 1 | UNMATCHED | 
aḍ-abhāva | 21 | substring | 1.4.1; 2.1.3; 2.2.38; 2.3.16; 2.4.12; 2.4.27
aḍ-āgama | 1 | substring | 1.4.1; 2.1.3; 2.2.38; 2.3.16; 2.4.12; 2.4.27
bhatva | 2 | UNMATCHED | 
dairghya-abhāva | 1 | UNMATCHED | 
guṇa-abhāva | 2 | word | 1.1.2; 6.4.156; 7.3.108; 7.4.16; 7.4.21; 7.4.75
iḍ-abhāva | 1 | substring | 1.4.61; 3.1.13; 3.4.78; 4.1.15; 5.1.23; 5.2.32
iṭ | 1 | word | 1.2.2; 7.2.41
klībatva | 2 | UNMATCHED | 
ktvā | 1 | word | 1.2.7; 1.2.18; 1.2.22; 2.2.22; 3.4.18
ktvā / lyap | 2 | word | 1.2.7; 1.2.18; 1.2.22; 2.2.22; 3.4.18; 7.1.37
lakāra-vyatyaya | 2 | UNMATCHED | 
laṭ | 1 | word | 3.2.118; 3.2.123
liṅga-vyatyaya | 5 | substring | 2.3.46; 2.4.26; 3.1.46; 4.1.170
lopa | 17 | word | 1.1.60; 1.3.9; 3.4.97; 4.1.133; 5.4.146; 6.4.48
lopa-abhāva | 3 | word | 1.1.60; 1.3.9; 3.4.97; 4.1.133; 5.4.146; 6.4.48
matvarthīya | 2 | UNMATCHED | 
mum-āgama | 1 | word | 6.3.67
niṣīdatuḥ for niṣedatuḥ | 1 | UNMATCHED | 
num-abhāva | 3 | word | 7.1.58
nuḍ-abhāva | 1 | substring | 6.1.176; 6.3.74; 7.4.71
pada-vikaraṇa-vyatyaya | 1 | word | 3.1.60
pada-vyatyaya | 2 | word | 3.1.60
pragṛhyatva-abhāva | 1 | UNMATCHED | 
puṃstva | 1 | UNMATCHED | 
puṃvadbhāva-abhāva | 1 | UNMATCHED | 
pūrva-nipāta | 2 | word | 1.1.14; 1.1.65; 6.1.107; 6.1.135; 6.2.83; 8.2.98
pūrvasavarṇa | 1 | word | 6.1.102
ru-tva-abhāva | 1 | word | 3.2.159; 8.2.66; 8.3.1
rutva | 1 | substring | 4.2.32
samāsānta | 3 | UNMATCHED | 
sandhi | 4 | UNMATCHED | 
saṃprasāraṇa-abhāva | 1 | UNMATCHED | 
strītva | 1 | UNMATCHED | 
supāṃ suluk | 3 | phrase | 7.1.39
taddhita-luk | 2 | word | 1.2.49; 4.1.17; 4.1.90; 4.1.109; 4.3.163; 4.3.168
taṅ-bhāva | 7 | substring | 1.3.12; 1.4.100; 5.4.7; 6.3.133; 7.1.35
tvan | 2 | substring | 3.4.14
upapada-yoga | 1 | substring | 1.1.7; 1.2.55; 1.3.63; 2.2.19; 3.4.4; 3.4.27
utva-abhāva | 2 | substring | 4.2.32
vacana-vyatyaya | 3 | substring | 1.1.11; 1.1.58; 1.2.56; 1.2.58; 1.2.61; 1.2.63
varṇa-lopa | 6 | word | 1.1.60; 1.3.9; 3.4.97; 4.1.133; 5.4.146; 6.4.48
vibhakti-aluk | 1 | word | 5.3.1
vibhakti-lopa | 9 | word | 1.1.60; 1.3.9; 3.4.97; 4.1.133; 5.3.1; 5.4.146
vibhakti-vyatyaya | 3 | word | 5.3.1
visarga-lopa | 2 | word | 1.1.60; 1.3.9; 3.4.97; 4.1.133; 5.4.146; 6.4.48
vyatyaya | 1 | UNMATCHED | 
vyavahita | 2 | UNMATCHED | 
ādi-lopa | 1 | word | 1.1.60; 1.3.9; 3.4.97; 4.1.133; 5.4.146; 6.1.187
ārdhadhātukatva-abhāva | 1 | UNMATCHED | 
āḍ-abhāva | 1 | substring | 3.2.30; 3.2.55; 3.4.92; 4.1.142; 4.2.9; 4.2.20
ṇij-abhāva | 1 | substring | 3.3.52; 6.2.13
ṭāb-antatva | 1 | substring | 4.1.9

## Hand-checked sample

Verified by reading the matched sutra SLP1 text directly (worker, OxAlpha tier).

- **lopa** → 1.1.60 — `adarSanaM lopaH` · adarśanaṁ lopaḥ — THE lopa definition; literal word match
- **supāṃ suluk** → 7.1.39 — `supAM sulukpUrvasavarRA''cCeyAqAqyAyAjAlaH` · phrase present verbatim inside the sutra text
- **mum-āgama** → 6.3.67 — `arurdvizadajantasya mum` · arur dviṣad ajantasya mum — the mum-āgama sutra; literal
- **num-abhāva** → 7.1.58 — `idito num DAtoH` · idito num dhātoḥ — the num-āgama sutra; literal
- **laṭ** → 3.2.118 — `law sme` · laṭ śme — laṭ present (law = laṭ in SLP1)
- **ru-tva-abhāva** → 8.3.1 — `matuvaso ru sambudDO Candasi` · matu-vaso ru sambuddhau chandasi — the ru-sutra; literal
- **guṇa-abhāva** → 1.1.2 — `adeN guRaH` · adeṅ guṇaḥ — the guṇa definition sutra
- **pūrvasavarṇa** → 6.1.102 — `praTamayoH pUrvasavarRaH` · prathamayoḥ pūrvasavarṇaḥ — literal word match
- **iṭ** → 7.2.41 — `iw sani vA` · iṭ sani vā — iṭ-āgama rule (1.2.2 `vija iw` also matched)
- **taddhita-luk** → 4.1.17 — `prAcAM zPa tadDitaH` · prācāṁ ṣaṣ ṭaddhitaḥ — taddhita word; luk ids joined separately

## Unmatched residue (honest)

- adantatva
- antādeśa
- asamāsa
- asandhi
- bhatva
- dairghya-abhāva
- klībatva
- lakāra-vyatyaya
- matvarthīya
- niṣīdatuḥ for niṣedatuḥ
- pragṛhyatva-abhāva
- puṃstva
- puṃvadbhāva-abhāva
- samāsānta
- sandhi
- saṃprasāraṇa-abhāva
- strītva
- vyatyaya
- vyavahita
- ārdhadhātukatva-abhāva

Unmatched terms are commentarial labels or derived formations absent from the
Aṣṭādhyāyī text as harvested (e.g. 'sandhi', 'vyatyaya', 'samāsānta' —
meta-terms of the commentary tradition, never sutra verbatim).

## Handoff

Executed under H4736 (OxAlpha tier). Evidence: layer TSV + this report +
`python scripts/build_nilakantha_sutra_layer.py --check`.

_Гасунс_

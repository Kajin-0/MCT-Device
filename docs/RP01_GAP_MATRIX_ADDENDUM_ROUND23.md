# RP-01 gap matrix addendum — Round 23: Te-rich horizontal-slider LPE execution

## Scope

This addendum tracks what Round 23 closed empirically for P03/P30 and what remains unresolved for exact RP-01 reproduction.

| Variable | Round-23 state | Evidence / disposition |
|---|---|---|
| Growth family | CLOSED AS PROCESS FAMILY | Te-rich atmospheric-pressure horizontal-slider LPE directly supported in Honeywell/Harman lineage |
| x≈0.30 tie-line center | DIRECT HISTORICAL HONEYWELL | `xL=.082`, `yL=.810`, `TL=507 °C` -> `xS=.29` |
| Total charge mass for x=.29 branch | OPEN | Honeywell patent gives composition, not total mass |
| Complete boat dimensions | OPEN | topology direct; machining dimensions not recovered |
| Boat topology | STRONGLY CLOSED | covered graphite base/slider/cover + solution well + substrate recess + auxiliary Hg source + moats |
| Nitrogen purge before heat | DIRECT HONEYWELL | exact flow/duration OPEN |
| Flowing H2 during growth | DIRECT HONEYWELL/HARMAN | exact flow/purity controls OPEN |
| Hg-loss compensation principle | DIRECT HONEYWELL | HgTe or HgTe+Te auxiliary source |
| Hg source mass | OPEN FOR x=.29 | RSG `3 g` is transfer-only |
| Source synthesis for RP-01 branch | OPEN | RSG gives strong separate empirical branch |
| RSG source synthesis | DIRECT TRANSFER | 10 g, 6N Hg/Cd/Te, evacuated quartz ampoule, 700 °C/8 h, grind/mix, ~4.8 g/run |
| In-situ solution preparation | ALTERNATE PRIMARY BRANCH | Bernardi 1988; do not merge into ampoule branch |
| Equilibration scale | PARTIAL | Harman ~1 h at 550 °C; exact x=.29 condition OPEN |
| Heat above liquidus before growth | DIRECT HONEYWELL | exact overshoot/hold OPEN |
| Thermal trajectory families | DIRECT HONEYWELL | step supercool / slow cooling / combination |
| Exact x=.29 supercooling | OPEN | 500 °C vs TL=507 gives 7 K derived screening point only |
| Growth contact method | CLOSED IN PRINCIPLE | slide well over substrate, later slide away |
| Growth duration | PARTIAL / BRANCH-DEPENDENT | Harman 0.25–10 min; Honeywell patent ~30-min example; exact RP-01 OPEN |
| Layer-thickness sensitivity to thermal path | DIRECT TRANSFER | Shinohara: 2–4 µm equilibrium-cooling vs 30–40 µm at 15 K step/supercool branch |
| Slider speed | OPEN | must be locally calibrated |
| Slider clearance | PHYSICAL REQUIREMENT IDENTIFIED | finite clearance avoids scratching; exact value OPEN |
| Wipe-off as controlled unit operation | CLOSED CONCEPTUALLY | Honeywell patents directly document residual-film/drop problem |
| CdTe-piece wipe-off | DIRECT HONEYWELL OPTION | pieces in slots ~1 mm apart; distinct hardware generation |
| Scribed CdTe apron | DIRECT HONEYWELL OPTION | tandem apron, diagonal scribes; distinct hardware generation |
| Exact RP-01 wipe-off hardware | OPEN | no evidence which generation produced supplier material |
| Post-contact cooldown | OPEN | must record full T(t) locally |
| Melt reuse / source depletion | OPEN HISTORICALLY | P03D/P30 define local genealogy controls |
| Downstream release | DEFINED | P06 x/thickness + morphology + P05 transport + later device outcome |

## New hard rules from Round 23

1. **Composition does not define charge mass.** `xL/yL` may not be converted into an absolute recipe until the growth-well geometry and selected total mass are defined.
2. **Do not merge growth-time branches.** Harman’s 0.25–10 min data and Honeywell’s ~30-min patent example are not values to average.
3. **Do not merge source-preparation branches.** Sealed-ampoule synthesis and in-situ vapor-transport preparation are separate recipe families.
4. **Do not merge wipe-off hardware generations.** The CdTe-piece well and the scribed CdTe apron are distinct Honeywell implementations.
5. **Slider motion is a material-process variable.** Clearance, speed, smoothness and separation temperature affect scratches, residual films and usable area.
6. **Thermal trajectory is a function, not a scalar.** `T_contact` alone does not reproduce supercooling history or thickness.
7. **Hg-source inventory is genealogical.** Source mass/geometry/reuse must be tracked with run-order composition drift.

## Highest-priority remaining LPE blockers

- exact Honeywell/Fermionics boat dimensions or engineering drawing;
- x≈0.29 total charge mass and melt height;
- actual source synthesis for the RP-01 supplier material;
- exact gas flows/purity/dew point;
- exact thermocouple location and thermal calibration;
- actual equilibration T/time;
- actual supercooling/cooling rate;
- actual contact duration for ~9.5 µm layer;
- slider speed/clearance;
- wipe-off hardware generation;
- cooldown and source reuse history.

# RP-01 gap matrix addendum — Round 24 Hg-overpressure annealing

**Date:** 2026-08-16

## Summary

Round 24 upgrades P04/P23 with P31, an empirical anneal apparatus/reservoir/trajectory layer. The carrier-state physics is substantially constrained, but the exact historical RP-01 anneal remains unrecovered.

| Process coordinate / outcome | Direct RP-01 | Primary transfer evidence | Current status | Release action |
|---|---|---|---|---|
| final x≈0.30, 9.5 µm, n≈9.8e14, µ≈4e4 | yes | — | `DIRECT-FINAL-STATE` | preserve as material target |
| exact historical anneal architecture | no | sealed, open-tube, in-situ all documented elsewhere | `OPEN` | local architecture must receive distinct recipe ID |
| sample temperature `T_s` | no | 250–300 °C strong low-T transfer region; Harman 250 °C/1 h | `CANDIDATE-P` | calibrate actual sample T, not controller only |
| Hg reservoir temperature `T_Hg` | no | Jones isothermal/two-temperature; TI two-zone examples | `CANDIDATE-P` | independent source-zone thermometry |
| Hg partial pressure / chemical potential | no | controlled by reservoir in primary studies | `EMPIRICAL-REQUIRED` | qualified source relation + geometry + state outcome |
| elemental-Hg reservoir mass | no | “enough for saturation” in patents, no universal mass | `OPEN` | determine local minimum inventory with margin; do not invent |
| source type | no | elemental Hg, HgTe and in-situ sources in distinct branches | `OPEN/HISTORICAL` | freeze one local source class per recipe |
| ampoule material | no | sealed quartz common primary branch | `TRANSFER-STRONG` | select/qualify local quartz architecture |
| ampoule ID/length/free volume | no | not recovered for RP-01 | `OPEN` | record local measured geometry |
| sample/source spacing | no | remote opposite ends in two-zone TI patent | `TRANSFER-STRONG` | local furnace/ampoule geometry qualification |
| furnace zones | no | two-zone architecture directly demonstrated | `TRANSFER-STRONG` | map both zones and cross-coupling |
| ramp rate | no | not recovered | `OPEN` | log local ramp; sensitivity later |
| dwell time | no | 250 °C/1 h Harman; bulk branches hours-days | `CANDIDATE-P / THICKNESS-DEPENDENT` | local time map on 9.5-µm x≈0.30 material |
| 400 °C use | no | Nagahama shows interface composition change; TI uses high-T defect branches | `SEPARATE-BRANCH` | exclude from first low-T stoichiometry screen |
| cooldown `T_s(t)` | no | primary multi-step/incremental cooling evidence | `EMPIRICAL-REQUIRED` | log complete trace |
| cooldown `T_Hg(t)` | no | two-zone sources show source/sample relation is causal | `EMPIRICAL-REQUIRED` | log complete trace |
| source coupling end point | no | not recovered | `OPEN/CAL` | define local criterion and timestamp |
| Hg condensation/dissolution avoidance | no | explicit TI two-zone warning | `TRANSFER-STRONG` | define source/sample temperature relationship |
| p↔n state boundary | no | Jones + P23 physics | `EMPIRICAL-REQUIRED` | signed Hall/tensor boundary map |
| final n-like response surface | no | — | `EMPIRICAL-REQUIRED` | P23 local Jacobian inside stable n-like region |
| Hall interpretation near transition | no | multicarrier physics | `CONTROLLED` | do not use reciprocal Hall density through sign change |
| composition preservation | final x only | Nagahama 250–300 good; 400 °C warning | `EMPIRICAL-REQUIRED` | pre/post P06 same-site map |
| Te precipitate response | no | low-T Hg can annihilate precipitates | `TRANSFER-STRONG` | inspect development coupons |
| dislocation multiplication risk | no | Schaake 1985 | `TRANSFER-STRONG` | pre/post defect metric where possible |
| high-T dislocation-control preanneal | no | TI patents 350–650 °C branches | `NOT-BASELINE` | only add if local starting material demands it |
| surface/passivation state during anneal | no | known to influence Hg exchange in other branches | `OPEN/QUAL` | freeze/record surface state |
| anneal repeatability across P30 runs | no | — | `EMPIRICAL-REQUIRED` | multiple independent growth + anneal genealogies |
| detector-level closure | RP-01 final performance only | — | `EMPIRICAL-REQUIRED` | P10/P11/P12/P13 confirmation |

## Highest-priority unresolved factual recovery

1. any Fermionics/UWA record identifying the actual anneal applied to the purchased RP-01 LPE material;
2. exact post-growth anneal details from the Nagahama x≈0.30 branch;
3. full Jones et al. experimental table/figures for exact `T_s`, `T_Hg`, time and resulting electrical states;
4. exact Harman in-situ anneal Hg-source temperature/pressure trajectory around the 250 °C/1 h example;
5. direct pressure-temperature relation/source used by the selected local elemental-Hg reservoir;
6. whether the historical RP-01 material arrived already annealed to the quoted n/µ state and therefore had no UWA-controlled P04 step.

## Process decision retained

The first local transfer branch should remain:

`x≈0.30 matched LPE coupons -> quantitatively Hg-controlled enclosure -> T_s≈250 °C -> isothermal/Hg-saturated-like state -> first time anchor ~1 h -> controlled retained-Hg cooldown -> P05/P06 closure`.

Every term is `QUALIFICATION-CANDIDATE`, not production release.

## Permanent prohibitions added by Round 24

- do not write “250 °C Hg anneal” without source/sample boundary condition;
- do not set `T_Hg=T_s` by controller command without demonstrating actual spatial equivalence;
- do not infer an Hg reservoir mass from another ampoule volume;
- do not copy multi-day bulk-slice times to a 9.5-µm epilayer;
- do not collapse high-T dislocation reduction and low-T vacancy control into one anneal step;
- do not accept n-type conversion without optical/defect preservation and Hall-model validity;
- do not omit cooldown from the controlled process.

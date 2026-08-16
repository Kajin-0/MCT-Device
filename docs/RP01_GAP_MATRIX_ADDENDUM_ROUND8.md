# RP-01 gap-matrix addendum — source-recovery round 8

**Date:** 2026-08-15 America/New_York

This addendum records the upstream source-preparation, melt-inventory/depletion and substrate-face/miscut overrides introduced after round 7.

| Module | Variable / evidence required | Current status | Round-8 interpretation |
|---|---|---|---|
| LPE source | historical x≈0.30 source-synthesis method | OPEN / CONTROLLED-QUAL | Honeywell patent starts with an already-prepared Te-rich charge; synthesis route not disclosed. P03C locally qualifies source preparation by mass closure, homogenization, liquidus behavior and resulting material quality. |
| LPE source | candidate sealed-elemental synthesis | CANDIDATE-P / QUAL | Related Radhakrishnan branch uses 6N Hg/Cd/Te, evacuated quartz, 700 °C/8 h, then grinding/mixing. Different x≈0.20 family; not direct Honeywell recipe. |
| LPE source | in-situ source preparation | DIFFERENT-BRANCH / RESEARCH OPTION | 1988 Te-solution process demonstrates Hg-vapor transport into Cd-rich Te melt; technically valid but not historical Honeywell. |
| LPE source | source-conditioning/reuse state | CONTROLLED-QUAL | P03C requires run-order/source-lot tracking and a maximum qualified use/depletion criterion. |
| LPE | historical charge mass | OPEN / CAL | Bowers–Schmit patent gives no gram quantity. Do not assign Radhakrishnan 4.8 g to x≈0.30 Honeywell process. |
| LPE | historical well volume/depth | OPEN / CAL | Patent describes tapered through-wells but no diameter/depth/volume. P03D requires dimensioned local geometry. |
| LPE | effective liquid depth/inventory | CONTROLLED-QUAL | P03D converts measured charge mass + density/geometry into effective liquid inventory/depth and propagates uncertainty. |
| LPE | finite-liquid depletion | CONTROLLED-QUAL | Primary 1990 model shows growth rate falls after a liquid-depth-related characteristic time and Hg loss can drive layer Cd-richer. Must be evaluated against local growth time/inventory. |
| LPE | run-order composition drift | CONTROLLED-QUAL | Track x/thickness/morphology vs source-use index and release a source depletion limit from measured output drift. |
| LPE | Hg-loss control | CANDIDATE-P / CONTROLLED-QUAL | Honeywell covered Hg-source architecture direct; independent x=0.30 Suh 1992 branch confirms Hg-loss-control geometry can stabilize solution composition. Local geometry/mass remains apparatus-specific. |
| LPE | substrate-area scaling | CONTROLLED-QUAL | Preserve physically relevant melt-volume/area or effective liquid-depth state, not same gram mass or simple linear mass scaling. |
| Substrate | exact RP-01 plane/polarity | OPEN / CONTROLLED-QUAL | RP-01/Honeywell public text still does not state face. Do not assign A/B historically. |
| Substrate | composition-matched face evidence | CANDIDATE-P / NONHISTORICAL | Independent x=0.30 Te-rich slider work used `(111)Cd` CdTe. Useful DOE anchor, not RP-01 closure and not CdZnTe. |
| Substrate | miscut screening range | CONTROLLED-QUAL | x=0.30 study: 1° miscut gives terrace morphology tied to miscut direction; above ~2° terraces begin becoming wave-like. Use 0–2° neighborhood as composition-matched DOE information, not historical spec. |
| Substrate | miscut azimuth | CONTROLLED-QUAL | 1° miscut toward four directions changed terrace-front orientation; record azimuth explicitly. |
| Substrate | morphology vs growth time | CONTROLLED-QUAL | independent x=0.30 study shows early wave-like surface evolves toward terraces and terrace width increases with growth time; face/miscut and P03B growth-time studies are coupled. |
| Substrate | final local face/miscut release | QUAL | Select by `Y_face={morphology, thickness uniformity, x uniformity, twin/defect metric, mobility, lifetime, usable area}` over repeated runs. |

## Round-8 control rule

The upstream process must not be represented as a single fixed recipe until four coupled apparatus/material states are locally closed:

`source preparation -> melt inventory/depletion -> substrate face/surface -> time/supercooling trajectory`.

The resulting material gate remains P05/P06/P13:

`{thickness/x maps, Hall/mobility state, morphology/crystal quality, lifetime/device proxy}`.

## Governing files

- `procedures/P03C_TE_RICH_SOURCE_SYNTHESIS_HOMOGENIZATION_QUALIFICATION.md`
- `procedures/P03D_LPE_MELT_INVENTORY_DEPLETION_QUALIFICATION.md`
- `procedures/P07B_CZT_FACE_MISCUT_LPE_SELECTION_QUALIFICATION.md`
- P03/P03A/P03B/P07/P07A.

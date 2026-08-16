# RP-01 gap matrix addendum — Round 27 — RIE reactor equivalence

**Date:** 2026-08-16 America/New_York

| Variable / function | Current evidence | Status after Round 27 | Required closure |
|---|---|---|---|
| Reactor manufacturer | Plasma Technology | DIRECT-RP01 | closed at manufacturer family only |
| Reactor model | no direct source recovered | OPEN-HISTORICAL | UWA thesis/lab record/manual |
| Reactor architecture | parallel-plate | DIRECT-RP01 | broad architecture closed |
| RF frequency | same-era RIE80 uses 13.56 MHz | OPEN-HISTORICAL / TRANSFER | direct UWA hardware record |
| Powered-electrode area | not disclosed | OPEN-HISTORICAL | dimensioned reactor record |
| Grounded-area ratio | not disclosed | OPEN-HISTORICAL | reactor geometry |
| Electrode spacing | not disclosed | OPEN-HISTORICAL | reactor/manual record |
| Sample placement/loading | not disclosed | OPEN-HISTORICAL | traveler/thesis/lab record |
| Forward RF power | 50 W | DIRECT-RP01 | closed as controller center |
| Reflected power | not disclosed | OPEN-HISTORICAL | local measured trace |
| DC self-bias | not disclosed; primary HgCdTe study shows -360 to -440 V branch | OPEN-HISTORICAL / REQUIRED-LOCAL | local measurement or ion-energy proxy |
| RF power density | same-UWA 0.4 W/cm² branch | SAME-UWA only | do not merge with 50-W RP-01 |
| Pressure | 100 mTorr | DIRECT-RP01 | closed as controller center |
| Pressure gauge / gas correction | not disclosed | OPEN-HISTORICAL | local calibrated gauge record |
| Base pressure | not disclosed; same-era RIE80 <0.5 mTorr transfer evidence | OPEN-HISTORICAL / TRANSFER | local measurement + direct historical recovery |
| Pump / throttle | not disclosed | OPEN-HISTORICAL | local hardware record |
| Gas notation | printed CH4/5H2 | DIRECT-RP01 | ratio interpretation still provenance-controlled |
| Total flow | 64 sccm | DIRECT-RP01 | closed |
| Individual CH4/H2 flows | secondary 1:5 interpretation only | PARTIAL | direct UWA source or explicit local branch |
| MFC model/range/calibration | not disclosed | OPEN-HISTORICAL | local calibration |
| Gas purity | not disclosed | OPEN-HISTORICAL | local defined grade |
| Gas stabilization time | not disclosed | OPEN-HISTORICAL | local qualification |
| Chamber clean/season | not disclosed | OPEN-HISTORICAL | local genealogy + historical recovery |
| Sample/chuck temperature | not disclosed | OPEN-HISTORICAL / REQUIRED-LOCAL | measured temperature/proxy |
| Sample thermal coupling | not disclosed | OPEN-HISTORICAL | local hardware record |
| RF-on time | 60 s | DIRECT-RP01 | closed |
| Oxide-clear time | not disclosed | OPEN-HISTORICAL / REQUIRED-LOCAL | P25-matched time series |
| Semiconductor exposure time | not directly stated | DERIVED-LOCAL only | `t_sem=t_RF-t_clear` after calibration |
| Physical HgCdTe recession | not directly closed for RP-01 contact step | OPEN / REQUIRED-LOCAL | profilometry/AFM/step witness |
| Electrical conversion depth | prior n-type ~8 µm cited, exact matched condition unrecovered | PARTIAL | matched LBIC/depth recovery |
| Lateral conversion distance | not closed | OPEN | LBIC mapping |
| Converted sheet state | volumetric averaged value published | PARTIAL | local sheet/Hall + independent depth |
| Cr/Au contact outcome | rho_c~9e-4 Ω cm² at 80 K | DIRECT-RP01 final outcome | preserve optical-background/TLM state |
| Minority blocking function | device response supports functionality | DIRECT-RP01 device outcome | local P08F closure |
| Orientation sensitivity | primary transfer evidence shows strong face dependence | PRIMARY-TRANSFER | preserve P29 face/polarity in RIE genealogy |
| Self-bias relevance | primary HgCdTe direct evidence | PRIMARY-TRANSFER | mandatory local record |
| Same-era RIE80 frequency | 13.56 MHz | PRIMARY-PLASMA-TECH-FAMILY | never promote to RP-01 without direct evidence |
| White 2005 thesis full reactor traveler | PDF route identified but 403 in current retrieval path | NOT-RECOVERED | future source recovery |

## Highest-priority unresolved variables

1. Exact Plasma Technology model.
2. RF frequency.
3. Electrode dimensions/spacing and sample loading.
4. Historical/self-bias and sample temperature.
5. Base pressure and pumping/throttle configuration.
6. Individual historical MFC flows/calibration.
7. Chamber clean/seasoning state.
8. Oxide-clear time and actual semiconductor exposure.
9. Exact RP-01 physical recession.
10. Exact reactor condition tied to the ~8-µm n-type conversion depth.

## Release consequence

The direct controller center is necessary but insufficient. A transferred reactor is released only through P34's multivariate output vector:

`Y_RIE = {t_clear, self_bias, T_sample, d_etch, morphology, sheet_state, d_conv, L_conv, rho_c, blocking_response, detector_noise_delta}`.

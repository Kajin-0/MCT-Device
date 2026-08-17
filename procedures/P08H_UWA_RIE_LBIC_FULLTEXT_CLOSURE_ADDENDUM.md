# P08H - UWA RIE/LBIC full-text closure addendum

**Status:** `SL` SAME-UWA PROCESS-LINEAGE EVIDENCE. Supplements P08/P08A-P08G/P24/P34/P37.

## Purpose

Freeze newly recovered same-UWA RIE/LBIC process states without blending distinct experiments into a universal recipe. The direct RP-01 blocking-contact anchor remains separate: Plasma Technology parallel-plate family, printed CH4/5H2 chemistry, 64 sccm total, 100 mTorr, 50 W, 60 s localized exposure. Round 64 does not derive missing RP-01 self-bias, electrode geometry, RF frequency or sample temperature from neighboring papers.

## Same-UWA process-state matrix

| Branch | Material/use | Gas | Pressure | Power | Thermal state | dc bias | Time | Result |
|---|---|---|---:|---:|---|---:|---:|---|
| Siliquini 1997 | x~.31 p conversion | H2 27 / CH4 5 sccm | 410 mTorr | 0.4 W/cm2 | cathode 18 C | printed 180 V | 60 s | ~0.2 um recession; ~1.5 um conversion |
| Smith 1999 | x~.31 mesa/conversion | CH4/5H2 notation; 30 sccm total | 400 mTorr | 0.4 W/cm2 | cathode 16 C | 180 V | branch-dependent | ~0.15 um/min; p/n modification; Hg-anneal recovery |
| Musca 1998 | x=.31 n depth study | H2 27 / CH4 5 sccm | 430 mTorr | 0.4 W/cm2 | cathode 18 C | ~200 V | 30 s | ~0.075 um recession; electrical signature to ~8 um |
| Antoszewski 2000 | x=.30 p conversion | H2/CH4 5:1; ~40 sccm | ~500 mTorr | ~100 W | not promoted | not promoted | 2 min | 2.0 +/- 0.5 um converted; multicarrier state |
| Nguyen 2002 | x=.31/.23 transport | CH4/H2 1:3 | not promoted | 0.4 W/cm2 | not promoted | not promoted | 2 min | ~0.3 um recession; thin surface + deeper high-mobility region |
| White 2001 SIMS | x~.31 mechanism | D2 54 / CH4 18 sccm | 100 mTorr | 0.2 W/cm2 | stage 15 C; sample T not directly measured | ~200 V | 2/20-min branches | multiple H/D populations; bake redistribution |
| Smith 2000 mesa PC | x=.31 n detector | literal `H2/5CH4`; 30 sccm total | 400 mTorr | 0.4 W/cm2 | cathode 16 C | 80 V | 70 min | ~0.15 um/min; detector performance degraded |

Do not interpolate these rows into one synthetic recipe.

## Approximately 8-um conversion branch

Musca 1998 now supplies the previously weakly documented deep-conversion state: x=.31 Fermionics n-type material; approximately 10-um remaining epilayer; nominal 350 x 350 um exposed region; H2 27 sccm; CH4 5 sccm; 430 mTorr; 0.4 W/cm2; cathode 18 C; approximately 200-V dc bias; 30 s; about 0.075-um physical etch. LBIC plus depth removal showed an electrical n+/n signature to approximately 8 um.

State: `SL-DEPTH-BRANCH-CLOSED / RP01-CONVERSION-DEPTH-OPEN`.

## Resist-profile rule

Musca 1998 shows that thin/tapered photoresist can permit plasma-induced electrical modification beneath nominally protected regions. Required fields now include resist ID and process history, thickness over protected regions, thickness versus distance from aperture, edge-profile/taper map, minimum protected thickness, post-RIE resist erosion/state, and correlation between resist profile and the LBIC boundary.

A CAD mask boundary alone is not a complete electrical boundary condition.

## Physical recession vs electrical conversion

Continue to record separately `d_etch`, `d_conv`, `L_conv`, oxide-clear time/state, plasma state and mask/resist state. The UWA papers show `d_conv/d_etch` can vary enormously; physical recession is not a proxy for blocking-contact depth.

## Multicarrier transport qualification

Antoszewski 2000 and Nguyen 2002 resolve at least two electron populations after RIE: a thin lower-mobility surface layer and a deeper high-mobility converted bulk region. Therefore low-field one-carrier Hall values are effective scalars unless a single-carrier model is justified. Physical depth/doping claims should use field-dependent Hall/QMSA, differential etchback, or an equivalent resolved method.

## Sample-temperature and post-bake discipline

White 2001 demonstrates that cooled-stage temperature is not identical to measured wafer temperature. Record stage/cathode setpoint, direct sample temperature when available, thermal contact, RF-on time, duty cycle, any estimated upper bound explicitly as an estimate, and every post-RIE bake. Mobile hydrogen can redistribute during modest post-process heating.

## Hg-anneal recovery branch

Smith 1998/1999 support a same-UWA diagnostic branch in which a sealed-Hg anneal at 200 C for 17 h restored p-type electrical state after particular RIE conditions. Preserve it as mechanistic/recovery evidence, not an automatic RP-01 repair step.

## Detector-performance gate

Smith 2000 directly shows long mesa RIE can strongly reduce responsivity, effective minority-carrier lifetime, noise performance and D* while leaving cutoff and DC resistance deceptively similar. Any new plasma condition, especially changes in exposed area or dose, requires matched controls with at minimum I-V/resistance, absolute responsivity, tau_eff, full noise spectrum, D* and LBIC mapping.

## Literal gas-notation conflict

Smith 2000 visibly prints `H2/5CH4` for the 70-min branch. Other UWA papers print CH4/5H2 or explicit H2/CH4 flows. Archive literal notation and prefer explicit MFC flows. Do not normalize historical shorthand by assumption.

## LBIC depth-calibration rule

Musca 1999 shows LBIC depth response depends on junction doping, optical wavelength, illumination direction, geometry and diffusion length. Absolute `d_conv` requires calibrated known-depth witnesses, destructive etchback, validated forward modeling, or another independent depth measurement. Bipolar LBIC alone proves an electrical boundary but does not uniquely determine depth.

## Remaining OPEN state

The exact RP-01 reactor model/run sheet, electrode areas/spacing, RF frequency, matching-network state, self-bias, actual sample temperature and electrical conversion depth under the 100-mTorr/50-W/64-sccm/60-s exposure remain `OPEN`.
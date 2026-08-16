# RP-01 gap-matrix addendum — source-recovery / qualification round 4

**Date:** 2026-08-15 America/New_York  
**Precedence:** This addendum supersedes older entries for P03/P04/P09/P14 where noted.

## P14 Mask-2 / lift-off — updated state

| Variable | Updated status | Evidence / next action |
|---|---|---|
| resist thickness | CLOSED-P | ~4–5 µm |
| prebake | CLOSED-P | 80 °C / 30 min |
| chlorobenzene treatment | CLOSED-P | 30 min |
| pattern/develop/water rinse | CLOSED-P sequence-level | exact exposure/developer still open |
| resist class / lift-off mechanism | MECHANISM-CLOSED / PRODUCT-OPEN | historical chlorobenzene lift-off is a single-layer positive diazo/novolak profile-modification process; exact RP-01 commercial resist not recovered |
| exact resist product | OPEN | do not assign AZ/Shipley from unrelated historical examples |
| spin recipe | OPEN / LOCAL-QUAL | establish measured 4–5-µm film with chosen local resist branch |
| chlorobenzene sequence relative to exposure | PARTIAL / QUAL | trust RP-01 wording; historical processes permit before/after exposure; do not reorder silently |
| developer identity/time/T | OPEN / LOCAL-QUAL | must be frozen by profile + RIE + lift-off outcome |
| developed undercut/overhang | CONTROLLED-QUAL | P14A requires cross-sectional/profile metrology |
| RIE resist erosion/profile change | CONTROLLED-QUAL | measure before/after P08 |
| resist:metal thickness ratio | CLOSED-D | ~13.3:1–16.7:1 for 4–5 µm resist vs 0.30 µm total Cr/Au; useful consistency metric, not sufficient lift-off criterion |
| lift-off solvent/time/agitation | OPEN / LOCAL-QUAL | historical examples on other substrates not transferable as RP-01 fact |

Procedure: `procedures/P14A_CHLOROBENZENE_LIFTOFF_LINEAGE_ADDENDUM.md`.

## P09 Cr/Au deposition — updated state

| Variable | Updated status | Evidence / next action |
|---|---|---|
| Cr thickness | CLOSED-P | 30 nm |
| Au thickness | CLOSED-P | 270 nm |
| historical deposition method | OPEN | later UWA work supports thermal evaporation as compatible, not historical proof |
| local deposition method | CONTROLLED-QUAL | P09A permits a qualified local method, leading candidate thermal evaporation |
| QCM/tooling calibration | CONTROLLED-QUAL | calibrate Cr and Au separately against independent witness thickness |
| historical base pressure | OPEN | source ceiling reached |
| local base/max deposition pressure | CONTROLLED-QUAL | derive from actual tool sensitivity vs TLM/morphology; do not invent universal number |
| historical Cr/Au rates | OPEN | source ceiling reached |
| local Cr/Au rates | CONTROLLED-QUAL | rate DOE with fixed 30/270-nm final thicknesses |
| historical RIE-to-metal delay | OPEN | source ceiling reached |
| local maximum RIE-to-metal delay | CONTROLLED-QUAL | timestamped delay DOE against 80-K TLM and stability |
| substrate thermal load | CONTROLLED-QUAL | measure/calibrate during deposition; correlate with resist profile/lift-off/contact outcome |
| Cr→Au vacuum-break rule | QUAL | preferred baseline no break where tool permits; any break is separate branch |
| final electrical benchmark | CLOSED-P / QUAL | historical rho_c≈9×10^-4 Ω·cm² at 80 K; local distribution and stability must be established |
| noise correlation | CONTROLLED-QUAL | static rho_c alone insufficient; compare P12 1/f/g-r behavior |

Procedure: `procedures/P09A_CR_AU_DEPOSITION_TRANSFER_DOE.md`.

## P03 LPE thickness schedule — updated state

| Variable | Updated status | Evidence / next action |
|---|---|---|
| x≈0.30 melt composition | CANDIDATE-P / strong lineage | xL=.082, yL=.810, TL=507 °C → xS=.29 |
| ~500 °C / ΔT≈7 °C center | CANDIDATE-P / QUAL | literature-grounded qualification center, not production setpoint |
| historical 30-min example | CANDIDATE-P / NOT THICKNESS-TIED | same Honeywell patent gives ~0.5 h example but not explicitly xS=.29 + 9.5 µm |
| Wood–Hager composition reproducibility | PRIMARY benchmark | σx≈0.002 layer-to-layer in same broad Honeywell slider lineage |
| exact 9.5-µm historical contact time | OPEN | public source ceiling reached |
| local thickness-time relation | CONTROLLED-QUAL | P03B maps t_contact × ΔT × thermal trajectory |
| supercooling sensitivity | CONTROLLED-QUAL | bracket around composition-matched center and measure thickness/x simultaneously |
| thermal-mode dependence | CONTROLLED-QUAL | step, controlled-cooling, combined are separate recipe branches |
| charge-history effect | CONTROLLED-QUAL | fresh/reused/replenished states tracked separately |
| apparatus timing/T tolerances | DERIVED AFTER DOE | derive from measured ∂d/∂t, ∂d/∂T and ∂x/∂T rather than guessing |

Procedure: `procedures/P03B_X030_GROWTH_TIME_SUPERCOOLING_CALIBRATION.md`.

## P04 Hg anneal — updated state

| Variable | Updated status | Evidence / next action |
|---|---|---|
| low-T Hg-rich process family | PRIMARY-SUPPORTED | composition-matched x≤.30 branch supports 250–300 °C n-type conversion without apparent composition shift |
| 400 °C warning | CLOSED-P | interface-region composition change reported |
| 250 °C / ~1 h screening center | CANDIDATE-P / NOT ENDPOINT | Harman primary process example; not RP-01 carrier-density endpoint |
| exact historical RP-01/Fermionics dwell | OPEN | not recovered |
| exact historical Hg source/pHg/cooldown | OPEN | not recovered |
| local time response | CONTROLLED-QUAL | P04A matched-coupon time mapping |
| local temperature response | CONTROLLED-QUAL | map within low-temperature composition-preserving region |
| Hg chemical-potential response | CONTROLLED-QUAL | define source T/pHg/saturation state quantitatively |
| cooldown sensitivity | CONTROLLED-QUAL | sample/source T(t) is part of process state |
| detector-relevant Hall state | CONTROLLED-QUAL | measure ~77–80 K plus additional T where useful for defect interpretation |
| composition-preservation gate | CONTROLLED-QUAL | matched pre/post P06 optical mapping |
| production tolerances | DERIVED AFTER DOE | derive from state sensitivities rather than arbitrary ±T/±time |

Procedure: `procedures/P04A_X030_HG_ANNEAL_STATE_MAPPING_DOE.md`.

## Round-4 practical conclusion

For P03/P04/P09/P14 the archival literature now provides enough process-family physics and historical anchors to design controlled local transfer, but not enough to justify a unique historical set of missing numbers. Further progress should preferentially come from:

- local metrology-driven qualification;
- exact archival records if newly found;
- not generic cleanroom/furnace conventions.

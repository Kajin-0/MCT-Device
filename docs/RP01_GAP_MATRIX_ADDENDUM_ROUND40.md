# RP-01 gap matrix addendum — Round 40 first-qualification-build integration

**Date:** 2026-08-16 America/New_York  
**Repository:** `Kajin-0/MCT-Device`

## Purpose

Round 40 converts the P16A gap inventory into one coherent candidate-build branch without falsely closing local apparatus or calibration states.

Primary integration artifact:

`travelers/P16B_FIRST_QUALIFICATION_BUILD_CANDIDATE_BRANCH_REGISTER.md`.

---

## 1. Row-by-row integration status

| ID | Round-40 candidate decision | What literature now fixes | What still requires a real laboratory | P16A state after Round 40 |
|---|---|---|---|---|
| R01 | high-purity elemental Hg/Cd/Te candidate | 6N is a real Te-rich LPE transfer purity; Honeywell composition selected | supplier/form/lot/certificate, actual source-prep implementation | `OPEN-CHOICE` |
| R02 | Cd0.96Zn0.04Te (111)B first-screen family | 4%-Zn/(111)B has strong x≈.30 LPE transfer | actual lot, dimensions, measured plane/polarity/miscut/defects/isolation | `OPEN-CHOICE` |
| R03 | preserve LPE Br2/methanol final-surface family | 2–3% Br2/methanol, few-seconds transfer exists | explicit basis/time/rinse/dry/removed depth/clean-to-load | `OPEN-CHOICE` |
| R04 | Honeywell covered graphite horizontal slider | topology, wells/plug/Hg recess/moats/quartz furnace | all dimensions, volume, clearances, furnace/actuator/thermometry | `APPARATUS-NOT-SELECTED` |
| R05 | Honeywell xL=.082/yL=.810 composition | derived Hg/Cd/Te mass fractions after Mcharge selected | total Mcharge, auxiliary Hg inventory, actual weighed genealogy | `OPEN-CHOICE` |
| R06 | N2 purge -> flowing H2 | atmosphere family/sequence | grades, flows, pressure, purification, monitors/calibration | `OPEN-CHOICE` |
| R07 | TL=507°C equilibrium center; calibrate locally | tie-line/liquidus center; transfer supercooling/contact envelopes | actual T(t), ΔTSC, contact, wipe, cooldown | `OPEN-CHOICE` |
| R08 | P06/P06A FTIR map | method/model architecture | actual FTIR/thickness reference/calibration/footprint | `METROLOGY-NOT-IMPLEMENTED` |
| R09 | P05 VdP/Hall | UWA/RP-01 Hall/VdP lineage; 80/300 K, up to 2 T in direct work | actual magnet/cryostat/electronics/contacts/calibration | `METROLOGY-NOT-IMPLEMENTED` |
| R10 | sealed Hg-reservoir ampoule family | primary closed-tube/Hg-reservoir architecture | ampoule/source/furnace geometry and inventory | `APPARATUS-NOT-SELECTED` |
| R11 | 250°C / 1 h / Hg-saturated first screen | direct Harman transfer center; 250–300°C near-x support | Ts/THg traces, cooldown, final Hall/optical qualification | `OPEN-CHOICE` |
| R12 | AZ4620 historical first product screen only | 3-µm AZ4620 Br2/HBr HgCdTe transfer | current resist/lot equivalence, spin/bake/exposure/developer/strip | `OPEN-CHOICE` |
| R13 | retain 2% Br2 / 3:1 EG:HBr center | Srivastav notation + same-SSPL v/v candidate support | actual concentration/ratio bases, HBr assay, reagent genealogy | `UNDEFINED-BASIS` |
| R14 | Srivastav output center + measured isolation endpoint | ~21°C, ~2.78 µm/min, A~.63, ~2-nm best RMS | bath state, quench/rinse/dry/wet transfer, air clock to P25 | `OPEN-CHOICE` |
| R15 | TI photoconductor anodization center | 0.1 mol KOH/L stated 90/10 EG/water, carbon cathode, 0.3 mA/cm², ~15 V/~2 min/~800 Å | 90:10 basis, reagents, cell dimensions, Aexposed, V(t)/Q/A, rinse | `OPEN-CHOICE` |
| R16 | direct RP-01 functional Mask-2 state | 4–5 µm, 80°C/30 min, chlorobenzene 30 min, water rinse, RIE/lift-off function | commercial product/lot, spin, aligner/dose, developer, lift-off | `OPEN-CHOICE` |
| R17 | 1:5 same-lineage gas candidate | total 64 sccm direct; derived 10.6667/53.3333 sccm candidate split | actual cylinders/manifold/MFC calibration | `UNDEFINED-BASIS` |
| R18 | local parallel-plate RIE must be mapped | Plasma Technology parallel-plate direct | reactor model/geometry/RF/sheath/T/pump/gauge/chamber state | `APPARATUS-NOT-SELECTED` |
| R19 | local clear-time calibration | total 60-s direct target | t_clear, t_sem and conversion/output gates in selected reactor | `OPEN-CHOICE` |
| R20 | thermal evaporation method-family candidate | direct 30/270-nm stack; same-UWA thermal evaporation | evaporator/source/vacuum/rates/QCM/thermal/handoff | `APPARATUS-NOT-SELECTED` |
| R21 | least-aggressive compatible local lift-off branch | chlorobenzene lift-off family exists | remover/temperature/time/agitation/rinse on actual stack | `OPEN-CHOICE` |
| R22 | calibrated final CD metrology | direct TLM/contact geometry reference | actual metrology tool/calibration/device-pair naming | `METROLOGY-NOT-IMPLEMENTED` |
| R23 | P09/P26 80-K TLM | 300×300 µm, 50–400-µm gaps, rho_c reference | actual cryogenic fixture/electronics/reduction uncertainty | `METROLOGY-NOT-IMPLEMENTED` |
| R24 | shared detector state at 10 V/cm reference | field definition and key RP-01 field state | bias/load/preamp network, terminal voltage, self-heating transfer | `METROLOGY-NOT-IMPLEMENTED` |
| R25 | P11 absolute radiometry | ~80 K, stated 60° FOV, 1-kHz spectral chop, RP-01 reference outputs | calibrated geometry/view factor/optical transfer/reference detector | `METROLOGY-NOT-IMPLEMENTED` |
| R26 | P12 terminal PSD | ~80 K, 10 V/cm, stated 60°, HP35665A lineage, ~3-kHz knee, 24.5 nV/√Hz HF level | actual network/preamp/analyzer transfer and ENBW/background | `METROLOGY-NOT-IMPLEMENTED` |
| R27 | same-UWA TPCD method transfer | 1.047 µm/25 ns/1 kHz/~77 K/HP54522A branch | actual source/spot/injection/electrical/package transfer | `METROLOGY-NOT-IMPLEMENTED` |
| R28 | low-force wire-saw first screen | Yoo 125-mm wire/16-µm BN/~1-h branch on finished CdZnTe | actual tool/protection/support/street/compatibility | `OPEN-CHOICE` |
| R29 | compatibility-defined post-cut clean | no universal finished-RP01 clean recovered | clean chemistry, edge/subsurface metrology, pre/post detector checks | `OPEN-CHOICE` |
| R30 | compliant silicone-family attach first screen | Honeywell silicone branch survived cryogenic test where glass cracked | current adhesive/carrier/bondline/cure/thermal response | `OPEN-CHOICE` |
| R31 | no invented generic wire branch | Cr/Au pad stack direct only | wire/ribbon, bonder/tool/settings and cryogenic/noise qualification | `OPEN-CHOICE` |
| R32 | measured 60°-class optical package | stated 60° FOV direct | aperture/window/shield dimensions/transmission/alignment | `OPEN-CHOICE` |
| R33 | measured vacuum/cooldown package state | intended near-80-K operation | Dewar/chamber/gauges/pump/bake/cooldown/die-T proxy | `OPEN-CHOICE` |
| R34 | post-build cycle qualification | failure modes/primary transfer physics known | actual repeated cryogenic package survival data | `RELEASE-DATA-OPEN` |
| R35 | instantiate existing genealogy architecture | P16/P17 structure already controlled | actual IDs/paths/signatures/timestamps | `LOCAL-BRANCH-FROZEN` conceptually |
| R36 | post-build SPC/release | P17 method exists | repeated frozen-route data/MSA/yield/capability | `RELEASE-DATA-OPEN` |

---

# 2. Documentary saturation categories

## Category A — architecture/center selected, but physical realization still local

Rows:

`R01, R02, R04, R05, R06, R07, R10, R11, R12, R15, R16, R17, R18, R20, R28, R30`.

These should no longer trigger broad “find another process family” searches unless a new primary source materially improves the selected branch.

## Category B — local calibration is the remaining scientific work

Rows:

`R03, R08, R09, R14, R19, R21–R27, R29, R31–R33`.

Further literature can inform experiment design, but it cannot replace measurement of the actual selected equipment/material state.

## Category C — intrinsically post-build release data

Rows:

`R34, R36`.

No pre-build paper can generate the required local survival/yield/capability evidence.

## Category D — control architecture already conceptually closed

Row:

`R35`.

Actual IDs still need instantiation, but the genealogy logic itself does not need another research module.

---

# 3. Highest-impact irreducible blanks

The following are now the dominant blockers to a genuinely executable first-build traveler:

1. dimensioned P30A LPE apparatus and numerical `M_charge`;
2. actual P31 anneal enclosure/source geometry and calibrated Ts/THg trajectory;
3. explicit mathematical R13 wet-etch formulation and certified reagents;
4. actual P25A electrolyte-basis/cell/area realization;
5. actual Mask-1 and Mask-2 products/process tools;
6. selected RIE reactor with gas/MFC/sheath/oxide-clear calibration;
7. selected Cr/Au evaporator with vacuum/QCM/rate/thermal characterization;
8. measurement chains R08/R09/R22–R27;
9. completed-device singulation protection/clean path;
10. cryogenic attachment/interconnect/optical/vacuum package implementation.

These are now explicitly classified as **local specification/calibration tasks**, not unresolved theoretical questions.

---

# 4. Readiness disposition

Round 40 does not alter the formal P16A row states.

Therefore:

- `TRACEABLE-FIRST-BUILD-READY = NO`;
- `HISTORICAL-RP01-REPRODUCED = NO`;
- `REPRODUCIBLE-RELEASE = NO`.

The material improvement is that the open rows are no longer an undifferentiated list: P16B now defines the preferred branch and the exact local information still required for each.
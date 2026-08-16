# P16D1 — supporting metrology / microfabrication acceptance register

**Status:** CONTROLLED PRE-BUILD ACCEPTANCE REGISTER ADDENDUM / ROUND 42  
**Date:** 2026-08-16 America/New_York  
**Use with:** P36A and P16D.

## 1. Purpose

Record acceptance evidence for source mass metrology, dimensional metrology, lithography, wet-mesa chemistry, anodization and critical handoff timing.

---

# 2. AT-MASS

Balance ID: ____________________  
Calibration ID: ____________________  
Expected Hg mass range: ____________________  
Expected Cd mass range: ____________________  
Expected Te mass range: ____________________

Repeatability near Cd mass: ____________________  
Linearity/bias: ____________________  
Tare repeatability: ____________________  
Propagated `u(xL)`: ____________________  
Propagated `u(yL)`: ____________________  
Dummy charge reconstruction raw-data ID: ____________________

State: ____________________

---

# 3. AT-DIM

Lateral metrology tool/calibration: ____________________  
Vertical µm-scale method/calibration: ____________________  
Sub-µm oxide/metal method/calibration: ____________________

| Scale/feature | Reference artifact | Measured bias/uncertainty | State |
|---|---|---|---|
| 50–400 µm gaps |  |  |  |
| ~300 µm contacts |  |  |  |
| 4–5 µm resist |  |  |  |
| ~9.5 µm layer/mesa scale |  |  |  |
| ~80 nm oxide |  |  |  |
| 30 nm Cr |  |  |  |
| 270 nm Au |  |  |  |
| singulation kerf/edge |  |  |  |

Coordinate registration demonstrated: YES / NO  
State: ____________________

---

# 4. AT-LITH — Mask-1 / Mask-2

Spin coater: ____________________  
Bake tool: ____________________  
Aligner/exposure: ____________________  
Dose calibration: ____________________  
CD/profile metrology: ____________________

## Mask-2 direct functional-state acceptance

Resist product/lot: ____________________  
Measured post-bake thickness: ____________________ µm  
4–5 µm requirement met: YES / NO  
80 °C / 30 min substrate thermal calibration: ____________________  
Chlorobenzene product/lot: ____________________  
30-min timing/bath state: ____________________  
Measured exposure dose: ____________________  
Developer identity/concentration/basis: ____________________  
Top/bottom CD: ____________________  
Profile/undercut: ____________________  
Scum/residue: ____________________  
Representative plasma-survival result: ____________________  
300-nm-class witness lift-off result: ____________________

Mask-2 state: ____________________

## Mask-1

Resist product/lot: ____________________  
Thickness: ____________________  
Dose/developer: ____________________  
P28 surrogate survival: ____________________  
HgCdTe residual: ____________________

Mask-1 state: ____________________

---

# 5. AT-WET — wet-mesa branch

Br2 percentage basis: ____________________  
EG:HBr ratio basis: ____________________  
HBr stock assay: ____________________  
Br2/HBr/EG product lots: ____________________  
Mixing order: ____________________  
Batch volume: ____________________  
Bath vessel: ____________________  
Bath temperature: ____________________  
Agitation state: ____________________  
Bath age/use rule: ____________________  
Rinse/dry sequence: ____________________

Volumetric/mass metrology calibration: ____________________  
Bath-temperature calibration: ____________________  
Timing uncertainty: ____________________  
Resist/surrogate compatibility: ____________________

HgCdTe residual:

- vertical rate: ____________________
- anisotropy: ____________________
- surface roughness/morphology: ____________________
- mesa isolation: ____________________
- undercut/profile: ____________________
- P28->P25 compatibility: ____________________

State: ____________________

---

# 6. AT-ANO — anodization

Electrolyte 90:10 basis definition: ____________________  
KOH assay: ____________________  
KOH mass calculation ID: ____________________  
EG/H2O/KOH lots: ____________________  
Mixing/final-volume convention: ____________________

Cell revision: ____________________  
Anode geometry: ____________________  
Cathode material/geometry: ____________________  
Electrode spacing/orientation: ____________________  
`A_exposed`: ____________________ cm²

Selected `J`: ____________________ mA/cm²  
Calculated `I=J A_exposed`: ____________________ mA  
Current-source calibration: ____________________  
Voltage-logger calibration/compliance: ____________________  
Timebase calibration: ____________________  
Dummy-cell result: ____________________

HgCdTe residual:

- V(t) fingerprint: ____________________
- oxide thickness: ____________________
- morphology/color: ____________________
- interface/passivation result: ____________________
- Mask-2 compatibility: ____________________
- RIE `t_clear` linkage: ____________________
- detector/contact/noise linkage: ____________________

State: ____________________

---

# 7. AT-HANDOFF — critical state transitions

Clock/timebase ID: ____________________  
Measured cross-station clock offset: ____________________

| Handoff | Previous end | Next start | Elapsed | Ambient/storage | Record complete |
|---|---|---|---|---|---|
| final CdZnTe surface -> LPE |  |  |  |  |  |
| wet mesa -> anodization |  |  |  |  |  |
| anodization -> Mask-2 |  |  |  |  |  |
| RIE -> Cr |  |  |  |  |  |
| Cr -> Au |  |  |  |  |  |
| singulation -> package |  |  |  |  |  |
| package -> P10–P13 |  |  |  |  |  |

Dummy genealogy raw-data ID: ____________________  
State: ____________________

---

# 8. P16D1 disposition

AT-MASS: ____________________  
AT-DIM: ____________________  
AT-LITH: ____________________  
AT-WET: ____________________  
AT-ANO: ____________________  
AT-HANDOFF: ____________________

All possible surrogate acceptance complete: YES / NO  
All HgCdTe residual gates explicit: YES / NO  
All chemistry bases locally unambiguous: YES / NO  
All calibration/raw data linked: YES / NO

Reviewer: ____________________  
Date: ____________________
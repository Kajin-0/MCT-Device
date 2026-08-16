# P36A — supporting metrology, lithography, wet-chemistry and anodization acceptance

**Status:** CONTROLLED PRE-BUILD COMMISSIONING / ACCEPTANCE ADDENDUM  
**Date:** 2026-08-16 America/New_York  
**Use with:** P36, P14/P14A, P25/P25A, P27, P28/P28A, P29, P32, P16C C01/C06/C12.

## 1. Purpose

Close the Round-42 acceptance coverage for supporting capabilities that are essential to the first qualification build but are not the large vacuum/thermal/test subsystems addressed in P36.

This addendum covers:

1. source weighing/mass accounting;
2. dimensional/CD/thickness metrology;
3. spin/bake/exposure/development capability;
4. wet-mesa bath definition and timing;
5. anodization cell/current/voltage/area metrology;
6. controlled handoff timing/data genealogy.

No commercial resist, developer, wet-etch concentration basis or anodization solvent-ratio basis is invented here.

---

# 2. AT-MASS — source weighing / charge-accounting acceptance

**Maps to:** P03/P03C/P30A, P16C C01, P16A R01/R05.

The controlled composition calculation freezes:

- Hg `200.59 g/mol`;
- Cd `112.414 g/mol`;
- Te `127.60 g/mol`;
- `w_Hg=0.2497382358`;
- `w_Cd=0.01250164993`;
- `w_Te=0.7377601143`.

`M_charge` remains local apparatus-dependent.

## AT-MASS-01 — balance identity/calibration

Record balance model/serial, calibration method, environmental controls and weighing vessels.

Calibration shall cover the **actual expected mass regions**, especially the much smaller Cd mass.

**PASS:** calibration/repeatability/linearity data exist at the intended Hg/Cd/Te load ranges; display resolution alone is not accepted as weighing capability.

## AT-MASS-02 — repeatability at Cd scale

Using traceable masses or a stable surrogate load near the planned Cd inventory, quantify repeated weighings including tare operations.

The downstream requirement is composition discrimination. Therefore propagate mass uncertainty through:

`xL_actual = N_Cd/(N_Hg+N_Cd)`

and

`yL_actual = N_Te/(N_Hg+N_Cd+N_Te)`.

**PASS:** the resulting `u(xL)`/`u(yL)` is acceptable for the P20/P21 material-state allocation once that allocation is frozen.

No independent arbitrary mg tolerance is assigned.

## AT-MASS-03 — end-to-end charge reconstruction

Execute a dummy three-component mass-accounting exercise with distinct inert standards or equivalent traceable masses.

Record target masses, actual masses, tare, reconstructed mole fractions, deviations and software/calculation version.

**PASS:** another reviewer can reproduce the calculated composition from raw recorded masses.

---

# 3. AT-DIM — dimensional / CD / thickness metrology acceptance

**Maps to:** P06, P09, P14, P25, P26, P27, P28, P35 and P16C C12.

Required capability includes measurements spanning:

- ~50–400-µm contact gaps;
- ~300×300-µm contacts;
- 4–5-µm resist thickness;
- ~9.5-µm HgCdTe thickness region;
- ~80-nm oxide;
- 30-nm Cr / 270-nm Au;
- mesa depth/profile;
- singulation kerf/edge metrics.

No single instrument is required to cover every scale.

## AT-DIM-01 — lateral calibration

Using traceable dimensional artifacts, calibrate microscopy/stage scale over the relevant tens-to-hundreds-of-micrometers range.

**PASS:** uncertainty supports field calculation `E=V_active/L_measured` and area/CD calculations without dominating the intended device comparison.

## AT-DIM-02 — vertical/thickness calibration

Commission independent methods appropriate to:

- micrometer-scale resist/HgCdTe/mesa steps;
- submicrometer oxide/metal films.

Use traceable step/film references or calibrated cross-method comparison.

**PASS:** every reported thickness carries method, location, correction and uncertainty; no QCM or optical-model thickness is treated as self-validating.

## AT-DIM-03 — coordinate registration

Demonstrate that measured map/CD positions can be related to sample orientation, wafer coordinates and later device/contact IDs.

---

# 4. AT-LITH — lithography acceptance

**Maps to:** P14/P14A/P27/P32, P16C C06, P16A R12/R16.

## AT-LITH-01 — spin/coating OQ

Using the selected candidate resist family once chosen, map film thickness versus controlled coating settings on surrogate wafers/coupons.

For Mask-2, demonstrate the ability to reproducibly reach a measured `4–5 µm` film after the controlled bake state.

For Mask-1, select thickness from P32 functional requirements rather than assuming Mask-2 equivalence.

Record:

- resist product/lot;
- dispense;
- spin program;
- substrate type;
- film thickness map;
- edge bead/coverage;
- elapsed time.

**PASS:** selected coating setpoint is tied to measured thickness, not nominal datasheet thickness.

## AT-LITH-02 — bake OQ

For the direct Mask-2 state, demonstrate calibrated `80 °C / 30 min` capability.

Measure wafer/coupon temperature response rather than using hotplate/oven display alone where the transfer is material.

**PASS:** the 30-min timing and actual substrate thermal state are reconstructable.

## AT-LITH-03 — chlorobenzene time/control

Demonstrate a controlled 30-min chlorobenzene treatment fixture/bath with named solvent grade/lot, volume/container, temperature state and timing method.

This acceptance establishes handling/timing capability, not historical product identity or exposure-order closure.

## AT-LITH-04 — exposure dose calibration

Calibrate exposure irradiance/dose at the wafer plane using a suitable radiometric method or traceable exposure calibration.

**PASS:** dose is a measured physical quantity; mask aligner timer/controller units alone are insufficient.

## AT-LITH-05 — development/profile surrogate PQ

For the selected resist/developer branch, characterize:

- clear dose/process window;
- top/bottom CD;
- sidewall/re-entrant profile;
- residue/scum;
- adhesion;
- repeatability.

Mask-2 surrogate PQ shall also evaluate profile after a plasma exposure representative of the planned RIE duration and after a 300-nm-class witness metal stack/lift-off challenge.

Actual HgCdTe/oxide compatibility remains residual.

---

# 5. AT-WET — wet-mesa chemistry acceptance

**Maps to:** P28/P28A/P32, P16C C06, P16A R13/R14.

## AT-WET-01 — chemistry definition gate

Before any execution, the local branch shall explicitly define:

- Br2 percentage basis;
- EG:HBr ratio basis;
- HBr stock assay;
- reagent grade/lot;
- calculation worksheet/version;
- mixing order;
- batch volume;
- bath vessel;
- temperature;
- agitation state;
- bath age/use history;
- rinse/dry sequence.

**PASS:** no ambiguous `%` or ratio notation remains in the local traveler.

The Srivastav `2% Br2 / 3:1 EG:HBr / ~21 °C` center remains transfer evidence until this local basis is declared.

## AT-WET-02 — volumetric/mass preparation OQ

Commission the balances/pipettes/volumetric devices required by the selected basis with traceable calibration at the actual batch scale.

**PASS:** prepared concentrations/ratios can be reconstructed with uncertainty from raw measurements.

## AT-WET-03 — bath-temperature/time OQ

At approximately the 21 °C transfer center, demonstrate measured bath temperature and timing capability over the expected etch interval.

Timing capability must satisfy P36 timing-discrimination rule relative to the shortest planned etch.

## AT-WET-04 — surrogate compatibility PQ

Use compatible witness materials to qualify resist survival, handling, rinse/dry and dimensional metrology. Do not claim the HgCdTe etch rate or anisotropy from a surrogate.

## AT-WET-05 — HgCdTe residual gate

Actual HgCdTe required to establish:

- vertical rate;
- anisotropy;
- surface roughness/morphology;
- mesa isolation;
- undercut/profile;
- bath-age response;
- downstream anodization compatibility.

The ~2.78 µm/min, `A≈0.63`, ~2-nm best roughness values remain transfer centers, not acceptance tolerances.

---

# 6. AT-ANO — anodization acceptance

**Maps to:** P25/P25A, P16C C06, P16A R15.

## AT-ANO-01 — electrolyte definition gate

Before execution, freeze locally:

- meaning of `90% EG / 10% DI water` basis;
- final volume convention;
- KOH assay;
- reagent lots;
- mixing sequence;
- batch/storage/use history.

Pure-KOH arithmetic remains:

`5.61056 g` per stated 1-L / 0.1000-mol basis before assay correction.

**PASS:** the local electrolyte is mathematically and procedurally unambiguous.

## AT-ANO-02 — cell geometry / exposed area

Dimension and record:

- vessel;
- anode fixture;
- cathode material/geometry;
- electrode spacing/orientation;
- masked/exposed region;
- electrochemically exposed area `A_exposed`.

Current is then calculated from:

`I = J A_exposed`.

No universal current is accepted without area.

## AT-ANO-03 — current-source/voltage-logger OQ

Using electrical dummy loads, calibrate constant-current operation around the first-screen current-density requirement after area conversion and demonstrate voltage logging with sufficient compliance around the expected ~15-V region.

The TI transfer center is approximately `J~0.3 mA/cm²`, ~15 V, ~2 min.

**PASS:** current, voltage and time are independently calibrated/logged; current density is traceable to measured area.

## AT-ANO-04 — dummy-cell PQ

Using a non-HgCdTe electrochemical/electrical surrogate where scientifically meaningful, verify wiring polarity, current control, voltage logging, timebase and data capture.

Do not infer HgCdTe oxide growth rate/interface quality from this test.

## AT-ANO-05 — HgCdTe residual gate

Actual HgCdTe required to establish:

- V(t) fingerprint;
- oxide thickness near the ~80-nm transfer center;
- morphology/color as secondary descriptors;
- interface/passivation response;
- Mask-2 compatibility;
- RIE oxide-clear behavior;
- detector/contact/noise correlation.

---

# 7. AT-HANDOFF — surface-state timing / genealogy acceptance

Critical sequences include:

- final CdZnTe surface -> LPE load;
- wet mesa -> anodization;
- anodization -> Mask-2;
- RIE -> Cr;
- Cr -> Au;
- singulation -> package;
- package -> detector metrology.

## AT-HANDOFF-01 — synchronized clock acceptance

Demonstrate that all stations used in a critical handoff share a traceable time basis or that clock offsets are measured.

## AT-HANDOFF-02 — state-transition dummy traveler

Execute one full dummy genealogy through the planned laboratory data system.

**PASS:** for every handoff the reviewer can recover:

- previous process end time;
- next process start time;
- elapsed time;
- ambient/storage state;
- operator/tool IDs;
- sample ID;
- deviation record.

No interval is reconstructed from memory.

---

# 8. P36A permanent rules

1. A ratio or percent with an undefined basis is not an executable recipe.
2. A resist thickness is measured after the relevant bake state, not assumed from product name/spin speed.
3. Exposure time is not dose until irradiance/transfer is calibrated.
4. Current is not current density until electrochemically exposed area is measured.
5. Surrogate wet-chemistry success does not define HgCdTe etch behavior.
6. Oxide thickness alone does not validate interface/passivation state.
7. Lateral geometry uncertainty propagates directly into electric field and area-normalized metrics.
8. Handoff time/ambient are process variables when surface state can evolve.

P36A closes acceptance-method gaps only. Physical local branch qualification remains open until actual tools/materials exist.
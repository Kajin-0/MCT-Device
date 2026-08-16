# P36 — laboratory subsystem commissioning and acceptance qualification

**Status:** CONTROLLED PRE-BUILD COMMISSIONING / ACCEPTANCE METHOD  
**Date:** 2026-08-16 America/New_York  
**Use with:** P16A, P16B, P16C, P03E, P05, P06, P08/P34, P09/P26A, P10–P13, P30A, P31, P33, P35.

## 1. Purpose

Convert the Round-41 minimum laboratory capability envelope into an **executable acceptance-test architecture** for a future laboratory.

P36 answers:

> Given a real tool or station, what evidence must exist before it is trusted as an input to HgCdTe process qualification?

P36 does not select vendors, certify institutional safety, release a HgCdTe process window, or establish historical RP-01 identity.

The commissioning chain is:

`identified hardware -> installation/configuration verification -> calibrated operating qualification -> surrogate performance qualification -> HgCdTe residual qualification -> P16C state update -> P16A local closure when all process-specific conditions are also met`.

A tool may pass P36 surrogate acceptance and still fail later HgCdTe qualification.

---

# 2. Acceptance-state vocabulary

Use these states exactly:

- `AT-NOT-STARTED`
- `AT-IQ-PASS` — identity/configuration/installation evidence complete.
- `AT-OQ-PASS` — calibrated operating range/control/measurement evidence complete.
- `AT-SURROGATE-PQ-PASS` — non-HgCdTe surrogate performance qualification complete.
- `AT-HGCDTE-RESIDUAL-PENDING` — surrogate acceptance complete but material-specific response still open.
- `AT-HGCDTE-PASS` — required HgCdTe/CdZnTe/device-specific acceptance completed.
- `AT-CONDITIONAL` — usable only under a documented restriction/deviation.
- `AT-FAIL`
- `AT-EH&S-BLOCKED`
- `AT-NOT-APPLICABLE`

P16C capability states remain separate.

---

# 3. Four-layer acceptance model

## 3.1 IQ — installation / identity qualification

For every critical subsystem record:

- tool/revision identity;
- relevant geometry/drawing;
- sensors, gauges, sources, MFCs, QCMs, probes, fixtures and software versions;
- utility/gas/vacuum/electrical interfaces;
- controlled raw-data path and clock source;
- maintenance/clean/season baseline;
- institutional EH&S authorization state.

IQ is documentary/configurational. It does not prove performance.

## 3.2 OQ — operating qualification

Demonstrate that the instrument can reach, measure and control the required physical envelope with traceable calibration.

OQ shall establish:

- range;
- accuracy/bias correction;
- repeatability;
- spatial uniformity where relevant;
- dynamic response/lag where relevant;
- resolution/timebase;
- transfer function where relevant;
- uncertainty budget sufficient for the intended process discrimination.

## 3.3 Surrogate PQ — non-HgCdTe performance qualification

Use standards, dummy hardware, witness substrates, passive electrical networks, certified optical references, inert thermal loads or mechanically representative coupons to test the complete measurement/control chain without consuming HgCdTe.

Surrogate PQ may establish apparatus competence but never material equivalence.

## 3.4 HgCdTe residual qualification

Reserve for responses that depend intrinsically on HgCdTe/CdZnTe or the completed detector stack, such as:

- LPE liquidus/growth response;
- anneal carrier-state response;
- wet-etch morphology/anisotropy on HgCdTe;
- anodic oxide interface response;
- RIE electrical conversion/blocking behavior;
- Cr/Au contact resistivity on converted HgCdTe;
- detector responsivity/noise/dynamics;
- completed-stack singulation damage;
- package-induced detector/noise/thermal changes.

---

# 4. General quantitative acceptance rules

## 4.1 Measurement capability must resolve the process decision

Do not impose an arbitrary universal calibration accuracy. For a controlled decision interval `DeltaX_decision`, require the expanded measurement uncertainty `U_X` to be small enough that states on opposite sides of the decision boundary can be distinguished.

Minimum logical requirement:

`U_X < DeltaX_decision/2`.

Preferred engineering target where practical:

`U_X <= DeltaX_decision/4`.

The latter is a design target, not historical evidence.

## 4.2 Timing capability

For a shortest controlled process interval `t_min`, the logged timing resolution/uncertainty shall satisfy:

`U_t < t_min/2`

and preferably

`U_t <= 0.1 t_min`.

## 4.3 Repeatability

Repeatability must be quantified at the **actual operating point**, not inferred from datasheet resolution. Use enough repeated observations to estimate short-term dispersion and retain the raw sequence.

No universal coefficient-of-variation threshold is assigned here; the observed dispersion must be small relative to the process/measurement decision interval defined by the downstream module.

## 4.4 Corrections

If a calibrated correction is applied, retain:

- raw reading;
- correction function/version;
- corrected result;
- uncertainty;
- calibration ID.

Do not overwrite raw controller values with corrected values.

---

# 5. AT-LPE — LPE furnace / boat / gas / actuator acceptance

**Maps to:** P30/P30A/P03E, P16C C02, P16A R04–R07.

## AT-LPE-01 — geometry and capacity IQ/OQ

Required evidence:

1. dimensioned boat/base/slider/cover drawing;
2. substrate recess, well opening, taper/depth, plug displacement, source recess and groove geometry;
3. actuator stroke/index positions and overlap geometry;
4. room-temperature `V_well,geom` with uncertainty;
5. permanent boat revision ID.

Surrogate methods may include calibrated dimensional metrology or a chemically compatible volume/capacity surrogate.

**PASS:** geometry is numerical and traceable; no instruction remains equivalent to “fill appropriately.”

**Residual HgCdTe gate:** hot usable volume/meniscus/wetting and selected `M_charge` remain open until actual process calibration.

## AT-LPE-02 — hot motion acceptance

Run the empty/dummy loaded boat through representative hot trajectories within the Round-41 engineering envelope around ~495–520 °C under the intended non-reactive commissioning atmosphere where permitted.

Record:

- commanded/actual slider position;
- transit time;
- repeatability;
- stick-slip or interference;
- temperature during movement;
- post-test dimensional/visual state.

**PASS:** all required process positions are reachable without collision or uncontrolled sticking; motion timing/position uncertainty is quantified and adequate for the shortest planned contact/separation interval.

## AT-LPE-03 — thermal field acceptance

Instrument a representative dummy boat/load and map at minimum:

- source-well region;
- substrate/contact region;
- auxiliary-source region;
- furnace axial position used for growth.

Map steady state and representative ramps/holds over approximately 495–520 °C.

Determine:

- sensor corrections;
- axial/transverse gradient;
- source-to-substrate offset;
- controller-to-process-region offset;
- drift;
- ramp lag;
- reproducibility after unload/reload.

The smallest literature-supported candidate supercooling scale currently carried is approximately 2 °C. Therefore a **design check** is:

`U_DeltaT < 1 °C` minimum logical discriminability,

with a preferred target near `<=0.5 °C` if the future branch intends to discriminate 2-°C differences directly.

This is an engineering measurement requirement, not a historical RP-01 tolerance.

**PASS:** corrected process-region temperatures can distinguish the intended above-liquidus, liquidus-neighborhood and below-liquidus states; uncertainty is propagated into `DeltaT_SC`.

## AT-LPE-04 — gas delivery acceptance

For the selected `N2 purge -> H2 process` branch, verify separately:

- gas identity/grade/lot recording;
- line/manifold identity;
- valve sequence;
- flow controller calibration at intended process flows;
- zero/offset and repeatability;
- pressure/backpressure measurement if controlled;
- purge/process transition logging;
- alarm/interlock function under institutional protocol.

**PASS:** actual delivered flow/pressure state is measurable and repeatable at the selected setpoints.

**Local blank:** no universal N2/H2 flow is assigned by literature.

## AT-LPE-05 — timebase/data acceptance

Demonstrate synchronized logging of:

- furnace/process temperatures;
- gas flows/pressure;
- slider commands/positions;
- event timestamps.

**PASS:** the reconstructed sequence can determine actual contact start/end, ramp/hold state and gas state without operator memory.

## AT-LPE-06 — HgCdTe residual gate

Requires actual matched charge/material:

- measured/local liquidus `TL_local`;
- above-liquidus equilibration convergence;
- selected `M_charge` and auxiliary Hg-source inventory;
- growth/no-growth or thickness/composition response versus `DeltaT_SC`, time and cooling trajectory;
- wipe/separation response;
- P06/P05 outputs.

P36 surrogate acceptance cannot close this row.

---

# 6. AT-ANN — Hg anneal furnace / ampoule / reservoir acceptance

**Maps to:** P31/P04/P23, P16C C03, P16A R10–R11.

## AT-ANN-01 — enclosure/fixture IQ

Record:

- ampoule/enclosure revision;
- sample and Hg-reservoir locations;
- internal/free volume where relevant;
- support fixtures;
- furnace-zone geometry;
- sensor positions;
- seal/evacuation method.

**PASS:** sample and reservoir boundary conditions are geometrically reconstructable.

## AT-ANN-02 — dual-temperature thermal map

Using an inert/dummy load, demonstrate independently logged:

- `T_s(t)` at sample position;
- `T_Hg(t)` at reservoir position;
- approximately 250–300 °C engineering mapping range;
- ramp/hold/cooldown response;
- zone cross-talk if zones are independently controlled.

For an isothermal first screen, demonstrate that the measured sample and reservoir temperatures satisfy the intended near-isothermal condition within a stated uncertainty rather than assuming identical controller setpoints imply equality.

**PASS:** `T_s(t)` and `T_Hg(t)` are independently traceable and the complete thermal trajectory is recoverable.

## AT-ANN-03 — one-hour dwell timing/stability

At approximately 250 °C, run a representative 1-h dummy dwell and quantify:

- temperature mean;
- drift;
- short-term fluctuation;
- sensor disagreement;
- timing error;
- cooldown reproducibility.

**PASS:** uncertainty/stability is adequate to distinguish the planned anneal-state map. No universal ±°C tolerance is manufactured here.

## AT-ANN-04 — enclosure integrity

Commission the seal/leak/vacuum or controlled-atmosphere method using an approved non-Hg surrogate configuration.

**PASS:** enclosure integrity meets the facility-approved criterion and the scientific pressure/atmosphere history is logged.

## AT-ANN-05 — HgCdTe/Hg residual gate

Only actual Hg-boundary operation can establish:

- Hg inventory/source state;
- effective `p_Hg` boundary behavior;
- carrier-state response;
- p/n state boundary;
- optical preservation;
- released dwell/cooldown.

Release through P05/P06/P23, not temperature/time alone.

---

# 7. AT-FTIR — FTIR composition/thickness station acceptance

**Maps to:** P06/P06A, P16C C04, P16A R08.

## AT-FTIR-01 — spectral range/resolution OQ

Demonstrate usable calibrated coverage approximately `500–5000 cm^-1` and resolution `<=4 cm^-1` for qualification unless P06 sensitivity analysis explicitly validates a coarser setting.

Use traceable spectral references covering the working region where available.

**PASS:** calibration residuals, resolution and spectral coverage are documented and sufficient to resolve the HgCdTe transmission edge/model parameters.

## AT-FTIR-02 — photometric repeatability / baseline

Using a stable blank/reference and representative transmissive witness:

- repeat background/sample acquisition;
- remove/reinsert witness;
- quantify baseline drift and repeatability;
- test aperture/beam-size effects;
- preserve raw interferograms/spectra where instrument permits.

**PASS:** repeated acquisition uncertainty is propagated into the P06 fitted edge/composition/thickness uncertainty and does not dominate the intended material discrimination.

## AT-FTIR-03 — mapping-stage registration

Commission at least the P06 9-point map geometry and, where practical, 5×5 development mapping.

Verify:

- stage coordinate repeatability;
- beam footprint/aperture;
- sample registration/orientation;
- coordinate export.

**PASS:** spectral map points can be tied to physical wafer coordinates and later device genealogy.

## AT-FTIR-04 — independent thickness reference

Using calibration films/steps or another traceable thickness method spanning the expected ~5–15-µm region, demonstrate the physical thickness-reference chain.

**PASS:** thickness reference uncertainty is known and can validate the optical fit rather than being circularly derived from it.

## AT-FTIR-05 — HgCdTe residual gate

Requires HgCdTe/CdZnTe spectra to validate:

- chosen optical model/constants;
- composition inference;
- edge metric behavior;
- substrate/etalon handling;
- map reproducibility on actual material.

---

# 8. AT-HALL — Hall / Van der Pauw station acceptance

**Maps to:** P05/P23/P31, P16C C05, P16A R09.

## AT-HALL-01 — magnetic-field OQ

Calibrate measured field at the sample position across the P05 initial grid:

`0, ±0.01, ±0.025, ±0.05, ±0.10, ±0.20, ±0.50 T`.

Verify polarity, zero/remanence, repeatability and spatial uniformity over the intended sample region.

**HARD-MINIMUM:** reach at least ±0.50 T.

Extended ~±2 T capability remains preferred, not mandatory.

**PASS:** B used in Hall reduction is measured/corrected at the sample state, not inferred solely from magnet current.

## AT-HALL-02 — current/voltage chain OQ

Using calibrated resistive networks and reversal sequences, verify:

- current magnitude and reversal;
- voltage gain/offset/noise;
- switching matrix continuity/isolation;
- common-mode behavior;
- time synchronization.

Test currents should include the order of magnitude expected in P05 (~10–100 µA initial series) without implying those are universally safe for every sample.

## AT-HALL-03 — cryogenic temperature OQ

Demonstrate stable measurement around 80 K and 300 K with calibrated sample-temperature proxy and complete thermal trajectory.

## AT-HALL-04 — Hall-reference surrogate PQ

Use a suitable Hall/semiconductor reference or independently characterized sample to test the full signed Hall reduction, field/current reversal and uncertainty propagation.

**PASS:** sign, magnitude and reversal symmetry are recovered within the reference uncertainty and the system correctly flags invalid/singular one-carrier reductions.

## AT-HALL-05 — HgCdTe residual gate

Actual HgCdTe required to validate:

- contact geometry/ohmicity;
- multi-carrier behavior;
- p/n transition handling;
- as-grown/post-anneal state.

---

# 9. AT-RIE — CH4/H2 RIE reactor acceptance

**Maps to:** P08/P24/P34, P16C C07, P16A R17–R18.

## AT-RIE-01 — gas MFC OQ

Calibrate at and around the candidate branch points:

- CH4 `10.6667 sccm`;
- H2 `53.3333 sccm`;
- total `64 sccm`.

Record gas-specific calibration, range, zero, repeatability and uncertainty.

**PASS:** the 1:5 candidate ratio and 64-sccm total are physically measurable/reproducible; they are not merely controller settings.

## AT-RIE-02 — pressure OQ

At representative flow/plasma conditions, calibrate process pressure around `100 mTorr`, including gauge identity, gas dependence/correction if applicable, dynamic stabilization and repeatability.

**PASS:** 100-mTorr process state is traceable with quantified uncertainty.

## AT-RIE-03 — RF / self-bias OQ

At the direct 50-W controller point, record:

- forward power;
- reflected power;
- matching state;
- RF frequency;
- self-bias or another calibrated sheath/ion-energy proxy;
- electrode/sample geometry.

**PASS:** forward W and a sheath/ion-energy proxy are both available. A 50-W display alone is insufficient for reactor equivalence.

## AT-RIE-04 — sample thermal surrogate PQ

Use a thermally representative dummy/witness to characterize sample/chuck temperature during the 60-s exposure and repeated runs.

**PASS:** sample thermal state is measured or bounded with a validated proxy and run-to-run behavior is documented.

## AT-RIE-05 — chamber-state reproducibility

Define and test:

- clean state;
- seasoning state;
- idle time;
- prior-process history;
- loading geometry;
- pumpdown/process pressure trace.

**PASS:** a repeatable chamber-state protocol exists; chamber genealogy is not omitted from runs.

## AT-RIE-06 — oxide-clear residual gate

A generic surrogate oxide may verify timing/endpoint instrumentation, but actual P25 anodic oxide on HgCdTe is required to establish `t_clear` for the selected stack.

Then separate:

`t_sem = t_RF - t_clear`.

## AT-RIE-07 — HgCdTe electrical residual gate

Actual HgCdTe required to establish:

- physical etch depth;
- conversion depth/sheet state;
- blocking behavior;
- `rho_c` interaction;
- detector noise/responsivity effect.

---

# 10. AT-MET — Cr/Au deposition acceptance

**Maps to:** P09/P26/P26A, P16C C08, P16A R19–R20.

## AT-MET-01 — vacuum/source IQ/OQ

Record tool/pump/gauge/source geometry, sample position, QCM position and source-to-sample geometry.

Demonstrate repeatable pumpdown/deposition pressure traces.

**No universal base-pressure number is assigned.**

## AT-MET-02 — Cr QCM/witness calibration

Deposit nominal 30-nm Cr witnesses over multiple runs.

For each retain:

- QCM raw thickness/rate;
- tooling/density/acoustic settings;
- independent witness thickness;
- location;
- pressure trace;
- sample/witness thermal proxy.

Fit/establish the local Cr tooling correction and uncertainty.

**PASS:** commanded/QCM thickness can predict witness thickness with uncertainty small enough to discriminate the released metal-thickness window once P26 defines it.

## AT-MET-03 — Au QCM/witness calibration

Repeat independently around nominal 270-nm Au.

Do not reuse the Cr tooling factor without measured equivalence.

## AT-MET-04 — sequential deposition PQ

Demonstrate the selected Cr->Au sequence, including whether vacuum is maintained between layers, timestamps, shutter/source changes and thermal history.

**PASS:** the full 30/270-nm stack can be reproduced on witnesses and independently measured.

## AT-MET-05 — sample thermal PQ

Measure or bound substrate/witness temperature for representative Cr/Au runs.

Holder temperature is not accepted as wafer temperature unless transfer is calibrated.

## AT-MET-06 — HgCdTe residual gate

Actual RIE-modified HgCdTe required for:

- adhesion without undocumented cleaning;
- lift-off on Mask-2 geometry;
- TLM `rho_c`;
- cryogenic stability;
- detector noise/contact behavior.

---

# 11. AT-DET — integrated 77–80 K detector-station acceptance

**Maps to:** P10/P10A/P11/P11A/P12/P12A/P12B/P12C/P13/P13A/P33, P16C C09, P16A R22–R27.

The station is accepted as an integrated measurement system, not as a list of individually working boxes.

## AT-DET-01 — cryogenic temperature / vacuum PQ

Using a dummy package/thermal load, demonstrate:

- repeatable 77–80 K operation;
- sample-temperature sensor calibration/proxy;
- cooldown/warmup trajectory;
- vacuum/purge state;
- temperature stability during representative electrical/optical measurements.

**PASS:** detector temperature and thermal state are quantitative, not inferred solely from coolant presence.

## AT-DET-02 — DC bias/load network OQ

Using precision dummy loads spanning the expected device range, verify:

- source voltage/current calibration;
- load resistor values and temperature state;
- terminal-voltage sensing;
- current limiting/protection;
- network transfer;
- dissipated-power calculation;
- safe sweep scripting/manual sequence.

The canonical future detector point is `E=10 V/cm`; the historical sweep reaches roughly 50 V/cm. Electric field acceptance is geometric:

`E = V_active/L_measured`.

**PASS:** terminal voltage/current are known at the DUT and field can be calculated from measured geometry with uncertainty.

## AT-DET-03 — radiometric wavelength/transfer OQ

Commission the optical chain over a first-build MWIR envelope approximately 2–6 µm, with:

- calibrated 4-µm point;
- coverage through/beyond ~4.4-µm edge;
- wavelength calibration;
- reference detector transfer;
- monochromator/filter/order suppression state;
- aperture/view-factor geometry;
- 1-kHz modulation capability.

**PASS:** incident spectral power at the DUT plane is traceable with an uncertainty budget and nominal “60° FOV” is not used as a substitute for geometry.

## AT-DET-04 — modulation/timebase OQ

Verify optical modulation frequency/waveform and reference phase, including the 1-kHz direct RP-01 spectral condition.

Record waveform factors used in responsivity conversion.

## AT-DET-05 — noise-chain electronics-floor PQ

With DUT replaced by appropriate terminations/dummy impedances, measure electronics-referred PSD/ASD across at least the historical 100-Hz–10-kHz region and any broader intended range.

Record:

- preamp complex gain;
- input voltage/current noise model;
- analyzer/digitizer transfer;
- FFT/window/ENBW normalization;
- cable/load state;
- repeated floor spectra.

The historical detector plateau ~24.5 nV/sqrtHz is a **comparison scale**, not a 1-kHz value.

If electronics are allocated fraction `beta` of detector plateau PSD, the design relation is:

`e_elec <= 24.5 sqrt(beta) nV/sqrtHz`.

Example only: `beta=0.10 -> e_elec<=7.75 nV/sqrtHz`.

This is not an RP-01 requirement.

**PASS:** the measured electronics floor and its uncertainty are low enough for the selected detector-noise objective and are stored separately from detector noise.

## AT-DET-06 — Johnson-noise absolute validation

Use traceable resistors at known temperature to compare measured voltage-noise PSD with:

`S_v = 4 k_B T R`

or the full network prediction when loading is non-negligible.

Test more than one resistance spanning the relevant impedance region.

**PASS:** PSD normalization, gain, temperature and loading jointly reproduce the physical reference within the combined uncertainty.

This is the strongest pre-HgCdTe absolute validation of the noise chain.

## AT-DET-07 — temporal/frequency transfer PQ

Using a known electrical/optical reference system, characterize the measurement transfer at least at:

- 1 kHz;
- 10 kHz;
- 100 kHz;
- 1 MHz;

and lower frequencies ~10–100 Hz where practical.

If a ~25-ns pulsed branch is used, the first-order instrument sizing check is approximately:

`BW ~ 0.35/25 ns ~ 14 MHz`.

This is a source/readout design check, not an RP-01 detector bandwidth.

**PASS:** source, reference detector, bias network, preamp, cable and digitizer transfer functions are separately known well enough to de-embed the DUT response.

## AT-DET-08 — package thermal-kernel PQ

Using a dummy heater/die or equivalent package stimulus, measure package thermal response over the time scales that could overlap P13 carrier dynamics.

**PASS:** package thermal poles are independently characterized so they cannot automatically be called carrier lifetime.

## AT-DET-09 — matched-state data integrity

Demonstrate one synthetic/dummy run in which DC, radiometry, noise and temporal datasets all carry the same explicit:

- DUT/package ID;
- contact pair;
- L/W/t geometry;
- temperature;
- bias/load;
- field;
- background/aperture/window state;
- timestamp/calibration IDs.

**PASS:** cross-module state identity can be reconstructed automatically or from controlled records without inference.

## AT-DET-10 — HgCdTe residual gate

Actual detector required to establish:

- R(T), self-heating and sweepout;
- absolute responsivity/QE;
- detector-terminal PSD and 1/f/g-r behavior;
- NEP/D*;
- detector frequency/transient response;
- matched-state performance.

---

# 12. AT-SING — singulation acceptance

**Maps to:** P35, P16C C10, P16A R28–R29.

## AT-SING-01 — dimensional/mechanical surrogate PQ

Use brittle II–VI-compatible or mechanically representative sacrificial material to characterize:

- commanded cut path;
- kerf;
- wander;
- edge chipping;
- support/protection behavior;
- tool load/speed or equivalent controlled variables;
- consumable/slurry genealogy.

For a low-force wire-saw branch, verify the tool can handle ~1-cm-class coupons at the deliberately slow screening conditions without uncontrolled fracture.

**PASS:** the mechanical process is reproducible and its edge-damage metrics are measurable.

## AT-SING-02 — clean/release surrogate PQ

Verify temporary mount/protection/slurry removal on representative oxide/metal witness structures without visible or measured attack.

**PASS:** clean/release chemistry is fully named and leaves no unacceptable residue/damage on the witness system.

## AT-SING-03 — CdZnTe/HgCdTe residual gate

Actual CdZnTe/HgCdTe/completed-stack coupons are required to establish:

- subsurface damage;
- functional edge damage;
- pre/post electrical/noise/responsivity change;
- completed-passivation/metal compatibility;
- cryogenic crack propagation.

No deep bromine damage-removal etch is introduced automatically.

---

# 13. AT-PKG — package / Dewar / interconnect acceptance

**Maps to:** P33/P15/P17A/P18A, P16C C11, P16A R30–R34.

## AT-PKG-01 — dummy package thermal/mechanical PQ

Build representative dummy assemblies with the selected carrier/cold-finger geometry and candidate compliant attachment family.

Measure:

- bondline thickness/coverage/void proxy;
- die tilt/position;
- thermal resistance/impulse response;
- cooldown/warmup;
- repeated thermal cycles;
- visual/mechanical integrity.

**PASS:** package thermal and mechanical state is repeatable and measurable.

## AT-PKG-02 — interconnect PQ

Using representative Cr/Au pad witnesses or package coupons, qualify the selected wire/ribbon/bond method for:

- continuity;
- resistance;
- pull/shear or equivalent integrity test where appropriate;
- pad damage;
- repeated cryogenic cycling;
- microphonic/noise susceptibility where measurable.

## AT-PKG-03 — optical geometry PQ

Measure:

- aperture dimensions;
- aperture-to-die spacing;
- window/filter material/thickness/coating;
- spectral transmission;
- shield geometry;
- alignment.

**PASS:** view factor/FOV is calculable from measured geometry; nominal angle labels are secondary descriptors only.

## AT-PKG-04 — vacuum/bake/cooldown PQ

Using dummy assembly, record pump/purge/bake/cooldown and pressure/temperature history.

**PASS:** the intended detector state near 77–80 K is repeatable without uncontrolled condensation/outgassing or unexplained thermal excursions under the selected local acceptance criterion.

## AT-PKG-05 — HgCdTe residual gate

Actual completed detector required for:

- cooldown crack survival;
- contact/interconnect stability;
- detector noise/responsivity change;
- package thermal interaction with P13;
- repeated thermal-cycle release.

---

# 14. Acceptance decision hierarchy

For each subsystem, P16D shall record:

1. IQ result;
2. OQ result;
3. surrogate PQ result;
4. open HgCdTe residual tests;
5. deviations/restrictions;
6. calibration expiration/requalification trigger;
7. linked raw-data location.

A subsystem may become `AT-SURROGATE-PQ-PASS` before HgCdTe is available.

`P16C-INFRASTRUCTURE-READY = YES` requires all mandatory infrastructure to have at least the state defined in P16C; it does not waive HgCdTe residual gates needed for P16A.

---

# 15. Requalification / change-control triggers

Re-run the affected acceptance tests after any change that can materially alter the transfer function or process state, including:

- furnace/boat/slider revision or position change;
- thermocouple/sensor replacement or relocation;
- MFC/gas/gauge replacement;
- anneal enclosure/fixture/zone change;
- FTIR source/detector/beamsplitter/stage/software-model change affecting calibration;
- Hall magnet/probe/current/voltage/switching/cryostat change;
- RIE electrode, RF, gauge, MFC, pump, chamber clean/season protocol or chuck change;
- evaporator source/QCM/head/sample geometry/pump/gauge change;
- detector-station preamp/load/cable/digitizer/reference detector/optics/cryostat change;
- singulation tool/consumable/support/protection change;
- package carrier/adhesive/bondline/interconnect/window/shield/vacuum change.

A calibration date alone is insufficient if configuration has changed.

---

# 16. Acceptance evidence package

Every accepted subsystem shall retain:

- signed/dated P16D row;
- tool configuration snapshot;
- calibration certificates/data;
- raw acceptance data;
- analysis/reduction files;
- uncertainty statement;
- deviations;
- photographs/drawings where geometry matters;
- software/firmware versions;
- next requalification trigger/date;
- explicit list of HgCdTe residual gates.

---

# 17. Round-42 permanent rules

1. **Tool installed != tool qualified.**
2. **Controller reaches setpoint != physical state calibrated.**
3. **Surrogate passes != HgCdTe process passes.**
4. **A numerical acceptance tolerance must trace to a process decision, measurement equation or explicit engineering allocation.**
5. **When literature gives only a process center, acceptance verifies capability at that center; it does not fabricate an unpublished process window.**
6. **For RIE, watts without self-bias/sheath state are insufficient.**
7. **For evaporated metal, QCM without independent witness calibration is insufficient.**
8. **For detector noise, analyzer display without absolute PSD/ENBW/gain validation is insufficient.**
9. **For detector dynamics, package/source/electrical transfer must be characterized before assigning intrinsic lifetime.**
10. **For LPE/anneal, actual material response remains the final residual gate.**

P36 closes the commissioning-method gap. It does not itself close any physical P16A readiness row.
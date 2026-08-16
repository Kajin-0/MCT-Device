# P18 — Failure-analysis / diagnostic atlas for RP-01 process development

**Status:** CONTROLLED DIAGNOSTIC FRAMEWORK.

## 1. Purpose

Provide a disciplined route from an observed process/device failure to:

1. plausible physical mechanisms;
2. the fastest discriminating measurement(s);
3. affected process module(s);
4. immediate containment action;
5. required requalification before release.

P18 is not a list of single-cause rules. HgCdTe process signatures are often non-unique.

The diagnostic sequence is:

`observed signature -> competing hypotheses -> discriminating data -> most-supported mechanism -> corrective action -> verification`.

## 2. Non-negotiable diagnostic rules

1. **Do not infer cause from one scalar metric.**
2. **Preserve pre-process baselines** whenever possible.
3. **Use matched controls/witnesses** to isolate process stages.
4. **Check measurement-chain artifacts before destructive rework.**
5. **Keep source/process genealogy intact.**
6. **Record failed/negative diagnoses**, not only successful fixes.
7. **Do not average away bimodality or spatial gradients.**
8. **Re-test the final detector function after corrective action**, not just the intermediate metric.

## 3. Failure record schema

Every failure-analysis record should contain:

- Failure ID;
- material/substrate/source/run/device genealogy;
- process revision;
- observed signature;
- measurement method/configuration;
- raw data location;
- expected/reference behavior;
- candidate mechanisms;
- discriminating test sequence;
- evidence for/against each mechanism;
- containment action;
- corrective action;
- requalification scope;
- final disposition;
- recurrence status.

---

# A. UPSTREAM MATERIAL / LPE FAILURES

## A1. Mean optical edge / inferred x is too red (Cd fraction too low)

### Signature

- P06 mean edge shifts to longer wavelength than target;
- full-spectrum fit indicates lower x;
- possibly detector cutoff also red-shifted after fabrication.

### Competing mechanisms

1. actual source composition too Hg-rich / Cd-deficient;
2. Hg-loss compensation too strong relative to intended source state;
3. growth temperature/liquidus/supercooling differs from qualified state;
4. source not equilibrated/homogeneous;
5. local temperature-sensor offset;
6. P06 optical-model/calibration error;
7. spatial grading makes one-point edge metric misleading.

### Fastest discriminating tests

1. repeat P06 with check standard / same-coordinate spectrum;
2. compare full spatial x/edge map, not one point;
3. inspect P03E measured liquidus and complete T(t);
4. recompute actual source composition from weighed masses;
5. compare source-use/run-order trend from P03D;
6. compare another wafer grown from same source lot.

### Affected modules

P03C, P03D, P03E, P03B, P06.

### Containment

Hold source charge and all wafers from the same source/thermal excursion until metrology versus true composition drift is resolved.

---

## A2. Mean optical edge / inferred x is too blue (Cd fraction too high)

### Competing mechanisms

1. source Cd fraction too high;
2. selective Hg loss from source;
3. source depletion after repeated growths;
4. growth temperature/trajectory shifted;
5. P06 calibration/model error;
6. unintended high-temperature post-growth composition change.

### Discriminating tests

- source-use index versus x trend;
- Hg-source state/mass/proxy;
- P03E liquidus shift;
- P06 pre- versus post-P04 matched-coordinate spectra;
- source mass-closure audit.

### Key clue

If as-grown P06 is correct but post-anneal P06 shifts blue, investigate P04/P04B thermal/Hg trajectory before changing P03 source composition.

### Affected modules

P03C/D/E, P04/P04B, P06.

---

## A3. Strong x gradient across wafer

### Signature

- P06 spatial map shows monotonic edge/x gradient;
- detector cutoff varies systematically by die position.

### Competing mechanisms

1. furnace axial/transverse gradient;
2. melt-depth/mass-transfer gradient;
3. source/substrate contact geometry;
4. Hg-loss/nonuniform vapor distribution;
5. substrate miscut/morphology interaction;
6. composition-model artifact caused by thickness/fringe fitting;
7. source depletion during contact across slider motion.

### Discriminating tests

- compare x map with P03E thermal map coordinates;
- compare x gradient with thickness gradient;
- rotate substrate orientation relative to furnace in controlled experiment;
- compare repeated runs at same boat orientation;
- inspect Hg-distribution groove/source geometry;
- independent composition measurement on selected points where available.

### Interpretation examples

- x gradient correlates with temperature map -> thermal-field suspect;
- x and thickness gradients co-vary with melt-flow direction -> mass-transfer geometry suspect;
- x gradient flips when substrate is rotated -> crystallographic/miscut interaction more likely.

---

## A4. Thickness too high at correct x

### Competing mechanisms

1. growth time too long;
2. supercooling too large;
3. local growth temperature lower than assumed;
4. melt inventory/depth changes growth-rate response;
5. source-use conditioning changes rate;
6. P06 thickness model error.

### Discriminating tests

- independent profilometry/cross-section thickness;
- P03B time/supercooling response model;
- actual TL/ΔT from P03E;
- source-use index from P03D.

### Key rule

Do not correct xL to solve a pure thickness problem until composition is shown to be the cause.

---

## A5. Thickness too low at correct x

Same diagnostic structure as A4, with likely directions reversed:

- contact time too short;
- insufficient supercooling;
- finite-source depletion/run-order effect;
- incomplete source/substrate contact;
- premature separation/wipe-off;
- thickness-model error.

Inspect growth-contact timestamps and substrate wetting evidence before modifying source composition.

---

## A6. Thickness nonuniformity with nearly uniform x

### Likely mechanisms

- local contact/wetting geometry;
- substrate bow/TTV;
- melt-depth variation;
- slider parallelism;
- wipe-off interaction;
- crystallographic step-flow/miscut morphology;
- local thickness-fit artifact.

### Discriminating tests

- compare thickness map to substrate TTV/bow;
- overlay residual-melt/wipe marks;
- repeat after rotating substrate in same boat;
- independent profilometry at map extremes;
- compare P07B face/miscut structures.

---

## A7. Residual Te-rich melt droplets / low usable area

### Likely mechanisms

- inadequate wipe-off geometry/contact;
- incorrect separation temperature;
- slider velocity/contact force inappropriate;
- melt inventory too large;
- wetting changes due substrate face/surface preparation;
- Hg-source/thermal state altering melt viscosity/composition.

### Discriminating tests

- map droplet position versus wipe direction;
- compare P03D melt inventory;
- inspect wipe-piece state/spacing;
- compare P07B face/miscut and P07C final surface state;
- quantify separation T from P03E.

### Containment

Do not send droplet-contaminated regions into mesa photolithography as if the issue were only cosmetic.

---

## A8. Rough / wavy / terraced morphology changes unexpectedly

### Competing mechanisms

- substrate miscut/polarity;
- growth time;
- supercooling;
- source depletion;
- final substrate chemical treatment;
- thermal gradient;
- heterogeneous nucleation from excessive supercooling.

### Discriminating tests

- compare P07B miscut direction/magnitude;
- P03B growth time/ΔT;
- P07C AFM/DIC before growth;
- source-use index;
- inspect for nucleated particles/secondary deposits.

---

## A9. Correct x and thickness but low electron mobility after anneal

### Competing mechanisms

1. impurity contamination from source/substrate/vessel;
2. high dislocation/twin density;
3. compensation/multicarrier state;
4. precipitate/anneal damage;
5. substrate impurity diffusion (e.g. Cu);
6. Hall reduction invalid;
7. surface inversion/channel contribution.

### Discriminating tests

- P05 variable-B Hall / mobility-spectrum test;
- HRXRD/EPD/structural map;
- SIMS/trace analysis where available;
- compare substrate lot/impurity record;
- P06 composition/thickness check;
- P13 lifetime proxy.

### Key clue

Low mobility at correct apparent one-carrier n may actually be multicarrier averaging. Test field dependence before changing anneal chemistry.

---

## A10. As-grown or post-anneal carrier type is wrong

### Signature

- p-type when n-type desired;
- n-type after a process intended to preserve p-type control coupon;
- sign changes with B or T.

### Competing mechanisms

- Hg-vacancy state not equilibrated;
- incorrect sample/reservoir temperature relation;
- insufficient dwell;
- cooldown trajectory changed;
- source/substrate impurity compensation;
- RIE/plasma exposure accidentally included;
- surface channel / multicarrier Hall sign artifact.

### Discriminating tests

- full P05 variable-B data;
- repeat Hall at multiple temperatures;
- audit P04B T_sample/T_reservoir/pHg trajectory;
- compare matched anneal coupon;
- inspect P06 pre/post composition;
- compare untouched bulk coupon against processed surface coupon.

---

## A11. Carrier density correct but highly non-reproducible run-to-run

### Competing mechanisms

- cooldown trajectory not controlled;
- Hg reservoir/source state varies;
- anneal initial state differs;
- source/substrate impurity lot effect;
- Hall measurement long-term variation;
- source-use/depletion effect feeding different as-grown vacancy state.

### Discriminating tests

- P17 variance-component analysis;
- P05 check-standard / measurement-system audit;
- run chronology versus P04B trajectory variables;
- source/lot random-effect comparison.

---

# B. MESA / PASSIVATION FAILURES

## B1. Mesa does not fully isolate active layer

### Signature

- residual lateral conduction after etch;
- unexpected low resistance between nominally isolated regions;
- profilometry shows insufficient depth.

### Likely mechanisms

- etch rate lower than assumed;
- local bath temperature/concentration drift;
- Br2 evaporation;
- film thicker than nominal;
- endpoint/fixed-time method inadequate.

### Discriminating tests

- P01 depth map;
- P06 local pre-etch layer thickness;
- bath temperature/age history;
- cross-sectional confirmation.

### Rule

Through-layer isolation is defined by measured depth + electrical isolation, not nominal etch time.

---

## B2. Excessive mesa undercut / active width too small

### Likely mechanisms

- wet-etch isotropy and time;
- higher bath temperature;
- Br2 concentration drift;
- resist adhesion/profile;
- overetch used to compensate rate uncertainty.

### Discriminating tests

- P01 lateral/vertical rates and anisotropy;
- P14 measured resist CD before etch;
- compare undercut versus depth and bath T;
- inspect resist edge lifting.

### Consequence

Use measured final active geometry in P10/P11/P12; do not use mask dimensions.

---

## B3. Rough mesa sidewalls / edge defects

### Competing mechanisms

- etch chemistry/temperature;
- damaged pre-etch surface;
- mask-edge defects;
- crystallographic face/miscut interaction;
- excessive overetch.

### Discriminating tests

- compare P01 surface roughness and anisotropy controls;
- inspect resist edge before etch;
- P02C perimeter-sensitivity test after passivation.

---

## B4. Oxide thickness correct but responsivity/noise poor after passivation

### Competing mechanisms

1. sidewalls inadequately passivated;
2. top-surface interface electrically poor despite correct thickness;
3. induction/agitation/electrochemical history changed;
4. fixed charge/interface state shifted;
5. contamination introduced during rinse/dry;
6. detector surface aged before/after oxide;
7. apparent change is measurement/bias heating.

### Discriminating tests

- P02 voltage-time trace versus qualified envelope;
- P02C P/A scaling;
- P13 lifetime before/after passivation;
- P12 1/f noise before/after;
- planar versus mesa witness comparison;
- check detector R(T)/self-heating.

### Rule

Oxide thickness is necessary but not sufficient evidence of passivation quality.

---

## B5. High 1/f noise appears after passivation

### Competing mechanisms

- interface traps / unstable native oxide;
- sidewall states;
- contact-window contamination later in flow;
- bias/heating changed because resistance changed;
- readout source-impedance noise not correctly referred;
- ambient aging/humidity before packaging.

### Discriminating tests

1. P12B electronics-noise check at matched source impedance;
2. P12 noise versus bias field at constant T;
3. P02C perimeter scaling;
4. time/aging study after passivation;
5. P13 transient/interface-trap signature.

---

## B6. Oxide formation voltage-time trace anomalous

### Possible mechanisms

- electrolyte concentration/age error;
- current-density error;
- poor electrical contact in anodization cell;
- agitation/bubble/mass-transfer difference;
- starting surface chemistry different;
- exposed area calculation wrong;
- endpoint instrument error.

### Discriminating tests

- verify actual current/area;
- check cell/reference electrical path;
- compare planar witness and device geometry;
- audit P07/P01 surface history;
- independent oxide-thickness measurement.

---

# C. LITHOGRAPHY / RIE / CONTACT FAILURES

## C1. Contact-window CD differs strongly from mask

### Competing mechanisms

- resist exposure/develop bias;
- chlorobenzene soak/profile effect;
- resist thickness variation;
- RIE lateral oxide clear;
- plasma-induced lateral electrical conversion beyond physical opening.

### Discriminating tests

Track full P14 chain:

`CD_mask -> CD_resist -> CD_RIE_open -> CD_n+ -> CD_metal`.

Do not diagnose from final metal image alone.

---

## C2. Oxide not fully cleared after RIE

### Signature

- high contact resistance;
- residual optical/ellipsometric oxide;
- patchy metal contact.

### Likely mechanisms

- local oxide thicker than witness;
- oxide etch rate changed with chamber history;
- insufficient `t_clear`;
- poor plasma uniformity;
- sample loading/self-bias difference.

### Discriminating tests

- P08D oxide-clear split;
- local oxide thickness;
- self-bias/pressure/temperature log;
- spatial contact-resistance map.

---

## C3. Physical HgCdTe recession excessive after RIE

### Competing mechanisms

- oxide clears too early, extending semiconductor exposure;
- self-bias/ion energy too high;
- sample temperature/chamber state changed;
- gas ratio changed;
- process time wrong.

### Discriminating tests

- compare `t_clear` and total RF time;
- profilometry `d_etch`;
- self-bias and sample T;
- chamber history;
- matched witness.

### Rule

Physical recession cannot be used as a proxy for electrical conversion depth.

---

## C4. RIE Hall result looks acceptable but TLM is poor

### Competing mechanisms

- surface contamination/oxide regrowth before metal;
- excessive damaged low-mobility surface sheet;
- metal deposition problem;
- incomplete oxide clear locally;
- lift-off residue;
- Hall reduction masks multicarrier surface state.

### Discriminating tests

- P08E multicarrier Hall/QMSA-type analysis;
- P09 RIE-to-metal delay audit;
- surface/metal morphology;
- TLM I-V linearity and regression;
- compare immediate versus delayed metal split.

---

## C5. TLM `rho_c` acceptable but detector still sweeps out badly

### Interpretation

This is a direct example of `rho_c != S_c`.

### Competing mechanisms

- majority-carrier ohmic behavior good but minority-carrier contact recombination remains high;
- n+ depth/doping insufficient;
- lateral blocking region geometry poor;
- active gap/field geometry drives carriers into contact region;
- contact region damaged/trapping.

### Discriminating tests

- P08F responsivity versus field;
- P13 `tau_eff(E)`;
- LBIC/spatial response near contacts;
- validated 2-D transport model;
- compare n+ depth/lateral extent.

---

## C6. TLM high and non-ohmic

### Likely mechanisms

- incomplete RIE/oxide clear;
- wrong metal/interface state;
- excessive atmospheric delay;
- Cr/Au thickness/deposition problem;
- contaminated lift-off residue;
- device damaged during probing/cooling.

### Discriminating tests

- room/80-K I-V symmetry;
- P08 oxide-clear witness;
- RIE-to-metal timing;
- P09 deposition pressure/rate history;
- metal thickness witness;
- microscopy.

---

## C7. Good TLM initially, degrades after cryogenic cycling

### Competing mechanisms

- metal adhesion/interdiffusion;
- die/package stress transmitted to contacts;
- wire-bond damage;
- oxide/interface aging;
- cracks/thermal-expansion mismatch.

### Discriminating tests

- TLM pre/post thermal cycle;
- optical/SEM metal inspection;
- package stress controls;
- bond pull/shear witness where appropriate;
- resistance/noise change localized by device geometry.

---

# D. DETECTOR ELECTRICAL / OPTICAL FAILURES

## D1. Resistance much higher than material prediction

### Competing mechanisms

- actual active geometry smaller/longer than assumed;
- low mobility / carrier density;
- contact resistance significant;
- mesa active cross-section overetched;
- device temperature different;
- current crowding/nonuniform field.

### Discriminating tests

- P14 measured geometry;
- P05 material state;
- TLM contact subtraction;
- R(T) temperature check;
- finite-element/2-D model if geometry nonuniform.

---

## D2. Resistance much lower than material prediction

### Competing mechanisms

- parasitic surface sheet conduction;
- RIE lateral/deep conversion encroaches active area;
- substrate leakage;
- incomplete mesa isolation;
- actual active gap shorter;
- carrier density higher than expected.

### Discriminating tests

- P08E multicarrier transport;
- P01 isolation check;
- substrate leakage witness;
- P14 gap metrology;
- Hall/material comparison.

---

## D3. Responsivity much lower than expected at low field

### Competing mechanisms

- poor passivation/surface recombination;
- incorrect optical power calibration;
- active area wrong;
- contact recombination;
- low lifetime;
- incorrect detector temperature;
- insufficient absorption/thickness;
- frequency response attenuates the chosen modulation frequency.

### Discriminating tests

- P11 reference detector / power transfer;
- P14 active area;
- P13 low-frequency plateau / tau;
- P02C perimeter sensitivity;
- P06 thickness/x;
- P10 actual T and field.

---

## D4. Responsivity rises then saturates/declines strongly with field

### Likely mechanisms

- minority-carrier sweepout;
- self-heating;
- field-dependent lifetime;
- contact-region recombination;
- load/readout compression.

### Discriminating tests

- P10 self-heating indicator;
- P08F sweepout control devices;
- P13 tau(E);
- check readout linearity;
- bias polarity comparison.

---

## D5. Responsivity asymmetry with bias polarity

### Competing mechanisms

- asymmetric contacts;
- lateral n+ conversion difference;
- geometry/metal difference;
- spatial generation asymmetry;
- package wiring/contact damage.

### Discriminating tests

- TLM/contact comparison for both sides;
- LBIC near each contact;
- microscopy/CD metrology;
- swap readout wiring while preserving optical geometry.

---

## D6. Detector spectral cutoff differs from P06 material expectation

### Rule

Do not immediately call this composition error.

### Competing mechanisms

- different cutoff convention;
- finite absorption/thickness;
- optical calibration/normalization;
- spatial x grading;
- P06 full-spectrum model error;
- detector response shaped by contacts/optics/passivation.

### Discriminating tests

- compare raw P06 transmission spectrum and raw detector response;
- report explicit edge/cutoff definitions;
- inspect thickness and x grading;
- independently calibrate monochromator/reference detector.

---

# E. NOISE / D* FAILURES

## E1. Measured white floor above expected Johnson + detector model

### Competing mechanisms

- preamp voltage/current noise;
- source-impedance interaction;
- EMI/grounding;
- contact excess noise;
- true g-r floor higher;
- analyzer normalization error;
- detector heating.

### Discriminating tests

1. P12B electronics floor using matched dummy resistance;
2. calibrated resistor Johnson-noise check;
3. detector bias-off/bias-on comparison;
4. source-impedance sweep;
5. shielding/grounding configuration test;
6. temperature/bias-power check.

---

## E2. 1/f knee much higher than historical ~3 kHz

### Competing mechanisms

- passivation/interface instability;
- poor contacts;
- higher bias/current density;
- self-heating;
- readout current noise coupled through higher detector resistance;
- environmental interference masquerading as 1/f;
- data reduction/window artifact.

### Discriminating tests

- normalize bias field/current/power;
- electronics floor versus source resistance;
- perimeter scaling;
- TLM and contact aging;
- repeat at multiple temperatures;
- PSD settings/window/stationarity audit.

---

## E3. Apparent g-r plateau changes with analyzer settings

### Diagnosis priority

Measurement artifact is likely until disproven.

### Discriminating tests

- verify ASD/PSD units;
- change FFT span/line count/window/averaging while preserving physical density;
- integrate known resistor PSD to expected RMS;
- P12B ENBW/normalization check.

A true detector spectral density should not scale incorrectly with arbitrary RBW/line count.

---

## E4. Good responsivity and noise separately, but D* unexpectedly poor

### Competing mechanisms

- wrong active area;
- responsivity/noise evaluated at different frequencies;
- noise not detector-referred;
- incorrect units;
- FOV/background mismatch;
- area includes inactive regions;
- calibration/reference power mismatch.

### Discriminating tests

Recompute from primitive quantities:

`D*(lambda,f) = R_lambda(f) sqrt(A_measured) / e_n(f)`.

Audit each input and its units independently.

---

## E5. Device appears BLIP only at some biases

### Competing mechanisms

- background shot/g-r dominance at favorable field;
- self-heating at higher field;
- contact sweepout;
- 1/f/electronics noise at lower field;
- optical background geometry changes.

### Discriminating tests

- controlled background on/off or temperature/FOV variation;
- field-dependent P11/P12/P10 dataset;
- compare measured background dependence to photon-statistics model.

---

# F. TEMPORAL / BANDWIDTH FAILURES

## F1. Measured bandwidth far lower than expected

### First question

Is the pole actually the detector?

### Competing mechanisms

- preamp/load/cable pole;
- optical modulator/chopper rolloff;
- lock-in filter;
- detector effective lifetime longer than expected;
- contact blocking increases carrier lifetime;
- traps/interface transients;
- package capacitance.

### Discriminating tests

- P13 external transfer de-embedding;
- reference fast detector;
- electrical injection through readout;
- compare bare die versus packaged;
- bias-field dependence;
- amplitude + phase fit jointly.

---

## F2. Frequency response is not single-pole

### Possible mechanisms

- bulk + surface recombination;
- contact-region dynamics;
- trap/interface states;
- multiple electrical poles not fully de-embedded;
- spatially varying generation/transport;
- thermal response.

### Discriminating tests

- amplitude and phase residuals;
- time-domain transient fit-window analysis;
- wavelength dependence;
- bias dependence;
- perimeter scaling;
- package/bare-die comparison.

Do not average multiple time constants into a claimed bulk lifetime.

---

## F3. Extracted lifetime changes with optical modulation amplitude

### Likely mechanism

Nonlinear/high-injection recombination or readout compression.

### Discriminating tests

- P13 low-injection linearity sweep;
- harmonic content;
- reduce modulation depth while holding mean background constant;
- check preamp overload/recovery.

---

## F4. Lifetime shortens strongly with field

### Competing mechanisms

- carrier sweepout/contact extraction;
- field-dependent recombination;
- self-heating;
- readout pole changes with detector resistance.

### Discriminating tests

- P10 thermal control;
- P08F contact comparison;
- de-embedded electrical chain at each resistance;
- spatial model/LBIC.

---

# G. PACKAGING / SYSTEM FAILURES

## G1. Bare die passes; packaged device develops higher noise

### Competing mechanisms

- microphonic pickup;
- package capacitance/readout interaction;
- wire-bond/contact degradation;
- grounding/shielding path;
- mechanical stress changes resistance/contact state;
- contamination/bake changes passivation.

### Discriminating tests

- bare-die versus package impedance/noise transfer;
- mechanical excitation/microphonic test;
- TLM/contact witness pre/post package;
- package capacitance;
- bias-off spectrum;
- thermal-cycle correlation.

---

## G2. Packaged detector resistance changes after bakeout

### Competing mechanisms

- HgCdTe/passivation thermal history altered;
- contact metallurgy changed;
- die-attach stress/outgassing;
- wire-bond damage;
- measurement temperature mismatch.

### Discriminating tests

- pre/post TLM or contact control;
- matched unbonded bake coupon;
- P05/P06 material witness if available;
- package stress/adhesive control;
- exact temperature-time history.

### Rule

Package bakeout is part of detector thermal history.

---

## G3. Responsivity falls after packaging but electrical resistance is stable

### Competing mechanisms

- optical aperture/window/vignetting;
- passivation contamination;
- package stress changes lifetime without large R change;
- alignment/FOV difference;
- contact sweepout due changed thermal boundary.

### Discriminating tests

- optical throughput/reference detector;
- remove/alter aperture if reversible;
- P13 lifetime pre/post;
- compare calibrated FOV;
- spatial beam scan.

---

## G4. Bandwidth falls only after packaging

### Likely mechanisms

- added capacitance/load;
- cable/interconnect pole;
- mechanical/thermal change in detector effective lifetime.

### Discriminating tests

- P13 electrical de-embedding bare/package;
- impedance/capacitance measurement;
- phase comparison;
- same detector at matched T/field.

---

# H. MEASUREMENT-SYSTEM FAILURES

## H1. Same sample gives different Hall density on different days

### First checks

- contact stability;
- magnet calibration;
- temperature;
- current/self-heating;
- field reversal;
- multicarrier curvature;
- instrument drift.

Use P17 measurement-process variance before declaring material aging.

---

## H2. FTIR x shifts without any physical process step

### Likely mechanisms

- spectrometer wavelength calibration;
- purge/background/reference changes;
- sample angle/position;
- thickness-model/fringe fit;
- temperature difference;
- analysis-version change.

### Discriminating tests

- reference standard;
- same raw spectrum with old/new analysis version;
- remount study;
- wavelength calibration check.

---

## H3. D* changes after software update

### Diagnosis priority

Audit calculation/model revision before process rework.

Check:

- ASD versus PSD units;
- ENBW;
- area units;
- responsivity frequency;
- optical power/reference normalization;
- background/FOV convention;
- filtering/averaging.

Preserve the previous analysis version for exact comparison.

---

# I. CROSS-MODULE DIAGNOSTIC CHAINS

## I1. Low D* with high 1/f and low lifetime

High-priority suspects:

- passivation/interface quality;
- sidewall recombination;
- contact damage;
- contaminated surface.

Recommended sequence:

`P12 electronics check -> P02C perimeter scaling -> P13 lifetime -> P09/P08 contact check -> surface/process-history audit`.

---

## I2. Low D* with good noise floor but low responsivity

High-priority suspects:

- radiometric calibration;
- absorption/thickness;
- lifetime/surface recombination;
- sweepout/contact blocking;
- active area/geometry.

Sequence:

`P11 calibration -> P06 material -> P14 geometry -> P13 lifetime -> P08F field sweep`.

---

## I3. Low D* with normal responsivity but high white noise

High-priority suspects:

- electronics/preamp;
- contact excess noise;
- true elevated g-r noise;
- temperature/bias heating.

Sequence:

`P12B dummy resistor -> T/current/power check -> TLM/contact -> detector-temperature sweep -> recombination model`.

---

## I4. Correct material metrics but poor device yield

Likely downstream/fabrication causes:

- lithography/CD;
- wet-etch variability;
- sidewall passivation;
- RIE/contact nonuniformity;
- lift-off/metal;
- packaging.

Use P17 yield stage breakdown to find where yield collapses rather than tightening upstream x unnecessarily.

---

## I5. Final devices vary strongly within one wafer

Compare spatial maps of:

- P06 x/thickness;
- P01/P14 geometry;
- oxide/passivation/perimeter;
- RIE/contact outcomes;
- final responsivity/noise.

If device variation tracks pre-fabrication P06 maps, upstream material dominates. If P06 is uniform but device outputs are spatially clustered by mask/chamber position, frontside processing dominates.

---

# J. CONTAINMENT / REQUALIFICATION LOGIC

## J1. Measurement artifact confirmed

- correct/recalibrate measurement system;
- reprocess affected data from preserved raw data where valid;
- no fabrication rework unless material/device actually changed;
- document analysis revision.

## J2. Upstream source/LPE cause confirmed

Contain:

- source charge;
- all wafers from affected source-use interval;
- related substrate lot if implicated.

Requalify P03/P07/P04 path as appropriate.

## J3. Anneal cause confirmed

Contain all coupons/wafers sharing:

- anneal run;
- reservoir state;
- cooldown trajectory;
- furnace/sensor anomaly.

Repeat P05/P06 before frontside continuation.

## J4. Frontside chemistry cause confirmed

Contain all devices sharing:

- bath/electrolyte lot;
- mask/process lot;
- RIE chamber state;
- metal deposition lot.

Use witness structures before reprocessing product wafers.

## J5. Package cause confirmed

Hold package process revision; retain passing bare-die baseline as the reference. Requalify package only unless evidence indicates bake/stress permanently changed detector material/frontside state.

---

# K. FAILURE-ANALYSIS PRIORITY RULE

When several mechanisms are plausible, choose the next test by the expected information gained per destroyed sample / time / cost.

Prefer initially:

1. re-analysis of preserved raw data;
2. nondestructive repeat metrology;
3. matched witness/control measurement;
4. spatial correlation across existing maps;
5. reversible parameter sweeps (T, field, frequency, optical power);
6. destructive section/chemistry only after the hypothesis space has narrowed.

This preserves scarce HgCdTe material and avoids correcting the wrong process stage.

# L. RELEASE INTEGRATION WITH P17

Every confirmed failure mechanism should feed P17:

- failure category frequency;
- process module;
- variance/capability impact;
- whether engineering limits need revision;
- whether measurement uncertainty was causal;
- change-control/requalification trigger.

A mature process should show not only improved average performance but a declining recurrence rate for previously identified failure modes.

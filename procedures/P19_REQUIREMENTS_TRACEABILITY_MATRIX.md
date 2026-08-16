# P19 — RP-01 requirements / physics / process traceability matrix

**Status:** CONTROLLED SYSTEM-INTEGRATION DOCUMENT.

## 1. Purpose

Make every controlled process variable traceable to a detector-level requirement.

The traceability chain is:

`detector requirement -> physical characteristic -> intermediate material/device metric -> controlling Pxx process -> measurement -> release criterion -> failure response`.

A process variable that cannot be connected to a detector requirement should be questioned rather than controlled by tradition alone.

P16A supplies the complementary readiness question: whether every required process/measurement branch is executable for a first traceable build.

## 2. Requirement maturity classes

- `HISTORICAL-REFERENCE` — value reported by RP-01 or same-lineage source; not automatically a production specification.
- `PHYSICS-REQUIREMENT` — required by device operation/architecture.
- `LOCAL-SPEC-OPEN` — physical quantity is required but numerical local specification must be established from qualification data.
- `LOCAL-QUALIFIED` — local numerical window demonstrated.
- `RELEASED` — statistical/process release established under P17.

## 3. Top-level detector requirements

The canonical RP-01 reproduction aims to demonstrate an n-type MWIR HgCdTe photoconductor that is comparable to the historical device in:

- spectral operating band / response edge;
- cryogenic operating temperature;
- responsivity;
- noise spectral density;
- detectivity / NEP;
- stable ohmic majority-carrier contacts;
- suppression of minority-carrier sweepout;
- useful frequency response;
- mechanical/singulation/package integrity;
- reproducibility/yield.

Historical references include:

- nominal x≈0.30;
- 9.5-µm active layer;
- n≈9.8×10^14 cm^-3;
- µ≈4×10^4 cm²/Vs;
- 80-K operation;
- detector response cutoff ~4.4 µm;
- 1/f knee ~3 kHz;
- g-r plateau ~24.5 nV/√Hz;
- D*~2×10^11 cm Hz^1/2/W at 4 µm;
- contact rho_c~9×10^-4 Ωcm² at 80 K.

Treat these as historical reference values unless a numerical tolerance is independently justified.

---

# A. SPECTRAL BAND / COMPOSITION TRACEABILITY

## Requirement A1 — detector responds in intended MWIR band

### Physical characteristics

- HgCdTe band structure / alloy composition x;
- temperature-dependent band gap;
- absorption coefficient versus wavelength;
- active-layer thickness;
- composition grading/nonuniformity.

### Intermediate metrics

- P06/P06A full transmission spectrum;
- optical edge descriptors;
- inferred x/model result;
- x spatial map;
- thickness map;
- final detector spectral response/cutoff under P11.

### Controlling processes

- P03C source composition/synthesis;
- P03D melt inventory/Hg loss/depletion;
- P03E actual liquidus/thermal field;
- P03B supercooling/time trajectory;
- P30 apparatus/contact/wipe/cooldown realization;
- P04/P04B/P31 composition/defect-state anneal.

### Failure response

P18 A1/A2/A3/D6.

### Status

Historical x≈.30 and detector cutoff ~4.4 µm are known; exact local specification linking P06 x/edge to detector response remains `LOCAL-SPEC-OPEN`.

## Requirement A2 — spectral response is spatially uniform across usable wafer area

### Protected by

- substrate quality/uniformity;
- furnace thermal field;
- melt mass-transfer uniformity;
- Hg-loss control;
- source conditioning.

### Metrics

- P06 x/edge map;
- detector cutoff map by die/position;
- P17 spatial versus run variance.

### Processes

P07/P29, P03D, P03E, P30, P06.

---

# B. ABSORPTION / ACTIVE-LAYER THICKNESS TRACEABILITY

## Requirement B1 — sufficient/controlled optical absorption and active volume

### Physical characteristics

- active layer thickness `d`;
- absorption coefficient `alpha(lambda)`;
- optical generation profile;
- photoconductive gain/lifetime geometry.

### Metrics

- P06/P06A thickness map;
- full-spectrum transmission fit;
- independent physical thickness reference;
- P11 responsivity;
- P13 wavelength-dependent time response where relevant.

### Processes

P03B/P03D/P03E/P30.

### Historical reference

`d≈9.5 µm`.

### Failure response

P18 A4/A5/A6/D3.

---

# C. BULK TRANSPORT / RESISTANCE / FIELD TRACEABILITY

## Requirement C1 — n-type low-density high-mobility active material

### Why

Carrier density and mobility control:

- resistivity;
- current at a given electric field;
- electric-field distribution;
- free-carrier absorption;
- photoconductive gain/transport;
- Johnson noise through device resistance;
- sensitivity to contact/surface channels.

### Metrics

- P05 carrier sign;
- `n_H` / multicarrier result;
- `mu_H`;
- sheet resistance;
- P10/P10A device R and I-V;
- P13 lifetime proxy.

### Processes

- P03/P30 source/growth material quality;
- P04/P04A/P04B/P31 native-defect/stoichiometry control;
- P07/P29 substrate impurity/interface control.

### Historical reference

- n≈9.8×10^14 cm^-3;
- µ≈4×10^4 cm²/Vs;
- historical measurement temperature unknown.

### Failure response

P18 A9/A10/A11/D1/D2.

## Requirement C2 — applied field is physically comparable among devices

### Why

Photoconductor gain, sweepout, heating and noise depend on electric field, not terminal voltage alone.

### Metrics

- P14 measured gap;
- P10/P10A detector contact voltage;
- `E=V_contact/L_measured`;
- current/power/temperature.

### Failure response

P18 D4/D5/F4.

---

# D. SUBSTRATE / EPITAXIAL INTERFACE TRACEABILITY

## Requirement D1 — low-defect, low-contamination epitaxial interface

### Physical characteristics

- lattice mismatch;
- dislocation/twin density;
- substrate inclusions;
- final surface damage/chemistry;
- clean-to-load history;
- meltback/interface reaction.

### Metrics

- P07/P29 HRXRD/EPD/inclusion map;
- P07B face/miscut output;
- P07C removed depth/roughness/chemistry proxy;
- P06 morphology/x/thickness;
- P05 mobility;
- P13 lifetime.

### Processes

P07/P07A/P07B/P07C/P29, P03/P30 interface/meltback.

### Failure response

P18 A6/A8/A9.

---

# E. STOICHIOMETRY / HG-VACANCY TRACEABILITY

## Requirement E1 — final native-defect state yields reproducible detector transport

### Physical characteristics

- Hg-vacancy concentration;
- donor/acceptor compensation;
- Hg chemical potential;
- defect diffusion/annihilation kinetics.

### Metrics

- P05 Hall/multicarrier state;
- P06/P06A pre/post optical state;
- P13 lifetime/device proxy.

### Processes

P04/P04A/P04B/P23/P31.

### Mandatory trajectory variables

- `T_sample(t)`;
- `T_reservoir(t)`;
- `pHg(t)`/source-state proxy;
- dwell;
- cooldown.

### Failure response

P18 A9/A10/A11.

---

# F. MESA / ELECTRICAL ISOLATION / GEOMETRY TRACEABILITY

## Requirement F1 — active geometry is electrically isolated and known

### Physical characteristics

- complete through-layer mesa isolation;
- lateral undercut;
- final active width/gap;
- sidewall roughness.

### Metrics

- P01/P28 depth/undercut;
- electrical isolation;
- P14/P32 CD chain;
- P10 measured active geometry.

### Processes

P01/P01A/P28/P32/P14.

### Failure response

P18 B1/B2/B3/D1/D2.

---

# G. PASSIVATION / SURFACE RECOMBINATION TRACEABILITY

## Requirement G1 — surfaces/sidewalls do not dominate recombination or low-frequency noise

### Physical characteristics

- interface state density / fixed charge;
- surface recombination velocity;
- sidewall coverage;
- oxide uniformity/stability;
- surface contamination/aging.

### Metrics

- P02/P25 oxide thickness and voltage-time/charge trace;
- P02C perimeter-to-area scaling;
- P12 1/f noise;
- P13 lifetime/perimeter dependence;
- responsivity.

### Processes

P02/P02A/P02B/P02C/P25.

### Historical reference

RP-01 native oxide ~80 nm.

### Failure response

P18 B4/B5/B6/I1.

---

# H. BLOCKING CONTACT / SWEEPOUT TRACEABILITY

## Requirement H1 — majority-carrier contact is ohmic/stable

### Metric

P09/P26 TLM `rho_c`, I-V symmetry, cryogenic stability.

### Historical reference

`rho_c≈9×10^-4 Ωcm² at 80 K`.

## Requirement H2 — minority-carrier contact loss is sufficiently blocked

### Physical characteristics

- converted-region depth/doping/profile;
- lateral extent;
- surface damage channel;
- minority-carrier contact recombination `S_c`;
- active field/contact geometry.

### Metrics

- P08D/P08E/P34 transport/depth;
- P08F responsivity versus field;
- P13 tau(E);
- LBIC/spatial response;
- final NEP/D*.

### Key distinction

`rho_c != S_c`.

TLM success does not prove sweepout suppression.

### Processes

P08 through P08G, P24/P34, P09/P09A/P26.

### Failure response

P18 C4/C5/C6/D4/F4.

---

# I. RESPONSIVITY TRACEABILITY

## Requirement I1 — calibrated absolute responsivity at defined lambda, field, frequency and T

### Physical dependence

Responsivity integrates:

- optical absorption;
- quantum efficiency;
- lifetime/gain;
- geometry;
- electric field;
- contact sweepout;
- modulation frequency;
- package/window/FOV state.

### Metrics/processes

- P11/P11A absolute radiometry;
- P10/P10A field/T;
- P13 dynamic attenuation;
- P14 active area;
- P06/P06A thickness/x;
- P08F blocking contacts;
- P33 package/window geometry.

### Failure response

P18 D3/D4/D5/I2.

---

# J. NOISE / NEP / D* TRACEABILITY

## Requirement J1 — detector-referred noise is measured at same operating point/frequency as responsivity

### Metrics

- P12/P12C ASD/PSD;
- P12B electronics floor/gain/window/ENBW;
- P10/P10A field/T/current/power;
- P11 R(lambda,f);
- package/background state.

### Calculation

`D*(lambda,f)=R_lambda(f) sqrt(A_measured)/e_n(f)`.

### Failure response

P18 E1–E5/I1–I3/H3.

## Requirement J2 — final D* meets system requirement

Historical reference:

~`2×10^11 cm Hz^1/2 W^-1` at 4 µm, 80 K, stated 60° FOV.

Historical value is not yet a local production tolerance.

P17 must define final engineering requirement/yield target.

---

# K. TEMPORAL RESPONSE / BANDWIDTH TRACEABILITY

## Requirement K1 — intrinsic detector bandwidth is known and adequate

### Physical characteristics

- bulk/surface/contact recombination;
- carrier sweepout;
- trapping;
- blocking-contact strength;
- external RC/readout;
- package thermal/electrical dynamics.

### Metrics

- P13/P13A de-embedded amplitude/phase;
- `f_-3dB`;
- `tau_eff`;
- time-domain decay;
- bias/wavelength dependence;
- P33 package thermal kernel.

### Key coupling

Stronger blocking can improve responsivity/D* while increasing lifetime and reducing bandwidth. Package poles can also mimic detector lifetime.

### Failure response

P18 F1–F4/G4.

---

# L. THERMAL / SELF-HEATING TRACEABILITY

## Requirement L1 — detector remains at defined operating temperature under bias

### Physical characteristics

- device resistance/current;
- Joule power;
- thermal conductance/package;
- temperature-dependent material properties.

### Metrics

- P10/P10A current/power/R(T) indicator;
- P33 package thermal state;
- cryostat sensor/calibration.

### Failure response

P18 D4/E1/E2/F4/G2.

---

# M. SINGULATION / DIE-EDGE TRACEABILITY

## Requirement M0 — separation does not create hidden mechanical, chemical or functional detector degradation

### Physical characteristics

- kerf/position error;
- visible chipping/crack geometry;
- subsurface damage;
- crystallographic crack propagation;
- residue/contamination;
- passivation/metal damage;
- functional edge-damage extent;
- cryogenic crack growth.

### Metrics

- P35 die dimensions/kerf/edge inspection;
- `d_visible`, `d_functional`, `d_release`;
- subsurface-damage witness measurement;
- pre/post P10 resistance/I-V;
- pre/post P12 noise;
- pre/post P11 responsivity where practical;
- P33 cryogenic edge-survival feedback.

### Processes

P35 with P29 crystallography and P33 cryogenic feedback.

### Requirement rule

`mechanically intact die != detector-function-qualified die`.

A room-temperature acceptable cut is not final until the package/cooldown route demonstrates no edge crack propagation or correlated detector degradation.

### Failure response

P18 singulation/package branches and P35 nonconformance record.

### Status

Historical RP-01 singulation method/edge exclusion remain open. Local numerical `d_release` remains `LOCAL-SPEC-OPEN` until a finished-device stack is qualified.

---

# N. PACKAGE / OPTICAL INTERFACE TRACEABILITY

## Requirement N1 — package does not degrade electrical/noise/bandwidth state

### Metrics

- bare-die versus packaged R/I-V;
- noise;
- P13 bandwidth;
- contact/TLM witnesses;
- P33 package thermal response;
- cryogenic cycling;
- P35 edge survival.

### Processes

P15/P33/P35.

### Failure response

P18 G1/G2/G4 plus P35/P33 nonconformance.

## Requirement N2 — package/window/aperture preserves calibrated optical throughput/FOV

### Metrics

- P11/P11A reference-detector throughput;
- actual aperture/FOV/view-factor geometry;
- packaged responsivity;
- spatial beam test;
- window/filter transmission.

### Processes

P11/P15/P33.

### Failure response

P18 G3.

---

# O. REPRODUCIBILITY / YIELD TRACEABILITY

## Requirement O1 — process is statistically stable and capable against detector-derived limits

### Metrics

P17 measurement-system and variance/capability register.

### Required variance separation

`measurement -> spatial -> run-to-run -> source/substrate lot -> long-term tool/operator`.

Include singulation-tool/consumable and package-construction genealogy where they contribute materially.

### Failure response

P18 recurrence/yield Pareto.

## Requirement O2 — changes are traceable and requalified by physical impact

### Metrics

P17/P17A change-control register.

### Examples

- substrate supplier change -> P07/P29/P03/P04 + detector verification;
- RIE chamber change -> P34/P08/P09 + detector functional contact verification;
- singulation blade/wire/laser/protection/clean change -> P35 edge/subsurface + selected P10/P12/P11 + P33 cryogenic survival;
- die-attach/carrier/interconnect change -> P33 + P10/P12/P13/P11 as physically affected;
- preamp change -> P12B unless detector loading changes.

---

# P. MASTER TRACEABILITY TABLE

| Final detector requirement | Protected physical characteristic | Intermediate metric | Primary control modules | Release layer | Failure atlas |
|---|---|---|---|---|---|
| MWIR spectral band | x/Eg/absorption | P06 x/edge + detector response | P03/P30/P04/P31/P06/P11 | P17 | A1-A3,D6 |
| Absorption/active volume | thickness | P06 d map | P03B/D/E/P30 | P17 | A4-A6,D3 |
| Correct resistance/transport | n,mu,geometry | P05 + P10 | P03/P30/P04/P31/P07/P29/P14 | P17 | A9-A11,D1-D2 |
| Low surface recombination | passivation/interface | lifetime,P/A,1/f | P02/P25/P02C/P13/P12 | P17 | B4-B5,I1 |
| Ohmic contact | majority contact | TLM rho_c | P08/P24/P34/P09/P26 | P17 | C2-C7 |
| Sweepout suppression | minority contact/S_c | R(E),tau(E),LBIC | P08F/P34/P13 | P17 | C5,D4,F4 |
| High responsivity | absorption/gain/lifetime | P11 R | P06/P08/P10/P13/P33 | P17 | D3-D5 |
| Low noise | bulk/surface/contact/readout | P12 ASD/PSD | P02/P08/P09/P12/P33 | P17 | E1-E3 |
| High D* / low NEP | R versus noise and area | P11+P12 | full chain | P17 | E4-E5,I1-I3 |
| Adequate bandwidth | lifetime/transport/RC/package thermal | P13 | P08/P10/P12/P33 | P17 | F1-F4,G4 |
| Singulation integrity | edge/subsurface/chemical damage | P35 + pre/post device metrics | P35/P29/P33 | P17 | P35/P18 |
| Cryogenic stability | edge/contact/package/passivation | pre/post package metrics | P09/P35/P15/P33 | P17 | C7,G1-G4,P35 |
| Optical package fidelity | aperture/window/FOV | P11 package-state radiometry | P11/P15/P33 | P17 | G3 |
| Reproducibility/yield | process stability | variance/yield | all Pxx | P17/P17A | all |

---

# Q. REQUIREMENT-CHANGE RULE

If a final detector/system requirement changes, use P19 to identify which intermediate specifications must be revisited.

Examples:

### Faster bandwidth required

Revisit:

- lifetime target;
- blocking-contact strength;
- active gap/field;
- package capacitance/thermal dynamics;
- readout bandwidth;

without automatically changing x or thickness.

### Longer wavelength required

Revisit:

- x / growth liquid/thermal state;
- absorption/thickness;
- Auger/background/noise regime;
- anneal/material state;

rather than simply re-labeling cutoff.

### Smaller die / reduced edge exclusion required

Revisit:

- P35 singulation branch;
- street/kerf control;
- functional edge-distance study;
- subsurface-damage evidence;
- P29 crystallography if scribe/cleave is used;
- P33 cryogenic edge survival.

Do not reduce mechanical street width from visible-chip statistics alone.

### Lower operating temperature / different FOV

Re-evaluate:

- background photon flux;
- BLIP condition;
- noise hierarchy;
- material transport;
- package/thermal configuration;
- cryogenic stress/singulation survival if cold endpoint changes.

---

# R. CURRENT STATUS

P19 provides qualitative/structural traceability now, including the finished-device singulation/package path.

Numerical requirement allocation remains `LOCAL-SPEC-OPEN` until detector/system requirements and local sensitivity/capability data exist.

When local data are generated, each row should be augmented with:

- numerical requirement;
- uncertainty budget;
- allocated intermediate tolerance;
- sensitivity coefficient;
- process capability/risk result;
- current release status.

P16A determines whether these controlled branches are executable for a first traceable build; P17 determines whether repeated evidence supports release.
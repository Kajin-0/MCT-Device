# Round 59 — operator-completeness and mathematical-typesetting revision

**Date:** 2026-08-17 America/New_York

## Purpose

Round 59 responds to the review of the Round-58 LaTeX artifact. Round 58 established the correct document class and professional mathematical typesetting, but two weaknesses remained:

1. residual pseudo-code notation survived in prose/tables (`A_wet`, `E_Smith`, `+/-`, raw inequalities, ASCII units, etc.);
2. several procedures still delegated execution through phrases such as “use the qualified method/carrier/procedure” rather than exposing what the researcher actually needs to know.

Round 59 therefore performs a full notation cleanup and an operator-question audit without changing the established Round-57 scientific/metrology conclusions.

## Document class

The active artifact is an **exhaustive research-fabrication protocol**: a hybrid of a scientific methods monograph, an SOP, and a process-development laboratory reference.

The governing question is:

> What exactly does the researcher do, with what material, tool, geometry, quantity, timing, measurement, calculation, acceptance criterion, failure response, and retained raw data?

A procedure is not considered complete merely because it cites a paper or an internal qualification file.

## Mathematical-typesetting closure

Round 59 removes the remaining code-like notation identified in the Round-58 visual review.

Examples now consistently appear as mathematics:

- `x_L`, `y_L`, `T_L`, `x_S`;
- `A_wet`, `t_clear`, `d_etch`, `rho_c`, `L_T`;
- `E_Smith`, `E_bulk,est`;
- `R_v(lambda)`, `A_Dstar`, `NEP`, `D*`;
- `T_record`, `T_rep`, `tau_slowest`;
- inequalities, plus/minus tolerances and powers of units.

The final source scan found no remaining matches for the residual pseudo-code patterns used in the audit.

## Operator-detail changes promoted into the main protocol

### Substrate electrical isolation

A concrete SYN guarded-leakage screen is included instead of the unqualified word “insulating” being the only operator gate:

- removable guarded electrodes separated by 5.0 mm;
- 10 V applied;
- 60 s settling;
- 30 s acquisition;
- research screen `|I_leak| <= 10 nA` and final-30-s drift <= 1 nA.

This does not become an RP-01 historical acceptance limit.

### Final CdZnTe surface

The bromine/methanol operation now names the certified bromine-compatible hood state rather than referring generically to an “appropriate hood.” Institutional PPE/EH&S authorization remains external to the process document.

### Te-rich source synthesis

The ampoule operation now gives numerical performance requirements while deliberately refusing to invent an unsupported quartz wall thickness:

- empty-ampoule helium leak rate <= 1e-8 mbar L/s;
- pre-seal pressure <= 1e-5 Torr after a 30-min isolated-manifold hold;
- 100 C/h ramp to 700 C;
- 8 h dwell;
- 50 C/h cool to 300 C, then furnace-off cool;
- do not open above 23 C;
- ampoule drawing, grade, dimensions, free volume, seal geometry and pressure/temperature qualification are required closure records.

### Horizontal-slider LPE

New explicit SYN implementation coordinates include:

- N2 purge >=5 measured tube-volume exchanges at 1 tube-volume/min;
- purge endpoints O2 <10 ppm and dew point < -60 C;
- H2 process flow at 1 measured tube-volume/min, actual sccm recorded;
- growth-region thermometry within 5 mm equivalent location and dummy-boat correction uncertainty <=1 C;
- nominal slider translation 2.0 mm/s with measured stroke/travel within +/-10%;
- disposable CdTe scribed-apron wipe-off reference with 1.0-mm diagonal scribe pitch.

Exact Honeywell boat machining dimensions remain unrecovered; Round 59 requires a local dimensioned boat drawing and thermal map rather than inventing them.

### Mask 1

Round 59 exposes a complete first reference implementation around the AZ4620 screening branch:

- 0.50 mL dispense;
- 4000 rpm / 30 s;
- 1000 rpm/s acceleration;
- 3.0 +/- 0.2 um target thickness;
- 365 nm / 300 mJ/cm2 nominal exposure;
- vacuum-contact exposure;
- exposure uniformity +/-5%;
- AZ400K:DI = 1:4 at 21 +/-1 C;
- gentle bath displacement every 15 s;
- 60 s DI rinse.

These are SYN transfer coordinates, not historical RP-01 Mask-1 facts.

### Mask 2

The direct RP-01 anchors remain 4–5 um resist, 80 C / 30 min prebake and 30-min chlorobenzene. Round 59 supplies a concrete screening implementation:

- 0.50 mL dispense;
- 3500 rpm / 30 s;
- 1000 rpm/s acceleration;
- 4.3 +/-0.3 um target;
- 365 nm / 150 mJ/cm2 nominal vacuum-contact exposure;
- 60 s developer at 21 C;
- 60 s DI rinse;
- profile-witness re-entrant undercut target 0.3–1.0 um per side before committing D1/T1 to RIE/metal.

### RIE

Carrier language is now geometrically explicit:

- sample center within 5 mm of powered-electrode center;
- same carrier revision used for thermal/self-bias qualification;
- full CdZnTe backside seating;
- no grease, adhesive or active-surface clamp shadow without separate qualification.

Reactor-equivalence screening now records dc self-bias and rejects a transfer when self-bias differs by > +/-10% from the reactor reference or the calibrated sample-temperature proxy exceeds 40 C.

### Cr/Au metallization

Round 59 makes the reference thermal-evaporation geometry more explicit:

- nominal source-to-sample distance 150 mm, held to +/-2 mm after QCM qualification;
- 10 rpm sample rotation during Cr and Au;
- cool under vacuum until holder <30 C for at least 10 min;
- vent with dry N2.

Direct RP-01 authority remains the 30/270-nm Cr/Au stack, not these SYN tool coordinates.

### Cryogenic packaging

The main protocol now exposes additional first screening coordinates:

- detector-seat flatness <=10 um over footprint;
- bondline target 50 +/-15 um measured at four die edges;
- die tilt <=1 degree;
- 25-um Au wire;
- first screening bond-force coordinate 5 gf;
- sacrificial pull-test screen >=2 gf with no pad lift before D1;
- after cycling, resistance change <2% at same T/field and no new discrete excess-noise feature.

These are research implementation coordinates, not RP-01 packaging facts.

### Absolute responsivity

The Round-57 underfilled radiant-power geometry remains. Round 59 additionally freezes useful instrument-operation coordinates:

- substitution-block source/reference stability <=0.5%;
- 1.000-kHz lock-in reference;
- 100-ms time constant;
- 24-dB/oct low-pass;
- settle >=5 lock-in time constants after wavelength motion;
- combined relative standard uncertainty target <=5% over 3–5 um.

## Explicit unresolved-coordinate appendix

Round 59 adds an operator-completeness appendix rather than hiding open apparatus coordinates.

It lists the exact closure records still required for:

- sealed source-synthesis ampoule geometry/qualification;
- horizontal-slider boat dimensions, clearances, well volumes and furnace/thermocouple map;
- Mask-1 and Mask-2 tool-specific spin/exposure/development characterization;
- RIE electrode/carrier/self-bias/thermal equivalence;
- metallization source/QCM/holder geometry;
- package carrier/adhesive/wire-bond construction;
- optical train and reference-detector implementation;
- noise/transient analog-chain and analysis-code identity.

This is not a return to blank forms. It is an explicit list of the remaining empirical apparatus knowledge that must be generated before claiming local executability.

## Artifact QA

Final Round-59 artifact:

- 62 physical PDF pages;
- letter size;
- text-native and unencrypted;
- 0 form fields / no XFA;
- all fonts embedded;
- no remaining overfull/underfull LaTeX box warnings;
- all 62 final pages rendered and visually inspected after final pagination repair;
- the standalone near-empty anodization evidence page from the intermediate build was removed;
- residual pseudo-code audit returned no matches for the targeted notation patterns.

SHA-256:

- PDF `bb51def36f7fdc8c25d595c8789286dd112938664adb0d96f5605141615d71ee`;
- TeX `352c170cca4c42d0bdeaea91878aa79e7020cdc12199ce69179ca81437dcc11b`.

## Scientific maturity

Round 59 introduces additional SYN execution coordinates but does not change the core maturity state:

- not a historical RP-01 reproduction;
- not an empirically validated end-to-end integrated fabrication line;
- not a production process capability release.

The next scientific pass should test whether the new SYN execution coordinates are the strongest defensible starting implementations and continue closing the explicit apparatus-coordinate appendix with primary evidence or actual local measurements.

# Recovery checkpoint — round 12 requirements traceability integration

**Date:** 2026-08-15 America/New_York

**Purpose:** Fast handoff after adding the requirements/physics/process traceability layer.

## 1. New file

- `procedures/P19_REQUIREMENTS_TRACEABILITY_MATRIX.md`

## 2. Purpose of P19

P19 links:

`final detector requirement -> physical characteristic -> intermediate metric -> controlling Pxx module -> release criterion -> P18 failure response`.

This prevents process variables from being controlled solely because they are historical or conventional.

## 3. Core detector requirements traced

P19 now traces:

- MWIR spectral band / detector response edge;
- active-layer absorption/thickness;
- low-density high-mobility n-type transport;
- low-defect epitaxial interface;
- Hg-vacancy/native-defect state;
- mesa isolation and measured geometry;
- surface/sidewall passivation;
- majority-carrier contact quality;
- minority-carrier sweepout suppression;
- absolute responsivity;
- detector-referred noise / NEP / D*;
- temporal response/bandwidth;
- self-heating/thermal stability;
- package electrical/optical integrity;
- reproducibility/yield/change control.

## 4. Example traceability chains

### Spectral band

`detector MWIR requirement -> x/Eg/absorption -> P06 edge/x map -> P03 source/inventory/liquidus/growth + P04 composition preservation -> P17 spec/capability -> P18 x/cutoff diagnostics`.

### Transport/resistance

`detector R/gain/noise requirement -> n,µ,geometry -> P05 + P10 -> P03/P04/P07/P14 -> P17 -> P18 low/high resistance & low-mobility chains`.

### Passivation

`low surface recombination / low 1/f -> interface/sidewalls -> P02/P02C + P12/P13 -> P17 -> P18 B4/B5/I1`.

### Blocking contact

`low sweepout -> minority-carrier contact loss/S_c -> P08F + P13 tau(E) + LBIC -> P17 -> P18 C5/D4/F4`.

Important distinction retained:

`rho_c != S_c`.

### D*

`D*=R(lambda,f)sqrt(A)/e_n(f)`

requires the whole chain:

- P14 measured area;
- P11 calibrated R at defined f;
- P12 detector-referred e_n at same f;
- P10 T/E;
- P17 final requirement/capability;
- P18 E4 diagnostics when the scalar D* appears inconsistent.

## 5. Requirement-change propagation

P19 now makes future architecture changes traceable.

Examples:

### Faster detector required

Primary revisit path:

- lifetime/contact blocking;
- active gap/field;
- package/readout capacitance;
- P13/P08/P10/P15.

Do not automatically change x/thickness.

### Longer-wavelength detector required

Primary revisit path:

- x / growth source & thermal state;
- absorption/thickness;
- material noise/recombination regime;
- anneal state.

Do not merely relabel the cutoff convention.

## 6. Requirement maturity

P19 uses:

- `HISTORICAL-REFERENCE`
- `PHYSICS-REQUIREMENT`
- `LOCAL-SPEC-OPEN`
- `LOCAL-QUALIFIED`
- `RELEASED`.

Most numerical tolerances remain `LOCAL-SPEC-OPEN` because no local repeated-device sensitivity/capability dataset exists yet.

The existing historical RP-01 scalar values remain reference points rather than fabricated tolerance bands.

## 7. Current complete process-control architecture

The repo now has four integration layers:

1. **P01–P16** — fabrication, material metrology, detector characterization and master traveler;
2. **P17** — measurement-system qualification, statistical process capability, release and change control;
3. **P18** — failure diagnosis, containment, corrective action and recurrence tracking;
4. **P19** — requirements/physics/process traceability.

## 8. Current major open historical variables

Despite the strong architecture, the following remain historically unresolved:

- exact RP-01/Fermionics substrate face/miscut/final clean;
- exact Honeywell x=.29 source synthesis / melt mass / well geometry;
- exact x=.29 equilibration/ramp;
- exact Fermionics anneal/cooldown;
- exact Br2 percentage basis in the best wet-mesa source;
- exact UWA native-oxide traveler;
- exact RP-01 resist/exposure/developer;
- exact CH4/H2 MFC values and Plasma Technology reactor geometry;
- exact condition tied to ~8-µm n+ depth;
- exact Cr/Au vacuum/rates/RIE-to-metal delay;
- historical low-noise preamp circuit/RBW/ENBW;
- package construction;
- exact contact pair used in historical device plots.

Crucially, each high-impact gap now has a local qualification method or an explicitly identified archival acquisition path.

## 9. Next logical work

The next integration step should be one of:

1. **manual assembly:** convert the modular files into a coherent chapter-ordered technical manual while preserving provenance/OPEN flags;
2. **requirements allocation:** derive the first numerical intermediate specifications from an explicit detector-level design target (e.g. exact desired spectral band, D*, bandwidth, operating background);
3. **simulation-assisted sensitivity:** use analytical/2-D models to estimate which open tolerances most strongly affect final performance and therefore deserve the tightest qualification effort.

Because no real fabrication data exist in this repo yet, P17 production capability numbers cannot be populated honestly.

## 10. Recovery order

1. `AGENTS.md`
2. this checkpoint after round 11
3. `procedures/P19_REQUIREMENTS_TRACEABILITY_MATRIX.md`
4. P17 and P18 integration files
5. branch-specific Pxx procedures for implementation.

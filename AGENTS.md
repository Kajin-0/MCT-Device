# AGENTS.md — MCT-Device front-door continuity record

## Mission

Build a source-traceable, end-to-end HgCdTe photodetector fabrication and characterization manual that a competent researcher can reproduce without undocumented tribal knowledge.

Canonical first process: **RP-01**, Smith et al., *Semiconductor Science and Technology* 16, 455–462 (2001), DOI `10.1088/0268-1242/16/6/306`.

There is **no end-to-end `REPRODUCIBLE-RELEASE` yet**. The repository now contains the complete control architecture from substrate/material preparation through detector characterization, statistical release, failure analysis and requirements traceability.

## Non-negotiable rules

1. Never invent a missing number. Use `OPEN`, `CAL`, `QUAL`, `PARTIAL`, `CANDIDATE-P`, or explicit derivation.
2. Never splice incompatible HgCdTe process families and call the result a published recipe.
3. Separate direct publication, derived physics, apparatus calibration and local qualification.
4. Every critical step needs outcome metrology and a pass/fail gate.
5. Preserve negative searches, rejected inferences, corrections and source conflicts.
6. Keep Hall quantities, optical-edge quantities, physical etch depth, electrical conversion depth, sheet density and measured geometry distinct.
7. Keep majority-carrier contact resistivity `rho_c` distinct from minority-carrier contact recombination velocity `S_c`.
8. Use measured fabricated geometry for field/area/D* normalization.
9. Treat passivation, post-RIE exposure, thermal cooldown and packaging as detector-process variables.
10. A measured system bandwidth is not detector bandwidth until external transfer functions are de-embedded.
11. Specifications come from physics/performance; observed process spread does not define its own passing limits.
12. Failure diagnosis uses competing hypotheses and discriminating tests; never force one cause from one symptom.
13. Every controlled process variable should trace forward to a final detector requirement.
14. Repository scientific specifications do not replace institution-specific Hg/Cd/Br2/HBr/H2/CH4/high-temperature/vacuum/cryogenic EH&S authorization.

## Current checkpoint — READ THIS FIRST

Latest recovery checkpoint:

`research/2026-08-15_checkpoint_after_source_recovery_round12.md`

Current integration files:

- `procedures/P17_STATISTICAL_PROCESS_CAPABILITY_RELEASE.md`
- `travelers/P17_PROCESS_RELEASE_CAPABILITY_REGISTER.md`
- `procedures/P18_FAILURE_ANALYSIS_DIAGNOSTIC_ATLAS.md`
- `travelers/P18_FAILURE_ANALYSIS_RECORD.md`
- `procedures/P19_REQUIREMENTS_TRACEABILITY_MATRIX.md`

For detailed source provenance, also read round-9/8/7/6 source and gap addenda.

## Controlled module set

- P01 wet mesa + P01A
- P02 anodic oxide + P02A/P02B/P02C
- P03 x≈0.30 LPE + P03A/P03B/P03C/P03D/P03E
- P04 Hg anneal + P04A/P04B
- P05 Hall/VdP
- P06 FTIR composition/thickness
- P07 CdZnTe + P07A/P07B/P07C
- P08 RIE blocking contact + P08A–P08G
- P09 Cr/Au/TLM + P09A
- P10 DC bias/self-heating
- P11 absolute radiometry
- P12 noise/PSD/NEP/D* + P12A/P12B
- P13 temporal response + P13A
- P14 lithography/CD + P14A
- P15 cryogenic package
- P16 master end-to-end traveler + blank traveler
- P17 statistical process capability/release + blank register
- P18 failure-analysis diagnostic atlas + blank failure record
- **P19 requirements / physics / process traceability matrix**.

## Direct RP-01 anchors — do not drift

### Material

- LPE n-HgCdTe on insulating CdZnTe
- nominal `x≈0.30`
- supplier `n=9.8×10^14 cm^-3`
- supplier `µ=4.0×10^4 cm²/V·s`
- thickness `9.5 µm`
- supplier n/µ measurement temperature not stated.

### Contact-window RIE

- Plasma Technology parallel-plate reactor
- printed `CH4/5H2`
- total `64 sccm`
- `100 mTorr`
- `50 W`
- `60 s`
- converted density `~2.0×10^15 cm^-3`, explicitly averaged over converted thickness
- mobility `~3.3×10^4 cm²/V·s`.

P08A secondary same-lineage evidence supports `CH4:H2=1:5`; conditional split 10.6667/53.3333 sccm. Not direct historical MFC closure.

P08B: if `d_conv≈8 µm`, conditional `N_s≈1.6×10^12 cm^-2`. Use sheet/multicarrier state plus independently measured depth.

### Mask-2/passivation/metal

- resist ~`4–5 µm`
- prebake `80 °C / 30 min`
- chlorobenzene `30 min`
- pattern/develop/water rinse
- anodic oxide `800 Å`
- Cr `300 Å`
- Au `2700 Å`.

### Geometry/TLM

- nine 300×300-µm contacts
- adjacent gaps 50–400 µm in 50-µm increments
- 80-K `rho_c≈9×10^-4 Ω·cm²`
- Figures 3/5/6/7 same device
- exact selected contact pair/gap remains `OPEN` and is not uniquely invertible from published D*/noise/responsivity.

### Detector benchmark

- 80 K
- stated 60° FOV
- spectral response at 1 kHz
- representative noise field 10 V/cm
- low-noise preamp + HP35665A
- 1/f knee ~3 kHz
- g-r plateau ~24.5 nV/√Hz
- cutoff ~4.4 µm
- BLIP D* ~`2.0×10^11 cm Hz^1/2 W^-1` at 4 µm
- QE ~70%.

Do not assume 24.5 nV/√Hz is the historical 1-kHz noise used in the spectral D* curve.

## Current material/process state

Historical Honeywell tie line:

`xL=.082, yL=.810, TL=507 °C -> historical xS≈.29`.

Derived source mass fractions Hg `.249738`, Cd `.012502`, Te `.737760`.

Historical source synthesis, charge mass/well volume, exact substrate face, final clean and exact anneal trajectory remain undisclosed, but all now have explicit local qualification paths.

### P03C/D/E

- source prep: mass closure/homogenization/material output;
- melt inventory/depletion: dimensioned geometry, source-use and Hg-loss state;
- liquidus/equilibration: actual `TL,heat`, local `ΔT_SC`, sensor/melt offset, spatial thermal field and convergence;
- temperature uncertainty derived from local process sensitivity.

### P07B/C

- select face/miscut from morphology/x/thickness/crystal quality/mobility/lifetime;
- final surface released by removed depth, morphology/chemistry proxy and clean-to-load history, not etch time alone.

### P04B

Cooldown is part of the Hg-stoichiometry process. Record `T_sample(t),T_reservoir(t),pHg(t)` and accept on `{carrier sign,n_H/multicarrier,µ_H,optical x/edge,thickness,morphology,lifetime}`.

## RIE/blocking-contact state

P08C/D/E govern source separation, reactor equivalence and multicarrier transport. The `50 W / 0.4 W cm^-2` electrode-area inference is rejected.

P08F/G require detector-level sweepout suppression without unacceptable noise/bandwidth penalty. `rho_c != S_c`.

## Frontside/passivation state

P01 x=.28 wet-mesa source: nominal 2% Br2 in3:1 EG:HBr, ~2.78 µm/min at21 °C; full primary text still does not define percentage basis.

P02 exact UWA traveler open. TI-family candidate: 0.1 M KOH /90% EG+10% DI, ~0.3 mA/cm², ~15 V, ~2 min, ~800 Å; x≈.30 lineage confirms strong surface-state/mass-transfer dependence.

P02C requires sidewall/perimeter passivation verification.

P09 historical Cr/Au 30/270 nm direct; vacuum/rates/RIE-to-metal delay locally qualified in P09A.

P14 exact resist/developer remains open; chlorobenzene supports a positive-resist undercut/lift-off mechanism class, not a product identity.

## Measurement state

P12A: later UWA work cites J. F. Siliquini's 1995 UWA PhD thesis for a custom bias-capable low-noise preamp. P12B closes local gain/noise/PSD/ENBW calibration independent of the missing historical circuit.

P13 bulk-lifetime interpretation requires low-field/bias-independence and external transfer de-embedding.

## P17 — statistical release

Engineering specification limits come from detector physics/performance, not observed process spread.

Before capability claims characterize measurement repeatability, long-term variation, stability, bias, resolution, linearity, configuration dependence and uncertainty.

Separate:

`measurement -> within-wafer spatial -> run-to-run -> source/substrate lot -> long-term tool/operator`.

P17 does not impose a generic Cpk threshold. Current end-to-end process remains below `PILOT-RELEASE` because no local repeated fabrication dataset exists.

## P18 — failure analysis

Diagnostic rule:

`signature -> competing mechanisms -> discriminating tests -> root cause -> containment/corrective action -> verification`.

Prefer raw-data reanalysis and nondestructive/reversible tests before destructive analysis. Every confirmed failure feeds P17 variance/yield/change-control records.

## P19 — requirements traceability

P19 now links:

`final detector requirement -> physical characteristic -> intermediate metric -> controlling Pxx process -> P17 release -> P18 failure response`.

Key traced requirements include:

- spectral band / x / absorption;
- active thickness;
- n-type low-density high-mobility transport;
- substrate/epitaxial interface quality;
- Hg-vacancy state;
- mesa isolation/measured geometry;
- passivation/surface recombination;
- majority-carrier contact quality;
- minority-carrier sweepout suppression;
- absolute responsivity;
- noise / NEP / D*;
- intrinsic bandwidth;
- self-heating;
- package electrical/optical integrity;
- reproducibility/yield.

Requirement maturity labels:

- `HISTORICAL-REFERENCE`
- `PHYSICS-REQUIREMENT`
- `LOCAL-SPEC-OPEN`
- `LOCAL-QUALIFIED`
- `RELEASED`.

Most numerical tolerances remain `LOCAL-SPEC-OPEN` because local sensitivity/capability data do not yet exist.

## Current architecture

The repository now has four integrated layers:

1. **P01–P16:** fabrication/material/device methods + end-to-end traveler;
2. **P17:** statistical process release/capability/change control;
3. **P18:** failure diagnosis/corrective action;
4. **P19:** final-requirement-to-process traceability.

## Next logical work

Three strong next paths:

1. **Manual assembly:** synthesize P01–P19 into chapter order without losing provenance and OPEN flags.
2. **Numerical requirement allocation:** choose an explicit detector-level design target and derive first intermediate tolerances/sensitivity budgets.
3. **Analytical sensitivity ranking:** estimate which currently open process variables have the largest effect on final D*, responsivity, noise and bandwidth, so qualification effort is prioritized rationally.

Do not populate production capability/tolerance numbers without local repeated-device data.
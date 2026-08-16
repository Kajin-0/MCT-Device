# AGENTS.md — MCT-Device front-door continuity record

## Mission

Build a source-traceable, end-to-end HgCdTe photodetector fabrication and characterization manual that a competent researcher can reproduce without undocumented tribal knowledge.

Canonical first process: **RP-01**, Smith et al., *Semiconductor Science and Technology* 16, 455–462 (2001), DOI `10.1088/0268-1242/16/6/306`.

There is **no end-to-end `REPRODUCIBLE-RELEASE` yet**. The repository contains a controlled qualification/transfer architecture from CdZnTe substrate through LPE, Hg anneal, frontside processing, packaging, radiometry, noise and temporal characterization.

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
12. Repository scientific specifications do not replace institution-specific Hg/Cd/Br2/HBr/H2/CH4/high-temperature/vacuum/cryogenic EH&S authorization.

## Current checkpoint — READ THIS FIRST

Latest recovery checkpoint:

`research/2026-08-15_checkpoint_after_source_recovery_round10.md`

Current process-release files:

- `procedures/P17_STATISTICAL_PROCESS_CAPABILITY_RELEASE.md`
- `travelers/P17_PROCESS_RELEASE_CAPABILITY_REGISTER.md`

For the latest physics/source state also read:

- `docs/SOURCE_LEDGER_ADDENDUM_ROUND9.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND9.md`
- earlier round addenda for RIE, blocking contacts, source synthesis, substrate and frontside history.

## Current controlled module set

Important modules/addenda:

- P01 wet mesa + P01A
- P02 anodic oxide + P02A/P02B/P02C
- P03 x≈0.30 LPE + P03A/P03B/P03C/P03D/P03E
- P04 Hg anneal + P04A/P04B
- P05 Hall/VdP
- P06 FTIR composition/thickness
- P07 CdZnTe + P07A/P07B/P07C
- P08 RIE blocking contact + P08A through P08G
- P09 Cr/Au/TLM + P09A
- P10 DC bias/self-heating
- P11 absolute radiometry
- P12 noise/PSD/NEP/D* + P12A/P12B
- P13 temporal response + P13A
- P14 lithography/CD + P14A
- P15 cryogenic package
- P16 master end-to-end traveler + blank traveler
- **P17 statistical process capability/release + blank capability register**.

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

## Upstream material state — rounds 8–9

### Honeywell tie line

Best explicit composition anchor:

`xL=.082, yL=.810, TL=507 °C -> historical xS≈.29`.

Derived source mass fractions:

- Hg `.249738`
- Cd `.012502`
- Te `.737760`.

Historical source synthesis, charge mass/well volume, exact substrate face and exact anneal trajectory remain undisclosed.

### P03C/P03D source and melt

Honeywell treats the Te-rich source as already prepared and gives no well volume/charge mass.

Local release therefore uses:

- source mass closure/composition/homogenization;
- dimensioned well/melt inventory;
- source-use/depletion state;
- Hg-loss proxy;
- resulting P06 x/thickness and P05/P13 material quality.

Do not combine the Radhakrishnan x≈.20 branch's 700 °C/8 h, ~4.8 g/run and 3-g HgTe values with the Honeywell tie line as historical data.

### P03E liquidus/equilibration/thermal metrology

Do not equate controller temperature to actual melt liquidus.

Use/record:

- `TL,heat` as equilibrium liquidus reference;
- `Tnuc,cool` separately;
- local `ΔT_SC=TL,measured-T_contact`;
- sensor calibration and source-to-sensor offset;
- spatial thermal map;
- hold-time convergence;
- local `∂x/∂T`, `∂d/∂T`.

Derive allowed temperature uncertainty from material tolerances rather than arbitrary controller precision.

### P07B/P07C substrate face and final surface

Exact historical CdZnTe polarity/miscut/final clean remain open.

Independent x=.30 Te-rich slider work supports low-degree `{111}` miscut screening but does not prove RP-01 polarity.

Final surface release is based on:

`Y_surface={removed depth,roughness,pit/wave density,chemical-state proxy,t_clean-to-load,epilayer morphology,interface defect,mobility,lifetime}`.

Brief 2–3% Br2/methanol immediately before boat loading is a different-composition LPE candidate, not historical RP-01.

### P04B cooldown trajectory

Cooldown is part of the Hg-stoichiometry process.

Kawazu x=.20 work proves quench versus gradual cooling after matched Hg-rich anneal can change final carrier state; its 8 h/~200 min values are not transferred.

Jones/Quelch/Capper/Gosney x≈.17–.31 show isothermal versus two-temperature sample/reservoir conditions can drive different carrier states and kinetics.

Record:

`T_sample(t), T_reservoir(t), pHg(t)`

through dwell and cooldown.

Illustrative only: at `D_Hg~1e-9 cm²/s`, diffusion length in 200 min is ~35 µm and `L²/D` across 9.5 µm is ~15 min. This demonstrates cooldown relevance, not a timing recommendation.

Final gate:

`Y_cool={carrier sign,n_H/multicarrier,µ_H,optical x/edge,thickness,morphology,lifetime}`.

## RIE/blocking-contact state

P08C/D/E govern source separation, reactor equivalence and multicarrier transport. Do not infer historical electrode area from `50 W/0.4 W cm^-2`.

P08F/G require detector-level sweepout suppression without unacceptable noise/bandwidth penalty. `rho_c != S_c`.

## Frontside/passivation state

P01 x=.28 wet-mesa source: nominal 2% Br2 in 3:1 EG:HBr, ~2.78 µm/min at21 °C, anisotropy ~.63, best RMS ~2 nm; full primary text still does not define percentage basis.

P02 exact UWA traveler open. TI-family candidate: 0.1 M KOH /90% EG+10% DI, ~0.3 mA/cm², ~15 V, ~2 min, ~800 Å. x≈.30 Janousek/Carscallen lineage supports strong surface-state/mass-transport dependence.

P02C requires sidewall/perimeter passivation verification.

P09 historical Cr/Au 30/270 nm direct; vacuum/rates/RIE-to-metal delay open and locally qualified in P09A.

P14 chlorobenzene is consistent with positive diazo/novolak undercut lift-off; exact resist/developer open.

## Measurement state

P12A: later UWA work cites J. F. Siliquini's 1995 UWA PhD thesis for a custom bias-capable low-noise preamp. Thesis remains actionable archival target. P12B closes local gain/noise/PSD/window/ENBW/Johnson-noise calibration.

P13: bulk-lifetime interpretation requires low-field/bias-independence and external transfer de-embedding.

## P17 — statistical release state

P17 now defines how `QUAL` becomes a released local process window.

### Key rule

**Engineering specification limits come from detector physics/performance, not observed process spread.**

Only evaluate capability after the process is stable/in-control and the measurement system is qualified.

### Measurement-system requirements

Characterize each critical metric for:

- repeatability;
- long-term/reproducibility variation;
- stability/drift;
- bias;
- resolution;
- linearity;
- geometry/configuration dependence;
- uncertainty.

Do not use one wafer's spatial map points as independent LPE-run replicates.

### Variance hierarchy

Separate:

`measurement -> within-wafer spatial -> run-to-run -> source/substrate lot -> long-term tool/operator`.

### Capability

P17 includes standard `Cp/Cpk` forms for stable approximately normal processes but deliberately does **not** hard-code a generic Cpk ≥1.33/1.67 production rule.

Required capability/yield risk must be defined by the actual detector program.

### Release maturity

- `OPEN`
- `CANDIDATE-P`
- `LOCAL-QUALIFIED`
- `PILOT-RELEASE`
- `PRODUCTION-RELEASE`.

Current RP-01 reconstruction remains below `PILOT-RELEASE` because no local repeated fabrication dataset exists.

`travelers/P17_PROCESS_RELEASE_CAPABILITY_REGISTER.md` is the blank controlled register for measurement-system results, engineering limits, variance components, capability/risk, coupled LPE/anneal/RIE windows, yield, change control and signoff.

## Next integration target

Build the **failure-analysis / diagnostic atlas**:

`observed signature -> plausible mechanisms -> discriminating measurement -> affected Pxx module -> containment/requalification`.

Priority signatures should include:

- cutoff/x drift;
- thickness gradient;
- p-type or wrong n after anneal;
- low mobility at correct carrier density;
- residual melt / poor morphology;
- excessive mesa undercut;
- high 1/f after passivation;
- poor TLM;
- responsivity sweepout;
- noise plateau mismatch;
- unexpectedly low bandwidth;
- package-induced drift/noise.

The atlas must preserve ambiguity: use discriminating tests rather than forcing one cause from one symptom.
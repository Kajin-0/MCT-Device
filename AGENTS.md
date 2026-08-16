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
11. Repository scientific specifications do not replace institution-specific Hg/Cd/Br2/HBr/H2/CH4/high-temperature/vacuum/cryogenic EH&S authorization.

## Current checkpoint — READ THIS FIRST

Latest recovery checkpoint:

`research/2026-08-15_checkpoint_after_source_recovery_round9.md`

Current source/gap overrides:

- `docs/SOURCE_LEDGER_ADDENDUM_ROUND9.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND9.md`
- round-8 addenda for source synthesis/melt inventory/substrate face;
- round-7 addenda for sidewall passivation/blocking-contact function;
- round-6 addenda for RIE reactor/LBIC/multicarrier state;
- earlier addenda for lithography, metallization and measurement-chain history.

## Current controlled module set

Important modules/addenda:

- P01 wet mesa + P01A
- P02 anodic oxide + P02A/P02B/P02C
- P03 x≈0.30 LPE + P03A/P03B/P03C/P03D/**P03E liquidus/equilibration/thermal metrology**
- P04 Hg anneal + P04A + **P04B cooldown-trajectory qualification**
- P05 Hall/VdP
- P06 FTIR composition/thickness
- P07 CdZnTe + P07A/P07B/**P07C final surface/clean-to-load**
- P08 RIE blocking contact + P08A through P08G
- P09 Cr/Au/TLM + P09A
- P10 DC bias/self-heating
- P11 absolute radiometry
- P12 noise/PSD/NEP/D* + P12A/P12B
- P13 temporal response + P13A
- P14 lithography/CD + P14A
- P15 cryogenic package
- P16 master end-to-end traveler + blank traveler.

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

Historical source synthesis, charge mass/well volume and exact substrate face remain undisclosed.

### P03C source synthesis

Honeywell treats the Te-rich source as an already prepared charge. Local source preparation is released through mass closure, homogenization/liquidus behavior, P06 x/thickness, P05 mobility, P13 lifetime/device proxy and source conditioning/reuse.

Do not combine the different Radhakrishnan x≈.20 branch's 700 °C/8 h, ~4.8 g/run and 3-g HgTe numbers with the Honeywell tie line as historical data.

### P03D melt inventory/depletion

Honeywell patent gives no well dimensions or charge mass. Primary finite-liquid modeling shows growth rate can fall after a liquid-depth-related characteristic time and Hg loss can drive material Cd-richer.

Use:

`d_layer=f(t_growth,ΔT,thermal trajectory,liquid inventory/depth,source-use index,Hg-loss state)`.

Track run-order x/thickness/morphology and release depletion limit from measured drift.

### P03E liquidus/equilibration/thermal metrology

Do not equate controller temperature to actual melt liquidus.

Use/record:

- heating liquidus `TL,heat` as equilibrium reference;
- cooling nucleation `Tnuc,cool` separately;
- local `ΔT_SC = TL,measured - T_contact`;
- sensor calibration;
- source-to-sensor offset;
- spatial temperature map;
- hold-time convergence;
- local `∂x/∂T` and `∂d/∂T`.

Derive temperature uncertainty from material tolerances, e.g. `u_T <= u_x,T/|∂x/∂T|`, rather than imposing arbitrary ±0.01 °C stability.

Harman's ~1 h at 550 °C is an independent Te-rich equilibration benchmark only, not the Honeywell hold.

### P07B face/miscut

Exact RP-01/Honeywell polarity remains open. Independent x=.30 Te-rich slider work on `(111)Cd` CdTe shows significant morphology changes over ~0–2° miscut. Use only as a local DOE anchor; substrate/process differ.

### P07C final surface / clean-to-load

Exact Fermionics final CdZnTe clean remains open.

LPE-specific different-composition branch supports brief 2–3% Br2/methanol immediately before graphite-boat loading. Independent CdZnTe surface studies show Br-MeOH removes polishing damage but leaves a Te-rich surface and can shift morphology between pitting/waviness.

Release on:

`Y_surface={removed depth,roughness,pit/wave density,chemical-state proxy,t_clean-to-load,epilayer morphology,interface defect,mobility,lifetime}`.

Record rinse/dry and clean-to-load timestamps. Requalify when face/miscut changes. Couple with meltback removed depth.

### P04B cooldown trajectory

Cooldown is part of the Hg-stoichiometry process.

Kawazu et al. 1995, x=.20, directly showed quench versus gradual cooling after the same Hg-rich anneal can change final carrier type. Its 8 h / ~200 min conditions are **not** transferred to RP-01.

Jones/Quelch/Capper/Gosney x≈.17–.31 show isothermal versus two-temperature reservoir/sample paths can drive different carrier states and affect time to equilibrium.

Therefore record:

`T_sample(t), T_reservoir(t), pHg(t)`

through dwell and cooldown.

Illustrative only: using Kawazu's `D_Hg>~1e-9 cm²/s`, a 200-min diffusion length is >~35 µm and `L²/D` across 9.5 µm is ~15 min. This demonstrates cooldown relevance, not an RP-01 timing recommendation.

Final anneal/cooldown gate:

`Y_cool={carrier sign,n_H/multicarrier,µ_H,optical x/edge,thickness,morphology,lifetime}`.

## RIE/blocking-contact state

Do not conflate p-type conversion branches with RP-01 n-type contact processing. P08C/D/E govern source separation, reactor equivalence and multicarrier transport.

The `50 W / 0.4 W cm^-2 =125 cm²` electrode-area back-calculation is rejected because identical reactor geometry is unproven.

P08F/G require detector-level sweepout suppression without unacceptable noise/bandwidth penalty. `rho_c != S_c`.

## Frontside/passivation state

P01 x=.28 wet-mesa source: nominal 2% Br2 in 3:1 EG:HBr, ~2.78 µm/min at 21 °C, anisotropy ~.63, best RMS ~2 nm; full primary text still does not define percentage basis.

P02 exact UWA traveler open. TI-family candidate: 0.1 M KOH /90% EG+10% DI, ~0.3 mA/cm², ~15 V, ~2 min, ~800 Å. x≈.30 Janousek/Carscallen lineage supports dissolution–precipitation and strong surface-state/mass-transport dependence.

P02C requires sidewall/perimeter passivation verification because RP-01 anodizes after mesa.

P09 historical Cr/Au 30/270 nm direct; vacuum/rates/RIE-to-metal delay open and locally qualified in P09A.

P14 chlorobenzene is consistent with positive diazo/novolak undercut lift-off; exact resist/developer open.

## Measurement state

P12A: later UWA work cites J. F. Siliquini's 1995 UWA PhD thesis for a custom bias-capable low-noise preamp. Thesis remains an actionable archival target. P12B closes local gain/noise/PSD/window/ENBW/Johnson-noise calibration.

P13: same-UWA x≈.30 work near 77 K deliberately uses low bias to avoid sweepout into high-recombination contacts. Bulk-lifetime interpretation requires low-field/bias-independence plus external transfer de-embedding.

## Next phase

The major historical blanks now have explicit local qualification paths. The next logical phase is **statistical process release**:

1. define measurement-system qualification before capability claims;
2. convert repeated P03/P04/P05/P06 results into numerical process windows;
3. separate within-run, wafer-spatial, run-to-run and lot-to-lot variance;
4. define engineering specification limits from detector physics/performance, not from observed process spread;
5. define change-control/requalification rules when apparatus, source chemistry, substrate face or downstream surface history changes.

Do not set capability thresholds or production tolerances before the measurement uncertainty and detector-relevant specification limits are defensible.
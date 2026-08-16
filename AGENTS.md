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
9. Treat passivation, post-RIE surface exposure, bakeout and packaging as detector-process variables.
10. A measured system bandwidth is not detector bandwidth until external transfer functions are de-embedded.
11. Repository scientific specifications do not replace institution-specific Hg/Cd/Br2/HBr/H2/CH4/high-temperature/vacuum/cryogenic EH&S authorization.

## Current checkpoint — READ THIS FIRST

Latest recovery checkpoint:

`research/2026-08-15_checkpoint_after_source_recovery_round8.md`

Current source/gap overrides:

- `docs/SOURCE_LEDGER_ADDENDUM_ROUND8.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND8.md`
- round-7 addenda for passivation/blocking-contact function;
- round-6 addenda for RIE reactor/LBIC/multicarrier state;
- earlier addenda for lithography, metallization, measurement-chain and passivation history.

## Current controlled module set

Important modules/addenda include:

- P01 wet mesa + P01A primary experimental addendum
- P02 anodic oxide + P02A/P02B lineage + P02C sidewall-passivation qualification
- P03 x≈0.30 LPE + P03A lineage + P03B thickness/supercooling + **P03C source synthesis/homogenization + P03D melt inventory/depletion**
- P04 Hg anneal + P04A state-mapping DOE
- P05 Hall/VdP metrology
- P06 FTIR composition/thickness mapping
- P07 CdZnTe qualification + P07A surface prep + **P07B face/miscut selection**
- P08 RIE blocking contact + P08A through P08G
- P09 Cr/Au/TLM + P09A deposition transfer DOE
- P10 DC bias/self-heating
- P11 absolute radiometry
- P12 noise/PSD/NEP/D* + P12A preamp lineage + P12B analyzer/readout qualification
- P13 temporal response + P13A UWA transient-decay lineage
- P14 lithography/CD + P14A chlorobenzene lift-off lineage
- P15 cryogenic package qualification
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
- reported converted density `~2.0×10^15 cm^-3`, explicitly averaged over converted thickness
- mobility `~3.3×10^4 cm²/V·s`.

P08A: secondary same-lineage evidence supports `CH4:H2=1:5`; conditional 64-sccm split = 10.6667/53.3333 sccm. Not direct historical MFC closure.

P08B: if historical averaged density is applied over `d_conv≈8 µm`, conditional `N_s≈1.6×10^12 cm^-2`. Use sheet/multicarrier state + independently measured depth for transfer.

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
- Figures 3/5/6/7 use the same device
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

## Upstream LPE state — round 8

### Historical Honeywell composition is strong; source preparation is not

Best explicit tie line:

- `xL=.082`
- `yL=.810`
- `TL=507 °C`
- historical `xS=.29`
- `xS/xL=3.54`.

Derived source mass fractions:

- Hg `.249738`
- Cd `.012502`
- Te `.737760`.

The Honeywell patent treats this Te-rich growth solution as an **already prepared charge**. It does not state whether the charge was made from elements, binaries, a ternary ingot, or in situ. Source synthesis is historically `OPEN`.

### P03C — source synthesis/homogenization

Local release is by measured outcome:

`{mass closure, actual source composition, homogenization/thermal history, liquidus/growth behavior, P06 x/thickness, P05 mobility, P13 lifetime/device proxy, source conditioning/reuse}`.

Radhakrishnan 2003 is a different x≈.20 branch and gives a candidate method only: 6N elements, evacuated quartz, 700 °C/8 h, source ground/mixed, ~4.8 g/run, 3 g HgTe. Never combine those masses with the Honeywell x=.29 composition as historical data.

An independent 1988 in-situ Hg-vapor/Te-solution preparation route is a separate process family.

### P03D — melt inventory/depletion

Full Honeywell patent describes tapered through-wells but gives **no well diameter/depth/volume, melt depth or charge mass**. Do not infer them from drawings.

Primary 1990 finite-liquid modeling shows:

- growth rate falls after a characteristic time related to liquid thickness;
- Hg loss drives the layer Cd-richer;
- outcome depends on liquid dimensions and Hg-loss flux.

Therefore total melt mass is not released independently of geometry/time.

Local response:

`d_layer = f(t_growth, ΔT, thermal trajectory, liquid inventory/depth, source-use index, Hg-loss state)`.

Track x/thickness/morphology versus source-use index and release a depletion limit from actual drift.

Independent Suh et al. 1992 x=.2/.3/.7 slider work shows a graphite element between solution and HgTe wells can materially stabilize Hg loss/solution composition. Use as composition-matched evidence that Hg-loss geometry matters; do not transplant the hardware into Honeywell without a separate process branch.

### P07B — face/miscut

Exact RP-01/Honeywell polarity/miscut remains `OPEN`.

Independent composition-matched Te-rich slider work on Hg0.7Cd0.3Te used `(111)Cd` CdTe and found:

- 1° miscut -> terrace fronts tied to miscut direction;
- terrace width decreases and height increases with larger miscut;
- above ~2° terraces begin becoming wave-like.

This supports a local low-degree-miscut DOE around the `{111}` family, but **does not prove RP-01 used (111)Cd/A** and uses CdTe rather than CdZnTe.

Select locally using:

`Y_face={morphology, thickness uniformity, x uniformity, twin/defect metric, mobility, lifetime, usable area}`.

Independent x=.30 work also shows morphology evolves with growth time, so P07B and P03B must be interpreted jointly.

## RIE / blocking-contact state — rounds 6–7

Do not conflate p-type conversion studies with RP-01 n-type blocking contact.

- 1997 vacancy p-type x≈.31: 410 mTorr, CH4/H2, 0.4 W/cm², ~0.2-µm physical etch vs ~1.5-µm electrical conversion.
- 1998 As p-type x≈.29: UWA institutional record gives 340 mTorr, 0.4 W/cm²; secondary 390-mTorr value flagged as discrepancy.
- RP-01 n-type x≈.30: 100 mTorr / 64 sccm / 50 W / 60 s; cited ~8-µm prior n+ depth remains process-unclosed.

The algebraic inference `50 W / 0.4 W cm^-2 = 125 cm²` is rejected because identical reactor/electrode geometry is unproven.

P08D local equivalence requires gas split, RF frequency, electrode geometry, self-bias/ion-energy proxy, sample T, chamber history, oxide-clear time, physical recession, multicarrier transport, conversion depth/lateral spread and TLM.

P08E: RIE-converted HgCdTe can contain a damaged surface electron sheet + deeper high-mobility converted region + residual holes. One uniform n+ slab is not the default model.

P08F/P08G: blocking-contact release requires detector-level sweepout suppression without unacceptable noise/bandwidth penalty. `rho_c` is not `S_c`. Historical predecessor accumulation/heterojunction contacts are physics benchmarks, not RP-01 recipes.

## Passivation/frontside state

P01 near-composition x=.28 wet-etch source: nominal `2% Br2 in 3:1 EG:HBr`, ~2.78 µm/min at 21 °C, anisotropy ~.63, best RMS ~2 nm. Full primary text still does not define Br2 percentage basis; genuine source omission.

P02 exact UWA anodization traveler remains open. Direct TI-family candidate: 0.1 M KOH / 90% EG + 10% DI, ~0.3 mA/cm², ~15 V, ~2 min, ~800 Å. x≈.30 Janousek/Carscallen lineage supports dissolution–precipitation physics and strong dependence on surface state/mass transport/pH.

P02C: same-UWA work shows sidewall passivation can materially affect photoconductor responsivity. Because RP-01 anodizes after mesa, planar 80-nm oxide thickness alone is not a complete passivation gate; qualify mesa perimeter/sidewalls electrically or physically.

P09 historical Cr/Au stack 30/270 nm is direct; vacuum/rates/RIE-to-metal delay remain open. P09A locally qualifies them against 80-K TLM, cryogenic stability and noise.

P14 chlorobenzene mechanism is consistent with positive diazo/novolak undercut lift-off, but exact RP-01 resist/developer remain open.

## Measurement state

P12A: later UWA work cites `J. F. Siliquini, Ph.D. thesis, University of Western Australia, 1995` for a custom bias-capable low-noise voltage preamplifier. Thesis remains an actionable archival target. P12B closes local gain/noise/PSD/window/ENBW/Johnson-noise calibration independent of missing historical circuit.

P13: same-UWA x≈.30 work near 77 K deliberately uses low bias to avoid sweepout into high-recombination contacts. Bulk-lifetime interpretation requires low-field/bias-independence plus external transfer de-embedding.

## Highest-value next work

The largest remaining upstream uncertainties are now bounded rather than blank. Next priorities:

1. define/qualify the **x=.29 tie-line equilibration criterion and furnace thermal-uniformity/temperature-uncertainty budget**;
2. tighten **final CdZnTe surface preparation** for x≈.30 Te-rich slider growth;
3. improve **Hg anneal pHg/time/cooldown state mapping** toward the RP-01 low-density n state;
4. build statistical release/capability criteria linking the P03/P04/P05/P06 material chain;
5. pursue old UWA/Honeywell archival sources only when a genuinely new provider/document route appears.

Do not replace unresolved historical values with generic semiconductor practice.
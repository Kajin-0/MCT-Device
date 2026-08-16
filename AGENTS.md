# AGENTS.md — MCT-Device front-door continuity record

## Mission

Build a source-traceable, end-to-end HgCdTe photodetector fabrication and characterization manual that a competent researcher can reproduce without undocumented tribal knowledge.

Canonical first process: **RP-01**, Smith et al., *Semiconductor Science and Technology* 16, 455–462 (2001), DOI `10.1088/0268-1242/16/6/306`.

There is **no end-to-end `REPRODUCIBLE-RELEASE` yet**. The repo contains a controlled qualification/transfer architecture from CdZnTe substrate through LPE, Hg anneal, frontside processing, packaging, radiometry, noise and temporal characterization.

## Non-negotiable rules

1. Never invent a missing number. Use `OPEN`, `CAL`, `QUAL`, `PARTIAL`, `CANDIDATE-P`, or explicit derivation.
2. Never splice incompatible HgCdTe process families and call the result a published recipe.
3. Separate direct publication, derived physics, apparatus calibration and local qualification.
4. Every critical step needs outcome metrology and a pass/fail gate.
5. Preserve negative searches, rejected inferences, corrections and source conflicts.
6. Keep Hall quantities, optical-edge quantities, physical etch depth, electrical conversion depth, sheet density and measured geometry distinct.
7. Use measured fabricated geometry for field/area/D* normalization.
8. Treat passivation, post-RIE surface exposure, bakeout and packaging as detector-process variables.
9. A measured system bandwidth is not detector bandwidth until external transfer functions are de-embedded.
10. Repository scientific specifications do not replace institution-specific Hg/Cd/Br2/HBr/H2/CH4/high-temperature/vacuum/cryogenic EH&S authorization.

## Current checkpoint — READ THIS FIRST

Latest recovery checkpoint:

`research/2026-08-15_checkpoint_after_source_recovery_round6.md`

Prior recovery checkpoints exist through rounds 1–5 and `checkpoint_through_P16.md`. Read them only when detailed historical reasoning is needed.

Current source/gap overrides:

- `docs/SOURCE_LEDGER_ADDENDUM_ROUND6.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND6.md`
- prior round-3/4/5 addenda remain relevant for non-RIE branches.

## Current controlled module set

Important modules/addenda:

- P01 wet mesa + P01A primary experimental addendum
- P02 anodic oxide + P02A/P02B lineage addenda
- P03 x≈0.30 LPE + P03A lineage + P03B thickness/supercooling calibration
- P04 Hg anneal + P04A state-mapping DOE
- P05 Hall/VdP metrology
- P06 FTIR composition/thickness mapping
- P07 CdZnTe qualification + P07A surface prep
- P08 RIE blocking contact + **P08A/P08B/P08C/P08D/P08E**
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
- supplier measurement temperature for n/µ is not stated.

### Contact-window RIE

- Plasma Technology parallel-plate reactor
- printed `CH4/5H2`
- total `64 sccm`
- `100 mTorr`
- `50 W`
- `60 s`
- converted density ~`2.0×10^15 cm^-3`, explicitly averaged over converted thickness
- mobility ~`3.3×10^4 cm²/V·s`.

P08A: same-lineage secondary evidence supports `CH4:H2=1:5`; conditional 64-sccm split is 10.6667/53.3333 sccm. This is **not** direct historical MFC closure.

P08B: volume density depends on conversion depth. If `d_conv≈8 µm`, conditional `N_s≈1.6×10^12 cm^-2`. Report sheet/multicarrier state first.

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

## Critical RIE state — round 6

### P08C — source separation

Do not conflate the following UWA experiments:

1. **1997 vacancy-doped p-type x≈0.31**: 410 mTorr, CH4/H2, 0.4 W/cm², ~0.2-µm physical etch, ~1.5-µm electrical conversion. Direct proof `d_conv != d_etch`.
2. **1998 arsenic-doped p-type x≈0.29**: UWA institutional record gives **340 mTorr**, CH4/H2, 0.4 W/cm². Secondary reposts giving 390 mTorr are a source discrepancy; use 340 mTorr pending publisher audit.
3. **RP-01 n-type x≈0.30**: 100 mTorr / 64 sccm / 50 W / 60 s. The cited ~8-µm n+ depth remains a prior same-lab result under similar conditions; exact process condition is still unrecovered.

Musca et al. 1999, DOI `10.1007/s11664-999-0042-x`, is the formal LBIC junction-depth method source. Depth extraction depends on doping, wavelength, illumination direction and test geometry; store raw maps/model inputs.

### P08D — reactor equivalence

The tempting inference `50 W / 0.4 W cm^-2 = 125 cm²` (equivalent circular diameter ~12.6 cm) is **rejected/unreleased** because identical reactor/electrode geometry has not been proven.

A local reactor is not equivalent merely because it matches `64 sccm / 100 mTorr / 50 W / 60 s`.

Qualify/record:

`{gas split, RF frequency, electrode area/spacing, sample position/loading, forward/reflected power, self-bias/ion-energy proxy, sample T, chamber history, t_clear, d_etch, transport state, d_conv, L_conv, rho_c}`.

### P08E — multicarrier transport

Same-UWA differential-Hall/QMSA work demonstrates RIE-converted HgCdTe can contain:

- a damaged moderate-mobility surface electron sheet
- a deeper high-mobility converted n region
- residual holes where conversion is incomplete.

For x=0.30 p-type conversion examples, surface sheet densities ~`9×10^12–1×10^13 cm^-2` and deeper electron mobilities ~`4–6×10^4 cm²/Vs` were reported. These are **not RP-01 targets**; they prove a one-uniform-layer Hall model is not a safe default.

Use one-carrier reduction only after B-dependent Hall/MR data support it.

## Other major current branch states

### P01 wet mesa

Near-composition x=.28 primary source selects nominal `2% Br2 in 3:1 EG:HBr`, ~2.78 µm/min at 21 °C, anisotropy ~0.63, best RMS ~2 nm. Full primary text still does not define the Br2 percentage basis; genuine source omission. Fixed time alone is not a release method.

### P02 anodic oxide

Exact UWA traveler remains open. Direct TI-family candidate: 0.1 M KOH / 90% EG + 10% DI water, constant current ~0.3 mA/cm², ~15-V endpoint, ~2 min, ~800 Å. x≈.30 Janousek/Carscallen primary lineage supports dissolution–precipitation physics and sensitivity to mass transport/pH/surface state.

### P03 LPE

Best explicit Honeywell tie line: `xL=.082`, `yL=.810`, `TL=507 °C` → `xS=.29`. Derived mass fractions Hg .249738, Cd .012502, Te .737760. Same lineage supports covered graphite slider, auxiliary Hg source, N2 purge, H2, above-liquidus equilibration then growth below liquidus. ~30-min example is not tied to xS=.29 + 9.5 µm. P03B recovers local time/supercooling/thickness response surface.

### P04 Hg anneal

250–300 °C composition-matched branch can produce n-type material without the composition shift seen near 400 °C. Exact historical dwell/pHg/cooldown remains open. P04A maps T/time/Hg chemical potential to final Hall + FTIR state.

### P09 Cr/Au

Historical 30/270-nm stack is direct; historical vacuum/rates/RIE-to-metal delay remain open. P09A locally qualifies deposition environment/rates/thermal load/delay against 80-K TLM, cryogenic stability and detector noise.

### P12 measurement chain

Later UWA work cites `J. F. Siliquini, Ph.D. thesis, University of Western Australia, 1995` for a custom bias-capable low-noise voltage preamplifier. The thesis remains an actionable archival acquisition target; UWA stores many pre-2017 PhD theses in print/storage and can provide scans. P12B defines local gain/noise/PSD/window/ENBW/Johnson-noise calibration independent of the missing historical circuit.

### P13 temporal response

Same-UWA x≈.30 work near 77 K deliberately used low bias to avoid sweepout into high-recombination contacts. Bulk lifetime interpretation therefore requires low-field/bias-independence plus external transfer de-embedding.

## Current highest-value archival targets

1. Full Musca et al. 1998 JEM n-type LBIC paper: exact condition tied to ~8 µm.
2. Full Smith et al. 1999 JVST-A experimental section: reactor identity/geometry.
3. Full Smith et al. 2000 SIMC-XI in-situ processing paper: reactor-to-metal sequence.
4. Siliquini 1995 UWA PhD thesis: preamp schematic and possible fabrication/process details.
5. Exact RP-01 resist/exposure/developer and UWA anodization traveler.

Do not repeat metadata-only searches unless a genuinely new archive/provider appears. Where historical closure has hit a practical ceiling, use the explicit Pxx local qualification method rather than generic cleanroom convention.
# AGENTS.md — MCT-Device front-door continuity record

## Mission

Build a source-traceable, end-to-end HgCdTe photodetector fabrication and characterization manual that a competent researcher can reproduce without undocumented tribal knowledge.

Canonical first process: **RP-01**, Smith et al., *Semiconductor Science and Technology* 16, 455–462 (2001), DOI `10.1088/0268-1242/16/6/306`.

There is **no end-to-end `REPRODUCIBLE-RELEASE` yet**. The repository currently contains a controlled qualification/transfer architecture from CdZnTe substrate through LPE, Hg anneal, device fabrication, packaging, responsivity, noise and temporal characterization.

## Non-negotiable rules

1. Never invent a missing process number. Use `OPEN`, `CAL`, `QUAL`, `PARTIAL`, `CANDIDATE-P`, or an explicit derivation.
2. Never splice incompatible HgCdTe process families and call the result a published recipe.
3. Separate direct publication, derived physics, apparatus calibration and local qualification.
4. Every critical step needs outcome metrology and a pass/fail gate.
5. Preserve negative source searches, rejected branches, corrections and unresolved ambiguities.
6. Keep Hall quantities, optical-edge quantities, physical etch depth, electrical conversion depth and measured device geometry distinct.
7. Use measured fabricated geometry for field, active area and D* normalization.
8. Treat passivation, post-RIE surface exposure, bakeout and packaging as detector-process variables when they can alter detector behavior.
9. A measured system bandwidth is not detector bandwidth until external transfer functions are de-embedded.
10. Repository scientific specifications do not replace institution-specific Hg/Cd/Br2/HBr/H2/CH4/high-temperature/vacuum/cryogenic EH&S authorization.

## Current checkpoint — READ THIS FIRST

Latest recovery checkpoint:

`research/2026-08-15_checkpoint_after_source_recovery_round5.md`

Recovery history, in order:

1. `research/2026-08-15_checkpoint_through_P16.md`
2. `research/2026-08-15_checkpoint_after_source_recovery_round1.md`
3. `research/2026-08-15_checkpoint_after_source_recovery_round2.md`
4. `research/2026-08-15_checkpoint_after_source_recovery_round3.md`
5. `research/2026-08-15_checkpoint_after_source_recovery_round4.md`
6. `research/2026-08-15_checkpoint_after_source_recovery_round5.md` **CURRENT**

Current source/gap overrides:

- `docs/SOURCE_LEDGER_ADDENDUM_ROUND3.md`
- `docs/SOURCE_LEDGER_ADDENDUM_ROUND4.md`
- `docs/SOURCE_LEDGER_ADDENDUM_ROUND5.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND3.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND4.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND5.md`

Read the older monolithic source ledger/gap matrix for broader history, but use newer addenda where they override stale entries.

## Important current module set

Key controlled modules/addenda include:

- P01 wet mesa + `P01A_SRIVASTAV_PRIMARY_EXPERIMENTAL_ADDENDUM.md`
- P02 anodic oxide + P02A + `P02B_X030_ANODIZATION_LINEAGE_ADDENDUM.md`
- P03 x≈0.30 LPE + P03A + `P03B_X030_GROWTH_TIME_SUPERCOOLING_CALIBRATION.md`
- P04 Hg anneal + `P04A_X030_HG_ANNEAL_STATE_MAPPING_DOE.md`
- P05 Hall/van-der-Pauw material metrology
- P06 FTIR composition/thickness mapping
- P07 CdZnTe qualification + P07A surface-prep addendum
- P08 RIE blocking contact + P08A gas-ratio provenance + P08B Hall/depth coupling
- P09 Cr/Au/TLM + `P09A_CR_AU_DEPOSITION_TRANSFER_DOE.md`
- P10 DC bias/self-heating
- P11 absolute spectral responsivity/radiometry
- P12 noise/PSD/NEP/D* + `P12A_UWA_PREAMPLIFIER_LINEAGE_ADDENDUM.md` + `P12B_NOISE_READOUT_ANALYZER_TRANSFER_QUALIFICATION.md`
- P13 temporal/frequency response + P13A UWA transient-decay lineage
- P14 lithography/CD + `P14A_CHLOROBENZENE_LIFTOFF_LINEAGE_ADDENDUM.md`
- P15 cryogenic package qualification
- P16 master end-to-end traveler + blank traveler form.

## Direct RP-01 anchors — do not drift

Starting material:

- LPE n-HgCdTe on insulating CdZnTe;
- nominal `x≈0.30`;
- supplier `n=9.8×10^14 cm^-3`;
- supplier `µ=4.0×10^4 cm²/V·s`;
- thickness `9.5 µm`;
- supplier n/µ measurement temperature is not stated.

Contact-window RIE:

- Plasma Technology parallel-plate reactor;
- printed `CH4/5H2`;
- total `64 sccm`;
- `100 mTorr`;
- `50 W`;
- `60 s`;
- converted density ~`2.0×10^15 cm^-3`, explicitly averaged over converted thickness;
- mobility ~`3.3×10^4 cm²/V·s`.

P08A: same-lineage secondary evidence supports `CH4:H2=1:5`; conditional derived split is 10.6667/53.3333 sccm. This is not yet primary MFC closure.

P08B: volume density is coupled to conversion depth. If `d_conv≈8 µm`, conditional sheet-density scale is `N_s≈1.6×10^12 cm^-2`. Qualify `{R_sheet/N_s, µ_H or multicarrier state, d_conv, L_conv, d_etch, rho_c}`, not volume density alone. Exact Musca-1998 conditions tied to ~8 µm remain open.

Mask-2/passivation/metal:

- resist ~`4–5 µm`;
- prebake `80 °C / 30 min`;
- chlorobenzene `30 min`;
- pattern/develop/water rinse;
- anodic oxide `800 Å`;
- Cr `300 Å`;
- Au `2700 Å`.

Geometry/TLM:

- nine 300×300-µm contacts;
- adjacent gaps 50–400 µm in 50-µm increments;
- 80-K `rho_c≈9×10^-4 Ω·cm²`;
- Figures 3/5/6/7 use the same device;
- exact selected contact pair/gap remains legitimately `OPEN`; see `research/2026-08-15_rp01_active_gap_inference_audit.md`.

Detector benchmark:

- 80 K;
- stated 60° FOV;
- spectral response at 1 kHz;
- representative noise field 10 V/cm;
- low-noise preamp + HP35665A;
- 1/f knee ~3 kHz;
- g-r plateau ~24.5 nV/√Hz;
- cutoff ~4.4 µm;
- BLIP D* ~`2.0×10^11 cm Hz^1/2 W^-1` at 4 µm;
- QE ~70%.

Do not assume 24.5 nV/√Hz is the historical 1-kHz noise used in the spectral D* curve.

## Major scientific state

### P01 wet mesa

Near-composition x=.28 primary source selects nominal `2% Br2 in 3:1 EG:HBr`, ~2.78 µm/min at 21 °C, anisotropy ~0.63, best RMS ~2 nm. Full primary text was audited and still does **not** define the Br2 percentage basis. This is a genuine source omission. P01A records sample preparation, test geometry, Dektak/phase-contrast metrology and Br2 evaporation drift. A 9.5-µm fixed-time estimate spans roughly 2.71–4.62 min using the source rate variation, demonstrating timed etch alone is not a release method.

### P02 anodic oxide

Exact UWA local traveler remains open. Direct TI-family candidate: 0.1 M KOH / 90% EG + 10% DI water, constant current ~0.3 mA/cm², ~15-V endpoint, ~2 min, ~800 Å.

Composition-matched x≈.30 Janousek/Carscallen primary lineage establishes dissolution–precipitation initial oxide growth and sensitivity to stirring/mass transport/pH. P02B therefore controls voltage-time induction, current density, integrated charge/area, agitation and starting surface state. Do not transplant the old bulk x=.30 experiment's ~20-µm pre-etch onto a 9.5-µm RP-01 film.

### P03 LPE

Best explicit Honeywell tie line: `xL=.082`, `yL=.810`, `TL=507 °C` → `xS=.29`. Derived charge mass fractions Hg .249738, Cd .012502, Te .737760. Same lineage supports covered graphite slider, auxiliary Hg source, N2 purge, H2, above-liquidus equilibration then below-liquidus growth. A ~30-min example is not tied to xS=.29 + 9.5 µm.

P03B recovers the local schedule by mapping contact time × supercooling × thermal trajectory while measuring thickness and x simultaneously. Derive timing/T tolerances from measured sensitivities.

### P04 Hg anneal

Composition-matched branch supports 250–300 °C Hg-rich conversion to n-type without the interface composition change reported near 400 °C. Exact historical dwell/pHg/cooldown remains open. P04A maps time/T/Hg chemical potential/cooldown into final Hall + optical state. ~250 °C/1 h is a screening center only.

### P09 Cr/Au

Historical 30/270-nm stack is direct. Historical vacuum/rates/RIE-to-metal delay remain open after repeated source searching. P09A qualifies local deposition pressure, rates, thermal load and delay against 80-K TLM, cryogenic stability and detector noise rather than inventing generic PVD numbers.

### P14 lift-off

Chlorobenzene mechanism is historically closed as a single-layer positive diazo/novolak undercut/overhang process. Exact RP-01 resist/developer remain open. Do not assign AZ1350J/AZ4000/Shipley products from unrelated examples. P14A requires profile metrology before/after RIE and after metal deposition/lift-off.

### P13 lifetime

Same-UWA 1998 thesis on n-type x≈.30 HgCdTe near 77 K explicitly kept bias small to avoid sweeping carriers into high-recombination contacts. Bulk-lifetime interpretation requires a low-field/bias-independence gate and external transfer de-embedding.

## Round-5 measurement-chain result — current active frontier

RP-01 only says `low-noise pre-amplifier + HP35665A` for Figure 5.

A later UWA photoconductor paper directly states that its detector output was connected to a **custom low-noise voltage preamplifier specifically designed to permit detector bias**, and cites:

`J. F. Siliquini, Ph.D. thesis, University of Western Australia, 1995`

for that preamp.

The thesis is now an **actionable archival target**:

- author John Frank Siliquini;
- UWA PhD, 1995;
- UWA currently states most pre-2017 UWA PhD theses are held in print/storage and can be found/requested through OneSearch/storage services;
- external researchers/libraries can request scanned thesis copies.

Exact thesis title/call number is still not publicly recovered.

P12A records the lineage/acquisition target. P12B defines the local recovery method:

- calibrated `G(f)`;
- source-impedance-dependent preamp/electronics noise;
- Johnson-noise end-to-end PSD check;
- bias-network loading;
- exact FFT/window/ENBW/averaging record;
- PSD-level electronics-floor subtraction;
- stationarity/microphonic/burst checks;
- direct `e_n(1 kHz)` for 1-kHz D*.

Official Keysight documentation confirms the 35665A supports PSD, linear spectrum, cross-spectrum and frequency response with up to 102.4-kHz single-channel bandwidth. Historical Figure-5 settings remain open.

## Highest-impact remaining blockers

1. Acquire Siliquini 1995 UWA thesis / preamp schematic and any analyzer settings.
2. Primary CH4:H2 MFC split and exact Musca-1998 ~8-µm process conditions.
3. Exact RP-01 resist product/exposure/developer.
4. Exact UWA anodization traveler/rinse/dry.
5. P01 Br2 percentage basis or explicitly new qualified local formulation.
6. Exact x≈.30 source synthesis/homogenization.
7. Final CdZnTe polarity/miscut/surface preparation.
8. Original mask/device log identifying the historical Figures 3/5/6/7 contact pair.
9. Historical package/interconnect construction.

P03/P04/P09/P12/P14 now have explicit local recovery methods. Do not restart generic searches for already-documented archival dead ends unless a genuinely new source route appears.

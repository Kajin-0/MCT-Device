# AGENTS.md — MCT-Device continuity record

## Mission

Build a source-traceable, end-to-end HgCdTe photodetector fabrication and characterization manual that a competent researcher can reproduce without undocumented tribal knowledge.

Canonical first process: **RP-01**, Smith et al., *Semiconductor Science and Technology* 16, 455–462 (2001), DOI `10.1088/0268-1242/16/6/306`.

This is the front-door handoff. Detailed history is in the checkpoints, source ledgers, gap-matrix addenda and Pxx procedure files.

## Non-negotiable rules

1. Never invent a missing number. Use `OPEN`, `CAL`, `QUAL`, `PARTIAL`, `CANDIDATE-P`, or explicit derivation.
2. Never splice incompatible HgCdTe process families and call the result a published recipe.
3. Separate direct publication, derived physics, apparatus calibration and local qualification.
4. Every critical step needs outcome metrology and a pass/fail gate.
5. Preserve negative searches, rejected branches, corrections and unresolved ambiguities.
6. Keep Hall quantities, optical-edge quantities, physical etch depth, electrical conversion depth and measured geometry rigorously distinct.
7. Use measured fabricated geometry for field/area/D* normalization.
8. Treat packaging/bakeout and passivation/surface exposure as device-process variables when they affect detector behavior.
9. A measured system bandwidth is not detector bandwidth until external transfer functions are de-embedded.
10. Repository scientific specifications do not replace institution-specific Hg/Cd/Br2/HBr/H2/CH4/high-temperature/vacuum/cryogenic EH&S authorization.

## Current state

A controlled qualification architecture exists from CdZnTe substrate through LPE, Hg anneal, mesa, native oxide, contact-window RIE, Cr/Au, packaging and detector characterization. There is **no end-to-end `REPRODUCIBLE-RELEASE` yet**.

Important current/addendum modules include:

- P01 + `P01A_SRIVASTAV_PRIMARY_EXPERIMENTAL_ADDENDUM.md`
- P02 + P02A + `P02B_X030_ANODIZATION_LINEAGE_ADDENDUM.md`
- P03 + P03A + `P03B_X030_GROWTH_TIME_SUPERCOOLING_CALIBRATION.md`
- P04 + `P04A_X030_HG_ANNEAL_STATE_MAPPING_DOE.md`
- P05 Hall/VdP material metrology
- P06 FTIR composition/thickness mapping
- P07 + P07A CdZnTe substrate/surface preparation
- P08 + P08A + P08B RIE contact qualification
- P09 + `P09A_CR_AU_DEPOSITION_TRANSFER_DOE.md`
- P10 DC bias/self-heating
- P11 absolute spectral responsivity/radiometry
- P12 noise/PSD/NEP/D*
- P13 + P13A temporal response/lifetime
- P14 + `P14A_CHLOROBENZENE_LIFTOFF_LINEAGE_ADDENDUM.md`
- P15 cryogenic package qualification
- P16 master end-to-end traveler + blank traveler form.

## Direct RP-01 anchors that must not drift

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
- total flow `64 sccm`;
- `100 mTorr`;
- `50 W`;
- `60 s`;
- reported converted density `~2.0×10^15 cm^-3`, explicitly averaged over converted thickness;
- reported mobility `~3.3×10^4 cm²/V·s`.

P08A: same-lineage secondary review supports `CH4:H2=1:5`; if applied to RP-01's 64 sccm total, conditional derived flows are CH4 `10.6667 sccm` and H2 `53.3333 sccm`. Primary MFC confirmation remains open.

P08B: volume density is depth-coupled. If `d_conv≈8 µm`, conditional `N_s≈1.6×10^12 cm^-2`. Qualify `{R_sheet/N_s, µ_H or multicarrier state, d_conv, L_conv, d_etch, rho_c}`, not n_vol alone. Exact Musca-1998 conditions tied to ~8 µm remain unresolved.

Mask-2 / metal:
- resist `~4–5 µm`;
- prebake `80 °C / 30 min`;
- chlorobenzene `30 min`;
- pattern/develop/water rinse;
- native oxide `800 Å`;
- Cr `300 Å`;
- Au `2700 Å`.

Geometry/TLM:
- nine 300×300-µm contacts;
- adjacent gaps 50–400 µm in 50-µm increments;
- 80-K `rho_c≈9×10^-4 Ω·cm²`;
- Figures 3/5/6/7 use the same typical device, exact contact pair unknown.

Detector benchmark:
- 80 K;
- stated 60° FOV;
- responsivity at 1 kHz;
- representative noise field 10 V/cm;
- HP35665A + low-noise preamp;
- 1/f knee ~3 kHz;
- g-r plateau ~24.5 nV/√Hz;
- detector-response cutoff ~4.4 µm;
- BLIP D* ~`2.0×10^11 cm Hz^1/2/W` at 4 µm;
- QE ~70%.

## Major current conclusions

### P01 wet mesa

Same-UWA evidence supports wet mesa rather than blanket dry RIE. Near-composition x=.28 primary source selects nominal `2% Br2 in 3:1 EG:HBr`, ~2.78 µm/min at 21 °C, anisotropy ~0.63, best RMS ~2 nm. Full primary text was audited and still does **not** define the Br2 percentage basis. P01A adds sample-prep/test-geometry/metrology details. A 9.5-µm timed-etch estimate spans roughly 2.71–4.62 min using the source ±26% rate variation, demonstrating fixed-time etch is not a release method.

### P02 native oxide

Exact UWA traveler remains open. Direct TI-family candidate is `0.1 M KOH / 90% EG +10% DI`, constant current ~0.3 mA/cm², ~15-V endpoint, ~2 min, ~800 Å.

Composition-matched x≈.30 Janousek/Carscallen primary lineage establishes dissolution–precipitation initial growth and sensitivity to stirring/mass transport/pH. P02B therefore controls voltage-time induction, current density, integrated charge/area, agitation and surface history. Do not transplant the old mechanistic study's ~20-µm pre-etch onto a 9.5-µm RP-01 epilayer.

### P03 LPE

Best Honeywell tie line: `xL=.082`, `yL=.810`, `TL=507 °C` → `xS=.29`; derived mass fractions Hg .249738, Cd .012502, Te .737760. Same lineage supports covered graphite slider, Hg source, N2 purge, H2, above-liquidus equilibration then below-liquidus growth. A ~30-min example exists but is not tied to xS=.29 + 9.5 µm.

P03B now recovers the local schedule by mapping `contact time × supercooling × thermal trajectory` while measuring thickness and x simultaneously. Derive timing/temperature tolerances from measured sensitivities, not arbitrary numbers.

### P04 Hg anneal

Composition-matched branch supports 250–300 °C Hg-rich conversion to n-type without the interface composition change reported near 400 °C. Exact historical dwell/pHg/cooldown remains open. P04A maps time, temperature, Hg chemical potential and cooldown into final `{carrier sign,n_H,µ_H,optical x,thickness,morphology}`. ~250 °C/1 h is a screening center only.

### P09 Cr/Au

Historical 30/270-nm stack is direct. Historical vacuum/rates/delay remain open. P09A qualifies local deposition pressure, rates, thermal load and RIE-to-metal delay against 80-K TLM, cryogenic stability and detector noise rather than inserting generic PVD numbers.

### P14 lift-off

Chlorobenzene mechanism is historically closed as a single-layer positive diazo/novolak undercut/overhang process. Exact RP-01 resist/developer remain open; do not assign AZ1350J/AZ4000/Shipley products from unrelated examples. P14A requires profile metrology before/after RIE and after metal deposition. Resist:metal thickness ratio is ~13:1–17:1, a consistency metric only.

### P13 lifetime

Same-UWA 1998 thesis on n-type x≈.30 HgCdTe near 77 K explicitly kept bias small to avoid sweeping carriers into high-recombination contacts. Bulk-lifetime interpretation requires low-field/bias-independence plus external de-embedding.

## Current recovery checkpoints — read in order

1. `research/2026-08-15_checkpoint_through_P16.md`
2. `research/2026-08-15_checkpoint_after_source_recovery_round1.md`
3. `research/2026-08-15_checkpoint_after_source_recovery_round2.md`
4. `research/2026-08-15_checkpoint_after_source_recovery_round3.md`
5. `research/2026-08-15_checkpoint_after_source_recovery_round4.md` **CURRENT**

Then read:
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND3.md` and `...ROUND4.md`;
- `docs/SOURCE_LEDGER_ADDENDUM_ROUND3.md` and `...ROUND4.md`;
- broader original gap/source ledgers;
- relevant Pxx/PxxA/PxxB procedures.

## Highest-impact remaining blockers

1. P01 Br2 percentage basis or explicitly new local formulation.
2. Exact UWA anodization traveler/rinse/dry.
3. Exact RP-01 resist product/exposure/developer.
4. Primary CH4:H2 MFC split and exact Musca-1998 ~8-µm conditions.
5. Historical RIE reactor geometry/self-bias/sample temperature.
6. Exact x≈.30 source synthesis/homogenization.
7. Final CdZnTe face/miscut/surface prep.
8. Historical low-noise preamp and analyzer RBW/ENBW convention.
9. Exact historical contact pair/gap for Figures 3/5/6/7.
10. Historical package/interconnect.

P03/P04/P09/P14 now have explicit local recovery procedures; do not restart generic archival searches for already-documented dead ends unless a new source route appears.

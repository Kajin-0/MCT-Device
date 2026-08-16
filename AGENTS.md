# AGENTS.md — MCT-Device continuity record

## Mission

Build a source-traceable, end-to-end HgCdTe photodetector fabrication and characterization manual that a competent researcher can reproduce without undocumented tribal knowledge.

Canonical first process: **RP-01**, the n-type MWIR HgCdTe photoconductor in Smith et al., *Semiconductor Science and Technology* 16, 455–462 (2001), DOI `10.1088/0268-1242/16/6/306`.

This file is the **front-door handoff**. Detailed scientific history belongs in the checkpoints, source ledger, gap matrix, procedures and research notes.

## Non-negotiable rules

1. Never invent a missing number. Use `OPEN`, `CAL`, `QUAL`, `PARTIAL`, `CANDIDATE-P`, or an explicit derivation.
2. Never splice values from incompatible HgCdTe process families and call the result a published recipe.
3. Separate direct publication, derived physics, apparatus calibration and local qualification.
4. Every critical step needs outcome metrology and a pass/fail gate.
5. Preserve negative searches, incompatible branches, corrections and unresolved ambiguities.
6. Report Hall quantities as Hall quantities unless Hall-factor/multicarrier assumptions are justified.
7. Keep transmission edge, inferred band gap, inferred alloy composition and detector-response cutoff distinct.
8. Keep oxide clearing, physical etch depth, electrical conversion depth and lateral conversion distinct.
9. Use measured fabricated geometry for field, area and D* normalization.
10. Treat packaging/bakeout as detector process steps when they can alter electrical, noise or optical behavior.
11. A measured system bandwidth is not detector bandwidth until external transfer functions are de-embedded.
12. Repository scientific specifications do not replace local Hg/Cd/Br2/HBr/H2/CH4/high-temperature/vacuum/cryogenic EH&S authorization.

---

# Current controlled module set

Core modules and important addenda now include:

- `P01_WET_MESA_QUALIFICATION.md`
- `P01A_SRIVASTAV_PRIMARY_EXPERIMENTAL_ADDENDUM.md`
- `P02_ANODIC_OXIDE_QUALIFICATION.md`
- `P02A_ANODIC_OXIDE_LINEAGE_ADDENDUM.md`
- `P02B_X030_ANODIZATION_LINEAGE_ADDENDUM.md`
- `P03_LPE_X030_QUALIFICATION.md`
- `P03A_HONEYWELL_LPE_LINEAGE_ADDENDUM.md`
- `P04_HG_ANNEAL_QUALIFICATION.md`
- `P05_HALL_VDP_MATERIAL_METROLOGY.md`
- `P06_FTIR_COMPOSITION_THICKNESS_MAPPING.md`
- `P07_CZT_SUBSTRATE_QUALIFICATION.md`
- `P07A_CZT_PRE_LPE_SURFACE_PREP_ADDENDUM.md`
- `P08_RIE_BLOCKING_CONTACT_QUALIFICATION.md`
- `P08A_RIE_GAS_RATIO_PROVENANCE_ADDENDUM.md`
- `P08B_RIE_HALL_DEPTH_COUPLING_ADDENDUM.md`
- `P09_CR_AU_METALLIZATION_TLM_QUALIFICATION.md`
- `P10_DEVICE_DC_BIAS_SELF_HEATING.md`
- `P11_ABSOLUTE_SPECTRAL_RESPONSIVITY_RADIOMETRY.md`
- `P12_NOISE_PSD_NEP_DETECTIVITY.md`
- P13 temporal/frequency-response module + `P13A_UWA_TRANSIENT_DECAY_LINEAGE_ADDENDUM.md`
- `P14_LITHOGRAPHY_MASK_GEOMETRY_CD_QUALIFICATION.md`
- `P15_DIE_ATTACH_INTERCONNECT_CRYOGENIC_PACKAGE_QUALIFICATION.md`
- `P16_MASTER_END_TO_END_PROCESS_TRAVELER.md`
- P16 blank traveler/form.

There is **no end-to-end `REPRODUCIBLE-RELEASE` yet**. These are controlled qualification/transfer modules.

---

# Direct RP-01 anchors that must not drift

## Starting material

- LPE n-HgCdTe on electrically insulating CdZnTe.
- nominal `x≈0.30`.
- supplier carrier density `9.8×10^14 cm^-3`.
- supplier electron mobility `4.0×10^4 cm²/V·s`.
- active-layer thickness `9.5 µm`.
- supplier measurement temperature for n/µ is not stated.

## Contact-window RIE

- Plasma Technology parallel-plate reactor.
- printed gas notation `CH4/5H2`.
- total flow `64 sccm`.
- pressure `100 mTorr`.
- RF power `50 W`.
- time `60 s`.
- reported converted density `~2.0×10^15 cm^-3`.
- reported mobility `~3.3×10^4 cm²/V·s`.
- Hall/resistivity measurements at 80 K and 300 K with variable field up to 2 T.

### P08A gas-ratio state

A same-lineage HgCdTe RIE review explicitly summarizes the relevant RF parallel-plate branch as `CH4:H2=1:5`.

Evidence grade: **secondary same-lineage**, not direct RP-01 MFC data.

Conditional split from 64 sccm total:

- CH4 `10.6667 sccm`;
- H2 `53.3333 sccm`.

Primary individual-MFC confirmation remains open.

### P08B Hall/depth correction

RP-01 says `2.0×10^15 cm^-3` is **averaged over the RIE-converted thickness**.

Therefore volume density is not independent of `d_conv`.

If `d_conv≈8 µm`, conditional `N_s≈1.6×10^12 cm^-2`; if the full 9.5-µm layer were used, ~`1.9×10^12 cm^-2`.

Qualify RIE using at least:

`{R_sheet/N_s, µ_H or multicarrier state, d_conv, L_conv, d_etch, rho_c}`.

The exact Musca-1998 conditions tied to ~8-µm conversion remain unresolved.

## Mask-2/passivation/metal

- resist ~`4–5 µm`.
- prebake `80 °C / 30 min`.
- chlorobenzene `30 min`.
- then pattern/develop/water rinse.
- native anodic oxide `800 Å = 80 nm`.
- Cr `300 Å = 30 nm`.
- Au `2700 Å = 270 nm`.

## Geometry/TLM

- nine contacts, each `300×300 µm`.
- adjacent gaps `50,100,...,400 µm`.
- same structure supports TLM and photoconductor measurements.
- 80-K `rho_c≈9×10^-4 Ω·cm²`.
- Figures 3/5/6/7 use the same typical device, but the exact contact pair/gap remains unknown.

## Detector benchmark

- `80 K`.
- stated FOV `60°`.
- spectral responsivity at `1 kHz`.
- representative noise field `10 V/cm`.
- HP35665A + low-noise preamp.
- 1/f knee ~`3 kHz`.
- g-r plateau ~`24.5 nV/√Hz`.
- detector-response cutoff ~`4.4 µm`.
- BLIP `D*≈2.0×10^11 cm Hz^1/2/W` at 4 µm.
- QE ~`70%`.

Do not assume the 24.5-nV/√Hz white/g-r value is the exact noise used in the historical 1-kHz D* curve.

---

# Major current scientific decisions

## P01 wet mesa

Retain wet mesa isolation; use RIE only at contacts.

Near-composition primary source x=0.28:

- selected nominal `2% Br2 in 3:1 EG:HBr`;
- ~`2.78 µm/min` at 21 °C;
- ~±26% source rate variation;
- anisotropy ~0.63;
- best RMS ~2 nm.

**Full primary text has now been audited and still does not define the Br2 percentage basis.** This is a genuine source omission.

New P01A direct details include the source sample prep, 50/30-µm trench masks, Dektak vertical metrology, phase-contrast lateral metrology, ~7.5-kcal/mol activation energy and Br2 evaporation as a reproducibility mechanism.

For a 9.5-µm RP-01 film, source mean-rate timing is ~3.42 min, but the source ±26% spread gives ~2.71–4.62 min. Diagnostic only: fixed-time etching is not an adequate release method.

## P02 anodic oxide

Exact UWA local traveler remains open.

Direct executable TI-family candidate:

- `0.1 M KOH`;
- `90% EG / 10% DI water`;
- constant current ~`0.3 mA/cm²`;
- terminal formation voltage ~`15 V`;
- ~`2 min`;
- ~`800 Å` oxide.

### Composition-matched x≈0.30 support — P02B

Primary sources:

- B. K. Janousek & R. C. Carscallen, “The mechanism of (Hg,Cd)Te anodic oxidation,” *J. Appl. Phys.* 53, 1720–1726 (1982).
- B. K. Janousek & R. C. Carscallen, “Hg0.70Cd0.30Te anodic oxidation,” *J. Vac. Sci. Technol.* 21, 442 (1982), DOI `10.1116/1.571674`.

These establish dissolution–precipitation initial oxide formation and sensitivity to mass transport/stirring/pH on composition-matched x≈0.30 HgCdTe.

Talasek's later technical synthesis explicitly attributes an x=0.30 experiment to Janousek/Carscallen using nominal 5% Br2/methanol pre-etch and 0.1 N KOH in 90% EG/10% water. Those detailed values remain **secondary-A attributed to primary**, not directly re-read primary setpoints.

Important P02 controls now include complete voltage-time trace, induction time, current density, integrated charge/area, terminal voltage, bath agitation, surface history and independent oxide thickness.

Do not transplant the old x=0.30 experiment's ~20-µm pre-etch removal onto the 9.5-µm RP-01 epilayer.

## x≈0.30 Te-rich LPE

Best explicit Bowers–Schmit tie line:

- `xL=0.082`;
- `yL=0.810`;
- `TL=507 °C`;
- `xS=0.29`;
- `xS/xL=3.54`.

Derived mass fractions: Hg `0.249738`, Cd `0.012502`, Te `0.737760`.

Same Honeywell lineage supports covered graphite slider, auxiliary Hg source, N2 purge, H2 processing, above-liquidus equilibration then growth below liquidus. An example ~30-min growth exists but is not tied to xS=.29 + 9.5 µm and is not released.

## Temporal response

P13 requires external de-embedding and amplitude+phase validation before assigning detector lifetime.

P13A same-UWA 1998 thesis uses n-type x≈0.30 HgCdTe near 77 K and explicitly keeps bias small to avoid sweeping excess carriers into high-recombination contact regions. A bulk-lifetime interpretation therefore requires a low-field/bias-independence gate.

---

# Current recovery checkpoints — read in order

1. `research/2026-08-15_checkpoint_through_P16.md`
2. `research/2026-08-15_checkpoint_after_source_recovery_round1.md`
3. `research/2026-08-15_checkpoint_after_source_recovery_round2.md`
4. `research/2026-08-15_checkpoint_after_source_recovery_round3.md` **CURRENT**

Then read:

- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND3.md` for current P01/P02/P08/P13 overrides;
- `docs/RP01_GAP_MATRIX.md` for the broader matrix;
- `docs/SOURCE_LEDGER_ADDENDUM_ROUND3.md` plus prior source ledgers;
- relevant Pxx/PxxA/PxxB files;
- branch-specific dated research notes.

---

# Highest-impact remaining blockers

## Frontside chemistry / lithography

1. exact Br2 percentage basis for P01, or explicitly define and qualify a new local formulation;
2. exact UWA RP-01 anodization traveler, especially rinse/dry/cell details;
3. full Janousek/Carscallen experimental section / exact current-density labels if accessible;
4. exact Mask-1/Mask-2 resist, spin, exposure, developer and development time;
5. Cr/Au base pressure/rates, RIE-to-metal delay and lift-off sequence.

## RIE

6. primary confirmation of CH4:H2 ratio / individual MFCs;
7. exact Musca-1998 conditions tied to ~8-µm conversion depth;
8. reactor electrode geometry, RF frequency, self-bias and sample temperature.

## Upstream

9. x≈0.30 charge synthesis/homogenization;
10. selected CdZnTe face/miscut and final surface prep;
11. x≈0.30 LPE thickness-versus-time relation;
12. Hg anneal pHg/time/cooldown that reproduces RP-01 transport state.

## Historical characterization/package

13. exact contact pair/gap used for Figures 3/5/6/7;
14. historical low-noise preamplifier and RBW/ENBW settings;
15. package/interconnect construction.

## Next work rule

Avoid repeating metadata-only searches already documented as dead ends. Prefer primary full texts, patents, proceedings, thesis records and inherited same-lab processes. Where historical closure has reached a practical ceiling, define an explicit local qualification DOE rather than filling the gap with ordinary cleanroom convention.

# AGENTS.md — MCT-Device continuity record

## Mission

Build a source-traceable, end-to-end HgCdTe photodetector fabrication and characterization manual that a competent researcher can reproduce without undocumented tribal knowledge.

First canonical process: **RP-01**, the n-type MWIR HgCdTe photoconductor in Smith et al., *Semiconductor Science and Technology* 16, 455–462 (2001), DOI `10.1088/0268-1242/16/6/306`.

This is the front-door handoff file. For full scientific history, read the checkpoints listed below.

## Non-negotiable rules

1. Never invent a missing number. Use `OPEN`, `CAL`, `QUAL`, `PARTIAL`, `CANDIDATE-P`, or an explicit derivation.
2. Never splice values from incompatible HgCdTe process families and call the result a published recipe.
3. Separate direct publication, derived physics, apparatus calibration, and local qualification.
4. Every process step needs outcome metrology and a pass/fail gate.
5. Preserve negative searches, incompatible branches, corrections, and unresolved ambiguities.
6. Report Hall quantities as Hall quantities unless Hall-factor/multicarrier assumptions are justified.
7. Keep transmission edge, inferred band gap, inferred alloy composition and detector-response cutoff separate.
8. Keep oxide clearing, physical etch depth, electrical conversion depth and lateral conversion separate.
9. Use measured fabricated geometry for field, area and D* normalization.
10. Treat packaging and bakeout as detector process steps when they can alter electrical/noise/optical behavior.
11. A measured system bandwidth is not detector bandwidth until external transfer functions are de-embedded.
12. Repository scientific specifications do not replace local Hg/Cd/Br2/HBr/H2/CH4/high-temperature/vacuum/cryogenic EH&S authorization.

---

# Current process architecture

Controlled qualification modules currently include:

- `P01_WET_MESA_QUALIFICATION.md`
- `P02_ANODIC_OXIDE_QUALIFICATION.md`
- `P02A_ANODIC_OXIDE_LINEAGE_ADDENDUM.md`
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
- `P13_TEMPORAL_FREQUENCY_RESPONSE_LIFETIME.md`
- `P13A_UWA_TRANSIENT_DECAY_LINEAGE_ADDENDUM.md`
- `P14_LITHOGRAPHY_MASK_GEOMETRY_CD_QUALIFICATION.md`
- `P15_DIE_ATTACH_INTERCONNECT_CRYOGENIC_PACKAGE_QUALIFICATION.md`
- `P16_MASTER_END_TO_END_PROCESS_TRAVELER.md`
- `P16A_MASTER_TRAVELER_FORM.md`

There is **no end-to-end `REPRODUCIBLE-RELEASE` yet**. The architecture is controlled; several process-critical setpoints still require primary-source recovery or local qualification.

---

# RP-01 direct anchors

## Starting material

- LPE-grown n-HgCdTe on electrically insulating CdZnTe.
- nominal `x≈0.30`.
- supplier carrier density `9.8×10^14 cm^-3`.
- supplier electron mobility `4.0×10^4 cm²/V·s`.
- active-layer thickness `9.5 µm`.
- supplier measurement temperature for n/µ is not stated.

## Contact-window RIE

Direct RP-01:

- Plasma Technology parallel-plate reactor.
- printed gas notation `CH4/5H2`.
- total flow `64 sccm`.
- pressure `100 mTorr`.
- RF power `50 W`.
- time `60 s`.
- reported converted density `~2.0×10^15 cm^-3`.
- reported mobility `~3.3×10^4 cm²/V·s`.
- Hall/resistivity measurements at 80 K and 300 K with variable field up to 2 T.

### Important gas-ratio state — P08A

A same-lineage HgCdTe RIE review explicitly summarizes the relevant RF parallel-plate branch as `CH4:H2 = 1:5`.

Evidence grade: **secondary same-lineage**, not direct RP-01 MFC data.

Conditional derived split from 64 sccm total:

- CH4 `10.6667 sccm`;
- H2 `53.3333 sccm`.

Do not say Smith et al. directly published those individual flows until a primary source is recovered.

### Important Hall/depth correction — P08B

RP-01 explicitly says `2.0×10^15 cm^-3` is **averaged over the RIE-converted thickness**.

Therefore the volume density is not independent of `d_conv`.

For a uniform converted layer:

`N_s = n_vol d_conv`.

If the cited prior `d_conv≈8 µm` was the thickness used, the conditional sheet-density scale is

`N_s≈1.6×10^12 cm^-2`.

Do not qualify RIE only by `n_vol`. The controlled RIE state vector must include at least:

`{R_sheet / N_s, µ_H or multicarrier state, d_conv, L_conv, d_etch, rho_c}`.

The exact Musca-1998 conditions attached to the cited ~8-µm depth remain unresolved. Keep ~8 µm as `P-OTHER-SOURCE / SIMILAR-CONDITIONS`, not a directly measured RP-01 depth.

## Lithography/passivation/metal

Direct RP-01:

- Mask-2 resist ~`4–5 µm`.
- prebake `80 °C / 30 min`.
- chlorobenzene treatment `30 min`.
- pattern/develop/water rinse.
- native anodic oxide `800 Å = 80 nm`.
- Cr `300 Å = 30 nm`.
- Au `2700 Å = 270 nm`.

Still open: resist product/spin/dose/developer, exact UWA anodization recipe, deposition base pressure/rates/substrate T, RIE-to-metal delay, lift-off solvent/time.

Same-UWA passivation/contact paper identified but publicly indexed experimental recipe remains unavailable. TI KOH/ethylene-glycol anodization remains a **non-UWA transfer candidate**, not historical fact.

## Test geometry

- nine contacts.
- each `300×300 µm`.
- adjacent gaps `50,100,...,400 µm`.
- same structure supports TLM and photoconductor performance measurements.
- 80-K `rho_c≈9×10^-4 Ω·cm²`.
- Figures 3,5,6,7 correspond to the same typical device, but exact contact pair/gap remains unknown.

## Detector benchmark

- `80 K`.
- stated `60°` FOV.
- spectral responsivity at `1 kHz`.
- representative noise field `10 V/cm`.
- HP35665A + low-noise preamp.
- 1/f knee ~`3 kHz`.
- g-r plateau ~`24.5 nV/√Hz`.
- detector-response cutoff ~`4.4 µm`.
- BLIP `D*≈2.0×10^11 cm Hz^1/2/W` at `4 µm`.
- QE ~`70%`.

Do not assume the 24.5-nV/√Hz plateau is the exact noise value used in the historical 1-kHz D* curve.

---

# Upstream state

## x≈0.30 Te-rich LPE

Correct key article is Schmit–Hager–Wood 1982, not the earlier mistaken Tung attribution.

Best explicit Bowers–Schmit tie line:

- `xL=0.082`;
- `yL=0.810`;
- `TL=507 °C`;
- `xS=0.29`;
- `xS/xL=3.54`.

Derived charge mass fractions:

- Hg `0.249738`;
- Cd `0.012502`;
- Te `0.737760`.

Total charge mass remains apparatus dependent.

Same Honeywell patent lineage directly supports covered graphite horizontal-slider architecture, auxiliary HgTe/HgTe+Te source, N2 purge, H2 processing, heating above liquidus followed by growth below liquidus, and step/continuous/combined cooling. An example ~30-min growth period exists but is **not tied to xS=.29 + 9.5 µm**, so it is not a released growth time.

## Substrate

Use measured lattice mismatch, A/B polarity, miscut, HRXRD, EPD, inclusions, impurities, electrical isolation and final surface state.

A different-composition CdZnTe LPE branch supports a final `2–3% Br2 in methanol` treatment for a few seconds immediately before loading. This is a transfer candidate only, not the x≈0.30 Honeywell recipe.

## Hg anneal

Low-temperature Hg-rich anneal is the leading route to the final low-density n state. Historical screening region ~200–300 °C; Harman example 250 °C/1 h is not the RP-01 endpoint. Release by measured Hall + optical final state, not temperature×time alone.

---

# Key downstream decisions

## Mesa

Retain wet mesa isolation. Same-UWA detector work shows blanket CH4/H2 dry mesa degrades n-HgCdTe PC performance relative to wet bromine/HBr mesa.

Best near-composition candidate: `2% Br2 in 3:1 EG:HBr`, x=.28, ~2.78 µm/min at 21 °C. Concentration basis remains unresolved.

## Temporal response — P13/P13A

De-embed source/optics/bias/readout before assigning detector bandwidth.

A same-UWA 1998 thesis supervised by John Dell and assisted by David Redfern/Ed Smith used n-type `x≈0.30` HgCdTe at ~77 K under vacuum and explicitly kept bias small to avoid sweeping excess carriers into high-recombination contact regions.

Therefore a lifetime interpretation requires a low-field/bias-independence gate. Use `tau_eff` unless bulk lifetime is independently justified.

## Geometry

Track:

`CD_mask -> CD_resist -> CD_mesa -> CD_RIE_open -> CD_n+ -> CD_metal -> measured active gap/area`.

## Package

Historical package is not disclosed. P15 qualifies packaging by preservation of detector behavior plus mechanical integrity rather than inventing historical materials.

---

# Recovery checkpoints — read in order

1. `research/2026-08-15_checkpoint_through_P16.md`
2. `research/2026-08-15_checkpoint_after_source_recovery_round1.md`
3. `research/2026-08-15_checkpoint_after_source_recovery_round2.md` **CURRENT**

Then read:

- `docs/RP01_GAP_MATRIX.md`;
- `docs/SOURCE_LEDGER.md` and addenda;
- the relevant Pxx procedure/addendum;
- branch-specific dated research notes.

---

# Highest-impact remaining blockers

## RIE/contact

1. primary confirmation of CH4:H2=1:5 / exact individual UWA MFC values;
2. exact Musca-1998 conditions tied to ~8-µm conversion depth;
3. raw/derived sheet Hall reduction used historically;
4. reactor electrode geometry, RF frequency, self-bias, sample temperature;
5. metal base pressure/rates/RIE-to-metal delay/lift-off sequence.

## Lithography/passivation/mesa

6. exact resist product/spin/exposure/developer;
7. exact UWA anodization electrolyte/current/endpoint/rinse;
8. wet-mesa Br2 concentration basis and final rinse/strip.

## Upstream

9. x≈0.30 source synthesis/homogenization;
10. selected CdZnTe face/miscut and final surface preparation;
11. x≈0.30 growth-time/thickness relation;
12. Hg anneal chemical potential/time/cooldown that reaches RP-01 transport state.

## Historical characterization

13. exact contact pair/gap used for Figures 3/5/6/7;
14. historical low-noise preamp and analyzer RBW/ENBW convention;
15. package/interconnect construction.

---

# Recommended next work

Do **not** repeat generic metadata-only title searches that have already failed.

Prefer:

1. later UWA full-text detector/MEMS publications that inherit the same fabrication line and may disclose process recipes;
2. patents/proceedings/theses by exact UWA authors;
3. primary-source recovery of wet mesa/passivation/lithography details;
4. where source closure fails, define statistically controlled local transfer DOEs for P01/P02/P08/P09 instead of filling conventional cleanroom values by assumption;
5. synchronize `docs/RP01_GAP_MATRIX.md` and `docs/SOURCE_LEDGER.md` as each major result is promoted.

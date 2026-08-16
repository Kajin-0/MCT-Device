# AGENTS.md — MCT-Device continuity record

## Mission

Build a source-traceable, end-to-end HgCdTe photodetector fabrication and characterization manual whose final released process can be followed by a competent researcher without undocumented tribal knowledge.

First canonical process: **RP-01**, an n-type MWIR HgCdTe photoconductor reconstructed around Smith et al., *Semiconductor Science and Technology* 16, 455–462 (2001), DOI `10.1088/0268-1242/16/6/306`.

This file is the **front-door recovery map**. Detailed evidence lives in `docs/`, `procedures/`, `calculations/`, and `research/`. Always read the newest `research/*checkpoint*.md` after this file.

---

## Non-negotiable rules

1. Never invent a missing process number. Use `OPEN`, `CAL`, `QUAL`, `PARTIAL`, or `CANDIDATE-P`.
2. Never splice values from incompatible HgCdTe process families and present the result as a published recipe.
3. Distinguish direct publication, derived physics, apparatus calibration, and qualification experiment.
4. Every critical process step requires outcome metrology and a pass/fail gate.
5. Preserve corrections, rejected branches, and unresolved contradictions.
6. Report `n_H/p_H` and `µ_H` unless Hall-factor/multicarrier assumptions are justified.
7. Keep transmission edge, inferred `Eg`, inferred `x`, and detector-response cutoff distinct.
8. Keep physical etch depth, oxide-clear depth, electrical conversion depth and lateral conversion distinct.
9. Use measured fabricated geometry for field/area normalization; never substitute CAD/nominal dimensions when metrology exists.
10. A packaging step is a detector process step if it changes electrical/noise/optical behavior.
11. A measured system bandwidth is not detector bandwidth until source/readout transfer functions are de-embedded.
12. Safety/EH&S authorization is external to this scientific manual; hazardous-material operating authorization must be institution-specific.

---

# Current state — through P16

Controlled modules now exist for the complete path from substrate to packaged detector characterization:

1. `P01_WET_MESA_QUALIFICATION.md`
2. `P02_ANODIC_OXIDE_QUALIFICATION.md`
3. `P03_LPE_X030_QUALIFICATION.md`
4. `P04_HG_ANNEAL_QUALIFICATION.md`
5. `P05_HALL_VDP_MATERIAL_METROLOGY.md`
6. `P06_FTIR_COMPOSITION_THICKNESS_MAPPING.md`
7. `P07_CZT_SUBSTRATE_QUALIFICATION.md`
8. `P08_RIE_BLOCKING_CONTACT_QUALIFICATION.md`
9. `P09_CR_AU_METALLIZATION_TLM_QUALIFICATION.md`
10. `P10_DEVICE_DC_BIAS_SELF_HEATING.md`
11. `P11_ABSOLUTE_SPECTRAL_RESPONSIVITY_RADIOMETRY.md`
12. `P12_NOISE_PSD_NEP_DETECTIVITY.md`
13. `P13_TEMPORAL_FREQUENCY_RESPONSE_LIFETIME.md`
14. `P14_LITHOGRAPHY_MASK_GEOMETRY_CD_QUALIFICATION.md`
15. `P15_DIE_ATTACH_INTERCONNECT_CRYOGENIC_PACKAGE_QUALIFICATION.md`
16. `P16_MASTER_END_TO_END_PROCESS_TRAVELER.md`

**Important:** these are controlled qualification/transfer modules. There is **not yet** an end-to-end `REPRODUCIBLE-RELEASE` recipe because several process-critical historical variables remain open.

---

# RP-01 direct historical anchors

## Material

- LPE n-type HgCdTe on electrically insulating CdZnTe.
- nominal `x≈0.30`.
- supplier carrier density `9.8×10^14 cm^-3`.
- supplier electron mobility `4.0×10^4 cm²/V·s`.
- layer thickness `9.5 µm`.
- supplier measurement temperature for n/µ is **not stated**; never relabel it 77/80 K.

## Contact-window RIE

- Plasma Technology parallel-plate reactor.
- printed gas notation `CH4/5H2`.
- total flow `64 sccm`.
- pressure `100 mTorr`.
- RF power `50 W`.
- process time `60 s`.
- converted carrier density ~`2.0×10^15 cm^-3`.
- converted mobility ~`3.3×10^4 cm²/V·s`.
- converted material measured at 80 and 300 K with variable B up to 2 T.
- exact individual CH4/H2 MFC flows remain unresolved; do not guess what `CH4/5H2` means.

## Mask-2 / passivation / metal

- resist thickness ~`4–5 µm`.
- prebake `80 °C / 30 min`.
- chlorobenzene soak `30 min`.
- then pattern/develop/water rinse.
- native anodic oxide `800 Å = 80 nm`.
- Cr `300 Å = 30 nm`.
- Au `2700 Å = 270 nm`.

## Contact/device test structure

- nine contacts.
- each `300×300 µm`.
- first gap `50 µm`, then +50 µm increments, giving adjacent gaps 50–400 µm.
- same structure supports TLM and photoconductor performance evaluation.
- historical 80-K specific contact resistivity ~`9×10^-4 Ω·cm²`.
- derived sequential nine-contact string extent, if arranged in one line as described: `4.5 mm`; confirm actual mask topology before using as die/mesa dimension.

## Detector performance

- temperature `80 K`.
- stated FOV `60°`.
- spectral responsivity chopped at `1 kHz`.
- representative noise field `10 V/cm`.
- HP35665A analyzer + low-noise preamp.
- 1/f knee ~`3 kHz`.
- g-r plateau ~`24.5 nV/√Hz`.
- detector-response cutoff ~`4.4 µm`.
- BLIP `D*≈2.0×10^11 cm Hz^1/2/W` at `4 µm`.
- reported 300-K/60° background photon flux ~`1×10^15 cm^-2 s^-1`.
- QE ~`70%`.

Figures 3, 5, 6 and 7 are explicitly the **same typical device**. What remains unknown is which of the 50–400-µm contact gaps was used.

---

# Major process decisions already established

## Wet mesa branch

Same-UWA-lineage detector work shows blanket CH4/H2 dry mesa modifies active electrical material and degrades PC performance relative to wet bromine/HBr mesa. RP-01 therefore keeps wet mesa isolation and confines RIE to the contacts where n+ conversion is intentional.

Best current near-composition wet-etch transfer source (x=0.28):

- `2% Br2 in 3:1 EG:HBr`;
- ~21 °C rate `2.78 µm/min`;
- anisotropy ~`0.63`;
- best RMS roughness ~`2 nm`.

Critical blocker: the source does not unambiguously define the concentration basis of `2% Br2`. Never guess it.

## Native oxide branch

RP-01 closes only the 80-nm oxide thickness.

Strong historical transfer candidate:

- `0.1 M KOH`;
- `90% ethylene glycol / 10% DI water`;
- constant current ~`0.3 mA/cm²`;
- endpoint ~`15 V`;
- ~`2 min`;
- ~80 nm oxide.

Do not label this the exact UWA recipe until lineage or local qualification closes it.

## x≈0.30 Te-rich LPE

Correct key article: Schmit–Hager–Wood 1982, DOI `10.1016/0022-0248(82)90468-7`; early project notes incorrectly called it Tung et al.

Best explicit Bowers–Schmit tie line:

- `xL=0.082`;
- `yL=0.810`;
- `TL=507 °C`;
- resulting `xS=0.29`;
- `xS/xL=3.54`.

Derived mass fractions:

- Hg `0.249738`;
- Cd `0.012502`;
- Te `0.737760`.

Total charge mass is apparatus-specific and remains open. Never combine Radhakrishnan's ~4.8-g x≈0.20 charge with this composition and present the combination as published x≈0.30 data.

Supported apparatus family: covered graphite horizontal slider, auxiliary HgTe/HgTe+Te source, N2 purge, H2 process atmosphere, above-liquidus equilibration then growth below TL. Near 500 °C corresponds to derived ~7 °C supercooling for this tie line; qualification center only.

Cd weighing dominates direct xL uncertainty because Cd is only ~1.25 wt% in the candidate melt.

## Wipe-off

Correct patent is US4592304A. Dedicated wipe well uses loose unpolished CdTe pieces in vertical slots ~1 mm apart to remove residual melt. Translation speed/contact force remain apparatus qualification variables.

## Hg anneal

Low-temperature Hg-rich treatment is the leading bridge from as-grown native-defect p-type material to low-density n-type state.

Historical screening region:

- roughly 200–300 °C;
- broad pHg region 0.1–250 Torr depending defect state;
- Harman example 250 °C / 1 h.

That example generally ends in low-10^16 cm^-3 material, so it is not the RP-01 endpoint. Control by final Hall + optical state, not T×time.

## Material metrology

P05: full VdP/current+field reversal, symmetric B sweep, multicarrier escalation.

P06: full FTIR spectra/spatial map; keep optical edge/Eg/x/detector cutoff separate.

Hansen at x=.30, 80 K gives band-gap-equivalent wavelength ~5.09 µm while detector response cutoff is ~4.4 µm; this is not treated as a contradiction.

## RIE blocking contact

Separate oxide clearing, physical recession, electrical conversion depth and lateral conversion.

RP-01 cites earlier similar-condition n-type work indicating ~8-µm conversion depth; not yet matched sufficiently to call it a directly measured RP-01 depth.

## Metallization

Historical stack 30-nm Cr / 270-nm Au. Thermal evaporation is a later-UWA-compatible transfer candidate but not proven exact RP-01 deposition method. Base pressure, rate, substrate T and RIE-to-metal delay remain qualification variables.

## Bias/geometry

Use actual measured gap and active-region voltage:

`E = V_active / L_gap`.

Never compare different devices merely at the same applied voltage when gap differs.

## Radiometry/FOV

P11 Planck consistency check: 300-K photons integrated to 4.4 µm through a 30° half-angle cone gives ~`1.12×10^15 cm^-2 s^-1`, close to RP-01's quoted `1×10^15`. Thus historical “60° FOV” is provisionally consistent with a 60° full cone, but this remains an inference.

## Noise / D*

`D*(λ,f) = Rλ(f) sqrt(A) / e_n(f)`.

Historical ambiguity: responsivity is at 1 kHz while 1/f knee is ~3 kHz and 24.5 nV/√Hz is the g-r plateau. Do not assume that plateau is the noise inserted into historical 1-kHz spectral D*.

## Temporal response

P13 requires source/readout de-embedding and joint amplitude/phase validation before calling a pole a detector lifetime.

Same-UWA source recovered: Redfern, Musca, Smith, Dell, Faraone 1999, “On the Transient Photoconductive Decay Technique for Lifetime Extraction in HgCdTe.”

Broad historical Kruse benchmark: <=10^-7-s response for studied 77-K HgCdTe PCs; not RP-01-specific.

## Lithography / geometry

P14 tracks:

`CD_mask → CD_resist → CD_mesa → CD_RIE_open → CD_n+ → CD_metal → measured gap/area`.

Hatzakis 1980 and Collins/Halsted 1982 explain chlorobenzene lift-off profile control but do not identify RP-01 resist.

Tempting 50-µm historical-device inference remains unproven: W=300 µm, L=50 µm plus R≈4e5 V/W and e_n=24.5 nV/√Hz numerically gives D*≈2e11, but exact R, noise-frequency convention and active width are insufficiently closed.

## Packaging

RP-01 does not disclose die attach, wire bond, carrier, window, aperture or vacuum construction. P15 therefore qualifies package by pre/post detector behavior and mechanical reliability rather than inventing a historical package recipe.

Package bakeout is treated as part of the detector thermal history.

## Master integration

P16 orders the whole process and defines genealogy, witnesses, hold points, elapsed-time clocks, deviations, rework handling and the final data package.

---

# Latest recovery documents

Read in this order:

1. `AGENTS.md`
2. newest `research/*checkpoint*.md` — currently create/read `2026-08-15_checkpoint_through_P16.md`
3. `procedures/P16_MASTER_END_TO_END_PROCESS_TRAVELER.md`
4. `docs/RP01_GAP_MATRIX.md`
5. `docs/SOURCE_LEDGER.md` plus `docs/SOURCE_LEDGER_ADDENDUM_P13_P14.md`
6. relevant Pxx procedure(s)
7. corresponding dated `research/` notes
8. supporting calculations

---

# Highest-impact blockers remaining

## Upstream

- final substrate face/miscut and exact final surface preparation;
- selected growth-well geometry/total charge mass;
- x≈0.30 source synthesis/homogenization;
- exact equilibration/supercooling/cooling/growth-time calibration;
- wipe-off translation mechanics;
- Hg anneal time/chemical potential/cooldown to hit target transport state.

## Frontside

- Br2 concentration basis/post-etch rinse;
- exact UWA anodization recipe or complete local qualification;
- Mask-1 and Mask-2 resist identity/exposure/developer;
- exact CH4/H2 MFC split;
- exact ~8-µm conversion source conditions;
- metal base pressure/rates/RIE-to-metal interval;
- lift-off solvent/time.

## Geometry/package/measurement

- which historical contact pair/gap generated Figures 3/5/6/7;
- historical package/interconnect details;
- historical low-noise preamp and exact ENBW/noise convention for Figure 7;
- statistical numerical acceptance windows/yield after local device data exist.

---

# Next recommended work

1. Create/maintain the checkpoint through P16.
2. Convert P16 into a practical blank traveler/template under `travelers/`.
3. Continue source recovery on the remaining high-impact blockers, prioritizing exact CH4/H2 split, lithography chemistry and same-lineage LPE/anneal details.
4. Do not add a new detector architecture until RP-01 reaches a coherent local qualification/release boundary.

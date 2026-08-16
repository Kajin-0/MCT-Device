# AGENTS.md — MCT-Device continuity record

## Mission

Build a source-traceable, end-to-end HgCdTe photodetector fabrication and characterization manual whose final released process can be followed by a competent researcher without undocumented tribal knowledge.

First canonical process: **RP-01**, an n-type MWIR HgCdTe photoconductor reconstructed around Smith et al., *Semiconductor Science and Technology* 16, 455–462 (2001), DOI `10.1088/0268-1242/16/6/306`.

Detailed evidence lives in `docs/`, `procedures/`, `calculations/`, and `research/`. This file preserves the current scientific state and the guardrails future agents must not violate.

---

## Non-negotiable rules

1. Never invent a missing process number. Use `OPEN`, `CAL`, or `QUAL`.
2. Never splice values from incompatible HgCdTe process families and present the result as a published recipe.
3. Distinguish direct publication, derived physics, apparatus calibration, and qualification experiment.
4. Every critical process step requires outcome metrology and a pass/fail gate.
5. Preserve corrections, rejected branches, and unresolved contradictions.
6. Report `n_H/p_H` and `µ_H` unless Hall-factor/multicarrier assumptions are justified.
7. Keep transmission edge, inferred `E_g`, inferred `x`, and detector-response cutoff distinct.
8. Keep physical etch depth, oxide-clear depth/time, electrical conversion depth, and lateral conversion distinct.
9. Keep PSD (`V²/Hz`), ASD (`V/√Hz`), finite-band RMS noise, and ENBW distinct.
10. For D*, responsivity and noise must refer to the same `T`, `E`, `f`, optical background, device geometry, load, and active-area convention.
11. Safety/facility authorization is separate from scientific process definition; repository procedures do not replace EH&S requirements.

---

# RP-01 direct anchors

## Starting material

- LPE HgCdTe on electrically insulating CdZnTe.
- approximately `x≈0.30`, n-type.
- supplier-specified carrier density `9.8×10^14 cm^-3`.
- supplier-specified mobility `4.0×10^4 cm²/V·s`.
- active layer thickness `9.5 µm`.
- **Temperature of the supplier n/µ values is not stated.** Do not relabel them as 77 K or 80 K.

## Contact-window RIE

- Plasma Technology parallel-plate RIE.
- printed gas notation `CH4/5H2`.
- total flow `64 sccm`.
- pressure `100 mTorr`.
- RF power `50 W`.
- time `60 s`.
- converted density ~`2.0×10^15 cm^-3`.
- converted mobility ~`3.3×10^4 cm²/V·s`.
- converted material measured at 80 K and 300 K with variable B to 2 T.

**Critical blocker:** individual CH4/H2 MFC flows corresponding to `CH4/5H2` are not source-verified. Do not infer 1:5, 5:1, 5%, etc.

## Lithography / passivation / metal

- resist ~`4–5 µm`.
- prebake `80 °C / 30 min`.
- chlorobenzene soak `30 min`.
- anodic oxide `800 Å = 80 nm`.
- Cr `300 Å = 30 nm`.
- Au `2700 Å = 270 nm`.

## Contact-string / TLM structure

- nine contacts.
- each ~`300×300 µm`.
- first gap `50 µm`, then increments of `50 µm`.
- historical `ρ_c≈9×10^-4 Ω·cm² at 80 K`.

The structure served both TLM and photoconductor performance work. The exact contact pair/gap used for every historical “typical device” spectrum/noise curve remains open.

## Detector benchmark

- detector `T=80 K`.
- FOV `60°`.
- optical chop `1 kHz`.
- canonical field `10 V/cm`.
- responsivity sweeps extend to roughly `50 V/cm`.
- HP35665A analyzer + unidentified low-noise preamplifier.
- 1/f knee ~`3 kHz`.
- g-r noise ASD ~`24.5 nV/√Hz`.
- detector-response cutoff ~`4.4 µm`.
- BLIP `D*≈2.0×10^11 cm√Hz/W` at `4 µm`.
- reported 300-K/60° background photon flux ~`1.0×10^15 cm^-2 s^-1`.
- quoted QE ~`70%`.

RP-01 directly defines

`D*_lambda = (R_lambda/V_n) sqrt(l w Δf)`.

---

# Controlled end-to-end architecture

1. `P07` qualify CdZnTe substrate.
2. Prepare composition-matched Te-rich LPE charge.
3. `P03` grow x≈0.30 HgCdTe in Hg-contained horizontal-slider LPE.
4. `P06` map thickness/composition and `P05` measure electrical state.
5. `P04` Hg-overpressure anneal toward the RP-01 n-type state.
6. Repeat `P05/P06` gates.
7. `P01` wet mesa isolation.
8. `P02` native anodic-oxide passivation.
9. Contact-window lithography.
10. `P08` localized CH4/H2 RIE n+ blocking-contact formation.
11. `P09` Cr/Au deposition, lift-off and TLM.
12. `P10` define active electrical geometry, DC field and self-heating state.
13. Package/interconnect.
14. `P11` absolute spectral responsivity/radiometry.
15. `P12` noise PSD/ASD, NEP and D*.
16. Future module: temporal/frequency response and lifetime.

No end-to-end `REPRODUCIBLE-RELEASE` exists yet.

---

# P01 — wet mesa

`procedures/P01_WET_MESA_QUALIFICATION.md`

Near-composition source (x=0.28):

- `2% Br2` in `3:1 ethylene glycol:HBr`.
- 21 °C rate `2.78 µm/min`.
- rate variation ~`±26%`.
- anisotropy ~`0.63 ±11%`.
- best RMS roughness ~`2 nm`.
- rate approximately doubles per +10 °C.

Same-UWA x≈0.31 detector comparison supports wet mesa over blanket H2/CH4 dry mesa.

**Blocker:** concentration basis of “2% Br2” is unresolved.

---

# P02 — anodic oxide

`procedures/P02_ANODIC_OXIDE_QUALIFICATION.md`

RP-01 closes only ~80-nm native oxide thickness.

Strong transfer candidate:

- `0.1 M KOH`.
- `90% EG / 10% DI water`.
- constant current ~`0.3 mA/cm²`.
- ~`15 V` endpoint.
- ~`2 min`.
- ~80-nm oxide.

Do not call this the exact UWA recipe until lineage/local qualification closes it.

---

# P03 — x≈0.30 Te-rich LPE

`procedures/P03_LPE_X030_QUALIFICATION.md`

Correct core article: Schmit–Hager–Wood 1982, DOI `10.1016/0022-0248(82)90468-7`. Early project attribution to “Tung et al.” was wrong.

Bowers–Schmit composition-matched tie line:

- `xL=0.082`.
- `yL=0.810`.
- `TL=507 °C`.
- `xS=0.29`.
- tabulated `xS/xL=3.54`.

Derived elemental mass fractions:

- Hg `0.249738`.
- Cd `0.012502`.
- Te `0.737760`.

Total charge mass is apparatus dependent.

Architecture: covered graphite horizontal slider, auxiliary HgTe/HgTe+Te source, quartz tube, N2 purge, H2 process atmosphere, heat above liquidus then grow below.

~500 °C corresponds to derived ~7 °C supercooling for the tie line; qualification center point only.

Radhakrishnan 2003 contributes apparatus engineering (6N elements, 700 °C/8 h source synthesis, meltback, wipe-off) but belongs to ~x=0.20. Never combine its 4.8-g charge with the Bowers–Schmit x≈0.30 composition and call it published.

Charge sensitivity: `calculations/LPE_CHARGE_COMPOSITION_SENSITIVITY.md`; Cd weighing dominates direct xL uncertainty.

---

# LPE wipe-off

Primary apparatus: US4592304A.

- dedicated wipe-off well.
- loose unpolished CdTe pieces.
- ~1-mm slot spacing.
- mechanical wiping + surface-tension adhesion + capillary wicking.

Open: slider speed, contact force, wipe T, scratch and residual-droplet limits.

---

# P04 — Hg anneal

`procedures/P04_HG_ANNEAL_QUALIFICATION.md`

- broad Hg-rich regime roughly 200–300 °C.
- broad primary Hg partial-pressure range 0.1–250 Torr depending defect state.
- Harman example `250 °C / 1 h`.

That example gives low-10^16 cm^-3 material, so it is not the RP-01 endpoint.

Nagahama: 250–300 °C can yield n-type x≤0.30 material without apparent composition shift; 400 °C can alter interface composition.

Control by final measured `(sign, n_H, µ_H, optical edge/x, thickness, morphology)`, not T×t alone.

---

# P05 — Hall / van der Pauw

`procedures/P05_HALL_VDP_MATERIAL_METROLOGY.md`

- eight zero-field reversal/reciprocity states.
- full van der Pauw solution.
- current-linearity/self-heating check.
- symmetric B sweep.
- current + field reversal.
- raw data retention.
- one-carrier reduction only after Hall-linearity/model test.
- multicarrier escalation where needed.

VdP gate:

- ≤3% PASS.
- >3–5% conditional.
- >5% fail.

Qualification B grid:

`0, ±0.01, ±0.025, ±0.05, ±0.10, ±0.20, ±0.50 T`.

One-carrier RP-01 consistency:

- `ρ≈0.159 Ω·cm`.
- `Rs≈168 Ω/sq`.
- `|RH|≈6.37×10^3 cm³/C`.

---

# P06 — FTIR composition/thickness mapping

`procedures/P06_FTIR_COMPOSITION_THICKNESS_MAPPING.md`

- retain raw transmission.
- report traceable transmission edge separately.
- fringe/full-spectrum thickness fit cross-calibrated against physical thickness.
- full-spectrum composition model preferred.
- same map coordinates before/after anneal.
- minimum 9-point map; 5×5+ preferred during LPE qualification.

Hansen x=.30 at 80 K gives `Eg≈0.243684 eV`, band-gap-equivalent wavelength ~`5.09 µm`; RP-01 detector cutoff ~4.4 µm. Do not force these quantities to equality.

---

# P07 — CdZnTe substrate

`procedures/P07_CZT_SUBSTRATE_QUALIFICATION.md`

Record:

- Zn fraction / measured lattice mismatch.
- A/B polarity.
- miscut magnitude and azimuth.
- HRXRD linewidth.
- EPD/dislocation metric.
- IR Te-inclusion/precipitate map.
- trace impurities, especially Cu.
- substrate leakage/resistivity.
- dimensions/TTV/bow.
- polish/roughness.
- final chemical preparation and clean-to-load delay.

Historical high-quality benchmark: Cd0.96Zn0.04Te around `EPD≈5×10^4 cm^-2`, HRXRD linewidth ~`25 arcsec`; not released limits.

Exact polarity/miscut remains qualification dependent.

---

# P08 — RIE blocking contact

`procedures/P08_RIE_BLOCKING_CONTACT_QUALIFICATION.md`

Direct nominal recipe:

`64 sccm total / 100 mTorr / 50 W / 60 s / CH4/5H2`.

Required separate outputs:

- oxide-clear time.
- physical HgCdTe recession `d_etch`.
- P05 n+/µH.
- electrical conversion depth `d_conv`.
- lateral conversion `L_conv`.
- P09 TLM outcome.

RP-01 cites prior n-type work with ~8-µm conversion under similar conditions. Tag as other-source/similar-condition evidence until exact Musca-1998 conditions are matched.

Counterexample: related UWA p-HgCdTe RIE physically removed ~0.2 µm while electrical conversion extended ~1.5 µm.

LBIC anchors:

- Waterloo Scientific scanner.
- Nd:YLF 1.047 µm.
- ~400 mW/cm².
- 80 K.
- ~300×300-µm RIE squares.

---

# P09 — Cr/Au + TLM

`procedures/P09_CR_AU_METALLIZATION_TLM_QUALIFICATION.md`

Direct stack:

- Cr 30 nm.
- Au 270 nm.

Historical benchmark:

`ρ_c≈9×10^-4 Ω·cm² at 80 K`.

Historical deposition method/base pressure/rates remain open. Later UWA HgCdTe work supports thermal evaporation as a transfer candidate, not historical proof.

Require:

- RIE-to-metal exposure timestamps.
- base/deposition pressure logs.
- QCM/witness calibration.
- rate histories.
- sample temperature.
- no undocumented in-situ ion clean.
- lift-off visual QC.
- symmetric low-field I–V.
- raw nine-contact TLM regression.
- thermal-cycle/aging qualification.

---

# P10 — device geometry, field and self-heating

`procedures/P10_DEVICE_DC_BIAS_SELF_HEATING.md`

Primary bias variable is measured active-region field

`E=V_active/L`,

with measured gap `L`, not nominal source voltage.

Historical canonical condition: `10 V/cm`; responsivity field sweep to ~50 V/cm.

Using the one-carrier RP-01 consistency state, `W=300 µm`, `t=9.5 µm`:

- ideal current at 10 V/cm ~`1.79 mA`, independent of gap in the uniform bulk model.
- for 50–400 µm gaps, ideal power spans ~`0.0895–0.716 mW`.

These are derived screening values, not measured historical currents.

P10 requires:

- actual gap/width/area metrology.
- series/contact voltage-drop correction.
- symmetric dark I–V.
- current/power/temperature logging.
- low-bias `R(T)` thermometer calibration or direct thermal method.
- pulsed-vs-DC heating check.
- sweepout metric `S(E)=R_meas/R_low-field-linear`.
- polarity comparison.
- complete load/bias circuit documentation.

---

# P11 — absolute spectral responsivity / radiometry

`procedures/P11_ABSOLUTE_SPECTRAL_RESPONSIVITY_RADIOMETRY.md`

Preferred architecture: spectral comparison to a traceable calibrated IR transfer detector.

Modern NIST IR spectral-comparator facilities cover the RP-01 MWIR region with percent-level absolute responsivity uncertainty. Historical low-background measurement lineage used an Optronics 735D relative spectral system with pyroelectric reference monitoring plus broadband blackbody absolute scaling.

P11 controls:

- wavelength calibration.
- slit/bandpass convolution.
- order sorting/stray light.
- atmospheric H2O/CO2.
- reference/DUT substitution geometry.
- radiant-power vs irradiance responsivity.
- calibrated electronics gain.
- optical linearity.
- 80 K / 10 V/cm / 1 kHz canonical state.
- exact chopper/RMS/peak/fundamental convention.
- aperture/view-factor blackbody radiometry.
- full uncertainty budget.

Target for laboratory absolute `R_v(4 µm)`: initially `<5%` expanded uncertainty (project target, not historical claim).

### FOV inference

`calculations/RP01_300K_BACKGROUND_FLUX_CHECK.md` shows ideal 300-K Planck photon flux to 4.4 µm:

- 60° **full cone** (30° half-angle): `1.124×10^15 cm^-2 s^-1`.
- 60° half-angle: `3.372×10^15 cm^-2 s^-1`.

RP-01 quotes ~`1.0×10^15`. Therefore historical “60° FOV” is provisionally interpreted as **60° full angle**, tagged as an inference until physical optical geometry is recovered.

---

# P12 — noise PSD, NEP and D*

`procedures/P12_NOISE_PSD_NEP_DETECTIVITY.md`

Direct RP-01 noise anchors:

- 80 K.
- 10 V/cm.
- 60° FOV.
- HP35665A + low-noise preamp.
- 1/f knee ~3 kHz.
- g-r ASD ~24.5 nV/√Hz.

Required distinctions:

- PSD `S_v` in V²/Hz.
- ASD `e_n=sqrt(S_v)` in V/√Hz.
- finite-band RMS noise.
- FFT/filter ENBW.

Default new-measurement detectivity rule:

`D*(lambda,f)=R_v(lambda,f) sqrt(A) / e_n(f)`

with responsivity/noise evaluated at the same signal frequency and state.

### Important historical ambiguity

RP-01 responsivity was chopped at 1 kHz, but its 1/f knee is ~3 kHz. Therefore the white/g-r `24.5 nV/√Hz` floor cannot automatically be assumed to be the noise used for the published 1-kHz D* curve. Exact historical noise-frequency convention remains open.

P12 requires:

- electronics-floor states.
- gain calibration.
- PSD normalization validation with resistor/noise source.
- PSD-level quadrature subtraction, never linear ASD subtraction.
- 1/f exponent/knee fit.
- g-r plateau reporting.
- `e_n(1 kHz)` for canonical P11 pairing.
- NEP.
- measured D*.
- background-flux sweep before strong BLIP claim.
- complete uncertainty budget.

---

# Current controlled modules

- `P01_WET_MESA_QUALIFICATION.md`
- `P02_ANODIC_OXIDE_QUALIFICATION.md`
- `P03_LPE_X030_QUALIFICATION.md`
- `P04_HG_ANNEAL_QUALIFICATION.md`
- `P05_HALL_VDP_MATERIAL_METROLOGY.md`
- `P06_FTIR_COMPOSITION_THICKNESS_MAPPING.md`
- `P07_CZT_SUBSTRATE_QUALIFICATION.md`
- `P08_RIE_BLOCKING_CONTACT_QUALIFICATION.md`
- `P09_CR_AU_METALLIZATION_TLM_QUALIFICATION.md`
- `P10_DEVICE_DC_BIAS_SELF_HEATING.md`
- `P11_ABSOLUTE_SPECTRAL_RESPONSIVITY_RADIOMETRY.md`
- `P12_NOISE_PSD_NEP_DETECTIVITY.md`

Calculations:

- `HANSEN_BANDGAP_MODEL.md`
- `LPE_CHARGE_COMPOSITION_SENSITIVITY.md`
- `RP01_300K_BACKGROUND_FLUX_CHECK.md`

---

# Highest-priority unresolved items

## Growth/material

- full Schmit–Hager–Wood x≈0.30 experimental section.
- exact CdZnTe face/miscut for selected slider process.
- final CdZnTe surface etch/rinse/load delay.
- boat well geometry and charge mass.
- exact x≈0.30 charge synthesis/homogenization.
- exact equilibration/supercooling/cooling trajectory.
- growth-time/thickness calibration.
- wipe-off velocity/contact mechanics.
- exact Hg anneal chemical potential/time/cooldown for RP-01 transport state.

## Device fabrication

- exact detector active gap used for historical performance curves.
- Mask-1/Mask-2 resist identities/exposure/develop.
- P01 2% Br2 concentration basis and post-etch rinse.
- exact UWA anodization recipe or completed P02 transfer qualification.
- individual CH4/H2 gas flows.
- full Musca-1998 ~8-µm conversion condition.
- RIE reactor geometry/self-bias/sample temperature.
- historical/selected Cr/Au deposition method/rates/base pressure.
- exact lift-off solvent/time/agitation.
- die attach/wire bond/package geometry.

## Characterization

- exact historical Optronics system and calibration reference.
- historical load/bias circuit.
- active optical area convention.
- exact HP35665A settings and preamp model.
- historical noise point used for D*.
- temporal/frequency-response/lifetime SOP.
- final absolute uncertainty budgets and production acceptance windows.

---

# Next work

1. Build a controlled temporal/frequency-response and lifetime module.
2. Continue searching UWA theses/full papers for `CH4/5H2`, RIE conversion depth, lithography and metallization details.
3. Build packaging/die-attach/wire-bond only after pad geometry/material compatibility is closed enough.
4. Synchronize `docs/RP01_GAP_MATRIX.md` and `docs/SOURCE_LEDGER.md` with P08–P12 sources/status.
5. Begin converting qualified modules into literal process travelers only after all process-critical OPEN variables in that module are either source-closed or experimentally qualifiable.

# AGENTS.md — MCT-Device continuity record

## Mission

Build a source-traceable, end-to-end HgCdTe detector fabrication and characterization manual whose final released process can be followed by a competent researcher without relying on undocumented tribal knowledge.

The first canonical reference process is **RP-01**, an n-type MWIR HgCdTe photoconductor reconstructed around Smith et al. 2001, DOI `10.1088/0268-1242/16/6/306`.

This file is a continuity map. Detailed evidence and procedures live in `docs/`, `procedures/`, `calculations/`, and `research/`.

---

## Non-negotiable research rules

1. Never invent a missing setpoint. Use `OPEN`, `CAL`, or `QUAL` instead.
2. Never combine values from unrelated HgCdTe process branches and present the combination as a published recipe.
3. Distinguish direct publication, derivation, apparatus calibration, and local qualification.
4. Every process step must have an outcome measurement and a pass/fail gate.
5. Preserve negative results, incompatible branches, and corrected citations.
6. Report Hall quantities as `n_H/p_H` and `µ_H` unless Hall-factor/multicarrier assumptions are explicitly justified.
7. Keep transmission edge, inferred `Eg`, inferred `x`, and detector-response cutoff separate.
8. Keep physical etch depth and plasma-induced electrical conversion depth separate.
9. Safety/facility authorization is external to the scientific process specification; do not omit scientific variables merely because a hazardous-material SOP is separately required.

---

# RP-01 direct anchors

## Starting material

- LPE HgCdTe on electrically insulating CdZnTe.
- approximately `x≈0.30`, n-type.
- supplier-specified carrier density `9.8×10^14 cm^-3`.
- supplier-specified electron mobility `4.0×10^4 cm²/V·s`.
- layer thickness `9.5 µm`.
- **measurement temperature for the supplier n/µ values is not stated**. Do not relabel them as 77 K or 80 K.

## Contact-window RIE

- Plasma Technology parallel-plate reactor.
- printed gas notation `CH4/5H2`.
- total flow `64 sccm`.
- pressure `100 mTorr`.
- RF power `50 W`.
- time `1 min`.
- converted density `~2.0×10^15 cm^-3`.
- converted mobility `~3.3×10^4 cm²/V·s`.
- converted material measured at 80 K and 300 K with variable B up to 2 T; current accessible text does not uniquely assign the summary n/µ pair to one temperature.

**Critical unresolved variable:** the exact individual CH4/H2 MFC flows corresponding to `CH4/5H2` are not yet source-verified. Do not infer 1:5, 5:1, 5%, etc.

## Lithography/passivation/metallization

- resist ~`4–5 µm`.
- prebake `80 °C / 30 min`.
- chlorobenzene soak `30 min`.
- native anodic oxide `800 Å = 80 nm`.
- Cr `300 Å = 30 nm`.
- Au `2700 Å = 270 nm`.

## TLM

- nine contacts.
- each `300×300 µm`.
- first separation `50 µm`; successive separation increment `50 µm`.
- specific contact resistivity `~9×10^-4 Ω·cm² at 80 K`.

## Detector benchmark

- detector T `80 K`.
- FOV `60°`.
- chopping `1 kHz`.
- representative noise field `10 V/cm`.
- HP35665A analyzer + low-noise preamplifier.
- 1/f knee ~`3 kHz`.
- g-r noise ~`24.5 nV/√Hz`.
- detector-response cutoff ~`4.4 µm`.
- BLIP `D*≈2.0×10^11 cm·Hz^1/2/W` at `4 µm`.
- QE ~`70%`.

---

# Controlled process architecture

Current reconstruction:

1. `P07` qualify CdZnTe substrate.
2. Prepare composition-matched Te-rich LPE charge.
3. `P03` grow x≈0.30 HgCdTe in Hg-contained horizontal-slider LPE.
4. `P06` map thickness/composition; `P05` measure electrical state.
5. `P04` Hg-overpressure anneal toward RP-01 n-type state.
6. Repeat `P05/P06` material gates.
7. `P01` wet mesa isolation.
8. `P02` native anodic-oxide passivation.
9. Mask-2 contact-window lithography.
10. `P08` localized CH4/H2 RIE blocking-contact formation.
11. `P09` Cr/Au deposition, lift-off and TLM qualification.
12. Packaging/interconnect.
13. Absolute responsivity, spectral response, noise, temporal response and D* characterization.

No end-to-end `REPRODUCIBLE-RELEASE` exists yet.

---

# P01 — wet mesa

File: `procedures/P01_WET_MESA_QUALIFICATION.md`

Best current near-composition quantitative source, x=0.28:

- `2% Br2` in `3:1 ethylene glycol:HBr`.
- 21 °C mean vertical rate `2.78 µm/min`.
- rate variation ~`±26%`.
- anisotropy `~0.63 ±11%`.
- best RMS roughness ~`2 nm`.
- rate approximately doubles per +10 °C.

**Blocker:** concentration basis of “2% Br2” is not source-verified.

Same-UWA x≈0.31 detector comparison supports wet mesa over blanket H2/CH4 dry mesa.

---

# P02 — anodic oxide

File: `procedures/P02_ANODIC_OXIDE_QUALIFICATION.md`

RP-01 closes film thickness at 80 nm but not formation recipe.

Strong transfer candidate from primary HgCdTe process literature:

- 0.1 M KOH.
- 90% EG / 10% DI water.
- constant current ~0.3 mA/cm².
- ~15 V formation endpoint.
- ~2 min.
- ~80 nm oxide.

Do not label this the exact UWA recipe until lineage or local qualification closes it.

---

# P03 — x≈0.30 Te-rich LPE

File: `procedures/P03_LPE_X030_QUALIFICATION.md`

Correct core article: Schmit–Hager–Wood 1982, DOI `10.1016/0022-0248(82)90468-7`; early project attribution to “Tung et al.” was incorrect.

Best composition-matched Bowers–Schmit tie line:

- `xL=0.082`.
- `yL=0.810`.
- `TL=507 °C`.
- `xS=0.29`.
- tabulated `xS/xL=3.54`.

Derived charge mass fractions:

- Hg `0.249738`.
- Cd `0.012502`.
- Te `0.737760`.

Total charge mass remains apparatus dependent.

Bowers–Schmit architecture: covered graphite horizontal slider, auxiliary HgTe/HgTe+Te source, quartz tube, N2 purge, H2 processing, heat above liquidus then grow below.

~500 °C corresponds to a derived ~7 °C supercooling relative to the 507 °C tie line; this is a qualification center point, not production release.

Radhakrishnan 2003 contributes apparatus engineering (6N elements, 700 °C/8 h source synthesis, meltback, wipe-off) but is an x≈0.20 branch. Never combine its 4.8-g charge with the Bowers–Schmit composition as a published recipe.

Charge sensitivity: `calculations/LPE_CHARGE_COMPOSITION_SENSITIVITY.md`; Cd weighing dominates direct xL uncertainty because Cd is only ~1.25 wt% of the candidate charge.

---

# LPE wipe-off

Primary apparatus: US4592304A.

- dedicated wipe-off well.
- loose unpolished CdTe pieces.
- vertical slots ~1 mm apart.
- mechanical wiping + surface-tension adhesion + capillary wicking.

Open: slider speed, wiper geometry/contact force, wipe T, scratch and residual-droplet limits.

---

# P04 — Hg-overpressure anneal

File: `procedures/P04_HG_ANNEAL_QUALIFICATION.md`

Primary screening anchor:

- Hg-rich anneal regime roughly 200–300 °C.
- broad published Hg partial-pressure range 0.1–250 Torr depending defect state.
- Harman example `250 °C / 1 h`.

That example typically yields low-10^16 cm^-3 material, so it is **not** the RP-01 endpoint.

Nagahama branch: 250–300 °C can yield n-type x≤0.30 material without apparent composition shift; 400 °C gives interface composition change.

Control the anneal by final measured state `(carrier sign, n_H, µ_H, optical edge/x, thickness, morphology)`, not temperature×time alone.

---

# P05 — Hall / van der Pauw

File: `procedures/P05_HALL_VDP_MATERIAL_METROLOGY.md`

- eight zero-field reversal/reciprocity states.
- full van der Pauw solution.
- current-linearity/self-heating screen.
- symmetric B sweep.
- current and field reversal.
- raw data retained.
- one-carrier reduction only after Hall-linearity/model check.
- multicarrier escalation on curvature/sign changes/unexplained MR.

VdP consistency gate:

- ≤3% PASS.
- >3–5% conditional.
- >5% fail.

Project qualification B grid: `0, ±0.01, ±0.025, ±0.05, ±0.10, ±0.20, ±0.50 T`.

One-carrier RP-01 consistency values for n=9.8×10^14, µ=4×10^4, t=9.5 µm:

- `ρ≈0.159 Ω·cm`.
- `Rs≈168 Ω/sq`.
- `|RH|≈6.37×10^3 cm³/C`.

---

# P06 — FTIR composition/thickness mapping

File: `procedures/P06_FTIR_COMPOSITION_THICKNESS_MAPPING.md`

- raw transmission retained.
- traceable edge descriptor reported separately.
- fringe/full-spectrum thickness fit cross-calibrated against physical thickness.
- full-spectrum composition model preferred.
- same coordinates before/after anneal.
- minimum 9-point map; 5×5+ preferred during LPE qualification.

Do not force detector cutoff = hc/Eg. Hansen x=.30 at 80 K gives band-gap-equivalent wavelength ~5.09 µm, whereas RP-01 detector response is ~4.4 µm; the quantities/conventions are not identical.

---

# P07 — CdZnTe substrate

File: `procedures/P07_CZT_SUBSTRATE_QUALIFICATION.md`

The substrate is a measured process input, not simply “Cd0.96Zn0.04Te (111).” Record:

- Zn/lattice mismatch.
- A/B polarity.
- miscut magnitude and azimuth.
- HRXRD linewidth.
- EPD/dislocation metric.
- IR inclusion/Te-precipitate map.
- trace impurities, especially Cu.
- substrate resistivity/leakage.
- dimensions/TTV/bow.
- polish/roughness.
- final surface preparation and clean-to-load delay.

Historical high-quality benchmark: Cd0.96Zn0.04Te around `EPD≈5×10^4 cm^-2`, XRD linewidth `≈25 arcsec`; these are benchmarks, not released limits.

Literature shows polarity/miscut effects are process dependent. Some LPE studies favor ~1.2–2° off (111)A; other successful slider systems use (111)B. Exact RP-01 face/miscut remains QUAL.

---

# P08 — RIE blocking contact

File: `procedures/P08_RIE_BLOCKING_CONTACT_QUALIFICATION.md`

Direct nominal RP-01 recipe remains:

`64 sccm total / 100 mTorr / 50 W / 60 s / CH4/5H2`

but individual gas flows remain OPEN.

Mandatory separate outputs:

- oxide-clear time `t_clear`.
- physical HgCdTe recession `d_etch`.
- P05 n+/µ_H state.
- electrical conversion depth `d_conv`.
- lateral conversion `L_conv`.
- TLM contact outcome after P09.

RP-01 cites earlier n-type work indicating `d_conv≈8 µm` under similar conditions. Tag as `P-OTHER-SOURCE/SIMILAR-CONDITIONS`, not as a directly measured RP-01 depth until Musca 1998 full conditions are matched.

Counterexample proving `d_conv != d_etch`: related p-type UWA RIE work at 410 mTorr and 0.4 W/cm² physically etched ~0.2 µm while electrical conversion extended ~1.5 µm.

LBIC anchors from RP-01:

- Waterloo Scientific scanner.
- Nd:YLF laser 1.047 µm.
- ~400 mW/cm².
- sample 80 K.
- qualification squares ~300×300 µm.

Reactor-transfer variables requiring closure: electrode area/spacing, RF frequency, self-bias, sample T, base pressure, chamber conditioning, exact gas split and MFC calibration.

Research record: `research/2026-08-15_rie_blocking_contact_lineage.md`.

---

# P09 — Cr/Au metallization and TLM

File: `procedures/P09_CR_AU_METALLIZATION_TLM_QUALIFICATION.md`

Direct RP-01 stack:

- Cr 30 nm.
- Au 270 nm.

Historical outcome:

- `ρ_c≈9×10^-4 Ω·cm² at 80 K` on the RIE-modified contact region.

Exact historical deposition method, base pressure and rates are not closed.

A later UWA HgCdTe process demonstrates thermal evaporation of Cr/Au, so thermal evaporation is the leading transfer candidate but is not claimed as the exact RP-01 tool/process.

P09 requires:

- RIE-to-metal exposure timestamps.
- base/deposition pressure logging.
- QCM calibration against witness thickness.
- Cr/Au rate histories.
- substrate-temperature monitoring/calibration.
- lift-off visual gate.
- symmetric low-field I–V.
- nine-contact TLM with raw regression data.
- thermal-cycle/contact-aging qualification.

Do not invent conventional vacuum/rate numbers before TLM capability data exist.

---

# Current module inventory

1. `P01_WET_MESA_QUALIFICATION.md`
2. `P02_ANODIC_OXIDE_QUALIFICATION.md`
3. `P03_LPE_X030_QUALIFICATION.md`
4. `P04_HG_ANNEAL_QUALIFICATION.md`
5. `P05_HALL_VDP_MATERIAL_METROLOGY.md`
6. `P06_FTIR_COMPOSITION_THICKNESS_MAPPING.md`
7. `P07_CZT_SUBSTRATE_QUALIFICATION.md`
8. `P08_RIE_BLOCKING_CONTACT_QUALIFICATION.md`
9. `P09_CR_AU_METALLIZATION_TLM_QUALIFICATION.md`

Supporting calculations:

- `HANSEN_BANDGAP_MODEL.md`
- `LPE_CHARGE_COMPOSITION_SENSITIVITY.md`

---

# Highest-priority unresolved variables

## Upstream

- full Schmit–Hager–Wood x≈0.30 experimental section.
- exact substrate face/miscut for selected slider process.
- final CdZnTe Br2/methanol surface preparation.
- boat well geometry and total charge mass.
- x≈0.30 charge synthesis/homogenization.
- exact equilibration/supercooling/cooling trajectory.
- growth-time/thickness calibration.
- wipe-off translation mechanics.
- exact Hg-anneal chemical potential/time/cooldown to hit RP-01 transport state.

## Downstream

- exact detector active dimensions.
- Mask-1 and Mask-2 resist identities/exposure/develop details.
- P01 Br2 concentration basis/post-etch rinse.
- exact UWA anodization recipe or completed local P02 qualification.
- `CH4/5H2` individual gas flows.
- exact Musca-1998 ~8-µm conversion conditions.
- RIE reactor geometry/self-bias/sample T.
- historical/selected Cr/Au deposition method, rates, base pressure.
- lift-off solvent/time/agitation.
- die attach/wire bond/package geometry.

## Characterization

- absolute responsivity/radiometry chain.
- exact noise preamp and analyzer RBW/ENBW/averaging.
- frequency-response/lifetime SOP.
- final D* uncertainty budget.

---

# Most natural next work

1. Search UWA theses/full papers for the explicit `CH4/5H2` gas split and Musca-1998 depth conditions.
2. Close Mask-2 resist/developer/exposure/lift-off chemistry from the same lineage.
3. Build a controlled **device electrical geometry / DC bias / self-heating** module.
4. Build **absolute spectral responsivity/radiometry** and **noise PSD/D*** modules.
5. Build packaging/wire-bond procedure only after contact-pad geometry and metal stack reliability are sufficiently closed.
6. Keep `docs/RP01_GAP_MATRIX.md`, `docs/SOURCE_LEDGER.md`, and dated research logs synchronized with all new modules.

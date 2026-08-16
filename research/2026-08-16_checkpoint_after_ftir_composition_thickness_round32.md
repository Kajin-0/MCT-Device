# Checkpoint — Round 32: FTIR composition / thickness / optical-edge / detector-cutoff closure

**Date:** 2026-08-16 America/New_York

## Round objective

Audit `P06_FTIR_COMPOSITION_THICKNESS_MAPPING.md` and determine whether a new top-level procedure was required to reproduce HgCdTe material optical metrology around RP-01.

Result: **P06 was already operator-capable.** No duplicate top-level spectroscopy procedure was created. Round 32 instead adds P06A as an empirical apparatus/model/provenance layer and a qualification register.

---

## Files created

- `procedures/P06A_FTIR_COMPOSITION_THICKNESS_CUTOFF_LINEAGE_ADDENDUM.md`
- `travelers/P06A_FTIR_COMPOSITION_THICKNESS_QUALIFICATION_REGISTER.md`
- `docs/SOURCE_LEDGER_ADDENDUM_ROUND32.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND32.md`
- this checkpoint

`AGENTS.md` is refreshed separately after this checkpoint.

---

# Main scientific outcome

The following quantities are now permanently separated:

`{d_physical, d_FTIR, lambda_transmission_edge, E_g,opt / x_opt, lambda_detector_cutoff}`.

They may correlate, but they are not interchangeable measurements.

In particular:

- a physical thickness is not an interference-fit thickness until calibrated;
- a transmission edge is not automatically a band gap;
- a band-gap-equivalent wavelength is not a detector cutoff;
- a detector cutoff is not an exact material composition coordinate.

---

# RP-01 historical state

Smith et al. 2001 directly provide:

- LPE n-HgCdTe on electrically insulating CdZnTe;
- material described approximately as `x≈0.30`;
- active thickness `9.5 µm`;
- detector cutoff stated as `4.4 µm` at the relevant 80-K spectral-response condition.

The recovered paper does **not** disclose:

- an FTIR material measurement;
- how `x≈0.30` was obtained;
- how `9.5 µm` was measured;
- the formal response criterion used to label the detector cutoff `4.4 µm`.

Therefore do not claim that RP-01 used FTIR unless a direct supplier/UWA record is recovered.

---

# Hansen consistency branch

Hansen, Schmit and Casselman 1982 give

`Eg(x,T) = -0.302 + 1.93x - 0.810x^2 + 0.832x^3 + 5.35e-4 T(1-2x)` eV.

For `x=0.300`, `T=80 K`:

`Eg = 0.243684 eV`.

Using `hc=1.239841984 eV µm`:

`lambda_g,eq = 5.0879 µm`.

Conversely, if the RP-01 detector cutoff `4.4 µm` is deliberately converted only as a consistency exercise:

`E_eq = 0.281782 eV`,

and inversion of Hansen at 80 K gives approximately

`x_Hansen,eq ≈ 0.3241`.

This does **not** prove that the historical material was x=.3241 or that x=.30 was wrong. It demonstrates that detector cutoff and band-gap/composition coordinates cannot be identified without an explicit measurement/model/convention.

The Hansen paper's ~`0.013 eV` standard error is the error of a global empirical fit compiled from many studies. It is not a local FTIR measurement uncertainty.

---

# Primary apparatus/method transfer recovered

## Chang et al. 2005 — automated FTIR microscope mapping

Primary author text exposes:

- Thermo Nicolet Centaur µs IR microscope;
- Thermo Nicolet 870 FTIR;
- computerized x-y stage;
- stated stage-position precision ~`1 µm`;
- adjustable aperture down to approximately `25 µm` at a wavelength of `10 µm`;
- approximately `100 µm` aperture chosen for mapping throughput/SNR;
- automatic transmission-curve fitting;
- composition from the intrinsic absorption edge;
- thickness from interference-pattern fitting below the intrinsic absorption region.

This is a strong mapping-apparatus transfer example, not RP-01 bench identity.

Permanent rule: **aperture setting is not automatically spatial resolution.** Measure/project the sample-plane footprint and account for diffraction/blur, stage repeatability/backlash and coordinate registration.

## Murthy et al. 2009 — directly relevant LPE/CdZnTe branch

The source reports:

- LPE HgCdTe on `Cd0.96Zn0.04Te`;
- Te-rich horizontal-slider growth;
- in-situ Te-saturation anneal near `230 °C`;
- composition estimated from the IR absorption spectrum at `300 K`;
- Bruker IFS 66v/S FTIR;
- an LPE sample with reported `x=0.200`;
- `34 µm` layer thickness estimated from FTIR interference fringes.

This is strong practical transfer evidence for the exact material/growth family relevant to P03/P30, but it is not RP-01 apparatus identity.

## Yue et al. 2019 — evacuated optical branch

Direct apparatus:

- Bruker IFS 66v/S;
- KBr beamsplitter;
- LN2-cooled HgCdTe detector;
- evacuated spectrometer path.

The paper's brief `1% Br2/methanol` premeasurement treatment remains experiment-specific and shall not be transplanted into RP-01 P06 automatically.

---

# Edge-metric / nonuniformity lineage

Gopal, Ashokan and Dhar 1992 establish a room-temperature transmission method using both:

- a 50%-transmission frequency;
- a zero-intercept/cut-on metric.

Disagreement between composition estimates obtained by the two edge metrics is useful evidence of composition nonuniformity/grade or model inadequacy.

### Source conflict retained

Current indexed text renders a thickness validity interval as `10–30 mm`, while an author/profile summary describes micrometre-scale epilayers. This is almost certainly a unit/indexing problem but has **not** been silently repaired.

Status:

`SOURCE-UNIT-CONFLICT / PRIMARY-PDF-LINE-NOT-YET-CHECKED`.

---

# Interference-fringe interpretation strengthened

Primary HgCdTe/CdZnTe work shows that poor interface state / Hg in-diffusion can reduce below-gap transmission and suppress the interference fringe pattern.

Therefore:

`weak/absent fringes != instrument failure`

without further diagnosis.

Possible causes to investigate include:

- interface quality;
- Hg diffusion;
- substrate transmission;
- roughness/scattering;
- free-carrier absorption;
- surface films;
- actual grading/stack complexity;
- instrument SNR.

Do not force `d_FTIR` from a spectrum with insufficient fringe information.

---

# Pre/post anneal rule

A spectral-edge shift following P04/P31 annealing does not by itself prove an alloy-composition change.

Consider simultaneously:

- P05 Hall state;
- free-carrier/band-filling effects;
- defect population;
- surface state;
- substrate/interface state;
- optical-model version;
- map re-registration;
- actual anneal trajectory.

Only after competing mechanisms are excluded should the shift be promoted to a composition change.

---

# P06A instrument/output vectors

Local instrument state:

`X_FTIR={instrument,source,beamsplitter,detector,path vacuum/purge,spectral range,resolution,apodization,phase correction,aperture/spot,incidence geometry,scan count,scan speed,background/reference,sample T,x-y registration,surface state,model/version}`.

Minimum output:

`Y_FTIR={raw T(nu),QC,lambda_50T,lambda_T-int,Eg,opt,x_opt,d_FTIR,grade/model state,residuals,uncertainties,map coordinates}`.

Physical thickness is stored separately as `d_physical`.

---

# P06A release labels

- `RAW-SPECTRUM-ONLY`
- `EDGE-METRIC-QUALIFIED`
- `THICKNESS-QUALIFIED`
- `COMPOSITION-MODEL-QUALIFIED`
- `MAP-QUALIFIED`
- `PREPOST-ANNEAL-COMPARABLE`
- `DEVICE-CORRELATED`

`DEVICE-CORRELATED` requires P11 detector-response data linked to a known P06 material coordinate/genealogy.

---

# Remaining high-value OPEN items

Historical:

- whether RP-01 supplier/UWA used FTIR for `x≈0.30`;
- how `9.5 µm` was measured;
- exact RP-01/UWA material spectrometer and optical configuration;
- source/beamsplitter/detector/path/resolution/coadds;
- whether the material was spatially mapped;
- exact material measurement temperature;
- exact model used to label x;
- exact detector-response cutoff convention for `4.4 µm`;
- same-material coordinate linking optical material state to the Figure-3/5/6/7 detector;
- primary PDF line resolving the Gopal 1992 thickness-unit conflict.

Local qualification:

- wavenumber-axis uncertainty;
- physical sample-plane beam footprint;
- x-y registration/repeatability;
- full optical-stack model/version;
- d_FTIR vs independent d_physical calibration;
- x-model systematic uncertainty;
- final map density;
- process limits after repeated LPE/device correlation.

---

# Negative-search record

No direct primary source was recovered this round showing that the RP-01 `x≈0.30` or `9.5 µm` values came from an FTIR measurement.

No direct late-1990s UWA FTIR traveler tied to the Figure-3/5/6/7 detector was recovered.

“Not recovered” does not mean absent.

---

# Strongest next empirical round

Proceed with **Round 33: singulation / dicing / die-edge damage / package-ready die preparation**.

Rationale: P33 still lists the RP-01 die separation method as historical OPEN, while the end-to-end manual currently has no controlled operation between processed wafer/coupon and package-ready die.

Audit first:

- `P15_DIE_ATTACH_INTERCONNECT_CRYOGENIC_PACKAGE_QUALIFICATION.md`;
- `P33_CRYOGENIC_DIE_ATTACH_INTERCONNECT_EMPIRICAL_PROCESS_WINDOW.md`;
- `P16_MASTER_END_TO_END_PROCESS_TRAVELER.md`;
- P18 failure atlas for edge-crack/damage signatures.

Then search primary HgCdTe/CdZnTe detector fabrication papers, patents, theses and vendor/institutional process records for:

- saw versus scribe/cleave/lap routes;
- blade type/grit/thickness;
- spindle speed/feed/depth;
- coolant/cleaning compatibility with HgCdTe/CdZnTe/Cr-Au/anodic oxide;
- protective coatings/tapes;
- street/kerf dimensions;
- edge chipping/subsurface damage;
- post-dice cleaning/drying;
- contamination/particle control;
- die handling/pickup;
- edge-to-active-region exclusion;
- pre/post-singulation electrical/noise/optical qualification;
- cryogenic survival after singulation.

Create a new top-level empirical module only if this is truly a missing process operation; unlike Rounds 28–32, singulation appears to be a genuine end-to-end fabrication gap.

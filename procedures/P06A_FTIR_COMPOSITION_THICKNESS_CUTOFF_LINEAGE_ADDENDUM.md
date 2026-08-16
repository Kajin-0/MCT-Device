# P06A — FTIR composition / thickness / optical-edge / detector-cutoff lineage addendum

**Status:** CONTROLLED EMPIRICAL METROLOGY LINEAGE / HISTORICAL RP-01 FTIR APPARATUS OPEN. Supplements `P06_FTIR_COMPOSITION_THICKNESS_MAPPING.md`.

**Date:** 2026-08-16 America/New_York

## 1. Purpose

Convert the already adequate P06 transmission SOP into a more empirical execution and provenance layer without creating a duplicate top-level spectroscopy procedure.

The central requirement is to keep four physically different quantities separate:

`{d_physical, E_g/x_optical, lambda_optical_edge, lambda_detector_cutoff}`.

They can correlate strongly, but they are not interchangeable measurements.

---

## 2. Evidence classes

- `DIRECT-RP01` — directly reported by Smith et al. 2001.
- `PRIMARY-HGCDTE-LPE-OPTICAL` — primary HgCdTe transmission/absorption studies directly applicable to LPE or bulk material.
- `PRIMARY-HGCDTE-MAPPING-TRANSFER` — primary automated FTIR/microscope mapping studies; apparatus/method transfer only unless the material branch matches.
- `PRIMARY-HGCDTE-BANDGAP` — empirical band-gap/composition model papers.
- `SAME-UWA-OPTICAL-CONTEXT` — UWA work showing infrared transmission as a material-characterization tool but not closing the RP-01 FTIR traveler.
- `DERIVED-CONSISTENCY` — calculations made from published equations/data; never historical apparatus facts.
- `LOCAL-QUAL` — locally frozen apparatus/model state validated against independent standards/metrology.

---

## 3. RP-01 direct optical/material state

Smith et al. 2001 directly provide:

- starting material described as approximately `x≈0.30`;
- LPE n-HgCdTe on electrically insulating CdZnTe;
- active layer thickness `9.5 µm`;
- detector spectral responsivity at `80 K`, `10 V/cm`, stated `60° FOV`;
- experimental detector cutoff wavelength stated as `4.4 µm`.

The paper does **not** disclose a material FTIR measurement used to obtain either the `x≈0.30` label or `9.5 µm` thickness.

Therefore the following remain `OPEN-HISTORICAL` for RP-01:

- FTIR instrument/model;
- source/beamsplitter/detector;
- transmission versus reflection configuration;
- sample temperature;
- spectral range/resolution;
- aperture/spot size;
- reference/background method;
- number of scans/coadds;
- purge/vacuum state;
- optical model;
- exact definition used for material composition;
- independent thickness reference method.

Do not write that RP-01 used FTIR unless documentary evidence is recovered.

---

## 4. Permanent quantity-separation rule

Every optical/material data record shall use explicit names.

### 4.1 Physical thickness

`d_physical`

obtained by a physical dimensional method such as cross-section microscopy or a calibrated step/profile method.

### 4.2 FTIR optical thickness

`d_FTIR`

obtained from a full optical-stack/interference fit.

### 4.3 Optical absorption edge

Examples:

- `lambda_50T` — 50% of a defined transmission plateau;
- `lambda_T-int` — tangent/zero-intercept transmission metric;
- `E_g,opt` — band-edge energy estimated from a declared absorption model.

### 4.4 Optical composition

`x_opt`

obtained from a stated absorption/transmission model or from a stated `E_g(x,T)` mapping.

### 4.5 Detector cutoff

`lambda_det,c`

obtained from detector responsivity/relative-response data under a declared convention.

No unqualified `lambda_c` is permitted in a controlled traveler.

---

## 5. Hansen equation — correct role and quantitative RP-01 consistency check

G. L. Hansen, J. L. Schmit and T. N. Casselman, *J. Appl. Phys.* 53, 7099–7101 (1982), DOI `10.1063/1.330018`, derived from data from 22 studies:

`E_g(x,T) = -0.302 + 1.93x - 0.810x^2 + 0.832x^3 + 5.35e-4 T(1-2x)` eV.

The paper reports validity over the full alloy-composition range and approximately `4.2–300 K`, with a standard error of estimate of about `0.013 eV`.

### 5.1 Interpretation rule

The `0.013 eV` is the standard error of the empirical global fit. It is **not**:

- an FTIR instrument uncertainty;
- a local uncertainty of every individual x estimate;
- a detector-cutoff uncertainty;
- permission to assign `±0.013 eV` independently to every point in a spatial map.

Separate model-form/systematic uncertainty from local measurement repeatability.

### 5.2 Derived RP-01 consistency branch

For `x=0.300`, `T=80 K`:

`E_g = 0.243684 eV`.

Using `hc = 1.239841984 eV µm` gives the **band-gap-equivalent wavelength**:

`lambda_g,eq = hc/E_g = 5.0879 µm`.

This is not the RP-01 detector cutoff.

If the published detector cutoff `4.4 µm` is deliberately but only hypothetically converted by `E=hc/lambda`, then:

`E_eq(4.4 µm) = 0.281782 eV`.

Inverting the Hansen relation at `80 K` gives approximately:

`x_Hansen,eq ≈ 0.3241`.

This ~0.024 difference in x is a **consistency warning**, not evidence that either historical number is erroneous.

Possible causes include:

- the `x≈0.30` label being approximate;
- detector cutoff convention differing from `hc/E_g`;
- finite layer thickness / wavelength-dependent absorption;
- longitudinal/lateral composition gradients;
- optical stack/reflection effects;
- different material locations or states;
- carrier/doping/defect effects on observed absorption edge;
- response normalization convention.

Permanent rule: **never infer an exact material x from an undefined detector cutoff.**

---

## 6. Hougen 1989 — LPE full-transmission-model lineage

C. A. Hougen, “Model for infrared absorption and transmission of liquid-phase epitaxy HgCdTe,” *J. Appl. Phys.* 66, 3763–3766 (1989), DOI `10.1063/1.344038`.

This is the primary model lineage already used by P06. Its value is that transmission is treated as an optical-stack/material problem rather than identifying one arbitrary spectral point with the energy gap.

P06A therefore retains full-spectrum fitting as the preferred route when the data support it.

Do not silently replace the Hougen/validated optical constants with a new library between lots.

---

## 7. Gopal–Ashokan–Dhar 1992 — edge metrics and composition-uniformity diagnostic

V. Gopal, R. Ashokan and V. Dhar, “Compositional characterization of HgCdTe epilayers by infrared transmission,” *Infrared Physics* 33, 39–45 (1992), DOI `10.1016/0020-0891(92)90053-V`.

Primary results:

- HgCdTe epilayers in approximately the `0.2<x<0.3` regime were modeled;
- room-temperature transmission was used;
- both the 50%-transmission frequency and a zero-intercept/cut-on metric were correlated with composition;
- disagreement between composition estimates from the two metrics was proposed as an indicator of compositional nonuniformity/grade.

### Source-text conflict retained

Current ScienceDirect index text renders the applicable thickness range as `10–30 mm`, which is physically inconsistent with the epilayer context and almost certainly an indexing/unit-rendering defect. An author/profile summary describes approximately `20–30 µm` epilayers.

Until the primary PDF line is directly recovered and checked, **do not freeze the thickness-validity interval from the index text**.

This is a provenance conflict, not a license to silently repair the paper.

---

## 8. Chang et al. 2005 — quantitative FTIR microscope mapping apparatus transfer

Y. Chang et al., “Composition and thickness distribution of HgCdTe molecular beam epitaxy wafers by infrared microscope mapping,” *J. Crystal Growth* 277, 78–84 (2005), DOI `10.1016/j.jcrysgro.2005.01.051`.

An author-uploaded primary full text exposes unusually useful apparatus detail:

- **Thermo Nicolet Centaur µs infrared microscope**;
- connected to a **Thermo Nicolet 870 FTIR spectrometer**;
- computerized `x-y` translation stage;
- stated positioning precision approximately `1 µm`;
- adjustable IR aperture down to approximately `25 µm` at `10 µm` wavelength;
- mapping aperture set to approximately `100 µm` to improve signal and throughput;
- transmissivity curves fitted automatically;
- composition extracted from the intrinsic absorption edge;
- thickness extracted by fitting the interference pattern below the intrinsic absorption region.

Example reported map performance includes:

- CdZnTe-substrate HgCdTe sample average `x≈0.2182`, `σ_x≈0.0006`;
- average thickness `≈7.84 µm`, `σ_d≈0.03 µm` for that example.

These are demonstration results from an MBE process, **not RP-01 acceptance limits**.

### P06A apparatus-transfer consequence

A locally executable mapping branch may use this as a strong method template:

`FTIR -> IR microscope -> calibrated aperture -> computerized x-y stage -> automatic full-spectrum fit -> x/thickness maps`.

Instrument equivalence is based on metrological output, not on matching Nicolet brand/model.

---

## 9. LPE-specific FTIR apparatus transfer — Murthy et al. 2009

O. V. S. N. Murthy et al., “Multicarrier conduction and Boltzmann transport analysis of heavy hole mobility in HgCdTe near room temperature,” *J. Appl. Phys.* 106, 113708 (2009), DOI `10.1063/1.3266015`.

This source is especially relevant because its sample C was:

- **LPE HgCdTe**;
- on `Cd0.96Zn0.04Te`;
- grown from a **Te-rich melt using a horizontal-slider setup**;
- followed by an in-situ Te-saturation anneal around `230 °C`.

For optical characterization:

- composition was estimated from the IR absorption spectrum at `300 K`;
- instrument: **Bruker IFS 66v/S FTIR**;
- the LPE epilayer was reported as `x=0.200`;
- thickness `34 µm` was estimated from FTIR interference fringes.

This is direct proof that the `300 K absorption + interference-fringe thickness` workflow is used on a physically relevant Te-rich horizontal-slider LPE/CdZnTe branch.

It is still transfer evidence, not RP-01 apparatus identity.

---

## 10. Evacuated FTIR / detector / beamsplitter transfer example

F.-Y. Yue et al., “Optical characterization of defects in narrow-gap HgCdTe for infrared detector applications,” *Chinese Physics B* 28, 017104 (2019), DOI `10.1088/1674-1056/28/1/017104`, reports optical absorption measurements using:

- Bruker IFS 66v/S;
- KBr beamsplitter;
- liquid-nitrogen-cooled HgCdTe detector;
- evacuated spectrometer path to suppress atmospheric absorption.

This gives direct apparatus evidence for one successful HgCdTe absorption branch.

The paper also used a brief `1% Br2/methanol` surface treatment before its optical experiment. That surface treatment belongs to that material/experiment and shall **not** be imported automatically into RP-01 P06 because surface preparation itself can alter the measured optical state and downstream process genealogy.

---

## 11. Instrument-state vector for local P06 transfer

Record the full state:

`X_FTIR = {instrument, source, beamsplitter, detector, path vacuum/purge, spectral range, resolution, apodization, phase correction, aperture/spot, incidence geometry, scan count, scan speed, background/reference, sample T, x-y registration, surface state, model/version}`.

The minimum output vector is:

`Y_FTIR = {raw T(nu), QC metrics, lambda_50T, lambda_T-int where used, E_g,opt, x_opt, d_FTIR, gradient/model state, residuals, uncertainties, map coordinates}`.

---

## 12. Wavenumber-axis qualification

Composition extraction is strongly sensitive to edge location. Therefore instrument wavelength/wavenumber calibration must be independently checked.

Local procedure shall record:

- calibration standard/reference method;
- residual wavenumber error over the edge region;
- repeatability after instrument restart/configuration change;
- whether the sample and reference used the same optical path configuration.

Do not assume the nominal FTIR laser calibration alone satisfies the final x uncertainty requirement without verification.

---

## 13. Aperture and spatial-map qualification

A nominal `100 µm aperture` is not automatically a `100 µm spatial resolution` at the sample.

Measure or bound:

- projected aperture/beam footprint at the sample plane;
- diffraction/optical blur versus wavelength;
- stage repeatability and backlash;
- sample rotation/coordinate registration;
- edge exclusion;
- beam clipping at wafer/coupon boundaries.

For pre/post-anneal comparison, map points shall be re-registered physically, not merely by nominal stage coordinates.

---

## 14. CdZnTe substrate and interface handling

The optical model must include the actual substrate/interface state.

Primary HgCdTe/CdZnTe work shows that degraded interfaces/Hg in-diffusion can reduce below-gap transmission and eliminate or degrade interference fringes. Therefore loss of fringe contrast is not automatically an FTIR-instrument failure.

If fringe quality changes materially, investigate:

- substrate transmission;
- interface quality;
- Hg in-diffusion;
- roughness/scattering;
- free-carrier absorption;
- surface films;
- thickness/grade complexity.

Do not force a thickness result from weak/absent fringes.

---

## 15. Thickness release hierarchy

For a new local implementation:

1. obtain `d_FTIR` from a full optical/interference fit;
2. retain adjacent-fringe spacing as a diagnostic only;
3. cross-check representative samples against `d_physical`;
4. model bias versus thickness/composition/surface condition;
5. release FTIR thickness only over the calibrated range.

The textbook relation

`d ≈ 1/(2 n_g Delta_nubar)`

is useful for screening, but is not the final production estimator unless dispersion and stack effects are shown negligible at the required uncertainty.

---

## 16. Edge / composition release hierarchy

For every measured location store at least:

- raw transmission spectrum;
- a simple traceable edge metric (`lambda_50T` or equivalent);
- full-fit composition `x_opt`;
- full-fit residual/model state;
- sample temperature.

When two edge metrics produce incompatible x estimates, classify the point as a possible grade/model inadequacy rather than averaging the x values.

---

## 17. Defect/doping warning near the optical edge

Optical edge position and shape are not functions of alloy composition alone. Primary HgCdTe optical work shows sensitivity to:

- doping/Fermi level;
- defects;
- band filling / Burstein-Moss effects where relevant;
- Urbach/tail behavior;
- anneal-induced defect-state changes.

Therefore a pre/post-anneal spectral shift is not automatically a change in x.

The release decision must consider Hall state from P05 and the complete anneal genealogy from P04/P31.

---

## 18. Relationship to detector cutoff

Detector spectral response from P11 is a system/device quantity.

For a finite-thickness photoconductor, detector response can depend on:

- absorption coefficient versus wavelength;
- physical thickness;
- optical reflections;
- carrier collection and recombination;
- contact/sweepout state;
- normalization convention;
- readout frequency.

Therefore P06 shall compare `x_opt`, `E_g,opt` and defined optical-edge metrics against `lambda_det,c`, but shall never make them equal by definition.

The final empirical correlation should be learned from locally fabricated devices:

`{x_opt, d_FTIR, edge shape, gradient} -> spectral responsivity / lambda_det,c`.

---

## 19. P06A release labels

Use one of:

- `RAW-SPECTRUM-ONLY`
- `EDGE-METRIC-QUALIFIED`
- `THICKNESS-QUALIFIED`
- `COMPOSITION-MODEL-QUALIFIED`
- `MAP-QUALIFIED`
- `PREPOST-ANNEAL-COMPARABLE`
- `DEVICE-CORRELATED`

A wafer/coupon can hold multiple labels simultaneously.

No `DEVICE-CORRELATED` claim is allowed until P11 detector-response data are linked to known P06 coordinates/material genealogy.

---

## 20. Remaining historical gaps

Still `OPEN-HISTORICAL` for RP-01:

- whether supplier/UWA used FTIR at all for the quoted `x≈0.30`;
- exact source of the `9.5 µm` thickness;
- exact supplier composition definition;
- FTIR hardware/configuration;
- material measurement temperature;
- optical constants/model;
- spectral resolution/range;
- aperture and map position;
- whether material was spatially mapped;
- exact spectral-response cutoff convention used to call the detector `4.4 µm`.

---

## 21. Primary references

1. E. P. G. Smith et al., *Semicond. Sci. Technol.* 16, 455–462 (2001), DOI `10.1088/0268-1242/16/6/306`.
2. G. L. Hansen, J. L. Schmit, T. N. Casselman, *J. Appl. Phys.* 53, 7099–7101 (1982), DOI `10.1063/1.330018`.
3. C. A. Hougen, *J. Appl. Phys.* 66, 3763–3766 (1989), DOI `10.1063/1.344038`.
4. V. Gopal, R. Ashokan, V. Dhar, *Infrared Physics* 33, 39–45 (1992), DOI `10.1016/0020-0891(92)90053-V`.
5. J. H. Chu, B. Li, K. Liu, D. Tang, *J. Appl. Phys.* 75, 1234–1235 (1994), DOI `10.1063/1.356464`.
6. Y. Chang et al., *J. Crystal Growth* 277, 78–84 (2005), DOI `10.1016/j.jcrysgro.2005.01.051`.
7. O. V. S. N. Murthy et al., *J. Appl. Phys.* 106, 113708 (2009), DOI `10.1063/1.3266015`.
8. F.-Y. Yue et al., *Chinese Physics B* 28, 017104 (2019), DOI `10.1088/1674-1056/28/1/017104`.

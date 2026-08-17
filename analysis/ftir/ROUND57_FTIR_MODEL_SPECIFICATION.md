# Round-57 FTIR model specification

**Status:** publication-level model/record specification; not a replacement for the primary Hougen implementation or coefficient tables.

## Purpose

Close ambiguity in the empirical-protocol publication about the depth coordinate, composition-gradient parameter and model identity required for reproducible full-spectrum HgCdTe transmission fitting.

Primary model lineage remains C. A. Hougen, “Model for infrared absorption and transmission of liquid-phase epitaxy HgCdTe,” *Journal of Applied Physics* 66, 3763–3766 (1989), DOI `10.1063/1.344038`, plus controlled later extensions where explicitly declared.

## Coordinate convention

For an HgCdTe layer of physical/fit thickness `d` on CdZnTe:

- `z=0` at the HgCdTe/CdZnTe interface;
- `z=d` at the free HgCdTe surface.

The Round-57 first-order composition profile is

`x(z) = x0 + g (z/d - 0.5)`.

Therefore:

- `x0` is the layer-midplane composition under this parameterization;
- `x_interface = x0 - g/2`;
- `x_surface = x0 + g/2`;
- `g = x_surface - x_interface`.

Positive `g` means Cd fraction increases from substrate interface toward the free surface.

## Optional unresolved lateral/nonuniform composition parameter

Round 57 may include an optional `s_x` representing the standard deviation of a Gaussian unresolved composition distribution used to smear/average the local optical response when justified by spectral residuals.

Important provenance rule:

`SYN-MANUAL-PARAMETER`: the symbol and exact Gaussian implementation `s_x` are a Round-57 manual choice. Do not cite `s_x` as Hougen’s original notation unless the primary source explicitly supports that claim.

Do not activate `s_x` merely to improve numerical fit quality. Compare residual structure, parameter identifiability and information criteria/model-validation diagnostics.

## Optical-stack requirements

The implemented forward model shall declare at minimum:

- HgCdTe complex refractive index / absorption model as a function of wavelength, composition and temperature;
- CdZnTe substrate optical constants/source;
- front-surface reflection;
- HgCdTe/CdZnTe interface reflection;
- coherent treatment of the thin HgCdTe layer sufficient to model Fabry–Pérot fringes;
- declared treatment of the thick substrate/back-surface coherence;
- incidence angle/polarization convention;
- instrument line-shape convolution where material;
- atmospheric/purged spectral regions included/excluded;
- any free-carrier absorption term and its source;
- any surface film/oxide term if included.

## Fit objective

Reference weighted least-squares form:

`chi2(theta) = sum_i [(T_meas_i - T_model_i(theta))/sigma_T_i]^2`.

The run record shall state:

- fitted spectral interval(s);
- excluded atmospheric/artifact intervals;
- weighting/noise model used to obtain `sigma_T_i`;
- parameter bounds and fixed parameters;
- optimizer/solver;
- convergence criterion;
- initial conditions or multi-start scheme;
- residual diagnostics.

## Minimum fit outputs

- `x0` and 95% interval;
- `g` and 95% interval if a graded model is justified;
- `s_x` and interval if activated;
- `d_FTIR` and interval;
- full covariance/correlation matrix or equivalent posterior covariance representation;
- residual/RMSE/weighted objective;
- independent edge descriptors such as `lambda_50T`;
- model comparison result when choosing uniform vs graded/smeared models.

## Beam footprint and mapping

For every map point record:

- measured/projected aperture/beam footprint at the sample;
- wavelength dependence if significant;
- x-y stage coordinate;
- edge exclusion/beam-clipping check;
- sample orientation relative to LPE slider/growth direction.

No point may be accepted if a material fraction of the beam footprint lies outside the intended HgCdTe region unless the forward model explicitly represents that geometry.

## Independent thickness closure

During qualification, compare `d_FTIR` with a physical reference on representative material (profilometric step, cross-section microscopy, or another traceable method).

Store:

`Delta d = d_FTIR - d_physical`

with measurement uncertainties and repeatability.

## Reproducibility / archival identity

A real FTIR result is incomplete unless the exact model state is archived.

The data record shall include:

- repository path to forward-model implementation;
- repository commit or version;
- SHA-256 of the actual implementation file(s) used;
- repository path/version/SHA-256 of optical-constant/coefficient files;
- instrument method/export version;
- raw spectrum file checksum;
- fit configuration file/checksum;
- environment/dependency version if numerical output depends materially on it.

Do not write only “Hougen model” in a run record; that is not enough to reproduce a specific numerical inversion.

## Interpretation boundary

- `d_FTIR`, `x_opt`, `g`, `s_x`, `lambda_50T`, and detector cutoff are distinct outputs.
- Hansen `Eg(x,T)` may be used as a consistency mapping, not as a replacement for the declared transmission forward model.
- The RP-01 ~4.4-µm detector response cutoff is not the same quantity as the ~5.09-µm band-gap-equivalent wavelength calculated for x=.30 at 80 K.
- Model-form uncertainty and the Hansen global-fit error are not instrument repeatability and shall not be collapsed into one scalar without a declared propagation model.
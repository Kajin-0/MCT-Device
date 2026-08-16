# P06A — FTIR composition/thickness/edge qualification register

**Status:** CONTROLLED LOCAL QUALIFICATION RECORD. Use with `P06_FTIR_COMPOSITION_THICKNESS_MAPPING.md` and `P06A_FTIR_COMPOSITION_THICKNESS_CUTOFF_LINEAGE_ADDENDUM.md`.

## A. Sample identity

- Sample / wafer / coupon ID:
- Growth run / source genealogy:
- LPE branch / apparatus:
- CdZnTe substrate lot / composition / face / polarity / miscut:
- HgCdTe nominal x:
- HgCdTe nominal thickness:
- As-grown / annealed / processed state:
- P04/P31 anneal genealogy ID if applicable:
- Front surface state:
- Back surface state:
- Coating/passivation present:
- Measurement side:
- Orientation relative to slider/growth direction:

## B. Instrument-state vector

- FTIR manufacturer/model/serial:
- IR microscope/accessory:
- Source:
- Beamsplitter:
- Detector:
- Optical path: vacuum / dry purge / ambient:
- Pressure or purge condition:
- Spectral range:
- Spectral resolution:
- Apodization:
- Phase correction:
- Scan speed / mirror velocity:
- Number of scans/coadds:
- Background/reference acquisition ID:
- Background age/time separation from sample:
- Sample temperature:
- Temperature uncertainty:
- Incidence geometry:
- Nominal aperture:
- Measured/projected sample-plane footprint:
- Stage model:
- Stage positioning resolution:
- Measured repeatability/backlash:
- Method/software version:

## C. Wavenumber-axis qualification

- Calibration standard/method:
- Calibration date:
- Edge-region residual error:
- Repeat measurement after restart/configuration change:
- PASS / REVIEW / FAIL:

Rule: do not treat nominal instrument laser accuracy as the full composition uncertainty unless verified for the actual configuration.

## D. Spatial-coordinate qualification

- Sample fiducials used:
- Coordinate origin:
- Rotation relative to stage axes:
- Re-registration uncertainty:
- Edge exclusion:
- Beam clipping check:
- Map grid / point count:
- PASS / REVIEW / FAIL:

## E. Raw spectral QC per map point

For every point store:

- x coordinate [mm]:
- y coordinate [mm]:
- raw interferogram retained? Y/N
- raw transmission spectrum file:
- `T_max` and baseline window:
- absorbed-region floor/noise:
- transparent-region RMS noise:
- atmospheric residual metric:
- fringe contrast:
- usable fringe count:
- edge slope:
- saturation/clipping flag:
- anomaly/scattering flag:
- raw-spectrum disposition:

## F. Traceable edge metrics

- `lambda_50T` [µm]:
- `nubar_50T` [cm^-1]:
- baseline/Tmax definition:
- `lambda_T-int` [µm], if used:
- tangent/fit range:
- other edge metric and definition:

Do not enter an unqualified `lambda_c`.

## G. Optical thickness

- Optical-stack model/version:
- HgCdTe refractive-index source/version:
- CdZnTe optical constants source/version:
- Fit spectral interval:
- `d_FTIR` [µm]:
- fit statistical uncertainty:
- fit residual/RMSE:
- simple fringe-spacing screening estimate:
- number of fringes used:
- physical reference method:
- `d_physical` [µm]:
- physical-reference uncertainty:
- `d_FTIR - d_physical` [µm]:
- thickness disposition:

If fringes are weak/absent, classify `THICKNESS-NOT-QUALIFIED`; do not force a fit.

## H. Optical composition / band edge

- Absorption model/version:
- `E_g,opt` [eV]:
- `x_opt`:
- fit temperature:
- composition-gradient model:
- gradient parameter(s):
- fit residual:
- covariance/confidence statement:
- Hansen comparison x, if used:
- Hansen equation/version:
- model-form/systematic uncertainty statement:

Rule: the Hansen global-fit standard error is not the local FTIR repeatability.

## I. Edge-model consistency

- x from 50%-transmission method:
- x from tangent/zero-intercept method:
- full-fit x:
- difference among methods:
- within qualified consistency band? Y/N
- if no: grading / defects / optical-model investigation opened? Y/N

Do not average incompatible x estimates to create an apparently precise number.

## J. Substrate/interface/fringe diagnosis

- Substrate transmission reference measured? Y/N
- Interface/scattering anomaly:
- Evidence for Hg in-diffusion:
- Free-carrier absorption concern:
- Surface-film concern:
- Fringe loss relative to baseline:
- independent microscopy/EDS/SIMS evidence if available:
- disposition:

## K. Pre/post-anneal matched-point comparison

If applicable:

- Pre-anneal spectrum ID:
- Post-anneal spectrum ID:
- Physical re-registration method:
- `Delta lambda_50T`:
- `Delta E_g,opt`:
- `Delta x_opt`:
- `Delta d_FTIR`:
- Hall-state change from P05:
- Surface-state change:
- Difference exceeds combined measurement repeatability? Y/N
- Composition change actually justified? Y/N
- Alternative mechanisms considered:

A spectral edge shift alone does not prove composition changed.

## L. Detector-correlation identity

If device data exist:

- Device ID:
- P06 map coordinate / material genealogy:
- P11 spectral-responsivity dataset:
- Detector temperature:
- Detector cutoff definition:
- `lambda_det,c` [µm]:
- `lambda_50T` [µm]:
- `E_g,opt` [eV]:
- `x_opt`:
- `d_FTIR` [µm]:
- Same physical material location reasonably established? Y/N

Do not correlate unrelated wafer positions as though they were the same material state.

## M. RP-01 consistency branch — calculation only

For reference, not historical reconstruction:

- Hansen `x=0.300`, `T=80 K` -> `E_g=0.243684 eV` -> `lambda_g,eq=5.0879 µm`.
- RP-01 published detector cutoff `4.4 µm` -> `hc/lambda=0.281782 eV` -> Hansen-equivalent `x≈0.3241` at 80 K.

Classification: `DERIVED-CONSISTENCY`. Never write this as the measured RP-01 material composition.

## N. Qualification labels

Check all that apply:

- [ ] `RAW-SPECTRUM-ONLY`
- [ ] `EDGE-METRIC-QUALIFIED`
- [ ] `THICKNESS-QUALIFIED`
- [ ] `COMPOSITION-MODEL-QUALIFIED`
- [ ] `MAP-QUALIFIED`
- [ ] `PREPOST-ANNEAL-COMPARABLE`
- [ ] `DEVICE-CORRELATED`

## O. Historical reconstruction fields

Current RP-01 status:

- Exact FTIR apparatus: `OPEN-HISTORICAL`
- Exact source of x≈0.30: `OPEN-HISTORICAL`
- Exact source of 9.5-µm thickness: `OPEN-HISTORICAL`
- Exact detector cutoff convention for 4.4 µm: `OPEN-HISTORICAL`

Any future documentary closure shall identify the source and evidence class before these are changed.

## P. Final disposition

- PASS / REVIEW / FAIL:
- Primary reason:
- Deviations:
- CAPA / follow-up:
- Analyst:
- Date:

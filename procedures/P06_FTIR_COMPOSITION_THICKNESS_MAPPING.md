# P06 — FTIR transmission mapping for HgCdTe composition, thickness, and longitudinal uniformity

**Status:** `CONTROLLED-QUALIFICATION-METROLOGY` — suitable for LPE/anneal process development; final RP-01 production limits and the selected full-spectrum optical model remain qualification items.

**Purpose:** Use non-destructive infrared transmission to measure and map the optical absorption edge, HgCdTe epilayer thickness, and evidence of longitudinal/spatial composition nonuniformity before detector fabrication.

P06 is a required material gate after P03 LPE and before/after P04 Hg-overpressure annealing.

---

## 1. Quantities that must remain distinct

The manual shall not use the word “cutoff” without a subscript/definition.

P06 distinguishes at least:

1. **transmission-edge metric** — a wavelength or wavenumber defined directly from the measured transmission spectrum;
2. **optically inferred band gap** `E_g,opt` — obtained from a stated absorption/transmission model;
3. **optically inferred alloy composition** `x_opt` — obtained from a stated `E_g(x,T)` or full transmission model;
4. **detector spectral-response cutoff** `λ_det` — obtained only after device fabrication from responsivity/relative-response data under a separately defined convention.

These are related but are not interchangeable.

---

## 2. RP-01 consistency issue that motivates the distinction

RP-01 describes the Fermionics starting material as approximately `x≈0.30` and reports detector response with a spectral cutoff around `4.4 µm` at `80 K`.

Using the Hansen–Schmit–Casselman empirical band-gap relation as a consistency calculation:

`E_g(x,T) = -0.302 + 1.93x - 0.810x² + 0.832x³ + 5.35×10^-4 T(1-2x)` eV.

At `x=0.30`, `T=80 K`:

- `E_g≈0.243684 eV`;
- `hc/E_g≈5.09 µm`.

Thus the nominal composition and detector-response “cutoff” should not be forced into equality.

Possible reasons include:

- `x≈0.30` is approximate;
- detector cutoff convention differs from `hc/E_g`;
- finite absorption thickness changes the spectral edge;
- composition grading affects transmission/response;
- optical stack/reflections alter measured spectral shape;
- supplier and detector measurements may refer to different positions/wafer states.

**P06 rule:** preserve each measured quantity and its convention; do not back-calculate a supposedly exact `x` from an undefined detector cutoff.

---

## 3. Primary optical-model lineage

### 3.1 Hougen 1989

C. A. Hougen, *Journal of Applied Physics* 66, 3763–3766 (1989), DOI `10.1063/1.344038`, developed a room-temperature IR absorption/transmission model for LPE HgCdTe.

The model explicitly treats:

- detector/epilayer thickness;
- composition profile;
- surface nonuniformity;
- detector-back reflections;
- empirical absorption coefficient.

A key result is that composition profile and photoconductive relative response can be predicted from room-temperature transmission data without arbitrarily equating a chosen spectral point to the band gap.

### 3.2 Composition/thickness extraction literature

Subsequent primary studies demonstrate:

- empirical extraction of composition from defined IR transmission edge metrics for HgCdTe epilayers;
- use of Fabry–Pérot/interference fringes below the absorption edge to infer epilayer thickness;
- computerized full-spectrum fitting to map both composition and thickness;
- extension of transmission fitting to longitudinal composition-profile parameters.

P06 therefore uses **full-spectrum fitting as the preferred method**, with simple edge metrics retained as traceable QC descriptors rather than the sole composition estimator.

---

## 4. Sample requirements

Record before measurement:

- sample/wafer ID;
- growth-run ID;
- substrate material and lot;
- nominal CdZnTe composition;
- HgCdTe nominal `x`;
- nominal layer thickness;
- anneal state: as-grown / annealed / process step;
- front/back surface condition;
- any coating/passivation present;
- sample orientation and dimensions;
- measurement-side convention.

For P03/P04 process control, transmission should preferably be measured on bare material before device patterning.

---

## 5. FTIR equipment capability

Minimum required capability for the RP-01 MWIR material branch:

- Fourier-transform infrared spectrometer covering the absorption edge and a sufficiently broad transparent region below the edge;
- room-temperature measurement capability;
- microscope/beam aperture small enough to support spatial mapping on the selected substrate size;
- calibrated wavenumber scale;
- purge or vacuum optical path adequate to suppress atmospheric H2O/CO2 structure in the fit region;
- detector/beamsplitter combination with adequate SNR over the selected spectral range;
- reference/background acquisition without the sample;
- raw interferogram or minimally processed spectrum retained where instrument permits.

### Initial qualification spectral range

For x≈0.30 MWIR HgCdTe, an initial range spanning approximately

`500–5000 cm^-1` (`20–2 µm`)

is recommended so that both the low-energy interference region and absorption edge are captured.

This range is a P06 engineering selection, not an RP-01 published instrument setting.

### Initial qualification resolution

Use spectral resolution `≤4 cm^-1` for process qualification unless a sensitivity study demonstrates that coarser resolution does not materially change fitted x/thickness.

Primary optical work on HgCdTe commonly uses single-digit-cm^-1 resolution; P06 requires the exact resolution to be recorded with every spectrum.

---

## 6. Instrument qualification before wafer data

Before accepting P06 data:

1. verify wavenumber calibration using the instrument's traceable/reference procedure;
2. acquire background/reference spectrum;
3. verify detector is not saturated in the high-transmission region;
4. verify no clipping/zeroing of negative or >100% processed transmission values occurs silently;
5. repeat the same reference specimen at least three times;
6. determine repeatability of:
   - selected edge metric;
   - fitted thickness;
   - fitted x;
7. store the resulting repeatability as the instrument contribution to the P06 uncertainty budget.

Do not set production x tolerances smaller than demonstrated measurement repeatability.

---

## 7. Spatial mapping geometry

P06 uses a normalized wafer coordinate system so data remain comparable across different substrate sizes.

For a development wafer/coupon large enough to support mapping, use at minimum:

- center;
- four quadrant/diagonal interior points;
- four near-edge interior points;

for a **9-point minimum map**.

For LPE process qualification, a `5×5` or denser rectangular grid is preferred when beam size permits.

Record for every point:

- physical x–y coordinate in mm;
- normalized x–y coordinate;
- beam/aperture diameter;
- edge exclusion;
- orientation relative to growth/slider direction.

The same coordinates should be reused before and after annealing whenever feasible.

---

## 8. Acquisition sequence at each map point

For each point:

1. move to recorded x–y coordinate;
2. verify aperture lies fully on usable material;
3. acquire transmission spectrum using the frozen instrument method;
4. record sample temperature;
5. store raw spectrum before any model fitting;
6. visually/algorithmically inspect atmospheric lines, saturation, channel fringes, and discontinuities;
7. repeat acquisition if QC fails;
8. fit only after raw-spectrum acceptance.

The number of coadds/scans shall be selected during instrument qualification to achieve the required repeatability and then frozen in the measurement method. It shall not be changed ad hoc between map points without recording the change.

---

## 9. Raw spectral QC metrics

For every accepted spectrum calculate/store:

- maximum transmission `T_max` in a defined low-absorption window;
- minimum/noise-floor transmission in the strongly absorbed region;
- local RMS spectral noise in at least one transparent window;
- atmospheric-line residual metric where relevant;
- fringe contrast;
- number of resolvable fringes used for thickness fit;
- edge slope metric;
- fit residual after modeling.

A spectrum with insufficient fringe contrast may still support an edge metric but cannot be assigned a high-confidence optical thickness without an alternate thickness measurement.

---

## 10. Traceable transmission-edge descriptors

At minimum report one normalized transmission edge descriptor independent of the full fit.

Recommended descriptor:

`λ_50T` = wavelength where transmission on the absorption edge equals `0.5 T_max`, with `T_max` and the baseline window explicitly defined.

Also record the same point in wavenumber:

`νbar_50T = 1/λ_50T` with consistent units.

If a zero-intercept/tangent method is used, record it separately as `λ_T-int` or equivalent.

Do not call either quantity simply `λ_c`.

---

## 11. Thickness extraction from interference fringes

Uniform LPE HgCdTe on an IR-transparent substrate commonly produces Fabry–Pérot fringes in the low-absorption region.

A first-order normal-incidence relation is

`Δνbar ≈ 1/(2 n_g d)`

where `d` is layer thickness and `n_g` is the appropriate dispersive/group optical index over the interval.

Because HgCdTe refractive index is dispersive and the substrate/interface reflections matter, **P06 does not release thickness using this simple equation alone**.

Preferred method:

- fit the measured transparent-region interference pattern with a transfer/transmission model that includes layer refractive index, substrate, reflections, and thickness;
- obtain `d_FTIR` and fit uncertainty;
- retain fringe spacing as an independent diagnostic.

---

## 12. Independent thickness calibration

During P03 process development, FTIR thickness shall be cross-checked against an independent physical method on representative sacrificial coupons.

Preferred references:

- stylus profilometry across a deliberate etched/cleaved layer step;
- calibrated cross-sectional microscopy;
- another traceable thickness method with stated uncertainty.

For each qualification lot calculate:

`Δd = d_FTIR - d_reference`.

Release the FTIR thickness model only after bias and repeatability are quantified across the expected 5–15 µm thickness range.

RP-01 target reference thickness is approximately `9.5 µm`.

---

## 13. Full-spectrum composition fit

The preferred P06 composition analysis fits the entire relevant transmission spectrum rather than converting one edge point directly to x.

The model should, at minimum, represent:

- absorption coefficient versus photon energy/composition/temperature;
- epilayer thickness;
- front/back reflection;
- substrate transmission/refraction;
- Fabry–Pérot interference;
- selected composition-profile parameterization;
- instrumental spectral resolution/convolution where material.

Candidate model lineage: Hougen 1989 plus later validated extensions for HgCdTe LPE transmission.

### Fit outputs

Store at minimum:

- fitted surface/representative composition `x_opt`;
- fitted thickness `d_FTIR`;
- composition-gradient parameter(s), if justified by data;
- model residual/RMSE;
- covariance/confidence interval where available;
- fit spectral range;
- fixed model parameters and their source/version.

Do not allow the fitting software to change optical constants or empirical coefficients silently between wafers.

---

## 14. Composition-gradient diagnostic

A single uniform-x layer model shall not be accepted automatically.

Escalate to a graded model when:

- absorption-edge shape cannot be fit within the qualified residual threshold;
- edge and fringe regions cannot be fit simultaneously;
- `x` inferred from different edge descriptors disagrees beyond measurement uncertainty;
- destructive depth profiling or growth history suggests grading;
- spectra from thinned samples of the same growth cannot be represented by a common composition model.

Primary HgCdTe transmission literature explicitly uses disagreement among edge metrics and full-spectrum fitting as indicators of longitudinal composition nonuniformity.

---

## 15. Hansen band-gap relation: allowed use

The Hansen relation is allowed as:

- an independent consistency calculation;
- a documented mapping from a separately estimated `E_g` to x;
- a temperature-normalization aid.

It shall not be used to define a detector-response cutoff by `λ=hc/E_g` without labeling that quantity as a **band-gap-equivalent wavelength**.

The 1982 Hansen relation has a reported standard error of approximately `0.013 eV`, which is substantial compared with the energy changes associated with small x shifts in MWIR HgCdTe. This model uncertainty must not be ignored when claiming very precise x from `E_g` alone.

---

## 16. Pre/post anneal comparison

P04 requires composition preservation.

For each matched point before and after Hg-overpressure anneal, compare:

- `λ_50T`;
- fitted `x_opt`;
- fitted thickness;
- edge-slope/gradient parameter;
- fit residual.

Use the same:

- instrument method;
- map coordinate;
- temperature;
- spectral resolution;
- optical model/version.

Report the observed shift and repeatability uncertainty separately.

A statistically significant shift in the optical edge is not automatically called a composition change until potential changes in free-carrier absorption, surface condition, interference model, and measurement registration have been considered.

---

## 17. LPE uniformity metrics

For each map report:

### Composition

- mean `x_opt`;
- standard deviation `σ_x`;
- min/max;
- peak-to-valley `Δx_PV`;
- spatial gradient along slider/growth direction;
- spatial gradient transverse to growth direction.

### Thickness

- mean thickness;
- standard deviation;
- min/max;
- peak-to-valley thickness;
- percentage nonuniformity under a stated formula.

### Edge metric

- mean `λ_50T`;
- standard deviation;
- min/max;
- peak-to-valley wavelength spread.

Do not quote “uniformity ±X%” without stating whether X means half-range/mean, standard deviation/mean, or another statistic.

---

## 18. Initial qualification acceptance philosophy

Final numerical RP-01 production limits are still open.

During process development, a material lot shall fail P06 if any of the following occur:

- no stable, reproducible absorption edge;
- thickness model cannot be reconciled with independent thickness metrology;
- gross spatial nonuniformity inconsistent with the intended detector geometry;
- isolated spectral anomalies suggesting inclusions, residual melt, delamination, or local thickness defects;
- post-anneal edge shift exceeding combined measurement repeatability without explanation;
- optical model residual indicates the chosen model is physically inadequate.

Statistical x/thickness limits will be released only after detector-performance sensitivity and repeated LPE capability are known.

---

## 19. Suggested development benchmark around RP-01

For a nominally `9.5 µm`, `x≈0.30` material lot:

- use `9.5 µm` only as the initial thickness center target;
- treat `x≈0.30` as a coarse supplier/reference composition rather than a ±0.001 specification;
- record actual P06 `x_opt`, `λ_50T`, and `d_FTIR` independently;
- do not force the fit to x=0.30 merely because RP-01 used that label.

The eventual canonical RP-01 reproduction target should be defined by the measured material state that yields the desired detector spectral response, not by an approximate historical composition label alone.

---

## 20. Data record

Every P06 spectrum/map must retain:

- sample/growth/anneal ID;
- instrument/method version;
- date/time/operator;
- sample temperature;
- spectral range/resolution;
- beamsplitter/detector/source configuration;
- aperture/spot size;
- scan/coadd count;
- background/reference ID;
- x–y coordinate;
- raw transmission data;
- normalized data;
- edge metrics;
- fringe metrics;
- fitted thickness;
- fitted composition/profile;
- fit residual;
- uncertainty/repeatability statement;
- PASS/FAIL/REVIEW disposition.

---

## 21. Release blockers

P06 remains qualification-level until closed:

1. exact FTIR hardware and detector/beamsplitter configuration;
2. frozen spectral range/resolution/coadd method;
3. calibrated spot size and spatial-coordinate registration;
4. selected optical-constant/absorption model and software implementation;
5. independent thickness calibration over the expected range;
6. quantified x/thickness fit repeatability;
7. composition-model systematic uncertainty;
8. production map density;
9. numerical uniformity limits;
10. numerical pre/post-anneal composition-shift limit;
11. relationship between P06 metrics and final detector spectral-response cutoff.

---

## 22. Primary references

1. C. A. Hougen, “Model for infrared absorption and transmission of liquid-phase epitaxy HgCdTe,” *Journal of Applied Physics* 66, 3763–3766 (1989), DOI `10.1063/1.344038`.
2. “Compositional characterization of HgCdTe epilayers by infrared transmission,” *Infrared Physics* 33, 39–45 (1992), DOI `10.1016/0020-0891(92)90053-V`.
3. “New method for the estimation of bulk HgCdTe composition by infrared transmission,” *Infrared Physics & Technology* 37, 445–450 (1996), DOI `10.1016/1350-4495(95)00125-5`.
4. Gu Renjie, Zhang Chuanjie, Yang Jianrong, Chen Xinqiang, Wei Yanfeng, “Evaluation of the Composition Profile of HgCdTe LPE Films by IR Transmission Spectrum,” *Journal of Semiconductors* 29, 534–538 (2008).
5. G. L. Hansen, J. L. Schmit, T. N. Casselman, “Energy gap versus alloy composition and temperature in Hg1−xCdxTe,” *Journal of Applied Physics* 53, 7099–7101 (1982), DOI `10.1063/1.330018`.

### Supporting thickness/uniformity literature

A later wafer-mapping study, DOI `10.1016/j.jcrysgro.2005.01.051`, demonstrates automated HgCdTe composition/thickness mapping using transmission-curve fitting and Fourier/interference information. Its MBE growth architecture differs from RP-01, so it is used for metrology methodology rather than process-transfer values.

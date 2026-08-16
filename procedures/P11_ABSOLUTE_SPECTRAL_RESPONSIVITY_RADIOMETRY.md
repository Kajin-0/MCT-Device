# P11 — Absolute spectral responsivity and low-background radiometry

**Status:** `CONTROLLED-QUALIFICATION-METROLOGY` — the measurement architecture, equations and traceability requirements are defined; the exact historical Optronics optical train, active-area convention, chopper/lock-in amplitude convention, calibration-detector chain, and final uncertainty limits remain qualification items.

**Purpose:** Measure the absolute voltage responsivity spectrum of the completed RP-01 photoconductor under controlled temperature, electric field, modulation frequency, field of view and optical background, with sufficient radiometric traceability to support quantitative NEP and D* calculations.

---

## 1. RP-01 direct measurement anchors

Smith et al. 2001 report spectral-response measurements using:

- Optronics Laboratories Spectral Response Measurement System `[P-RP01]`;
- detector temperature `80 K` `[P-RP01]`;
- electric field `10 V/cm` `[P-RP01]`;
- field of view `60°` `[P-RP01]`;
- chopping frequency `1 kHz` `[P-RP01]`;
- detector-response cutoff approximately `4.4 µm` `[P-RP01]`.

The paper also reports:

- BLIP `D*≈2.0×10^11 cm Hz^1/2 W^-1` at `4 µm`;
- nominal quantum efficiency `~70%`;
- 300-K/60° background photon flux approximately `1.0×10^15 cm^-2 s^-1`.

The exact historical spectral-system model/configuration, calibration standard, optical aperture geometry and signal-amplitude convention are not sufficiently closed by the RP-01 paper alone.

---

## 2. Measurement quantity

Define spectral **voltage responsivity** at wavelength `lambda` as

`R_v(lambda,f,E,T) = V_sig(lambda,f,E,T) / P_inc(lambda)`

with units

`V/W`.

Every reported responsivity must state:

- wavelength;
- modulation frequency;
- detector electric field;
- detector temperature;
- optical background/FOV;
- incident-power definition;
- signal-amplitude convention: RMS, peak, peak-to-peak, Fourier fundamental amplitude, etc.;
- whether voltage is measured directly at the detector or after a known gain stage.

A bare number in V/W without these conditions is incomplete.

---

## 3. Preferred metrological architecture

P11 uses a **spectral comparator** architecture consistent with NIST infrared detector metrology.

### Path A — direct spectral comparison to a calibrated transfer detector

At each wavelength:

1. monochromator produces a narrowband beam;
2. a NIST-traceable or equivalently calibrated reference detector measures the beam;
3. detector under test (DUT) is placed in the same defined optical plane;
4. DUT response/reference response ratio transfers absolute spectral responsivity.

For a reference detector with calibrated spectral power responsivity `R_ref(lambda)`:

`P_inc(lambda) = S_ref(lambda) / R_ref(lambda)`

where `S_ref` is the reference-detector electrical signal after all calibrated gains/conversions.

Then

`R_DUT(lambda) = S_DUT(lambda) / P_inc(lambda)`

or equivalently

`R_DUT(lambda) = [S_DUT(lambda)/S_ref(lambda)] R_ref(lambda)`

provided both signals refer to the same optical power and signal-amplitude convention.

### Path B — historical relative-spectrum + broadband absolute scaling

The 1989 low-background detector-radiometry lineage describes:

- a long-wave relative spectral-response system centered on an Optronics Laboratories model 735D triple-grating subtractive double monochromator covering approximately 2–30 µm;
- pyroelectric reference detectors to monitor relative spectral irradiance;
- absolute broadband low-background blackbody measurements;
- numerical integration combining relative response and calibrated broadband photon flux to obtain absolute spectral response.

This architecture is historically relevant to the RP-01-era Optronics measurement ecosystem.

P11 permits either architecture, but the chosen branch must be explicit and independently uncertainty-budgeted.

---

## 4. Modern traceability target

NIST's infrared spectral comparator facilities disseminate detector spectral responsivity over the relevant infrared range using calibrated transfer detectors and monochromator-based comparison.

The current NIST IR comparator architecture covers approximately `0.6–24 µm`, including the RP-01 3–5 µm region, and supports radiant-power/irradiance responsivity calibrations with percent-level expanded uncertainties depending on mode/wavelength.

### P11 requirement

The reference detector used to establish absolute spectral power shall have:

- calibration traceable to SI/NIST or equivalent national metrology institute;
- calibration certificate with wavelength grid and uncertainty;
- valid calibration date/history;
- known active area;
- documented spatial uniformity;
- documented modulation-frequency dependence or calibration performed at compatible frequency;
- adequate linearity at the incident power level.

Pyroelectric detectors are strong broadband transfer candidates because of relatively flat spectral response, but their response can depend on modulation frequency and thermal geometry; this must be included in the calibration transfer.

---

## 5. Spectral source / monochromator requirements

Minimum system:

- stable broadband IR source;
- monochromator covering at least the entire detector response band and out-of-band regions needed to verify rejection;
- order-sorting filters as required;
- reproducible entrance/exit slit geometry;
- chopper/modulator;
- beam-forming optics;
- reference/DUT substitution plane or calibrated beamsplitter-monitor geometry;
- purge/vacuum path where atmospheric absorption is material.

Record for every measurement method:

- source type and operating condition;
- monochromator make/model;
- grating used;
- slit widths/heights;
- spectral bandwidth;
- wavelength step;
- order-sorting filter;
- beam diameter/profile;
- purge/vacuum state;
- chopper location and frequency;
- reference-detector identity.

---

## 6. Wavelength calibration

Calibrate the monochromator wavelength scale using traceable/known spectral features or a qualified wavelength standard spanning the measurement region.

Store:

- commanded wavelength;
- measured/corrected wavelength;
- calibration residual;
- date and method.

The wavelength uncertainty must be propagated into any edge/cutoff metric because a steep HgCdTe response edge converts wavelength error directly into apparent composition/cutoff error.

Do not quote detector cutoff with more precision than the wavelength calibration and edge-definition permit.

---

## 7. Spectral bandwidth and convolution

The measured responsivity is a convolution of the DUT response with monochromator bandpass.

Record either:

- spectral FWHM at each grating/slit configuration; or
- instrument line-shape function.

Near the steep cutoff edge, deconvolution/model fitting may be required if the monochromator bandwidth is not negligible relative to the response-edge width.

P11 shall not compare two edge slopes measured with substantially different slit/bandwidth settings without correcting or qualifying the effect.

---

## 8. Stray light and order suppression

HgCdTe is highly responsive at shorter wavelengths than its long-wave edge, so short-wavelength stray light can falsely elevate measured response beyond the true cutoff.

For each spectral region:

- use appropriate order-sorting filters;
- measure blocked-source dark signal;
- measure out-of-band response with a long-pass/short-pass validation filter where available;
- perform at least one spectral-stray-light stress test near and beyond cutoff.

A nonzero apparent long-wavelength tail that disappears with stronger order sorting is an optical artifact, not detector physics.

---

## 9. Atmospheric absorption

NIST IR spectral-comparator work identifies atmospheric absorption as a material source of calibration uncertainty.

For the 3–5 µm region, H2O/CO2 absorption can distort both incident power and measured spectral shape.

Preferred:

- purge monochromator/beam path with dry N2; or
- use an evacuated optical path.

Record:

- purge gas;
- flow/time to equilibrium;
- humidity/pressure if available;
- unpurged path length.

Spectral intervals severely contaminated by atmospheric absorption should be flagged rather than smoothed silently.

---

## 10. Detector mounting and operating state

Before optical calibration:

- P10 contact gap/active geometry must be measured;
- detector temperature stabilized at `80 K` for RP-01 comparison;
- electric field set to `10 V/cm` using active-region voltage, not nominal source voltage;
- self-heating check passed;
- bias polarity recorded;
- detector resistance/current recorded;
- package window/filter identity recorded;
- FOV/aperture geometry fixed.

If the absolute calibration is performed at another T/E/f, it is a separate dataset and shall not be relabeled RP-01-equivalent.

---

## 11. Modulation and signal-amplitude convention

RP-01 uses `1 kHz` chopping.

The measured lock-in signal depends on chopper waveform and instrument convention.

For a 50%-duty square-wave modulation between optical states `P_on` and `P_off`, the Fourier fundamental amplitude differs from the full on-off difference.

Therefore P11 shall explicitly record:

- chopper duty cycle;
- waveform;
- reference phase;
- lock-in harmonic;
- lock-in output convention (RMS/peak);
- whether quoted optical power is average, on-state, on-off difference, or fundamental-equivalent power.

### Calibration principle

The safest method is to calibrate the reference detector and DUT using the **same modulation waveform, frequency and signal convention**, causing most waveform factors to cancel in the response ratio.

Do not insert a generic square-wave correction unless the optical-power and electrical-amplitude definitions make it necessary and the factor is derived explicitly.

---

## 12. Reference/DUT substitution geometry

To transfer absolute responsivity accurately, reference detector and DUT must sample the same beam.

Record and control:

- reference plane;
- detector surface position along optical axis;
- lateral centering;
- detector angular orientation;
- aperture diameter;
- beam diameter/profile;
- fraction of beam intercepted;
- polarization if relevant.

NIST IR-comparator work emphasizes detector positioning and beam-profile effects as important uncertainty terms.

### Spatial-uniformity check

Map the calibrated reference detector and DUT response over the incident spot or demonstrate that the spot lies entirely within a uniform region.

If DUT active area is smaller than the calibration beam, operate in irradiance mode or introduce a calibrated limiting aperture rather than silently assuming all beam power reaches the detector.

---

## 13. Radiant-power versus irradiance responsivity

Distinguish:

### Power responsivity

`R_P(lambda) = signal / total radiant power incident on active detector/aperture`

Units `V/W`.

### Irradiance responsivity

`R_E(lambda) = signal / spectral irradiance at detector plane`

Units such as `V/(W cm^-2)`.

Conversion requires a well-defined active/aperture area and uniform irradiance.

For D* calculations, P11 ultimately needs incident optical power on the **same active-area convention** used in the D* area normalization.

Do not mix an irradiance-calibrated optical measurement with a different geometric area in D*.

---

## 14. Relative spectral responsivity acquisition

At each wavelength:

1. stabilize monochromator/source;
2. measure reference-detector signal;
3. measure DUT dark/bias baseline;
4. measure DUT modulated signal;
5. repeat reference measurement after DUT where substitution drift may matter;
6. record source monitor if available;
7. repeat enough cycles to estimate repeatability.

A preferred drift-compensated sequence is:

`REF_before -> DUT -> REF_after`.

Interpolate incident power at DUT time from the two reference readings when source drift is significant.

---

## 15. Absolute response transfer equation

If both DUT and reference signals have known electronic gains `G_DUT` and `G_ref`, define detector-terminal-equivalent signals:

`V_DUT = S_DUT/G_DUT`

`V_ref = S_ref/G_ref`.

If the reference calibration is `R_ref(lambda)` in V/W under a compatible modulation convention:

`P_inc(lambda) = V_ref/R_ref(lambda)`

and

`R_DUT(lambda) = V_DUT/P_inc(lambda)`.

Hence

`R_DUT(lambda) = [V_DUT/V_ref] R_ref(lambda)`.

If reference calibration is in A/W, convert its measured current using the calibrated transimpedance/current readout rather than assuming a voltage responsivity.

---

## 16. Electronics calibration

Every gain/filter in the responsivity path must be calibrated at 1 kHz and across any frequency band used.

Record:

- preamplifier model;
- voltage/transimpedance gain setting;
- measured complex gain `G(f)`;
- input impedance;
- output impedance;
- AC coupling/high-pass pole;
- low-pass filters;
- lock-in time constant and filter slope;
- input range;
- overload status.

Calibrate actual gain with an injected electrical reference or traceable instrument method. Manufacturer nominal gain alone is insufficient for a high-accuracy responsivity result.

---

## 17. Detector signal linearity

At a representative wavelength near `4 µm`, vary incident optical power over the range covering the intended calibration condition.

At each power measure:

- detector signal;
- reference power;
- detector DC current/resistance;
- temperature.

Fit a linear model over the calibration region.

Report:

- responsivity slope;
- intercept;
- nonlinearity residual;
- maximum deviation from linearity.

Do not extrapolate an absolute responsivity calibration beyond the verified optical-power range.

---

## 18. Field dependence / canonical responsivity point

RP-01 reports responsivity versus electric field and a canonical spectral/noise condition at `10 V/cm`.

P11 shall therefore measure:

- absolute responsivity near `4 µm` at `10 V/cm`, 80 K, 1 kHz;
- optional responsivity-field curve using P10 so sweepout/self-heating are separated.

If absolute spectral calibration at every field is impractical, calibrate one canonical field absolutely and obtain relative field dependence under a stable optical source.

---

## 19. Field of view and blackbody background

A quoted `60° FOV` is insufficient for precision radiometry unless full-angle/half-angle convention and physical aperture geometry are known.

### RP-01 internal-consistency inference

`calculations/RP01_300K_BACKGROUND_FLUX_CHECK.md` shows:

- ideal 300-K blackbody;
- detector response approximated as a step to `4.4 µm`;
- **60° full cone = 30° half-angle**;

produces approximately

`1.124×10^15 photons cm^-2 s^-1`,

very close to RP-01's quoted `1.0×10^15 cm^-2 s^-1`.

If 60° were a half-angle, the ideal flux would be approximately

`3.37×10^15 cm^-2 s^-1`.

Therefore the historical 60° FOV is provisionally interpreted as a **full cone angle**. This is an inference, not documentary proof.

### P11 release rule

The final setup shall define FOV by physical aperture dimensions and distance/view factor, not by a nominal angle alone.

---

## 20. Lambertian blackbody photon flux

For blackbody temperature `T`, spectral photon radiance is

`N_lambda(T) = [2c/lambda^4] / [exp(hc/(lambda k_B T)) - 1]`.

For a Lambertian source filling a circular cone of half-angle `theta`, incident photon flux density is

`Phi = pi sin^2(theta) integral N_lambda(T) d(lambda)`

over the chosen band, before window/filter/QE weighting.

For real geometry use the exact aperture view factor whenever the far-field/cone approximation is insufficient.

NIST low-background blackbody calibration practice explicitly derives radiometric quantities from measured absolute optical power together with precision aperture geometry and includes diffraction corrections for small apertures when necessary.

---

## 21. Exact aperture/view-factor approach

For source and detector defining apertures:

Record:

- source aperture area/radius;
- detector/field-stop aperture area/radius;
- separation;
- coaxial offset/tilt;
- aperture temperature;
- emissivity;
- window/filter transmission.

Use the exact radiometric view factor appropriate to the geometry rather than approximating `Omega=A/R²` when apertures are not in the far field.

For small apertures, include diffraction if it is non-negligible; NIST LBIR work shows aperture dimension and diffraction can be material error sources at low flux.

---

## 22. Blackbody absolute calibration branch

If P11 uses a blackbody for absolute broadband scaling, the source shall have:

- calibrated radiance/radiance temperature;
- known aperture area;
- known emissivity or calibration already incorporating effective emissivity;
- measured source temperature with traceable calibration;
- known view factor;
- controlled background/shroud temperature;
- shutter/reference condition.

Do not equate contact thermometer temperature to radiance temperature without calibration. NIST low-background blackbody measurements have shown errors exceeding 1 K in some sources even when conventional contact thermometry appeared nominal.

---

## 23. Broadband-to-spectral scaling method

If only a relative spectral curve `r(lambda)` is available and an absolute broadband detector signal `V_BB` is measured under a known blackbody photon/radiant spectrum, define a scale factor `C` such that

`R_v(lambda) = C r(lambda)`.

For power-domain radiometry:

`V_BB = integral R_v(lambda) P_lambda,inc(lambda) d(lambda)`

so

`C = V_BB / integral r(lambda) P_lambda,inc(lambda) d(lambda)`.

For photon-domain detector models, keep photon responsivity/quantum efficiency definitions explicit and do not mix photon flux with watt responsivity without multiplying/dividing by photon energy.

This integral method is the mathematically clean version of the historical relative-spectrum + broadband absolute calibration architecture.

---

## 24. Detector spectral-response descriptors

From the calibrated spectral curve report separately:

- peak responsivity and wavelength;
- `R_v(4 µm)` at the canonical condition;
- normalized relative spectral response;
- detector cutoff using an explicitly stated convention, e.g. `lambda_50R`, `lambda_10R`, tangent intercept, etc.;
- edge slope/broadening metric;
- uncertainty in each descriptor.

Do not report `lambda_c=4.4 µm` in new measurements without specifying the convention used to recover that value.

Historical RP-01's “cutoff 4.4 µm” remains a quoted benchmark with convention not yet fully closed.

---

## 25. Quantum-efficiency consistency calculation

For an ideal photodiode, current responsivity relates directly to QE by `R_i=eta q lambda/(hc)`. A photoconductor can exhibit photoconductive gain, so this simple relation does not generally equal its external voltage responsivity.

Therefore the RP-01 quoted `70%` quantum efficiency should be treated as a separate detector/absorption parameter in BLIP modeling rather than inferred naively from measured photoconductive voltage responsivity.

Any extraction of QE from RP-01-like photoconductor response must include:

- absorption efficiency;
- carrier lifetime/transit-time gain;
- contact/sweepout effects;
- electrical readout gain.

---

## 26. Responsivity uncertainty budget

At minimum include:

### Reference scale

- calibrated reference responsivity uncertainty;
- calibration interpolation between certificate wavelengths;
- reference aging/stability.

### Optical transfer

- source drift between REF/DUT measurements;
- beam-position repeatability;
- beam spatial nonuniformity;
- aperture-area uncertainty;
- detector positioning;
- wavelength calibration;
- monochromator bandpass;
- stray light/order overlap;
- atmospheric absorption;
- window/filter transmission.

### DUT electrical

- preamplifier gain;
- lock-in scale factor;
- signal repeatability/noise;
- detector temperature;
- electric field;
- modulation frequency;
- optical linearity.

### Geometry

- active-area definition when irradiance is converted to power;
- FOV/view factor for background measurements.

Combine independent standard uncertainties by root-sum-square only where independence is justified; separately document correlated scale uncertainties.

---

## 27. Target uncertainty philosophy

NIST IR spectral-comparator calibrations demonstrate that percent-level responsivity uncertainty is practical in the 3–5 µm region.

For this research manual, the initial goal should be:

- **<5% expanded uncertainty (k≈2)** in absolute `R_v(4 µm)` for a laboratory implementation;
- then improve toward the few-percent national-metrology scale once geometry/reference/atmospheric terms are controlled.

This is a project qualification target, not a historical RP-01 claim.

A result with unknown optical power uncertainty cannot be used as a quantitative D* benchmark even if the spectral curve looks plausible.

---

## 28. Measurement sequence — canonical RP-01 comparison

### A. System preparation

1. stabilize monochromator source;
2. purge/evacuate optical path;
3. calibrate/check wavelength;
4. verify order-sorting filter state;
5. set chopper to `1 kHz`;
6. verify reference detector calibration and linearity;
7. acquire dark/reference baselines.

### B. DUT preparation

8. mount detector in qualified cryogenic fixture;
9. stabilize at `80 K`;
10. set physical FOV/aperture geometry;
11. set active electric field `10 V/cm` using P10;
12. confirm self-heating gate;
13. record current/resistance/polarity.

### C. Spectral scan

14. acquire REF-DUT-REF sequence at each wavelength or a drift-equivalent monitor sequence;
15. record raw electrical signals and gains;
16. record actual wavelength, bandpass and reference power;
17. repeat selected wavelengths periodically for drift/repeatability;
18. extend beyond apparent cutoff to establish noise/stray-light floor.

### D. Absolute calculation

19. transfer reference calibration to incident power;
20. calculate `R_v(lambda)`;
21. propagate uncertainty;
22. calculate/report normalized response and explicit cutoff descriptors.

### E. Background check

23. expose to calibrated 300-K background through released FOV geometry;
24. calculate photon/radiant flux from calibrated geometry/spectrum;
25. compare background-loaded electrical/noise state against the spectral model.

---

## 29. Data record

Every P11 dataset shall store:

- DUT ID/wafer/contact pair;
- measured L/W/t/active area;
- detector T;
- E/current/power;
- FOV/aperture geometry;
- source/monochromator/grating/slits;
- wavelength calibration version;
- chopper frequency/duty/waveform;
- reference detector ID/certificate;
- reference and DUT raw signals;
- preamp/lock-in gains and phase;
- beam/aperture coordinates;
- atmospheric/purge condition;
- spectral bandwidth;
- order-sorting filter;
- absolute incident power;
- `R_v(lambda)`;
- uncertainty components;
- cutoff descriptors;
- repeatability/drift checks;
- PASS/REVIEW disposition.

---

## 30. Failure modes

Log explicitly:

- reference detector outside calibration range;
- detector/reference spatial mismatch;
- beam larger than active area with no irradiance treatment;
- monochromator wavelength drift;
- second-order/stray-light contamination;
- atmospheric absorption artifacts;
- reference signal nonlinear/saturated;
- DUT signal nonlinear/saturated;
- lock-in overload;
- unknown RMS/peak convention;
- self-heating at 10 V/cm;
- source drift between substitutions;
- uncalibrated window/filter loss;
- FOV full-angle/half-angle ambiguity;
- active-area mismatch with later D* calculation;
- response beyond cutoff inconsistent with stray-light tests.

---

## 31. Release blockers

P11 remains qualification-level until closed:

1. exact historical or selected Optronics/monochromator system configuration;
2. released reference detector and traceability chain;
3. exact wavelength calibration procedure;
4. frozen slit/bandpass configuration;
5. chopper waveform/duty and signal-amplitude convention;
6. detector/preamp/lock-in gain calibration;
7. active detector optical area;
8. physical 60° FOV geometry and confirmation of full-angle interpretation;
9. cryostat window/filter transmission;
10. absolute blackbody calibration method if broadband scaling is used;
11. exact responsivity cutoff convention used for RP-01 comparison;
12. full uncertainty budget and laboratory capability result;
13. reproducibility across detector remounts and multiple days.

---

## 32. Primary / official references

1. E. P. G. Smith et al., “A simplified fabrication process for HgCdTe photoconductive detectors using CH4/H2 reactive-ion-etching-induced blocking contacts,” *Semiconductor Science and Technology* 16, 455–462 (2001), DOI `10.1088/0268-1242/16/6/306`.
2. A. Migdall, G. Eppeldauer, *Spectroradiometric Detector Measurements: Part III—Infrared Detectors*, NIST Special Publication 250-42 (1998), DOI `10.6028/NIST.SP.250-42`.
3. V. B. Podobedov, G. P. Eppeldauer, L. M. Hanssen, T. C. Larason, “Calibration of spectral responsivity of IR detectors in the range from 0.6 µm to 24 µm,” NIST / Metrologia (2017); NIST IR spectral-comparator work.
4. V. Podobedov, G. Eppeldauer, T. Larason, “Evaluation of optical radiation detectors in the range from 0.8 µm to 20 µm at the NIST infrared spectral calibration facility,” Proc. SPIE 8550 (2012), DOI `10.1117/12.980937`.
5. NIST Low Background Infrared (LBIR) facility publications on absolute cryogenic radiometry, precision aperture geometry and calibrated blackbody sources.
6. A. C. Carter, R. V. Datla, T. M. Jung, A. W. Smith, J. A. Fedchak, “Low Background Temperature Calibration of Infrared Blackbodies,” *Metrologia* 43 (2006).
7. S. G. Kaplan et al., “Design, calibration, and application of a cryogenic low-background infrared radiometer for spectral irradiance and radiance measurements from 4 µm to 20 µm wavelength,” *Optical Engineering* 60, 034102 (2021), DOI `10.1117/1.OE.60.3.034102`.
8. Historical lineage: “Relative Spectral Response And Low Background Radiometric Detector Measurements,” Proc. SPIE 1108, *Test and Evaluation of Infrared Detectors and Arrays* (1989), describing the Optronics 735D / pyroelectric relative-response + broadband-blackbody absolute-scaling architecture. Full primary text/DOI remains to be acquired before using its detailed numerical settings as controlled setpoints.

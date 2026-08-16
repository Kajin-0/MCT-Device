# P11A — UWA Optronics spectral-response lineage and radiometric transfer addendum

**Status:** `CONTROLLED-LINEAGE-ADDENDUM / EMPIRICAL-TRANSFER`  
**Parent:** `P11_ABSOLUTE_SPECTRAL_RESPONSIVITY_RADIOMETRY.md`

## 1. Purpose

Strengthen P11 with the recoverable experimental lineage behind the RP-01 spectral-response measurements and define the minimum empirical checks needed to reproduce the reported absolute responsivity / D* state without inventing undocumented Optronics hardware or calibration settings.

P11 remains the canonical radiometry SOP. P11A does **not** create a competing method.

---

## 2. Direct RP-01 optical anchors

Smith et al. 2001 directly report that the photoconductor measurements used an **Optronics Laboratories Spectral Response Measurement System**.

Direct operating conditions include:

- detector temperature: `80 K`;
- chopping frequency: `1 kHz`;
- stated field of view: `60°`;
- single-wavelength responsivity versus field at `4 µm`;
- spectral responsivity at `10 V/cm`;
- spectral detectivity at `10 V/cm`;
- detector cutoff approximately `4.4 µm`;
- BLIP `D*≈2.0×10^11 cm Hz^1/2 W^-1` at `4 µm`;
- quoted 300-K / 60° background photon flux `≈1.0×10^15 cm^-2 s^-1`;
- quoted quantum efficiency `≈70%`.

The paper does **not** close:

- Optronics system model;
- source type;
- monochromator model/gratings/slits;
- reference detector;
- absolute calibration chain;
- wavelength calibration procedure;
- order-sorting filters;
- beam size/profile;
- window/filter transmission;
- physical dimensions producing the 60° FOV;
- full-angle versus half-angle wording;
- chopper duty/waveform;
- preamplifier/lock-in amplitude convention;
- active-area convention used in the reported D*.

These remain `OPEN-HISTORICAL`.

---

## 3. Same-UWA Optronics lineage

A 1997 UWA monolithic dual-band HgCdTe photoconductor paper independently reports responsivity measurements using an **Optronics Laboratories Spectral Response Measurement System** at a chopping frequency of `1 kHz`.

The reported spectral measurements were made:

- at `80 K`;
- over approximately `3–12 µm`;
- with an applied field of `10 V/cm` in the published spectral-response figure.

This provides strong same-laboratory evidence that the Optronics spectral-response system and the `1 kHz / 80 K / 10 V cm^-1` measurement family predated RP-01 by several years.

### Evidence limit

This does **not** prove:

- that the same physical Optronics instrument remained unchanged;
- which Optronics model was used;
- that reference-detector calibration was unchanged;
- identical monochromator slit/bandpass settings;
- identical FOV/aperture geometry;
- identical electronics or signal-amplitude convention.

Treat it as **same-UWA measurement-lineage evidence**, not historical apparatus closure.

Primary citation:

G. Parish, C. A. Musca, J. F. Siliquini, J. Antoszewski, J. M. Dell, B. D. Nener, L. Faraone, G. J. Gouws, “A monolithic dual-band HgCdTe infrared detector structure,” *IEEE Electron Device Letters* 18, 352–354 (1997), DOI `10.1109/55.596934`.

---

## 4. Optronics 735D historical lead — not yet promoted to primary evidence

A 1989 SPIE paper titled **“Relative Spectral Response And Low Background Radiometric Detector Measurements”** is repeatedly indexed as describing a system centered on an Optronics Laboratories model `735D` triple-grating subtractive-mode double monochromator, approximately `2–30 µm`, with pyroelectric relative-irradiance references and broadband blackbody scaling.

However, the full primary SPIE text has not yet been recovered through the present source route.

Therefore:

- `Optronics 735D` is a **historical equipment lead**;
- pyroelectric-reference + blackbody-scaling architecture is a **historical-method lead**;
- neither may be relabeled as the RP-01 system without direct documentary closure.

This negative-evidence discipline is important because “Optronics Laboratories Spectral Response Measurement System” could refer to multiple configurations or generations.

---

## 5. Modern empirical comparator benchmark

NIST infrared spectral-comparator work provides a controlled transfer benchmark for a modern reproduction.

Published NIST implementation details include:

- calibrations in radiant-power and irradiance modes;
- reference detectors including pyroelectric, InSb and extended-InGaAs architectures;
- high-throughput monochromator with interchangeable gratings;
- attention to beam profile, detector positioning and atmospheric absorption;
- mapped detector spatial nonuniformity;
- typical expanded uncertainties of order `1%` in radiant-power mode and `2.5%` in irradiance mode for the cited facility configuration.

This is **not** historical RP-01 evidence. It establishes a practical metrology target for the replacement system.

Primary/official references:

- V. B. Podobedov, G. P. Eppeldauer, T. C. Larason, Proc. SPIE 8550 (2012), DOI `10.1117/12.980937`.
- V. B. Podobedov, G. P. Eppeldauer, L. M. Hanssen, T. C. Larason, NIST IR spectral-responsivity calibration work spanning approximately `0.6–24 µm`.

---

## 6. Blackbody radiance temperature is not contact temperature

NIST low-background blackbody calibrations show that contact thermometry and radiance temperature can disagree materially; in the published survey, multiple calibrated blackbodies exhibited errors exceeding `1 K` over parts of their operating range.

Therefore P11/P11A prohibit using a nominal `300 K` blackbody controller or contact sensor alone as the absolute radiance scale.

Required for an absolute background-flux claim:

- calibrated radiance temperature or calibrated emitted radiance;
- source emissivity/effective-emissivity treatment;
- aperture dimensions;
- source-to-detector geometry;
- window/filter transmission;
- uncertainty.

Primary reference:

A. C. Carter et al., “Low Background Temperature Calibration of Infrared Blackbodies,” *Metrologia* 43 (2006).

---

## 7. Exact two-aperture geometry

For coaxial circular source and detector apertures, NIST LBIR practice determines calibration from measured optical power plus physical aperture geometry rather than a nominal F-number or FOV label.

For a blackbody aperture radius `r1`, detector/receiver aperture radius `r2`, and separation `R`, use the exact applicable view-factor expression or validated numerical radiometric model.

P11A therefore requires the physical geometry to be recorded even when the setup is colloquially described as “60° FOV.”

### 7.1 RP-01 60° consistency family

The existing repository Planck check shows that interpreting the historical `60°` as a **full cone** gives a 30° half-angle and a 300-K photon flux close to the quoted RP-01 value.

For a simple circular field stop viewed from the active plane:

`theta_half = 30°`

and therefore

`a/z = tan(30°) = 0.57735`

for stop radius `a` and axial distance `z` in the simple geometrical cone model.

The ordinary solid angle of that cone is

`Omega = 2*pi*(1-cos 30°) ≈ 0.84179 sr`.

For a Lambertian radiance incident on a planar detector, the projected angular integral is

`Omega_proj = pi*sin^2(30°) = pi/4 ≈ 0.78540 sr`.

These values define a **geometry family**, not historical dimensions.

Do not choose `a` or `z` from these relations and call the resulting assembly historical RP-01 hardware.

---

## 8. Photoconductor irradiance/background linearity gate

HgCdTe photoconductors can exhibit response nonlinearity that depends on irradiance and background state. Consequently, a calibration performed with the same total radiant power but a different beam area/background can be non-equivalent.

P11A requires a linearity/background check at the actual calibration geometry.

At minimum, near the canonical `4 µm / 80 K / 10 V cm^-1 / 1 kHz` state:

1. vary monochromatic irradiance over the intended calibration range;
2. record detector signal, resistance/current and temperature;
3. repeat at the released background/FOV state;
4. repeat with the background blocked or altered in a documented manner;
5. establish the usable linear interval and whether responsivity shifts with background loading.

Primary supporting literature includes NPL/Optica experimental measurements showing photoconductive HgCdTe nonlinearity depends on irradiance, and later radiometric work showing background fluctuations can couple with detector nonlinearity to create slow apparent responsivity drift.

This is a **general HgCdTe photoconductor metrology rule**, not a claim that RP-01 suffered a specific unreported calibration error.

---

## 9. Three-branch reproduction architecture

### Branch A — same-lineage condition reproduction

Preserve the direct RP-01 operating coordinates:

- `80 K`;
- `1 kHz`;
- `10 V/cm` for spectral responsivity / D*;
- physical geometry selected to realize the released FOV;
- same detector package/window state used for noise and responsivity where D* is combined.

This branch tests device comparability, not SI traceability by itself.

### Branch B — SI-traceable spectral comparator

At each wavelength:

`R_DUT(lambda) = [S_DUT(lambda)/S_REF(lambda)] * R_REF(lambda)`

with:

- same optical reference plane;
- calibrated detector positioning;
- same modulation convention where possible;
- traceable reference responsivity;
- beam-profile and spatial-uniformity control;
- calibrated electronics.

### Branch C — calibrated 300-K background cross-check

Establish a calibrated broadband background state using:

- radiance-calibrated blackbody;
- measured aperture geometry/view factor;
- measured window/filter transmission;
- measured detector active area;
- released FOV convention.

Compare measured background-loaded current/noise/responsivity with the spectral-response model.

A reproduced detector is strongest when Branches B and C close consistently within their combined uncertainty.

---

## 10. Required empirical closure vector

Define

`Y_RAD = {R_v(lambda), R_v(4um), lambda_edge metrics, P_inc(lambda), background flux, FOV geometry, linearity, drift, package transmission, D* consistency}`.

A system is not `RP01-RADIOMETRY-TRANSFER-QUALIFIED` from a matching spectral shape alone.

Required closure includes:

1. calibrated absolute `R_v(4 µm)`;
2. stable normalized spectrum through and beyond cutoff;
3. physical FOV geometry;
4. verified active area;
5. background-flux reconstruction;
6. detector linearity at actual irradiance/background;
7. package/window transmission state;
8. P12 noise measured under the same declared optical-background state;
9. D* recomputed from the same area/responsivity/noise conventions.

---

## 11. Mandatory raw records

Store:

- Optronics/replacement instrument make/model/revision;
- source type and operating state;
- monochromator/grating/slits/bandpass;
- order-sorting filters;
- wavelength calibration;
- reference detector and certificate;
- beam profile/diameter;
- reference plane and detector coordinates;
- chopper frequency/duty/waveform;
- preamp/lock-in model, gain and amplitude convention;
- active area and aperture dimensions;
- detector-to-aperture distance;
- window/filter transmission;
- blackbody radiance calibration and temperature history;
- raw REF/DUT signals;
- detector bias/current/resistance/temperature;
- background state;
- uncertainty budget;
- repeatability across remount/day.

---

## 12. Historical blockers after Round 28

Still `OPEN-HISTORICAL`:

- exact RP-01 Optronics model;
- whether RP-01 used an OL 735D or another model;
- source lamp/blackbody used for the spectral scan;
- monochromator gratings/slits/bandpass;
- reference detector product/calibration;
- exact absolute scaling method;
- optical train and beam diameter;
- window/filter material/transmission;
- physical 60° FOV dimensions;
- chopper duty/waveform;
- preamplifier and lock-in model for responsivity;
- RMS/peak/fundamental signal convention;
- exact active-area convention used in D*;
- exact historical cutoff definition.

These gaps are now isolated. They should not be filled by assuming that a generic Optronics system or the 1989 OL-735D facility was identical to UWA’s apparatus.

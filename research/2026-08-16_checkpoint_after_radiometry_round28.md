# Checkpoint — after empirical radiometry / Optronics lineage Round 28

**Date:** 2026-08-16  
**Round:** 28  
**Main objective:** audit P11 and close as much of the RP-01 spectral-response / blackbody / FOV execution chain as primary evidence permits.

---

## 1. Audit decision

`procedures/P11_ABSOLUTE_SPECTRAL_RESPONSIVITY_RADIOMETRY.md` was audited before creating any new top-level procedure.

Result: **P11 is already operationally adequate as the canonical radiometry SOP.**

It already controls:

- spectral comparator architecture;
- broadband-blackbody scaling branch;
- wavelength calibration;
- bandpass/convolution;
- stray light/order sorting;
- atmospheric absorption;
- 80-K / 10-V-cm^-1 / 1-kHz RP-01 state;
- signal-amplitude convention;
- reference/DUT substitution geometry;
- radiant-power versus irradiance definitions;
- electronics gain calibration;
- linearity;
- FOV/view-factor geometry;
- blackbody radiance calibration;
- uncertainty;
- active-area/D* consistency.

Therefore **no P35 duplicate radiometry module was created**.

Instead Round 28 created a controlled lineage/transfer supplement:

- `procedures/P11A_UWA_OPTRONICS_RADIOMETRY_LINEAGE_ADDENDUM.md`
- `travelers/P11A_OPTRONICS_RADIOMETRY_TRANSFER_REGISTER.md`
- `docs/SOURCE_LEDGER_ADDENDUM_ROUND28.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND28.md`

---

## 2. Strongest new historical result

The UWA Optronics apparatus is not a one-paper mention.

Parish et al. 1997 independently reports an **Optronics Laboratories Spectral Response Measurement System** used for HgCdTe photoconductor responsivity measurements at:

- 1-kHz chopping;
- 80 K;
- spectral response over ~3–12 µm;
- 10 V/cm in the published spectral-response figure.

This supports a persistent UWA Optronics measurement lineage before RP-01.

It does **not** identify the exact model or prove identical calibration hardware/settings.

Primary source:

G. Parish et al., *IEEE Electron Device Letters* 18, 352–354 (1997), DOI `10.1109/55.596934`.

---

## 3. RP-01 direct optical state retained

Do not drift from:

- Optronics Laboratories Spectral Response Measurement System;
- `80 K`;
- `1 kHz`;
- stated `60°` FOV;
- `4 µm` single-wavelength responsivity versus field;
- `10 V/cm` spectral responsivity / D* state;
- cutoff ~`4.4 µm`;
- BLIP `D*≈2.0e11 cm Hz^1/2 W^-1` at 4 µm;
- 300-K/60° quoted photon flux `≈1.0e15 cm^-2 s^-1`;
- quoted QE ~70%.

The paper does not close the exact optical bench or amplitude convention.

---

## 4. 60° FOV result

The existing Planck consistency calculation remains valid as a **consistency inference**:

- 60° full cone -> 30° half-angle;
- idealized 300-K step-response flux to 4.4 µm is close to the quoted `1e15 photons cm^-2 s^-1`;
- 60° half-angle would yield a much larger flux.

Round 28 adds the geometric family:

`a/z = tan(30°) = 0.57735`

for a simple circular field stop of radius `a` a distance `z` from the detector plane.

Also:

- ordinary cone solid angle `Omega≈0.84179 sr`;
- Lambertian projected angular integral `pi sin^2(30°)=pi/4≈0.78540 sr`.

These do **not** recover historical aperture dimensions.

NIST LBIR practice confirms that absolute blackbody calibration should use measured aperture dimensions/separation and exact view factor, with diffraction correction where needed.

---

## 5. Blackbody calibration rule strengthened

A nominal/contact thermometer reading of 300 K is not an absolute radiance calibration.

NIST low-background blackbody calibrations found multiple real sources with radiance-temperature versus contact-thermometry discrepancies exceeding 1 K over parts of their range.

P11A therefore requires:

- calibrated radiance temperature or calibrated radiance;
- effective emissivity treatment;
- source/detector aperture geometry;
- view factor;
- transmission;
- uncertainty.

---

## 6. HgCdTe photoconductor linearity/background rule

Primary HgCdTe radiometry literature adds an important control not to treat as optional:

- photoconductive HgCdTe nonlinearity can depend on **irradiance**, not merely total radiant power;
- background fluctuations can couple with detector nonlinearity to create slow apparent responsivity drift.

Therefore local RP-01 transfer requires a linearity scan at the actual beam size/background and a repeat/background-drift check.

This is a general transfer rule, not evidence that RP-01's published result is wrong.

---

## 7. D* state-matching rule

A numerically correct formula does not rescue mismatched measurement states.

For local release:

`D* = R_v sqrt(A) / e_n`

may only combine P11 and P12 data when the following are matched or explicitly corrected:

- detector temperature;
- electric field;
- package/window state;
- FOV/background state;
- active-area convention;
- response/noise frequency as applicable.

This rule is now explicit in the P11A traveler.

---

## 8. Optronics 735D lead remains quarantined

A 1989 SPIE paper titled “Relative Spectral Response And Low Background Radiometric Detector Measurements” is repeatedly indexed as describing:

- Optronics Laboratories model 735D;
- triple-grating subtractive-mode double monochromator;
- ~2–30 µm;
- pyroelectric relative references;
- broadband blackbody absolute scaling.

However the full primary SPIE paper was not recovered in this round.

Status remains:

`SECONDARY-LEAD / PRIMARY-FULL-TEXT-NOT-RECOVERED`.

Do not write “RP-01 used an OL-735D.”

---

## 9. Remaining high-priority historical gaps

- exact RP-01 Optronics model;
- source;
- monochromator/grating/slits/bandpass;
- reference detector and calibration chain;
- wavelength calibration;
- order sorting;
- physical FOV dimensions;
- window/filter;
- chopper duty/waveform;
- responsivity preamplifier/lock-in;
- RMS/peak/fundamental convention;
- beam diameter/profile;
- detector optical active area;
- exact 4.4-µm cutoff convention;
- exact area/background/noise conventions used in historical D*.

---

## 10. Strongest next action

Proceed with **Round 29: P12 noise / analyzer / background-state audit and empirical closure**.

Audit P12/P12A/P12B before creating any P35/P36 module.

Priority recovery:

1. exact UWA low-noise preamplifier used in RP-01;
2. HP35665A configuration: input range, coupling, window, FFT span/lines, averaging and ASD normalization;
3. exact detector contact pair/geometry used for Figure 5;
4. bias supply/load topology and bias-resistor noise contribution;
5. optical-background geometry during noise measurement;
6. whether the 60° FOV was filled by a 300-K scene during the noise PSD measurement or only used as a quoted detector environment;
7. noise trace calibration from analyzer input back to detector-terminal V/sqrt(Hz);
8. distinction among analyzer bin width, ENBW and PSD/ASD units;
9. match P12 background/frequency state to P11 before D* closure.

If P12 is already operationally sufficient, create only a lineage/transfer addendum analogous to P11A rather than a duplicate top-level SOP.

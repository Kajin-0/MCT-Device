# P11A — Optronics / absolute radiometry transfer qualification register

**Status:** BLANK CONTROLLED REGISTER  
**Parent:** P11 / P11A

Use one register per detector/remount/day unless the acquisition system stores all fields in a traceable run database.

---

## A. Device identity

- wafer / growth lot:
- die ID:
- package ID:
- contact pair:
- measured contact gap `L`:
- active width `W`:
- active optical area convention:
- passivation/window state:
- P33 package revision:

## B. Detector operating state

- detector temperature:
- temperature sensor / calibration:
- thermal stability criterion:
- electric field:
- active-region voltage:
- detector current:
- detector resistance:
- dissipated electrical power:
- self-heating gate PASS/FAIL:
- bias polarity:
- elapsed time after cooldown:

For RP-01 comparison, deviations from `80 K / 10 V cm^-1 / 1 kHz` must be explicit.

---

## C. Spectral instrument

- instrument manufacturer:
- model:
- serial/revision:
- source type:
- source operating current/temperature:
- monochromator model:
- grating/order:
- entrance slit:
- exit slit:
- measured spectral FWHM / line shape:
- wavelength step:
- purge/vacuum state:
- atmospheric path length:
- order-sorting filter(s):
- stray-light validation filter/test:

### Historical-lineage classification

- [ ] direct RP-01 apparatus identity recovered
- [ ] same-UWA Optronics lineage only
- [ ] modern replacement comparator
- [ ] other

Do not mark an OL-735D as historical RP-01 hardware without direct documentary evidence.

---

## D. Wavelength calibration

- calibration standard/features:
- date:
- commanded wavelength table stored? Y/N
- corrected wavelength table stored? Y/N
- RMS residual:
- maximum residual:
- uncertainty assigned near 4 µm:

---

## E. Reference detector / optical scale

- reference detector manufacturer/model:
- serial:
- detector type:
- calibration institute:
- certificate ID/date:
- calibrated quantity: radiant power / irradiance / radiance
- calibration wavelength grid:
- calibration uncertainty near 4 µm:
- active area:
- spatial uniformity map ID:
- modulation-frequency dependence verified? Y/N
- linearity range verified? Y/N
- readout model:
- calibrated transimpedance/gain:

### Substitution geometry

- reference plane definition:
- DUT/reference axial repeatability:
- lateral centering repeatability:
- angular orientation:
- beam diameter/profile:
- fraction of beam intercepted:

---

## F. Modulation / electronics

- chopper/modulator model:
- frequency:
- duty cycle:
- waveform:
- modulation plane/location:
- reference phase:
- lock-in model:
- harmonic:
- lock-in output convention: RMS / peak / other
- preamplifier model:
- nominal gain:
- measured complex gain at 1 kHz:
- filter settings:
- input/output range:
- overload observed? Y/N

Define the optical power convention used with the signal:

- [ ] on-state power
- [ ] on-off difference
- [ ] time-average power
- [ ] fundamental-equivalent modulated power
- [ ] other:

---

## G. FOV / aperture geometry

- historical comparison target: `60°` stated RP-01 FOV
- adopted convention: full angle / half angle / other
- evidence class for convention:
- source aperture radius/area:
- detector limiting-aperture radius/area:
- source-to-aperture distance:
- detector-to-field-stop distance:
- coaxial offset:
- tilt:
- cold-shield geometry:
- window clear aperture:
- geometric half-angle:
- geometric full angle:
- ordinary cone solid angle:
- projected angular factor used:
- exact view-factor calculation ID/version:

If using the provisional RP-01 full-cone interpretation, `theta_half=30°`; this is not documentary proof of historical dimensions.

---

## H. Window / filter / package transmission

- window material:
- thickness:
- coating:
- filter identity:
- transmission dataset/certificate:
- measurement temperature:
- angle of incidence:
- contamination/frost inspection:
- effective `T(lambda)` file:

---

## I. Relative spectral scan

For every wavelength retain raw:

- timestamp
- wavelength
- reference-before signal
- DUT dark/baseline
- DUT signal
- reference-after signal
- source monitor
- detector T
- detector I/R
- gains/ranges

Required repeat points:

- near 3 µm:
- near 4 µm:
- near edge:
- beyond edge / stray-light floor:

REF-before -> DUT -> REF-after drift correction used? Y/N

---

## J. Absolute responsivity reduction

- raw file ID:
- reduction script/version:
- detector-terminal-equivalent signal convention:
- reference responsivity interpolation method:
- `P_inc(lambda)` file:
- `R_v(lambda)` file:
- `R_v(4 µm)`:
- peak `R_v` and wavelength:
- cutoff descriptor used:
- cutoff value:
- spectral-edge uncertainty:

Never write only “cutoff = 4.4 µm” for a new measurement; state the descriptor.

---

## K. Irradiance / background linearity

At representative `~4 µm` record at least 3–5 irradiance levels spanning the calibration condition.

For each level:

- irradiance/power:
- beam area:
- background state:
- signal:
- responsivity:
- detector current/resistance:
- detector temperature:

Fit interval:
- slope:
- intercept:
- maximum nonlinearity residual:
- background-dependent shift observed? Y/N
- accepted linear calibration range:

---

## L. Calibrated blackbody background cross-check

- blackbody manufacturer/model:
- serial:
- cavity/aperture geometry:
- radiance calibration source/certificate:
- contact-temperature sensor:
- controller setpoint:
- contact temperature:
- calibrated radiance temperature:
- effective emissivity:
- aperture radius/area:
- detector/aperture separation:
- shutter/reference state:
- ambient/shroud temperature:
- exact view factor:
- diffraction correction if applicable:
- window/filter weighted transmission:
- calculated photon flux at detector:
- calculated radiant flux/power:

### RP-01 comparison

- calculated flux near target `1.0e15 photons cm^-2 s^-1`? Y/N
- difference:
- uncertainty:
- full-angle/half-angle assumption explicitly stated? Y/N

Do not use blackbody contact temperature alone as the radiance scale.

---

## M. P12 / D* closure

- P12 dataset ID:
- noise ASD frequency used:
- optical-background state identical/qualified? Y/N
- detector area used in D*:
- area convention same as P11? Y/N
- responsivity wavelength:
- responsivity value:
- noise value:
- recomputed `D*`:
- uncertainty:
- BLIP/background-dominance evidence:

Do not combine P11 responsivity and P12 noise from unqualified different FOV/background/package states.

---

## N. Uncertainty budget

Record standard uncertainties for:

- reference responsivity:
- reference interpolation:
- source drift:
- positioning:
- beam uniformity:
- wavelength:
- bandpass:
- stray light:
- atmospheric absorption:
- gain:
- signal repeatability:
- detector temperature:
- electric field:
- active area:
- aperture dimensions:
- view factor:
- blackbody radiance temperature:
- window/filter transmission:
- linearity/background dependence:

Combined standard uncertainty:
Expanded uncertainty / k:

---

## O. Repeatability / remount closure

- same-mount repeat scan ID:
- next-day scan ID:
- remount scan ID:
- `R_v(4 µm)` spread:
- edge spread:
- FOV/geometry remeasurement:
- disposition:

---

## P. Release disposition

### Required gates

- [ ] wavelength calibration
- [ ] reference scale traceable
- [ ] same optical plane / beam quantified
- [ ] modulation convention known
- [ ] electronics gain calibrated
- [ ] active area measured
- [ ] physical FOV geometry measured
- [ ] package transmission known
- [ ] irradiance/background linearity checked
- [ ] blackbody radiance scale calibrated where used
- [ ] P12 background state matched for D*
- [ ] uncertainty budget complete
- [ ] repeatability/remount gate passed

Final status:

- [ ] `RP01-RADIOMETRY-TRANSFER-QUALIFIED`
- [ ] `QUALIFICATION-INCOMPLETE`
- [ ] `FAIL / INVESTIGATE`

Operator:
Date:
Reviewer:
Notes/deviations:

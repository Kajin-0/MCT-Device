# Source ledger addendum — Round 28

**Topic:** RP-01 Optronics spectral response / absolute radiometry / FOV / blackbody transfer

Evidence classes used below:

- `DIRECT-RP01` — directly stated in Smith et al. 2001.
- `SAME-UWA` — same UWA detector group / measurement lineage, not proof of identical hardware.
- `PRIMARY-METROLOGY` — primary/official radiometric metrology source used to define a transfer method.
- `PRIMARY-HGCDTE-TRANSFER` — primary HgCdTe detector metrology evidence outside RP-01.
- `SECONDARY-LEAD` — bibliographic lead only; cannot set controlled historical values.

---

## R28-S01 — Smith et al. 2001

**Class:** `DIRECT-RP01`

E. P. G. Smith, K. J. Winchester, C. A. Musca, J. M. Dell, L. Faraone, “A simplified fabrication process for HgCdTe photoconductive detectors using CH4/H2 reactive-ion-etching-induced blocking contacts,” *Semiconductor Science and Technology* 16, 455–462 (2001).

DOI: `10.1088/0268-1242/16/6/306`

Direct optical anchors recovered:

- Optronics Laboratories Spectral Response Measurement System;
- 80 K;
- 60° FOV;
- 1-kHz chopping for responsivity measurements;
- single-wavelength responsivity near 4 µm as function of field;
- spectral responsivity / detectivity at 10 V/cm;
- cutoff ~4.4 µm;
- BLIP D* ~2e11 cm Hz^1/2 W^-1 at 4 µm;
- 300-K/60° background photon flux ~1e15 photons cm^-2 s^-1;
- quoted QE ~70%.

Not directly closed:

- Optronics model;
- source/monochromator/slit/grating;
- reference detector/calibration;
- physical FOV dimensions;
- full-vs-half angle convention;
- signal-amplitude convention;
- active-area convention.

---

## R28-S02 — Parish et al. 1997

**Class:** `SAME-UWA`

G. Parish et al., “A monolithic dual-band HgCdTe infrared detector structure,” *IEEE Electron Device Letters* 18, 352–354 (1997).

DOI: `10.1109/55.596934`

Same-UWA optical anchors:

- Optronics Laboratories Spectral Response Measurement System;
- chopping frequency 1 kHz;
- spectral response shown at 80 K;
- applied field 10 V/cm in the spectral-response figure;
- spectral range approximately 3–12 µm for the dual-band device.

Use:

- demonstrates a UWA Optronics / 1-kHz HgCdTe photoconductor measurement lineage before RP-01.

Do not infer:

- exact same physical instrument;
- exact Optronics model;
- same optical train or calibration chain;
- same FOV.

Institutional source record: University of Western Australia Profiles and Research Repository.

---

## R28-S03 — Podobedov, Eppeldauer, Larason 2012

**Class:** `PRIMARY-METROLOGY`

V. B. Podobedov, G. P. Eppeldauer, T. C. Larason, “Evaluation of optical radiation detectors in the range from 0.8 µm to 20 µm at the NIST infrared spectral calibration facility,” Proc. SPIE 8550 (2012).

DOI: `10.1117/12.980937`

Official NIST record reports:

- radiant-power and irradiance detector-calibration modes;
- reference detectors including pyroelectric, InSb and sphere-input extended InGaAs;
- high-throughput monochromator with interchangeable gratings;
- source branches including a high-temperature blackbody and quartz-halogen source;
- beam profile, detector positioning and atmospheric absorption as important uncertainty terms;
- spatial-uniformity mapping;
- typical expanded uncertainties about 1% in radiant-power mode and 2.5% in irradiance mode for the described facility.

Use:

- modern transfer architecture and uncertainty benchmark.

Not historical RP-01 proof.

---

## R28-S04 — Podobedov et al. 2017

**Class:** `PRIMARY-METROLOGY`

V. B. Podobedov, G. P. Eppeldauer, L. M. Hanssen, T. C. Larason, “Calibration of spectral responsivity of IR detectors in the range from 0.6 µm to 24 µm,” NIST / Metrologia-era IR detector calibration work (2017).

Official NIST source record confirms extension of calibrated spectral responsivity coverage through the RP-01 MWIR band and both radiant-power and irradiance measurement modes.

Use:

- SI-traceable replacement-system architecture.

---

## R28-S05 — Carter et al. 2006

**Class:** `PRIMARY-METROLOGY`

A. C. Carter, R. V. Datla, T. M. Jung, A. W. Smith, J. A. Fedchak, “Low Background Temperature Calibration of Infrared Blackbodies,” *Metrologia* 43 (2006).

Official NIST source record reports:

- calibrated low-background blackbody performance;
- some sources showing radiance-temperature versus contact-thermometry errors >1 K over portions of their range;
- absolute cryogenic radiometers as detector standards;
- detailed uncertainty treatment.

Use:

- prohibits treating controller/contact temperature as the absolute radiance scale.

---

## R28-S06 — NIST LBIR broadband calibration geometry

**Class:** `PRIMARY-METROLOGY`

NIST project: “Infrared cryogenic blackbody broadband calibration.”

Official geometry explicitly uses:

- measured radiant power;
- blackbody aperture radius;
- receiver aperture radius;
- aperture separation;
- exact view-factor expression;
- diffraction correction where needed.

Use:

- physical FOV/view-factor transfer framework.

Not historical RP-01 geometry.

---

## R28-S07 — Smith et al. 2003 small-aperture radiometry

**Class:** `PRIMARY-METROLOGY`

A. W. Smith, A. C. Carter, S. R. Lorentz, T. M. Jung, R. V. Datla, “Radiometrically Deducing Aperture Sizes,” *Metrologia* 40 (2003).

Use:

- confirms aperture dimensional uncertainty, diffraction, aperture heating/light leakage become important in low-power IR radiometry.

---

## R28-S08 — NPL HgCdTe absolute linearity paper

**Class:** `PRIMARY-HGCDTE-TRANSFER`

“Absolute linearity measurements on HgCdTe detectors in the infrared region,” *Applied Optics* 43 (2004).

Primary publisher record reports:

- experimental comparison of photoconductive and photovoltaic HgCdTe;
- photoconductive HgCdTe nonlinearity is a function of irradiance rather than total incident radiant power.

Use:

- irradiance/beam-area must be controlled in P11/P11A linearity qualification.

Not evidence for a specific RP-01 nonlinearity magnitude.

---

## R28-S09 — HgCdTe radiometric drift / background coupling

**Class:** `PRIMARY-HGCDTE-TRANSFER`

“Practical limit of the accuracy of radiometric measurements using HgCdTe detectors,” *Applied Optics* 45 (2006).

Primary publisher record reports:

- slow spectral-responsivity drift in HgCdTe detectors;
- background-temperature fluctuations coupling with detector nonlinearity as a major cause.

Use:

- requires background state and drift checks during high-accuracy responsivity calibration.

Not evidence that RP-01 suffered the same drift magnitude.

---

## R28-S10 — 1989 Optronics 735D system lead

**Class:** `SECONDARY-LEAD / PRIMARY-FULL-TEXT-NOT-RECOVERED`

Title: “Relative Spectral Response And Low Background Radiometric Detector Measurements,” Proc. SPIE 1108, *Test and Evaluation of Infrared Detectors and Arrays* (1989).

Search-indexed descriptions consistently identify:

- Optronics Laboratories 735D;
- triple-grating subtractive-mode double monochromator;
- approximately 2–30 µm spectral range;
- pyroelectric reference detectors;
- blackened-thermocouple comparison for reference-detector relative response;
- broadband blackbody scaling to absolute response.

### Control rule

The full primary SPIE paper was **not recovered in Round 28**. None of these details may be assigned to RP-01 as historical facts.

The item remains a high-priority source-recovery target because it may reveal a historically relevant Optronics architecture.

---

# Round-28 source conclusion

P11 already contained the correct metrology architecture. Round 28 adds a stronger provenance hierarchy:

1. direct RP-01 operating coordinates;
2. same-UWA Optronics measurement lineage;
3. primary modern radiometric transfer methods;
4. primary HgCdTe nonlinearity/background warnings;
5. an explicitly quarantined 1989 OL-735D historical lead.

No exact historical Optronics model or 60° aperture geometry has yet been recovered.

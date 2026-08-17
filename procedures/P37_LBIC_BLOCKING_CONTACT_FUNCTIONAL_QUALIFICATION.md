# P37 — LBIC blocking-contact functional qualification on sacrificial W1 witness

**Status:** ROUND-57 REFERENCE QUALIFICATION PROTOCOL / RESEARCH SCREEN  
**Date:** 2026-08-16 America/New_York

## 1. Purpose

Provide an executable functional test of the localized CH4/H2 RIE-induced n+/n blocking-contact state. This protocol closes the logic gap that TLM measures majority-carrier contact resistance but does not by itself establish minority-carrier blocking.

P37 is intended for a dedicated process-control witness `W1`, not for destructive modification of the finished D1 detector.

## 2. Evidence basis

Primary/same-UWA-lineage evidence:

- C. A. Musca, J. F. Siliquini, E. P. G. Smith, J. M. Dell, L. Faraone, “Laser Beam Induced Current Imaging of Reactive Ion Etching Induced n-Type Doping in HgCdTe,” *Journal of Electronic Materials* 27, 661–667 (1998), DOI `10.1007/s11664-998-0032-4`.
- E. P. G. Smith et al. 2001 RP-01 process paper, DOI `10.1088/0268-1242/16/6/306`.

Direct/same-lineage anchors include:

- RIE-exposed square scale about `300 × 300 µm`;
- `1.047 µm` CW excitation;
- irradiance about `400 mW/cm²`;
- `80 K` measurement;
- bipolar LBIC spatial response interpreted as evidence of an n+/n junction associated with the RIE region.

The exact Round-57 scan pitch, spot diameter and quantitative pass/fail thresholds are `SYN` research-screening choices.

## 3. Witness geometry

W1 shall be derived from the same parent material and passivation state as D1/T1 and shall be co-processed through the same RIE chamber run.

Reference W1:

- isolated mesa sufficiently large for a `700 × 700 µm` scan field;
- central `300 × 300 µm` RIE-converted square;
- nominal RIE-square boundaries x=`±150 µm`, y=`±150 µm` relative to scan origin;
- remote electrical collector pads outside the diagnostic square;
- metal-exclusion/shadow feature keeps the central RIE square optically accessible after collector metallization.

Do not substitute D1 as the default LBIC specimen.

## 4. Reference measurement state

| Parameter | Reference implementation | Basis |
|---|---:|---|
| Temperature | 80.0 K | SL/RP |
| Optical wavelength | 1.047 µm CW | SL/PT |
| Irradiance | 400 mW/cm² nominal | SL/PT |
| Spot diameter | 10 µm 1/e²-equivalent nominal | SYN |
| Scan field | 700 × 700 µm | SYN |
| Scan pitch | 5 µm | SYN |
| External bias | 0 V | SYN / diagnostic |
| Readout | virtual-ground TIA current | SYN |
| Prescribed line scans | y = −100, −50, 0, +50, +100 µm | SYN |
| Lobe SNR | both signs >=5 sigma_0 | SYN |
| Boundary tolerance | lobe center within 50 µm of ±150-µm nominal RIE boundary | SYN |
| Witness pass | >=4 of 5 lines + consistent 2-D bipolar map | SYN |

## 5. Equipment

- cryostat capable of stable 80 K specimen temperature;
- 1.047-µm CW laser or traceably equivalent source;
- beam attenuation and irradiance calibration at specimen plane;
- scanning microscope/stage with <=5-µm positioning increment and recorded repeatability;
- spot-size measurement/qualification method;
- low-noise transimpedance amplifier operated at virtual ground;
- digitizer/lock-in as appropriate to the scanning modulation/readout implementation;
- coordinate registration to the RIE-mask geometry.

## 6. Procedure

1. Select W1 that shares parent material, anodization and RIE chamber treatment with the D1/T1 run being qualified.
2. Verify the central RIE square is optically exposed and measure its actual boundaries from optical/mask metrology.
3. Mount W1 in the cryostat and stabilize at `80.0 K`.
4. Configure zero external detector bias and virtual-ground current readout. Record any residual offset/current before optical excitation.
5. Set the 1.047-µm source to nominal `400 mW/cm²` at the specimen plane. Measure/record the actual irradiance and its uncertainty.
6. Measure/record the optical spot using the declared diameter convention. Target `10 µm` 1/e²-equivalent for the Round-57 reference implementation.
7. Register scan coordinates so the measured center of the 300×300-µm RIE square is `(0,0)`.
8. Acquire a `700 × 700 µm` LBIC map on a `5 µm` pitch or finer. Retain raw current and stage-coordinate data.
9. Estimate `sigma_0` from off-feature regions away from the RIE boundaries and any collector-metal artifacts. Preserve the region definition with the data.
10. Extract line profiles at y=`−100, −50, 0, +50, +100 µm` using the measured coordinate system.
11. For each line, identify the strongest positive and negative boundary-associated extrema. Require both magnitudes to be at least `5 sigma_0`.
12. Determine each lobe center using one frozen method (e.g. local extremum coordinate or fitted lobe centroid) and require the corresponding center to lie within `50 µm` of the appropriate nominal/measured x boundary near `−150` or `+150 µm`.
13. Mark a line PASS only if both signs and boundary-localization conditions are met.
14. Mark W1 PASS only when at least four of five prescribed lines pass and the full 2-D map shows a spatially consistent sign reversal associated with the RIE-square boundaries rather than isolated noise/collector artifacts.
15. Archive raw map, irradiance calibration, spot-size result, TIA transfer/gain, scan registration, `sigma_0`, line profiles and disposition.

## 7. Passivation / destructive comparison rule

The baseline W1 test is performed with the process passivation state intact.

If comparison with an oxide-stripped state is scientifically useful, use a **duplicate sacrificial W1** and a separately documented diluted-HCl strip derived from the historical diagnostic lineage. Never strip D1 merely to satisfy P37.

A difference between intact-oxide and stripped duplicate W1 is itself process information and shall not be silently averaged away.

## 8. Interpretation boundary

A P37 PASS is evidence that the co-processed RIE feature creates a reproducible spatially bipolar photoresponse consistent with the historical n+/n blocking-contact mechanism.

It does not alone prove:

- exact conversion depth;
- exact minority-carrier collection efficiency in D1;
- a production acceptance limit;
- equivalence across different RIE reactors;
- detector-level D* performance.

P37 is therefore combined with TLM/contact data and later detector measurements.

## 9. Research handoff

For the Round-57 reference program:

`TLM/LBIC -> detector tests`

requires:

- Protocol-14 `rho_c` within the declared research-screening range around the RP-01 benchmark; and
- P37 W1 PASS.

TLM alone is insufficient.

## 10. Troubleshooting

| Observation | Likely cause | Response |
|---|---|---|
| No signal anywhere | optical/readout/collector failure | Verify irradiance, TIA gain, electrical continuity and scan registration before changing RIE. |
| One-sign response only | geometry/readout asymmetry or no bipolar junction signature | Check collector geometry, zero-bias condition and polarity; repeat on duplicate W1 before interpreting conversion failure. |
| Bipolar lobes displaced far from boundary | registration error, lateral conversion, optical spot/collector artifact | Re-register mask geometry; compare lateral conversion metrology; inspect 2-D map. |
| Only isolated >5-sigma pixels | noise/spurious pickup | Require line-profile morphology and 2-D spatial consistency; do not pass by peak threshold alone. |
| Intact/stripped W1 differ strongly | passivation/interface contribution | Preserve both datasets; do not assume the stripped state is the finished-device state. |

## 11. Evidence classification

- `SL/PT`: 1.047-µm CW / ~400 mW cm^-2 / 80-K bipolar LBIC evidence on RIE regions.
- `SYN`: W1 mask details, 10-µm spot target, scan field/pitch, zero-bias virtual-ground implementation and numerical 5-sigma/4-of-5 research screen.

These SYN thresholds remain research criteria until correlated with detector-level blocking/performance across repeated process runs.
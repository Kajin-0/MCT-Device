# Source-ledger addendum — Round 52 manuscript adversarial review

**Date:** 2026-08-16 America/New_York

## Scope

Round 52 did not add a new external source family. It re-audited already controlled primary/same-lineage/metrology sources against the integrated Draft 0.1 manuscript and corrected how several existing facts are represented.

## Source-use corrections

### Smith et al. 2001 / RP-01

Retain as direct:

- Figures 3, 5, 6 and 7 correspond to the same representative device;
- Figure-5 noise state includes 80 K, 10 V/cm, stated 60° FOV, low-noise preamplifier and HP35665A;
- high-frequency g-r noise is approximately 24.5 nV/sqrt(Hz) and the historical 1/f knee is about 3 kHz;
- RIE-converted carrier density `~2.0e15 cm^-3` is reported averaged over the converted thickness;
- RIE-converted mobility `~3.3e4 cm²/Vs`;
- exact performance-device contact pair/gap remains unrecovered;
- exact D* noise-frequency/reduction convention remains unrecovered.

### P08B / same-UWA RIE conversion-depth lineage

Use the cited approximately 8-um converted-depth scale only as same-lineage/conditional context. Do not treat it as the proven RP-01 reduction thickness unless that historical linkage is recovered.

### P11A radiometry lineage

Retain the 60° full-cone / 30° half-angle interpretation only as a derived consistency result because it reproduces the reported 300-K photon-flux scale reasonably. It is not documentary proof of the historical aperture convention.

### P20A uncertainty architecture

Retain the distinction between D* normalization area and optical incident-power geometry. If the same area coordinate affects both, preserve covariance. Do not impose physical equality between detector normalization area and beam/aperture area when the measurement equation defines them separately.

### P36/P36A commissioning architecture

Promote these modules into the main manuscript crosswalk. They define the future laboratory's tool/metrology acceptance logic and therefore are the correct bridge between a reference manual and an executable local traveler.

## Numerical authority

The authoritative LPE elemental-mass conversion remains:

`calculations/LPE_CHARGE_COMPOSITION_SENSITIVITY.md`

with Hg 200.59, Cd 112.414, Te 127.60 g/mol and:

- `w_Hg=0.2497382358`;
- `w_Cd=0.01250164993`;
- `w_Te=0.7377601143`.

No source reclassification occurred in Round 52.

## Negative evidence retained

No reviewed source closes the remaining universal/local values for future-lab furnace offsets, MFC calibration, total LPE charge mass, exact local lithography dose, QCM tooling factors, package bondline geometry, or optical view factor. These remain local calibration/qualification coordinates, not missing numbers to infer from generic practice.
# RP-01 gap-matrix addendum — Round 56

**Date:** 2026-08-16 America/New_York

## Closed Round-55 publication blockers

### G56-01 — detector/TLM mask geometry contradiction

**Round 55:** one `500 × 500 µm` mesa was presented as though it could support the direct RP-01 nine-contact TLM string.

**Round 56:** separate geometries are defined:

- D1 `900 × 500 µm`, two `300 × 300 µm` contacts, 100-µm reference gap;
- T1 `5000 × 500 µm`, nine `300 × 300 µm` contacts with 50–400-µm gaps;
- direct contact-string minimum longitudinal envelope = `4500 µm`.

State: `CLOSED-IN-PUBLICATION`.

### G56-02 — anodization lacked physical anode/current geometry

Round 56 adds temporary anode-contact patch, PTFE fixture, wetted-area equation, sidewall inclusion, lead protection, microampere current examples and source-resolution target.

State: `CLOSED-IN-PUBLICATION`.

### G56-03 — transient protocol undersampled the excitation

Round 56 replaces 20-ns interval with 500-MS/s / 2-ns acquisition and adaptive >=10-tau record length.

State: `CLOSED-IN-PUBLICATION`.

## Major scientific framing gaps repaired

### G56-04 — upstream process could be misread as RP-01 growth reconstruction

Protocols 1–7 are now explicitly labeled a **composite literature-derived upstream material hypothesis**. Smith purchased the Fermionics material; the reconstructed growth branch is a research hypothesis.

State: `CLOSED-IN-PUBLICATION`.

### G56-05 — fixed wet-mesa timing lacked rate margin

Fixed 4.00-min production time removed. Same-bath witness rate now determines `t_etch=(t_epi+d_overetch)/r_witness`.

State: `CLOSED-IN-PUBLICATION`.

### G56-06 — FTIR inverse problem underspecified

Model identity, optical stack, fit objective, bounds, instrument convolution, beam footprint, residual/covariance output and physical-thickness cross-check are now explicit.

State: `SUBSTANTIALLY-CLOSED-IN-PUBLICATION`; exact Hougen coefficient implementation/version still must accompany real data.

### G56-07 — Hall-density terminology too strong

Round 56 reports `n_H` and `mu_H`, not unqualified microscopic carrier concentration. Weak-field fit is separated from high-field diagnostics.

State: `CLOSED-IN-PUBLICATION`.

### G56-08 — D* area convention ambiguous

RP-comparison area is frozen to active optical region between planar contacts: `A_Dstar=L_gap*W_active`.

State: `CLOSED-IN-PUBLICATION`.

### G56-09 — noise metrology incomplete

Round 56 specifies an analog anti-alias filter, independent periodograms, approximate degrees of freedom/confidence interval, same-state closure and source-level 1-kHz/~3-kHz ambiguity.

State: `CLOSED-AS-REFERENCE-METHOD`; final uncertainty budget remains empirical.

### G56-10 — false process precision

Nominal setpoints are rounded to realizable scales and separated from instrument accuracy/calibration/process criteria.

State: `SUBSTANTIALLY-CLOSED`; continue auditing individual SYN values.

## Remaining high-priority scientific gaps

1. Empirical validation of the combined upstream LPE recipe remains open.
2. Absolute LPE charge/hardware/synthesis compatibility remains cross-lineage.
3. Hg anneal state boundary remains material-dependent and requires experiment.
4. Exact modern Mask-1/Mask-2 resist transfer still requires lithography qualification.
5. RIE reactor equivalence requires measured self-bias/thermal/conversion-state data.
6. Cr/Au transfer settings require actual QCM/contact data.
7. Cryogenic package construction requires measured thermal/mechanical/noise data.
8. Final detector performance requires same-device/state responsivity/noise/dynamics data.
9. Numerical research-screening gates are not production process capability limits.

## Maturity

- `RP01-EMPIRICAL-PROTOCOL-ROUND56-REVIEW-CANDIDATE = YES`.
- `TRACEABLE-FIRST-BUILD-READY = NO` for an unspecified/uninstantiated laboratory.
- `HISTORICAL-RP01-REPRODUCED = NO`.
- `REPRODUCIBLE-RELEASE = NO`.

# RP-01 gap-matrix addendum — Round 57

**Date:** 2026-08-16 America/New_York

## Major Round-56 re-review findings closed in publication

### G57-01 — `10 V/cm` field definition ambiguous

**Problem:** D1 has only two contacts. Round 56 called for active-region voltage but did not define how contact drops were separated, and Smith’s historical applied-field convention is terminal voltage divided by contact spacing.

**Round 57:** freeze and report both:

- `E_Smith=V_terminal/L_gap` for direct historical comparison;
- `E_bulk,est=[V_terminal-I(Rc1+Rc2)]/L_gap` using TLM-derived contact estimates.

`E_bulk,est` is explicitly an estimate, not a measured Kelvin voltage.

State: `CLOSED-IN-PUBLICATION`.

### G57-02 — absolute optical power lacked beam-footprint closure

**Round 57:** canonical Protocol 18 is underfilled spectral radiant-power comparator mode. D1 100×300-µm gap must contain >=99% measured beam power; <=60-µm stated diameter at 3.0/4.0/4.4/5.0 µm; center ±10 µm; reference/DUT plane mismatch <=0.10 mm. Otherwise use a separately defined irradiance method.

State: `CLOSED-AS-REFERENCE-METROLOGY`.

### G57-03 — LBIC required but not executable

**Round 57:** new W1 witness / P37 protocol at 80 K, 1.047 µm CW, ~400 mW/cm², 10-µm nominal spot, 700×700-µm map, 5-µm pitch, five prescribed line scans and quantitative 5-sigma bipolar-boundary criterion.

State: `CLOSED-IN-PUBLICATION`.

## Secondary findings closed or substantially closed

### G57-04 — seven-run LPE design overcalled a response surface

Renamed a blocked `2² + center` factorial validation screen. Independent source syntheses B/C provide center blocks. Optional axial points are separate if a quadratic surface is desired.

State: `CLOSED-IN-PUBLICATION`.

### G57-05 — T1 finite-width spreading not modeled

Primary TLM reduction now uses a 2-D sheet/contact PDE with actual 500-µm mesa and 300-µm pads; long-contact relation only cross-checks scale.

State: `CLOSED-AS-REFERENCE-METHOD`; actual solver/mesh convergence remains implementation data.

### G57-06 — singulation mechanics incomplete

Round-57 SYN starting branch specifies actual 100-µm cutting wire, 5.0-N tension, 20 m/min wire speed, 0.020 mm/min feed, 16-µm BN and 10-wt% slurry. Source “125-mm saw” wording is retained only as source text, not treated as wire diameter.

State: `CLOSED-AS-REFERENCE-IMPLEMENTATION`.

### G57-07 — transient record length and repetition period could conflict

`T_record>=10 tau_slowest`, `T_rep>=T_record+5 tau_slowest`, with baseline-recovery gate and 1-kHz only as an upper cap.

State: `CLOSED-IN-PUBLICATION`.

### G57-08 — FTIR g/s definitions and coefficient identity incomplete

Round 57 defines z coordinate and `x(z)=x0+g(z/d−0.5)`; optional `s_x` is manual Gaussian composition-smear parameter, not Hougen nomenclature. Real data must archive exact implementation/coefficient paths and hashes.

State: `SUBSTANTIALLY-CLOSED`; the manual does not invent unavailable original coefficients.

### G57-09 — wet-etch witness insufficiently geometry matched

Witness is now same AZ4620 stack, orientation, representative 500×500-µm opening scale, co-immersed near D1 in the same bath.

State: `CLOSED-IN-PUBLICATION`.

### G57-10 — PSD DOF assumed from non-overlap alone

Round 57 requires lag-1 correlation and first-half/second-half stationarity screens before using nominal 128 per-bin DOF. The fixed 995–1005-Hz band final estimator gets a record-level bootstrap interval.

State: `CLOSED-AS-REFERENCE-METHOD`.

## Remaining scientific gaps

1. The composite upstream LPE/anneal route remains unvalidated as a combined process.
2. Many `SYN` lithography, metallization, packaging and mechanical values remain reference starting points rather than demonstrated optima/process windows.
3. Actual FTIR coefficient/model implementation and uncertainty must be frozen with real run data.
4. LBIC quantitative screen is a Round-57 research criterion; it must itself be validated against detector blocking behavior before it can become a production acceptance limit.
5. The finite-width TLM solver requires mesh/model verification on real geometries.
6. Absolute responsivity requires actual measured beam-profile/overlap and calibrated reference-detector uncertainty.
7. Same-device responsivity/noise/dynamics and empirical package thermal response remain unmeasured in this literature-only project.
8. Research continuation gates are not production capability/tolerance specifications.

## Maturity

- `RP01-EMPIRICAL-PROTOCOL-ROUND57-REVIEW-CANDIDATE = YES`.
- `TRACEABLE-FIRST-BUILD-READY = NO` for an unspecified/uninstantiated laboratory.
- `HISTORICAL-RP01-REPRODUCED = NO`.
- `REPRODUCIBLE-RELEASE = NO`.
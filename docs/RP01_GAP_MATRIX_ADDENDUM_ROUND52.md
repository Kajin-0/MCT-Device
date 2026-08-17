# RP-01 gap-matrix addendum — Round 52 manuscript adversarial review

**Date:** 2026-08-16 America/New_York

## Purpose

Record gap-state changes caused by the Draft-0.1 adversarial review. This addendum changes manuscript interpretation/control; it does not promote any physical laboratory maturity state.

## Closed manuscript gaps

### G52-01 — reproducibility title overclaim

**Before:** manuscript title could be read as asserting a demonstrated reproducible process.

**After:** closed in Draft 0.2 by retitling to source-traceable qualification fabrication/characterization.

State: `MANUSCRIPT-CLAIM-CORRECTED`.

### G52-02 — reference-center / executable-branch ambiguity

**Before:** literature qualification centers were labeled correctly but some imperative wording could still be read as executable.

**After:** closed by the irreversible-step preflight rule. `[REF-CENTER] != executable local setpoint` is now normative.

State: `MANUSCRIPT-EXECUTION-SEMANTICS-CLOSED`.

### G52-03 — P36/P36A integration omission

**Before:** integrated manuscript crosswalk stopped at P35.

**After:** P36/P36A are now normative commissioning/preflight references.

State: `MANUSCRIPT-COMMISSIONING-CROSSWALK-CLOSED`.

### G52-04 — RIE volume-density depth coupling

**Before:** the reference table could be read as treating `2.0e15 cm^-3` as an independent converted-region target.

**After:** Draft 0.2 explicitly states the density is averaged over converted thickness and requires `R_s/N_s/mu_H/d_conv/L_conv/d_etch/rho_c/blocking_response` to be tracked separately.

State: `MANUSCRIPT-RIE-DEPTH-COUPLING-CLOSED`.

### G52-05 — D* area/power convention

**Before:** wording implied D* normalization area and optical incident-power area had to be physically identical.

**After:** Draft 0.2 defines `A_Dstar` separately from optical geometry and requires covariance when a common area enters `P_inc`.

State: `MANUSCRIPT-DSTAR-AREA-CONVENTION-CLOSED`.

### G52-06 — RP-01 same-device performance chain

**Before:** manuscript required matched states but did not strongly exploit P12C closure that Figures 3/5/6/7 are the same representative device.

**After:** same-device/contact/state lock is normative for new D* closure unless explicitly corrected.

State: `MANUSCRIPT-PERFORMANCE-STATE-IDENTITY-CLOSED`.

### G52-07 — 60-degree FOV convention

**Before:** 60° was called nominal but full-cone/half-angle ambiguity was not prominent enough.

**After:** physical geometry and angle convention are mandatory; 60° full cone / 30° half-angle is retained only as a derived flux-consistency interpretation.

State: `MANUSCRIPT-FOV-CONVENTION-CLOSED`.

## Deliberately still open

These remain legitimate local/historical gaps and must not be numerically invented:

- actual future-lab LPE charge mass/boat dimensions/thermal offsets/gas flows/contact trajectory;
- actual anneal enclosure/Hg inventory/thermal offsets and released trajectory;
- exact Mask-1 and Mask-2 commercial process identities;
- exact Br2 and EG:HBr historical preparation bases;
- exact anodization 90:10 solvent-ratio basis for the transfer disclosure and exact UWA/RP-01 cell;
- exact RP-01 Plasma Technology model, self-bias, sample temperature, individual MFC settings, and converted-depth reduction basis;
- exact deposition method/vacuum/rates/QCM factors;
- exact RP-01 FOV hardware, Optronics chain, preamp/analyzer configuration, and D* reduction convention;
- singulation/package historical construction;
- direct RP-01 lifetime/frequency response.

## Known controlled internal discrepancy

`calculations/LPE_CHARGE_COMPOSITION_SENSITIVITY.md` is authoritative for the LPE mass convention:

- Hg 200.59;
- Cd 112.414;
- Te 127.60 g/mol;
- `w_Hg=0.2497382358`;
- `w_Cd=0.01250164993`;
- `w_Te=0.7377601143`.

One P30A section retains older ppm-scale rounded values from the previously logged numerical erratum. Draft 0.2 uses the authoritative calculation values. The P30A text should be repaired/annotated in a later housekeeping pass; it is not allowed to override the calculation module.

## Maturity effect

New document state:

`RP01-MANUSCRIPT-ADVERSARIAL-REVIEW-PASSED = YES`.

Unchanged physical states:

- `TRACEABLE-FIRST-BUILD-READY = NO` for an unspecified/uninstantiated lab;
- `HISTORICAL-RP01-REPRODUCED = NO`;
- `REPRODUCIBLE-RELEASE = NO`.
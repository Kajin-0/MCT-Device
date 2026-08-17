# Checkpoint after adversarial empirical-protocol repair — Round 56

**Date:** 2026-08-16 America/New_York  
**Repository:** `Kajin-0/MCT-Device`

## Input review disposition

The Round-55 34-page empirical protocol was subjected to an extreme methods-referee review. The review found the arithmetic and much of the characterization logic strong, but identified three non-negotiable release blockers and several major transfer/metrology weaknesses.

Round 56 repairs the publication rather than defending Round 55.

## Three blockers repaired

1. **Mask geometry:** detector and TLM structures are now separate. D1 is 900×500 µm with two 300×300 µm contacts and a 100-µm reference gap. T1 is 5000×500 µm and contains the nine-contact 50–400-µm gap string whose minimum envelope is 4500 µm.
2. **Anodization integration:** actual temporary anode contact, PTFE fixture, dry-contact patch, sidewall-inclusive wetted area and microampere current calculations are specified. Nominal D1 current is ~1.40 µA; T1 ~7.78 µA.
3. **Transient acquisition:** 500 MS/s / 2-ns sampling replaces the Round-55 20-ns interval. Initial record is 100 µs; final record extends to >=10× the slowest fitted detector pole; package thermal recovery is measured on a separate slow time base where necessary.

## Major framing repair

Protocols 1–7 are no longer allowed to read as an RP-01 upstream growth reconstruction. Smith et al. purchased the Fermionics LPE material. The upstream section is labeled **COMPOSITE LITERATURE-DERIVED UPSTREAM MATERIAL HYPOTHESIS**.

The 500 °C / 5 min LPE point is now the center of a seven-run validation matrix, not an asserted optimum.

## Additional repairs

- same-bath witness-calibrated wet-mesa time;
- explicit 48-wt% HBr reference stock definition;
- explicit FTIR inverse model and uncertainty/covariance outputs;
- Hall-density/Hall-mobility terminology and weak-field-first analysis;
- Hg reservoir mass treated only as vapor non-starvation evidence;
- practical RIE flow precision + MFC/self-bias/thermal recording;
- Cr/Au QCM witness and sample-temperature controls;
- corrected interpretation of the Honeywell silicone/5-g/40-g experiment;
- pulse-width/duty self-heating extrapolation to zero deposited energy;
- D* area frozen to inter-contact active region;
- analog anti-alias filtering and PSD confidence logic;
- explicit preservation of Smith’s 1-kHz spectral / ~3-kHz noise-knee ambiguity;
- value-level source location/transfer-delta table;
- explicit research continuation gates between process families;
- reduced false precision.

## Artifact state

Round-56 files:

- `RP01_HgCdTe_Empirical_Protocol_Manual_Round56.docx`
- `RP01_HgCdTe_Empirical_Protocol_Manual_Round56.pdf`

QA:

- final length: 37 pages;
- DOCX accessibility: 0 high / 0 medium / 0 low findings;
- all DOCX-render pages visually inspected after two pagination repairs;
- PDF inspector/preflight: 37 letter-size pages, unencrypted, openable, text-native, zero form fields;
- all 37 PDF pages independently rendered at 200 dpi and visually inspected.

SHA-256:

- DOCX `9b9388aa3963489787c72e5899140202eae74ed0f5549e1eacd33b95b946ab21`;
- PDF `697212dca8b4808b9d2cba1a16437f08b569bbf1be9e06c1b2a588379c4cf71c`.

## Current maturity

`RP01-EMPIRICAL-PROTOCOL-ROUND56-REVIEW-CANDIDATE = YES`.

Still false:

- `TRACEABLE-FIRST-BUILD-READY` for an unspecified lab;
- `HISTORICAL-RP01-REPRODUCED`;
- `REPRODUCIBLE-RELEASE`.

## Next work

Continue with adversarial review of remaining SYN values and cross-lineage interactions. Priority targets are upstream LPE synthesis/hardware, Hg anneal state map, Mask-1/Mask-2 modern resist implementation, RIE reactor equivalence, metallization transfer, and package bondline/interconnect construction. Preserve the hard-number recipe model; strengthen weak values rather than reverting to blank fields.

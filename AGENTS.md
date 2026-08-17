# AGENTS.md — MCT-Device continuity record

**Current continuity round:** 56  
**Date:** 2026-08-16 America/New_York  
**Repository:** `Kajin-0/MCT-Device`

## User-facing mission

Produce a source-traceable **empirical protocol manual** for HgCdTe photoconductor fabrication and characterization. The publication should read as a hard-number experimental methods paper rather than a condensed review, manufacturing traveler, or blank-field SOP.

Canonical downstream historical anchor:

E. P. G. Smith, K. J. Winchester, C. A. Musca, J. M. Dell, L. Faraone, “A simplified fabrication process for HgCdTe photoconductive detectors using CH4/H2 reactive-ion-etching-induced blocking contacts,” *Semiconductor Science and Technology* 16, 455–462 (2001), DOI `10.1088/0268-1242/16/6/306`.

## READ FIRST

1. `docs/RP01_EMPIRICAL_PROTOCOL_REPAIR_ROUND56.md` — active scientific disposition after adversarial review.
2. `research/2026-08-16_checkpoint_after_empirical_protocol_round56.md` — latest continuity checkpoint.
3. `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND56.md` and `docs/SOURCE_LEDGER_ADDENDUM_ROUND56.md`.
4. `manuscript/RP01_HGCDTE_PHOTOCONDUCTOR_PROCESS_MANUAL_DRAFT.md` — integrated technical source draft.
5. Detailed `procedures/P01...P36A`, calculations, and prior source-ledger material remain the technical evidence corpus.
6. Round 55 is retained as superseded review history; do not restore its known blocker defects.

## Current publication state

- `RP01-EMPIRICAL-PROTOCOL-ROUND56-REVIEW-CANDIDATE = YES`.
- `ROUND55-RELEASE-BLOCKERS-REPAIRED-IN-PUBLICATION = YES`.
- `TRACEABLE-FIRST-BUILD-READY = NO` for an unspecified/uninstantiated laboratory.
- `HISTORICAL-RP01-REPRODUCED = NO`.
- `REPRODUCIBLE-RELEASE = NO`.

Round 56 is an **adversarially repaired literature-derived experimental protocol candidate**. It is not an end-to-end validated fabrication process.

## Round-56 architecture

The document retains 20 self-contained protocols using:

`objective -> starting state -> equipment/materials -> hard-number reference recipe -> numbered procedure -> timing -> expected result -> analysis -> troubleshooting -> evidence note`.

The main text contains no fill-in-the-blank fields.

Evidence codes remain:

- `RP` — direct Smith/RP-01 value;
- `SL` — same-lineage method/value;
- `PT` — primary transfer evidence;
- `DER` — derived quantity;
- `SYN` — explicit synthesized empirical starting choice.

`SYN` never means historical identity or empirical validation.

## Critical Round-56 repairs

### 1. Detector and TLM geometry separated

Round 55 incorrectly placed the published nine-contact TLM string on a 500 × 500 µm mesa even though the contacts plus 50–400 µm gaps require a 4500 µm minimum longitudinal envelope.

Round 56 defines separate structures:

- `D1` detector mesa: `900 × 500 µm`; two `300 × 300 µm` contacts; `100 µm` reference gap; nominal `100 µm` longitudinal margins.
- `T1` TLM mesa: `5000 × 500 µm`; nine `300 × 300 µm` contacts with successive `50,100,...,400 µm` gaps; minimum published contact-string envelope `4500 µm`; `250 µm` nominal end margins.

Never use T1 geometry as the detector optical active area and never put the nine-contact string on D1.

### 2. Anodization fixture instantiated

The TI anodization chemistry remains a strong transfer anchor, but Round 56 adds the missing electrical geometry for isolated mesas.

Reference implementation:

- `0.100 M KOH` in `900 mL EG + 100 mL DI water`;
- HgCdTe is the anode; carbon rod cathode;
- `0.300 mA/cm²` for `120 s`, expected ~`15 V`, ~`80 nm` deep-blue oxide;
- PTFE fixture and PTFE-coated spring microprobe;
- dry temporary-contact patch `100 × 100 µm`, wholly inside a future metal-contact window;
- wetted area includes mesa top outside the dry patch plus sidewalls;
- D1 nominal wetted area ~`0.00467 cm²` -> current ~`1.40 µA`;
- T1 nominal wetted area ~`0.02595 cm²` -> current ~`7.78 µA`;
- current-source target accuracy `<=1% of setpoint or +/-20 nA, whichever is larger`.

Isolated mesas are anodized sequentially unless independently controlled contacts exist.

### 3. Transient acquisition repaired

Round 55 used a 20-ns interval for a 25-ns pulse, only 1.25 sample intervals.

Round 56 uses:

- `500 MS/s`;
- `2.0 ns` interval;
- ~`12.5` intervals across a 25-ns source pulse;
- initial record `100 µs`, `50,000` samples, `10 µs` pretrigger;
- `128` averages;
- final record length `>=10 × tau_slowest`;
- separate slower package-thermal acquisition where necessary.

Do not infer `f_3dB=1/(2*pi*tau)` unless a one-pole transfer function is empirically justified.

## Upstream material branch is not RP-01 reconstruction

Smith et al. purchased the starting LPE HgCdTe/CdZnTe material from Fermionics. Therefore Protocols 1–7 are now explicitly labeled:

**COMPOSITE LITERATURE-DERIVED UPSTREAM MATERIAL HYPOTHESIS**.

The LPE center retains the composition-matched Honeywell tie line `xL=.082, yL=.810, TL=507 °C -> xS≈.29`, but absolute charge, synthesis, boat execution and growth schedule combine separate primary lineages.

Round-56 validation matrix for the explicit 500 °C / 5 min center:

- 497 °C / 3 min;
- 497 °C / 7 min;
- 503 °C / 3 min;
- 503 °C / 7 min;
- three independent center runs at 500 °C / 5 min.

Do not call 500 °C / 5 min an established optimum until this or stronger empirical validation exists.

## Other Round-56 scientific repairs

- Wet mesa is now same-bath witness-calibrated, not fixed at 4.00 min: `t_etch=(t_epi+d_overetch)/r_witness`, `d_overetch=max(1.0 µm,0.10*t_epi)`.
- Round-56 reference HBr implementation is explicitly `48 wt% aqueous HBr`; this is a SYN reagent definition, not Srivastav historical identity.
- FTIR now freezes an explicit coherent-film/incoherent-substrate full-spectrum inverse model, fit bounds, residual weighting, beam-footprint rule, covariance reporting and physical-thickness cross-check.
- Hall output is `n_H`/`mu_H`, not unqualified true carrier density; fit weak-field data first (`|B|<=0.10 T`) and use higher fields diagnostically.
- Anneal Hg inventory is treated only as a non-starvation check; carrier-state outcome still requires paired Hall/FTIR validation.
- RIE individual nominal flows are rounded to realizable setpoints (`10.7 sccm CH4`, `53.3 sccm H2`) with actual MFC uncertainty recorded; direct historical authority remains total 64 sccm, 100 mTorr, 50 W, 60 s.
- Cr/Au rates and vacuum remain SYN transfer settings with QCM witness closure and sample-temperature ceiling.
- Packaging text no longer implies 5 g is a Honeywell optimum; both silicone/40-g and silicone/5-g historical branches survived, so compliance is the causal evidence.
- DC self-heating uses pulse-width/duty sweeps and zero-deposited-energy extrapolation rather than one 10-ms pulse test.
- RP-comparison D* area is frozen as `A_Dstar=L_gap*W_active`; nominal D1 `100 µm × 300 µm = 3.00e-4 cm²`; do not substitute mesa area.
- Noise metrology includes explicit analog anti-alias filtering, independent-record PSD averaging, approximate DOF/confidence interval and preservation of the historical 1-kHz/~3-kHz source ambiguity.
- False numerical precision is reduced: process records distinguish nominal setpoint, instrument resolution/calibration uncertainty and allowed research-screening criterion.
- Critical transferred numbers now have source-location / transfer-delta entries in the publication.

## Round-56 research continuation gates

The manual now inserts explicit research gates between process families so a failed state is not carried downstream simply because the next tool is available. These are research-screening criteria, not historical production tolerances.

Examples:

- LPE -> anneal: FTIR/morphology plus completion of the seven-run validation matrix.
- anneal -> lithography: N-like state; `n_H 4.9e14–2.0e15 cm^-3`; `mu_H>=3e4 cm²/Vs`; no paired optical-edge shift beyond `3 sigma_pair`.
- mesa -> anodize: measured depth >= `t_epi+d_overetch` and verified electrical isolation.
- anodize -> Mask 2: oxide metrology/V(t) closure.
- RIE -> metal: oxide-clear and converted-state evidence plus reactor thermal/self-bias state.
- TLM -> detector: majority-contact metric plus independent functional blocking evidence.
- package -> optical/noise: cryogenic cycles plus measured package thermal pole.
- responsivity/noise -> D*: same detector/contact/geometry/T/E/FOV/loading/frequency state.
- transient claim: source/readout/package de-embedding and adequate record length.

## Round-56 artifact QA

Review artifacts:

- `RP01_HgCdTe_Empirical_Protocol_Manual_Round56.docx`
- `RP01_HgCdTe_Empirical_Protocol_Manual_Round56.pdf`

Final render:

- `37 pages`;
- monochrome and text-native;
- zero PDF form fields;
- DOCX accessibility audit `0 high / 0 medium / 0 low`;
- all DOCX-render pages visually reviewed after pagination repairs;
- PDF inspector/preflight: letter size, openable, unencrypted, not scanned;
- all 37 PDF pages independently rendered at 200 dpi and visually reviewed.

SHA-256:

- DOCX `9b9388aa3963489787c72e5899140202eae74ed0f5549e1eacd33b95b946ab21`.
- PDF `697212dca8b4808b9d2cba1a16437f08b569bbf1be9e06c1b2a588379c4cf71c`.

The binary files remain conversation review artifacts. Repository Markdown/procedure/calculation files remain the controlled evidence corpus until a final validated issue exists.

## Immediate next work

Do not reopen the three repaired blocker defects. The next scientific pass should adversarially audit the remaining SYN values, especially cross-lineage LPE and anneal assumptions, lithography implementation, reactor equivalence, metallization transfer, and package construction. Replace weak SYN choices with stronger hard-number evidence or physics; do not revert to blank fields and do not promote them to validated process windows without experiments.

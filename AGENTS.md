# AGENTS.md — MCT-Device continuity record

**Current continuity round:** 59  
**Date:** 2026-08-17 America/New_York  
**Repository:** `Kajin-0/MCT-Device`

## User-facing mission

Produce an **exhaustive research-fabrication protocol** for HgCdTe photoconductor fabrication and characterization: a hybrid of a scientific methods monograph, an SOP, and a process-development laboratory reference. The document should preserve essentially every experimentally useful detail that can be recovered, derived, or defensibly synthesized.

The dominant question on every protocol page is:

> What exactly does the researcher do, with what material, tool, geometry, quantity, timing, measurement, calculation, acceptance criterion, failure response, and retained raw data?

Explanatory physics is included when it improves execution or interpretation, but execution remains primary. Do not revert to blank-field traveler formatting or condensed review-article prose.

Canonical downstream historical anchor:

E. P. G. Smith, K. J. Winchester, C. A. Musca, J. M. Dell, L. Faraone, “A simplified fabrication process for HgCdTe photoconductive detectors using CH4/H2 reactive-ion-etching-induced blocking contacts,” *Semiconductor Science and Technology* 16, 455–462 (2001), DOI `10.1088/0268-1242/16/6/306`.

## READ FIRST

1. `docs/RP01_OPERATOR_COMPLETENESS_LATEX_ROUND59.md` — active presentation/operator-completeness disposition.
2. `research/2026-08-17_checkpoint_after_operator_completeness_round59.md` — latest continuity checkpoint.
3. `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND59.md` and `docs/SOURCE_LEDGER_ADDENDUM_ROUND59.md`.
4. Round-57 scientific/metrology closure remains controlling where Round 59 did not intentionally add a SYN execution coordinate:
   - `docs/RP01_EMPIRICAL_PROTOCOL_METROLOGY_CLOSURE_ROUND57.md`;
   - `procedures/P37_LBIC_BLOCKING_CONTACT_FUNCTIONAL_QUALIFICATION.md`;
   - `analysis/ftir/ROUND57_FTIR_MODEL_SPECIFICATION.md`.
5. Detailed P01–P37 procedures, calculations and source ledger remain the technical evidence corpus.

## Current publication state

- `RP01-EXHAUSTIVE-EMPIRICAL-PROTOCOL-ROUND59-OPERATOR-CANDIDATE = YES`.
- Round 59 is a **mathematical-typesetting and operator-completeness revision** of the Round-57 scientific/metrology baseline plus explicitly labeled new SYN execution coordinates.
- `TRACEABLE-FIRST-BUILD-READY = NO` for an unspecified/uninstantiated laboratory.
- `HISTORICAL-RP01-REPRODUCED = NO`.
- `REPRODUCIBLE-RELEASE = NO`.

## Document class and grammar

The preferred label is **exhaustive research-fabrication protocol**. It is intentionally not forced into a conventional journal-paper or manufacturing-SOP template.

Each process follows approximately:

`physical objective -> starting state -> equipment/materials -> hard-number reference recipe -> numbered procedure -> timing -> expected result -> analysis/process notes -> troubleshooting -> evidence/transfer limits`.

The main body contains no blank traveler fields. A historically unrecovered parameter is handled by one of three paths:

1. direct/primary value if recovered;
2. derived or SYN hard-number starting implementation when defensible;
3. explicit apparatus-closure record when a number cannot responsibly be invented.

## Round-59 mathematical-typesetting closure

Native LaTeX is the active presentation layer.

Round 59 completes the residual notation cleanup begun in Round 58:

- variables are mathematical objects rather than ASCII/pseudo-code strings;
- inequalities, plus/minus tolerances and powers are typeset conventionally;
- equations and reductions are displayed/aligned where analytically meaningful;
- units and chemistry use consistent TeX notation;
- gate/provenance/troubleshooting tables use the same symbol definitions as the main protocol.

A targeted final source scan found no remaining matches for the pseudo-code patterns used in the Round-58 audit.

## Round-59 operator-completeness additions

### Substrate isolation

A SYN guarded leakage screen now gives an explicit first implementation:

- removable guarded electrodes separated by `5.0 mm`;
- apply `10 V`;
- settle `60 s`;
- record `30 s`;
- research screen `|I_leak| <= 10 nA` and final-30-s drift `<=1 nA`.

This is not an RP-01 historical limit.

### Te-rich source synthesis

Round 59 adds explicit engineering coordinates while refusing to invent unsupported quartz-wall geometry:

- empty-ampoule helium leak `<=1e-8 mbar L/s`;
- pre-seal pressure `<=1e-5 Torr` after a `30 min` isolated-manifold hold;
- `100 °C/h` ramp to `700 °C`;
- `8 h` dwell;
- `50 °C/h` cool to `300 °C`, then furnace-off cool;
- do not open above `23 °C`.

Ampoule quartz grade, ID/OD/wall, free volume, seal geometry and pressure/temperature qualification remain explicit apparatus records.

### Horizontal-slider LPE

New SYN execution coordinates include:

- N2 purge `>=5` measured tube-volume exchanges at `1 tube-volume/min`;
- purge endpoints `O2<10 ppm`, dew point `<-60 °C`;
- H2 process flow at `1 measured tube-volume/min` with actual sccm recorded;
- growth-region thermometry within `5 mm` equivalent location and dummy-boat correction uncertainty `<=1 °C`;
- nominal slider translation `2.0 mm/s`, measured stroke/travel within `±10%`;
- disposable CdTe scribed-apron reference with `1.0 mm` diagonal scribe pitch.

Exact historical boat machining dimensions remain unrecovered; Appendix C requires a local dimensioned drawing and thermal map instead of fabricated historical numbers.

### Mask 1

Round 59 exposes a complete first AZ4620 screening implementation:

- dispense `0.50 mL`;
- `4000 rpm / 30 s`;
- acceleration `1000 rpm/s`;
- `3.0±0.2 µm` target film;
- `365 nm / 300 mJ/cm²` nominal vacuum-contact exposure;
- exposure uniformity `±5%`;
- AZ400K:DI `1:4` at `21±1 °C`;
- gentle bath displacement every `15 s`;
- `60 s` DI rinse.

These are SYN transfer coordinates, not recovered RP-01 Mask-1 facts.

### Mask 2

Direct RP-01 anchors remain `4–5 µm`, `80 °C / 30 min` prebake and `30 min` chlorobenzene.

Round 59 supplies a concrete screening branch:

- `0.50 mL` dispense;
- `3500 rpm / 30 s`;
- `1000 rpm/s` acceleration;
- `4.3±0.3 µm` target;
- `365 nm / 150 mJ/cm²` nominal vacuum-contact exposure;
- `60 s` developer at `21 °C`;
- `60 s` DI rinse;
- re-entrant undercut witness target `0.3–1.0 µm` per side before D1/T1 enter RIE/metal.

### RIE

Carrier geometry is now explicit:

- specimen center within `5 mm` of powered-electrode center;
- same carrier revision used for thermal/self-bias qualification;
- full CdZnTe backside seating;
- no grease, adhesive or active-surface clamp shadow without a separate qualification branch.

Reactor-equivalence research screen:

- measured dc self-bias within `±10%` of the qualified reference;
- calibrated sample-temperature proxy `<=40 °C`.

Direct RP-01 controller state remains printed `CH4/5H2`, total `64 sccm`, `100 mTorr`, `50 W`, `60 s`.

### Cr/Au metallization

Direct RP-01 stack remains `30/270 nm` Cr/Au. Round-59 SYN thermal-evaporation geometry adds:

- nominal source-to-sample distance `150 mm`, maintained `±2 mm` after QCM qualification;
- sample rotation `10 rpm`;
- cool under vacuum to holder `<30 °C` for at least `10 min`;
- dry-N2 vent.

### Cryogenic packaging

Round 59 adds first-screen construction coordinates:

- detector-seat flatness `<=10 µm` over the die footprint;
- bondline `50±15 µm`, measured at four edges;
- die tilt `<=1°`;
- `25 µm` Au wire;
- first screening bond-force coordinate `5 gf`;
- sacrificial pull-test screen `>=2 gf` with no pad lift before D1;
- after cryogenic cycling, matched-state resistance change `<2%` and no new discrete excess-noise feature.

These are SYN research coordinates, not historical package facts.

### Absolute responsivity

The Round-57 underfilled radiant-power comparator geometry remains controlling. Round-59 SYN instrument-operation coordinates add:

- substitution-block source/reference stability `<=0.5%`;
- lock-in reference `1.000 kHz`;
- time constant `100 ms`;
- `24 dB/oct` low-pass;
- settle `>=5` lock-in time constants after wavelength motion;
- combined relative standard uncertainty target `<=5%` over `3–5 µm`.

## Explicit unresolved apparatus coordinates

Appendix C is a deliberate operator-completeness device, not a blank traveler.

It enumerates the exact remaining knowledge that must be generated or recovered for:

- source-synthesis ampoule geometry/qualification;
- horizontal-slider boat dimensions, clearances, well volumes and furnace/thermocouple map;
- Mask-1/Mask-2 tool-specific coating/exposure/development state;
- RIE electrode/carrier/self-bias/thermal equivalence;
- metallization source/QCM/holder geometry;
- package carrier/adhesive/wire-bond construction;
- responsivity optical-train/reference-detector implementation;
- noise/transient analog-chain and analysis-code identity.

Do not replace these with invented historical numbers merely for apparent completeness.

## Scientific state inherited from Round 57

Do not reopen these closures without stronger contrary evidence:

- D1 detector and T1 TLM geometries are separate and physically closed.
- Native-oxide anodization includes an explicit isolated-mesa anode/contact geometry and microampere current calculation.
- Transient sampling uses `500 MS/s / 2 ns` sampling with adaptive record and repetition periods.
- Protocols 1–7 remain a **COMPOSITE LITERATURE-DERIVED UPSTREAM MATERIAL HYPOTHESIS**, not an RP-01 historical growth reconstruction.
- Mesa etch is geometry-matched witness calibrated.
- FTIR uses an explicit full-spectrum inverse-model specification with archived model/coefficient hashes when real data are generated.
- Hall reports Hall quantities and separates weak-field one-carrier reduction from higher-field diagnostic behavior.
- Detector measurement reports both Smith-style terminal field and separately labeled contact-corrected bulk-field estimate.
- Absolute responsivity uses the defined underfilled spectral radiant-power comparator geometry.
- TLM alone does not prove blocking; P37/W1 LBIC is the functional blocking-contact witness gate.
- `A_Dstar` is the inter-contact optical area for direct RP comparison; do not substitute mesa area.
- The historical 1-kHz spectral / ~3-kHz noise-knee ambiguity is preserved rather than silently repaired.

Evidence codes remain `RP`, `SL`, `PT`, `DER`, `SYN`. A `SYN` hard number is a concrete empirical starting hypothesis, not validated process capability.

## Round-59 artifact state

Review artifacts:

- `RP01_HgCdTe_Exhaustive_Empirical_Fabrication_Protocol_Round59.pdf`
- `RP01_HgCdTe_Exhaustive_Empirical_Fabrication_Protocol_Round59.tex`

Final PDF state:

- `62` physical pages;
- letter size;
- text-native, openable and unencrypted;
- no XFA/form fields;
- all fonts embedded;
- all 62 final pages re-rendered and visually inspected after final pagination repair;
- no remaining overfull/underfull LaTeX box warnings;
- intermediate nearly blank anodization evidence page removed by consolidation.

SHA-256:

- PDF `bb51def36f7fdc8c25d595c8789286dd112938664adb0d96f5605141615d71ee`;
- TeX `352c170cca4c42d0bdeaea91878aa79e7020cdc12199ce69179ca81437dcc11b`.

The binary/TeX artifacts remain conversation review artifacts. Repository Markdown/procedure/calculation files remain the controlled scientific evidence corpus.

## Immediate next work

Use Round 59 as the preferred presentation/operator model. The next scientific pass should adversarially test the new SYN execution values and close Appendix-C apparatus coordinates from stronger primary evidence or actual local metrology where possible. Strengthen explicit details; do not regress to vague prose, blank fields, or pseudo-code mathematics.

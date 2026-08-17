# AGENTS.md — MCT-Device continuity record

**Current continuity round:** 60  
**Date:** 2026-08-17 America/New_York  
**Repository:** `Kajin-0/MCT-Device`

## User-facing mission

Produce an **exhaustive research-fabrication protocol** for HgCdTe photoconductor fabrication and characterization: a hybrid of a scientific methods monograph, an SOP, and a process-development laboratory reference. Preserve essentially every experimentally useful detail that can be recovered, derived, or defensibly synthesized.

The controlling question is:

> What exactly does the researcher do, with what material, tool, geometry, quantity, timing, measurement, calculation, acceptance criterion, failure response, and retained raw data?

This is **not** a manufacturing traveler. Do not add operator signoff forms, blank traveler fields, Cp/Cpk requirements, lot-release paperwork, or production-control charts merely to resemble manufacturing documentation.

Canonical downstream historical anchor:

E. P. G. Smith, K. J. Winchester, C. A. Musca, J. M. Dell, L. Faraone, “A simplified fabrication process for HgCdTe photoconductive detectors using CH4/H2 reactive-ion-etching-induced blocking contacts,” *Semiconductor Science and Technology* 16, 455–462 (2001), DOI `10.1088/0268-1242/16/6/306`.

## READ FIRST

1. `docs/RP01_DEEP_RESEARCH_APPARATUS_INTEGRATION_ROUND60.md` — Round-60 deep-research integration and apparatus findings.
2. `research/2026-08-17_checkpoint_after_deep_research_round60.md` — latest checkpoint.
3. `docs/SOURCE_LEDGER_ADDENDUM_ROUND60.md` — new source families and evidence restrictions.
4. Round-57 scientific/metrology closure remains controlling where Round 60 did not intentionally add a better-supported execution/apparatus coordinate:
   - `docs/RP01_EMPIRICAL_PROTOCOL_METROLOGY_CLOSURE_ROUND57.md`;
   - `procedures/P37_LBIC_BLOCKING_CONTACT_FUNCTIONAL_QUALIFICATION.md`;
   - `analysis/ftir/ROUND57_FTIR_MODEL_SPECIFICATION.md`.
5. Detailed P01–P37 procedures, calculations and source ledger remain the technical evidence corpus.

## Current publication state

- `RP01-EXHAUSTIVE-EMPIRICAL-PROTOCOL-ROUND60-DEEP-RESEARCH-CANDIDATE = YES`.
- Round 60 integrates a primary/official-source deep-research pass into the Round-59 LaTeX/operator-completeness document.
- `TRACEABLE-FIRST-BUILD-READY = NO` for an unspecified/uninstantiated laboratory.
- `HISTORICAL-RP01-REPRODUCED = NO`.
- `REPRODUCIBLE-RELEASE = NO`.

## Evidence classes

Publication codes remain:

- `RP` — direct Smith/RP-01 evidence;
- `SL` — same-lineage evidence;
- `PT` — primary transfer evidence;
- `DER` — derived quantity;
- `SYN` — explicit synthesized empirical starting choice.

Round 60 may append a confidence modifier to synthesized apparatus values:

- `SYN-H` — strongly constrained by primary/official evidence;
- `SYN-M` — plausible working coordinate with partial direct support;
- `SYN-L` — low-confidence prototype coordinate used to make an otherwise unspecified apparatus physically testable.

These modifiers do **not** promote provenance or imply historical identity or demonstrated capability.

## Major Round-60 deep-research recoveries

### Source synthesis and horizontal-slider LPE

Radhakrishnan, Sitharaman and Gupta (J. Cryst. Growth 252, 79–86, 2003; DOI `10.1016/S0022-0248(02)02530-7`) provides more apparatus detail than previously carried into the publication:

- high-purity/high-density graphite horizontal-slider architecture;
- `15 × 15 × 1 mm` CdZnTe substrate;
- horizontal quartz tube with stainless-steel end flanges;
- gas-flow ports, push-pull rod and thermocouple access;
- 6N Hg/Cd/Te source elements;
- evacuated-quartz-ampoule synthesis at `700 °C / 8 h`;
- `10 g` source synthesis, `~4.8 g` charge per growth and `3 g` HgTe reservoir per run;
- architecture explicitly addressing Hg-loss compensation, substrate meltback, intact substrate removal and growth-solution wipe-off.

Honeywell primary patents add:

- substrate recess and capped/tapered solution wells;
- separate HgTe source depression;
- upper/lower Hg-vapor moats under a close graphite cover;
- N2 purge followed by H2 process atmosphere;
- later dedicated CdTe wipe-off elements with approximately `1 mm` guide spacing.

The literature still does **not** publish a complete dimensioned boat drawing.

### Round-60 prototype apparatus coordinates — synthesized, not historical

To make a physically testable first implementation while retaining source honesty, Round 60 now gives a clearly labeled development geometry:

- source-synthesis ampoule development geometry: `25 mm OD / 22 mm ID`, approximately `150 mm` usable internal length, gross cylindrical volume `~57 mL`, target loaded free volume `50±5 mL` (`SYN-M`, pressure qualification mandatory);
- LPE substrate recess: `15.10 × 15.10 mm`, depth `t_s+0.02 mm` (`SYN-L`);
- slider thickness: `4.00 mm` (`SYN-L`);
- growth-well upper envelope: about `15.5 × 15.5 mm`, lower opening `14.5–14.8 mm`, depth `4.0 mm`, geometric volume `~0.961 mL` (`SYN-L`);
- Hg-source cavity: about `20 × 15 × 2 mm` (`SYN-L`);
- first-prototype Hg-vapor moat cross section: about `1 × 1 mm` (`SYN-L`);
- target active-region flatness `<20 µm` (`SYN-M`);
- nominal slider velocity `2.0 mm/s` remains a development center.

These are **not** recovered Honeywell or Fermionics dimensions. The manuscript requires a dimensioned drawing, metrology, dummy thermal map and apparatus qualification before material conclusions are attributed to the recipe.

### Source ampoule handling

Round 60 distinguishes direct HgCdTe source-synthesis facts from transfer sealing practice. It uses PNNL quartz-ampoule work for seal cleanliness/inspection practice only and explicitly rejects that report's different slight-vacuum irradiation-specimen pressure as an HgCdTe synthesis vacuum.

The Hg-bearing charge is kept cold during pump-down with an Hg-compatible trapping/containment scheme. The 700 °C loaded ampoule is treated as a pressure-bearing hazardous containment system requiring facility-specific pressure/thermal engineering qualification before use.

### Wet processing and lithography

Round 60 adds:

- wet-mesa mixing order `EG -> HBr -> thermal equilibration -> Br2 last`;
- `5±1 min` post-mix equilibration and bath-age record;
- explicit reagent assay and same-bath witness logic;
- current AZ P4620 manufacturer data as implementation guidance only, not historical identity;
- measured UV dose rather than exposure seconds as the transferable exposure coordinate.

Existing stronger direct/primary-transfer resist thickness/process anchors are retained where the deep-research report proposed weaker generic replacements.

### RIE apparatus definition

Direct RP-01 controller coordinates remain `CH4/5H2`, total `64 sccm`, `100 mTorr`, `50 W`, `60 s`.

Round 60 now explicitly records:

- powered-electrode diameter/area, material and spacing;
- powered/grounded assignment;
- RF frequency;
- MFC model/full scale/calibration (development MFC classes ~20 sccm CH4 and ~100 sccm H2 are SYN-M);
- chamber/base-pressure history;
- specimen x/y position and backside seating;
- forward/reflected power, dc self-bias and sample thermal state.

Historical self-bias and electrode dimensions remain OPEN. Power density `P/A_e` may be reported as context but is not reactor equivalence.

### Cr/Au metallization

Direct stack remains `30/270 nm` Cr/Au. Round 60 deepens the apparatus record with:

- physical QCM `x,y,z,theta` position;
- independent Cr/Au tooling factors and substrate-plane witness closure;
- source/boat/crucible geometry;
- source-to-substrate geometry;
- rate history, rotation and specimen temperature.

For a multiplicative tooling-factor controller, a witness update may be written

`TF_new = TF_old * t_witness/t_QCM`,

but controller convention must be verified before applying the expression.

### Packaging

Historical Honeywell evidence continues to support compliant silicone attachment as the causal family rather than one uniquely optimal obsolete product or bonding force.

Round 60 adds:

- `<=2 K/min` initial cooldown/warmup qualification coordinate;
- five development cycles between 300 K and 77–80 K;
- `<=0.5°` die tilt;
- `>=30 min` cold dwell after thermal stability;
- geometry-derived adhesive dispense example (`2×2 mm` die, `50 µm` ideal bondline -> `0.200 µL`; +20% allowance -> `~0.24 µL`);
- modern silicone candidates only after cryogenic/vacuum equivalence, with NASA outgassing prescreening.

### Absolute responsivity

Round 60 retains the Round-57 underfilled spectral radiant-power comparator geometry and strengthens it with NIST detector-metrology guidance:

- prefer a traceably calibrated InSb power-responsivity working-standard class for the 3–5.2 µm region;
- measure beam profile/centering at the detector plane;
- preserve reference-before/DUT/reference substitution;
- distinguish radiant-power and irradiance calibration modes;
- include an explicit planning uncertainty budget. The representative Round-60 budget gives about `1.65%` relative standard uncertainty (`k=1`) and `~3.3%` expanded (`k=2`), but those figures must be replaced by measured campaign terms.

## Appendix D — apparatus-definition coordinates

Round 60 adds a permanent apparatus-definition appendix spanning source ampoule, synthesis furnace, LPE furnace/boat/drive/gases, wet processing, anodization, spinner/aligner, RIE, evaporator/QCM, packaging/wire bonding, cryostat, optical bench/monochromator, lock-in/noise/transient chain and analysis-code identity.

This appendix is **not a traveler**. Its purpose is to make an experimental process coordinate physically meaningful and reconstructible by preserving dimensions, calibration state, actual sensor definitions and analysis identity — not to collect signatures.

## Stable scientific controls inherited from Round 57/59

Do not reopen without stronger contrary evidence:

- D1 and T1 geometry separation;
- area-specific anodization current calculation;
- 500-MS/s / 2-ns transient sampling and adaptive record/repetition period;
- Protocols 1–7 remain a composite upstream hypothesis, not an RP-01 historical material reconstruction;
- witness-calibrated mesa etch;
- explicit FTIR inverse model;
- Hall weak-field-first analysis;
- Smith terminal field plus contact-corrected bulk-field estimate;
- underfilled absolute radiant-power geometry;
- P37/W1 LBIC functional blocking gate;
- finite-width TLM;
- inter-contact D* area;
- preserved 1-kHz / ~3-kHz historical noise ambiguity.

## Round-60 artifact state

Review artifacts:

- `RP01_HgCdTe_Exhaustive_Empirical_Fabrication_Protocol_Round60.pdf`
- `RP01_HgCdTe_Exhaustive_Empirical_Fabrication_Protocol_Round60.tex`

Final state:

- `69` physical pages;
- letter size;
- text-native, openable and unencrypted;
- no XFA/form fields;
- all fonts embedded;
- all 69 pages rendered and visually inspected, including the new source/LPE/apparatus/metrology pages;
- no remaining reported overfull/underfull LaTeX box or undefined-control errors in the release compile;
- static protocol index used so page navigation is stable in a single-pass release build.

SHA-256:

- PDF `a42e5c14ddfff5c4ae598184617958c3fa2416ace2fdb1112bfafb63cabba7cd`;
- TeX `8f2665a1df60970b9faccccc56c6762d83bee2cca1dafe2df5516db28aa775ca`.

## Immediate next work

Round 60 is now the preferred review candidate. The next adversarial pass should attack **whether each new SYN-H/M/L coordinate is physically justified and whether any remaining OPEN coordinate can be closed from additional primary sources, archived theses, patents or tool documentation**. Do not respond to residual uncertainty by converting the manual into a traveler or by inventing historical dimensions.
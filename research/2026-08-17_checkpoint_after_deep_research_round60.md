# Checkpoint after deep-research apparatus integration — Round 60

**Date:** 2026-08-17 America/New_York  
**Repository:** `Kajin-0/MCT-Device`

## Trigger

After Round 59, an adversarial assessment correctly concluded that the publication was already unusually complete as a literature-derived manual but that the largest remaining documentation opportunity was apparatus/operator detail rather than manufacturing traveler/process-capability paperwork.

The user explicitly rejected traveler framing and requested an extremely deep research pass to recover additional empirical detail.

## Deep-research result

The research pass followed primary papers, patents, DOE/PNNL reports, NIST metrology publications and current manufacturer/official documentation.

The largest recovery was upstream:

- Radhakrishnan 2003 resolves a 15×15×1-mm CdZnTe development substrate, high-purity/high-density graphite slider context, quartz-tube/stainless-flange/push-pull/thermocouple architecture, 6N elements, 700 °C/8 h evacuated-quartz source synthesis, 10-g batches, ~4.8-g run charge and 3-g HgTe reservoir.
- Honeywell patents recover capped/tapered solution wells, substrate recess, auxiliary HgTe source, vapor moats and CdTe wipe-off architecture.
- exact machining dimensions still remain unrecovered.

The research also strengthened source-ampoule implementation, wet-processing preparation, RIE physical-definition requirements, evaporation/QCM closure, cryogenic packaging construction, and NIST-style absolute responsivity.

## Round-60 publication changes

The 62-page Round-59 LaTeX artifact was rebuilt as a 69-page Round-60 review candidate.

Major additions:

- evidence-preserving SYN-H/M/L confidence modifiers;
- source-synthesis apparatus/pressure-boundary section;
- 25/22-mm fused-silica development ampoule geometry with mandatory pressure/thermal qualification;
- recovered Radhakrishnan/Honeywell LPE hardware architecture;
- explicit first LPE prototype dimensions clearly labeled SYN-L;
- stronger wet-etch bath preparation/age/agitation definition;
- RIE electrode/MFC/RF/self-bias/thermal apparatus definition;
- QCM physical location/tooling-factor and source-geometry closure;
- tighter package thermal/cooldown/dispense-volume construction;
- NIST-style InSb reference and uncertainty structure;
- new Appendix D with apparatus coordinates and suggested measurement/recording precision across the complete process and characterization chain.

The publication explicitly states that Appendix D is not a traveler and does not collect signatures.

## Round-60 artifact QA

Release artifacts:

- `RP01_HgCdTe_Exhaustive_Empirical_Fabrication_Protocol_Round60.pdf`
- `RP01_HgCdTe_Exhaustive_Empirical_Fabrication_Protocol_Round60.tex`

Final PDF:

- 69 physical pages;
- letter size;
- text-native;
- openable and unencrypted;
- no XFA/form fields;
- all fonts embedded;
- static protocol index with stable page numbers;
- all 69 pages rendered and visually inspected, with focused review of source ampoule, LPE hardware, RIE, packaging, responsivity uncertainty and Appendix D;
- no reported overfull/underfull box, undefined-control or LaTeX-error findings in the release compile.

SHA-256:

- PDF `a42e5c14ddfff5c4ae598184617958c3fa2416ace2fdb1112bfafb63cabba7cd`;
- TeX `8f2665a1df60970b9faccccc56c6762d83bee2cca1dafe2df5516db28aa775ca`.

## Scientific maturity

Unchanged:

- Protocols 1–7 remain a composite literature-derived upstream hypothesis;
- historical RP-01/Fermionics material process has not been recovered;
- the integrated synthesized sequence has not been experimentally demonstrated end to end;
- `TRACEABLE-FIRST-BUILD-READY = NO` for an unspecified/uninstantiated laboratory;
- `HISTORICAL-RP01-REPRODUCED = NO`;
- `REPRODUCIBLE-RELEASE = NO`.

The purpose of Round 60 is documentation completeness and physical-definition quality, not manufacturing-process release.

## Best next work

1. Adversarially review every new SYN-H/M/L coordinate for physical plausibility and cross-lineage compatibility.
2. Continue targeted primary-source searches for genuinely OPEN geometry, especially old HgCdTe theses, patents and archived Fermionics/UWA/Honeywell apparatus sources.
3. Where no historical number exists, improve the engineering derivation and uncertainty of the synthesized prototype rather than inserting a blank or claiming historical identity.
4. Preserve the Round-60 LaTeX/exhaustive empirical protocol format; do not revert to traveler/process-capability framing.
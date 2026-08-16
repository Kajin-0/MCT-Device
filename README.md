# MCT-Device

A source-controlled effort to build a reproducible, quantitatively specified fabrication and characterization manual for HgCdTe (MCT) infrared photodetectors.

## Objective

The target is not a generic review. The repository is intended to converge on one or more **closed reference processes** that a competent semiconductor researcher can audit and reproduce. Each process step must state:

- purpose and physical rationale;
- incoming material state;
- equipment and calibration requirements;
- process setpoints, tolerances, times, rates, atmospheres, and geometry;
- required measurements before and after the step;
- acceptance/rejection criteria;
- uncertainty and apparatus-specific calibration requirements;
- known failure modes and diagnostics;
- source provenance for every quantitative value.

A process is not considered reproducible merely because every field contains a number. Parameters from incompatible HgCdTe processes must not be combined without a demonstrated physical basis.

## Provenance classes

Every quantitative parameter in the eventual process traveler should carry one or more provenance tags:

- **[P] Published** — directly reported experimental value in the cited source.
- **[B] Book/authoritative reference** — reported in a technical monograph or review and traceable to primary literature where possible.
- **[D] Derived** — calculated from published inputs; equation and assumptions must be shown.
- **[C] Calibration-dependent** — must be established on the actual apparatus before use.
- **[Q] Qualification-required** — plausible/reference value that cannot yet be released as a production setpoint until a qualification experiment closes it.
- **[T] Tentative** — research lead only; must not be treated as a fabrication instruction.

## Current reference process

**RP-01** is initially anchored to the 2001 Smith–Winchester–Musca–Dell–Faraone MWIR n-type HgCdTe photoconductor fabrication process (DOI `10.1088/0268-1242/16/6/306`). This was selected because the paper reports the starting material, RIE conditions, photolithography/lift-off details, passivation thickness, metallization, contact characterization, detector noise, spectral response, and detectivity for actual fabricated devices.

RP-01 is **not yet a complete end-to-end recipe**. In particular, the upstream LPE growth, substrate preparation, mesa wet-etch chemistry, anodization conditions, cleaning sequence, exact mask geometry, package/attach method, and several calibration details are not fully specified by that paper. Those gaps are tracked explicitly rather than filled by guesswork.

## Repository structure

- `AGENTS.md` — continuity record and operating rules for future agents/researchers.
- `docs/00_MANUAL_ARCHITECTURE.md` — planned structure of the final manual.
- `docs/01_RP01_REFERENCE_DEVICE.md` — frozen reference-device specification and known gaps.
- `docs/SOURCE_LEDGER.md` — source/claim/provenance registry.
- `research/` — dated research logs recording discoveries, rejected paths, unresolved contradictions, and next actions.
- `procedures/` — validated or qualification-stage process modules as they are developed.
- `travelers/` — eventual executable process travelers/checklists.
- `calculations/` — equations, parameter derivations, and uncertainty calculations.

## Rule for process closure

No module graduates into `procedures/` as a reproducible procedure until all critical setpoints have traceable sources or explicit local-calibration methods, all required metrology has been defined, and the module has clear acceptance criteria.

## Immediate research program

1. Close the RP-01 downstream photoconductor process from mesa delineation through electrical/optical characterization.
2. Find and audit an LPE process capable of producing a materially compatible x≈0.30 n-type epilayer on insulating CdZnTe rather than splicing in an unrelated x≈0.20 LWIR growth recipe.
3. Establish the material-property equations and metrology required to verify composition, thickness, carrier concentration, mobility, resistivity, lifetime, and spectral cutoff before device fabrication.
4. Convert the closed process into a manufacturing-style traveler with mandatory record fields and go/no-go gates.

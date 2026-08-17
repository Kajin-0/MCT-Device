# Round 54 — corrective procedural-manual rebuild review

**Date:** 2026-08-16 America/New_York  
**Base technical source:** Draft 0.2 / Round 52 + controlled P01–P36/P36A procedures and calculation modules.

## Trigger

The user rejected the Round-53 22-page publication candidate. The substantive defects were:

- presentation was too compressed for a fabrication manual;
- organization read like a technical overview rather than a recipe/SOP;
- figures were generic/sloppy and did not carry enough apparatus or measurement meaning;
- detailed operator controls already present in the repository were summarized away;
- equipment, local setpoints, measurements, hold points and retained-record requirements were not sufficiently visible at the bench level.

This was a publication-architecture failure, not evidence that the underlying P01–P36 technical corpus lacked detail.

## Corrective design rule

Round 54 does **not** cosmetically revise Round 53. It rebuilds the manual around a repeated SOP grammar:

1. purpose / controlled transition;
2. prerequisites and incoming material state;
3. equipment, tooling, consumables, references;
4. direct/reference values with evidence classification;
5. conspicuous mandatory local fields that must be instantiated before execution;
6. numbered operator sequence;
7. in-process measurements and raw records;
8. GO / HOLD / REWORK / STOP decision gate;
9. output state and handoff.

No artificial page limit is imposed.

## Result

The corrective candidate is 47 pages and contains 17 sequential SOP modules:

1. incoming Hg/Cd/Te and CdZnTe control;
2. final CdZnTe surface, charge calculation and source preparation;
3. Te-rich horizontal-slider LPE;
4. FTIR + Hall/VdP material qualification;
5. Hg-overpressure anneal;
6. Mask-1 + wet mesa;
7. anodic oxide;
8. Mask-2 contact-window/lift-off lithography;
9. CH4/H2 RIE blocking contact;
10. Cr/Au, lift-off, dimensional verification and TLM;
11. bare-device DC/self-heating;
12. singulation/die-edge qualification;
13. package/interconnect/thermal response;
14. absolute spectral responsivity;
15. noise PSD/ASD, NEP and D*;
16. temporal/frequency-response/lifetime interpretation;
17. final closure/reproducibility data package.

The document also includes failure-isolation logic, worked calculations/uncertainty template, operator release checklists, symbols/units, controlled bibliography, and deliberately open historical identities.

## Figure correction

Round-53 generic publication diagrams are not the design standard going forward. Round 54 uses nine deterministic engineering schematics tied directly to process decisions:

- end-to-end release gates;
- LPE apparatus coordinates;
- anneal boundary condition and temperature trajectories;
- mesa/oxide/RIE/Cr-Au frontside physical sequence;
- RIE physical recession versus electrical conversion depth/lateral extent;
- nine-contact TLM geometry;
- package thermal path;
- spectral-responsivity comparator;
- noise/D* same-state measurement chain.

Schematics are labeled as schematic wherever historical geometry is not directly known.

## Local-instantiation visibility

Hardware/material-dependent coordinates are shown as dedicated `MUST FILL BEFORE EXECUTION` fields instead of being buried in prose. This implements the permanent rule:

`REF-CENTER != EXECUTABLE-LOCAL-SETPOINT`.

A blank required field is a HOLD state, not an invitation to infer a generic semiconductor value.

## Scientific disposition

The rebuild changes presentation architecture, not the Round-52 scientific conclusions. It preserves, among other controls:

- authoritative xL=.082/yL=.810 LPE mass convention;
- apparatus-dependent total LPE charge;
- dual `T_s(t)` / `T_Hg(t)` anneal state;
- wet-mesa formulation ambiguity and local calibration requirement;
- anodization current scaling from measured exposed area;
- Mask-2 direct 4–5 µm / 80 °C 30 min / chlorobenzene 30 min fingerprint;
- RIE `t_clear` versus `t_sem`, physical versus electrical depth, sheet-state-first reduction and reactor-equivalence controls;
- direct Cr/Au 30/270 nm with local deposition-tool/vacuum/rate/QCM qualification;
- same-device/contact/state lock for D*;
- 60° FOV historical ambiguity;
- high-frequency 24.5 nV/sqrtHz versus 1-kHz-noise distinction;
- package-thermal de-embedding before lifetime interpretation.

No new historical setpoint was invented to make the SOP look complete.

## QA gate

Final review artifact hashes:

- DOCX `399e51aa26046acfde1de283ce690e23f4dbdef9f293ea534e5478f65ce823e2`;
- PDF `a4d27a11471dfad35a79d60727d0d71c847e26d2b6268209501f30b39ecdeaac`.

Verification:

- 47-page DOCX render inspected after final navigation/accessibility edits;
- DOCX accessibility audit: 0 high, 0 medium, 0 low findings;
- PDF inspector/preflight: 47 pages, 612x792 pt, openable, unencrypted, text-native;
- independent 200-dpi PDF render completed for all 47 pages.

## Document state

`ROUND53-PUBLICATION-PRESENTATION-ACCEPTED = NO`.

`RP01-PROCEDURAL-MANUAL-CORRECTIVE-CANDIDATE-READY = YES`.

This is still a review candidate, not a final issued/reproducible process release.

Physical states remain unchanged:

- `TRACEABLE-FIRST-BUILD-READY = NO`;
- `HISTORICAL-RP01-REPRODUCED = NO`;
- `REPRODUCIBLE-RELEASE = NO`.

## Next gate

Perform a line-by-line operator/scientific adversarial review of the Round-54 candidate. Expand any section where the publication version still hides a control that could alter an actual operation or scientific interpretation. Final issue requires that audit and user acceptance.

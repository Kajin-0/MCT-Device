# RP-01 gap matrix addendum — Round 46 sequential material-release / campaign execution

**Date:** 2026-08-16 America/New_York  
**Repository:** `Kajin-0/MCT-Device`

## 1. Purpose

Round 46 does not close the remaining physical implementation gaps. It restructures them around a new question:

> Even when a process step and its experiment are defined, is there enough current evidence and remaining material optionality to justify crossing the next irreversible boundary?

The new gap categories below prevent “procedure exists” from being confused with “sample is released.”

---

# 2. New integration state

Round 46 adds:

`P16H-SEQUENTIAL-MATERIAL-RELEASE-CONTROL-READY`.

Current state:

`NO / NOT PHYSICALLY INSTANTIATED`.

P16H sits after the planning layers:

- P16E uncertainty/requirements allocation;
- P16F empirical-campaign readiness;
- P16G genealogy/material-plan readiness.

It controls execution of actual material through those plans.

---

# 3. New Round-46 gap labels

Use the following labels where appropriate:

- `GATE-EVIDENCE-OPEN`
- `RELEASE-AUTHORITY-OPEN`
- `CONFIGURATION-FREEZE-OPEN`
- `POST-COMMIT-FEASIBILITY-OPEN`
- `HOLDOUT-QUARANTINE-OPEN`
- `RESERVE-RELEASE-TRIGGER-OPEN`
- `RUN-ORDER-BLOCKING-OPEN`
- `ADAPTIVE-SELECTION-RULE-OPEN`
- `REWORK-ROUTE-OPEN`
- `FAILURE-DISPOSITION-OPEN`
- `EXECUTION-AUDIT-OPEN`
- `MATERIAL-RELEASE-CONTROL-READY`

These are implementation/control gaps, not historical evidence classes.

---

# 4. Cross-program release gaps

| Gap | Current state | Why open | Closure path |
|---|---|---|---|
| named material-release authority | `RELEASE-AUTHORITY-OPEN` | no physical laboratory organization exists | P16H program header / local authority assignment |
| exact active configuration registry | `CONFIGURATION-FREEZE-OPEN` | no selected tools/calibrations exist | P16H configuration register + P16C/P16D implementation |
| gate records tied to physical samples | `GATE-EVIDENCE-OPEN` | no physical samples exist | execute P22C/P16H on actual genealogy nodes |
| post-commit material-feasibility proof | `POST-COMMIT-FEASIBILITY-OPEN` | actual outlines/descendants/reserve unavailable | P16G CAD/material balance + P16H gate sheet |
| holdout model-freeze/quarantine | `HOLDOUT-QUARANTINE-OPEN` | no active empirical dataset/model exists | instantiate P16F/P16H holdout records |
| reserve release triggers | `RESERVE-RELEASE-TRIGGER-OPEN` | no empirical reserve/yield state exists | P16G reserve terms + P16H release trigger |
| run-order/blocking implementation | `RUN-ORDER-BLOCKING-OPEN` | actual hard constraints/tools/run dates unknown | P22C/P16H run-order table |
| adaptive next-state selection | `ADAPTIVE-SELECTION-RULE-OPEN` | no active sequential campaign | freeze algorithm/criterion before adaptive execution |
| rework identity rules | `REWORK-ROUTE-OPEN` | no local qualified rework routes | qualify route by process state; reassess sample role |
| failure route on actual material | `FAILURE-DISPOSITION-OPEN` | no physical failure exists | P18 + P16H event record |
| complete execution audit trail | `EXECUTION-AUDIT-OPEN` | no physical campaign | P16H + immutable raw/genealogy records |

---

# 5. G0 gaps — authorization before HgCdTe consumption

Required evidence is structurally defined but physically open:

- relevant P16C tool identity;
- relevant P16D subsystem acceptance;
- relevant P16E measurement/control allocation;
- active P16F Stage-0/design resolution;
- active P16G material feasibility;
- EH&S/facility authorization.

Current status:

`G0 = HOLD / NOT PHYSICALLY EVALUABLE`.

This is not a statement about any real laboratory; none is instantiated in the repository.

---

# 6. G1 gaps — Stage-0 to formal LPE DOE

Still open:

- local independent-growth variance;
- local P06 repeatability on actual material;
- actual feasible morphology region;
- actual factor perturbation limits;
- exact selected F2 branch;
- run-order constraints from actual source-use/apparatus;
- physically available independent roots;
- holdout roots.

Round 44/45 give structural options and root floors, but no formal F2 campaign can be released without these local inputs.

Current:

`G1 = GATE-EVIDENCE-OPEN`.

---

# 7. G2 gaps — F2 root to anneal

For every future root, still open:

- actual P06 result;
- usable-material polygon;
- F2 role/selection basis;
- dedicated/qualified P05 branch;
- exact F3 treatment assignment;
- untreated/control descendant needs;
- post-commit material feasibility.

Permanent restriction:

A good P06 result alone does not release a root to anneal.

---

# 8. G3 gaps — annealed material to RIE/passivation

Still open:

- actual anneal trace validity;
- actual P05 carrier-state classification;
- actual P06 optical-preservation result;
- local definition of F4 intended material regime;
- actual RIE chamber acceptance/configuration;
- witness/detector allocation.

Transition/multicarrier material remains a controlled classifier/boundary state and is not automatically a standard detector input.

---

# 9. G4 gaps — RIE state to full detector fabrication

This remains one of the highest-value scarcity gates.

Still open:

- actual measured self-bias/sheath state;
- actual oxide-clear time and semiconductor exposure;
- actual converted sheet/depth/lateral state;
- actual stability over RIE-to-metal handoff;
- actual information value of a full detector descendant;
- actual detector-bearing state subset;
- actual physical detector layout/available area;
- actual controls/holdouts.

Round 46 deliberately does not release a rule such as “fabricate detectors for the best three RIE conditions.”

Selection must follow the protected information/decision criterion.

---

# 10. G5 gaps — detector characterization

Still open:

- actual detector geometry/contact pair;
- actual detector continuity/I-V state;
- actual P10/P11/P12/P13 chain commissioning;
- actual field/power/heating guard;
- actual state-reversibility/order effects;
- actual F1 perturbation half-range.

Round-43/44 equations remain planning tools only until local data exist.

---

# 11. G6 gaps — singulation release

Still open:

- actual P35 singulation tool/branch;
- physical street/kerf/wander;
- functional edge exclusion;
- actual device die outline;
- pre/post singulation performance result;
- protection/support/clean compatibility;
- retained unsingulated comparator need.

Current candidate family remains low-force CdZnTe-compatible wire-saw screening, not a released RP-01 method.

---

# 12. G7 gaps — package release

Still open:

- surrogate package-family result;
- actual adhesive/carrier/interconnect branch;
- actual bondline/void/tilt state;
- exact die/package geometry;
- actual pre-package baseline;
- actual package holdout assignment;
- protected remaining die reserve;
- actual cryogenic survival/performance.

A package candidate family is not an authorization to consume a detector die.

---

# 13. Holdout leakage gap

Round 44/45 required holdouts but had not defined data-access control.

Round 46 now distinguishes:

- validity QC access; and
- protected scientific outcome access.

Current physical state remains:

`HOLDOUT-QUARANTINE-OPEN`.

Closure requires a real model-freeze event/revision and actual holdout ID.

---

# 14. Reserve release gap

Round 45 established reserve classes but left their release timing open.

Round 46 closes the method:

- release occurs when protected purpose closes or is formally replaced;
- failure of another sample does not automatically unlock reserve;
- reserve may later be sized probabilistically from empirical success data.

Physical reserve quantities remain open.

---

# 15. Run-order / blocking gaps

Round 46 requires actual campaigns to classify each factor as:

- easy-to-change/randomizable;
- hard-to-change/split-plot;
- sequential/source-history;
- block/covariate.

Actual classifications remain partly tool-specific.

Likely important unresolved physical coordinates include:

- LPE source-use/depletion;
- anneal ampoule/reservoir state;
- RIE clean/season/chamber age;
- package cure/build batch;
- calendar/operator.

These must be frozen before execution, not reconstructed after observing responses.

---

# 16. Rework gaps

No broad “rework allowed” state exists.

Separate routes remain open for:

- re-anneal;
- repeat RIE;
- oxide/passivation rework;
- metallization rework;
- singulation clean/recovery;
- package rework.

Any one route must be qualified for its exact material state and followed by evidence-role reassignment.

A reworked sample may become a new treatment state rather than remain a valid replicate/holdout of its original state.

---

# 17. Failure-result classification gap

Round 46 establishes the method but not actual classifications.

Future failures must be separated into:

- measurement invalidity;
- handling damage;
- process excursion;
- true treatment response;
- genealogy/identity error;
- unknown.

A true process failure stays in the dataset under the frozen analysis rule.

Automatic outlier deletion is prohibited.

---

# 18. P16H closure criteria

P16H can become YES only when a real active laboratory/campaign has:

1. named release roles;
2. active configuration/calibration registry;
3. physical gate IDs and sample nodes;
4. separate technical and material-feasibility checks;
5. holdout lock/model-freeze control;
6. reserve locks/release triggers;
7. run-order/blocking control;
8. failure/P18 routing;
9. rework role-reassignment control;
10. complete audit trail;
11. current EH&S/facility authority.

Current:

`P16H-SEQUENTIAL-MATERIAL-RELEASE-CONTROL-READY = NO`.

---

# 19. No maturity promotion

Round 46 does not change:

`TRACEABLE-FIRST-BUILD-READY = NO`

`HISTORICAL-RP01-REPRODUCED = NO`

`REPRODUCIBLE-RELEASE = NO`

`P16C-INFRASTRUCTURE-READY = NO / NOT PHYSICALLY INSTANTIATED`

`P16D-SURROGATE-COMMISSIONING-COMPLETE = NO / NOT PHYSICALLY INSTANTIATED`

`P16E-REQUIREMENTS-ALLOCATION-COMPLETE = NO`

`P16F-EMPIRICAL-JACOBIAN-CAMPAIGN-READY = NO / NOT PHYSICALLY INSTANTIATED`

`P16G-MATERIAL-GENEALOGY-PLAN-READY = NO / NOT PHYSICALLY INSTANTIATED`

New:

`P16H-SEQUENTIAL-MATERIAL-RELEASE-CONTROL-READY = NO / NOT PHYSICALLY INSTANTIATED`.

Permanent relation:

`candidate branch != infrastructure ready != surrogate commissioned != uncertainty allocated != campaign ready != genealogy ready != release-control ready != local branch frozen != historical identity != reproducible release`.
# Research checkpoint — Round 34: first-build / release-readiness integration

**Date:** 2026-08-16 America/New_York

## Repository state established by this checkpoint

Round 34 is a systems-integration round. It does not add a new HgCdTe process recipe. It converts the accumulated procedure/source/gap architecture into an explicit pre-build and release-readiness system.

New controlled documents:

- `procedures/P16A_FIRST_BUILD_RELEASE_READINESS_AUDIT.md`
- `travelers/P16A_FIRST_BUILD_READINESS_REGISTER.md`
- `procedures/P17A_SINGULATION_PACKAGE_CHANGE_CONTROL_ADDENDUM.md`
- `procedures/P18A_SINGULATION_PACKAGE_EDGE_FAILURE_DIAGNOSTICS.md`
- `docs/SOURCE_LEDGER_ADDENDUM_ROUND34.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND34.md`

Base documents revised:

- `procedures/P16_MASTER_END_TO_END_PROCESS_TRAVELER.md`
- `procedures/P19_REQUIREMENTS_TRACEABILITY_MATRIX.md`

---

## Central conceptual result

Three claims are now formally different:

### `TRACEABLE-FIRST-BUILD-READY`

A pre-execution state. A competent laboratory can execute one complete qualification route without making undocumented decisions. Every mandatory irreversible process branch, material identity, setpoint/trajectory, endpoint and gate metrology implementation is explicitly selected.

### `HISTORICAL-RP01-REPRODUCED`

A historical identity claim. Requires source closure for process details represented as historical RP-01 rather than local transfer.

### `REPRODUCIBLE-RELEASE`

A statistical/process release claim. Requires P17/P17A measurement-system adequacy, detector-derived numerical specifications, repeated stability/capability/yield and change control.

A local process can eventually be reproducibly released without being a literal historical reconstruction.

---

## New blocker taxonomy

Use:

- `HISTORICAL-IDENTITY-ONLY`
- `EXECUTION-BLOCKER`
- `LOCAL-IMPLEMENTATION-GATE`
- `RELEASE-BLOCKER`

Do not use one undifferentiated OPEN list for readiness decisions.

---

## Current maturity disposition

As of this checkpoint:

- `TRACEABLE-FIRST-BUILD-READY = NO`
- `HISTORICAL-RP01-REPRODUCED = NO`
- `REPRODUCIBLE-RELEASE = NO`

The primary reason for the first NO is unresolved empirical execution branches, not lack of theory.

---

## Highest-impact execution blockers

1. **P30 LPE:** actual boat/well, total melt inventory, source/charge realization, atmosphere, thermometry, equilibration, contact, wipe-off and cooldown branch.
2. **P07C/P29 final CdZnTe surface:** selected final chemistry/removed depth/clean-to-load branch.
3. **P31 anneal:** selected apparatus/reservoir + `Ts(t), THg(t), pHg/source proxy, dwell, cooldown`.
4. **P32/P28 Mask-1 + wet mesa:** resist process plus explicit Br2/EG:HBr/HBr preparation basis, rinse/strip/endpoint.
5. **P25 oxide:** actual local electrochemical cell/bath branch.
6. **P27 Mask-2:** full resist/exposure/developer/chlorobenzene/lift-off branch.
7. **P34 RIE:** actual local CH4/H2 gas realization and reactor/sheath/sample thermal state.
8. **P26 metal:** deposition tool/base pressure/rates/QCM/RIE-to-Cr/lift-off branch.
9. **P35 singulation:** selected cutting/support/protection/clean/street/inspection branch.
10. **P33 package:** selected carrier/attach/interconnect/optical/vacuum construction.

---

## Local implementation gates

Methods are scientifically controlled but the actual lab implementation still must be instantiated for:

- P05 Hall/VdP;
- P06/P06A FTIR;
- P10/P10A bias/load;
- P11/P11A radiometry;
- P12/P12B/P12C noise;
- P13/P13A dynamics;
- P35 edge/subsurface inspection;
- P33 package thermal measurement.

Exact historical instrument identity is generally not required for these local methods.

---

## P16 repair

P16 now:

- integrates the architecture through P35 rather than saying P01–P15;
- requires P16A readiness authorization for a no-tribal-knowledge end-to-end route;
- routes Phase G STEP G1 to P35;
- records full P35 singulation process/edge/subsurface state;
- routes die attach/interconnect/optical/vacuum through P15/P33;
- feeds cryogenic P33 results back to final P35 singulation disposition;
- includes P35/P33 evidence in the minimum final data package;
- separates qualification-run status, historical reproduction and statistical release.

---

## P19 repair

P19 now contains an explicit singulation/die-edge requirement:

`mechanically intact die != detector-function-qualified die`.

It traces P35 outputs to:

- P10 electrical state;
- P12 noise;
- P11 responsivity;
- P33 cryogenic edge survival;
- final P17 yield/release.

Package requirements now reference P15/P33/P35 rather than P15 alone.

---

## P17A change-control extension

Changes to any of the following now trigger formal impact review/requalification:

- blade/wire/laser method or tool;
- grit/bond/dimensions;
- feed/speed/downfeed/pass strategy;
- coolant/slurry;
- protection/support;
- clean/removal chemistry;
- street/edge exclusion;
- package carrier/die attach/bondline/cure;
- interconnect;
- aperture/window/shield;
- vacuum/bake/cooldown.

Mechanical yield and functional detector yield are separate.

---

## P18A diagnostic extension

New post-singulation diagnostic branches cover:

- visible chipping/cracking;
- hidden electrical damage with clean-looking edge;
- increased 1/f noise;
- reduced responsivity;
- first-cooldown crack propagation;
- progressive thermal-cycle edge cracking;
- laser stoichiometry/redeposition;
- wire-saw/blade residue aging/package interaction.

P35 × P33 interactions must be discriminated rather than assigning all cooldown cracks to one process automatically.

---

## Important historical gaps that do not by themselves block local first build

Once local calibrated branches exist, the following primarily block literal historical claims:

- exact RP-01 FTIR/material-metrology instrument;
- exact Optronics model/calibration;
- exact HP35665A settings;
- exact 2001 preamp circuit;
- exact historical performance contact pair;
- exact 4.4-µm cutoff convention;
- exact historical lifetime/f3dB;
- exact historical singulation/die outline;
- exact historical package construction.

Do not spend disproportionate effort on these while upstream process operations still cannot be executed without undocumented choices.

---

## Strongest next action — Round 35

Proceed with **P30 LPE absolute apparatus / charge / contact-trajectory closure**, because P16A ranks it as the highest-leverage execution blocker.

Audit P03/P03A–E/P30 and prior Honeywell/Fermionics/Bowers–Schmit evidence before adding anything new.

Research target:

`X_LPE_EXEC={boat/well geometry,substrate recess,total melt mass/depth,Hg/Cd/Te/HgTe inventory,Hg-source state,atmosphere/flow/pressure,thermometry geometry/calibration,equilibration criterion,T_contact,t_contact,T(t),separation/wipe geometry/motion,cooldown}`.

Priority source recovery:

1. Honeywell/Fermionics patents/papers with actual slider boat drawings/dimensions and charge masses.
2. UWA theses/process records that identify received material/growth provenance.
3. Bowers–Schmit primary phase-equilibrium/growth apparatus text beyond tie-line numbers.
4. Historical Te-rich horizontal-slider LPE studies with quantitative well dimensions, charge mass, substrate size and contact/wipe mechanics.
5. Direct evidence for source reuse/depletion and Hg-loss control in the selected x≈0.30 regime.

Do not create a theoretical absolute charge mass from tie-line fractions alone.

If historical hardware remains unrecovered, Round 35 should define the minimum **local calibration program** required to move P30 from `OPEN-CHOICE` to `LOCAL-BRANCH-FROZEN` without inventing a historical recipe.

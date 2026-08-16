# P16A — first-build / historical-reproduction / release-readiness audit

**Status:** CONTROLLED SYSTEM-INTEGRATION / PRE-EXECUTION READINESS METHOD  
**Date:** 2026-08-16 America/New_York

## 1. Purpose

Separate three different project claims that must never be conflated:

1. `TRACEABLE-FIRST-BUILD-READY` — a competent laboratory can execute one complete qualification build without undocumented choices, using explicitly selected historical or local-transfer branches and recording the required metrology/genealogy;
2. `HISTORICAL-RP01-REPRODUCED` — the build is sufficiently source-closed to claim reproduction of the historically used RP-01 process rather than a locally qualified functional reconstruction;
3. `REPRODUCIBLE-RELEASE` — the selected local process has demonstrated measurement-system adequacy, repeated stability/capability, numerical acceptance criteria, change control and detector-performance/yield closure under P17.

These maturity states answer different questions.

A device can be physically excellent without satisfying any of them. Conversely, a traceable first build can be scientifically valuable even though historical identity and production capability remain open.

---

## 2. Blocker taxonomy

Every unresolved item in P16/P19/source-gap ledgers shall be assigned one primary class.

### `HISTORICAL-IDENTITY-ONLY`

Missing historical detail that is required to claim literal RP-01 historical reconstruction but does **not** prevent a local build if a documented equivalent/transfer branch is selected.

Examples:

- exact historical FTIR model/bench;
- exact historical Optronics model;
- exact Figure-5 HP35665A acquisition settings;
- exact historical 4.4-µm cutoff convention;
- exact historical package identity when a local package is explicitly used and not called historical;
- exact historical performance contact pair when a local pair is physically measured and recorded.

### `EXECUTION-BLOCKER`

A missing choice/value without which an operator cannot execute an irreversible or state-defining step from the controlled record.

Typical forms:

- reagent concentration basis is undefined;
- commercial resist/developer/process branch is not selected;
- gas split or gas-delivery realization is undefined;
- apparatus geometry/charge inventory is not defined well enough to calculate a load;
- thermal trajectory is not specified;
- singulation/support/clean branch is not selected;
- package attachment/interconnect construction is not selected.

An execution blocker may be closed either by direct historical evidence or by an explicitly selected `LOCAL-QUAL` branch. Historical identity is not required for first-build readiness.

### `LOCAL-IMPLEMENTATION-GATE`

The scientific method is defined, but the actual laboratory instrument/tool/reference standard/calibration implementation has not yet been frozen and qualified.

Examples:

- actual FTIR instrument/method;
- Hall magnet/sample holder;
- blackbody/reference-detector radiometry implementation;
- preamplifier/analyzer transfer calibration;
- cryogenic thermometer/reference plane.

This class blocks `TRACEABLE-FIRST-BUILD-READY` until the laboratory implementation exists, even though no further historical source recovery may be necessary.

### `RELEASE-BLOCKER`

The process can be executed for qualification, but repeated local data, measurement-system capability, detector-derived numerical limits, stability/yield evidence or change-control closure are still missing.

Release blockers generally do **not** prevent a first qualification build.

---

## 3. Readiness principle

`TRACEABLE-FIRST-BUILD-READY` does **not** mean every step is historically exact or statistically capable.

It means that before material is irreversibly processed:

- every process branch is named;
- every material/reagent/product/tool is identified;
- every necessary setpoint/trajectory is numerically or operationally defined;
- every endpoint/gate is defined;
- every measurement implementation needed for that gate is available and qualified enough for the qualification purpose;
- all unresolved historical substitutions are labeled as substitutions;
- no operator must invent a process decision from memory or generic semiconductor practice.

A branch may still be `CANDIDATE-P` or `LOCAL-QUALIFICATION-RUN` if the purpose of the build is to generate qualification data.

---

## 4. Round-34 audit result — major execution blockers

The following are the highest-impact current blockers to a no-tribal-knowledge first end-to-end build.

### 4.1 P03/P30 LPE apparatus and absolute charge realization — `EXECUTION-BLOCKER`

Known empirical anchors include the xS≈0.29 tie-line family and a candidate liquidus near 507 °C, but an actual build still requires a frozen local apparatus branch defining at minimum:

- boat/well/substrate recess geometry;
- total melt mass/depth;
- source inventory/charge masses;
- atmosphere and gas-flow realization;
- sensor/sample geometry and calibration;
- equilibration criterion;
- first-contact temperature;
- contact interval/thermal trajectory;
- slide-out/wipe-off geometry and motion;
- cooldown trajectory;
- source-use genealogy.

Historical Honeywell/Fermionics identity is desirable but not required if a local P30 branch is explicitly frozen and qualified.

### 4.2 P07C/P29 final CdZnTe surface branch — `EXECUTION-BLOCKER`

The final pre-LPE surface chemistry/removed depth/clean-to-load branch must be selected and frozen. The exact RP-01 supplier/UWA process remains historical-open, but a local interface-qualified branch can close first-build execution.

### 4.3 P04/P31 Hg anneal trajectory — `EXECUTION-BLOCKER`

A run requires an actual sample/reservoir enclosure branch with numerical:

`{T_s(t), T_Hg(t), source state/pHg proxy, dwell, cooldown}`.

A generic `250 °C` historical screening value is insufficient. The selected trajectory may be qualification-stage but must be executable and carry Hall/optical outcome gates.

### 4.4 P32/P28 Mask-1 + wet-mesa branch — `EXECUTION-BLOCKER`

The current record still does not supply one fully frozen Mask-1 + wet-etch execution branch for RP-01-like material. Required closure includes:

- resist product/lot and coating thickness;
- bake/exposure/developer;
- selected etchant preparation with explicit `2% Br2` basis or a separately qualified local chemistry;
- explicit `3:1 EG:HBr` preparation basis if that branch is selected;
- HBr stock assay;
- bath temperature/age/agitation;
- rinse/quench/dry;
- measured depth/isolation endpoint;
- resist strip;
- etch-to-passivation clock.

Historical UWA identity is not necessary for first-build readiness, but an executable local branch is.

### 4.5 P25 anodic oxide implementation — `EXECUTION-BLOCKER` until one branch is selected

P25 has strong empirical transfer evidence and a candidate process center, but a first build requires one actual local cell/bath branch to be frozen with reagent basis, exposed area, current density, V(t)/charge endpoint, rinse/dry and oxide/interface outcome gates.

### 4.6 P27 Mask-2 lithography/lift-off — `EXECUTION-BLOCKER`

Direct RP-01 anchors `4–5 µm / 80 °C 30 min / chlorobenzene 30 min` do not identify a complete runnable photoresist process. One branch must define:

- resist;
- spin/coating method;
- exposure dose/tool;
- developer;
- chlorobenzene bath state and exact sequence consistent with the historical wording;
- post-develop state;
- metal lift-off solvent/time/agitation;
- compatibility with P08/P26.

### 4.7 P34 RIE gas/reactor realization — `EXECUTION-BLOCKER`

The historical controller anchors `64 sccm / 100 mTorr / 50 W / 60 s / CH4/5H2` are not a complete reactor recipe.

Before first build the local branch must define:

- actual CH4 and H2 delivery realization/composition;
- reactor/electrode/sample-holder geometry;
- pressure-control/gauge state;
- RF frequency/tool configuration;
- measured self-bias or qualified ion-energy proxy;
- sample thermal state;
- oxide-clear time;
- semiconductor exposure time;
- chamber clean/season genealogy;
- post-RIE transfer to metal;
- physical + electrical conversion outcome gates.

The historical exact individual gas split is an historical-reconstruction gap; the absence of **any selected local realization** is the execution blocker.

### 4.8 P26 Cr/Au deposition/lift-off realization — `EXECUTION-BLOCKER`

Historical film thicknesses are known (`Cr 30 nm / Au 270 nm`), but a build requires a selected deposition method/tool, base pressure, rates, substrate thermal limit, QCM/witness calibration and RIE-to-Cr transfer rule, plus a frozen compatible lift-off branch.

### 4.9 P35 singulation branch — `EXECUTION-BLOCKER` for packaged end-to-end build

P35 now defines the qualification method, but one local cutting/support/protection/clean branch and sacrificial street geometry must be selected before a package-ready die can be produced without improvisation.

A bare-wafer device-characterization run may stop before P35; an end-to-end packaged build may not.

### 4.10 P33 package/interconnect branch — `EXECUTION-BLOCKER`

A complete end-to-end build requires a frozen carrier/cold-finger, die-attach, bondline/cure, wire/interconnect, aperture/window/shield and vacuum/pump/bake branch. Historical RP-01 package identity can remain open if the construction is labeled local-transfer and closes P10/P11/P12/P13 performance after packaging.

---

## 5. Major local implementation gates

These methods are conceptually controlled but require actual laboratory implementations before a first build can pass all gates.

### P05 Hall/VdP

Freeze:

- magnet/system and calibrated B;
- cryogenic/sample fixture;
- current/voltage instrumentation;
- contact/witness method;
- temperature measurement;
- raw reversal/tensor reduction implementation.

### P06/P06A optical material metrology

Freeze:

- FTIR/instrument configuration;
- background/reference method;
- aperture/footprint/map registration;
- spectral resolution/coadds;
- optical constants/model/software version;
- independent thickness reference.

Historical RP-01 FTIR identity is not required.

### P11/P11A radiometry

Freeze:

- source/reference detector calibration chain;
- monochromator/FTIR spectral branch as used;
- wavelength calibration;
- aperture/view-factor/reference plane;
- package/window transmission;
- electronics transfer;
- signal convention and uncertainty budget.

Historical Optronics model is not required for a valid local absolute measurement.

### P12/P12B/P12C noise

Freeze:

- actual bias/load network;
- preamplifier and gain/input-noise/loading characterization;
- analyzer/FFT/window/ENBW convention;
- detector-terminal ASD referral;
- optical-background state.

Historical HP35665A settings are not required for local detector noise, but are required for literal reconstruction of Figure 5.

### P13/P13A dynamics

Freeze source waveform, injection level, electrical transfer, package thermal de-embedding and analysis model. Historical RP-01 lifetime remains open and does not block local characterization.

---

## 6. Historical-identity gaps that do not by themselves block first build

The following should remain active archival targets but must not be allowed to halt a clearly labeled local-transfer qualification program:

- exact supplier method behind `x≈0.30` and `9.5 µm`;
- exact RP-01 FTIR or optical-material bench;
- exact Optronics model and historical calibration chain;
- exact HP35665A Figure-5 configuration;
- exact low-noise preamplifier circuit used in 2001;
- exact historical performance contact pair/gap;
- exact historical 4.4-µm cutoff criterion;
- exact historical singulation method/die outline;
- exact historical package/interconnect construction;
- exact historical temporal-response/lifetime method for the Figure-3/5/6/7 device, if any.

These become blockers only for the label `HISTORICAL-RP01-REPRODUCED`.

---

## 7. Release blockers after first-build execution is possible

Even after every execution blocker is converted into a frozen qualification branch, the project remains below `REPRODUCIBLE-RELEASE` until P17 is satisfied.

At minimum this requires:

- measurement-system repeatability/reproducibility/bias/uncertainty for release metrics;
- repeated LPE/anneal runs sufficient to separate source/run/spatial variation;
- repeated lithography/etch/passivation/RIE/metal/singulation/package results;
- detector-derived numerical engineering limits rather than historical single-value tolerances;
- process stability assessment before capability indices;
- final performance/yield definition;
- change-control and requalification triggers;
- failure/Pareto/CAPA feedback;
- demonstrated repeatability of the complete frozen route.

Therefore:

`TRACEABLE-FIRST-BUILD-READY` is a pre-execution maturity state;

`LOCAL-QUALIFIED` is a process/module evidence state;

`REPRODUCIBLE-RELEASE` is an end-to-end statistical/release state.

---

## 8. Formal readiness rules

### 8.1 `TRACEABLE-FIRST-BUILD-READY`

May be declared only when every mandatory row in the companion P16A readiness register is one of:

- `DIRECT-EXECUTABLE`;
- `LOCAL-BRANCH-FROZEN`;
- `NOT-APPLICABLE` with rationale.

No mandatory row may remain:

- `OPEN-CHOICE`;
- `UNDEFINED-BASIS`;
- `APPARATUS-NOT-SELECTED`;
- `METROLOGY-NOT-IMPLEMENTED`.

This state authorizes a **qualification build**, not production release.

### 8.2 `HISTORICAL-RP01-REPRODUCED`

Requires, in addition to a completed traceable build:

- source closure of the historically critical process identities being claimed;
- no locally substituted branch being silently represented as historical;
- published-state detector comparison under sufficiently matched/corrected measurement conditions;
- explicit list of any residual historical uncertainties.

A functional local reconstruction with substituted wet etch, resist, RIE reactor or package does not qualify for this label unless those substitutions are excluded from the historical claim.

### 8.3 `REPRODUCIBLE-RELEASE`

Requires:

- frozen released process revisions;
- numerical detector-derived acceptance criteria;
- qualified measurement systems;
- repeated stable/capable runs or an explicitly justified alternative risk model;
- final yield/performance evidence;
- controlled change/requalification system;
- complete P16 data package and P18 failure history.

Historical identity is not logically required for a strong local `REPRODUCIBLE-RELEASE`; scientific reproducibility and historical reconstruction are separate axes.

---

## 9. Readiness vector

Use the following compact system state:

`R_BUILD={P07C/P29_surface,P30_LPE,P31_anneal,P32/P28_mesa,P25_oxide,P27_mask2,P34_RIE,P26_metal,P35_singulation,P33_package,P05_Hall,P06_FTIR,P10_bias,P11_radiometry,P12_noise,P13_dynamic,genealogy,data_capture}`.

Each coordinate shall carry:

`{selected_branch,procedure_rev,tool/material IDs,setpoints/endpoints,measurement_gate,status,evidence_class}`.

The weakest mandatory coordinate controls first-build readiness.

---

## 10. Priority order for closure

To minimize wasted detector material, close execution blockers in this order:

1. **LPE physical apparatus/charge/thermal branch** — upstream and highest material leverage;
2. **CdZnTe final surface + anneal branch** — determines whether usable material state can be made reproducibly;
3. **Mask-1 + wet mesa + anodic oxide** — first irreversible finished-layer device sequence;
4. **Mask-2 + RIE + Cr/Au/lift-off** — contact architecture closure;
5. **measurement implementations P10–P13** — establish whether device function actually matches intent;
6. **P35 singulation + P33 package** — close package-ready detector route;
7. repeated frozen-route runs under P17.

Do not optimize packaging or historical analyzer reconstruction while upstream material/fabrication branches are still non-executable.

---

## 11. P16/P19 integration corrections required by Round 34

The following are normative corrections to the system architecture:

1. P16 no longer conceptually stops at P01–P15; it must invoke the empirical transfer modules through P35 where applicable.
2. P16 Phase G STEP G1 shall use **P35** as the singulation procedure; P15/P33 own package construction after the P35 handoff.
3. P35 room-temperature release is not final: P33 cryogenic cycling feeds back to final `RP01-SINGULATION-QUALIFIED` disposition.
4. P19 shall include an explicit singulation/die-edge requirement and reference P35 in package/cryogenic integrity traceability.
5. P17 change control shall treat singulation tool/process/protection/clean and package construction as requalification triggers.
6. P16's final data package shall include the P35 traveler, edge/subsurface-damage evidence and cryogenic singulation disposition.

Until the base documents are directly revised, this section is the controlled Round-34 integration rule and supersedes stale P16/P19 references.

---

## 12. Current project disposition after audit

As of Round 34:

- `TRACEABLE-FIRST-BUILD-READY` = **NO**;
- `HISTORICAL-RP01-REPRODUCED` = **NO**;
- `REPRODUCIBLE-RELEASE` = **NO**.

The reason is not lack of theoretical understanding. The dominant blockers are still **unfrozen empirical execution branches** for several irreversible material/fabrication/package operations.

The repository is nevertheless substantially closer to a real fabrication manual because the missing decisions are now enumerated explicitly rather than buried inside broad `OPEN` lists.

---

## 13. Exit criterion for the next phase

Round 34 is complete when:

- the companion readiness register exists;
- every major unresolved item has a blocker class;
- P35 is integrated into the end-to-end architecture;
- continuity/gap records are updated;
- the next research work is prioritized around closing an actual execution blocker rather than accumulating more historical trivia.

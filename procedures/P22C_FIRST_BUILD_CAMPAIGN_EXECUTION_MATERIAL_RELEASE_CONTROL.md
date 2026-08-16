# P22C — first-build campaign execution and sequential material-release control

**Status:** CONTROLLED PRE-EXECUTION METHOD / ROUND 46  
**Date:** 2026-08-16 America/New_York  
**Use with:** P16E, P16F, P16G, P16H, P18, P20/P20A, P21/P22/P22A/P22B, P23/P24/P25/P26/P33/P35/P36.

## 1. Purpose

P22C converts the Round-44 experiment architecture and Round-45 material-genealogy plan into a controlled chronological execution system.

It answers:

> What exact evidence must exist before a physical HgCdTe node is allowed to cross the next irreversible process boundary?

The method is intended to minimize three avoidable losses:

1. consuming scarce material before the required measurement chain is trustworthy;
2. committing high-value descendants before upstream process state is identified;
3. destroying holdouts/reserves because of ad hoc recovery after a failure.

This procedure does not authorize HgCdTe handling without local EH&S/facility approval.

---

# 2. Governing rule

Every irreversible material action requires both:

- technical/scientific eligibility; and
- post-commit genealogy/material feasibility.

The gate decision is one of:

`GO / HOLD / REWORK / STOP`.

No other informal state such as “probably okay,” “continue for now,” or “use spare” is permitted in the controlled record.

---

# 3. Gate record identity

Every gate event receives a unique ID:

`GATE-<campaign>-<physical-node>-<revision>-<sequence>`.

Record:

- physical node ID;
- root-growth ID;
- current genealogy path;
- intended irreversible operation;
- procedure revision;
- apparatus/configuration revision;
- calibration IDs;
- DOE/model revision;
- P16G layout/material-plan revision;
- protected requirement/decision;
- release authority;
- date/time;
- final disposition.

A gate decision applies only to that node/configuration combination.

---

# 4. Universal pre-gate checklist

Before evaluating any stage-specific gate, confirm:

## 4.1 Identity / genealogy

- physical ID readable and unique;
- root ID known;
- parent/descendant links complete;
- treatment history complete;
- sample coordinate/orientation retained where relevant;
- no undocumented split, merge, re-label or rework.

## 4.2 Configuration

- current process traveler revision identified;
- actual tool/revision identified;
- relevant calibrations valid for the current configuration;
- no unreviewed hardware/software/method change since prior gate;
- environmental state/clock synchronized where handoff time matters.

## 4.3 Evidence

- required upstream raw data present;
- reductions trace to raw data;
- required uncertainty/acceptance checks complete;
- no unresolved anomaly that can alter the release decision.

## 4.4 Material balance

- proposed descendant role exists in P16G;
- required holdouts remain locked;
- archive/FA material remains sufficient according to current plan;
- downstream detector/package roles remain feasible;
- release does not create treatment/root perfect confounding.

## 4.5 EH&S

- local authorization current;
- facility controls applicable to the proposed operation current;
- operator authorization/training current.

Failure of any mandatory item produces `HOLD` unless a qualified `REWORK` path explicitly applies.

---

# 5. Release authority and review roles

A future laboratory shall assign named roles for:

- process owner;
- metrology owner;
- genealogy/material-control owner;
- DOE/statistical owner where an empirical campaign is active;
- EH&S/facility authority;
- independent reviewer for holdout/model-freeze release.

One person may hold more than one role in a small laboratory, but the role must still be recorded explicitly.

For protected holdout release and destructive consumption of the sole remaining bridge/FA reserve, require an independent second review whenever practical.

---

# 6. Chronological campaign map

The default development sequence is:

`G0 infrastructure/authorization`
`-> G1 Stage-0 to formal F2 LPE`
`-> G2 selected F2 roots to F3 anneal`
`-> G3 selected annealed descendants to F4 RIE/passivation`
`-> G4 selected RIE states to full detector fabrication`
`-> G5 detector characterization / F1`
`-> G6 singulation`
`-> G7 actual package build`
`-> G8 evidence promotion / P16E update / P17 handoff`.

This is a control sequence, not a requirement that every physical node visit every stage.

Nodes may terminate earlier as:

- material-only fit points;
- boundary samples;
- archive;
- destructive FA;
- process witnesses.

---

# 7. G0 — active-campaign authorization

## 7.1 Purpose

Prevent consumption of HgCdTe before the immediate process/measurement chain can produce interpretable evidence.

## 7.2 Required evidence

For the active campaign only:

- relevant P16C capability physically identified;
- relevant P16D IQ/OQ/surrogate acceptance PASS;
- relevant P16E uncertainty allocation supports the intended contrast/decision;
- active P16F model/experimental-unit/perturbation/holdout block defined;
- active P16G material allocation and protected-role map feasible;
- data/genealogy system functioning;
- EH&S/facility authorization current.

## 7.3 Decision

`GO` — campaign may consume the material class explicitly listed.

`HOLD` — missing capability/evidence; do not use HgCdTe as a substitute commissioning artifact.

`REWORK` — only for a qualified infrastructure/configuration correction followed by repeat acceptance.

`STOP` — active campaign abandoned/replaced; preserve material for another approved role.

---

# 8. G1 — Stage-0 LPE release to formal F2 DOE

## 8.1 Required Stage-0 outputs

Before releasing the formal independent-growth set:

- actual LPE apparatus branch identified;
- charge/thermal/contact realization sufficiently controlled for the selected factors;
- at least the Stage-0 data required by P22/P22A available;
- P06 measurement repeatability and fit stability measured;
- independent-growth variance estimate available for protected responses;
- morphology/feasible region preliminarily bounded;
- information-resolution calculation complete;
- same-regime upper bound on each selected perturbation justified;
- exact F2 design matrix and run-order/block structure frozen;
- formal holdout growth states frozen;
- Stage-0 centers classified as `FORMAL-CENTER-REUSED` or `PILOT-NONREUSABLE` before seeing future DOE outcomes;
- P16G structural root/material plan closes.

## 8.2 Resolution gate

For every active factor `u_i`, document that the planned half-range satisfies both:

`Delta u_i >= information lower bound`

and

`Delta u_i <= same-regime physics upper bound`.

If these bounds do not overlap, the design is not ready.

Disposition: `HOLD` and improve measurement/process stability or redesign the factorization.

## 8.3 Run-order rule

Create the full feasible randomization/blocking plan before the first formal DOE root is executed.

Hard constraints such as source-use sequence may remain nonrandom, but they must be encoded as blocks/covariates.

Do not assign all low states early and high states late unless the design intentionally estimates that time/source effect.

---

# 9. F2 run execution control

For every formal growth:

1. verify G1 still valid;
2. execute the assigned design state;
3. retain realized physical controls, not setpoint only;
4. perform P06 on intact material where geometry permits;
5. classify execution deviation before examining downstream detector performance;
6. assign root to fit/holdout/failure-boundary according to frozen rules;
7. update material geometry and descendant availability in P16G.

### 9.1 Adaptive F2 designs

If a sequential/adaptive design is used:

- selection algorithm/criterion must be frozen before candidate response inspection;
- candidate set and feasibility constraints must be logged;
- expected information/decision-value score retained;
- the selected next state and rejected alternatives retained.

Adaptive design is controlled selection, not operator intuition.

---

# 10. G2 — release selected F2 material to anneal

## 10.1 Why this gate exists

Annealing consumes process optionality. It changes carrier state and potentially optical state. Therefore intact grown material should not be annealed merely because it exists.

## 10.2 Required evidence

- P06 raw spectra/map accepted;
- local thickness/composition/edge descriptors recorded;
- morphology and usable polygon identified;
- selected root role identified by F2/F3 plan;
- P05 branch allocated;
- F2 holdout status preserved;
- F3 treatment history and independent-unit definition assigned;
- pre-anneal state stored;
- enough untreated/alternate descendants remain if required by the design.

## 10.3 Root-selection bias control

A root may be advanced because it is:

- a predetermined design state;
- a predetermined center/control;
- an information-optimal adaptive choice under a frozen criterion;
- a deliberate failure/boundary challenge.

Do not advance only the visually best roots and then interpret F3 as representative of F2.

---

# 11. F3 anneal execution / boundary control

## 11.1 Run identity

Each independent anneal history records:

- sample/root block;
- ampoule/enclosure ID;
- Hg source/reservoir state;
- sample and Hg-zone temperature traces;
- dwell;
- cooldown;
- co-loaded sample IDs;
- run order;
- deviations.

Co-loaded pieces are tagged as within-history siblings unless local evidence supports a different independent-unit definition.

## 11.2 Boundary samples

Carrier-transition samples are valuable classifier evidence but are not automatically standard detector inputs.

After P05:

- stable n-like -> candidate for continuous n-like Jacobian / downstream detector path;
- transition/multicarrier -> F3 boundary evidence; standard detector path `HOLD/STOP` unless explicitly studying that regime;
- unintended p-like/outside-region -> retain as boundary/failure evidence; do not hide it by excluding from the campaign.

---

# 12. G3 — anneal to RIE/passivation release

Required:

- anneal execution valid;
- P05 carrier sign/state established;
- P06 optical-preservation comparison complete where required;
- local material state lies inside the intended F4 input regime;
- F4 chamber/treatment plan frozen;
- witness structures and detector-bearing descendants allocated separately;
- RIE chamber acceptance current;
- material balance remains feasible after allocation.

### 12.1 HOLD triggers

- Hall contacts/process may have altered intended device input and reuse was not qualified;
- multicarrier state incompatible with the chosen detector model;
- optical edge/thickness changed beyond the study's declared acceptable input region;
- remaining material cannot support required F4 witnesses/holdouts.

---

# 13. F4 RIE/passivation staging

F4 shall normally execute in two material-cost tiers.

## Tier 1 — witness-dominant process-state learning

For each exploratory chamber state, prioritize the minimum physical structures needed to determine:

- oxide clear / recession;
- plasma realized state;
- converted sheet transport;
- conversion depth/lateral extent where selected;
- contact/TLM state where needed;
- stability over the intended handoff interval.

## Tier 2 — detector-bearing confirmation

Release full detector descendants only for states that are:

- center/baseline states;
- high-information contrasts;
- model-required combined states/interactions;
- independent holdouts;
- deliberate detector-bridge points.

This tiering is mandatory unless a documented geometry/process reason makes witness-only treatment impossible.

---

# 14. G4 — witness state to full detector-bearing fabrication

This gate requires:

- valid RIE chamber execution;
- relevant material-state witness results accepted;
- no unresolved chamber excursion;
- RIE-to-metal timing/stability compatible with the intended state;
- full detector geometry/process branch ready;
- P24/P25/P26/P27/P28/P32 dependencies frozen as required by the selected path;
- protected detector comparison/control state identified;
- information-value justification for spending a full detector descendant;
- post-commit material balance PASS.

### 14.1 Dominated-state rule

If one candidate chamber state has no greater expected detector-decision information than another feasible state while requiring more HgCdTe or creating greater confounding risk, it should not receive a detector descendant without a documented scientific reason.

---

# 15. Detector fabrication execution control

For each detector-bearing descendant preserve:

- root/growth state;
- anneal state;
- mesa/passivation revision;
- RIE treatment and chamber position;
- Cr/Au deposition state;
- mask/CD state;
- contact pair/gap;
- elapsed handoff times;
- singulation status;
- package status.

Do not assemble P10/P11/P12/P13 performance from mismatched descendants unless an explicit correction/bridge model is part of the analysis.

---

# 16. G5 — completed detector to matched characterization/F1

Before high-value detector characterization:

- continuity and pad integrity PASS;
- actual geometry measured;
- contact pair named;
- basic I-V suitable for the intended bias range;
- detector temperature measurement active;
- relevant P10/P11/P12/P13 measurement chains commissioned;
- common state vector frozen;
- maximum field/power/heating guard defined;
- measurement order frozen or counterbalanced if order effects are possible.

Preferred sequence where reversible:

`P10 -> P11 -> P12 -> P13 -> F1 local field derivative`.

If a measurement is suspected to alter the device, place it after non-invasive measurements or allocate a separate descendant and document the reason.

---

# 17. G6 — detector to singulation

Singulation is not a neutral logistics step.

Require:

- pre-singulation P10 baseline;
- P12/P11 baseline where the P35 qualification design needs them;
- P35 selected branch/tool/support/protection instantiated;
- street/kerf/edge-exclusion layout frozen;
- die outline compatible with P33 package;
- method has sufficient surrogate/actual-stack evidence for this release tier;
- unsingulated comparator/archive preserved if required;
- package role still protected.

After singulation, measure the P35 required post-cut state before G7.

---

# 18. G7 — singulated die to actual package build

Require:

- die-edge/chip/subsurface checks accepted under selected P35 branch;
- electrical/noise degradation check accepted where required;
- exact die identity/genealogy retained;
- selected P33 carrier/adhesive/interconnect family passed surrogate screen;
- actual package DOE/build level assigned prospectively;
- paired pre-package detector baseline complete;
- package fixture/vacuum/cryogenic measurement chain ready;
- remaining protected die reserve feasible.

### 18.1 Package holdout

An independent package holdout is locked before its post-package response is measured.

A package that fails its holdout prediction remains a failed holdout unless a documented execution-invalidity criterion is met.

---

# 19. G8 — evidence promotion / allocation update

After each F1-F5 campaign block:

1. freeze the final fitted model revision;
2. check rank/conditioning/model discrepancy;
3. evaluate the predeclared holdout;
4. calculate uncertainty in the protected derivative/boundary;
5. determine local valid range;
6. determine whether detector bridge is complete;
7. update P20/P16E contribution;
8. update P16F evidence state;
9. update P16G reserve/terminal material state;
10. decide whether another run has material decision value.

Allowed empirical evidence progression remains:

`EMPIRICAL-REQUIRED`
`-> DESIGN-IDENTIFIED`
`-> DESIGN-RESOLUTION-VERIFIED`
`-> EMPIRICAL-PRELIMINARY`
`-> EMPIRICAL-VERIFIED`
`-> DETECTOR-BRIDGED`
`-> ALLOCATION-ELIGIBLE`.

No stage is skipped because the numerical value happens to look plausible.

---

# 20. Run-order and block sheet

For each campaign fill:

| factor/state | type | randomizable? | block/covariate | physical constraint | run-order risk |
|---|---|---|---|---|---|
|  | easy-to-change / hard-to-change / sequential |  |  |  |  |

Then create a run-order table:

| execution order | design row | root/block | source/chamber/ampoule state | operator/time | randomized/counterbalanced rationale |
|---:|---|---|---|---|---|
|  |  |  |  |  |  |

The analysis model must reflect hard-to-change structure where applicable.

---

# 21. Dynamic holdout and reserve control

## 21.1 Holdout lock

Before processing a holdout, record:

- protected model/decision;
- process state;
- independent-unit basis;
- response vector;
- model-freeze event;
- replacement rule if execution-invalid.

## 21.2 Reserve release

A reserve node may move from `RESERVE-LOCKED` to `RESERVE-RELEASED` only when:

- the protected future role is no longer required; or
- a substitute node of equivalent genealogy/statistical role has been formally allocated; or
- the campaign has been redesigned and the prior protected role has been explicitly retired.

The reason must be recorded before the reserve is consumed.

---

# 22. Failure and deviation routing

When a process or measurement fails:

## Step 1 — freeze siblings

Do not immediately consume the next reserve/holdout sample.

Place potentially affected siblings in `HOLD`.

## Step 2 — classify event

- instrument/measurement invalidity;
- handling damage;
- process excursion;
- true treatment response;
- identity/genealogy error;
- unknown.

## Step 3 — invoke P18

Use the appropriate diagnostic branch and designated FA material where possible.

## Step 4 — decide

- resume `GO` if evidence shows no decision-affecting invalidity;
- `REWORK` only through a qualified route;
- replace an independent unit according to the frozen design rule;
- `STOP` the branch if the physical model/process family is invalid.

## Step 5 — preserve the record

No failed run is deleted from the campaign ledger.

If excluded from a fit, exclusion reason and predeclared criterion must be explicit.

---

# 23. Rework restrictions by evidence role

Rework can change a sample's scientific identity.

Examples:

- re-anneal changes F3 treatment history;
- repeat RIE changes dose/history;
- re-passivation changes surface-state branch;
- metal removal/redeposition changes contact genealogy;
- package rework changes F5 build state.

Therefore, after rework, determine whether the node remains eligible as:

- original fit point;
- new treatment point;
- holdout;
- bridge sample;
- engineering-only witness.

Do not keep the old role automatically.

---

# 24. Next-action review

At each major gate ask:

> Is the next protected uncertainty best reduced by another upstream information-rich run, or by consuming an existing descendant downstream?

Record for each candidate action:

- protected uncertainty contribution;
- expected reduction if successful;
- HgCdTe burden;
- independent-unit burden;
- downstream optionality lost;
- confounding risk;
- availability of surrogate alternative;
- whether action is Pareto-dominated.

Do not spend a detector die to answer a question that can be resolved by a lower-tier material witness unless the detector bridge itself is the quantity being learned.

---

# 25. Campaign pause / configuration change

A paused campaign must undergo re-entry review if any of the following changed:

- hardware;
- fixture/holder;
- source lot;
- gas/MFC;
- chamber clean/season basis;
- thermal sensor or calibration;
- optical/electrical transfer chain;
- analysis/model revision;
- sample-contact preparation;
- package construction.

A calendar-valid calibration does not prove configuration equivalence after physical modification.

---

# 26. Minimum gate evidence package

Every `GO` shall archive at minimum:

1. gate ID;
2. material node genealogy;
3. current physical state/geometry;
4. required upstream measurement IDs;
5. uncertainty/acceptance result;
6. active procedure/configuration/calibration revisions;
7. DOE/model/holdout role;
8. pre/post-commit material-feasibility check;
9. decision outcome;
10. reviewer/signature/date.

A verbal release is not a controlled release.

---

# 27. P16H connection

P16H is the laboratory fill-in register for this procedure.

`P16H-SEQUENTIAL-MATERIAL-RELEASE-CONTROL-READY = YES`

requires the active laboratory to have:

- named release roles;
- instantiated gate records;
- active configuration control;
- locked holdout/reserve assignments;
- post-commit feasibility checks;
- failure/rework routing;
- audit trail.

Current repository state remains `NO / NOT PHYSICALLY INSTANTIATED`.

---

# 28. Non-promotion warning

A complete P22C/P16H system does not imply:

- any gate has actually passed;
- any local HgCdTe material exists;
- any empirical coefficient has been measured;
- P16E is complete;
- P16F/P16G are complete;
- P16A first-build readiness;
- historical RP-01 reproduction;
- P17 reproducible release.
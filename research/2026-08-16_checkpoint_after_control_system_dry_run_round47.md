# Research checkpoint — after zero-HgCdTe control-system dry run Round 47

**Date:** 2026-08-16 America/New_York  
**Repository:** `Kajin-0/MCT-Device`

## 1. Round objective

Round 46 defined sequential GO/HOLD/REWORK/STOP material-release control, but the architecture had not yet been exercised as a system.

Round 47 therefore performed a repository-only, zero-HgCdTe dependency and synthetic fault-injection dry run.

Goals:

1. identify circular prerequisites/deadlocks;
2. test failure containment;
3. test holdout/reserve behavior;
4. test configuration invalidation;
5. verify that unrelated downstream capability does not block upstream learning;
6. verify that evidence promotion fails safely.

No real HgCdTe, hardware, calibration or local process result was assumed.

---

# 2. New controlled artifacts

Created:

- `calculations/RP01_CONTROL_DEPENDENCY_FAULT_INJECTION.md`;
- `procedures/P22D_ZERO_HGCDTE_CONTROL_SYSTEM_DRY_RUN.md`;
- `travelers/P16I_CONTROL_SYSTEM_DRY_RUN_REGISTER.md`;
- `docs/SOURCE_LEDGER_ADDENDUM_ROUND47.md`;
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND47.md`;
- this checkpoint.

Round 47 also repairs the P16F/P16G interface and refreshes `AGENTS.md`.

---

# 3. New integration state — P16I

Two states are deliberately separated:

`P16I-LOGIC-DRY-RUN-PASSED`

and

`P16I-LAB-DRY-RUN-PASSED`.

Current:

- `P16I-LOGIC-DRY-RUN-PASSED = YES`;
- `P16I-LAB-DRY-RUN-PASSED = NO / NOT PHYSICALLY INSTANTIATED`.

The first means the tested repository control logic is internally coherent after the repairs below.

The second requires an actual lab traveler/LIMS/configuration system and cannot be claimed now.

---

# 4. Major finding 1 — real P16F/P16G prerequisite cycle

Before Round 47, the architecture could be read as:

`P16F -> P16G -> P16F`.

Why:

- P16G needs P16F's defined campaign structure/counts/holdout roles;
- final P16F disposition asks whether P16G genealogy/material feasibility passes.

Treating P16F as one monolithic readiness state therefore produces a directed cycle.

This was a genuine control-architecture defect.

---

# 5. P16F phase split

Round 47 repairs the cycle by defining three scoped P16F states.

## 5.1 `P16F-CAMPAIGN-SKELETON-DEFINED`

Enough to authorize Stage-0 learning:

- protected quantity;
- response vector;
- experimental unit;
- candidate factors/states;
- Stage-0 variance/repeatability plan;
- preliminary feasibility bounds.

No Stage-0 variance is required yet.

## 5.2 `P16F-DESIGN-DEFINITION-READY`

Post-Stage-0 state used by P16G:

- Stage-0 variance/repeatability;
- design/model family;
- structural count;
- perturbation-resolution window;
- blocks/hard-to-change structure;
- holdout structural requirement;
- stopping/invalidation rule.

## 5.3 `P16F-EMPIRICAL-JACOBIAN-CAMPAIGN-READY`

Final state after:

- design-definition readiness;
- P16G genealogy/material feasibility;
- relevant infrastructure/EH&S readiness.

Repaired chain:

`P16F skeleton -> Stage-0 -> P16F design definition -> P16G -> final P16F readiness`.

Post-repair directed-cycle count in the tested graph: **0**.

---

# 6. Major finding 2 — Stage-0 data-before-readiness ambiguity

A second potential deadlock existed if G0 were interpreted to require final P16F readiness before Stage-0.

That is impossible because Stage-0 variance/repeatability is needed to determine final information resolution and design readiness.

Round 47 freezes the scoped rule:

Stage-0 G0 requires:

- relevant P16C capability;
- relevant P16D acceptance;
- scope-adequate P16E discrimination;
- `P16F-CAMPAIGN-SKELETON-DEFINED`;
- Stage-0 protected-material allocation;
- data/genealogy controls;
- EH&S.

It does not require final P16F/P16G/P17 or unrelated package capability.

---

# 7. Dependency graph result

The repaired principal spine is:

`P16B`
`-> P16C`
`-> P16D`
`-> scoped P16E`
`-> P16F skeleton`
`-> G0 Stage-0`
`-> Stage-0 data`
`-> P16F design definition`
`-> P16G`
`-> P16F final readiness`
`-> G1`
`-> F2/G2`
`-> F3/G3`
`-> F4 Tier-1/G4`
`-> detector/G5`
`-> G6`
`-> G7`
`-> G8`.

P16H is the operating gate/control system around the spine; it can be instantiated before every campaign is empirically complete.

No numerical critical-path duration is claimed because task durations do not exist.

---

# 8. Major finding 3 — failure containment must be local but strict

Round 47 formalizes the **minimum justified invalidation set**.

A fault invalidates:

- the directly affected node/configuration;
- descendants whose validity depends on that state/equivalence;
- prior releases only where they reused the invalidated state without an independent preserved baseline.

Do not globally invalidate unrelated evidence without common-cause support.

Do not shrink containment to preserve schedule/material.

Synthetic MFC replacement case demonstrates the intended behavior:

- RIE gas-delivery acceptance becomes HOLD/requalification-required;
- future RIE releases are held;
- independent FTIR/Hall/package evidence remains intact absent common cause.

---

# 9. Major finding 4 — scientific holdout failure is not invalidity

Round 47 explicitly dry-runs two different cases.

### Valid measurement, bad prediction

- prediction fails;
- holdout remains valid evidence;
- G8 promotion is blocked/downgraded;
- revised model needs a new independent holdout.

### Invalid execution

- predeclared validity criterion fails;
- observation may be invalidated;
- replacement follows the frozen rule;
- protected outcome cannot leak into tuning.

This distinction is now a required P16I test.

---

# 10. Major finding 5 — technical PASS can still produce HOLD

Synthetic FI-07 sets:

`T=PASS`

but

`M=FAIL`

because consuming the promising RIE descendant would destroy the sole remaining bridge/holdout.

Correct disposition:

`NO GO`.

This directly stress-tests the Round-46 two-pass release equation.

---

# 11. Major finding 6 — holdouts are not emergency spares

Synthetic loss of a fit-point sample does not release a locked holdout.

Allowed responses are:

- consume a process reserve whose trigger applies;
- execute the predeclared replacement strategy;
- redesign/stop the campaign.

Forbidden:

- silently relabel the holdout as replacement fit material.

This preserves the very independence that justifies the holdout.

---

# 12. Major finding 7 — state-changing rework invalidates role by default

Synthetic re-anneal/re-RIE of a holdout demonstrates:

- node can remain useful material;
- original scientific identity does not survive automatically;
- original holdout/fit role must be removed unless explicit equivalence is demonstrated;
- new treatment/engineering role is assigned prospectively.

---

# 13. Fault-injection summary

Fifteen synthetic cases were exercised:

1. irrelevant package subsystem unavailable during upstream Stage-0;
2. P16F/P16G cycle;
3. P06 repeatability failure;
4. LPE execution excursion;
5. anneal multicarrier transition;
6. RIE chamber excursion;
7. material shortage despite technical PASS;
8. valid holdout prediction failure;
9. execution-invalid holdout;
10. MFC/configuration change;
11. attempted holdout-as-spare use;
12. state-changing holdout rework;
13. genealogy loss;
14. detector test-chain invalidity;
15. package holdout failure.

Pre-repair architecture defects detected:

- directed prerequisite cycles: `1`;
- Stage-0 scope ambiguity: `1`.

Post-repair:

- directed prerequisite cycles: `0`;
- fail-safe declared synthetic cases: `15/15`.

`15/15` is not a reliability statistic. It only records that the tested cases obey the repaired control invariants.

---

# 14. Maturity state

Still NO / open as applicable:

- `TRACEABLE-FIRST-BUILD-READY`;
- `HISTORICAL-RP01-REPRODUCED`;
- `REPRODUCIBLE-RELEASE`;
- `P16C-INFRASTRUCTURE-READY`;
- `P16D-SURROGATE-COMMISSIONING-COMPLETE`;
- `P16E-REQUIREMENTS-ALLOCATION-COMPLETE`;
- `P16F-EMPIRICAL-JACOBIAN-CAMPAIGN-READY`;
- `P16G-MATERIAL-GENEALOGY-PLAN-READY`;
- `P16H-SEQUENTIAL-MATERIAL-RELEASE-CONTROL-READY`.

New validated repository-level state:

`P16I-LOGIC-DRY-RUN-PASSED = YES`.

Physical implementation remains:

`P16I-LAB-DRY-RUN-PASSED = NO / NOT PHYSICALLY INSTANTIATED`.

---

# 15. Strategic state after Round 47

The project now has:

**candidate branch + capability requirements + commissioning acceptance + uncertainty architecture + information-optimal DOE + genealogy/material accounting + sequential release control + synthetic control-system validation**.

It still has no actual laboratory implementation.

---

# 16. Next logical work — Round 48

The strongest next step is a **machine-checkable digital provenance / traveler schema** rather than another prose procedure.

Round 48 should define normalized records for:

- material nodes and parent-child genealogy;
- process/treatment events;
- measurements/raw-data references;
- configuration/calibration objects;
- gate decisions;
- holdout locks and access events;
- reserve locks/releases;
- model-freeze events;
- deviations/rework;
- evidence promotion;
- audit/signature events.

It should then encode state-transition constraints such as:

- no GO unless required prerequisites and T/M passes exist;
- no holdout outcome open before model freeze;
- no reserve use before release trigger;
- no reworked node retaining protected role without reassignment;
- no child without immutable parent genealogy;
- configuration change invalidates dependent future releases.

That work remains zero-HgCdTe and would directly support the later physical P16I lab dry run.
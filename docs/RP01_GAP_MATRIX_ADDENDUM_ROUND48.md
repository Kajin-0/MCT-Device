# RP-01 gap matrix addendum — Round 48 digital provenance

**Date:** 2026-08-16 America/New_York  
**Scope:** machine-checkable provenance/state-transition control

## 1. Purpose

Round 48 does not close historical RP-01 process gaps.

It closes a systems-control gap identified after Round 47:

> The project had a coherent prose state machine but no normalized, executable data contract capable of rejecting invalid genealogy/release/holdout/rework states automatically.

---

# 2. Gap-state vocabulary

New Round-48 states:

- `MACHINE-SCHEMA-DEFINED`
- `SEMANTIC-VALIDATOR-DEFINED`
- `SYNTHETIC-VALIDATION-PASSED`
- `LAB-DATA-MODEL-OPEN`
- `LAB-PERMISSIONS-OPEN`
- `LAB-SIGNATURE-TRUST-OPEN`
- `LAB-RAW-HASH-INGEST-OPEN`
- `LAB-CONFIGURATION-INTEGRATION-OPEN`
- `LAB-APPEND-ONLY-STORAGE-OPEN`
- `LAB-P16I-DRY-RUN-OPEN`

---

# 3. Gap matrix

| Gap | Pre-R48 state | Round-48 action | Post-R48 state | Physical implication |
|---|---|---|---|---|
| normalized material-state record | prose only | JSON schema | `MACHINE-SCHEMA-DEFINED` | none |
| physical object vs scientific state identity | conceptual | separate IDs + validator | `SEMANTIC-VALIDATOR-DEFINED` | none |
| genealogy DAG enforcement | dry-run logic | cycle/root/chronology validator | `SYNTHETIC-VALIDATION-PASSED` | none |
| split lineage | prose genealogy | `SPLIT` mode | `SEMANTIC-VALIDATOR-DEFINED` | none |
| process input/output traceability | prose | event lineage check | `SEMANTIC-VALIDATOR-DEFINED` | none |
| gate prerequisite traceability | aggregate PASS/HOLD | prerequisite assertions | `SEMANTIC-VALIDATOR-DEFINED` | none |
| T/M GO equation | prose/register | executable rejection | `SYNTHETIC-VALIDATION-PASSED` | none |
| configuration validity | prose/fault injection | time-bound objects | `SYNTHETIC-VALIDATION-PASSED` | none |
| calibration/config binding | prose | explicit binding | `SYNTHETIC-VALIDATION-PASSED` | none |
| holdout outcome sealing | prose/register | access events + model freeze | `SYNTHETIC-VALIDATION-PASSED` | none |
| holdout training leakage | conceptual | cross-record rejection | `SYNTHETIC-VALIDATION-PASSED` | none |
| reserve lock/release | prose state machine | append-only lock/release | `SYNTHETIC-VALIDATION-PASSED` | none |
| rework role reassignment | prose | new state + protected-role check | `SYNTHETIC-VALIDATION-PASSED` | none |
| evidence progression | prose | one-step validator | `SEMANTIC-VALIDATOR-DEFINED` | none |
| raw-data content identity | open | URI + SHA-256 field | `MACHINE-SCHEMA-DEFINED` | actual hashing still open |
| CI regression protection | absent | GitHub Actions self-test | `MACHINE-SCHEMA-DEFINED` | no lab implication |
| lab LIMS/database | absent | interface requirements defined | `LAB-DATA-MODEL-OPEN` | blocks lab P16J |
| real access control | absent | required fields only | `LAB-PERMISSIONS-OPEN` | blocks sealed holdout claim |
| trusted signatures | absent | audit record only | `LAB-SIGNATURE-TRUST-OPEN` | blocks strong electronic-signature claim |
| automatic raw hash ingest | absent | schema field only | `LAB-RAW-HASH-INGEST-OPEN` | blocks automated integrity claim |
| actual configuration integration | absent | schema model only | `LAB-CONFIGURATION-INTEGRATION-OPEN` | blocks lab P16J |
| append-only/tamper evidence | absent | philosophy documented | `LAB-APPEND-ONLY-STORAGE-OPEN` | blocks lab P16J |
| real system dry run | absent | P16J handoff defined | `LAB-P16I-DRY-RUN-OPEN` | no physical readiness |

---

# 4. Important closure distinction

Round 48 establishes:

`logic encoded != lab system installed != permissions enforced != physical data captured`.

Therefore:

`P16J-REPOSITORY-PROVENANCE-VALIDATOR-PASSED = YES`

does not imply:

`P16J-LAB-PROVENANCE-SYSTEM-READY = YES`.

---

# 5. Historical RP-01 gaps unchanged

Examples still open include:

- exact original LPE boat dimensions/absolute charge/trajectory;
- exact substrate supplier face/miscut/final surface;
- exact Hg anneal traveler;
- exact Mask-1 and Mask-2 product/exposure/developer details;
- exact wet-mesa chemistry basis and handoff;
- exact UWA anodization execution details;
- exact RIE gas realization/reactor/sheath/sample temperature;
- exact Cr/Au deposition hardware/rates/vacuum/handoff;
- exact singulation/package traveler;
- exact spectral-cutoff convention;
- direct lifetime/f3dB data.

A digital schema cannot close documentary history.

---

# 6. Physical maturity unchanged

Still NO/open as applicable:

- `TRACEABLE-FIRST-BUILD-READY`;
- `HISTORICAL-RP01-REPRODUCED`;
- `REPRODUCIBLE-RELEASE`;
- P16C–P16H physical/readiness states;
- `P16I-LAB-DRY-RUN-PASSED`.

Repository-only states may be YES without physical promotion.

---

# 7. Next closure path

To move `P16J-LAB-PROVENANCE-SYSTEM-READY` toward YES, a real laboratory must instantiate:

1. actual configuration IDs;
2. actual calibration objects;
3. actor identity/authentication;
4. protected holdout-field permissions;
5. raw-data hashing/storage;
6. append-only/auditable record persistence;
7. reserve/gate UI enforcement;
8. dummy/surrogate end-to-end G0–G8 traversal;
9. configuration-change fault injection;
10. P16I lab dry run.

Do not consume HgCdTe merely to test the software/data system.

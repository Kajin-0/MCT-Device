# Digital provenance operational reference implementation — Round 49

**Classification:** derived internal control / software reference implementation  
**Date:** 2026-08-16 America/New_York

## 1. Purpose

Round 48 established a machine-readable data contract and semantic validator. Round 49 answers the next question:

> Can those controls be exercised through an actual local transactional application rather than static JSON fixtures?

The answer at repository-reference level is yes. This does not mean a laboratory deployment exists.

## 2. Architecture

The prototype uses only Python standard library and SQLite.

Layering:

`raw file -> content-addressed object store -> operational SQLite event store -> Round-48 bundle export -> Round-48 semantic validator`.

The SQLite layer is intentionally event-oriented. The application does not update a material node in place to represent anneal, RIE, singulation, package, rework, or another state-changing process.

## 3. Canonical identity namespaces

Round 49 standardizes generated IDs as:

`MCT-<CLASS>-YYYYMMDDTHHMMSSZ-<12-hex>`.

Controlled prefixes include:

- `MAT` material-state node;
- `PHY` persistent physical object;
- `PROC` process event;
- `MEAS` measurement;
- `CFG` configuration;
- `CAL` calibration;
- `GATE` release decision;
- `HOLD` holdout lock;
- `RSV` reserve lock;
- `REL` reserve release;
- `MODEL` model freeze;
- `ACC` access event;
- `DEV` deviation/rework;
- `PROM` evidence promotion;
- `AUD` audit event;
- `RAW` content-addressed raw object;
- `SIG` prototype signature event.

The random suffix prevents accidental collision; the timestamp improves human navigation but is not the authoritative event time.

## 4. Immutable record model

The primary `records` table stores:

- immutable record ID;
- record type;
- created-at time;
- actor ID;
- canonical JSON payload;
- SHA-256 of the canonical payload.

SQLite triggers reject UPDATE and DELETE on controlled append-only tables.

This is stronger than an application convention: ordinary SQL mutation through the same database connection fails.

It is not protection against a privileged operator replacing the database file itself.

## 5. Transaction semantics

Each logical write uses `BEGIN IMMEDIATE`.

`append_batch()` permits a topologically ordered group of records to commit atomically.

Round-49 synthetic physical state transitions use this for:

`new immutable material state + process event`.

Therefore a process transition either commits its new state/event group or rolls the transaction back.

## 6. Actor / role model

Prototype roles:

- `SYSTEM_ADMIN`;
- `PROCESS_OWNER`;
- `METROLOGY_OWNER`;
- `DOE_OWNER`;
- `MATERIAL_CONTROL`;
- `RELEASE_AUTHORITY`;
- `INDEPENDENT_REVIEWER`.

Representative policy:

| Action | Allowed role(s) |
|---|---|
| create material/process event | process owner, material control as applicable, admin |
| measurement/raw ingest | metrology owner, admin |
| model freeze | DOE owner, admin |
| reserve lock | material control, admin |
| reserve release | material control/release authority/admin |
| GO/HOLD/STOP gate record | release authority/admin |
| protected holdout outcome opening | independent reviewer/admin |
| signature record | release authority/independent reviewer/admin |

This is a reference policy, not a final staffing requirement.

## 7. Holdout sealing

Protected numerical outcomes are not stored inside the ordinary Round-48 measurement record.

They are stored in a separate append-only `sealed_outcomes` table keyed by:

- holdout-lock ID;
- measurement ID;
- field name.

The ordinary application read path therefore does not reveal the protected value.

`open_holdout_outcome()` requires:

1. an independent-reviewer/admin actor;
2. a model-freeze record;
3. the model freeze to list the holdout;
4. access time after freeze;
5. requested fields to be protected fields;
6. creation of a Round-48 `access_event` before returning the value.

### Security limit

This is logical/application sealing, not encrypted storage. Direct SQLite/file access can bypass it. Cryptographic sealing and real ACL enforcement remain future laboratory controls.

## 8. Raw-data ingest

Raw ingest performs:

1. SHA-256 of source bytes;
2. copy to a temporary file under the content-addressed object directory;
3. SHA-256 verification after copy;
4. atomic rename to `objects/sha256/<first2>/<digest>`;
5. immutable metadata insertion.

Round-49 testing intentionally changes a stored object's bytes and confirms `verify_raw()` fails, then restores the bytes and confirms verification recovers.

Bundle export refuses to proceed when any recorded raw object fails byte verification.

## 9. Reserve control

A reserve remains protected by the Round-48 `reserve_lock` record.

A GO directed at a locked node is rejected until a valid `reserve_release` exists whose:

- lock ID matches;
- trigger key exactly matches the frozen lock trigger;
- basis records exist;
- release time follows lock time.

The synthetic traversal proves both the denial and the legal release path.

## 10. Configuration supersession

Round 48 validates configuration/calibration state at recorded event time.

Round 49 adds operational supersession.

`supersede_configuration(old,new)` creates an append-only supersession relationship and explicit invalidation rows for all prior GO gates that depended on the old configuration.

Important interpretation:

- the old gate remains historical evidence of what was approved at that time;
- the gate becomes ineligible for future reuse after the configuration change;
- unrelated records are not invalidated automatically.

The prototype also blocks new records from using a superseded configuration at or after the supersession time.

## 11. Prototype signature semantics

A signature row binds:

- target record ID;
- immutable payload digest;
- actor ID;
- key ID;
- signed-at time.

The reference algorithm is HMAC-SHA256.

Round-49 self-test verifies:

- correct key succeeds;
- wrong key fails.

This is deliberately described as a **content-signature prototype** only. There is no production key-management or trusted identity layer.

## 12. Synthetic G0-G8 traversal

The automated traversal creates only synthetic material and data.

Nominal path:

`G0 -> LPE state -> G1 -> G2 -> anneal -> G3 -> RIE -> G4 -> detector -> G5 -> measurement -> G6 -> singulation split -> G7 -> package -> holdout -> model freeze -> protected outcome opening -> G8 -> evidence progression`.

Singulation is explicitly represented as a split into:

- package die;
- archive sibling.

This tests the Round-48 physical-object versus material-state model.

## 13. Round-49 self-test controls

The reference test verifies:

1. injected multi-record failure rolls back the entire batch;
2. a process-owner actor cannot create a release gate;
3. raw ingest and verification succeeds;
4. reserve lock blocks GO;
5. holdout outcome is blocked before freeze;
6. actor role blocks unauthorized holdout opening;
7. outcome opens after the correct model freeze;
8. all G0-G8 gates are GO in the nominal synthetic traversal;
9. content signature verifies;
10. wrong signing key fails;
11. SQL UPDATE of immutable record fails;
12. SQL DELETE of immutable record fails;
13. raw-byte tampering is detected;
14. restored raw bytes reverify;
15. configuration supersession propagates gate invalidations;
16. an invalidated gate cannot be reused;
17. new use of a superseded configuration is blocked;
18. canonical generated IDs are used;
19. on repository/CI execution, the exported bundle has zero Round-48 semantic-validator errors.

The local development escape hatch may skip item 19 only when the Round-48 validator module is absent from the temporary development directory. CI does not use that escape hatch.

## 14. New maturity state

Round 49 defines:

`P16K-REFERENCE-PROVENANCE-APPLICATION-PASSED`.

Repository result may be YES only after:

- operational self-test passes;
- G0-G8 synthetic traversal completes;
- Round-48 validator accepts the generated bundle;
- CI passes on the committed revision.

Separate future state:

`P16K-LAB-DEPLOYMENT-QUALIFIED`.

It remains NO because the reference SQLite program has not been deployed against real laboratory identities, permissions, instruments, configurations or data stores.

## 15. What Round 49 does not solve

Still open:

- OS-level multi-user security;
- real database server authorization;
- field encryption;
- protected key custody;
- trusted time;
- identity provider integration;
- regulatory electronic-signature requirements;
- backup/disaster recovery;
- instrument adapters;
- actual lab configuration registry;
- actual calibration ingestion;
- P16I lab dry run;
- any HgCdTe processing evidence.

## 16. Deployment implication

Round 49 is sufficient to prove that the Round-48 state model can support a concrete transactional application without immediately collapsing into mutable spreadsheet semantics.

The next step should test deployment mechanics and security boundaries using dummy/surrogate laboratory objects before any HgCdTe is admitted.

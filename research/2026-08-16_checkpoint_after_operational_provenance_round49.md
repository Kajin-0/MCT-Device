# Research checkpoint — after operational provenance reference implementation Round 49

**Date:** 2026-08-16 America/New_York  
**Repository:** `Kajin-0/MCT-Device`

## 1. Objective

Round 48 established a schema and semantic validator, but did not prove that the state model could support a transactional application.

Round 49 builds and tests a local reference application without HgCdTe.

## 2. New implementation

Added:

- `tools/mct_provenance_store.py`;
- `tools/run_round49_reference.py`;
- `provenance/reference/README.md`;
- `docs/DIGITAL_PROVENANCE_OPERATIONAL_REFERENCE_ROUND49.md`;
- `travelers/P16K_PROVENANCE_REFERENCE_IMPLEMENTATION_REGISTER.md`;
- `docs/SOURCE_LEDGER_ADDENDUM_ROUND49.md`;
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND49.md`;
- this checkpoint.

Updated:

- provenance-validation GitHub Actions workflow;
- `AGENTS.md`.

## 3. Major result — event-sourced SQLite prototype

The repository now contains a stdlib-only SQLite reference implementation.

Controlled tables preserve append-only history through mutation/delete triggers.

Physical state changes are committed through atomic batches rather than mutable sample rows.

## 4. Identity

Generated IDs use the controlled form:

`MCT-<CLASS>-YYYYMMDDTHHMMSSZ-<12-hex>`.

`physical_object_id` persists through ordinary state transitions.

A split creates new physical-object IDs while retaining material genealogy.

## 5. Holdout outcome path

Synthetic sequence successfully exercises:

`holdout measurement -> protected value stored separately -> pre-freeze access denied -> model freeze -> independent-reviewer access -> access event persisted`.

This is application-level logical sealing only. It is not encrypted storage.

## 6. Reserve path

Synthetic archive sibling is reserve-locked.

A GO on the locked node is rejected.

A matching append-only reserve release with the frozen trigger and basis record permits later use.

## 7. Raw data

Synthetic raw files are ingested into a SHA-256 content-addressed object store.

Copy integrity is verified before atomic rename.

The self-test changes stored bytes and confirms verification fails, restores the original bytes and confirms verification passes.

Bundle export re-verifies all stored raw objects.

## 8. Configuration change propagation

A second configuration supersedes the original configuration after the nominal traversal.

All nine G0-G8 GO approvals that depended on the old configuration are retained historically but marked nonreusable.

This resolves the operational distinction between:

- “the gate was valid when executed”; and
- “the old gate may be reused after the configuration changed.”

## 9. Signature semantics

The reference application implements HMAC-SHA256 over:

- target record ID;
- immutable payload SHA-256;
- actor label;
- key ID;
- signing time.

Correct key verification succeeds and wrong-key verification fails in the synthetic test.

No regulatory or identity-assurance claim is made.

## 10. Synthetic G0-G8 traversal

The automated path contains all nine release gates:

`G0, G1, G2, G3, G4, G5, G6, G7, G8`.

It also includes:

- LPE-like state transition;
- anneal-like state transition;
- RIE-like state transition;
- detector creation;
- measurement/raw data;
- singulation split into die/archive sibling;
- reserve protection;
- package state;
- holdout lock;
- model freeze;
- outcome access;
- evidence progression to `ALLOCATION-ELIGIBLE`.

All objects remain synthetic.

## 11. Local development result

The standalone operational layer passes 18/18 controls when executed in a temporary development directory without importing the Round-48 validator.

The local controls include transaction rollback, gate-role denial, append-only UPDATE/DELETE denial, raw integrity, reserve/holdout controls, signature semantics and configuration supersession.

The Round-48 integration check is deliberately marked `SKIPPED` in that mode rather than falsely counted as a pass.

The committed CI must run without the escape hatch and therefore requires:

- Round-48 validator import;
- zero semantic errors on the generated Round-49 bundle.

## 12. New state

`P16K-REFERENCE-PROVENANCE-APPLICATION-PASSED` is the repository-level application state.

It may be set YES only after final committed CI passes.

`P16K-LAB-DEPLOYMENT-QUALIFIED = NO / NOT PHYSICALLY INSTANTIATED`.

## 13. Physical maturity

No physical state changes:

- P16C infrastructure remains uninstantiated;
- P16D commissioning remains uninstantiated;
- P16E remains incomplete;
- P16F/P16G/P16H remain uninstantiated;
- P16I lab dry run remains NO;
- P16J lab provenance system remains NO;
- first-build/historical/reproducible release remain NO.

## 14. Next logical work — Round 50

If final Round-49 CI passes, the strongest next zero-HgCdTe step is a **deployment/security simulation** around the reference application:

1. define a concrete single-host deployment profile;
2. separate application/service/operator identities;
3. add cryptographic protected-field storage or explicitly justify another isolation mechanism;
4. add key rotation/key-ID lifecycle and signature verification history;
5. add backup/restore integrity testing;
6. add clock/timestamp trust policy;
7. add a dummy instrument-ingest adapter and configuration/calibration import;
8. run P16I laboratory-style dry-run scenarios against that deployed surrogate system.

Do not introduce real HgCdTe solely to test software controls.

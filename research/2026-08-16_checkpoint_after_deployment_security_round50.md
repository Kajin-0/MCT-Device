# Research checkpoint — after deployment/security simulation Round 50

**Date:** 2026-08-16 America/New_York  
**Repository:** `Kajin-0/MCT-Device`

## 1. Objective

Round 49 established an executable transactional provenance reference application. Round 50 tests whether that application can be surrounded by a concrete single-host deployment/security control layer without using HgCdTe.

Protected questions:

1. can service/operator capabilities be separated;
2. can revoked sessions be denied;
3. can obvious clock regression be detected;
4. can protected holdout raw bytes and values be isolated from the ordinary provenance store;
5. can key rotation/revocation preserve correct signature-trust semantics;
6. can stale instrument configuration be rejected before byte ingestion;
7. can backups be integrity-authenticated, deliberately corrupted, and restored;
8. can all earlier Round-48/49 provenance invariants remain valid.

No real material, instrument, laboratory host or human authentication system is used.

## 2. New implementation

Added:

- `tools/mct_deployment_control.py`;
- `tools/mct_protected_vault.py`;
- `tools/round50_fixture.py`;
- `tools/run_round50_security.py`;
- `provenance/deployment/README.md`;
- `docs/DIGITAL_PROVENANCE_DEPLOYMENT_SECURITY_ROUND50.md`;
- `travelers/P16L_DEPLOYMENT_SECURITY_DRY_RUN_REGISTER.md`;
- `docs/SOURCE_LEDGER_ADDENDUM_ROUND50.md`;
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND50.md`;
- this checkpoint.

Updated:

- `.github/workflows/provenance-validation.yml`;
- `AGENTS.md`.

## 3. New P16L states

Repository/reference state:

`P16L-REFERENCE-DEPLOYMENT-SECURITY-DRY-RUN-PASSED`.

Laboratory state:

`P16L-LAB-SECURITY-DEPLOYMENT-READY`.

Controlled result after final main CI:

- repository/reference = YES;
- laboratory = NO / NOT PHYSICALLY INSTANTIATED.

## 4. Major result — protected raw data required architectural repair

Round 49 separated protected parsed values from ordinary provenance records, but a protected measurement's raw instrument file could still enter the ordinary content-addressed store.

That means the protected outcome could remain recoverable even if the parsed value was logically sealed.

Round 50 repairs this by enforcing:

`ordinary raw CAS != protected holdout raw CAS`.

Both protected raw bytes and protected parsed values live in a separate restricted vault.

The ordinary measurement retains:

- result-field identity;
- `vault://sha256/<digest>` URI;
- SHA-256 digest.

The synthetic test inserts the unique marker:

`R50_PROTECTED_OUTCOME_9D08A8C6F2`

into the protected instrument file and requires that this marker cannot be found anywhere under the ordinary store root.

This is a genuine strengthening over Round 49.

## 5. Encryption design decision

No custom encryption format was added.

Reason:

- the reference implementation is Python-standard-library-only;
- the standard library does not provide a suitable production authenticated-encryption API;
- inventing encryption would create false security confidence.

Round 50 therefore uses filesystem/process split-store isolation as the reference mechanism and explicitly leaves production encryption/KMS selection open.

Permanent rule:

`split-store reference isolation != encrypted storage`.

## 6. Identity/action separation

Deployment identities are separate from the underlying Round-49 provenance actor labels.

Reference identity classes:

- instrument service;
- configuration/calibration service;
- signing service;
- backup service;
- release operator;
- independent reviewer;
- DOE owner;
- administrator.

The synthetic test proves at least two cross-role denials:

- instrument service cannot approve a gate;
- release operator cannot ingest instrument data.

Sessions are random bearer tokens; only SHA-256 token digests are stored.

A revoked session is rejected.

No real user authentication claim follows.

## 7. Clock consistency

The deployment layer records accepted UTC observations and local monotonic-clock observations.

Synthetic sequence:

- forward time accepted;
- backward wall-clock step rejected;
- later forward time accepted.

This is a chronological consistency check only.

It is not trusted UTC, NTP/PTP authentication, secure timestamping or signing-time attestation.

## 8. Dummy instrument/configuration path

Round 50 creates a synthetic calibration for the existing Round-49 configuration B and acquires a dummy CSV measurement.

It then creates configuration C, calibration C and supersedes B.

Observed control behavior:

1. a B-dependent GO becomes nonreusable;
2. the stale B adapter is rejected;
3. rejection occurs before any additional ordinary raw object is copied;
4. the C adapter can acquire successfully.

This ordering matters: a stale-state measurement should not create an uncontrolled raw artifact before validity is evaluated.

## 9. Protected holdout path

Synthetic sequence:

`holdout lock`
`-> protected raw acquisition into vault`
`-> protected value sealed in vault`
`-> pre-freeze outcome access denied`
`-> wrong-role access denied`
`-> model freeze`
`-> independent-reviewer outcome access`
`-> Round-48 access event retained in ordinary provenance`.

The new protected outcome does not use the Round-49 ordinary `sealed_outcomes` table.

## 10. Key lifecycle result

Reference signing-key states:

`ACTIVE -> VERIFY_ONLY -> REVOKED`.

Synthetic result:

1. key K1 signs a controlled gate;
2. rotation moves K1 to VERIFY_ONLY and creates K2 ACTIVE;
3. K1 historical signature remains cryptographically valid/trusted while K1 is VERIFY_ONLY;
4. K1 cannot create a new signature;
5. K2 signs and verifies;
6. K1 is revoked;
7. the old K1 signature still matches cryptographically but is returned with trust state `REVOKED`;
8. verification decisions are persisted.

Permanent interpretation:

`key revocation changes trust state; it does not rewrite historical bytes or make a previously valid MAC mathematically unequal`.

## 11. Key-storage limitation

Reference keys are random local files protected by mode `0600` inside a `0700` directory.

This is not:

- HSM/KMS/TPM custody;
- hardware-backed identity;
- dual control;
- key escrow;
- secure recovery;
- regulatory signing infrastructure.

No secrets are committed to the repository.

## 12. Backup/restore result

Round 50 creates an integrity-authenticated backup containing:

- main provenance database;
- deployment database;
- protected-vault database;
- ordinary CAS;
- protected CAS;
- canonical SHA-256 file manifest.

The manifest is authenticated with a dedicated backup HMAC key.

The backup deliberately excludes key files.

Synthetic fault test:

- good backup verifies;
- one backed-up file is modified;
- modified backup fails verification;
- untouched backup restores to a new root;
- restored ordinary raw objects verify;
- restored protected raw objects verify;
- restored main record count matches;
- restored vault counts match.

Important boundary:

`backup integrity != backup confidentiality`.

The backup is not encrypted.

## 13. File-mode profile

Reference checks pass for:

- signing key file `0600`;
- key directory `0700`;
- protected-vault root `0700`;
- ordinary store root `0700`.

This does not establish actual OS-user separation, ACL/MAC confinement or protection from a privileged host administrator.

## 14. Candidate-branch validation strategy

Unlike earlier direct-to-main rounds, Round 50 was first committed to an isolated branch because the new deployment/security code is a larger executable change.

Temporary branch:

`agent/round50-security-dryrun`.

Candidate commit:

`1639fee3f75d9ba11df066ed7d194c946953ac3d`.

Candidate tree:

`a86554f9b3a372918c3a131a5da6e6350205fd10`.

Candidate GitHub Actions run:

`31980899498`.

## 15. Candidate CI result

All workflow stages passed:

- schema JSON syntax;
- Round-48 provenance fixture suite;
- compile all operational modules;
- Round-49 reference self-test;
- Round-50 deployment/security self-test.

Round-50 integrated result:

- controls: `33/33 PASS`;
- Round-49 prerequisite: `19/19 PASS`;
- generated provenance records: `50`;
- Round-48 semantic errors: `0`;
- clock events: `3`;
- deployment keys: `3`;
- protected raw objects: `1`;
- protected values: `1`;
- signature verification events: `3`;
- configuration supersessions: `2` total in combined traversal;
- gate invalidations: `10` total in combined traversal.

Candidate CI is pre-promotion evidence. Final repository state requires the final main commit to reproduce it.

## 16. Declared Round-50 checks

The 33 controlled checks are:

1. instrument service cannot approve gate;
2. release operator cannot ingest instrument data;
3. revoked session denied;
4. forward clock accepted;
5. clock backstep rejected;
6. later forward clock accepted;
7. dummy instrument B ingest;
8. config supersession invalidates dependent GO;
9. stale adapter rejected before copy;
10. replacement adapter ingest;
11. protected raw vault integrity;
12. protected outcome absent from ordinary store;
13. Round-49 ordinary sealed table unused for new protected outcome;
14. protected outcome denied before freeze;
15. protected outcome wrong-role denied;
16. protected outcome opens after freeze;
17. signing-key rotation identifies old key;
18. verify-only historical signature remains trusted;
19. retired key cannot sign;
20. rotated-key signature trusted;
21. revoked-key signature not trusted;
22. signature verification history recorded;
23. key file mode 0600;
24. key directory mode 0700;
25. protected vault directory mode 0700;
26. ordinary store directory mode 0700;
27. backup manifest verifies;
28. backup excludes key material;
29. backup tamper detected;
30. restored main record count matches;
31. restored vault count matches;
32. Round-48 semantic validator zero errors;
33. Round-49 prerequisite remains full pass.

## 17. Maturity after Round 50

Repository software/control states that may be YES after final CI:

- `P16I-LOGIC-DRY-RUN-PASSED`;
- `P16J-REPOSITORY-PROVENANCE-VALIDATOR-PASSED`;
- `P16K-REFERENCE-PROVENANCE-APPLICATION-PASSED`;
- `P16L-REFERENCE-DEPLOYMENT-SECURITY-DRY-RUN-PASSED`.

Remain NO/open:

- P16C infrastructure;
- P16D surrogate commissioning;
- P16E allocation completion;
- P16F campaign readiness;
- P16G material genealogy implementation;
- P16H laboratory release control;
- P16I laboratory dry run;
- P16J laboratory provenance system;
- P16K lab deployment qualification;
- P16L lab security deployment;
- TRACEABLE-FIRST-BUILD-READY;
- HISTORICAL-RP01-REPRODUCED;
- REPRODUCIBLE-RELEASE.

No physical maturity promotion occurred.

## 18. Next logical work — Round 51

The strongest next step is to leave the single-process CI model and construct a **reproducible real-host surrogate deployment harness**.

Priority:

1. declarative host bootstrap;
2. genuinely separate OS service users;
3. file ownership, group and ACL tests;
4. service confinement;
5. select vetted encryption/KMS technology for protected storage rather than inventing cryptography;
6. signing/backup key custody and recovery design;
7. external time synchronization/failure policy;
8. synthetic serial/network instrument endpoint;
9. concurrent-writer, crash/restart, disk-full and read-only-filesystem testing;
10. backup loss/key loss/partial recovery cases;
11. full no-HgCdTe P16I-style traversal on the deployed host.

Only after such a host exists should the project consider promoting any laboratory deployment state.
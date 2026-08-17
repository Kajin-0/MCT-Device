# Digital provenance deployment/security control — Round 50

**Status:** CONTROLLED ZERO-HgCdTe DEPLOYMENT/SECURITY SIMULATION  
**Date:** 2026-08-16 America/New_York

## 1. Question

Round 49 proved that a transactional provenance application can implement the controlled genealogy/release model. Round 50 asks a narrower next question:

> Can a concrete single-host reference deployment preserve those controls when identity boundaries, protected holdout data, signing keys, time, backups and instrument/configuration interfaces are exercised adversarially?

The answer at repository/reference level is YES for the declared synthetic tests. No real laboratory deployment exists.

## 2. New state

Repository/reference state:

`P16L-REFERENCE-DEPLOYMENT-SECURITY-DRY-RUN-PASSED`

Laboratory state:

`P16L-LAB-SECURITY-DEPLOYMENT-READY`.

Round-50 controlled disposition after final main CI:

- reference dry run = YES;
- laboratory deployment = NO / NOT PHYSICALLY INSTANTIATED.

## 3. Threat/failure model exercised

The reference test intentionally challenges:

1. cross-role privilege use;
2. revoked application session reuse;
3. backwards wall-clock movement;
4. stale instrument configuration reuse;
5. protected holdout raw-data leakage into the ordinary store;
6. pre-freeze protected-outcome access;
7. wrong-role protected-outcome access;
8. signing-key rotation;
9. use of retired signing keys;
10. trust interpretation after key revocation;
11. permissive file/directory modes;
12. backup corruption;
13. partial/incorrect restore state;
14. regressions against Round-48/49 invariants.

It does not simulate root compromise, kernel compromise, malicious SQLite replacement, memory scraping, physical host theft, network interception or sophisticated cryptanalysis.

## 4. Identity/session control

A deployment identity maps to a Round-49 provenance actor but is not identical to it.

The deployment layer uses separate identity types and allowed action sets. This prevents an instrument-service session from approving a release gate and prevents a release-operator session from ingesting instrument data.

Sessions are random bearer credentials. Only their SHA-256 digest is stored. Revocation is append-only.

Important limitation:

`session authorization != authenticated human identity != secure OS service account`.

The repository test proves policy behavior only.

## 5. Protected data architecture

### 5.1 Why split-store isolation

Round 49 isolated protected values logically but ordinary raw files could still contain the protected measurement outcome.

Round 50 closes that reference-architecture leak by moving both protected raw bytes and protected parsed values to a separate vault.

A custom encryption format was deliberately rejected. Vetted authenticated encryption and key management should be selected during a real deployment rather than reimplemented ad hoc.

### 5.2 Ordinary store

Contains:

- immutable measurement metadata;
- protected field names;
- vault URI;
- SHA-256 identity;
- model freeze;
- access event.

### 5.3 Protected vault

Contains:

- protected CAS object;
- protected value;
- holdout/measurement identity needed to recover the value.

Synthetic marker scan requires that the protected value does not appear anywhere under the ordinary store root.

### 5.4 Remaining threat

Both roots reside on the same synthetic host and are accessible to the executing account. Mode bits alone do not defeat a privileged host administrator.

## 6. Key lifecycle semantics

The signing-key lifecycle is modeled as an append-only state history.

Allowed reference progression:

`ACTIVE -> VERIFY_ONLY -> REVOKED`.

Interpretation:

- ACTIVE: may sign and verify;
- VERIFY_ONLY: historical verification allowed; new signing forbidden by policy;
- REVOKED: historical HMAC can still match, but trust state is no longer TRUSTED.

This avoids the incorrect conclusion that revocation changes old bytes or makes an old MAC mathematically false.

Every signature verification produces an append-only verification event containing the contemporaneous trust interpretation.

## 7. Key-storage boundary

Reference keys are random 256-bit local files with `0600` mode in a `0700` directory.

This demonstrates lifecycle mechanics only.

Not established:

- hardware-backed keys;
- protected process memory;
- least-privilege OS service account;
- KMS/HSM/TPM policy;
- dual control;
- escrow/recovery;
- signer identity proof;
- nonrepudiation;
- regulatory signature compliance.

No key bytes are stored in the repository.

## 8. Time semantics

The deployment ledger records wall-clock UTC and a local monotonic observation.

A backwards wall-clock step relative to the last accepted event is rejected in the synthetic test.

This protects ordering consistency against an obvious local regression. It does not establish trusted time.

Production deployment must define the authoritative time source, synchronization/failure policy and what happens during loss of trusted synchronization.

## 9. Instrument/configuration adapter semantics

The dummy CSV adapter performs configuration/calibration preflight before raw-byte copy.

This sequencing is mandatory because rejecting the measurement after ingest would still create an uncontrolled artifact associated with a stale instrument state.

Round 50 demonstrates:

`configuration B + calibration B -> valid measurement`

then:

`configuration B superseded by C -> B-dependent GO nonreusable`

and:

`stale B adapter -> reject before CAS copy`

then:

`configuration C + calibration C -> valid replacement measurement`.

The adapter is synthetic and proves interface behavior, not a real instrument protocol.

## 10. Backup integrity model

Backup contents include:

- main provenance SQLite database;
- deployment-control SQLite database;
- protected-vault SQLite database;
- ordinary CAS;
- protected CAS;
- canonical integrity manifest.

The manifest is authenticated by a separate backup HMAC key.

Key material itself is excluded from the backup.

This creates an intentional operational dependency: real deployment needs an independent key-custody/escrow/recovery plan.

Round 50 proves:

- intact backup verifies;
- modified backup fails verification;
- intact backup restores to a new destination;
- restored ordinary raw objects verify;
- restored protected objects verify;
- restored record/vault counts match.

It does not prove backup confidentiality, remote durability, retention policy or disaster-site recovery.

## 11. Reference permissions

The simulation hardens key/store/vault directories to `0700` and controlled files to `0600` where applicable.

This is a minimum reference profile, not proof of real separation. A future deployment must explicitly test actual ownership, groups, ACLs, service identities and confinement.

## 12. CI result on isolated candidate

Temporary branch candidate:

`1639fee3f75d9ba11df066ed7d194c946953ac3d`.

GitHub Actions run:

`31980899498`.

Result:

- Round-48 fixture suite: PASS;
- Round-49 operational suite: 19/19 PASS;
- Round-50 deployment/security controls: 33/33 PASS;
- generated Round-50 provenance records: 50;
- Round-48 semantic errors in generated bundle: 0;
- protected vault: 1 raw object + 1 sealed value;
- configuration supersessions in combined run: 2;
- dependent gate invalidations: 10;
- signature verification events: 3.

The temporary branch validates the code before promotion to `main`. Final P16L repository YES requires the final controlled main commit to pass the same CI.

## 13. Round-50 control invariants

Freeze the following:

1. protected outcome bytes must not be copied to the ordinary CAS merely because the parsed value is sealed;
2. no homemade encryption scheme is acceptable as a substitute for vetted encryption/key-management technology;
3. bearer-session policy is not identity assurance;
4. retired signing keys cannot create new signatures;
5. revocation changes trust interpretation, not historical cryptographic equality;
6. backup integrity and backup confidentiality are separate properties;
7. backup key custody must be independent of the backup it authenticates;
8. a clock-regression guard is not trusted time;
9. stale configuration must be rejected before instrument raw-data ingestion;
10. configuration supersession preserves historical records but blocks future reuse where dependency exists;
11. repository deployment simulation is not a physical laboratory deployment;
12. no software-control result promotes HgCdTe process evidence.

## 14. Physical/laboratory boundary

Still absent:

- real host/service-account separation;
- real authentication provider;
- production encrypted protected storage;
- KMS/HSM or defined key custody;
- real backup medium/site and recovery drill;
- external trusted-time source;
- actual instrument interface;
- actual asset/configuration/calibration system;
- real lab operators and permissions;
- P16I lab dry run.

Therefore:

`P16L reference PASS != P16L lab ready != P16K lab deployment qualified != P16I lab dry run passed`.

## 15. Next high-value step

After final Round-50 CI, the strongest next zero-HgCdTe step is a **real-host deployment harness** rather than more in-process simulation:

- separate OS users/service accounts;
- declarative installation/service configuration;
- filesystem ownership/ACL/confinement tests;
- selected vetted encryption/KMS approach;
- external time synchronization policy;
- synthetic serial/network instrument endpoint;
- concurrent writer/crash/restart/disk-full/read-only-filesystem fault injection;
- backup loss and key-loss recovery cases;
- end-to-end surrogate P16I dry run on the deployed host.

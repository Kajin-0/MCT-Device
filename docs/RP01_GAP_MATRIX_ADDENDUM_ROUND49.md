# RP-01 gap-matrix addendum — Round 49 operational provenance reference implementation

**Date:** 2026-08-16 America/New_York

## New gap states

- `REFERENCE-APPLICATION-IMPLEMENTED`
- `REFERENCE-TRANSACTION-TESTED`
- `REFERENCE-ROLE-POLICY-TESTED`
- `REFERENCE-HOLDOUT-SEAL-TESTED`
- `REFERENCE-RAW-INTEGRITY-TESTED`
- `REFERENCE-CONFIG-INVALIDATION-TESTED`
- `REFERENCE-SIGNATURE-SEMANTICS-TESTED`
- `LAB-IDENTITY-INTEGRATION-OPEN`
- `LAB-ACL-ENFORCEMENT-OPEN`
- `LAB-ENCRYPTION-OPEN`
- `LAB-KEY-MANAGEMENT-OPEN`
- `LAB-TRUSTED-TIME-OPEN`
- `LAB-INSTRUMENT-INGESTION-OPEN`
- `LAB-BACKUP-RECOVERY-OPEN`

## Structural closures at repository level

| Question | Round-49 state | Comment |
|---|---|---|
| Can provenance records be stored append-only? | `REFERENCE-APPLICATION-IMPLEMENTED` | SQLite triggers used |
| Can multi-record physical transitions be atomic? | `REFERENCE-TRANSACTION-TESTED` | single transaction batch |
| Can role policy be enforced by application? | `REFERENCE-ROLE-POLICY-TESTED` | synthetic actors only |
| Can holdout outcome stay unavailable until freeze? | `REFERENCE-HOLDOUT-SEAL-TESTED` | application-level logical sealing |
| Can raw bytes be content-addressed/reverified? | `REFERENCE-RAW-INTEGRITY-TESTED` | SHA-256 CAS |
| Can configuration changes invalidate future gate reuse? | `REFERENCE-CONFIG-INVALIDATION-TESTED` | gate invalidation ledger |
| Can a record digest be signed/verified in prototype? | `REFERENCE-SIGNATURE-SEMANTICS-TESTED` | HMAC reference only |

## Still open before a real laboratory deployment

1. authenticated human/service identities;
2. operating-system/database authorization boundaries;
3. encrypted protected-field storage if required;
4. protected signing keys and signer identity;
5. trusted timestamp source;
6. backup/restore/disaster-recovery qualification;
7. instrument adapters and automatic ingest;
8. live configuration and calibration interfaces;
9. real lab actor-role assignment;
10. P16I laboratory dry run through the deployed system.

## Critical non-equivalence

`reference application passes != lab provenance system ready != P16I lab dry run passed != HgCdTe process validated`.

No physical-process gap is closed by Round 49.

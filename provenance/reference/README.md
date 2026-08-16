# Round-49 operational provenance reference implementation

This directory documents the executable local reference application layered on the Round-48 provenance schema and validator.

Core files:

- `tools/mct_provenance_store.py` — append-only SQLite/event-store reference implementation;
- `tools/run_round49_reference.py` — automated synthetic G0-G8 traversal and operational self-test;
- `schemas/mct_provenance_bundle.schema.json` — Round-48 exchange/data-shape contract;
- `tools/validate_mct_provenance.py` — Round-48 cross-record semantic validator.

## Run

From repository root:

```bash
python tools/run_round49_reference.py
```

For inspection of the generated database/bundle:

```bash
python tools/run_round49_reference.py --workdir /tmp/mct-r49
```

The persistent work directory contains:

- `provenance.sqlite3`;
- `objects/sha256/...` content-addressed raw objects;
- `round49_generated_bundle.json`;
- `round49_result.json`.

## What the reference implementation enforces

- canonical ID namespaces;
- append-only provenance tables through SQLite mutation/delete triggers;
- atomic multi-record transactions for state transitions;
- role-based application permissions;
- logical holdout outcome sealing and independent-reviewer release;
- reserve lock and explicit release-trigger enforcement;
- content-addressed raw-file ingestion and byte re-verification;
- operational configuration supersession and dependent-gate invalidation;
- HMAC-SHA256 content-signature semantics for the prototype;
- export to the Round-48 provenance bundle;
- Round-48 semantic validation of the generated bundle;
- a complete synthetic G0-G8 traversal.

## Important security boundary

This is not a production LIMS or secure multi-user system.

The SQLite database can be read directly by an operating-system/database administrator. Application-level holdout sealing therefore does not equal cryptographic encryption or a hardened authorization boundary.

The synthetic HMAC mechanism proves only that a holder of the supplied key can bind an actor label, time, record ID and record digest. It does not establish trusted identity, independent time, protected private-key custody, nonrepudiation, 21 CFR Part 11 compliance, or any other regulatory status.

No secrets are stored in the repository.

## No physical promotion

The reference traversal uses only synthetic IDs and synthetic raw files. It does not establish:

- laboratory P16J readiness;
- P16I laboratory dry-run completion;
- HgCdTe process capability;
- first-build readiness;
- historical RP-01 reproduction;
- reproducible release.

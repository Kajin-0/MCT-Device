# MCT-Device digital provenance

**Round:** 48  
**Status:** machine-checkable repository control layer / synthetic validation only

This directory contains synthetic fixtures for the Round-48 provenance/state-machine architecture.

## Files

- `../schemas/mct_provenance_bundle.schema.json` — JSON Schema Draft 2020-12 structural contract.
- `../tools/validate_mct_provenance.py` — dependency-free semantic validator.
- `fixtures/valid/` — bundles that must validate.
- `fixtures/invalid/round48_invalid_cases.json` — named deliberately corrupted bundles that must be rejected.

## Validation

From the repository root:

```text
python tools/validate_mct_provenance.py --self-test
```

Validate a specific bundle:

```text
python tools/validate_mct_provenance.py path/to/bundle.json
```

Machine-readable output:

```text
python tools/validate_mct_provenance.py --json path/to/bundle.json
```

The GitHub Actions workflow `.github/workflows/provenance-validation.yml` runs the self-test automatically.

## Two validation layers

JSON Schema controls local record shape, required fields, enumerations and primitive types.

The Python validator controls cross-record invariants that JSON Schema cannot adequately express, including:

- globally unique record IDs;
- referential integrity;
- acyclic material genealogy;
- parent/root consistency;
- process-event input/output lineage;
- event chronology;
- configuration/calibration validity at use time;
- `GO` only when technical and material status both pass;
- locked reserve protection;
- holdout QC/outcome separation;
- model freeze before holdout outcome access;
- no protected holdout response in the training set;
- state-changing rework role reassignment;
- sequential evidence promotion.

## Material-state identity

A physical specimen may persist through several process steps. It therefore has:

- a stable `physical_object_id`; and
- a new immutable `material_node.id` for each scientifically distinct state.

Example:

```text
MAT-ROOT -> MAT-ANNEALED -> MAT-RIE -> MAT-DETECTOR
```

The physical object may be the same piece while the scientific state node changes. This prevents re-anneal, repeat RIE, re-passivation or package rework from silently overwriting prior provenance.

## Synthetic versus laboratory bundles

Round-48 repository fixtures use:

```text
mode = SYNTHETIC
```

and every record has `synthetic=true`.

A future laboratory system will use `mode=LAB` only after actual identifiers, configuration objects, calibration records, raw-data references, permissions and signatures are instantiated.

Synthetic validation is not physical commissioning, empirical HgCdTe evidence, first-build readiness or P17 release.

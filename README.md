# MCT-Device

A source-controlled effort to build an **Exhaustive Empirical Fabrication Protocol (EEFP)** for HgCdTe (MCT) infrared photodetectors, centered on a fully traceable research implementation of the Smith-Winchester-Musca-Dell-Faraone RP-01 photoconductor architecture.

## Objective

The target is not a generic literature review and not a document made to look complete by filling every blank with a number. Every consequential operation is classified by material state, apparatus geometry, thermal/chemical/electrical history, metrology, uncertainty, failure response and evidence provenance.

A process is not reproducible merely because every field contains a number. Values from different HgCdTe laboratories must not be combined as if they were one historical recipe.

## Reference architecture

RP-01 is anchored to:

E. P. G. Smith, K. J. Winchester, C. A. Musca, J. M. Dell, L. Faraone, “A simplified fabrication process for HgCdTe photoconductive detectors using CH4/H2 reactive-ion-etching-induced blocking contacts,” *Semiconductor Science and Technology* 16, 455-462 (2001), DOI `10.1088/0268-1242/16/6/306`.

The reconstructed route is:

`CdZnTe qualification -> surface preparation -> Te-rich horizontal-slider LPE -> FTIR/Hall -> Hg-rich anneal -> lithography -> wet mesa -> native oxide -> RIE blocking contacts -> Cr/Au -> TLM/LBIC -> singulation/package -> DC/responsivity/noise/dynamics`.

## Current maturity

- Released visual baseline body: **Round 61**, 74 pages.
- Current evidence/continuity layer: **Round 64**.
- `ROUND62-FULLTEXT-EVIDENCE-INTEGRATION = COMPLETE`.
- `ROUND63-TARGETED-LPE-CLOSURE = COMPLETE`.
- `ROUND64-SAME-LINEAGE-RIE-PASSIVATION-CLOSURE = COMPLETE`.
- `TRACEABLE-FIRST-BUILD-READY = NO` for an unspecified/uninstantiated laboratory.
- `HISTORICAL-RP01-REPRODUCED = NO`.
- `END-TO-END-EMPIRICALLY-VALIDATED = NO`.

The negative states are deliberate. The repository contains extensive executable procedures and qualification logic, but the composite process has not been executed end-to-end in one laboratory.

## Evidence vocabulary

- **RP** - direct Smith/RP-01 evidence.
- **SL** - same UWA/Faraone/Dell/Smith process-lineage primary evidence.
- **PT** - primary transfer evidence from another apparatus/laboratory or official source.
- **DER** - transparent derivation.
- **SYN** - explicit local implementation synthesized from evidence/physics.
- **OPEN** - consequential coordinate for which no defensible historical number is presently supported.

`OPEN` is a valid scientific state. A modern local experiment can establish local `SYN`; it cannot retroactively establish historical identity.

## Read first

1. `AGENTS.md`
2. `docs/RP01_SAME_LINEAGE_RIE_PASSIVATION_CLOSURE_ROUND64.md`
3. `research/2026-08-17_checkpoint_after_same_lineage_rie_passivation_round64.md`
4. `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND64.md`
5. `docs/SOURCE_LEDGER_ADDENDUM_ROUND64.md`
6. `procedures/P08H_UWA_RIE_LBIC_FULLTEXT_CLOSURE_ADDENDUM.md`
7. `procedures/P25B_PHOTOCONDUCTOR_PASSIVATION_SHUNT_NOISE_ADDENDUM.md`
8. `procedures/P03G_HONEYWELL_TECHNION_SLIDER_LPE_FULLTEXT_ADDENDUM.md`
9. `procedures/P26B_AU_HGCDTE_INTERFACE_CHEMISTRY_ADDENDUM.md`
10. Round-63, Round-62 and Round-61 controlled closure layers.
11. Round-57 metrology specifications and detailed procedures.

## Round-64 result

Round 64 integrates fifteen additional full papers. The largest scientific improvements are:

### Same-UWA RIE/LBIC

- a much more complete Plasma Technology reactor-state matrix from Smith/Musca/Dell/Faraone papers;
- the previously loose approximately 8-um electrical-conversion observation now tied to a specific Musca-1998 branch: H2 27 sccm, CH4 5 sccm, 430 mTorr, 0.4 W/cm2, 18 C cathode, approximately 200-V dc bias, 30 s, with only approximately 0.075-um physical recession;
- photoresist thickness/profile identified as a first-class electrical-conversion coordinate;
- multicarrier Hall/QMSA evidence separating a thin damaged surface layer from a deeper high-mobility converted region;
- explicit RIE-Hg-anneal reversibility in a 200 C / 17 h same-UWA branch;
- direct photoconductor evidence that extended mesa RIE can strongly degrade responsivity, lifetime, noise and D* even when cutoff and DC resistance appear similar;
- LBIC absolute depth recognized as calibration/model dependent.

Historical RP-01 self-bias, RF/electrode geometry, actual sample temperature and conversion depth remain OPEN.

### Passivation/noise

- Pal 1999 makes the accumulation tradeoff explicit: reduced surface recombination can increase lifetime while the same accumulation layer creates shunt conduction.
- Schoolar 1982 on x=.30 material demonstrates visible-light/field/time memory in anodic-oxide/interface charge.
- Bhan 2004 shows passivation-induced surface shunts can contribute to photoconductor noise and must be considered in detector-noise interpretation.

Passivation is therefore treated as a coupled state, not an oxide-thickness target alone.

### LPE

- Schmit/Hager/Wood 1982 strongly confirms the Honeywell atmospheric-pressure Te-rich horizontal-slider process family, including supercooled isothermal growth and the practical growth-time/thickness regime.
- Nemirovsky 1982 adds a semiclosed PT branch with explicit reservoir depletion, solution reuse and evidence that substrate state can change during equilibration before melt contact.

### Metallization

Davis 1984 demonstrates that Au deposition can alter HgCdTe surface stoichiometry and band bending. This strengthens P26 interface-state/vacuum/thermal/QCM controls without providing RP-01 Cr/Au deposition setpoints.

## Remaining documentary frontier

The highest-value unresolved items are now predominantly archival/apparatus-specific:

- exact RP-01/Fermionics LPE machine drawing and numerical dimension stack;
- exact RP-01 Plasma Technology model/run sheet, RF frequency, electrode dimensions/spacing, matching-network state, measured self-bias and sample temperature;
- exact electrical conversion depth/lateral spread for the direct RP-01 blocking-contact exposure;
- historical anodization electrode geometry;
- historical Cr/Au evaporator/QCM/source-to-sample geometry;
- original RP-01 cryostat/package/readout implementation.

Do not close these by analogy.

## Search disposition

Another broad literature sweep is not recommended. Highest-value future work is archival recovery or deliberate local qualification.

## Source-file provenance

Publisher PDFs are not redistributed in the repository. Exact reviewed byte identities are recorded in:

- `research/2026-08-17_round62_source_acquisition_sha256_manifest.md`
- `research/2026-08-17_round63_targeted_lpe_source_sha256_manifest.md`
- `research/2026-08-17_round64_source_sha256_manifest.md`

so future legally obtained copies can be verified against the exact sources used for evidence extraction.
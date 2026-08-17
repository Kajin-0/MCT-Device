# AGENTS.md — MCT-Device continuity record

**Current continuity round:** 62  
**Date:** 2026-08-17 America/New_York  
**Repository:** `Kajin-0/MCT-Device`

## Mission

Produce an **Exhaustive Empirical Fabrication Protocol (EEFP)** for HgCdTe photoconductor fabrication and characterization: a literature-derived scientific methods monograph with SOP-level experimental specificity, explicit metrology, failure response and evidence provenance.

The governing question is:

> What exactly does the researcher do, with what material, apparatus geometry, quantity, timing, physical state, measurement, calculation, endpoint, failure response, and retained raw data?

The project is not a claim that a composite process has already been reproduced in one laboratory. Do not make undocumented historical assignments merely to remove blanks.

Canonical downstream anchor:

E. P. G. Smith, K. J. Winchester, C. A. Musca, J. M. Dell, L. Faraone, “A simplified fabrication process for HgCdTe photoconductive detectors using CH4/H2 reactive-ion-etching-induced blocking contacts,” *Semiconductor Science and Technology* 16, 455–462 (2001), DOI `10.1088/0268-1242/16/6/306`.

## READ FIRST

1. `docs/RP01_FULLTEXT_SOURCE_ACQUISITION_ROUND62.md`
2. `research/2026-08-17_checkpoint_after_fulltext_source_acquisition_round62.md`
3. `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND62.md`
4. `docs/SOURCE_LEDGER_ADDENDUM_ROUND62.md`
5. Round-61 consequential-coordinate closure remains controlling where Round 62 did not revise it:
   - `docs/RP01_CONSEQUENTIAL_COORDINATE_CLOSURE_ROUND61.md`
   - `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND61.md`
   - `docs/SOURCE_LEDGER_ADDENDUM_ROUND61.md`
6. Round-57 metrology definitions remain controlling unless a later document intentionally supersedes them:
   - `docs/RP01_EMPIRICAL_PROTOCOL_METROLOGY_CLOSURE_ROUND57.md`
   - `procedures/P37_LBIC_BLOCKING_CONTACT_FUNCTIONAL_QUALIFICATION.md`
   - `analysis/ftir/ROUND57_FTIR_MODEL_SPECIFICATION.md`
7. Detailed P01–P37 procedures, travelers and calculations remain the technical execution corpus.

## Current publication / maturity state

- **Current typeset artifact:** Round 61, 74 pages.
- `RP01-EEFP-ROUND61-CONSEQUENTIAL-COORDINATE-CANDIDATE = YES`.
- `ROUND62-FULLTEXT-EVIDENCE-INTEGRATION = COMPLETE`.
- Round 62 is a controlled documentary layer, **not yet a new typeset EEFP PDF**.
- `TRACEABLE-FIRST-BUILD-READY = NO` for an unspecified/uninstantiated laboratory.
- `HISTORICAL-RP01-REPRODUCED = NO`.
- `END-TO-END-EMPIRICALLY-VALIDATED = NO`.

Do not call Round 62 a fabrication validation. No new physical HgCdTe experiment was performed.

## Evidence vocabulary

Use exactly:

- `RP` — direct Smith/RP-01 evidence.
- `SL` — same UWA/Faraone/Dell/Smith process-lineage primary evidence.
- `PT` — primary transfer evidence from an analogous process/apparatus or official technical source.
- `DER` — transparent derivation.
- `SYN` — explicit locally executable implementation synthesized from evidence/physics.
- `OPEN` — consequential coordinate for which no defensible numerical value is presently supported.

`OPEN` is a valid scientific state. A similar apparatus from another laboratory does not convert an RP-01 historical unknown to `RP`.

## Round-62 source-acquisition result

Nineteen primary papers were recovered in full text after Round 61. They materially strengthen six areas without closing the major historical apparatus unknowns.

### 1. LPE graphite, Hg compensation and slide-out

**Astles et al. 1992** provides a concrete HgCdTe-LPE transfer branch:

- POCO DFP-2 graphite;
- acid etched;
- boiling deionized-water cleaning for one week;
- 500 °C bake;
- scratch-free hand-polished slider/base/lid mating surfaces;
- shimmed slider-retaining rails;
- two distinct HgTe source paths;
- dummy-cycle gravimetric Hg-loss measurement, ~0.3 mg/min in that apparatus;
- ~460 °C / ~0.1 °C min^-1 growth branch;
- 250 °C / 48 h Hg-rich anneal example.

Important correction to Round 61: an acid graphite-cleaning method is no longer *unsupported*. It is now a valid `PT` qualification branch. It remains neither mandatory nor historical RP-01 identity.

**Chiang 1988 / Chen 1991** demonstrate independently heated Hg reservoirs connected through quartz two-arm covers. Consequence: `T_Hg(t)` and vapor-path topology are first-class thermochemical coordinates whenever that architecture is used. Source mass alone is insufficient.

**Radhakrishnan 2003** directly ties wipe clearance/non-smooth slide-out to slider scratches, transient meltback/re-growth texture and residual Te-rich melt. In that apparatus/composition branch, exposed layers held above ~350 °C after slide-out developed Hg-evaporation points, while excessively cool placement could yield HgTe soot. Preserve this as `PT`, not a universal temperature limit.

**Parker 1988** reinforces that holder/flow geometry, meltback, thermal gradients and growth rate affect terracing through hydrodynamic/supersaturation fields. Do not transfer its non-slider crucible dimensions.

### 2. CdZnTe substrate qualification

**Everson 1995** provides an executable `(111)B/(211)B` defect-screening branch:

`6 cm³ 48% HF + 24 cm³ HNO3 + 150 cm³ lactic acid`

for 2.5 min at room temperature with moderate agitation. Pits are approximately 10:1 width:depth and were validated against dislocations. Their `EPD <1×10^5 cm^-2` example is a transfer screening threshold, not an RP-01 purchase specification.

**Tobin 1995** requires separate treatment of room-temperature lattice mismatch and growth-temperature lattice mismatch. Crosshatch/EPD minima track matching, but the optimum room-temperature offset can shift because growth occurs hot.

**Tranchart 1985** directly supports `Cd0.96Zn0.04Te`-class material for `x≈0.30` HgCdTe LPE. Its `(111)A` face and 3-mm liquid depth are apparatus-specific PT data and must not be silently merged into the Round-61 `(111)B` branch.

**Bruder 1990** strengthens `(111)` orientation, XRD, EPD/topography and polishing metrology transfer.

### 3. Hg-rich low-temperature anneal

**Chandra, Schaake and Kinch 2003** materially strengthens the anneal model:

- annealed/converted skin depth approximately `∝ sqrt(t)`;
- `x_B²/t` is a useful diffusion-like response coordinate;
- rate depends strongly on starting metal-vacancy/excess-Te state, composition and temperature;
- x≈0.28 temperature-series activation energy ~1.1 eV.

Do not convert this into a universal 250 °C dwell. P31/P23 remain state-map problems.

### 4. Native anodic oxide

**Stahle/Helms 1989** supports `0.1 M KOH / 90% EG / 10% water / 0.3 mA cm^-2` and provides a two-region interface model, including a ~30–50-Å CdTeO3-rich inner region for an approximately 700-Å oxide.

**Nemirovsky/Kidron 1979** adds a consequential electrical detail: constant-current formation followed by constant-voltage completion. This strengthens Round-61's requirement to record `J(t), V(t), Q/A, d_ox` and makes termination mode a controlled coordinate.

**Ngoc/Nha 1998** provides a 0.2–0.5 mA/cm² branch, Pt counter-electrode alternative and 77-K C-V/interface metrics. Counter-electrode material is therefore not assumed from chemistry alone.

Historical anodization cell geometry remains `OPEN`.

### 5. Same-lineage RIE/LBIC

**Siliquini et al. 1997** is `SL` and now anchors a complete UWA physical state:

`H2 27 sccm / CH4 5 sccm / 410 mTorr / 0.4 W cm^-2 / cathode 18 °C / printed dc bias 180 V / 60 s`.

The branch produced only ~0.2 µm physical recession but ~1.5 µm electrical conversion depth.

LBIC implementation:

- 1.047-µm CW excitation;
- ~3-µm spot;
- 2.5-µm scan step;
- ~5-mm remote-contact spacing;
- sequential 0.1% Br2/methanol depth stripping;
- best-fit converted-region net doping near 1×10^15 cm^-3.

This strengthens P34's reactor-equivalence philosophy. It does **not** establish the self-bias of the RP-01 `100 mTorr / 50 W / 64 sccm / 60 s` condition.

Preserve P37's separate Musca-1998 80-K functional LBIC branch; do not merge the two experiments.

### 6. Package thermal response and contact noise

**Bartoli et al. 1976** directly fits bond-layer thermal conductance in HgCdTe photoconductor arrays. Example values:

- short-time epoxy path `k/d≈3.2 W cm^-2 K^-1`;
- long-time varnish path `k/d≈0.9 W cm^-2 K^-1`.

Use as a quantitative `PT` prior/extraction method for P33/P13. These are not Dow Corning 3110 or RP-01 constants.

**Beck et al. 1990** shows contact 1/f noise can remain a separate problem even when DC contact resistance is acceptable. P09/P12 should not infer low contact noise from low `rho_c` alone.

### 7. FTIR

**Gopal 1992** explicitly shows the 50%-transmission point depends on layer thickness for HgCdTe epilayers. This directly supports the Round-57 rule that scalar edge descriptors are not thickness-independent composition truth.

**Chang 2005** provides a full automatic spatial infrared-mapping implementation with self-consistent x/thickness fitting. Use as PT mapping/model evidence; do not replace the controlled LPE/Hougen forward model with its MBE-specific assumptions.

## Major historical OPEN coordinates after Round 62

Still `OPEN`:

- exact RP-01 LPE base/slider/cover/well/recess numerical dimension stack;
- x≈0.30 melt density/well area/melt depth relation;
- historical Hg-source exposed area/location/vapor volume;
- historical graphite grade/roughness/exact cleaning;
- x≈0.30 source-synthesis ampoule dimensions/free volume/hot pressure;
- historical wet-etch vessel/agitation/hydrodynamic state;
- historical anodization electrode spacing/area ratio/solution drop;
- RP-01 RIE model, RF frequency, powered/grounded areas, spacing, self-bias, sample temperature and chamber seasoning;
- historical Cr/Au evaporator source/QCM/sample geometry;
- original RP-01 package/readout/cryostat thermal implementation.

The correct response remains documentary recovery or local qualification, not invented historical values.

## Next documentary targets

Do **not** restart a broad literature sweep. Highest-value remaining targets are:

1. Suh et al. full slider-LPE precise-composition-control paper.
2. Shinohara et al. full Hg-loss compensation/wipe-off paper.
3. Honeywell/Fermionics/UWA machine drawings and notebooks.
4. TI anodization-cell drawings/lab records.
5. Historical UWA Plasma Technology run sheets/manuals.
6. Original RP-01 evaporator/QCM and cryostat/package records.

## Next publication step

Round 61 remains the current typeset review artifact. If a new PDF/TeX revision is generated, integrate only the deltas frozen in Round 62 and preserve the Round-57/61 metrology definitions unless new primary evidence directly requires a correction.
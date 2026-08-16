# P07B — CdZnTe face / polarity / miscut selection for x≈0.30 Te-rich LPE

**Status:** CONTROLLED LOCAL QUALIFICATION METHOD. Supplements P07/P07A and P03.

## 1. Purpose

Define how the CdZnTe growth face, A/B polarity, miscut magnitude and miscut azimuth shall be selected for the locally qualified x≈0.30 Te-rich horizontal-slider process when the exact RP-01/Honeywell historical substrate face is not publicly disclosed.

Do not replace the unknown with a generic statement such as “use (111)B” or “use (111)A.”

## 2. Historical/source state

RP-01 directly states only:

- HgCdTe grown by LPE;
- electrically insulating CdZnTe substrate.

The exact substrate:

- crystallographic plane;
- A/B polarity;
- offcut magnitude;
- offcut azimuth

are not stated.

The 1982/1983 Honeywell Te-rich horizontal-slider public abstracts identify large-area CdTe substrates but do not expose a face specification in the accessible text.

## 3. Relevant primary literature constraints

### Harman Te-rich horizontal slider

T. C. Harman's Te-rich LPE work reports that the highest-quality layers were obtained using `(111)`-oriented substrates, together with source wafers and supercooled growth solutions.

Use: strong support for testing the `{111}` family.

### Radhakrishnan/Sitharaman/Gupta horizontal slider

A later Te-rich horizontal-slider process used Cd0.96Zn0.04Te substrates nominally `(111)±0.5°` and produced detector-quality HgCdTe material.

Use: supports the practical relevance of a small-miscut `{111}` CdZnTe family.

Restriction: typical layer composition is x≈0.20 and the paper does not prove RP-01 polarity.

### Polarity/twinning literature

Independent HgTe/CdTe/HgCdTe growth literature shows that `(111)A` and `(111)B` can exhibit different twin densities and that the preferred polarity can depend on material composition and growth method.

Therefore orientation cannot be selected from a universal rule independent of the local LPE process.

## 4. Variables to qualify

At minimum define and record:

- nominal plane family;
- measured surface normal;
- A/B polarity;
- offcut magnitude;
- offcut azimuth;
- substrate Zn fraction/lattice parameter;
- substrate dislocation/inclusion state;
- final surface preparation;
- clean-to-load delay.

## 5. Initial face/miscut comparison

Where material availability allows, compare at least:

- `(111)A` near nominal;
- `(111)B` near nominal;
- one small controlled offcut on each polarity or on the better nominal polarity after the first screen.

The exact DOE must reflect supplier availability and actual metrology uncertainty.

A reasonable initial miscut scale for investigation is within the low-single-degree range because Te-rich LPE literature reports strong effects in this regime; this is a DOE range, not an RP-01 historical setpoint.

## 6. Keep all other growth variables matched

For a face/miscut experiment hold fixed as tightly as practical:

- substrate lot/quality class;
- final surface chemistry;
- source-preparation lot;
- xL/yL growth-liquid composition;
- total charge/melt geometry;
- Hg source condition;
- equilibration history;
- growth temperature/supercooling trajectory;
- substrate contact time;
- wipe-off sequence;
- post-growth Hg anneal.

Otherwise orientation effects cannot be separated from process drift.

## 7. Required outputs

For every face/miscut condition collect:

### Morphology

- whole-layer optical image;
- DIC/Nomarski map;
- terrace morphology;
- pinhole/void density;
- residual melt area;
- scratch/step features;
- surface roughness.

### Thickness/composition

Using P06:

- mean thickness;
- thickness uniformity;
- mean optical composition/edge;
- composition uniformity;
- edge exclusion behavior.

### Crystal quality

- HRXRD linewidth/rocking curve;
- twin/reflection features where measurable;
- EPD/dislocation metric;
- other structural characterization available to the lab.

### Electrical quality

After a matched P04 anneal:

- carrier sign;
- P05 Hall/multicarrier state;
- mobility;
- sheet resistance;
- spatial electrical uniformity if available.

### Lifetime/device proxy

Where material permits:

- P13 low-injection lifetime/decay proxy;
- or matched test-device responsivity/noise.

## 8. Selection objective

Do not choose the face solely by visual smoothness.

Define a multivariate orientation quality vector:

`Y_face = {morphology, thickness uniformity, x uniformity, twin/defect metric, mobility, lifetime, usable area}`.

The selected face/miscut should maximize detector-relevant material quality and run-to-run reproducibility.

## 9. Interaction with wetting and wipe-off

Face/miscut can alter step/terrace morphology and therefore potentially:

- growth-solution wetting;
- residual melt retention;
- wipe-off damage;
- lateral thickness profile.

Record wipe-off/residual-droplet behavior separately for each orientation during qualification.

## 10. Interaction with final surface preparation

A/B polarity and offcut can respond differently to Br2/methanol or other final surface treatments.

Therefore P07A final-surface qualification must be repeated or explicitly shown transferable when the selected face/polarity changes.

Do not assume one etch removal rate/morphology applies identically to A and B surfaces.

## 11. Interaction with lattice mismatch

The optimum Zn fraction depends on epilayer x and temperature; orientation does not replace lattice-match control.

For each substrate batch record measured lattice parameter/mismatch independently of face selection.

## 12. Release rule

The local substrate specification may be released only after one face/miscut window demonstrates:

- repeatable morphology;
- acceptable crystalline quality;
- acceptable thickness/x uniformity;
- acceptable post-anneal transport;
- no unacceptable yield penalty;
- reproducibility over multiple substrates/runs.

The final traveler must identify the selected plane, polarity, miscut magnitude and azimuth as **locally qualified** unless the historical RP-01 value is later recovered.

## 13. Historical closure status

Exact RP-01/Honeywell substrate face/miscut remains `OPEN`.

P07B provides the controlled local path to close that process variable experimentally without manufacturing historical precision.
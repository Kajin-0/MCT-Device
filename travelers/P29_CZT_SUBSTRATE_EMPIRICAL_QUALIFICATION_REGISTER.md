# P29 — CdZnTe substrate / final-surface empirical qualification register

**Status:** BLANK CONTROLLED TRAVELER  
**Use:** one record per substrate/coupon/lot entering P29 and linked P03 growth.

Do not substitute vendor labels for measured orientation/surface state where local metrology is available. Historical RP-01 fields remain `OPEN` unless directly sourced.

---

## A. Substrate identity / genealogy

- P29 run ID:
- date:
- operator:
- substrate/coupon ID:
- supplier:
- supplier lot:
- ingot/boule ID:
- ingot position if known:
- wafer/slice ID:
- date received:
- packaging/storage history:
- vendor designation (`epi-ready`, polished, etc.):
- certificate file/path:

---

## B. Composition / lattice state

- nominal Cd fraction:
- nominal Zn fraction:
- nominal Te stoichiometry:
- supplier composition method:
- independent composition method:
- measured Zn fraction:
- spatial positions measured:
- uncertainty:
- lattice parameter:
- measurement temperature:
- lattice-parameter uncertainty:
- intended HgCdTe x target:
- calculated/assessed lattice mismatch method:
- mismatch value and uncertainty:

Evidence class:

---

## C. Dimensions / flatness

- substrate length:
- width:
- thickness:
- thickness map:
- bow/warp/flatness:
- edge condition:
- chips/cracks:
- growth-side identification:

---

## D. Plane / polarity / miscut

- supplier nominal plane:
- supplier nominal polarity:
- supplier nominal miscut:
- supplier nominal azimuth:
- local orientation method:
- measured surface normal:
- local polarity-verification method:
- measured polarity:
- measured miscut magnitude:
- miscut uncertainty:
- measured miscut azimuth:
- azimuth uncertainty:
- reference sample/standard:
- permanent face/orientation mark applied? YES / NO
- orientation file/path:

Disposition: PASS / FAIL / CONDITIONAL

---

## E. Crystalline quality

### HRXRD

- instrument:
- reflection:
- scan geometry:
- FWHM center:
- FWHM spatial map/range:
- asymmetric/twin/subgrain features:
- raw data path:

### EPD / defect etch, if performed

- sacrificial? YES / NO
- etchant/recipe ID:
- face/polarity:
- count areas:
- total area:
- mean EPD:
- standard deviation/range:
- pit classification notes:
- microscopy path:

### Optical/DIC

- twin/subgrain evidence:
- cracks:
- polishing damage:
- other defects:

---

## F. IR inclusion / precipitate map

- instrument/wavelength band:
- inspected area:
- spatial resolution / minimum feature size:
- number of features:
- areal density:
- size distribution:
- largest feature:
- clustering/local hot spots:
- growth-area exclusion required? YES / NO
- map path:

---

## G. Trace impurities

- analytical method / certificate source:
- detection-limit document:

| Element | result | units | detection limit | sampling position | note |
|---|---:|---|---:|---|---|
| Cu | | | | | |
| Fe | | | | | |
| Ni | | | | | |
| Na | | | | | |
| other | | | | | |

- impurity anomaly? YES / NO
- P18/CAPA record if needed:

---

## H. Electrical isolation

- supplier electrical designation:
- supplier resistivity:
- measurement method:
- measurement temperature:
- electrode geometry:
- applied voltage/current range:
- measured resistivity/leakage:
- uncertainty:
- raw data path:
- disposition:

---

## I. Mechanical preparation genealogy

- slicing method:
- lapping sequence:
- lapping abrasives/grit:
- lapping removed depth:
- polishing method:
- polishing slurry/abrasive:
- pad:
- load/pressure:
- polish duration:
- polish removed depth:
- final vendor/local polish step:
- as-polished roughness:
- scratches/pits/edge damage map:
- unknown mechanical-history fields:

---

## J. Pre-final-clean surface state

- DIC image path:
- AFM RMS roughness:
- larger-scale roughness/waviness:
- particles/residue:
- XPS/EDS/surface chemistry if available:
- time since prior polish/clean:
- storage atmosphere:

---

## K. Final chemical surface recipe

Historical RP-01 recipe is `OPEN`. For local recipes define all concentrations mathematically.

- recipe ID:
- evidence class:
- solvent:
- solvent supplier/lot/grade:
- Br2 supplier/lot/grade:
- concentration basis (`w/w`, `v/v`, `w/v`, molar, other):
- Br2 amount:
- solvent amount:
- final volume/mass if relevant:
- solution preparation order:
- vessel material/ID:
- solution preparation timestamp:
- solution age at use:
- fresh/reused:
- prior substrate count/area:
- bath temperature before:
- bath temperature after:
- substrate face upward/downward/vertical:
- immersion start:
- immersion end:
- exposure duration:
- agitation method/cadence:
- observed bubbles/discoloration/abnormality:

---

## L. Rinse / dry

- first rinse solvent:
- first rinse start delay after etch:
- rinse duration/exchanges:
- DI water used? YES / NO
- additional rinse(s):
- final rinse:
- dry method:
- dry-complete timestamp:
- handling tools/material:
- visible residue after dry:

---

## M. Removed depth / final surface metrology

- protected-step or other removed-depth method:
- removed depth mean:
- removed depth range/std:
- measurement uncertainty:
- AFM RMS roughness:
- peak-to-valley/waviness:
- pit density/size:
- DIC/Nomarski result:
- XPS/chemistry result:
- Te enrichment/oxide/contamination observation:
- HRXRD change if measured:
- final-surface gate: PASS / FAIL / CONDITIONAL

---

## N. Clean-to-load clock

- `t_final_etch_end`:
- `t_final_rinse_end`:
- `t_dry_complete`:
- `t_boat_load`:
- `t_furnace_or_reactor_load`:
- `t_first_melt_contact`:

Derived:

- `Delta t_CTL = t_boat_load - t_final_etch_end`:
- `Delta t_surface_to_growth = t_first_melt_contact - t_final_etch_end`:

Environment by interval:

- final etch→rinse:
- rinse→dry:
- dry→boat load:
- boat load→furnace load:
- furnace load→melt contact:

Any accidental touch/exposure:

---

## O. P03 matched growth state

- P03 run ID:
- source/melt ID:
- source-use genealogy:
- liquid composition record:
- liquidus/equilibration record:
- actual supercooling:
- contact time:
- substrate face/polarity during growth:
- wipe-off method/result:
- post-growth anneal ID:

---

## P. Growth / wetting observations

- initial melt wetting observation:
- contact-angle measurement/proxy if available:
- incomplete wetting:
- residual melt/droplet count/area:
- wipe-off residue:
- wipe-off damage:
- nucleation anomaly:
- whole-wafer image path:

---

## Q. Epilayer morphology / structure

- DIC morphology:
- roughness:
- pits/craters/pinholes:
- usable-area fraction:
- HRXRD FWHM/shape:
- twin/subgrain features:
- epilayer EPD/TDD proxy:
- precipitate/inclusion map:

---

## R. P06 composition / thickness

- mean x / optical metric:
- x uniformity:
- mean thickness:
- thickness uniformity:
- edge-exclusion behavior:
- P06 data path:

---

## S. P05 electrical state

- test temperature(s):
- carrier state:
- Hall coefficient/field behavior:
- n/p where valid:
- mobility:
- sheet resistance/resistivity:
- spatial uniformity:
- P05 data path:

---

## T. Lifetime / detector correlation

- tau_eff/lifetime proxy:
- P13 data path:
- matched detector fabricated? YES / NO
- responsivity:
- noise/D*:
- detector yield:
- substrate-related performance concern:

---

## U. Failure classification / disposition

Check all applicable:

- [ ] orientation/polarity uncertainty
- [ ] miscut nonconforming to local class
- [ ] Zn/lattice anomaly
- [ ] high XRD width
- [ ] high EPD
- [ ] inclusion/precipitate anomaly
- [ ] impurity anomaly
- [ ] substrate leakage
- [ ] polish damage/residue
- [ ] final-etch pitting/waviness
- [ ] final-surface contamination/oxidation
- [ ] excessive clean-to-load delay
- [ ] poor wetting
- [ ] residual melt
- [ ] wipe-off damage
- [ ] epilayer structural defect
- [ ] electrical carrier/mobility anomaly
- [ ] other

- P18 record:
- root-cause status:

Final gates:

- incoming substrate: PASS / FAIL / CONDITIONAL
- final surface: PASS / FAIL / CONDITIONAL
- P03 interface/morphology: PASS / FAIL / CONDITIONAL
- epilayer structure/x/thickness: PASS / FAIL / CONDITIONAL
- electrical/device: PASS / FAIL / CONDITIONAL / NOT TESTED
- overall P29 disposition:
- approved for next qualification stage? YES / NO
- approver/date:

### Provenance statement

- direct RP-01 fields used:
- primary LPE transfer fields used:
- local qualification choices:
- fields still `OPEN`:

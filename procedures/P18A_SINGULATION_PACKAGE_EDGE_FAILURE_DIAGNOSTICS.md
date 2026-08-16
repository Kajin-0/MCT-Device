# P18A — singulation / die-edge / package-interaction failure diagnostics

**Status:** CONTROLLED DIAGNOSTIC ADDENDUM  
**Date:** 2026-08-16 America/New_York

Supplements `P18_FAILURE_ANALYSIS_DIAGNOSTIC_ATLAS.md` after creation of P35.

## 1. Purpose

Provide discriminating diagnostic paths when detector performance changes after singulation or when an apparently acceptable die fails during P33 cryogenic assembly/cycling.

Do not assign cause from visual edge appearance alone.

---

## S1. Visible edge chipping/cracking exceeds expectation

### Competing mechanisms

- excessive blade/wire force or feed;
- tool wear/dressing state;
- runout/wander;
- poor support/fixture;
- crystallographic cleavage interaction;
- pre-existing substrate crack/inclusion;
- entry/exit transient;
- laser taper/redeposition misread as mechanical chip.

### Discriminating tests

- compare chip map with cut direction and entry/exit edge;
- compare tool-age/dress/runout record;
- compare P29 plane/miscut orientation;
- inspect backside/frontside asymmetry;
- cross-section/destructive witness if needed;
- compare neighboring cuts from same tool state.

### Containment

Hold die from the affected tool/consumable state until mechanism is bounded.

---

## S2. Edge looks acceptable but detector resistance/I-V changes after singulation

### Competing mechanisms

1. hidden subsurface crack/damage reaching electrically active material;
2. edge/surface chemistry changed by coolant/slurry/clean;
3. protection/removal residue or ionic contamination;
4. contact/passivation damage away from the visible kerf;
5. electrostatic/handling damage;
6. actual change is fixture/contact-pair/loading artifact.

### Discriminating sequence

1. repeat P10 at identical contact pair/T/field/readout state;
2. inspect full die, not only edge, for pad/passivation damage;
3. compare residue/particle map and clean witness;
4. inspect edge/subsurface-damage witness from same tool state;
5. compare orientation/distance of active region to cut;
6. compare matched uncut or alternate-cut control.

### Key rule

`no visible chip != no electrically relevant singulation damage`.

---

## S3. 1/f or excess noise increases after singulation while DC resistance is nearly unchanged

### Competing mechanisms

- newly exposed/damaged edge surface introducing trapping/fluctuating conductance;
- passivation contamination by coolant/slurry/clean;
- microcrack-induced fluctuators/stress sensitivity;
- contact/pad contamination from protection removal;
- readout/source-impedance mismatch between pre/post tests;
- package/fixture microphonics if post measurement is already mounted.

### Discriminating sequence

- P12B electronics transfer at matched source impedance;
- noise versus active-edge distance/die orientation;
- perimeter/edge optical inspection and residue analysis;
- compare P12 spectrum before and after cleaning/remounting;
- mechanical perturbation/microphonic test;
- compare uncut control from same device region.

Do not attribute the increase to P02 interface traps until P35-specific hypotheses are tested.

---

## S4. Responsivity decreases after singulation

### Competing mechanisms

- functional edge damage increasing surface/contact recombination;
- crack/damage intersects active transport path;
- contamination or protection residue attenuates optical path;
- pad/contact damage changes actual field;
- package/fixture/FOV changed between measurements;
- self-heating/electrical state not matched.

### Discriminating sequence

- verify P10 contact voltage/field/current/T;
- verify P11 optical reference plane/FOV/beam overlap;
- map response versus position if possible;
- compare degradation versus distance to each cut edge;
- inspect P35 edge/subsurface records;
- compare noise and temporal response for recombination/trap signature.

---

## S5. Die survives room temperature but cracks during first cooldown

### Competing mechanisms

- singulation microcrack propagated under CTE stress;
- die-attach stiffness/void/bondline geometry;
- carrier CTE mismatch;
- wire/interconnect stress;
- pre-existing CdZnTe/HgCdTe defect/inclusion;
- cooldown rate/temperature gradient.

### Discriminating sequence

- locate crack origin relative to P35 cut edge/chip;
- compare bondline/void/tilt map;
- inspect P33 carrier/attach/cooldown genealogy;
- compare identical P35 die on alternate P33 package branch;
- compare alternate P35 edge state on same package branch;
- use sacrificial cross-section/fractography when justified.

### Interpretation

A crack originating at a cut edge does not prove P35 alone is causal; package stress can amplify a marginal P35 defect. Treat P35 × P33 as an interaction until discriminated.

---

## S6. Repeated thermal cycles produce progressive edge crack growth

### Competing mechanisms

- fatigue-like propagation from P35 damage;
- bondline hardening/shrinkage;
- carrier/package mismatch;
- wire/attach force path;
- moisture/outgassing/vacuum-history effects changing attachment state.

### Required records

- cycle number;
- warm/cold endpoints;
- ramp/dwell;
- crack length/map after selected cycles;
- P10/P12/P11 state after selected cycles;
- package thermal response and bondline condition.

Treat repeated measurements on one cycled die as a longitudinal genealogy, not independent replicates.

---

## S7. Laser-diced die has low chipping but altered edge chemistry/redeposition

### Competing mechanisms

- preferential II-VI ablation/stoichiometry change;
- redeposition/nodule formation;
- protection-film reaction;
- fluence/focus/overlap excursion;
- local thermal/photochemical damage.

### Discriminating tests

- compare near-edge chemistry/morphology with untreated control where capability exists;
- compare fluence/pass/overlap history;
- inspect redeposition directionality;
- measure detector response/noise versus edge distance;
- compare alternate laser state and abrasive control.

`non-contact` is not evidence of `no material modification`.

---

## S8. Wire-saw/blade branch leaves residue without obvious electrical failure

### Risk

A visually intact, currently functional die can still carry slurry/coolant/protection residue into P33 where vacuum bake, humidity or cooldown changes its electrical/mechanical effect.

### Discriminating tests

- qualified residue/particle inspection;
- controlled storage/aging check;
- compare pre/post P33 vacuum/bake state;
- witness surface chemistry where justified;
- P12 low-frequency noise before/after storage/package exposure.

Do not release solely from same-day room-temperature continuity.

---

## 2. Failure-code recommendation

For Round-34+ records use:

- `SING-MECH`
- `SING-SUBSURFACE`
- `SING-CHEM/RESIDUE`
- `SING-FUNCTIONAL`
- `SING-PKG-INTERACTION`
- `SING-MEAS-ARTIFACT`
- `SING-UNKNOWN`

Preserve `SING-UNKNOWN` when evidence is insufficient.

---

## 3. CAPA closure

A P35/P33 corrective action is closed only when:

1. the suspected process variable is changed intentionally;
2. the discriminating metric responds in the expected direction;
3. final detector electrical/noise/optical behavior is rechecked;
4. cryogenic survival is rechecked when relevant;
5. change-control/requalification scope is recorded under P17/P17A.

Improved edge appearance alone is not CAPA verification.
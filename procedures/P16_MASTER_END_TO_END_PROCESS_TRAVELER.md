# P16 — RP-01 master end-to-end process traveler

**Status:** CONTROLLED QUALIFICATION TRAVELER — NOT `REPRODUCIBLE-RELEASE`.

## 1. Purpose

Integrate P01–P15 into one auditable sequence from incoming CdZnTe substrate through a packaged, characterized HgCdTe photoconductor.

P16 does not replace the detailed procedure modules. It defines:

- process order;
- lot/sample genealogy;
- required witness structures;
- hold points;
- measurements that must exist before advancement;
- elapsed-time controls between sensitive steps;
- deviation/nonconformance handling;
- data package required to call one complete fabrication run traceable.

A run cannot be called “reproduced” merely because a functioning detector is obtained. It must satisfy the defined process-state and metrology gates.

---

## 2. Process-state codes

Use only the following traveler states:

- `NOT STARTED`
- `IN PROCESS`
- `HOLD — DATA REQUIRED`
- `HOLD — ENGINEERING REVIEW`
- `PASS`
- `PASS-CONDITIONAL` — only with documented rationale and disposition
- `FAIL`
- `SCRAPPED`
- `REWORK AUTHORIZED` — only under an approved rework instruction

Never convert `OPEN`, `CAL`, or `QUAL` variables in the procedure documents into arbitrary traveler setpoints.

---

## 3. Genealogy hierarchy

Every record must preserve this hierarchy:

`SOURCE LOT → LPE CHARGE → GROWTH RUN → EPILAYER/WAFER → COUPON/DIE → DEVICE → CONTACT PAIR → MEASUREMENT DATASET`

### 3.1 Required identifiers

Assign unique IDs for:

- `MAT-HG-####` mercury source lot;
- `MAT-CD-####` cadmium source lot;
- `MAT-TE-####` tellurium source lot;
- `SUB-CZT-####` CdZnTe substrate;
- `CHG-####` prepared growth charge;
- `LPE-YYYYMMDD-##` growth run;
- `WFR-####` resulting epitaxial wafer/sample;
- `COUP-####` material/process witness coupon;
- `DIE-####` singulated detector die;
- `DEV-####` individual device/string;
- `C1...C9` contact labels for the project nine-contact geometry;
- `DATA-####` measurement dataset.

The exact naming syntax may be adapted to the laboratory information system, but genealogy must remain one-to-one and reversible.

---

## 4. Required top-level traveler header

Record before work begins:

- traveler revision;
- RP-01 process revision;
- date opened;
- responsible researcher/operator;
- approved equipment set;
- facility/location;
- intended reference-device variant;
- target composition;
- target layer thickness;
- target post-anneal transport state;
- target operating temperature;
- planned device/contact geometry;
- applicable procedure revisions P01–P16;
- applicable source-ledger revision;
- known deviations approved before start.

---

# PHASE A — incoming materials and substrate

## STEP A0 — facility / calibration / safety readiness

**Procedure references:** all modules as applicable.

Before material handling verify/document:

- required facility authorization/EH&S controls active;
- balances calibrated;
- thermometry calibrated;
- gas-flow/MFC calibration current;
- pressure/vacuum gauges calibrated where used;
- lithography dose/spin/hotplate calibration current;
- Hall magnetic-field calibration current;
- FTIR wavelength/intensity checks current;
- RIE tool qualification current;
- metal-thickness/QCM calibration current;
- cryogenic thermometer calibration current;
- electrical/noise instrument calibration/current verification.

**Gate A0:** all critical calibrations/authorizations valid.

Status: ______  Date/time: ______  Operator: ______

---

## STEP A1 — elemental source receipt/lot record

Record for Hg/Cd/Te:

- supplier;
- lot;
- purity;
- CoA/impurity data;
- container state;
- storage history;
- opening date;
- mass inventory.

**Gate A1:** source materials meet current P03 qualification requirements.

---

## STEP A2 — CdZnTe substrate qualification

**Procedure:** `P07_CZT_SUBSTRATE_QUALIFICATION.md`

Record:

- substrate ID;
- dimensions/thickness;
- Zn/lattice parameter/mismatch metric;
- face/polarity;
- miscut magnitude/azimuth;
- HRXRD metric;
- EPD/dislocation metric;
- IR inclusion/precipitate map;
- trace-impurity data where available;
- resistivity/leakage;
- surface roughness/polish state;
- microscopy images.

**Gate A2:** P07 PASS or documented PASS-CONDITIONAL.

No LPE loading if substrate identity/polarity or surface condition is unresolved.

---

# PHASE B — charge preparation and LPE growth

## STEP B0 — growth-well / boat configuration record

**Procedure:** P03.

Record:

- graphite boat ID/revision;
- growth-well dimensions;
- calculated/verified melt volume/depth;
- substrate recess geometry;
- Hg-source geometry;
- cover configuration;
- wipe-off configuration;
- thermocouple/sensor positions;
- previous run/cleaning history.

**Gate B0:** apparatus configuration matches the qualified P03 branch.

---

## STEP B1 — charge calculation

Current composition-matched candidate tie line:

- `xL=0.082`;
- `yL=0.810`;
- derived mass fractions:
  - Hg `0.249738`;
  - Cd `0.012502`;
  - Te `0.737760`.

Total mass `M` must come from the locally qualified boat/melt-depth process; it remains apparatus-specific.

Record:

- target M;
- calculated target masses;
- balance ID;
- actual masses;
- actual normalized mole fractions;
- deviation from target xL/yL;
- propagated weighing uncertainty using the current charge-sensitivity calculation.

**Gate B1:** charge composition inside locally released tolerance.

Do not round Cd mass prematurely; Cd weighing dominates direct xL error in this tie-line formulation.

---

## STEP B2 — charge synthesis / homogenization

**Procedure:** P03.

Record complete:

- container/ampoule ID;
- loading sequence;
- evacuation/backfill conditions;
- temperature-time history;
- agitation/rocking history;
- cooldown;
- final visual state;
- recovered/available mass.

Current exact x≈0.30 synthesis schedule remains subject to qualification; do not silently insert Radhakrishnan's x≈0.20 synthesis as historical RP-01 fact.

**Gate B2:** qualified charge-preparation endpoint achieved.

---

## STEP B3 — substrate final pre-LPE surface preparation

**Procedures:** P07 + P03.

Record:

- final surface chemistry;
- concentrations;
- time;
- temperature;
- rinse/dry;
- microscopic surface state;
- completion timestamp;
- LPE-load timestamp.

Define:

`Δt_clean→load = t_load − t_clean_end`.

**Gate B3:** clean-to-load interval within qualified limit and surface free of visible contamination/damage.

Exact final CdZnTe surface chemistry remains a key release blocker until closed.

---

## STEP B4 — LPE atmosphere / thermal equilibration

**Procedure:** P03.

Record continuously where possible:

- N2 purge flow/time;
- residual O2/H2O if monitored;
- H2 flow;
- pressure;
- Hg source ID/mass/temperature;
- furnace-zone temperatures;
- growth-zone temperature;
- solution temperature;
- axial gradient;
- equilibration start/end;
- evidence/criterion used to declare equilibrium.

For the Bowers–Schmit xS≈0.29 candidate branch:

- `TL≈507 °C` is a published tie-line anchor;
- growth near 500 °C / derived ~7 °C supercooling is a qualification center point, not automatic release.

**Gate B4:** thermal/atmosphere state satisfies current qualified envelope.

---

## STEP B5 — growth initiation / run

Record:

- substrate-contact timestamp;
- actual contact/growth temperature;
- full temperature trajectory;
- slider position/state;
- growth duration;
- cooling trajectory during growth;
- abnormal events.

**Gate B5:** no process excursion outside approved qualification envelope.

---

## STEP B6 — growth termination / wipe-off

Record:

- separation/wipe timestamp;
- temperature;
- slider direction/speed where calibrated;
- wipe-off configuration;
- residual-melt observation;
- scratch/damage observation.

**Gate B6:** wafer safely separated; proceed to as-grown inspection.

---

# PHASE C — as-grown material state

## STEP C1 — as-grown visual/morphology inspection

Record:

- whole-surface image;
- residual melt droplets;
- pinholes/voids;
- terraces/scratches;
- cracks/delamination;
- usable-area map.

**Gate C1:** morphology inside current P03 criteria.

---

## STEP C2 — as-grown FTIR / composition / thickness map

**Procedure:** P06.

Record:

- map coordinates;
- raw spectra;
- edge metric;
- full-spectrum model version;
- inferred optical composition metric;
- thickness;
- within-wafer statistics.

**Gate C2:** composition/thickness suitable to enter anneal development.

Do not replace the optical map with a single center-point cutoff.

---

## STEP C3 — as-grown Hall / transport state

**Procedure:** P05.

Use dedicated material coupon or approved geometry.

Record:

- sample thickness;
- contact configuration;
- temperature;
- current;
- B grid;
- raw reversal data;
- VdP consistency;
- Hall sign;
- `n_H/p_H`;
- `µ_H`;
- magnetoresistance/linearity evidence;
- multicarrier escalation if required.

**Gate C3:** baseline electrical state established; not necessarily final n-type state.

---

# PHASE D — Hg-overpressure anneal

## STEP D1 — anneal setup

**Procedure:** P04.

Record:

- sample ID;
- Hg source/material;
- ampoule/reactor geometry;
- sample/source positions;
- pressure/chemical-potential control method;
- thermocouples;
- initial surface state.

---

## STEP D2 — anneal run

Record complete:

- ramp rate/history;
- sample temperature;
- Hg-source temperature;
- Hg pressure/chemical-potential proxy;
- soak time;
- cooldown path;
- vacuum/atmosphere.

Historical screening anchor `250 °C / 1 h` is not the RP-01 endpoint by itself.

---

## STEP D3 — post-anneal FTIR gate

Repeat P06 at the same coordinates where possible.

Compare:

- thickness;
- edge/composition metric;
- spectrum shape.

**Gate D3:** no unintended composition/thickness shift beyond qualified limit.

---

## STEP D4 — post-anneal Hall gate

Repeat P05.

Reference RP-01 material-state targets:

- n-type;
- historical supplier density `~9.8×10^14 cm^-3`;
- historical supplier mobility `~4.0×10^4 cm²/V·s`;
- historical supplier measurement temperature remains unknown.

Local production acceptance must specify measurement T and tolerance explicitly.

**Gate D4:** locally qualified final transport state reached.

If not, disposition = additional anneal development, reject, or documented rework; never repeatedly anneal without genealogy.

---

# PHASE E — frontside device fabrication

## STEP E1 — Mask-1 lithography

**Procedure:** P14.

Record:

- resist/lot;
- coating/spin data;
- thickness map;
- bake;
- mask ID/revision;
- exposure;
- developer;
- developed CD;
- alignment.

**Gate E1:** developed pattern inside qualified CD/profile window.

---

## STEP E2 — wet mesa isolation

**Procedure:** P01.

Record:

- etchant preparation and concentration basis;
- reagent lots;
- temperature;
- time;
- agitation;
- rinse/quench;
- depth;
- undercut;
- top/base CD;
- roughness/sidewall morphology.

**Gate E2:** complete electrical isolation with acceptable geometry/passivation-ready surface.

Current “2% Br2” concentration basis remains unresolved historically; no production run may use an undefined concentration convention.

---

## STEP E3 — anodic oxide passivation

**Procedure:** P02.

Record:

- electrolyte composition/basis;
- bath temperature;
- current density;
- voltage-versus-time trace;
- endpoint;
- time;
- rinse/dry;
- measured oxide thickness;
- witness/interface metrics.

Historical RP-01 target film thickness = `80 nm`.

**Gate E3:** oxide thickness/uniformity/electrical behavior inside qualified window.

---

## STEP E4 — Mask-2 lift-off/contact-window lithography

**Procedure:** P14.

Direct historical anchors:

- resist ~4–5 µm;
- prebake 80 °C / 30 min;
- chlorobenzene soak 30 min.

Record all locally qualified coating/exposure/development variables plus:

- thickness before/after soak;
- developed opening CD;
- lift-off-profile/overhang proxy;
- resist remaining height;
- alignment to Mask 1.

**Gate E4:** profile suitable for P08 RIE + P09 metal lift-off.

---

## STEP E5 — RIE contact-window / n+ formation

**Procedure:** P08.

Direct historical nominal anchors:

- total flow 64 sccm;
- printed gas notation `CH4/5H2`;
- 100 mTorr;
- 50 W;
- 60 s.

Record:

- exact individual gas flows from the released local recipe;
- MFC IDs/calibration;
- base pressure;
- chamber state;
- electrode configuration;
- RF frequency/power;
- self-bias where measured;
- sample temperature;
- process pressure;
- time;
- oxide-clear witness result;
- physical recession;
- n+ Hall/LBIC witness state;
- conversion/lateral extent where required.

**Gate E5:** RIE process outcome matches qualified electrical/contact-window state.

The historical individual CH4/H2 flows remain unresolved and must not be guessed.

---

## STEP E6 — RIE-to-metal transfer clock

Record:

- RIE plasma off time;
- chamber vent time if any;
- ambient exposure;
- metal-system load time;
- pumpdown start;
- Cr deposition start.

Compute:

`Δt_RIE→Cr`.

**Gate E6:** surface transfer inside qualified window.

---

## STEP E7 — Cr/Au deposition

**Procedure:** P09.

Historical thickness targets:

- Cr 30 nm;
- Au 270 nm.

Record:

- deposition method;
- tool ID;
- base pressure;
- deposition pressure;
- Cr rate/time/thickness;
- Au rate/time/thickness;
- QCM/witness calibration;
- substrate temperature;
- abnormal events.

**Gate E7:** metal thickness/process inside qualified window.

---

## STEP E8 — lift-off

Record:

- solvent/lot;
- temperature;
- time;
- agitation;
- rinse/dry;
- final optical inspection.

**Gate E8:** no bridges, fencing, flakes, delamination or contact damage.

---

## STEP E9 — final dimensional metrology

**Procedure:** P14.

For each device/contact pair record:

- final metal pad dimensions;
- actual gap;
- active width;
- mesa dimensions;
- alignment/clearances;
- device/contact-pair label.

These measured values, not CAD values, feed P10–P13.

---

## STEP E10 — TLM/contact QC

**Procedure:** P09.

For the nine-contact reference structure record:

- individual contact-pair resistance;
- gap;
- fit/regression;
- sheet/contact components;
- extracted `ρc`;
- temperature;
- I–V linearity/symmetry.

Historical benchmark: `ρc ~9×10^-4 Ω·cm² at 80 K`.

**Gate E10:** contact technology accepted for detector characterization.

---

# PHASE F — bare-die detector baseline

## STEP F1 — P10 DC field / self-heating baseline

Record:

- exact contact pair;
- actual gap;
- detector T;
- bias voltage;
- active-region voltage;
- field;
- current;
- power;
- I–V symmetry;
- thermal drift;
- sweepout behavior.

**Gate F1:** safe operating field envelope established.

---

## STEP F2 — optional pre-package optical/noise/dynamic baseline

Where the fixture permits, obtain selected:

- P11 responsivity;
- P12 noise;
- P13 temporal response.

This creates a pre/post package comparison for P15.

---

# PHASE G — singulation/package/interconnect

## STEP G1 — die separation

**Procedure:** P15.

Record singulation process/tool/settings, die dimensions and edge damage.

**Gate G1:** die mechanically/electrically intact.

---

## STEP G2 — die attach

Record:

- carrier/cold finger;
- attach material/lot;
- dispense/bondline;
- cure;
- placement/tilt;
- thermal history.

**Gate G2:** attachment visually/mechanically acceptable and within detector thermal budget.

---

## STEP G3 — wire bond/interconnect

Record full bonder construction/settings and bond map.

**Gate G3:** visual/electrical qualification passed; corresponding coupon pull-test process qualified.

---

## STEP G4 — aperture/window/shield / vacuum assembly

Record actual geometry/transmission and pump/bake history.

**Gate G4:** optical path and thermal/vacuum state fully defined.

---

## STEP G5 — cryogenic package qualification

Cool under measured thermal trajectory.

Repeat:

- P10 electrical baseline;
- selected P12 noise;
- selected P11 responsivity;
- P13 dynamic check where parasitics matter.

Perform prescribed thermal cycles and repeat critical metrics.

**Gate G5:** no unacceptable packaging-induced degradation.

---

# PHASE H — final detector characterization

## STEP H1 — absolute spectral responsivity

**Procedure:** P11.

Record complete traceable optical chain, detector geometry and same operating field/T/background used for comparison.

---

## STEP H2 — noise / NEP / D*

**Procedure:** P12.

Record:

- PSD/ASD normalization;
- electronics floor;
- frequency;
- ENBW;
- detector T/E/background;
- active area from P14;
- responsivity from the same frequency/state.

Use:

`D*(λ,f) = Rλ(f) sqrt(A) / e_n(f)`.

Do not substitute the historical 24.5-nV/√Hz g-r plateau into a 1-kHz D* calculation unless it is actually the noise at the signal frequency under the defined convention.

---

## STEP H3 — temporal response / bandwidth

**Procedure:** P13.

Record de-embedded amplitude/phase and time-domain response where available.

Determine whether the canonical 1-kHz P11/P12 measurement lies on the detector low-frequency plateau.

---

## STEP H4 — final report / release decision

Compile:

- full traveler;
- raw data locations;
- all deviations;
- source/material genealogy;
- calibration records;
- measurement uncertainty summaries;
- final performance table;
- failure/nonconformance history.

Final state options:

- `QUALIFICATION RUN — COMPLETE`
- `QUALIFICATION RUN — FAILED`
- `LOCAL PROCESS QUALIFIED`
- `REPRODUCIBLE-RELEASE` — **not permitted until every material process-critical OPEN variable is either source-closed or replaced by a statistically qualified local procedure with numerical acceptance criteria.**

---

# 5. Witness/coupon plan

A complete qualification run should reserve/process matched material for:

- Hall/VdP before anneal;
- Hall/VdP after anneal;
- FTIR/thickness map;
- passivation oxide thickness/interface witness;
- RIE oxide-clear/recession witness;
- RIE n+ Hall/LBIC witness;
- metal thickness witness;
- TLM structure;
- lift-off/profile witness;
- die-attach shear samples/coupons;
- wire-bond pull coupons;
- package thermal/noise qualification devices.

Do not consume the only detector die to learn a destructive-process parameter that could have been measured on a witness.

---

# 6. Elapsed-time variables to track

Surface and defect-sensitive processes require clocks. At minimum record:

- substrate final clean → LPE load;
- growth termination → first as-grown metrology;
- anneal end → electrical/optical metrology;
- mesa etch/rinse → passivation;
- anodization → Mask-2 coating;
- Mask-2 development → RIE;
- RIE → Cr deposition;
- Au deposition → lift-off;
- lift-off → first electrical test;
- singulation clean → die attach;
- die attach cure → wire bond;
- package pumpdown/bake → first cold test.

A future statistically qualified process may set maximum/minimum intervals for these clocks.

---

# 7. Deviation handling

Every deviation must record:

- affected sample IDs;
- intended setpoint;
- actual value/event;
- timestamp;
- suspected physical consequence;
- immediate disposition;
- required extra metrology;
- authorization for continue/rework/scrap.

Examples that require HOLD:

- unknown gas split;
- temperature excursion;
- uncalibrated balance/MFC/thermocouple;
- undefined reagent concentration basis;
- loss of contact-pair identity;
- missing active-area measurement before D* reporting;
- uncontrolled RIE-to-metal delay;
- package bake above qualified thermal budget.

---

# 8. Rework policy

Rework is allowed only when the specific rework physics and history are documented.

Potentially non-benign rework includes:

- repeat Hg anneal;
- repeat wet etch;
- stripping/regrowing passivation;
- repeat plasma exposure;
- metal strip/redeposit;
- repeated package bake;
- repeated wire bonding on the same pad.

Each may alter material/contact/interface state. Never relabel a reworked sample as if it followed the nominal sequence.

---

# 9. Minimum final data package

A completed qualification run must contain:

1. traveler with signatures/statuses;
2. raw source-material records;
3. exact charge calculations/actual masses;
4. full furnace/growth temperature traces;
5. gas/pressure/Hg-source records;
6. as-grown P05/P06 data;
7. anneal traces + post-anneal P05/P06;
8. lithography records/mask revisions/CD maps;
9. wet-etch preparation and geometry;
10. anodization trace/thickness;
11. RIE recipe + calibrated actual flows + witness data;
12. metal deposition traces/witness thickness;
13. TLM/raw I–V/regression;
14. actual device geometry/contact-pair mapping;
15. package traveler/thermal cycles;
16. absolute responsivity calibration files;
17. noise spectra/PSD processing;
18. P13 frequency/time response;
19. uncertainty and deviation reports;
20. final performance summary.

If any of these are unavailable, the run may still be scientifically useful but is not a complete reproducibility record.

---

# 10. Current master blockers to `REPRODUCIBLE-RELEASE`

Highest-impact unresolved variables remain:

### Material/growth

- exact selected x≈0.30 source-synthesis schedule;
- boat/well geometry and final total charge mass;
- exact substrate final surface preparation and selected face/miscut;
- exact equilibration/growth/cooling/thickness calibration;
- wipe-off mechanics;
- anneal chemical potential/time/cooldown for final transport target.

### Frontside fabrication

- P01 Br2 concentration basis and final rinse;
- exact P02 UWA anodization recipe or completed local transfer qualification;
- Mask-1/Mask-2 resist/exposure/developer recipes;
- exact CH4/H2 split corresponding to historical `CH4/5H2`;
- final RIE conversion-depth/lateral capability;
- metal base pressure/rates/RIE-to-metal interval;
- lift-off solvent/time.

### Geometry/package/measurement

- historical typical-device contact pair/gap;
- historical package/interconnect construction;
- final qualified package construction;
- historical preamp/ENBW convention for exact reproduction of the published D* curve;
- statistical numerical acceptance windows for material/device yield and performance.

P16 is therefore the **master qualification traveler**, not yet a claim that RP-01 can be reproduced from literature alone.

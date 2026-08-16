# Research checkpoint — after minimum laboratory capability specification Round 41

**Date:** 2026-08-16 America/New_York  
**Repository:** `Kajin-0/MCT-Device`

## 1. Round objective

Round 41 began from the Round-40 conclusion that the project is now largely branch-selected but not physically instantiated.

Objective:

> Convert the irreducible local identity/calibration groups into a procurement-neutral minimum laboratory capability envelope that a future facility can populate without confusing literature values, engineering margins and actual local measurements.

No vendor selection was performed. No new historical process identity was claimed. No physical measurement was invented.

---

## 2. New controlled artifacts

Created:

- `docs/FIRST_QUALIFICATION_BUILD_MINIMUM_LAB_CAPABILITY_SPEC.md`
- `travelers/P16C_MINIMUM_LAB_CAPABILITY_IMPLEMENTATION_REGISTER.md`
- `docs/SOURCE_LEDGER_ADDENDUM_ROUND41.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND41.md`
- this checkpoint.

AGENTS is refreshed at the end of the round.

---

## 3. New integration concept — P16C

P16C answers a third question distinct from P16A and P16B:

- **P16A:** is one no-tribal-knowledge build ready to execute?
- **P16B:** which evidence-ranked candidate process branch should be pursued?
- **P16C:** does a real laboratory have the required physical capability, calibration and commissioning infrastructure to instantiate that branch?

New label:

`P16C-INFRASTRUCTURE-READY`.

This is not a project maturity synonym.

Permanent relation:

`P16C-INFRASTRUCTURE-READY = YES`

may be necessary for a future build, but does not itself imply

`TRACEABLE-FIRST-BUILD-READY = YES`.

---

## 4. Capability classification system

Round 41 explicitly separates:

- `HARD-MINIMUM` — required by direct process state or measurement equation;
- `FIRST-BUILD-ENGINEERING-ENVELOPE` — useful range needed to qualify the branch;
- `DESIGN-CHECK` — derived sizing relation;
- `SURROGATE-COMMISSIONABLE` — can be verified without HgCdTe;
- `HGCDTE-REQUIRED` — cannot be closed honestly without HgCdTe/device material;
- `LOCAL-BLANK` — actual tool/geometry/calibration value still absent;
- `EH&S/FACILITY-GATE` — institutional authorization separate from scientific sufficiency.

This prevents a recurring failure mode: an engineering instrument range becoming misreported later as a historical process condition.

---

## 5. LPE capability result

The selected Honeywell-family LPE branch now has a minimum implementation architecture without inventing an absolute charge.

Hard anchors remain:

- `xL=.082`;
- `yL=.810`;
- `TL=507 °C`;
- above-local-liquidus equilibration;
- below-liquidus contact;
- N2 purge -> H2 process atmosphere;
- covered graphite horizontal-slider topology.

Round-41 first-build thermal coverage envelope:

approximately `495–520 °C`

around the process region so the future apparatus can resolve the 507 °C liquidus neighborhood, represented ~2–10 °C supercooling region and above-liquidus operation.

This is not a released T(t) trajectory.

Before HgCdTe is consumed, a future facility can commission:

- boat dimensions/capacity;
- hot slider motion;
- furnace thermal map;
- sensor/controller offsets;
- MFC/flow path;
- leak/pressure behavior.

Still HgCdTe-specific:

- actual hot meniscus/freeboard;
- `M_charge`;
- Hg transport/loss;
- local liquidus;
- growth/thickness/x response;
- wipe/contact trajectory.

---

## 6. Numerical-convention audit result

Round 41 found a real but very small documentation regression.

The authoritative controlled calculation

`calculations/LPE_CHARGE_COMPOSITION_SENSITIVITY.md`

freezes:

- `A_Hg=200.59 g/mol`;
- `A_Cd=112.414 g/mol`;
- `A_Te=127.60 g/mol`.

For `xL=.082`, `yL=.810`, this gives:

- `w_Hg=0.2497382358`;
- `w_Cd=0.01250164993`;
- `w_Te=0.7377601143`.

Later P30A/P16B/Round-40 integration text used approximately:

- `0.249740`;
- `0.012502`;
- `0.737758`;

which corresponds to using Hg atomic weight ~200.592 rather than the frozen 200.59.

Round-41 decision:

**the frozen calculation is authoritative.**

The difference is approximately ppm-scale and does not change any scientific conclusion or readiness state. Future charge arithmetic must use the frozen calculation values unless the atomic-weight convention is deliberately versioned and propagated.

---

## 7. Hg anneal capability result

The future anneal apparatus must not be specified as merely “250 °C furnace.”

Required state remains:

`{enclosure,Hg source,geometry,T_s(t),T_Hg(t),Hg boundary,dwell,cooldown}`.

First screen remains:

`~250 °C / ~1 h / Hg-saturated-isothermal-like`.

The apparatus should support low-temperature mapping through approximately 250–300 °C and must separately measure/log sample and reservoir/source temperatures even when nominally isothermal.

Thermal maps, sensor calibration, enclosure geometry and cooldown repeatability are surrogate-commissionable. Final carrier/optical state is HgCdTe-required.

---

## 8. Metrology capability results

### FTIR

Current P06 method becomes an implementation requirement:

- ~500–5000 cm^-1 coverage;
- <=4 cm^-1 qualification resolution unless sensitivity validates coarser;
- minimum 9-point map;
- preferred 5x5+ development map where geometry permits;
- independent physical thickness reference over expected ~5–15 µm.

These are local instrument requirements, not recovered historical RP-01 settings.

### Hall

Current P05 initial grid requires at least:

`+/-0.50 T`.

Therefore `>= +/-0.50 T` is the first hard magnetic-field implementation boundary.

Same-UWA converted-layer context extends toward ~2 T, so ~`+/-2 T` is preferred extended capability but not the initial hard minimum.

The station also requires ~80 K and 300 K operation plus current/field reversal and measured B at the sample.

---

## 9. Lithography / wet chemistry / anodization result

Mask-2 infrastructure must physically support the direct state:

- 4–5 µm resist;
- 80 °C / 30 min bake;
- chlorobenzene 30 min;
- measured exposure/development;
- survival through RIE;
- lift-off of 30 nm Cr + 270 nm Au.

Wet-mesa implementation cannot proceed until Br2 percentage basis, EG:HBr ratio basis and HBr stock assay are explicit local fields.

Anodization infrastructure must support the TI transfer center around:

- J ~0.3 mA/cm²;
- V formation neighborhood ~15 V;
- ~2-min first screen;
- ~80-nm oxide;
- continuous V(t).

Current is not preassigned:

`I=J A_exposed`.

---

## 10. RIE result

The future RIE must cover the direct controller center:

- 64 sccm total;
- 100 mTorr;
- 50 W;
- 60 s.

Candidate 1:5 split remains:

- CH4 10.6667 sccm;
- H2 53.3333 sccm.

But the actual reactor specification is now explicitly larger than those four controller values. Mandatory local observables include:

- actual gas flow calibration;
- process pressure trace;
- forward/reflected RF;
- self-bias or calibrated sheath proxy;
- sample/chuck thermal state;
- chamber clean/season genealogy;
- oxide-clear time;
- semiconductor exposure time.

No arbitrary base pressure is inserted.

---

## 11. Cr/Au result

Hard layer capability:

- Cr 30 nm;
- Au 270 nm.

Thermal evaporation remains the strongest candidate method family.

The future tool must provide:

- source/vacuum identity;
- pressure logging;
- separate Cr/Au QCM calibration unless equivalence is shown;
- witness thickness;
- rate trace;
- sample thermal proxy;
- RIE-to-Cr exposure clock;
- Cr-to-Au vacuum history.

A useful design equation is:

`u_t <= t b_t`

for an allocated fractional thickness uncertainty `b_t`.

No production `b_t` is released.

---

## 12. Integrated detector-station result

Round 41 freezes the architectural idea that P10/P11/P12/P13 are one matched-state station.

Shared state:

`{device,contact pair,geometry,package,T,E,I,P,background,FOV,window,load}`.

Minimum/reference capabilities include:

- detector near 80 K;
- canonical 10 V/cm;
- controlled exploration toward historical ~50 V/cm where heating/sweepout allow;
- absolute spectral point at 4 µm and coverage through/beyond ~4.4-µm edge;
- 1-kHz chopping state;
- noise coverage containing 100 Hz–10 kHz and the ~3-kHz knee;
- temporal transfer including 1 kHz, 10 kHz, 100 kHz and 1 MHz, with extension to >=5–10x measured f3dB when possible.

Two derived design checks were added without being made release criteria:

### Noise electronics floor

If electronics PSD is allocated fraction `beta` of the detector plateau PSD:

`e_elec <= 24.5 sqrt(beta) nV/sqrtHz`.

For example beta=0.10 -> ~7.75 nV/sqrtHz.

### 25-ns pulse resolution

If the same-UWA 25-ns transient branch is deliberately implemented, first-order rise-time sizing gives:

`BW ~ 0.35/25 ns ~ 14 MHz`.

This is source/instrument sizing, not RP-01 detector bandwidth.

---

## 13. Singulation / package result

No new tooling or material product is selected.

The future singulation system must support:

- ~1-cm-class brittle II–VI material;
- controlled low-force cutting;
- recorded tool/abrasive/feed/street state;
- edge and subsurface qualification;
- completed-stack-compatible protection/clean;
- pre/post detector-function comparison.

The future package/Dewar system must support:

- 77–80 K operation;
- compliant attachment screening;
- bondline measurement;
- interconnect qualification;
- measured optical geometry/transmission;
- vacuum/pump/bake/cooldown record;
- package thermal transient characterization;
- repeated thermal cycling.

---

## 14. What can be done without HgCdTe

Round 41 identifies a large amount of future commissioning that can precede expensive material:

- balances;
- LPE geometry/motion/thermal/gas calibration;
- anneal thermal/enclosure commissioning;
- FTIR/Hall instrument validation;
- spin/bake/dose/CD calibration;
- anodization electronics/cell area;
- RIE gas/pressure/RF/self-bias/thermal repeatability;
- evaporator QCM/witness/thermal calibration;
- detector-station electrical/optical/noise/temporal transfer functions;
- singulation mechanics;
- package vacuum/thermal/electrical infrastructure;
- genealogy/data system.

This is the central practical value of Round 41: future setup risk can be removed without pretending that surrogate commissioning proves HgCdTe process equivalence.

---

## 15. Readiness after Round 41

Unchanged:

- `TRACEABLE-FIRST-BUILD-READY = NO`
- `HISTORICAL-RP01-REPRODUCED = NO`
- `REPRODUCIBLE-RELEASE = NO`

No P16A row is promoted because no actual laboratory identity, calibration or HgCdTe qualification data have been supplied.

---

# 16. Strongest next action — Round 42

Proceed from broad capability envelopes to **subsystem acceptance-test specifications**, still procurement-neutral.

Highest-value sequence:

1. LPE furnace/boat/gas/actuator acceptance test specification;
2. Hg anneal furnace/ampoule/reservoir acceptance test specification;
3. integrated 80-K detector-station uncertainty and transfer-function budget;
4. RIE reactor/MFC/self-bias/oxide-clear acceptance specification;
5. Cr/Au QCM/vacuum/thermal acceptance specification.

For each subsystem, define:

- acceptance measurement;
- test artifact/surrogate;
- required raw data;
- calculation;
- pass/fail/conditional logic;
- what remains HgCdTe-only;
- recalibration/change-control triggers.

Do not select commercial vendors unless explicitly requested.

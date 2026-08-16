# RP-01 gap matrix addendum — Round 35: LPE absolute apparatus / charge closure

**Date:** 2026-08-16 America/New_York

Round 35 does **not** recover a literal Fermionics/Honeywell x≈0.30 growth traveler. It converts the principal LPE execution gap into a controlled apparatus-specific calibration path.

---

## 1. Gap status matrix

| Item | Current status | Strongest evidence | First-build effect | Required closure |
|---|---|---|---|---|
| Honeywell x≈.29 tie-line composition | `DIRECT-CLOSED` | US4317689A: xL=.082, yL=.810, TL=507°C, xS≈.29 | usable composition center | preserve as composition anchor |
| Honeywell covered horizontal-slider topology | `DIRECT-CLOSED-TOPOLOGY` | US4317689A/US4366771A | supports local architecture choice | no further source needed for topology |
| Honeywell growth-well numerical dimensions | `OPEN-HISTORICAL` | patent describes tapered wells/recesses but no recovered dimensions | local apparatus must be dimensioned | historical drawing or local P30A measurement |
| Honeywell substrate-recess numerical dimensions | `OPEN-HISTORICAL` | only qualitative size correspondence recovered | local apparatus must be dimensioned | historical drawing or local P30A measurement |
| Honeywell x≈.29 absolute growth charge | `OPEN-HISTORICAL` | no gram/mass value recovered | `EXECUTION-BLOCKER` until local `M_charge` selected | direct traveler or P30A capacity/inventory calibration |
| Honeywell auxiliary Hg/HgTe source mass | `OPEN-HISTORICAL` | ~0.1-atm vapor architecture, no universal mass | local source must be numerically defined | direct traveler or P30A independent source-inventory qualification |
| N2 purge flow/time | `OPEN-HISTORICAL` | direct sequence only | local branch required | explicit local gas/purge implementation |
| H2 flow/pressure | `OPEN-HISTORICAL` | direct flowing-H2 sequence only | local branch required | explicit local gas implementation |
| thermocouple type/location | `OPEN-HISTORICAL` | no exact x=.29 placement recovered | `LOCAL-IMPLEMENTATION-GATE` | calibrated local thermometry map |
| exact x≈.29 equilibration time | `OPEN-HISTORICAL` | Harman ~1 h branch is transfer only | local trajectory required | local liquidus/equilibration qualification |
| exact 9.5-µm contact time | `OPEN-HISTORICAL` | Honeywell ~30-min general example; Harman shorter branches | `EXECUTION-BLOCKER` until local trajectory frozen | P30A/P03B thickness-vs-trajectory calibration |
| exact cooling rate during growth | `OPEN-HISTORICAL` | multiple valid branches | local trajectory required | P30A numerical T(t) + P06 outcome |
| exact slide-out velocity | `OPEN-HISTORICAL` | qualitative smooth-motion requirement | local branch required | calibrated actuator/travel-time record |
| exact wipe-off generation for RP-01 material | `OPEN-HISTORICAL` | Honeywell CdTe-piece and scribed-apron branches | local branch required | choose one branch and qualify morphology |
| exact cooldown after separation | `OPEN-HISTORICAL` | no RP-01 traveler recovered | local branch required | numerical cooldown through unload-safe state |
| Radhakrishnan 4.8-g charge transfer | `PRIMARY-TRANSFER-CLOSED` | 15×15×1-mm CdZnTe, ~4.8 g/run | plausibility reference only | never area-scale into Honeywell mass |
| Radhakrishnan 3-g HgTe reservoir | `PRIMARY-TRANSFER-CLOSED` | same 2003 branch | separate-source plausibility reference | never universalize |
| Fermionics material provenance to UWA | `LINEAGE-CLOSED` | same-era UWA papers | supports supplier genealogy | does not close process traveler |
| Fermionics internal LPE process | `OPEN-HISTORICAL` | no recovered internal traveler | does not by itself block local substitution | direct archive/traveler if literal history desired |
| local boat dimensional metrology method | `METHOD-CLOSED` | P30A Round 35 | enables future execution closure | instantiate actual hardware |
| local absolute-charge selection method | `METHOD-CLOSED` | P30A Round 35 | enables future execution closure | numerical P30A inventory bracket + trial data |
| local trajectory/wipe/cooldown calibration method | `METHOD-CLOSED` | P30A + P30/P03B/P03E | enables future execution closure | numerical local branch + P06/P05 qualification |

---

## 2. P16A readiness consequences

Round 35 changes **closure capability**, not current physical readiness.

### R04 — LPE boat/well/source hardware

Remains:

`APPARATUS-NOT-SELECTED`.

P30A now defines exactly how to close it.

### R05 — absolute LPE charge

Remains:

`OPEN-CHOICE`.

The equations

`m_Hg = 0.249740 M_charge`

`m_Cd = 0.012502 M_charge`

`m_Te = 0.737758 M_charge`

are valid only after an apparatus-specific `M_charge` is selected.

### R06 — atmosphere

Remains:

`OPEN-CHOICE`.

Honeywell's N2-purge/H2-flow sequence is direct history, but flow, pressure, purity/monitoring and local acceptance are not instantiated.

### R07 — thermal/contact/wipe/cooldown

Remains:

`OPEN-CHOICE`.

A local branch must numerically define the complete trajectory and show P06/P05 outcome closure.

Therefore:

`TRACEABLE-FIRST-BUILD-READY = NO` remains unchanged.

---

## 3. Closed conceptual/methodological gaps

### 3.1 Absolute charge is now formally apparatus-specific

P30A permanently rejects the idea that a tie-line composition determines a charge mass.

### 3.2 Area scaling is explicitly prohibited

The project now records the rejected shortcut:

`M_new = M_reference × A_new/A_reference`

unless geometric similarity, melt depth, thermal field and Hg-loss/source-depletion equivalence are independently demonstrated.

### 3.3 Honeywell geometry has stronger provenance

The source record now distinguishes:

- direct apparatus topology;
- missing numerical apparatus dimensions.

This is more precise than treating the entire boat as simply “OPEN.”

### 3.4 Fermionics material and process provenance are separated

Fermionics-supplied UWA material is documented. Fermionics internal LPE settings remain unrecovered.

### 3.5 Harman 1980 and 1981 branches are separated

They are no longer treated as one undifferentiated historical process family.

---

## 4. Prohibited shortcuts added in Round 35

Do not:

- infer a Honeywell charge mass from xL/yL;
- infer a Honeywell charge mass from substrate area;
- scale the Radhakrishnan 4.8-g branch by area;
- use the Radhakrishnan 3-g HgTe reservoir as a Honeywell source mass;
- assume a 2×3-cm Honeywell substrate implies a particular solution inventory;
- infer melt depth from total charge without actual well geometry/density/wetting state;
- identify Fermionics material provenance with a recovered Fermionics process recipe;
- average Honeywell ~30-min, Harman 0.25–10-min and other trajectory branches into one growth time;
- call 500°C the actual substrate/solution temperature without local thermometry calibration;
- treat wipe-off hardware as a cosmetic accessory.

---

## 5. Round-35 closure artifacts

- `procedures/P30A_LPE_ABSOLUTE_CHARGE_APPARATUS_CALIBRATION_ADDENDUM.md`
- `travelers/P30A_LPE_ABSOLUTE_CHARGE_APPARATUS_CALIBRATION_REGISTER.md`
- updated `travelers/P16A_FIRST_BUILD_READINESS_REGISTER.md`
- `docs/SOURCE_LEDGER_ADDENDUM_ROUND35.md`

---

## 6. Highest-value historical recovery targets still open

1. dimensioned Honeywell/Fermionics graphite-boat drawing;
2. Fermionics production traveler for x≈.30 LPE/CdZnTe material;
3. charge-loading notebook or source-synthesis record with absolute grams;
4. Hg-source inventory/reuse record;
5. furnace/tube/thermocouple drawing;
6. x≈.30 thickness/contact-time run sheet around 9.5 µm;
7. slider/wipe-off hardware drawing tied to the RP-01 material lot.

These would improve historical identity but are no longer the only path to local execution because P30A defines a controlled substitution route.

---

## 7. Strongest next source-driven execution blocker

The next high-value item is P16A **R13 wet-mesa etchant preparation basis**, presently `UNDEFINED-BASIS`.

Unlike an apparatus-specific LPE charge, this may be closable through primary source recovery if the underlying Srivastav/thesis/process record defines:

- what `2% Br2` means;
- whether `3:1 EG:HBr` is volume, mass or another preparation basis;
- HBr stock assay;
- reagent addition order;
- bath temperature/volume/agitation;
- rinse/quench/dry.

Round 36 should prioritize the primary thesis/paper chain before defining a local substitute bath.
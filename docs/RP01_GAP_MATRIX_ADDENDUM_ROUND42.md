# RP-01 gap matrix addendum — Round 42 subsystem acceptance / commissioning

**Date:** 2026-08-16 America/New_York  
**Repository:** `Kajin-0/MCT-Device`

## Scope

Round 42 does not close historical RP-01 identity gaps. It converts the Round-41 laboratory-capability gaps into explicit **acceptance evidence gaps**.

The principal new question is:

> What must be measured on the actual future laboratory infrastructure before that infrastructure can be trusted to support HgCdTe qualification?

---

# 1. New gap class

Add:

`ACCEPTANCE-EVIDENCE-OPEN` — the required acceptance method is now controlled, but no actual tool data exist.

This is distinct from:

- `HISTORICAL-IDENTITY-ONLY`;
- `EXECUTION-BLOCKER`;
- `LOCAL-IMPLEMENTATION-GATE`;
- `RELEASE-BLOCKER`.

A row may carry more than one class.

---

# 2. LPE

## Previously known

- Honeywell-family topology selected;
- tie line `xL=.082`, `yL=.810`, `TL=507 °C`;
- total charge mass, boat dimensions, local thermal field, gas flows and growth trajectory local/open.

## Round-42 acceptance gap

`ACCEPTANCE-EVIDENCE-OPEN` for:

- dimensioned boat/capacity;
- hot slider motion;
- source/substrate thermal map;
- N2/H2 flow calibration;
- synchronized sequence logging;
- local liquidus/growth-response residual qualification.

P36 now defines how these are tested.

**Readiness impact:** no P16A R04–R07 state change until actual results exist.

---

# 3. Hg anneal

`ACCEPTANCE-EVIDENCE-OPEN` for:

- dimensioned enclosure/fixture;
- `T_s(t)` / `T_Hg(t)` calibration;
- 250–300 °C map;
- one-hour dummy dwell stability/timing;
- enclosure integrity;
- actual Hg/HgCdTe carrier-state residual qualification.

P36 closes the method, not the physical result.

---

# 4. FTIR

`ACCEPTANCE-EVIDENCE-OPEN` for:

- 500–5000 cm^-1 calibrated coverage;
- <=4 cm^-1 qualification resolution;
- photometric repeatability/baseline;
- map registration;
- independent thickness-reference chain;
- actual HgCdTe optical-model qualification.

---

# 5. Hall/VdP

`ACCEPTANCE-EVIDENCE-OPEN` for:

- measured B at sample through ±0.50 T initial grid;
- reversal symmetry/remanence/uniformity;
- current/voltage/switching chain;
- ~80 K / 300 K temperature chain;
- Hall-reference surrogate result;
- HgCdTe multi-carrier/contact state.

---

# 6. Source mass metrology

The calculation method is closed, but physical balance capability remains `ACCEPTANCE-EVIDENCE-OPEN` at the actual selected element masses, especially Cd.

No arbitrary balance tolerance is assigned. Acceptance shall propagate observed mass uncertainty into `u(xL)` and `u(yL)`.

---

# 7. Dimensional / film metrology

`ACCEPTANCE-EVIDENCE-OPEN` across:

- 50–400-µm contact gaps;
- ~300-µm contact geometry;
- 4–5-µm resist;
- ~9.5-µm HgCdTe/mesa scale;
- ~80-nm oxide;
- 30/270-nm metal;
- singulation kerf/edge metrics.

This is a cross-cutting local implementation gate because field, area, thickness, oxide and metal claims depend on it.

---

# 8. Lithography

Historical Mask-1/Mask-2 product identity remains open.

New `ACCEPTANCE-EVIDENCE-OPEN` items:

- spin-thickness transfer;
- actual substrate bake thermal state;
- chlorobenzene timing/bath implementation;
- exposure-dose calibration;
- developer/profile response;
- RIE survival / 300-nm-stack lift-off surrogate challenge;
- actual HgCdTe/oxide compatibility.

No P16A lithography row changes.

---

# 9. Wet mesa

Historical chemistry-basis ambiguity remains unresolved.

Round-42 now makes the following a hard pre-execution acceptance gap:

- Br2 percentage basis must be explicit;
- EG:HBr ratio basis must be explicit;
- HBr stock assay must be explicit;
- preparation/timing/temperature/rinse must be measurable.

Actual HgCdTe etch rate/anisotropy/morphology remain `HGCDTE-REQUIRED`.

---

# 10. Anodization

Historical 90:10 solvent-ratio basis remains open.

`ACCEPTANCE-EVIDENCE-OPEN` for:

- local solvent basis definition;
- cell geometry;
- measured `A_exposed`;
- constant-current calibration;
- voltage compliance/logger;
- timebase;
- actual HgCdTe V(t)/oxide/interface response.

No fixed current may be released before area is measured.

---

# 11. RIE

The controller-center coordinates are documentary closed enough for a candidate branch, but reactor equivalence is not.

`ACCEPTANCE-EVIDENCE-OPEN` for:

- CH4/H2 gas-specific MFC calibration around 10.6667/53.3333 sccm;
- 64-sccm total verification;
- 100-mTorr process-pressure calibration;
- forward/reflected RF state;
- self-bias/sheath proxy;
- sample thermal state;
- chamber-state repeatability;
- actual oxide `t_clear`;
- actual HgCdTe electrical conversion/blocking response.

No arbitrary base-pressure number is added.

---

# 12. Cr/Au deposition

`ACCEPTANCE-EVIDENCE-OPEN` for:

- Cr QCM/witness correlation around 30 nm;
- Au QCM/witness correlation around 270 nm;
- separate tooling factors unless equivalence proven;
- pressure trace;
- source/sample/QCM geometry;
- sample thermal state;
- sequential Cr->Au implementation;
- actual RIE->Cr handoff;
- HgCdTe TLM/contact behavior.

---

# 13. Integrated detector station

Round 42 identifies a large acceptance gap even before HgCdTe is measured.

`ACCEPTANCE-EVIDENCE-OPEN` for:

- calibrated 77–80 K detector-temperature state;
- DC/load network terminal transfer;
- MWIR wavelength/radiometry/view-factor chain;
- 1-kHz modulation/timebase;
- electronics PSD/ASD floor;
- FFT/window/ENBW normalization;
- Johnson-noise absolute validation;
- source/electrical/reference temporal transfer through at least 1 MHz;
- package thermal kernel;
- matched-state metadata integrity.

HgCdTe P10–P13 performance remains a separate residual gate.

---

# 14. Singulation

`ACCEPTANCE-EVIDENCE-OPEN` for:

- mechanical cut repeatability;
- kerf/wander/edge metrics;
- support/protection compatibility;
- clean/release compatibility;
- actual CdZnTe/HgCdTe subsurface and functional damage.

---

# 15. Package / Dewar

`ACCEPTANCE-EVIDENCE-OPEN` for:

- bondline geometry;
- dummy package thermal kernel;
- interconnect resistance/mechanical integrity;
- measured optical geometry/transmission;
- vacuum/bake/cooldown trajectory;
- repeated thermal-cycle behavior;
- actual completed-detector residual performance.

---

# 16. Critical handoff timing

Round 42 adds an explicit cross-module acceptance gap:

`ACCEPTANCE-EVIDENCE-OPEN` for synchronized/reconstructable elapsed time and ambient state across:

- final CZT surface -> LPE;
- mesa -> anodization;
- anodization -> Mask-2;
- RIE -> Cr;
- Cr -> Au;
- singulation -> package;
- package -> P10–P13.

This is important because surface and package states can evolve even when each isolated process tool is nominally qualified.

---

# 17. Readiness disposition after Round 42

No physical acceptance run was performed.

Therefore:

- `P16D-SURROGATE-COMMISSIONING-COMPLETE = NO / NOT PHYSICALLY INSTANTIATED`;
- `P16C-INFRASTRUCTURE-READY = NO / NOT PHYSICALLY INSTANTIATED`;
- `TRACEABLE-FIRST-BUILD-READY = NO`;
- `HISTORICAL-RP01-REPRODUCED = NO`;
- `REPRODUCIBLE-RELEASE = NO`.

Round 42 materially improves future executability by converting the generic phrase “calibrate the tool” into subsystem-specific evidence requirements, while preserving every unresolved historical and local physical quantity.
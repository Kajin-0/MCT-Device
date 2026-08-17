# RP-01 gap-matrix addendum — Round 61

**Date:** 2026-08-17 America/New_York

## Round-61 principle

A consequential coordinate is acceptable only when it is explicitly classified as `RP`, `SL`, `PT`, `DER`, `SYN`, or `OPEN`.

`OPEN` is now a formal documentation state. It means the parameter matters, no responsible hard number is currently supported, and the closure route is stated.

## G61-01 — source ampoule over-specification

**Round-60 issue:** development dimensions/free volume were useful for physical prototyping but insufficiently supported to be carried as the canonical synthesis vessel.

**Round-61 action:** demote tube ID/OD/wall, free volume, charge/free-volume ratio, seal geometry, support/orientation and hot internal pressure to `OPEN`.

**Closure:** pressure/thermal-stress engineering + dimensioned professional quartz revision + blank thermal qualification + loaded-source qualification.

State: `FALSE-COMPLETENESS-REMOVED`.

## G61-02 — LPE numerical apparatus geometry over-specified

**Round-60 issue:** recess/well/slider/Hg-cavity/moat prototype dimensions were SYN-L but visually risked being read as a canonical apparatus.

**Round-61 action:** preserve primary topology and hard transferred dimensions only; demote unrecovered numerical dimension stack to `OPEN`.

**Closure:** patent-figure CAD reconstruction, CMM/profilometry, dummy slide/wipe mechanics, thermal map.

State: `LPE-DIMENSION-STACK-OPEN-EXPLICIT`.

## G61-03 — LPE charge mass treated too independently from geometry

**Problem:** 4.8-g solution charge and 3-g HgTe reservoir come from a specific modified-slider geometry and cannot be universalized independently of well/source/vapor geometry.

**Action:** preserve as PT geometry-coupled values. Introduce:

`h_melt(T)=m_melt/[rho_melt(T) A_well]`

and

`Psi_Hg=A_Hg-source/V_enclosed`.

State: `GEOMETRY-COUPLING-EXPLICIT`.

## G61-04 — graphite material/cleaning incompletely specified

**Action:** define present-day procurement family as purified semiconductor-grade graphite, ~1–5-µm characteristic particle scale, no metallic impregnation, lot-specific contamination certificate.

Historical grade/roughness/machining/clean remain `OPEN`.

Do not insert unsupported acid cleaning.

State: `PROCUREMENT-CLOSED / SURFACE-PROCESS-OPEN`.

## G61-05 — controller temperature not equal to LPE growth-interface temperature

**Action:** require 3–5-sensor instrumented dummy-boat thermal map and three complete thermal cycles; provisional local mapping target ~±1 °C in active growth region.

State: `THERMAL-MAPPING-REQUIRED`.

## G61-06 — wet-etch hydrodynamics hidden

**Action:** expand state to bath age, volume/exposed area, vessel geometry, liquid height, agitation and quench latency. Add `Gamma_bath=V_etchant/A_exposed`.

State: `MASS-TRANSFER-STATE-EXPLICIT`.

## G61-07 — anodization treated primarily as time endpoint

**Action:** make `J(t)`, `V(t)`, `Q/A`, and `d_ox` explicit. Derived center `Q/A=0.036 C/cm²`. Cell geometry/electrolyte resistance remain part of the voltage interpretation.

State: `ELECTROCHEMICAL-TRAJECTORY-EXPLICIT`.

## G61-08 — RIE physical reactor state insufficiently formal

**Action:** define dynamic plasma vector and static geometry vector; require three nominal instrumented witness runs before DOE on a new reactor.

Initial SYN apparatus screens: reflected/forward power <5%, `CV(Vdc)<5%`, specimen T <40 °C, mean pressure within ~±2% target.

State: `REACTOR-STATE-EXPLICIT`.

## G61-09 — Cr/Au geometry over-generalized

**Action:** remove universal source-distance/rotation setting; preserve actual source/QCM/shutter/substrate geometry as apparatus coordinates. Add PT QCM Z-ratios 0.305 Cr and 0.381 Au and rate/pressure-conditioned shutter opening.

State: `PVD-GEOMETRY-LOCAL / QCM-TRANSFER-STRENGTHENED`.

## G61-10 — cryogenic measurement start tied too strongly to elapsed time

**Action:** distinguish package cooldown qualification from measurement equilibrium. Provisional stationarity screen: temperature SD <=0.05 K and resistance drift <0.2% over 10 min.

State: `THERMAL-ELECTRICAL-EQUILIBRIUM-DEFINED`.

## Remaining highest-priority OPEN coordinates

- LPE full numerical dimension stack;
- LPE melt density/well area/melt depth;
- LPE recess flushness after local mechanics;
- Hg-source exposed area/location/vapor geometry;
- historical graphite grade/finish/clean;
- source-synthesis vessel geometry and hot pressure;
- wet-etch hydrodynamic/vessel equivalence;
- anodization electrode geometry/solution drop;
- RIE historical self-bias/electrode/chamber state;
- RIE chamber seasoning/history;
- exact historical evaporation tool/source/QCM geometry;
- original cryostat/package/readout soak conditions.

The correct response is documentary recovery or deliberate local measurement, not invented historical values.
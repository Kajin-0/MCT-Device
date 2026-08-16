# RP-01 gap matrix addendum — Round 41 laboratory capability boundary

**Date:** 2026-08-16 America/New_York  
**Repository:** `Kajin-0/MCT-Device`

## Purpose

Convert the Round-40 irreducible local identity/calibration groups into implementation gaps with explicit closure evidence.

This round does **not** change P16A row states. It changes the question from:

`what number is missing from literature?`

to:

`what physical laboratory capability must exist before the number can be measured or frozen?`

---

# 1. Capability-gap matrix

| Group | Current documentary state | Required physical implementation | Can surrogate-close? | HgCdTe required? | P16A rows |
|---|---|---|---|---|---|
| source weighing | composition equation closed; absolute mass open | calibrated balance at actual component masses | largely | final allocation | R01/R05 |
| substrate identity | preferred (111)B/4% Zn family selected | actual lot + crystallographic/material metrology | partial | final growth correlation | R02/R03 |
| LPE hardware | topology selected | dimensioned boat/furnace/tube/actuator | yes, geometry/thermal/motion | yes, growth behavior | R04–R07 |
| LPE gas | N2->H2 family selected | gas trains/MFCs/purity/flow state | yes | final growth correlation | R06 |
| LPE thermal trajectory | 507 °C tie-line + transfer ranges | calibrated process-position thermometry/liquidus/contact/wipe | partial | yes | R07 |
| FTIR | method architecture defined | actual calibrated FTIR/map/thickness chain | yes, instrument | yes, model/material | R08 |
| Hall | method architecture defined | actual magnet/cryostat/current/voltage/field chain | yes, instrument | yes, transport validity | R09 |
| Hg anneal | 250 °C/1 h first screen selected | actual ampoule/reservoir/Ts/THg system | yes, thermal/enclosure | yes, final state | R10/R11 |
| Mask-1 | process family only | current resist/coater/bake/exposure/developer/strip | largely | yes, chemistry/surface | R12 |
| wet mesa | response center selected; basis open | explicit Br2/EG/HBr recipe + bath/profile metrology | partial | yes | R13/R14 |
| anodization | TI center selected | explicit solvent basis/cell/area/current/V(t) | largely | yes, interface | R15 |
| Mask-2 | direct functional state strong | actual resist/exposure/developer/lift-off branch | largely | yes, RIE/device compatibility | R16 |
| RIE gas | 1:5 candidate + 64 sccm direct | calibrated CH4/H2 MFC realization | yes | yes, conversion | R17 |
| RIE reactor | controller center direct | actual reactor/self-bias/thermal/chamber/t_clear | partial | yes | R18 |
| TLM/CD | method defined | calibrated dimensions/cryogenic electrical fixture | yes, instrument | yes, contacts | R19/R22/R23 |
| Cr/Au deposition | stack direct, thermal evaporation candidate | actual vacuum/source/QCM/rate/thermal chain | yes, apparatus | yes, interface | R20 |
| detector station | reference state defined | integrated 80-K DC/radiometry/noise/temporal chain | largely | yes, detector outputs | R24–R27 |
| singulation | low-force family selected | actual tool/protection/clean/street/inspection | partial | yes | R28/R29 |
| package | compliant attach family selected | actual carrier/adhesive/interconnect/optics/vacuum | partial | yes | R30–R33 |
| survival/capability | cannot pre-exist | repeated thermal/process/yield evidence | no | yes | R34/R36 |

---

# 2. New P16C infrastructure gate

Round 41 introduces:

`P16C-INFRASTRUCTURE-READY`.

This is a precondition describing whether the necessary physical tools/stations exist and are calibrated enough to begin the remaining HgCdTe-specific qualification.

It is **not** equivalent to P16A first-build readiness.

Logical relation:

`P16C-INFRASTRUCTURE-READY = YES`

is generally necessary but not sufficient for

`TRACEABLE-FIRST-BUILD-READY = YES`.

A laboratory may have excellent instruments yet still lack frozen local process choices.

---

# 3. Minimum quantitative capability boundaries now explicit

Round 41 makes the following implementation boundaries explicit without promoting them to historical RP-01 settings.

## LPE

- calibrated process-region coverage around ~`495–520 °C` as a first-build engineering envelope around the 507 °C liquidus and represented 2–10 °C supercooling region;
- actual charge mass remains unresolved until boat capacity/meniscus geometry exists.

## FTIR

- ~`500–5000 cm^-1` coverage;
- `<=4 cm^-1` qualification resolution unless sensitivity validates coarser;
- minimum 9-point mapping;
- physical thickness reference over expected ~5–15 µm.

## Hall

- HARD-MINIMUM field capability through at least `+/-0.50 T` to execute current P05 grid;
- ~`+/-2 T` preferred extended capability;
- ~80 K and 300 K states.

## RIE

- direct 64 sccm / 100 mTorr / 50 W / 60 s controller center;
- candidate 1:5 split -> 10.6667/53.3333 sccm;
- self-bias/sheath, reflected power, sample thermal state, chamber genealogy and oxide clear are mandatory local observables.

## Cr/Au

- 30/270-nm layer capability;
- independent QCM/witness calibration;
- no arbitrary base-pressure spec.

## Detector station

- ~80 K / 10 V/cm canonical state;
- 4-µm absolute point and through/beyond ~4.4-µm edge;
- 1-kHz modulation state;
- noise coverage including historical 100-Hz–10-kHz band and ~3-kHz knee;
- temporal chain through 1 MHz and beyond observed f3dB as practical.

---

# 4. Numerical-convention gap discovered

Round 41 identified a documentation regression in later integration text.

Authoritative frozen calculation:

`calculations/LPE_CHARGE_COMPOSITION_SENSITIVITY.md`

uses:

- Hg 200.59 g/mol;
- Cd 112.414 g/mol;
- Te 127.60 g/mol;

and yields:

- Hg `0.2497382358`;
- Cd `0.01250164993`;
- Te `0.7377601143`.

Some P30A/P16B/Round-40 text used approximately 0.249740/0.012502/0.737758 from a slightly different Hg atomic-weight convention.

Disposition:

`CONTROLLED-NUMERICAL-ERRATUM`.

Future calculations use the frozen calculation values until a deliberate versioned constant update is propagated throughout the repository.

No readiness row changes because the numerical difference is immaterial relative to the unresolved apparatus-dependent `M_charge` and process calibration.

---

# 5. What literature searching should not be used for after Round 41

Do not attempt to literature-search the following as though they were universal physical constants:

- local QCM tooling factor;
- local MFC correction/actual flow;
- actual furnace-to-melt temperature offset;
- actual boat hot usable volume;
- local RIE self-bias/chamber seasoning/t_clear;
- local detector-station electronics floor;
- local package bondline thickness/voiding;
- local singulation functional edge-damage distance.

Relevant literature may define what should be measured, but cannot supply the realized value of an unbuilt local apparatus.

---

# 6. Readiness disposition after Round 41

Unchanged:

- `TRACEABLE-FIRST-BUILD-READY = NO`
- `HISTORICAL-RP01-REPRODUCED = NO`
- `REPRODUCIBLE-RELEASE = NO`

Reason:

Round 41 defines the implementation requirements and fill-in register. No real laboratory/tool identities or calibration results have been supplied.

---

# 7. Next gap boundary

After Round 41, the strongest analytical work is no longer a generic literature search. It is to turn the capability specification into **procurement-neutral subsystem requirement sheets and acceptance-test protocols**, prioritizing the highest-risk upstream systems:

1. LPE furnace/boat/gas/actuator acceptance requirements;
2. Hg anneal enclosure/thermal-zone acceptance requirements;
3. integrated detector-station uncertainty budget;
4. RIE/QCM calibration acceptance protocols.

Vendor selection should remain deferred unless explicitly requested.

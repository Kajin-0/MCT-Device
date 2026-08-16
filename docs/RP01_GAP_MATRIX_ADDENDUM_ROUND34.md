# RP-01 gap matrix addendum — Round 34: first-build / release readiness

**Date:** 2026-08-16 America/New_York

Round 34 converts the accumulated gap record into a build-readiness hierarchy.

---

## 1. Current project maturity

| Maturity claim | Status | Dominant reason |
|---|---|---|
| `TRACEABLE-FIRST-BUILD-READY` | **NO** | multiple irreversible local process branches and metrology implementations remain unfrozen |
| `HISTORICAL-RP01-REPRODUCED` | **NO** | many historically critical apparatus/material/process identities remain source-open |
| `REPRODUCIBLE-RELEASE` | **NO** | no repeated end-to-end local capability/yield dataset and multiple execution branches not yet frozen |

---

## 2. Highest-impact execution blockers

| Area | Status | Why it blocks first packaged build | Closure route |
|---|---|---|---|
| P30 LPE boat/well/absolute charge/thermal/contact/wipe/cooldown | `EXECUTION-BLOCKER` | operator cannot instantiate one complete growth without selecting apparatus-specific values | recover direct traveler or freeze a fully documented local P30 qualification branch |
| P07C/P29 final CdZnTe surface | `EXECUTION-BLOCKER` | final interface state/clean-to-load route not selected | freeze one locally interface-qualified final-surface branch |
| P31 Hg anneal apparatus/reservoir/trajectory | `EXECUTION-BLOCKER` | final carrier-state operation requires actual Ts/THg/pHg/dwell/cooldown | freeze one qualification trajectory and Hall/optical gates |
| P32/P28 Mask-1 + wet mesa | `EXECUTION-BLOCKER` | resist and etchant preparation basis remain incomplete | source-close chemistry or freeze local branch with explicit bases/assays/rinse/endpoint |
| P25 anodic oxide branch | `EXECUTION-BLOCKER` | transfer center exists but actual local cell/bath branch not selected | instantiate cell, bath, area, current density, V(t)/charge and outcome gates |
| P27 Mask-2 | `EXECUTION-BLOCKER` | direct historical anchors do not form a complete resist process | freeze resist/spin/exposure/developer/chlorobenzene/lift-off branch |
| P34 RIE local realization | `EXECUTION-BLOCKER` | controller anchors do not define gas delivery/reactor/sheath/sample state | select reactor/gas realization and qualify oxide clear + electrical conversion |
| P26 Cr/Au deposition/lift-off | `EXECUTION-BLOCKER` | historical thickness does not define deposition implementation | freeze tool/base pressure/rates/QCM/thermal/RIE-to-metal/lift-off branch |
| P35 singulation | `EXECUTION-BLOCKER` for packaged route | package-ready die requires actual separation/protection/clean/street branch | freeze selected P35 branch and witness plan |
| P33 package/interconnect | `EXECUTION-BLOCKER` | end-to-end route requires actual carrier/attach/wire/optical/vacuum construction | freeze one P33 qualification branch |

---

## 3. Local implementation gates

| Method | Status | Required closure |
|---|---|---|
| P05 Hall/VdP | `LOCAL-IMPLEMENTATION-GATE` | actual magnet/cryostat/electrical/contact/temperature/reduction implementation |
| P06/P06A FTIR | `LOCAL-IMPLEMENTATION-GATE` | instrument/method/model/map/thickness-reference implementation |
| P10/P10A bias/load | `LOCAL-IMPLEMENTATION-GATE` | actual bias/load/contact-voltage/readout transfer implementation |
| P11/P11A radiometry | `LOCAL-IMPLEMENTATION-GATE` | calibrated source/reference/aperture/view-factor/wavelength/electronics chain |
| P12/P12B/P12C noise | `LOCAL-IMPLEMENTATION-GATE` | preamp/analyzer/window/ENBW/background/terminal-referral implementation |
| P13/P13A dynamics | `LOCAL-IMPLEMENTATION-GATE` | source/injection/readout/package-deembedding/analysis implementation |
| P35 edge/subsurface metrology | `LOCAL-IMPLEMENTATION-GATE` | edge/chip/subsurface/reidue measurement methods for selected cut branch |
| P33 package thermal state | `LOCAL-IMPLEMENTATION-GATE` | die-temperature proxy and package thermal-kernel measurement |

---

## 4. Historical identity gaps that should not halt local qualification once a branch is frozen

- exact historical FTIR/material-metrology instrument;
- exact Optronics model/calibration chain;
- exact Figure-5 HP35665A settings;
- exact 2001 low-noise preamplifier circuit;
- exact historical performance contact pair/gap;
- exact 4.4-µm cutoff convention;
- exact RP-01 temporal-response/lifetime method;
- exact historical singulation method/die outline;
- exact historical package/interconnect construction.

These block literal historical claims, not a transparently labeled local reconstruction.

---

## 5. Release blockers after first-build readiness

Even when the execution rows above are frozen, P17/P17A still require:

- MSA/repeatability/reproducibility/uncertainty for critical release measurements;
- repeated LPE/anneal/material runs;
- repeated frontside fabrication data;
- repeated P35/P33 functional yield;
- detector-derived engineering limits;
- stability assessment;
- final yield/performance target;
- capability/risk analysis;
- controlled change/requalification rules;
- repeated complete-route demonstration.

A successful first device cannot close these.

---

## 6. Round-34 architecture defects closed

### P16

Closed:

- obsolete statement that master flow integrates only P01–P15;
- obsolete Phase-G routing of singulation to P15;
- missing P35 singulation data package;
- missing cryogenic feedback from P33 to P35 final disposition;
- missing explicit distinction among first-build readiness, historical reproduction and release.

### P19

Closed:

- missing singulation/die-edge detector requirement;
- package traceability that omitted P33/P35;
- master traceability table that treated package as P15-only.

### P17

P17A now closes the missing singulation/package change-control and yield extension.

### P18

P18A now closes the missing dedicated post-singulation/edge/package-interaction diagnostic route.

---

## 7. Current highest-value historical recovery targets

Historical recovery remains useful where it can directly replace an execution blocker. Highest value now:

1. Honeywell/Fermionics/UWA LPE traveler giving boat/well geometry, absolute charge and contact/wipe trajectory.
2. Direct UWA/Srivastav wet-mesa preparation basis and rinse/strip details.
3. UWA Mask-1/Mask-2 resist/exposure/developer records.
4. Plasma Technology RP-01 reactor/gas-delivery/self-bias/sample-temperature records.
5. Direct UWA/Fermionics anneal apparatus/trajectory.
6. Cr/Au deposition traveler.

Lower immediate execution priority, although still historically valuable:

- Optronics model;
- HP35665A settings;
- historical lifetime method;
- exact historical package/singulation identity.

---

## 8. Strongest next action

Proceed with the first item in the P16A closure priority: **P30 LPE absolute apparatus / charge / contact-trajectory closure**.

Do not merely collect another tie-line or theoretical liquidus relation. The next round should attempt to recover or construct, from primary empirical evidence only, the minimum executable local/historical branch for:

`{boat/well geometry,total melt inventory,source genealogy,atmosphere,thermometry,equilibration,contact interval,separation/wipe,cooldown}`.

If direct historical closure fails, preserve that negative result and define exactly what must be locally calibrated before a first-build branch can move from `OPEN-CHOICE` to `LOCAL-BRANCH-FROZEN`.

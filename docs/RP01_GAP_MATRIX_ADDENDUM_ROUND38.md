# RP-01 gap matrix addendum — Round 38: Cr/Au deposition apparatus / vacuum / rate closure

**Date:** 2026-08-16 America/New_York

## 1. Scope

This addendum updates the P16A R20/R21 metallization state after a focused primary-source audit and the addition of P26A.

---

## 2. Gap table

| Gap | Current evidence | Historical identity | First-build effect | Closure route |
|---|---|---|---|---|
| Cr identity/thickness | RP-01 Cr `30 nm` | `CLOSED-DIRECT` | executable target | retain direct target; verify actual thickness by calibrated P26A/P26 metrology |
| Au identity/thickness | RP-01 Au `270 nm` | `CLOSED-DIRECT` | executable target | retain direct target; verify actual thickness by calibrated P26A/P26 metrology |
| historical deposition method | RP-01 silent; same-UWA 1998 uses angled thermal evaporation | `HISTORICAL-IDENTITY-OPEN` | local method must be selected | P26A method branch; thermal evaporation strongest same-UWA candidate but not RP-01 fact |
| historical deposition tool/model | not recovered | `HISTORICAL-IDENTITY-OPEN` | actual lab tool mandatory | P26A actual manufacturer/model/serial/revision |
| Cr source/boat/crucible | not recovered | `HISTORICAL-IDENTITY-OPEN` | actual lab source hardware mandatory | P26A source genealogy/hardware freeze |
| Au source/boat/crucible | not recovered | `HISTORICAL-IDENTITY-OPEN` | actual lab source hardware mandatory | P26A source genealogy/hardware freeze |
| source-to-sample geometry / incidence | same-UWA angled deposition exists, RP-01 geometry unknown | `HISTORICAL-IDENTITY-OPEN` | affects flux/lift-off/CD/thermal state | P26A dimensioned local geometry + P27/P26 lift-off gate |
| historical base pressure | not recovered | `HISTORICAL-IDENTITY-OPEN` | local pressure criterion mandatory | characterize actual tool; freeze P26A local base-accept rule from capability + P26 outcomes |
| historical deposition pressure | not recovered | `HISTORICAL-IDENTITY-OPEN` | local logging/limit mandatory | P26A/P26 pressure trace + correlation |
| historical Cr rate | not recovered | `HISTORICAL-IDENTITY-OPEN` | local rate must be frozen | P09A/P26 DOE; do not copy Au rate |
| historical Au rate | not recovered; other HgCdTe primary studies establish several-Å/s scales | `HISTORICAL-IDENTITY-OPEN` | local rate must be frozen | P09A/P26 DOE; transfer rates are screening context only |
| QCM/thickness monitor | not recovered | `HISTORICAL-IDENTITY-OPEN` | local metrology mandatory | P26A independent Cr/Au tooling-factor calibration against witnesses |
| sample thermal state during deposition | not recovered | `HISTORICAL-IDENTITY-OPEN` | local thermal calibration mandatory | P26A dummy/surrogate calibration + hold criterion |
| RIE-to-metal load-lock on actual RP-01 devices | paper describes capability/benefit, not demonstrated run history | `HISTORICAL-IDENTITY-OPEN` | local handoff branch mandatory | P26A actual `VACUUM/INERT/AIR` transfer + P26 delay qualification |
| Cr-to-Au vacuum break | not recovered | `HISTORICAL-IDENTITY-OPEN` | local sequence mandatory | freeze actual P26A same-vacuum or explicit break branch |
| pre-metal intervention | no direct RP-01 clean recovered | `HISTORICAL-IDENTITY-OPEN` | baseline forbids undocumented intervention | `P08 -> controlled transfer -> Cr`; any clean is new branch |
| lift-off solvent/time/T/agitation | RP-01 establishes successful lift-off but no detailed chemistry | `HISTORICAL-IDENTITY-OPEN` | R21 remains execution blocker | P27/P26 local lift-off qualification |
| TLM downstream outcome | `rho_c≈9e-4 Ω·cm² at 80 K` | `CLOSED-DIRECT` benchmark | local process must demonstrate function | P26/P09 TLM, stability and detector-noise gates |

---

## 3. P16A R20 disposition

Current state remains:

`R20 = APPARATUS-NOT-SELECTED`.

Reason:

P26A now supplies a controlled apparatus-instantiation method and register, but no actual laboratory deposition tool/revision/source geometry/vacuum criterion/QCM calibration/rate/thermal/handoff branch has been populated.

P26A method existence therefore does not satisfy first-build readiness.

R20 may become `LOCAL-BRANCH-FROZEN` only when the actual P26A register reaches `P26-APPARATUS-READY` with all mandatory first-build coordinates frozen under change control.

---

## 4. P16A R21 disposition

Current state remains:

`R21 = OPEN-CHOICE`.

Round 38 did not recover the RP-01 lift-off solvent, bath temperature, time, agitation, rinse or dry sequence.

P27/P26 remain the closure owners.

Do not infer acetone, NMP, ultrasonics or another generic lift-off sequence from common practice.

---

## 5. Documentary-limit rule

The following sources are already identified and should not be repeatedly rediscovered as if new:

- Smith et al. 2000 SIMC-XI in-situ vacuum-processing paper;
- Musca et al. 1999 contact/passivation conference paper.

Both remain high-value bridges, but full process text was not recovered in Round 38.

Reopen historical metallization search only with a new access path/source family.

---

## 6. First-build versus historical reproduction

A local thermal-evaporation branch can eventually satisfy first-build traceability if P26A and P26 are fully instantiated and qualified.

That would support:

`TRACEABLE-FIRST-BUILD-READY` for R20,

but **not**:

`HISTORICAL-RP01-REPRODUCED` for the metallization operation,

unless direct historical deposition identity is later recovered.

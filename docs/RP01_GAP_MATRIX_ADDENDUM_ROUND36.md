# RP-01 gap-matrix addendum — Round 36 wet-mesa chemistry basis

**Date:** 2026-08-16 America/New_York  
**Scope:** P16A R13–R14 / P01/P28/P28A.

| Gap | Historical state after Round 36 | First-build class | Closure route | Current disposition |
|---|---|---|---|---|
| RP-01 exact wet-mesa chemistry | not disclosed in recovered RP-01 text | historical identity | recover UWA traveler/notebook or use explicitly local P28/P28A branch | `OPEN-HISTORICAL` |
| Srivastav `2% Br2` basis | direct paper gives notation but no w/w/v/v/w/v/molar definition | execution | recover thesis/lab record or explicitly define local concentration mathematics | `UNDEFINED-BASIS` |
| Srivastav `3:1 EG:HBr` basis | ratio printed; mass/volume basis not stated | execution | recover direct definition or define local ratio mathematics | `UNDEFINED-BASIS` |
| HBr stock assay in Srivastav work | not recovered | execution | local recipe records certified stock assay/density/water state | `OPEN-CHOICE` |
| v/v historical hypothesis | same-SSPL/overlapping-author patent explicitly uses v/v Br2/MeOH; same-author review uses vol% for Br2/MeOH | evidence ranking | retain as `CANDIDATE-VV-SAME-LAB`, qualify locally | `CANDIDATE` only |
| alternate convention risk | primary Leech HgCdTe literature explicitly uses `0.1% (w/w) Br:HBr` | provenance control | never assume universal convention | `CLOSED-AS-WARNING` |
| reagent-addition order | not recovered | execution | explicit institution-approved local sequence + fixed branch ID | `OPEN-CHOICE` |
| bath volume/loading | not recovered for selected source result | execution | define local bath volume/exposed-area/run-order genealogy | `OPEN-CHOICE` |
| agitation implementation | mechanism discusses transport/agitation; exact source setting not recovered | execution | select reproducible local mode and recalibrate R_V/R_L | `OPEN-CHOICE` |
| Br2 volatility / bath age | source identifies concentration drift via volatility | execution/release | preparation/open-time/run-order genealogy + optional analytical proxy | `METHOD-CLOSED / LIMIT-OPEN` |
| patterned-mesa quench/rinse/dry | exact Srivastav sequence not recovered | execution | qualify local P28A handoff branch | `OPEN-CHOICE` |
| wet-mesa→P25 air exposure | exact RP-01 timing/ambient unknown; same-SSPL patent gives no-air-exposure surface-processing precedent | execution | timestamp etch/quench/rinse/dry/P25 and qualify downstream oxide response | `OPEN-CHOICE` |
| x≈0.30 transfer of rate/profile | source material x=0.28 | release | matched x≈0.30 coupon R_V/R_L/profile/roughness/isolation study | `RELEASE-DATA-OPEN` |
| through-9.5-µm isolation overetch | no direct historical margin | release | measured depth + electrical isolation + lateral-loss gate | `RELEASE-DATA-OPEN` |
| thesis `G25544.pdf` | official IISc record identified; full relevant text blocked by current retrieval path | historical identity | recover via accessible institutional copy/author archive; inspect relevant pages directly | `IDENTIFIED-NOT-RECOVERED` |

---

## P16A state after Round 36

### R13 — wet-mesa etchant preparation basis

`UNDEFINED-BASIS`

Reason: P28A provides an explicit method and a ranked `v/v` candidate, but no physical local recipe has yet selected the Br2 mathematical definition, EG:HBr ratio basis, HBr stock assay and actual reagent genealogy.

### R14 — endpoint / rinse / passivation handoff

`OPEN-CHOICE`

Reason: the local bath state, endpoint, rinse/dry/wet-transfer path and `t_etch→P25` trajectory remain unfrozen.

Therefore:

`TRACEABLE-FIRST-BUILD-READY = NO`.

---

## What Round 36 actually closed

- disproved the idea that an unspecified HgCdTe bromine percentage has a universal convention;
- elevated v/v from an unsupported guess to a same-SSPL/overlapping-author candidate convention;
- preserved the direct Srivastav notation without falsifying it;
- created a mathematically explicit local chemistry-definition path;
- made HBr stock assay a first-class recipe coordinate;
- linked wet-etch rinse/air exposure explicitly into the P25 passivation state;
- recorded the IISc thesis access failure without converting it into a negative-content claim.

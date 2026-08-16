# P16A — first-build readiness register

**Status:** CONTROLLED PRE-EXECUTION REGISTER  
**Date:** 2026-08-16 America/New_York

Use with `procedures/P16A_FIRST_BUILD_RELEASE_READINESS_AUDIT.md`.

## 1. Allowed row states

- `DIRECT-EXECUTABLE`
- `LOCAL-BRANCH-FROZEN`
- `OPEN-CHOICE`
- `UNDEFINED-BASIS`
- `APPARATUS-NOT-SELECTED`
- `METROLOGY-NOT-IMPLEMENTED`
- `RELEASE-DATA-OPEN`
- `HISTORICAL-IDENTITY-OPEN`
- `NOT-APPLICABLE`

`TRACEABLE-FIRST-BUILD-READY` requires every mandatory execution/metrology row to be `DIRECT-EXECUTABLE`, `LOCAL-BRANCH-FROZEN`, or justified `NOT-APPLICABLE`.

A controlled method for closing a row is not the same as row closure. Round 35 added P30A as the closure route for R04–R07; Round 36 adds P28A as the chemistry-definition/lineage closure route for R13–R14. Those rows remain open until actual laboratory branches are instantiated numerically and physically.

---

## 2. Master readiness table

| ID | Process / measurement | Controlled modules | Blocker class | Mandatory for packaged first build? | Current Round-36 state | Required closure before build |
|---|---|---|---|---|---|---|
| R01 | source-element identity/inventory | P03/P30/P30A | execution | YES | `OPEN-CHOICE` | freeze supplier/lots/purity/inventory and actual source/charge branch |
| R02 | CdZnTe substrate composition/face/miscut | P07/P29 | execution | YES | `OPEN-CHOICE` | select incoming substrate specification and record measured plane/polarity/miscut |
| R03 | final CdZnTe pre-LPE surface | P07C/P29 | execution | YES | `OPEN-CHOICE` | freeze mechanical/chemical final surface + removed depth + clean-to-load branch |
| R04 | LPE boat/well/source hardware | P03/P30/P30A | execution | YES | `APPARATUS-NOT-SELECTED` | instantiate P30A: specific dimensioned boat/furnace/tube/actuator; calibrated well volume, clearances, thermometry and hot motion |
| R05 | absolute LPE charge inventory | P03C/P03D/P30/P30A | execution | YES | `OPEN-CHOICE` | after R04, select numerical `M_charge`; calculate/record actual Hg/Cd/Te masses and independent auxiliary Hg/HgTe inventory; no substrate-area scaling |
| R06 | LPE atmosphere | P03/P30/P30A | execution | YES | `OPEN-CHOICE` | freeze gas identities/grades, purge/process flows, pressure/backpressure, purification and O2/H2O monitoring/acceptance |
| R07 | LPE thermal/contact/wipe/cooldown trajectory | P03B/P03E/P30/P30A | execution | YES | `OPEN-CHOICE` | calibrate local liquidus/thermometry; freeze numerical T(t), `ΔT_SC`, physical contact interval, separation/wipe motion and cooldown; attach P06/P05 outcome evidence |
| R08 | as-grown optical material metrology | P06/P06A | local implementation | YES | `METROLOGY-NOT-IMPLEMENTED` | select/qualify FTIR, optical model, map geometry and independent thickness reference |
| R09 | as-grown Hall/VdP | P05 | local implementation | YES | `METROLOGY-NOT-IMPLEMENTED` | select/qualify magnet, cryostat, contacts, current/voltage chain and reduction |
| R10 | Hg anneal enclosure/reservoir | P04/P31 | execution | YES | `APPARATUS-NOT-SELECTED` | freeze sample/reservoir geometry and Hg-source state |
| R11 | Hg anneal trajectory | P04A/P04B/P23/P31 | execution | YES | `OPEN-CHOICE` | freeze Ts(t), THg(t), pHg/source proxy, dwell and cooldown with Hall/optical gates |
| R12 | Mask-1 resist/lithography | P14/P32 | execution | YES | `OPEN-CHOICE` | choose resist, coating, bake, exposure, developer, alignment and strip branch |
| R13 | wet-mesa etchant preparation basis | P01/P01A/P28/P28A | execution | YES | `UNDEFINED-BASIS` | instantiate P28A: select an explicit Br2 definition and denominator, explicit EG:HBr ratio basis, certified HBr assay and actual reagent genealogy; same-SSPL `v/v` evidence is candidate support, not historical closure |
| R14 | wet-mesa endpoint/rinse/passivation handoff | P01/P28/P28A | execution | YES | `OPEN-CHOICE` | freeze bath T/agitation/age, measured isolation/depth endpoint, quench/rinse/dry or wet-transfer path, air-exposure trajectory and `t_etch→P25`; qualify resulting P25 response |
| R15 | anodic oxide cell/bath execution | P02/P25 | execution | YES | `OPEN-CHOICE` | select electrolyte/cell/exposed area/current-density/V(t)-charge endpoint/rinse branch |
| R16 | Mask-2 resist/exposure/develop/chlorobenzene | P14A/P27 | execution | YES | `OPEN-CHOICE` | freeze product, coating, exposure, developer, chlorobenzene bath state/sequence |
| R17 | RIE gas realization | P08/P24/P34 | execution | YES | `UNDEFINED-BASIS` | define actual CH4/H2 composition/delivery realizing local branch; do not guess historical split |
| R18 | RIE reactor/sheath/thermal state | P08D/P24/P34 | execution | YES | `APPARATUS-NOT-SELECTED` | select reactor and freeze geometry, pressure control, RF, self-bias proxy, holder/Ts, clean/season |
| R19 | oxide clear + semiconductor exposure | P08D/P34 | execution | YES | `OPEN-CHOICE` | measure t_clear and freeze t_sem/output gates for selected reactor |
| R20 | Cr/Au deposition | P09/P09A/P26 | execution | YES | `APPARATUS-NOT-SELECTED` | select deposition tool/method, base pressure, rates, QCM, thermal limit and RIE-to-Cr clock |
| R21 | lift-off | P14A/P26/P27 | execution | YES | `OPEN-CHOICE` | freeze solvent/time/temperature/agitation/rinse compatible with final device |
| R22 | final CD/contact geometry | P14/P10 | local implementation | YES | `METROLOGY-NOT-IMPLEMENTED` | freeze measurement method and device/contact-pair naming |
| R23 | TLM/contact QC | P09/P24/P26 | local implementation | YES | `METROLOGY-NOT-IMPLEMENTED` | freeze 80-K electrical fixture, geometry reduction and blocking-contact functional gate |
| R24 | bare-device bias/load/self-heating | P10/P10A | local implementation | YES | `METROLOGY-NOT-IMPLEMENTED` | freeze actual bias/load/preamp network and detector-contact voltage measurement |
| R25 | absolute responsivity | P11/P11A | local implementation | YES | `METROLOGY-NOT-IMPLEMENTED` | freeze calibrated optical transfer/radiometry chain and state conventions |
| R26 | detector-terminal noise/PSD | P12/P12B/P12C | local implementation | YES | `METROLOGY-NOT-IMPLEMENTED` | freeze preamp/analyzer transfer, FFT/window/ENBW, background and terminal referral |
| R27 | temporal/frequency response | P13/P13A | local implementation | qualification YES | `METROLOGY-NOT-IMPLEMENTED` | freeze source, injection, electrical/package transfer and analysis branch |
| R28 | singulation street/method/support/protection | P35 | execution | YES for packaged route | `OPEN-CHOICE` | select branch and define sacrificial street/edge-exclusion geometry |
| R29 | singulation clean/edge/subsurface inspection | P35 | execution + metrology | YES for packaged route | `OPEN-CHOICE` | freeze compatible clean and edge/subsurface-damage measurement route |
| R30 | die attach/carrier/cold finger | P15/P33 | execution | YES | `OPEN-CHOICE` | select materials, bondline, cure, carrier geometry and thermal qualification branch |
| R31 | wire/interconnect | P15/P33 | execution | YES | `OPEN-CHOICE` | select wire/ribbon, bonder/tool/settings and coupon qualification branch |
| R32 | aperture/window/shield/FOV | P11/P15/P33 | execution + metrology | YES | `OPEN-CHOICE` | define physical geometry, transmission and radiometric reference plane |
| R33 | vacuum/pump/bake/cooldown | P15/P33 | execution | YES | `OPEN-CHOICE` | freeze pressure measurement, pump/purge/bake thermal budget and cooldown trajectory |
| R34 | cryogenic singulation/package survival | P33/P35 | release of package-ready die | YES | `RELEASE-DATA-OPEN` | demonstrate no crack propagation/electrical-noise-optical degradation after intended cycles |
| R35 | end-to-end genealogy/data capture | P16/P17 | execution | YES | `LOCAL-BRANCH-FROZEN` conceptually | instantiate IDs, raw-data paths, revisions, deviations and signatures for actual laboratory |
| R36 | statistical process capability/yield | P17 | release | NO for first qualification build | `RELEASE-DATA-OPEN` | repeated frozen-route runs, MSA, stability, limits, yield and change control |

### Round-35 LPE status note

P30A closes a **methodological** gap: there is a controlled procedure and register for converting measured boat geometry into an empirically selected absolute charge and trajectory. It does not close the **physical implementation** gap because the project has not yet specified an actual laboratory boat/furnace/tube/actuator, numerical `M_charge`, atmosphere or trajectory.

Therefore R04–R07 remain blocking rows.

### Round-36 wet-mesa chemistry status note

P28A closes another **methodological/evidence-ranking** gap. The direct Srivastav paper still does not define the basis of `2% Br2`, the basis of `3:1 EG:HBr`, or the HBr stock assay. Same-SSPL/overlapping-author process evidence explicitly uses `v/v` for Br2/methanol, which upgrades a volume-based interpretation to a ranked candidate but does not redefine the historical mesa formulation. Primary HgCdTe literature also explicitly contains `w/w` Br:HBr conventions.

Therefore R13 remains `UNDEFINED-BASIS` until a local recipe is mathematically and materially instantiated, and R14 remains `OPEN-CHOICE` until the post-etch trajectory is frozen and qualified.

---

## 3. Historical-identity register

These do not block a clearly labeled local qualification build but block literal historical claims unless closed.

| Historical item | Current state | First-build effect |
|---|---|---|
| exact RP-01 CdZnTe supplier face/miscut/final surface | `HISTORICAL-IDENTITY-OPEN` | local qualified substrate branch may substitute |
| exact Honeywell/Fermionics LPE boat dimensions/charge/gas/contact traveler | `HISTORICAL-IDENTITY-OPEN` | Round-35 audit recovered detailed topology but no dimensions/grams; local P30/P30A branch may substitute once physically instantiated |
| exact supplier/UWA Hg-anneal history | `HISTORICAL-IDENTITY-OPEN` | local P31 branch may substitute |
| exact Mask-1 product/process | `HISTORICAL-IDENTITY-OPEN` | local P32 branch may substitute |
| exact Mask-2 resist/exposure/developer/lift-off | `HISTORICAL-IDENTITY-OPEN` | local P27 branch may substitute |
| exact Srivastav/RP-01 wet-mesa chemistry basis | `HISTORICAL-IDENTITY-OPEN` and execution currently unresolved | Round-36 same-SSPL evidence supports `v/v` as candidate only; local P28/P28A branch may substitute once explicitly defined and qualified |
| exact wet-mesa rinse/air-exposure/anodization handoff | `HISTORICAL-IDENTITY-OPEN` | same-SSPL and other primary transfer branches establish trajectory importance but do not identify RP-01 handoff |
| exact Plasma Technology reactor hardware/gas realization | `HISTORICAL-IDENTITY-OPEN` and execution currently unresolved | local P34 reactor branch may substitute once frozen |
| exact Cr/Au deposition hardware/rates/vacuum | `HISTORICAL-IDENTITY-OPEN` | local P26 branch may substitute |
| exact material method behind x≈0.30 / 9.5 µm | `HISTORICAL-IDENTITY-OPEN` | modern P06/P06A may measure local state |
| exact Optronics model/calibration | `HISTORICAL-IDENTITY-OPEN` | modern P11/P11A may establish absolute response |
| exact preamp/HP35665A settings | `HISTORICAL-IDENTITY-OPEN` | modern P12 chain may measure detector noise |
| exact performance contact pair/gap | `HISTORICAL-IDENTITY-OPEN` | local selected/measured pair is valid for local device |
| exact 4.4-µm cutoff convention | `HISTORICAL-IDENTITY-OPEN` | local response must state its own cutoff convention |
| exact RP-01 singulation/die outline | `HISTORICAL-IDENTITY-OPEN` | local P35 branch may substitute |
| exact RP-01 package/interconnect | `HISTORICAL-IDENTITY-OPEN` | local P33 branch may substitute |
| direct RP-01 lifetime/f3dB | `HISTORICAL-IDENTITY-OPEN` | local P13 may characterize actual device |

---

## 4. Pre-build authorization checklist

Before declaring `TRACEABLE-FIRST-BUILD-READY`, answer YES to all applicable questions:

- [ ] Every irreversible process has a selected branch and revision.
- [ ] Every chemical/reagent concentration has an explicit preparation basis and stock assay/grade where relevant.
- [ ] P28A contains an explicit Br2 mathematical definition/denominator, EG:HBr definition, HBr assay and reagent genealogy for the selected local mesa branch.
- [ ] P28/P28A contain a frozen bath-temperature/agitation/age and rinse/air-exposure/P25-handoff trajectory supported by coupon data.
- [ ] Every commercial consumable/product is identified by manufacturer/product/lot or a controlled equivalent specification.
- [ ] Every process tool is identified by model/serial/revision and required calibration state.
- [ ] Every required setpoint or trajectory is specified numerically or by a calibrated physical endpoint.
- [ ] P30A contains a dimensioned actual boat, calibrated well volume, numerical growth charge and independently defined Hg-source inventory.
- [ ] P30A contains an implemented gas/thermometry/contact/wipe/cooldown branch supported by P06/P05 qualification data.
- [ ] Every sensitive elapsed-time handoff has a recorded clock and current qualification rule.
- [ ] Every endpoint/gate has an implemented measurement method.
- [ ] Required destructive qualification is assigned to witnesses/coupons rather than the only detector die.
- [ ] Every historical substitution is labeled as local transfer rather than historical RP-01 fact.
- [ ] P35 is selected for packaged route and P33 accepts its incoming die state.
- [ ] P10–P13 share or explicitly correct detector state variables where combined.
- [ ] Data/genealogy identifiers and raw-data storage paths are instantiated before work begins.
- [ ] EH&S/facility authorizations are separately satisfied for the actual laboratory.

Authorization:

`TRACEABLE-FIRST-BUILD-READY = YES / NO`

Reviewer: __________  Date: __________  Revision: __________

---

## 5. Post-run maturity disposition

After one complete run, select only labels supported by evidence:

- [ ] `QUALIFICATION-RUN-COMPLETE`
- [ ] `QUALIFICATION-RUN-FAILED`
- [ ] one or more modules `LOCAL-QUALIFIED`
- [ ] `HISTORICAL-RP01-REPRODUCED`
- [ ] `PILOT-RELEASE`
- [ ] `REPRODUCIBLE-RELEASE`

Attach the P17 justification for any release label above qualification-run status.
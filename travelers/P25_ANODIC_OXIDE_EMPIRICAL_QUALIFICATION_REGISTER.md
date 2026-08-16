# P25 anodic-oxide empirical qualification register

**Status:** BLANK CONTROLLED DEVELOPMENT RECORD  
**Use with:** P02/P02A/P02B/P02C/P25, P08, P09, P10–P13

Do not fill unknown fields from nominal recipe values. Use `OPEN`, `N/A`, `NOT-MEASURED`, or the actual measured value.

---

## A. Run identity

- P25 run ID:
- date/time:
- operator:
- wafer/growth ID:
- coupon/die ID:
- wafer coordinate/orientation:
- process objective:
- provenance center used: `TI-TRANSFER / LOCAL / OTHER`:
- deviation/change-control reference:

---

## B. Incoming HgCdTe state

- growth family:
- nominal/measured x:
- P06 edge metric and temperature:
- active-layer thickness:
- incoming carrier state:
- Hall measurement temperature:
- `n_H/p_H` or multicarrier result:
- `mu_H`:
- sheet resistance:
- mesa already formed? Y/N:
- mesa depth:
- sidewall angle/profile reference:
- last wet-chemical step:
- semiconductor depth removed in last step:
- final rinse before anodization:
- final dry method:
- clean-to-anodization delay:
- storage atmosphere during delay:
- incoming DIC/image file:
- comments:

---

## C. Electrolyte batch

- bath ID:
- KOH supplier/lot/grade:
- KOH mass/amount:
- target molarity:
- calculated actual molarity:
- EG supplier/lot/grade:
- EG water-content specification:
- DI-water source/resistivity:
- EG:H2O ratio:
- ratio basis (`volume/mass/other/OPEN`):
- preparation order:
- preparation timestamp:
- bath volume:
- storage container/condition:
- bath age at use:
- fresh/reused/replenished:
- measured pH + method/calibration:
- measured conductivity + method/calibration:
- visible contamination/precipitate:
- bath temperature before run:
- bath temperature after run:

---

## D. Cell / fixture

- vessel material/ID:
- HgCdTe anode electrical-contact method:
- anode lead material/location:
- cathode material:
- cathode dimensions/exposed area:
- electrode separation:
- electrode orientation:
- sample orientation:
- immersion depth:
- masking/fixture material:
- exposed top area:
- exposed sidewall area estimate:
- exposed backside area:
- total electrochemically exposed area `A_exposed`:
- area determination method:
- agitation state (`UNSTIRRED/STIRRED/OTHER`):
- agitation method/rate:
- bubble observation before current:
- fixture/cell photo reference:

---

## E. Electrical setup

- constant-current source ID:
- calibration date/result:
- voltage meter/logger ID:
- calibration date/result:
- acquisition rate:
- voltage compliance:
- selected `J`:
- calculated current `I=J*A_exposed`:
- actual current mean:
- actual current range/stability:
- polarity verified? Y/N:
- raw V(t) file:

---

## F. Galvanostatic process

- current-on timestamp:
- initial voltage:
- induction interval `t_ind`:
- induction definition used:
- time of sustained voltage rise:
- defined growth-fit interval:
- `dV/dt` over growth-fit interval:
- time to 5 V:
- time to 10 V:
- time to 15 V:
- terminal voltage:
- termination basis:
- total duration:
- total charge:
- charge per exposed area:
- compliance event?:
- bubble/gas evolution observation:
- visible film change during process:
- abnormal event/log:

---

## G. Post-anodization handling

- time from current-off to first rinse:
- rinse fluid 1 / duration / agitation:
- rinse fluid 2 / duration / agitation:
- other rinse:
- dry method:
- time to dry completion:
- immediate film color:
- visual uniformity:
- matte/dark regions:
- pinholes/stains/residue:
- photograph reference:
- storage atmosphere after process:
- storage temperature:
- anodization-to-thickness-metrology delay:
- anodization-to-resist delay:
- anodization-to-P08 delay:

---

## H. Physical oxide metrology

- thickness method:
- calibration/reference:
- optical model if ellipsometry:
- oxide-step preparation if profilometry:
- coordinate 1 / thickness:
- coordinate 2 / thickness:
- coordinate 3 / thickness:
- additional map file:
- mean thickness:
- standard deviation/range:
- edge-to-center trend:
- target comparison to 80 nm:
- color under standardized illumination:
- color/thickness calibration status:
- top-surface morphology:
- sidewall coverage method/result:
- corner/perimeter result:

---

## I. Electrical/interface metrology

- pre/post sheet-resistance comparison:
- C–V structure ID/result:
- interface-state metric/model:
- fixed-charge/flat-band metric/model:
- field-effect/surface-conductance result:
- dark I–V structure/result:
- perimeter-to-area structure/result:
- lifetime/transient result:
- comments on accumulation/shunting:

Do not compare numerical interface-state/fixed-charge values to other-x literature as if they were RP-01 specifications.

---

## J. Downstream P08 compatibility

- P08 run ID:
- RIE reactor/state:
- oxide-clear method:
- oxide-clear time:
- residual oxide result:
- HgCdTe recession after clear:
- converted-region sheet/Hall result:
- LBIC result:
- conversion depth/lateral extent if measured:
- RIE abnormality attributable to oxide?:

---

## K. P09 contact closure

- P09 run ID:
- RIE-to-metal delay:
- Cr thickness:
- Au thickness:
- contact I–V:
- 80-K TLM `rho_c`:
- TLM regression/uncertainty:
- adhesion/lift-off result:

---

## L. Detector functional closure

At declared detector temperature, geometry, field and optical state:

- device ID:
- temperature:
- measured contact gap:
- electric field:
- dark current/resistance:
- responsivity:
- response wavelength/source:
- signal frequency:
- noise ASD/PSD:
- 1/f knee:
- g-r plateau:
- NEP:
- D*:
- `tau_eff/f_3dB`:
- perimeter dependence:
- self-heating check:
- passivation-related failure signature:

---

## M. Stability / thermal history

- cumulative room-temperature storage before device test:
- photoresist prebakes:
- vacuum bakes:
- other thermal excursions:
- cryogenic cycle count:
- aging/storage condition:
- pre/post-aging oxide appearance:
- pre/post-aging resistance/I–V:
- pre/post-aging noise:
- pre/post-aging responsivity:

---

## N. V(t) process-fingerprint comparison

Reference run ID:

- `t_ind` difference:
- growth-slope difference:
- terminal-voltage difference:
- charge/area difference:
- thickness difference:
- residual/shape metric if used:
- process-equivalent? `YES/NO/UNRESOLVED`:
- rationale:

A final 80-nm thickness alone is insufficient to declare process equivalence.

---

## O. Disposition

- physical oxide gate: `PASS/FAIL/OPEN`:
- interface/function gate: `PASS/FAIL/OPEN`:
- sidewall gate: `PASS/FAIL/OPEN`:
- P08 compatibility gate: `PASS/FAIL/OPEN`:
- contact gate: `PASS/FAIL/OPEN`:
- detector noise/responsivity gate: `PASS/FAIL/OPEN`:
- stability gate: `PASS/FAIL/OPEN`:
- overall disposition: `DEVELOPMENT-PASS / FAIL / HOLD / REPEAT / LOCAL-QUALIFIED-CANDIDATE`:
- failure record/P18 ID:
- next action:
- reviewer/date:

# P27 — Mask-2 lithography empirical qualification register

**Status:** BLANK CONTROLLED TRAVELER  
**Use:** one register per candidate resist/developer/lift-off branch and run.

Do not back-fill unknown historical values from memory or generic cleanroom practice.

---

## A. Run identity

- P27 run ID:
- date:
- operator:
- wafer/coupon IDs:
- material/growth ID:
- P25 oxide run ID:
- P08 target recipe ID:
- P26 metal target recipe ID:
- candidate resist product:
- candidate evidence class:
- developer product:
- lift-off solvent branch:
- recipe revision:

---

## B. Incoming surface / geometry

- oxide thickness:
- mesa geometry:
- mesa sidewall state:
- time since P25:
- storage environment:
- incoming surface inspection:
- dehydration step, if any:
- adhesion promoter, if any:
- deviation/change-control ID if promoter added:

---

## C. Resist lot / coating

- manufacturer:
- product:
- lot:
- positive-tone chemistry confirmed? YES / NO / UNKNOWN
- DNQ/diazo-novolak confirmed? YES / NO / UNKNOWN
- stated solids/viscosity:
- dilution/thinner:
- dispense volume/method:
- spin coater:
- chuck:
- acceleration:
- spin speed:
- spin duration:
- edge-bead treatment:
- ambient T/RH:
- film defects before bake:

Thickness after coat/bake:

| position | thickness |
|---|---:|
| center | |
| N | |
| S | |
| E | |
| W | |

- mean:
- range:
- historical target `4–5 µm` met? YES / NO

---

## D. Direct RP-01 prebake

Historical center: `80 °C / 30 min`.

- bake method: oven / hotplate / other
- calibrated temperature:
- actual duration:
- sample loading method:
- N2/air/other ambient:
- temperature trace/file:
- thickness before bake:
- thickness after bake:
- visible reflow/cracking:

---

## E. Chlorobenzene treatment

Historical duration: `30 min`.

- order branch: A pre-exposure / B post-exposure / other
- supplier:
- grade:
- lot:
- bath ID:
- fresh/reused:
- bath age:
- start temperature:
- end temperature:
- soak start:
- soak end:
- actual duration:
- static/agitated:
- sample orientation:
- bath covered? YES / NO
- visible contamination:
- dry method after soak:
- intentional post-soak bake? YES / NO
- post-soak bake T/time if YES:
- separate branch ID if nonhistorical bake added:
- film thickness pre-soak:
- film thickness post-soak/dry:
- thickness loss:

---

## F. Exposure

- aligner/tool:
- wavelength/band:
- lamp/source:
- calibrated irradiance:
- calibration date:
- contact/proximity/vacuum mode:
- mask ID/revision:
- mask tone:
- exposure duration:
- calculated/measured dose:
- clearing-dose reference:
- dose normalized to clearing dose:
- focus/gap:
- substrate temperature:
- alignment error:

---

## G. Development

- developer manufacturer/product:
- lot:
- concentrate:diluent ratio:
- diluent:
- DI water quality:
- developer age/reuse:
- developer temperature:
- develop method: puddle / immersion / spray / other
- start/end:
- total develop time:
- agitation:
- endpoint observation:
- water rinse method:
- water rinse time:
- final dry method:
- time developer-end to rinse:

---

## H. Post-develop profile metrology

For representative windows:

| feature ID | resist height | CD_top | CD_bottom | undercut/side | sidewall angle | scum | notes |
|---|---:|---:|---:|---:|---:|---|---|
| | | | | | | | |

- mean resist height:
- mean undercut:
- undercut variation:
- edge roughness:
- alignment to mesa:
- opening completely clear? YES / NO
- microscopy/SEM/profilometry files:
- pre-RIE profile gate: PASS / FAIL / CONDITIONAL

---

## I. P08 RIE survival

Historical-center reference: CH4/H2, 64 sccm total, 100 mTorr, 50 W, 60 s.

- P08 run ID:
- actual RIE condition:
- pre-RIE resist height:
- post-RIE resist height:
- thickness loss:
- pre-RIE CD_top/bottom:
- post-RIE CD_top/bottom:
- pre/post undercut:
- blistering:
- cracking:
- hardening:
- reflow:
- opening blockage/residue:
- plasma polymer/deposit:
- RIE-survival gate: PASS / FAIL / CONDITIONAL

---

## J. P26 metal deposition

- P26 run ID:
- Cr actual thickness:
- Au actual thickness:
- total:
- deposition method:
- source incidence geometry:
- sample maximum temperature:
- sidewall metal continuity visible? YES / NO
- fencing before lift-off:
- resist reflow:
- metal CD before lift-off if measured:

---

## K. Lift-off

- solvent/remover:
- lot:
- bath temperature:
- soak start:
- time to first visible release:
- total duration:
- bath exchanges:
- manual/static agitation:
- ultrasonics used? YES / NO
- ultrasonic frequency:
- power/setting:
- duration:
- rinse sequence:
- dry method:
- mechanical scraping used? YES / NO

If scraping used, automatic disposition = FAIL for process qualification unless explicitly justified as diagnostic only.

---

## L. Post-lift-off inspection

- complete unwanted-metal removal? YES / NO
- metal fences/stringers:
- flakes/redeposition:
- resist residue:
- Cr/Au delamination:
- pad damage:
- mesa damage:
- oxide/passivation damage:
- final contact dimensions:
- final gaps:
- metal edge roughness:
- microscopy files:
- lift-off gate: PASS / FAIL / CONDITIONAL

---

## M. Electrical closure

- P26 TLM data path:
- sample T:
- optical-background/shield state:
- I–V linear/symmetric? YES / NO
- extracted rho_c:
- historical comparison (`~9×10^-4 Ω·cm² at 80 K`):
- contact spread:
- thermal-cycle result:
- aging result:

---

## N. Detector closure, if fabricated

- detector ID:
- P10 I–V/self-heating:
- P11 responsivity:
- P12 noise/NEP/D*:
- P13 temporal response:
- 1/f-noise change attributable to lithography/lift-off? YES / NO / UNRESOLVED
- responsivity change attributable to contact/profile? YES / NO / UNRESOLVED

---

## O. Failure/deviation log

- coating nonuniformity:
- thickness outside 4–5 µm:
- chlorobenzene film loss anomaly:
- scum:
- overdevelopment:
- inadequate undercut:
- excess undercut/collapse:
- RIE profile erosion:
- metal fence:
- incomplete lift-off:
- ultrasound/mechanical damage:
- high rho_c:
- excess noise:
- other:
- P18 record ID:

---

## P. Disposition

- thickness gate: PASS / FAIL
- post-develop profile gate: PASS / FAIL / CONDITIONAL
- P08 survival: PASS / FAIL / CONDITIONAL
- lift-off: PASS / FAIL / CONDITIONAL
- TLM: PASS / FAIL / CONDITIONAL
- detector: PASS / FAIL / CONDITIONAL / NOT TESTED
- overall P27 disposition:
- advance candidate? YES / NO
- approver/date:

### Provenance statement

- direct RP-01 values used:
- primary transfer values used:
- local choices:
- unresolved historical fields:

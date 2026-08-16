# P28A — wet-mesa chemistry-definition qualification register

**Status:** BLANK CONTROLLED PRE-QUALIFICATION REGISTER  
**Use:** complete before a P28 etch-rate/profile run is interpreted as an executable chemistry branch.

A literature notation such as `2% Br2 / 3:1 EG:HBr` is not itself an executable recipe unless the preparation mathematics are known. If the historical basis remains open, assign a new local recipe ID.

---

## A. Chemistry branch identity

- P28A record ID:
- date:
- author/operator:
- target material / nominal x:
- linked P28 run IDs:
- linked Mask-1/P32 recipe:
- candidate recipe ID:
- evidence state:
  - [ ] `NOTATION-ONLY`
  - [ ] `CONVENTION-CANDIDATE`
  - [ ] `CHEMISTRY-DEFINED`
  - [ ] `COUPON-RATE-PROFILE-QUALIFIED`
  - [ ] `THROUGH-LAYER-ISOLATION-QUALIFIED`
  - [ ] `P25-HANDOFF-QUALIFIED`
  - [ ] `DEVICE-CORRELATED`

---

## B. Historical notation being transferred

- direct source:
- Br2 notation exactly as printed:
- EG:HBr notation exactly as printed:
- temperature:
- published etch-rate metric:
- published anisotropy/profile metric:
- published roughness metric:
- direct concentration basis recovered? YES / NO
- direct EG:HBr basis recovered? YES / NO
- direct HBr assay recovered? YES / NO
- direct mixing order recovered? YES / NO
- direct bath volume recovered? YES / NO
- direct agitation recovered? YES / NO
- direct rinse/handoff recovered? YES / NO

If any answer is NO, do not enter an inferred historical preparation value.

---

## C. Convention evidence review

### Same-SSPL / overlapping-author evidence

- source ID:
- chemistry:
- explicitly stated concentration convention:
- relevance to candidate:
- limitation:

### Same-author review evidence

- source ID:
- entry/table:
- concentration convention stated:
- relevance:
- limitation:

### Counterexample evidence

- source ID:
- chemistry:
- alternate convention (`w/w`, `v/v`, other):
- implication:

### Other primary transfer evidence

- source ID:
- formulation convention:
- rinse/handoff evidence:
- limitation:

- resulting ranked hypothesis:
  - [ ] `CANDIDATE-VV-SAME-LAB`
  - [ ] `LOCAL-WW`
  - [ ] other explicitly defined branch
- rationale:

---

## D. Explicit local Br2 definition

- local Br2 basis:
  - [ ] `v/v`
  - [ ] `w/w`
  - [ ] `w/v`
  - [ ] molarity
  - [ ] other
- mathematical definition:
- denominator definition:
- target numerical value:
- final-batch definition:
- temperature/reference condition for volume quantities if relevant:
- calculation sheet/file ID:

### Actual delivered quantities

- Br2 actual delivered mass:
- Br2 actual delivered volume if used:
- final measured batch mass:
- final measured batch volume if used:
- deviation from target:

**Gate:** Is the Br2 fraction mathematically unambiguous? PASS / FAIL

---

## E. Explicit local EG:HBr definition

- ratio basis:
  - [ ] volume
  - [ ] mass
  - [ ] other
- mathematical definition:
- target ratio:
- EG delivered mass:
- EG delivered volume if used:
- HBr stock delivered mass:
- HBr stock delivered volume if used:
- resulting ratio:

**Gate:** Is `EG:HBr` mathematically unambiguous? PASS / FAIL

---

## F. Reagent genealogy

### Bromine

- supplier/product:
- lot:
- purity/assay:
- storage/open-date state:

### Ethylene glycol

- supplier/product:
- lot:
- purity:
- water specification:
- density if used:

### HBr stock

- supplier/product:
- lot:
- certified assay:
- assay basis:
- density if used:
- water/concentration state:
- bottle-open/storage state:

**Gate:** Are all formulation-relevant assays/grades explicit? PASS / FAIL

---

## G. Vessel / mixing genealogy

- institution-approved chemical procedure ID:
- vessel material/ID:
- nominal vessel volume:
- cover/seal state:
- preparation start time:
- reagent-addition order identifier:
- mixing method identifier:
- mixing duration:
- bath temperature during/after preparation:
- preparation end time:
- ready-for-use time:
- visible phase/color/anomaly:

Do not treat a different mixing order as the same branch until equivalence is demonstrated.

---

## H. Volatility / bath-age controls

- bath + vessel mass after preparation if measured:
- analytical free-Br2 proxy/method if available:
- initial analytical result:
- first-open time:
- cumulative open time before first sample:
- bath temperature:
- exposed liquid area/proxy:
- cover state between samples:
- maximum qualification bath age currently allowed:
- maximum sample/run count currently allowed:
- evidence supporting those limits:

A mass loss is not automatically Br2 loss unless analytically validated.

---

## I. Candidate comparison matrix

Use separate recipe IDs for chemically distinct concentration conventions.

| Branch | Br2 definition | EG:HBr definition | HBr assay | bath T | agitation | bath age | material lot | status |
|---|---|---|---|---:|---|---:|---|---|
| | | | | | | | | |
| | | | | | | | | |

Do not pool branches merely because each is called “2%.”

---

## J. Coupon bridge outputs

For each linked P28 diagnostic run record:

| Run | branch | actual T | R_V | R_L | A | roughness | resist state | isolation | P25 handoff | disposition |
|---|---|---:|---:|---:|---:|---:|---|---|---|---|
| | | | | | | | | | | |

Attach:

- depth-versus-time regression;
- undercut/profile images;
- roughness data;
- bath-age/run-order plot;
- electrical isolation data;
- companion Hall/material-preservation data where available.

---

## K. Rinse / quench / dry / air-exposure trajectory

- local handoff recipe ID:
- etch end timestamp:
- first quench/rinse medium:
- first transfer timestamp:
- subsequent rinse sequence ID:
- rinse end timestamp:
- wet-transfer or dry-transfer branch:
- dry method if applicable:
- dry timestamp:
- first air-exposure timestamp / duration:
- storage atmosphere/container:
- P25 start timestamp:
- `Δt_etch→P25`:
- no-air-exposure maintained where intended? YES / NO / NA
- deviation:

### P25 outcome

- P25 run ID:
- anodization induction / V(t) signature:
- oxide thickness/state:
- passivation anomaly:

**Gate:** P28→P25 handoff reproducible? PASS / FAIL / OPEN

---

## L. Historical-identity statement

Select all that apply:

- [ ] direct Srivastav Br2 percentage basis recovered
- [ ] direct Srivastav EG:HBr basis recovered
- [ ] direct Srivastav HBr assay recovered
- [ ] direct Srivastav mixing order recovered
- [ ] direct Srivastav agitation recovered
- [ ] direct Srivastav rinse/handoff recovered
- [ ] only same-lab/same-author convention evidence recovered
- [ ] local branch intentionally substitutes for unresolved history

Narrative:

---

## M. Readiness disposition

- Br2 definition gate: PASS / FAIL
- EG:HBr definition gate: PASS / FAIL
- HBr assay gate: PASS / FAIL
- genealogy/bath-age gate: PASS / FAIL
- coupon rate/profile gate: PASS / FAIL / OPEN
- through-layer isolation gate: PASS / FAIL / OPEN
- P25 handoff gate: PASS / FAIL / OPEN
- device-correlation gate: PASS / FAIL / NOT TESTED

### P16A R13

- `UNDEFINED-BASIS`
- `OPEN-CHOICE`
- `LOCAL-BRANCH-FROZEN`

Selected state:

Justification:

### P16A R14

- `OPEN-CHOICE`
- `LOCAL-BRANCH-FROZEN`

Selected state:

Justification:

### Overall P28A disposition

- [ ] `NOTATION-ONLY`
- [ ] `CONVENTION-CANDIDATE`
- [ ] `CHEMISTRY-DEFINED`
- [ ] `COUPON-RATE-PROFILE-QUALIFIED`
- [ ] `THROUGH-LAYER-ISOLATION-QUALIFIED`
- [ ] `P25-HANDOFF-QUALIFIED`
- [ ] `DEVICE-CORRELATED`

Approver/date:

---

## Non-negotiable notes

1. Same-SSPL `v/v` evidence supports a candidate; it does not redefine the Srivastav paper.
2. Leech et al. explicitly used `w/w` for another Br:HBr HgCdTe etchant; historical bromine notation is not universal.
3. A local `v/v` or `w/w` recipe is a new controlled branch until historical identity is directly demonstrated.
4. Matching `2.78 µm/min` alone does not establish chemical identity.
5. HBr stock assay and water content are formulation coordinates.
6. Bath age, exposed area, temperature and vessel state are chemistry genealogy because Br2 is volatile.
7. Post-etch rinse/air exposure is part of the surface state delivered to P25.
8. This scientific register does not replace institution-specific Br2/HBr/Hg/Cd chemical safety procedures.

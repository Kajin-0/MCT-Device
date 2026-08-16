# Research checkpoint — after wet-mesa chemistry basis Round 36

**Date:** 2026-08-16 America/New_York

## Round objective

Resolve, or bound without invention, the execution ambiguity behind the strongest quantitative wet-mesa transfer notation:

`2% Br2 / 3:1 EG:HBr / 21 °C`

from Srivastav et al. 2005, and integrate the result into P16A first-build readiness.

---

## Files created

- `procedures/P28A_WET_MESA_CHEMISTRY_DEFINITION_LINEAGE_ADDENDUM.md`
- `travelers/P28A_WET_MESA_CHEMISTRY_DEFINITION_QUALIFICATION_REGISTER.md`
- `docs/SOURCE_LEDGER_ADDENDUM_ROUND36.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND36.md`
- this checkpoint.

## File revised

- `travelers/P16A_FIRST_BUILD_READINESS_REGISTER.md`

AGENTS is refreshed at the end of the round.

---

# 1. Direct Srivastav paper did not close the concentration basis

The full accessible 2005 paper directly establishes:

- x=0.28 source HgCdTe;
- nominal Br2 series 1–3%;
- selected `2% Br2`;
- selected `3:1 EG:HBr` / `75% EG + 25% HBr` notation;
- 21 °C principal comparison condition;
- mean process-variation R_V≈2.78 µm/min;
- A≈0.63;
- best roughness near ~2 nm;
- strong temperature sensitivity;
- Br2 volatility/reproducibility concern.

It does not explicitly state:

- w/w, v/v, w/v or other Br2 basis;
- mass/volume basis of EG:HBr;
- HBr stock assay;
- mixing order;
- bath volume;
- actual agitation setting;
- patterned-mesa rinse/dry sequence.

Therefore the exact historical formulation remains unresolved.

---

# 2. Same-SSPL evidence materially changes the candidate ranking

A 2003-filed / 2005-published DRDO/SSPL primary patent, “A Process For Passivation Of Mercury Cadmium Telluride,” includes inventors Ravinder Pal and Vishnu Gopal and explicitly defines bromine/methanol concentrations in `v/v` terms.

Direct examples include:

- 0.5% (v/v) Br2/MeOH;
- 0.05% (v/v) Br2/MeOH.

This does not prove the Br2/HBr/EG mesa basis, but it upgrades a v/v local interpretation from generic speculation to:

`CANDIDATE-VV-SAME-LAB`.

A same-author 2005 review also expresses a Br2/methanol etch-rate relation against `[Br] in vol%`.

---

# 3. Counterexample prevents false closure

Leech/Gwynn/Kibel 1989 explicitly use:

`0.1% (w/w) Br:HBr`.

Thus primary HgCdTe literature used more than one percentage convention.

Permanent rule:

`unspecified Br2 % != automatically v/v`.

The Srivastav 2% notation remains `OPEN-HISTORICAL` even though v/v is now the strongest lineage-supported local candidate.

---

# 4. Rinse / handoff is now treated as a process trajectory

Same-SSPL primary evidence explicitly controls post-bromine rinsing and subsequent electrochemical-clean transfer without air exposure.

US4436580A independently uses a bromine/methanol etch followed by methanol quench, acetone/methanol rinse and immediate N2 drying.

These are different transfer branches, but together reinforce that:

`same etch depth != same delivered surface state`.

P28A now requires timestamps and state for:

- etch end;
- first quench/rinse;
- rinse end;
- wet or dry transfer;
- first air exposure;
- storage;
- P25 start.

---

# 5. Srivastav thesis remains a live archival target

Official IISc metadata identifies:

Vanya Srivastav, *Modelling, Fabrication and Characterization of HgCdTe Infrared Detectors for High Operating Temperatures*, 2012, repository handle `2005/3165`, file `G25544.pdf` (~19.27 MB).

Current retrieval result:

- metadata/abstract indexed;
- direct official page/file retrieval through available route returns 403;
- targeted indexed searches did not surface the formulation-preparation passage.

Do not write “thesis does not define the basis.”

Correct state:

`IDENTIFIED-NOT-RECOVERED`.

---

# 6. P28A local branch architecture

Allowed local chemistry branches must define mathematics explicitly.

Examples:

- volume branch: `phi_Br2 = V_Br2 / V_final` plus an independently explicit EG:HBr volume definition;
- mass branch: `w_Br2 = m_Br2 / m_final` plus an independently explicit EG:HBr definition.

The recipe must also record certified HBr stock assay and reagent genealogy.

Equal nominal `2%` values under different definitions are not pooled as one chemistry.

`CANDIDATE-VV-SAME-LAB` is the evidence-ranked first candidate if historical recovery still fails, but it is local qualification until direct proof exists.

---

# 7. P16A readiness consequence

Round 36 added a closure method, not a frozen laboratory recipe.

Therefore:

- R13 wet-mesa preparation basis = `UNDEFINED-BASIS`;
- R14 endpoint/rinse/passivation handoff = `OPEN-CHOICE`;
- `TRACEABLE-FIRST-BUILD-READY = NO`.

Required physical closure is now explicit:

1. select actual concentration mathematics;
2. select EG:HBr basis;
3. record HBr stock assay;
4. freeze bath vessel/mixing/temperature/agitation/age branch;
5. calibrate R_V/R_L/profile on x≈0.30 coupons;
6. demonstrate through-layer electrical isolation;
7. freeze the rinse/air-exposure/P25 trajectory;
8. verify P25 and downstream device state.

---

# 8. Negative / rejected inferences preserved

Rejected:

- `same-lab used v/v elsewhere -> Srivastav 2% must be v/v`;
- `75% EG / 25% HBr -> necessarily 75 mL + 25 mL`;
- `commercial HBr is commonly sold at a certain assay -> historical stock had that assay`;
- `matching 2.78 µm/min -> chemistry identity proven`;
- `same wet-etch depth -> same post-etch/passivation surface`.

---

# 9. Strongest next research direction

The next highest-value **source-recoverable** execution ambiguity should be selected from P16A rather than returning to wet-etch speculation.

Recommended Round 37 target:

**R17 / P08A-P24-P34 CH4/H2 gas-realization provenance and premix/split closure.**

Reason:

- R17 is still `UNDEFINED-BASIS`, the same severity as R13;
- RP-01 prints `CH4/5H2` with total flow 64 sccm, but the exact gas-delivery meaning must not be guessed;
- same-UWA RIE papers, Plasma Technology reactor literature, gas-cylinder premix conventions and earlier P08A evidence may permit a more documentary closure than apparatus-dependent R18.

Round 37 should first audit P08A/P08/P24/P34 and prior source ledgers before performing new searches. If the gas notation has already been exhausted, pivot to R15/P25 anodic-oxide cell/bath execution rather than duplicating prior work.

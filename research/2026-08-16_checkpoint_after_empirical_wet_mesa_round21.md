# Checkpoint — after empirical wet-mesa Round 21

**Date:** 2026-08-16 America/New_York  
**Round:** 21  
**Primary new module:** P28

## Why this round was performed

After empirical closure work on blocking contacts, native oxide, metallization and Mask-2 lithography, the next large practical fabrication gap was RP-01 mesa isolation.

The existing P01/P01A branch already contained a strong near-composition source (Srivastav et al. 2005), but it had a dangerous ambiguity: the selected etchant is written as `2% Br2 in 3:1 EG:HBr`, yet the primary article does not define how either percentage/ratio is physically prepared.

Round 21 therefore prioritized formulation provenance before adding more theoretical process modeling.

---

# Files created

- `procedures/P28_WET_MESA_EMPIRICAL_PROCESS_WINDOW.md`
- `travelers/P28_WET_MESA_EMPIRICAL_QUALIFICATION_REGISTER.md`
- `docs/SOURCE_LEDGER_ADDENDUM_ROUND21.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND21.md`
- this checkpoint

`AGENTS.md` is refreshed after this checkpoint.

---

# Canonical RP-01 wet-mesa closure

Direct RP-01 closes only:

- wet chemical mesa delineation;
- mesa occurs before anodic oxide;
- active HgCdTe layer ~9.5 µm.

No exact RP-01 wet chemistry/time/temperature/rinse/endpoint has been recovered.

---

# Same-UWA wet-mesa functional closure

Smith/Musca/Redfern/Dell/Faraone 2000 directly compared x=0.31 n-HgCdTe photoconductors processed by H2/CH4 RIE versus wet bromine/HBr mesa etching.

Important result:

- wet chemical devices reached background-limited performance in the reported 80-K / 3-µm / stated 60°-FOV comparison;
- reported wet `D_lambda*≈2.5×10^11 cm Hz^1/2 W^-1`;
- dry branch ~`1.0×10^10`.

The 1999 same-UWA mesa paper also reports no significant LBIC electrical-property modification for chemical etching relative to the strong RIE-induced modification.

Therefore wet mesa is strongly supported by same-laboratory device evidence even though the exact UWA formulation is missing.

---

# Srivastav x=0.28 process anchors

Full primary text re-read in Round 21 confirms:

Material/preparation:

- x=0.28 HgCdTe;
- SMALL Enterprises, Ukraine;
- wire saw;
- sapphire mount;
- decreasing alumina grit lap/polish;
- chemomechanical polish;
- nominal 0.1% Br2/methanol free etch / 1 min;
- Nomarski + Gartner ellipsometry at 6328 Å.

Test patterns:

- ~600-µm lines / 50-µm trenches;
- 2D mesas separated by 30-µm trenches.

DOE:

- nominal Br2 1–3%;
- EG fraction in HBr 0–1;
- selected nominal 2% Br2 / 3:1 EG:HBr;
- temperature 5–50 °C.

Selected-condition outputs:

- mean vertical rate ~2.78 µm/min;
- ~±26% rate variation;
- A~0.63, ~±11%;
- `A=1-R_L/R_V`;
- roughness ~2–7 nm, best ~2 nm;
- apparent activation energy ~7.5 kcal/mol;
- rate approximately doubles per +10 °C;
- higher temperature worsens edge quality/photoresist attack;
- 10 °C SEM example shows better feature control than the 21 °C example.

Mechanistic/process statements:

- Br2 concentration raises rate;
- EG raises viscosity/limits free bromine and slows rate;
- HBr is acidic dissolution medium;
- Br2 evaporation is a process-drift mechanism;
- agitation assists reaction-product transport in the viscous solution.

Still missing from accessible primary text:

- basis of 2% Br2;
- physical preparation basis of 3:1 EG:HBr;
- HBr stock assay;
- mixing order;
- actual experimental agitation method/rate;
- rinse/quench/dry.

---

# Central Round-21 finding — concentration convention cannot be inferred

The project previously knew the Srivastav percentage basis was not stated. Round 21 now provides stronger primary evidence that **historical HgCdTe bromine notation is not uniform**.

Leech/Gwynn/Kibel 1989 explicitly use:

`0.1% (w/w) Br:HBr`.

CN101740502B explicitly defines its Br2:HBr process by **volume proportion**.

US4436580A explicitly gives a bromine/methanol example as `2% bromine / 98% solution (V/V)`.

Therefore neither `2% Br2` nor `3:1 EG:HBr` may be converted into reagent quantities by convention.

Permanent rule:

**source notation remains symbolic until its basis is recovered.**

If a local formulation is required, assign it a new recipe ID with an explicit mathematical concentration definition.

---

# HBr stock assay is a separate blocker

The primary x=0.28 paper does not state the HBr stock concentration/assay.

Do not assume a commercial 48-wt% HBr solution or any other stock.

A local recipe records the supplier/lot/certified assay and keeps that chemical state under change control.

This matters because HBr assay changes acidity, water fraction, viscosity and reaction-product dissolution.

---

# Bath genealogy is now mandatory

Because Br2 evaporation is a direct source-study drift mechanism, P28 records:

- batch recipe and explicit concentration basis;
- reagent lots/assays;
- mixing order;
- vessel/cover state;
- preparation timestamp;
- bath temperature;
- preparation-to-use age;
- cumulative open-vessel time;
- sample run order;
- cumulative exposed/etched area;
- use/reuse state.

Multiple samples from one etchant batch are **not independent etchant-batch replicates**.

Optional local diagnostics include a validated free-Br2 analytical proxy and/or batch mass tracking. Total mass loss is only an evaporation diagnostic, not direct bromine-loss metrology without a validated model.

---

# Agitation status

The Srivastav mechanism states that agitation of the viscous solution helps transport reaction products, but the actual agitation method/rate used for the published quantitative results is not specified.

Therefore:

- agitation relevance = directly supported;
- historical agitation state/rate = `OPEN`.

Local static/stirred/holder-motion branches require explicit recipe IDs and new rate calibration.

---

# Endpoint rule strengthened

The arithmetic:

`9.5 µm / 2.78 µm min^-1 ≈ 3.42 min`

remains diagnostic only.

Using source ±26% rate variation gives a rough 9.5-µm timing scale of about:

- ~2.71 min at the fast edge;
- ~4.62 min at the slow edge,

before overetch and transfer differences.

Permanent rule:

**time is an input; physical through-layer isolation is the output.**

P28 uses:

- measured incoming local HgCdTe thickness;
- measured etch depth;
- lateral undercut/profile;
- electrical mesa-to-mesa isolation;
- overetch only after substrate-interface crossing is established.

No generic overetch fraction is released.

---

# Rinse/quench remains legitimately open

No matched primary source recovered the Srivastav/RP-01 Br2/EG/HBr rinse.

Other primary branches are chemically different:

- one Br2/HBr micro-mesa patent uses DI-water cleaning;
- bromine/methanol/DMF processing uses chemistry-specific methanol/DMF quenching followed by solvent rinse/N2 dry.

This proves rinse is a process variable rather than a generic final step.

P28 requires a locally qualified rinse/quench recipe but does not label DI water, methanol or acetone as the historical UWA/Srivastav sequence.

---

# Post-etch surface / P25 handoff

Srivastav reports negligible apparent composition change by its ellipsometric metric for Br2/EG/HBr, while Br2/HBr without EG appeared probably Te-rich. This is explicitly qualitative.

Independent primary HgCdTe surface work shows Br-based etching can leave elemental Te, which oxidizes in air and affects surface recombination.

Therefore P28 records:

- etch-end time;
- rinse/dry time;
- atmosphere/storage;
- `t_etch_to_P25`;
- physical/surface witness data;
- P25 anodization `V(t)`/induction behavior.

The mesa/passivation interface is one continuous process boundary.

---

# Practical local replication sequence after Round 21

1. Define an explicit local formulation recipe; do not reinterpret the historical 2% notation.
2. Record certified HBr assay and reagent lots.
3. Prepare a fresh controlled batch with fixed vessel/mixing/cover protocol.
4. Equilibrate and measure bath temperature.
5. Establish `R_V` and `R_L` on matched x≈0.30 coupons for that exact batch state.
6. Measure anisotropy, roughness and resist survival.
7. Establish bath-age/run-order sensitivity.
8. Use measured incoming HgCdTe thickness for through-layer planning.
9. Etch device structures under the calibrated condition.
10. Execute a separately identified qualified rinse/quench.
11. Measure depth/profile and electrical isolation.
12. Record surface/air history and transfer promptly/consistently into P25.
13. Close with downstream passivation/contact/noise/responsivity tests.

---

# Negative source recovery retained

Vanya Srivastav's IISc thesis is identified in the institutional repository:

*Modelling, Fabrication and Characterization of HgCdTe Infrared Detectors for High Operating Temperatures*, file `G25544.pdf`.

The current web route exposes the thesis record but not the full experimental process text needed to close the concentration/rinse questions.

Status:

`PRIMARY-THESIS-IDENTIFIED / FULL-PROCESS-TEXT-NOT-RECOVERED`.

Do not infer that the missing details are absent from the thesis.

---

# Recommended next empirical branch

After P28, the next strongest practical recovery target should be selected by available primary evidence. Leading candidates:

1. **P07 CdZnTe substrate face/orientation/miscut/final-surface preparation**, because interface quality upstream of LPE remains incompletely specified;
2. **P04 Hg anneal apparatus / Hg reservoir geometry / actual pHg-control process**, if primary patents/theses can recover real hardware and trajectories;
3. **Mask-1 mesa lithography**, especially if same-lineage wet-mesa sources reveal actual resist/strip compatibility with Br/HBr.

Maintain empirical-source-first priority. Do not return to abstract tolerance modeling while an executable fabrication detail is recoverable from primary literature.

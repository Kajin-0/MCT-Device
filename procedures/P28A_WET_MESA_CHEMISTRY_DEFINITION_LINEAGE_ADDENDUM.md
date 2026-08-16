# P28A — wet-mesa chemistry-definition / lineage / handoff addendum

**Status:** CONTROLLED EMPIRICAL CLOSURE METHOD / PRE-FIRST-BUILD  
**Date:** 2026-08-16 America/New_York

## 1. Purpose

Close the specific formulation-definition gap in P01/P01A/P28 without converting an ambiguous historical percentage into an invented recipe.

The source center is V. Srivastav et al., *Journal of Electronic Materials* 34 (2005) 1440–1445, DOI `10.1007/s11664-005-0203-5`:

- x = 0.28 HgCdTe;
- nominal `2% Br2`;
- `3:1 EG:HBr`, also represented as `75% EG / 25% HBr`;
- reference condition near `21 °C`;
- measured mean vertical rate about `2.78 µm/min` in the process-variation set;
- mean anisotropy about `0.63`;
- best roughness near `2 nm`.

The unresolved question is not whether these words and measured outputs were published. They were. The unresolved question is **what laboratory preparation operation those concentration symbols encoded**.

P28A therefore separates:

`published notation -> convention evidence -> local mathematical definition -> reagent assay -> bath genealogy -> coupon outputs -> P25 handoff`.

P28A supplements P28. It does not replace the P28 etch-rate/profile/isolation qualification method.

---

# 2. Evidence classes used in this addendum

## `PRIMARY-X028-MESA`

Direct Srivastav et al. 2005 x=0.28 mesa paper.

## `SAME-SSPL-CONVENTION`

Primary HgCdTe process evidence from Solid State Physics Laboratory (SSPL) with overlapping authors/laboratory lineage, sufficiently close in time to inform notation practice but not identical in chemistry.

## `SAME-AUTHOR-REVIEW`

Srivastav/Pal/Vyas 2005 review evidence describing concentration conventions across HgCdTe wet-etch literature.

## `PRIMARY-CONVENTION-COUNTEREXAMPLE`

Primary HgCdTe literature explicitly using another concentration convention, demonstrating that no universal historical convention may be assumed.

## `PRIMARY-RINSE-HANDOFF-TRANSFER`

Primary HgCdTe process evidence for quench/rinse/dry or no-air-exposure handling, but not direct proof of the Srivastav/RP-01 mesa handoff.

## `CANDIDATE-VV-SAME-LAB`

A ranked local candidate based on same-laboratory convention evidence. This is **not** a historical fact.

## `LOCAL-QUAL`

Explicitly defined local chemistry/process branch requiring P28 qualification data.

## `OPEN-HISTORICAL`

Not recovered from the direct historical source.

---

# 3. Direct Srivastav formulation audit

The accessible full primary paper repeatedly uses:

- `1–3% Br2`;
- selected `2% Br2`;
- `3:1 EG:HBr`;
- `75% EG / 25% HBr` in a figure description;
- nominal `0.1% Br2 in methanol` during source-material surface preparation.

The recovered text does **not** state:

- `w/w`, `v/v`, `w/v`, molarity or mole fraction for the Br2 number;
- delivered Br2 mass or volume;
- final solution mass or volume;
- whether the Br2 denominator is final solution, pre-mixed EG:HBr carrier, or another laboratory convention;
- whether `3:1 EG:HBr` is a mass ratio or volume ratio;
- HBr stock assay/concentration;
- reagent-addition order;
- numerical bath volume;
- actual agitation method/rate for the reported `2.78 µm/min` process-variation data;
- an executable rinse/quench/dry sequence after patterned mesa etching.

Therefore:

`Srivastav 2% Br2 = OPEN-HISTORICAL concentration basis`  
`Srivastav 3:1 EG:HBr = OPEN-HISTORICAL ratio basis`.

No later inference in this file changes those evidence states.

---

# 4. Vanya Srivastav thesis recovery state

Official IISc repository metadata identifies:

Vanya Srivastav, *Modelling, Fabrication and Characterization of HgCdTe Infrared Detectors for High Operating Temperatures*, thesis, 2012; repository item `handle/2005/3165`; file `G25544.pdf`, approximately 19.27 MB.

Round-36 search result:

- official metadata/abstract are indexed;
- direct access to the repository item/full file from the available retrieval path returned HTTP 403;
- targeted searches for `Br2`, `HBr`, `EG`, `v/v`, and the 3:1 formulation did not expose the relevant thesis experimental passage.

Disposition:

`THESIS-FULL-TEXT = IDENTIFIED / NOT RECOVERED THROUGH CURRENT ACCESS PATH`.

This is a negative access result, not evidence that the thesis lacks the required preparation detail.

---

# 5. Same-SSPL convention evidence — important but not direct closure

A primary Indian patent from the same SSPL laboratory, filed in 2003 and published in 2005, **“A Process For Passivation Of Mercury Cadmium Telluride,”** lists inventors including Ravinder Pal and Vishnu Gopal. Gopal is an author of the Srivastav mesa paper and the work is from the same SSPL HgCdTe process environment.

That patent explicitly specifies bromine/methanol concentrations as **volume/volume**:

- chemo-mechanical polishing/free-etch family: `0.1–1%`, preferably `0.4–0.6% (v/v) Br2/MeOH`;
- working example: `0.5% (v/v) Br2/MeOH`;
- second free-etch step: `0.01–0.1%`, preferably `0.03–0.07% (v/v)`;
- working example: `0.05% (v/v) Br2/MeOH`.

It also directly states a handling sequence including methanol rinse and a no-air-exposure handoff into subsequent electrochemical cleaning.

### Interpretation

This establishes that the same laboratory/overlapping-author process culture explicitly used **v/v notation for liquid Br2 solutions** in the same period.

It does **not** establish that:

`Srivastav 2% Br2/HBr/EG = 2% v/v`.

The correct evidence upgrade is only:

`v/v hypothesis: generic guess -> SAME-SSPL-CONVENTION-SUPPORTED CANDIDATE`.

The historical basis remains open.

---

# 6. Same-author review evidence

Srivastav, Pal and Vyas, *Opto-Electronics Review* 13(3) (2005) 197–211, summarizes HgCdTe wet etchants.

Its wet-etch table includes a Br2/methanol entry with an etch-rate relation expressed against `[Br] in vol%`.

The same table separately lists:

- `Br2/HBr (1–5%)`;
- `Br2/HBr/ethylene glycol (in various ratios)`.

The table does **not** explicitly label the HBr/EG entry's percentage basis.

### Interpretation

This independently reinforces that Srivastav's laboratory/authors were comfortable expressing bromine concentration in volume percent in contemporaneous HgCdTe work.

It still does not close the exact 2% Br2/HBr/EG notation.

---

# 7. Primary counterexample — concentration convention was not universal

Leech, Gwynn and Kibel, *Applied Surface Science* 37 (1989) 291–298, DOI `10.1016/0169-4332(89)90491-1`, explicitly compare against:

`0.1% (w/w) Br:HBr`.

Therefore HgCdTe bromine literature demonstrably includes explicit **weight/weight** conventions.

This counterexample prohibits the inference:

`Br2 percentage in HgCdTe literature -> automatically v/v`.

---

# 8. Other primary volume-based branches

Two additional process families strengthen the conclusion that v/v is physically plausible but chemistry-specific:

1. US4436580A explicitly describes a bromine/methanol dip as `2% bromine / 98% solution (V/V)` and then methanol quench, acetone/methanol rinse and immediate dry nitrogen.
2. US5880510A describes a bromine/ethylene-glycol HgCdTe surface etch with bromine typically `0.25% by volume` for about 1–2 min.

These are `PRIMARY-CONVENTION/RINSE-TRANSFER` only.

Neither identifies the Srivastav Br2/HBr/EG preparation.

---

# 9. Permanent formulation rule

The source notation shall remain:

`2% Br2 / 3:1 EG:HBr`

when discussing the historical Srivastav result.

It shall **not** be silently rewritten as:

- 2 vol%;
- 2 wt%;
- 2 g/100 mL;
- a molarity;
- 75 mL EG + 25 mL HBr;
- any specific HBr stock assay.

A numerical laboratory recipe exists only after a local recipe ID defines the mathematics.

---

# 10. Local concentration definitions

P28A permits controlled local branches. The definition itself must be part of the recipe revision.

## 10.1 `P28A-LOCAL-VV-*`

If a volume-based branch is selected, define explicitly, for example:

`phi_Br2 = V_Br2 / V_final`

and separately define the carrier ratio, for example:

`r_EG:HBr = V_EG / V_HBr`.

The recipe must state the denominator convention and whether `V_final` is measured/final-volume adjusted or defined by delivered-component volumes.

This branch may be tagged `CANDIDATE-VV-SAME-LAB` during initial transfer because of Sections 5–6. It may not be tagged `PRIMARY-X028-MESA` for the preparation basis.

## 10.2 `P28A-LOCAL-WW-*`

For a mass-based branch, define explicitly:

`w_Br2 = m_Br2 / m_final`.

Define the EG:HBr ratio independently by mass or volume; do not leave the second ratio implicit.

## 10.3 Other branches

A `w/v`, molarity, or other branch is permitted only if its mathematical definition is unambiguous and it receives a separate recipe ID.

### Core rule

Equal nominal numerical percentages under different definitions are **not equal chemical states**.

Do not merge their etch-rate data into one calibration curve.

---

# 11. HBr stock assay is part of the chemistry

The historical Srivastav HBr stock concentration remains `OPEN-HISTORICAL`.

For every local recipe record:

- supplier/product/lot;
- certified HBr assay and assay basis;
- density when required by the selected formulation mathematics;
- water content or supplied concentration state where available;
- bottle-open/storage genealogy;
- actual delivered amount.

A commercial concentration such as a commonly available HBr assay must **not** be backfilled as historical fact.

Changing HBr stock concentration while retaining the same nominal `3:1 EG:HBr` notation is a chemistry change.

---

# 12. Bath genealogy and Br2 volatility

Srivastav directly identifies bromine volatility/concentration drift as an important contributor to process variability.

Therefore every local bath must record:

- preparation start/end;
- vessel material/ID;
- covered/sealed/open state;
- bath exposed surface geometry where material;
- temperature;
- time to first sample;
- cumulative open time;
- sample run order;
- cumulative exposed HgCdTe area;
- reuse state;
- actual reagent lots/amounts;
- optional bath/vessel mass change;
- optional analytical free-Br2 proxy.

A bath mass loss may diagnose volatility but shall not be converted directly into Br2 concentration loss without an independently validated composition measurement/model.

---

# 13. Mixing order remains a local controlled variable

No recovered matched primary source closes the Srivastav Br2/HBr/EG reagent-addition order.

Because concentrated acid, bromine and glycol mixing can change temperature and local reaction state, order is a controlled recipe coordinate rather than an operator preference.

P28A does not prescribe hazardous chemical handling. The actual sequence must be defined in the institution-approved laboratory procedure and then held fixed during process qualification.

A change in mixing order reopens chemistry equivalence unless validated.

---

# 14. Rinse / no-air-exposure / passivation handoff evidence

The exact Srivastav patterned-mesa rinse and the exact RP-01 wet-mesa-to-anodization handoff remain open.

However, primary transfer evidence shows that the handoff can be physically important:

- the same-SSPL passivation patent rinses bromine/methanol-treated HgCdTe in methanol and then running DI water and directs transfer into electrochemical cleaning without air exposure;
- US4436580A uses methanol quench until bromine is removed, acetone/methanol rinse and immediate dry N2 before the next process.

These are not interchangeable recipes, but both establish the same control principle:

`etch endpoint -> quench/rinse -> dry or wet transfer -> air exposure -> next surface/passivation step`

must be recorded as a trajectory.

P28/P25 shall therefore retain:

`t_etch_end`, `t_quench`, `t_rinse_end`, `t_dry`, `t_P25_start`, atmosphere/storage state, and visible/surface-analysis condition where available.

Do not assume that two mesas with the same depth are equivalent after different post-etch exposure histories.

---

# 15. Ranked local transfer strategy

If the historical basis remains unrecovered, the first local transfer shall not be described as “reproducing Srivastav.”

The evidence-ranked strategy is:

1. freeze a `CANDIDATE-VV-SAME-LAB` recipe definition because contemporaneous SSPL/overlapping-author evidence explicitly uses v/v for liquid Br2 solutions;
2. record the actual HBr assay and define the EG:HBr ratio mathematically;
3. establish a fresh-bath genealogy and one reproducible local mixing/handling branch under institutional chemistry controls;
4. calibrate on matched x≈0.30 coupons before a through-layer device etch;
5. use `21 °C` as the principal literature comparison coordinate, not as an automatic optimum;
6. retain a lower-temperature diagnostic point such as the published `10 °C` morphology branch when useful;
7. measure both vertical and lateral transfer, not blanket removal alone;
8. carry the resulting surface directly into a controlled P25 handoff study;
9. compare an alternative explicitly defined concentration convention only if needed to discriminate the historical notation or improve process performance.

The first candidate is evidence-ranked, not historically proven.

---

# 16. Minimum coupon bridge before a 9.5-µm device mesa

For each candidate chemistry branch use diagnostic Mask-1 structures sufficient to measure:

- `R_V` from multiple depth/time points;
- `R_L` from undercut;
- anisotropy `A = 1 - R_L/R_V`;
- profile/edge morphology;
- RMS roughness;
- photoresist survival;
- bath-age/run-order drift;
- complete electrical isolation at the substrate interface;
- companion Hall/material preservation where feasible;
- P25 anodization response after a controlled handoff.

A candidate chemistry does not advance to the actual RP-01-like through-layer device branch merely because one coupon gives approximately `2.78 µm/min`.

Matching one etch-rate number is not chemical identity.

---

# 17. Qualification dispositions

Use the following evidence states:

- `NOTATION-ONLY` — historical symbols known, preparation basis unknown;
- `CONVENTION-CANDIDATE` — local definition supported by lineage but not direct historical proof;
- `CHEMISTRY-DEFINED` — all concentration/ratio/stock-assay mathematics are explicit;
- `COUPON-RATE-PROFILE-QUALIFIED` — local R_V/R_L/profile/roughness response measured;
- `THROUGH-LAYER-ISOLATION-QUALIFIED` — complete isolation demonstrated on representative thickness/geometry;
- `P25-HANDOFF-QUALIFIED` — post-etch state transfers reproducibly into passivation;
- `DEVICE-CORRELATED` — downstream electrical/noise/responsivity performance linked to the same chemistry genealogy.

Only a physically instantiated local branch can become `CHEMISTRY-DEFINED` or higher.

---

# 18. P16A readiness consequence

Round 36 closes a **methodological and evidence-ranking gap** but does not physically freeze R13/R14.

Current state remains:

- R13 `UNDEFINED-BASIS` until an actual local recipe selects and records a mathematical concentration definition, EG:HBr definition and HBr assay;
- R14 `OPEN-CHOICE` until bath T/agitation/age, endpoint, rinse/dry and P25 elapsed-time handoff are physically frozen.

Therefore:

`TRACEABLE-FIRST-BUILD-READY = NO`.

The important improvement is that R13 no longer requires guessing what the literature meant: P28A now provides an evidence-ranked route to an explicitly local branch while preserving the unresolved historical notation.

---

# 19. Persistent historical gaps

Still open:

- direct basis of Srivastav `2% Br2`;
- direct basis of `3:1 EG:HBr`;
- Srivastav HBr stock assay;
- exact reagent-addition order;
- exact reported-run bath volume;
- exact agitation implementation;
- exact patterned-mesa rinse/dry sequence;
- direct UWA/RP-01 wet-mesa formulation;
- exact UWA/RP-01 wet-mesa-to-anodization elapsed-time/ambient trajectory;
- full relevant experimental text of Srivastav's IISc thesis through the current access path.

“Not recovered” does not mean nonexistent.

---

# 20. Primary sources

1. V. Srivastav et al., “Etching of Mesa Structures in HgCdTe,” *Journal of Electronic Materials* 34, 1440–1445 (2005), DOI `10.1007/s11664-005-0203-5`.
2. V. Srivastav, R. Pal, H. P. Vyas, “Overview of etching technologies used for HgCdTe,” *Opto-Electronics Review* 13(3), 197–211 (2005).
3. “A Process For Passivation Of Mercury Cadmium Telluride,” Director General, DRDO, India; filed 10 Nov 2003; publication 45/2005; inventors include R. Pal and V. Gopal, SSPL.
4. P. W. Leech, P. J. Gwynn, M. H. Kibel, “A selective etchant for Hg1−xCdxTe, CdTe and HgTe on GaAs,” *Applied Surface Science* 37, 291–298 (1989), DOI `10.1016/0169-4332(89)90491-1`.
5. US4436580A, “Method of preparing a mercury cadmium telluride substrate for passivation and processing.”
6. US5880510A, “Graded layer passivation of group II-VI infrared photodetectors.”
7. V. Srivastav, *Modelling, Fabrication and Characterization of HgCdTe Infrared Detectors for High Operating Temperatures*, IISc thesis, 2012, repository handle `2005/3165`, file `G25544.pdf` — full relevant text not recovered in Round 36.

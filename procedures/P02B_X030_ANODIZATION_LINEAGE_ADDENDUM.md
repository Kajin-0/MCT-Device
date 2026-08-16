# P02B — x≈0.30 anodic-oxidation lineage addendum

**Status:** COMPOSITION-MATCHED PRIMARY-LINEAGE SUPPORT / EXECUTABLE RP-01 RECIPE STILL NOT CLOSED. Supplements `P02_ANODIC_OXIDE_QUALIFICATION.md` and `P02A_ANODIC_OXIDE_LINEAGE_ADDENDUM.md`.

## 1. Purpose

Strengthen the RP-01 anodic-oxide branch with primary literature on n-type Hg0.70Cd0.30Te, which is compositionally much closer to RP-01 (`x≈0.30`) than the commonly cited x≈0.20 anodization studies.

This addendum deliberately separates:

- statements recovered directly from the 1982 Janousek/Carscallen primary papers/abstracts;
- detailed experimental conditions recovered through Robert T. Talasek's later technical synthesis of those papers;
- directly executable TI patent conditions already captured in P02.

Do not collapse those evidence grades.

## 2. Primary composition-matched source

B. K. Janousek and R. C. Carscallen, “The mechanism of (Hg,Cd)Te anodic oxidation,” *Journal of Applied Physics* 53(3), 1720–1726 (1982).

A second same-author 1982 paper is indexed as:

R. C. Carscallen and B. K. Janousek, “Hg0.70Cd0.30Te anodic oxidation,” *Journal of Vacuum Science & Technology* 21 (1982).

The exact page/DOI metadata should be checked against the publisher record before final bibliography release; the composition and title are well identified in the literature trail.

## 3. What the primary literature directly establishes

The Janousek/Carscallen work directly reports that HgCdTe anodic oxidation proceeds through an initial **dissolution–precipitation mechanism**, followed by bulk oxide growth.

Primary conclusions include:

- initial film formation is governed by electrochemical/mass-transport variables rather than being a purely field-driven barrier-oxide process from t=0;
- stirring during the initial dissolution stage can suppress film formation at sufficiently low current density by increasing transport of dissolved species away from the anode;
- increasing solution pH increases oxide solubility and allows semiconductor dissolution to persist to higher current density;
- the initial surface/oxide formation history affects the later HgCdTe/oxide electronic interface;
- an electroetch integrated into the passivation process can reduce oxide fixed charge, plausibly by removing the TeO2-rich surface film left after bromine/methanol treatment.

These points are highly relevant to RP-01 because they show that `current density`, `agitation`, `pH/electrolyte composition`, and the **starting surface state** are all process variables.

## 4. Composition match

The electrochemical study summarized in the primary lineage used:

- n-type material;
- slush-grown HgCdTe;
- `x=0.30`.

This is the strongest composition-matched anodic-oxidation lineage found so far for RP-01.

It is still a different growth family from the RP-01 LPE epilayer. Thus composition match does not automatically close interface equivalence.

## 5. Detailed experimental conditions recovered through Talasek's technical synthesis

Robert T. Talasek's chapter “Electrochemical Passivation of (Hg,Cd)Te” in *Electrochemistry of Semiconductors and Electronics* explicitly attributes the following constant-current experiment to Janousek and Carscallen (its reference 32):

- n-type slush-grown `x=0.30` material;
- extensive pre-anodization etch in nominal `5% Br2 in methanol`;
- approximately `20 µm` of semiconductor removed by that etch;
- electrolyte `0.1 N KOH in 90% ethylene glycol / 10% water`;
- constant-current anodization at several current densities;
- voltage-versus-time curves exhibit an **induction period** during which potential is approximately time-independent;
- at sufficiently low current density, the induction period can become effectively infinite, i.e. dissolution continues without stable oxide precipitation;
- stirring can prevent oxidation at low current density by enhancing removal of dissolved species.

### Evidence-grade warning

The bullet values above are currently recovered from Talasek's later technical synthesis of the Janousek/Carscallen experiment, not from a full re-read of the 1982 primary article.

Tag them:

`[SECONDARY-A / EXPLICITLY ATTRIBUTED TO COMPOSITION-MATCHED PRIMARY]`.

They materially support process-family selection, but they should not be relabeled `[P]` until the primary article's experimental section is acquired.

## 6. Relation to the TI 800-Å process

The existing P02 transfer candidate from the Catagnus/Baker TI patent directly discloses:

- `0.1 M KOH`;
- `90% ethylene glycol / 10% DI water`;
- constant-current density near `0.3 mA/cm²`;
- termination near `15 V`;
- approximately `2 min`;
- approximately `800 Å` native oxide.

The Janousek/Carscallen x=0.30 lineage independently places the same alkaline EG/water electrolyte family on composition-matched HgCdTe.

This significantly strengthens the physical/process plausibility of using the TI process as the **center of a local x≈0.30 qualification DOE**, while still not proving that UWA's RP-01 used the exact TI traveler.

## 7. Critical mechanistic implication: do not use elapsed time as the primary endpoint

Because the x=0.30 primary lineage shows an induction period that depends on mass transport/current density, a fixed `2 min` exposure is not intrinsically transferable between:

- different cell geometries;
- different sample areas;
- stirred vs unstirred baths;
- different surface-preparation histories;
- different bath temperatures/compositions;
- different current densities.

Therefore the controlled P02 process should record the complete voltage-time trace and use oxide thickness / formation voltage / interface outcome as state variables.

For local qualification define:

- `t_ind` = induction time before sustained oxide-growth voltage rise;
- `dV/dt` during the growth regime;
- terminal formation voltage;
- total charge per unit area `Q/A = ∫J dt`;
- independent final oxide thickness;
- post-growth electrical/interface metrics.

A process run with anomalous `t_ind` is a surface/chemistry diagnostic even if the final oxide happens to measure ~80 nm.

## 8. Agitation is now a controlled P02 variable

The composition-matched mechanistic literature shows agitation can alter whether oxide nucleation/precipitation occurs.

Therefore P02 must explicitly record:

- stirred vs unstirred;
- agitation method;
- rotation/stirring rate if used;
- electrode/sample orientation;
- cell spacing and geometry.

Do not treat agitation as an incidental operator detail.

For initial RP-01 transfer, an **unstirred** cell is the better-controlled starting condition because the directly executable TI-family disclosures use static/unstirred anodization and because agitation changes the mechanism. This is a project selection for qualification, not a recovered UWA historical fact.

## 9. Surface-preparation warning

The x=0.30 mechanistic study's ~20-µm removal using 5% Br2/methanol is far too aggressive to transplant automatically into an RP-01 9.5-µm LPE device layer.

It is evidence about oxide mechanism on a prepared bulk/slush-grown surface, not an RP-01 surface-prep recipe.

For RP-01:

- preserve the existing LPE film thickness;
- use P01/P07-compatible minimal-damage surface preparation;
- qualify the starting oxide/surface state independently;
- do not remove tens of micrometers from a 9.5-µm epilayer.

## 10. Proposed local P02 qualification center

A rational first local transfer DOE may use the directly published TI center:

- electrolyte family `0.1 M KOH / 90% EG / 10% water`;
- constant-current operation near `0.3 mA/cm²`;
- static bath at recorded room temperature;
- target formation voltage near `15 V`;
- independent target thickness near `80 nm`.

But release must be based on measured response, not on blindly reproducing those controller numbers.

For every split record:

1. sample composition / electrical state / surface history;
2. exposed area;
3. bath batch and age;
4. current density;
5. voltage-time trace;
6. induction time;
7. integrated charge per area;
8. terminal voltage;
9. oxide thickness;
10. color/visual uniformity;
11. post-passivation sheet/electrical behavior;
12. compatibility with P08 oxide opening and P12 1/f-noise performance.

## 11. Release state after this addendum

### Stronger than before

- The KOH/EG/water constant-current family is now supported not only by TI/x≈0.20 work but by a **composition-matched x=0.30 primary mechanistic lineage**.
- Agitation, induction time, and starting-surface condition are promoted to mandatory controlled variables.

### Still open

- exact UWA RP-01 electrolyte/current/endpoint/rinse;
- primary full-text current-density values and exact cell configuration in Janousek/Carscallen 1982;
- exact 90:10 preparation convention (volume basis should not be assumed without source confirmation in the final production traveler);
- RP-01 rinse/dry and clean-to-next-step interval;
- local interface/noise acceptance limits.

The correct status remains `QUALIFICATION-CANDIDATE`, not `CLOSED-P RP-01`.

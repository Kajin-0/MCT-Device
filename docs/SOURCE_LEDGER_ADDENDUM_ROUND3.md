# Source ledger addendum — source-recovery round 3

**Date:** 2026-08-15 America/New_York

This addendum records sources promoted or materially reinterpreted during source-recovery round 3. Read with `docs/SOURCE_LEDGER.md` and prior addenda.

## S-R3-01 — Srivastav et al. 2005 full experimental text

**Class:** Primary-A  
**Citation:** V. Srivastav, R. Pal, B. L. Sharma, A. Naik, D. S. Rawal, V. Gopal, H. P. Vyas, “Etching of Mesa Structures in HgCdTe,” *Journal of Electronic Materials* 34, 1440–1445 (2005).  
**DOI:** `10.1007/s11664-005-0203-5`

**Role:** Best current quantitative near-composition transfer source for P01 wet-mesa development.

**Newly extracted direct details:**

- material `x=0.28`;
- wire-saw dice, sapphire mounting, mechanical lapping/polishing, chemomechanical polishing;
- nominal 0.1% Br2/methanol free etch for 1 min before patterned studies;
- Nomarski and 6328-Å ellipsometric surface screening;
- test masks with 50-µm linear trenches and 30-µm 2-D trenches;
- Br2/HBr/EG matrix, selected nominal 2% Br2 in 3:1 EG:HBr;
- 21 °C reference rate ~2.78 µm/min, ~±26% source variation;
- anisotropy ~0.63 ±11%;
- best RMS roughness ~2 nm;
- activation energy ~7.5 kcal/mol;
- approximate rate doubling per +10 °C;
- Br2 evaporation/concentration drift identified as a process-reproducibility issue;
- Dektak vertical-depth metrology and phase-contrast lateral-undercut metrology.

**Critical negative result:** the accessible full primary text does **not** define the percentage basis for 0.1%, 1–3%, or selected 2% Br2. This is a genuine source omission, not merely an abstract/indexing loss.

**Procedure:** `procedures/P01A_SRIVASTAV_PRIMARY_EXPERIMENTAL_ADDENDUM.md`.

## S-R3-02 — Janousek & Carscallen 1982 — mechanism of HgCdTe anodic oxidation

**Class:** Primary-A  
**Citation:** B. K. Janousek, R. C. Carscallen, “The mechanism of (Hg,Cd)Te anodic oxidation,” *Journal of Applied Physics* 53(3), 1720–1726 (1982).

**Role:** Composition-matched (`x≈0.30`) primary mechanistic anchor for P02.

**Direct conclusions recovered through publisher/indexed abstract and cross-citation:**

- initial HgCdTe anodic-oxide formation proceeds by dissolution–precipitation;
- later bulk growth follows;
- stirring/mass transport can suppress initial film formation;
- initial electrochemical conditions affect final interface electronic behavior;
- integrating an electroetch with passivation can reduce fixed charge associated with the Br2/methanol-treated starting surface.

**Use restriction:** detailed electrolyte/current/pre-etch conditions currently used in P02B are explicitly identified as coming from Talasek's later technical synthesis of this experiment unless/until the complete primary experimental section is acquired.

## S-R3-03 — Carscallen & Janousek 1982 — Hg0.70Cd0.30Te anodic oxidation

**Class:** Primary-A  
**Citation:** R. C. Carscallen, B. K. Janousek, “Hg0.70Cd0.30Te anodic oxidation,” *Journal of Vacuum Science & Technology* 21 (1982). Exact final page/DOI metadata still to be verified against publisher archive before bibliography freeze.

**Role:** Same-author composition-explicit companion source supporting the P02 x≈0.30 anodization lineage.

**Direct abstract-level findings:**

- dissolution–precipitation initial mechanism;
- stirring can prevent film formation at low current density;
- higher pH increases oxide solubility and permits continued semiconductor dissolution to higher current density;
- electroetch/passivation sequence can reduce oxide fixed charge by removing the TeO2-rich film left by Br2/methanol surface treatment.

## S-R3-04 — Talasek 1992 — electrochemical passivation synthesis

**Class:** Secondary-A / technical synthesis  
**Citation:** Robert T. Talasek, “Electrochemical Passivation of (Hg,Cd)Te,” in J. McHardy and F. Ludwig (eds.), *Electrochemistry of Semiconductors and Electronics*, 1992.

**Role:** Source map and explicit reconstruction of older primary HgCdTe anodization experiments.

**High-value attribution to Janousek/Carscallen reference 32:**

- n-type slush-grown `x=0.30`;
- nominal 5% Br2/methanol pre-etch, approximately 20 µm material removal;
- electrolyte 0.1 N KOH in 90% EG / 10% water;
- constant-current voltage–time measurements at multiple current densities;
- induction period before stable passivation;
- sufficiently low current may yield an effectively infinite induction period;
- stirring can prevent oxidation at low current density.

**Use restriction:** these detailed conditions remain `[SECONDARY-A explicitly attributed to primary]`, not `[P]`, because the complete Janousek/Carscallen primary experimental section has not been directly recovered.

**Additional mechanistic value:** the chapter documents mass-transport effects, pH/KOH sensitivity, and comparative constituent dissolution rates; use as physical-process context, not to overwrite primary-source setpoints.

## S-R3-05 — Catagnus & Baker / Texas Instruments native oxide process

**Class:** Primary-B  
**Citation:** P. C. Catagnus, C. T. Baker, “Passivation of mercury cadmium telluride semiconductor surfaces by anodic oxidation,” U.S. Patent 3,977,018 (1976).

**Round-3 interpretation upgrade:** This remains the strongest **direct executable** 800-Å process disclosure and is now better supported by the composition-matched Janousek/Carscallen mechanism lineage.

Direct candidate center:

- 0.1 M KOH in 90% EG / 10% DI water;
- constant current ~0.3 mA/cm²;
- formation endpoint ~15 V;
- ~2 min;
- ~800 Å oxide.

Do not label it the exact UWA RP-01 process.

## S-R3-06 — independent x≈0.20 constant-current HgCdTe anodization

**Class:** Primary-A  
**Role:** Independent experimental bracket for the P02 electrolyte/current family.

**Direct experimental anchors:**

- Hg0.8Cd0.2Te;
- room-temperature constant-current anodization;
- 0.1 M KOH in 90% EG / 10% water;
- current densities 0.2–0.5 mA/cm²;
- pre-etch 1% Br2 in EG for 30–60 s followed by distilled-water wash.

**Compatibility warning:** composition and surface-prep branch differ from RP-01; use for transfer bracketing only.

## S-R3-07 — Rajaduray 1998 UWA thesis

**Class:** Primary-Thesis / Same-Lab  
**Citation:** Ramesh Rajaduray, *Investigation of Spatial Characterisation Techniques in Semiconductors*, B.E. (Hons) thesis, University of Western Australia, 1998; supervisor John M. Dell; acknowledgements include David Redfern and E. P. G. Smith.

**Role:** Same-laboratory temporal/lifetime methodology supporting P13.

**Key method:** n-type x≈0.30 HgCdTe near 77 K under vacuum; low bias deliberately used to avoid sweeping excess carriers into high-recombination contact regions.

**Procedure:** `procedures/P13A_UWA_TRANSIENT_DECAY_LINEAGE_ADDENDUM.md`.

## Round-3 source priorities

1. acquire full Janousek/Carscallen 1982 J. Appl. Phys. experimental section and exact current-density/cell data;
2. verify exact page/DOI metadata for “Hg0.70Cd0.30Te anodic oxidation”;
3. recover exact UWA RP-01 anodization traveler or author/lab record;
4. recover Br2 percentage convention from Srivastav lab lineage, if possible;
5. continue exact UWA RIE and metallization source recovery.

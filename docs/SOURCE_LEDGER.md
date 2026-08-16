# Source ledger

This file records the literature allowed to inform the controlled manual. Inclusion does not mean that every process condition in a source is compatible with RP-01. Quantitative process values are extracted into the relevant device/procedure document with provenance tags and compatibility notes.

## Source classes

- **Primary-A** — original peer-reviewed experimental paper.
- **Primary-B** — original patent/proceedings/source with useful technical detail requiring additional scrutiny.
- **Secondary-A** — authoritative monograph or review used for synthesis and source discovery.
- **Lead** — potentially useful source not yet sufficiently audited for controlled use.

---

## S001 — Smith et al. 2001

**Class:** Primary-A  
**Role:** RP-01 downstream fabrication and characterization anchor.  
**Citation:** E. P. G. Smith, K. J. Winchester, C. A. Musca, J. M. Dell, and L. Faraone, “A simplified fabrication process for HgCdTe photoconductive detectors using CH4/H2 reactive-ion-etching-induced blocking contacts,” *Semiconductor Science and Technology* 16, 455–462 (2001).  
**DOI:** `10.1088/0268-1242/16/6/306`

**Why it matters:** Reports an experimentally fabricated n-type HgCdTe photoconductor process and gives starting material properties, plasma-processing conditions, passivation and metallization information, contact characterization, responsivity, noise, cutoff, and detectivity.

**Limitations:** Does not disclose enough detail to reproduce the complete LPE history, mesa process, oxide formation, all lithographic conditions, packaging, or full measurement-chain calibration.

**Audit status:** Core paper substantially extracted into `docs/01_RP01_REFERENCE_DEVICE.md`.

---

## S002 — Hansen, Schmit, Casselman 1982

**Class:** Primary-A  
**Role:** HgCdTe band-gap versus composition and temperature relation.  
**Citation:** G. L. Hansen, J. L. Schmit, and T. N. Casselman, “Energy gap versus alloy composition and temperature in Hg1−xCdxTe,” *Journal of Applied Physics* 53, 7099–7101 (1982).  
**DOI:** `10.1063/1.330018`

**Why it matters:** Provides a widely used empirical Eg(x,T) relation over the full alloy range and 4.2–300 K with a reported standard error.

**Use restriction:** A band-gap-derived wavelength is a material-property consistency calculation and must not silently replace an experimentally defined detector cutoff convention.

**Audit status:** Equation identified; controlled calculation module added under `calculations/`.

---

## S003 — Radhakrishnan, Sitharaman, Gupta 2003

**Class:** Primary-A  
**Role:** Te-rich modified horizontal-slider LPE apparatus/process candidate.  
**Citation:** J. K. Radhakrishnan, S. Sitharaman, and S. C. Gupta, “Liquid phase epitaxial growth of HgCdTe using a modified horizontal slider,” *Journal of Crystal Growth* 252, 79–86 (2003).  
**DOI:** `10.1016/S0022-0248(02)02530-7`

**Why it matters:** Describes a high-detail horizontal-slider arrangement with explicit Hg-loss compensation and in-situ substrate meltback, together with charge-preparation information: high-purity/high-density graphite, a 15×15×1 mm CdZnTe recess, 6N elements, 700 °C/8 h charge synthesis, ~4.8 g per growth run, and 3 g HgTe compensation.

**Compatibility warning:** Its typical melt/material branch is around x≈0.20. Use it as an apparatus/process-engineering source, not as the direct composition source for RP-01 x≈0.30.

**Audit status:** Major apparatus/charge anchors extracted; remaining experimental details still being recovered.

---

## S004 — Harman 1980

**Class:** Primary-A  
**Role:** Te-rich Hg-Cd-Te liquidus/solidus and horizontal-slider LPE growth-window constraints.  
**Citation:** T. C. Harman, “Liquidus isotherms, solidus lines and LPE growth in the Te-rich corner of the Hg-Cd-Te system,” *Journal of Electronic Materials* 9 (1980).  
**DOI:** `10.1007/BF02822728`

**Why it matters:** Reports Te-rich liquidus isotherms from 425–600 °C, horizontal-slider growth under flowing H2, solid x≈0.1–0.8, growth temperatures 450–550 °C, growth times 0.25–10 min, typical equilibration about 1 h at 550 °C, and 3–15 µm layer thicknesses.

**Audit status:** Abstract-level process constraints extracted; full article audit pending.

---

## S005 — Schmit, Hager, Wood 1982

**Class:** Primary-A  
**Role:** High-priority x≈0.30 Te-rich horizontal-slider LPE source.  
**Citation:** J. L. Schmit, R. J. Hager, and R. A. Wood, “Liquid phase epitaxy of Hg1−xCdxTe,” *Journal of Crystal Growth* 56, 485–489 (1982).  
**DOI:** `10.1016/0022-0248(82)90468-7`

**Why it matters:** Reports atmospheric-pressure horizontal-slider Te-rich LPE of n- and p-HgCdTe on substrates up to 2×3 cm, explicitly including controlled solid compositions x=0.2, 0.3, and 0.4.

**Correction:** This source was previously mislabeled “Tung et al. 1982” in the project. The correct authors are Schmit, Hager, and Wood.

**Audit status:** Metadata/abstract verified. Full experimental section remains a high-priority acquisition target.

---

## S006 — Capper/Garland monograph

**Class:** Secondary-A  
**Role:** Literature map and cross-check source.  
**Title:** *Mercury Cadmium Telluride: Growth, Properties and Applications*.

**Use rule:** Process-critical numerical values should be traced to original literature whenever possible before process release.

**Audit status:** Chapter-by-chapter audit pending.

---

## S007 — Smith et al. 2000 — mesa etch comparison

**Class:** Primary-A  
**Role:** Same-UWA-lineage evidence for RP-01 mesa-isolation choice.  
**Citation:** E. P. G. Smith, C. A. Musca, D. A. Redfern, J. M. Dell, and L. Faraone, “H2-based dry plasma etching for mesa structuring of HgCdTe,” *Journal of Electronic Materials* 29(6), 853–858 (2000).  
**DOI:** `10.1007/s11664-000-0237-7`

**Why it matters:** Directly compares mesa isolation of n-type x≈0.31 HgCdTe photoconductors using H2/CH4 RIE and wet chemical etching using bromine in hydrobromic acid. The detector-level comparison strongly supports preserving wet mesa isolation in RP-01.

**Audit status:** Bibliographic/abstract evidence verified; exact wet formulation is not sufficiently disclosed in accessible material.

---

## S008 — Musca et al. 1998 — RIE-induced n-type region / LBIC

**Class:** Primary-A  
**Role:** Same-UWA-lineage source for spatial characterization of RIE-induced n-type doping.  
**Citation:** C. A. Musca, J. F. Siliquini, E. P. G. Smith, J. M. Dell, and L. Faraone, “Laser Beam Induced Current Imaging of Reactive Ion Etching Induced n-Type Doping in HgCdTe,” *Journal of Electronic Materials* 27, 661–667 (1998).  
**DOI:** `10.1007/s11664-998-0032-4`

**Why it matters:** Demonstrates LBIC as a nondestructive method for confirming the presence and spatial extent of RIE-induced n-type/n+ regions and is directly cited by RP-01.

**Audit status:** Metadata/abstract verified; full quantitative depth extraction pending.

---

## S009 — Agnihotri, Musca, Faraone 1998 — passivation review

**Class:** Secondary-A  
**Role:** Same-UWA-lineage map of HgCdTe surface-passivation physics and technologies.  
**Citation:** O. P. Agnihotri, C. A. Musca, and L. Faraone, “Current status and issues in the surface passivation technology of mercury cadmium telluride infrared detectors,” *Semiconductor Science and Technology* 13, 839–847 (1998).  
**DOI:** `10.1088/0268-1242/13/8/002`

**Use restriction:** Executable anodization setpoints must be traced to primary experiments.

**Audit status:** Identified; primary references being followed.

---

## S010 — Nemirovsky and Bahir 1989 — passivation

**Class:** Primary-A  
**Role:** HgCdTe surface-passivation/interface-behavior source.  
**Citation:** Y. Nemirovsky and G. Bahir, “Passivation of mercury cadmium telluride surfaces,” *Journal of Vacuum Science & Technology A* 7, 450–459 (1989).  
**DOI:** `10.1116/1.576202`

**Audit status:** Citation identified; full method extraction pending.

---

## S011 — Srivastav et al. 2005 — wet mesa optimization

**Class:** Primary-A  
**Role:** Best current quantitative transfer source for Br2/HBr/ethylene-glycol wet mesa etching near RP-01 composition.  
**Citation:** V. Srivastav, R. Pal, B. L. Sharma, A. Naik, D. S. Rawal, V. Gopal, and H. P. Vyas, “Etching of Mesa Structures in HgCdTe,” *Journal of Electronic Materials* 34, 1440–1445 (2005).  
**DOI:** `10.1007/s11664-005-0203-5`

**Key anchors:** x=0.28 material; selected 2% Br2 in 3:1 ethylene glycol:HBr; 21 °C mean vertical rate 2.78 µm/min; anisotropy ~0.63; process temperature 5–50 °C; lower temperature improves dimensional control; best reported roughness around 2 nm.

**Critical limitation:** The accessible primary text does not unambiguously define the concentration basis of “2% Br2.” The process therefore remains a qualification candidate, not a released recipe.

**Procedure:** `procedures/P01_WET_MESA_QUALIFICATION.md`.

---

## S012 — Texas Instruments native anodic oxide process

**Class:** Primary-B  
**Role:** Strong historical qualification candidate for the RP-01 800 Å native anodic oxide.  
**Citation:** Texas Instruments Incorporated, “Passivation of mercury cadmium telluride semiconductor surfaces by anodic oxidation,” U.S. Patent 3,977,018.

**Key anchors:** 0.1 M KOH in 90% ethylene glycol / 10% deionized water; constant-current anodization around 0.3 mA/cm²; endpoint near 15 V; approximately 2 min; approximately 800 Å oxide; profilometric/optical thickness verification described.

**Compatibility warning:** The numerical match to RP-01's 800 Å film does not prove that the UWA RP-01 process used the identical chemistry/electrical conditions.

**Procedure:** `procedures/P02_ANODIC_OXIDE_QUALIFICATION.md`.

---

## S013 — Bowers and Schmit 1982 — Hg containment / x≈0.30 tie-line

**Class:** Primary-B  
**Role:** Highest-detail current source for a composition-matched Te-rich horizontal-slider charge and Hg containment architecture.  
**Citation:** J. E. Bowers and J. L. Schmit, “Mercury containment for liquid phase growth of mercury cadmium telluride from tellurium-rich solution,” U.S. Patent 4,317,689 (1982).

**Why it matters:** Same Honeywell/Schmit process lineage as S005. Gives covered graphite-slider architecture, N2 purge/H2 flow, HgTe or HgTe+Te auxiliary Hg source, and explicit liquid/solid tie-line data.

**Critical tie line:** liquid xL=0.082, yL=0.810, TL=507 °C → solid xS=0.29, k=3.54. The source describes growth near 500 °C after first taking the melt above liquidus and then operating below liquidus.

**Audit status:** Detailed text extracted. This source materially closes the candidate x≈0.30 melt-composition variable.

**Procedure:** `procedures/P03_LPE_X030_QUALIFICATION.md`.

---

## S014 — Tranchart et al. 1985 — CdZnTe substrate for x≈0.30 LPE

**Class:** Primary-A  
**Role:** Substrate compatibility for RP-01-like x≈0.30 Te-rich LPE material.  
**Citation:** J. C. Tranchart, B. Latorre, C. Foucher, and Y. Le Gouge, “LPE growth of Hg1−xCdxTe on Cd1−yZnyTe substrates,” *Journal of Crystal Growth* 72, 468–473 (1985).

**Why it matters:** Reports Cd1−yZnyTe with y≈0.04 and improved-quality Te-rich LPE HgCdTe around x≈0.30; 32-element 3–5 µm detector arrays were made from the material.

**Important nuance:** Other primary lattice-matching work reports an optimum ZnTe fraction near 2.9% for Hg0.7Cd0.3Te. The controlled manual will therefore specify substrate lattice mismatch from measurement rather than declare a universal exact Zn fraction.

**Audit status:** Abstract verified; full experimental section still needed.

---

## S015 — Nagahama et al. 1984 — post-growth Hg annealing

**Class:** Primary-A  
**Role:** Candidate bridge from as-grown Te-rich p-type material to RP-01 low-density n-type material.  
**Citation:** K. Nagahama, R. Ohkata, K. Nishitani, and T. Murotani, “LPE growth of Hg1−xCdxTe using conventional slider boat and effects of annealing on properties of the epilayers” (1984; complete journal metadata pending verification).

**Key anchors:** x≈0.17–0.30; conventional slider, open-tube H2; as-grown p-type; Hg-overpressure annealing studied from 250–400 °C; 250–300 °C produced well-behaved n-type layers without apparent composition change, whereas 400 °C produced compositional change near the interface.

**Limitation:** Anneal duration, Hg source configuration, cooldown, and the final n/µ for RP-01 x≈0.30 are not yet closed.

---

# Priority source gaps

1. **x≈0.30 LPE process:** full S005 experimental section, especially charge synthesis, exact supercooling/cooling rate, equilibration, thickness/time relation, and electrical outputs.
2. **CdZnTe substrate:** full S014 process and a measurement-based lattice-mismatch specification for the selected RP-01 substrate.
3. **Post-growth n-type anneal:** full S015 metadata/method, especially time, Hg chemical potential/source geometry, and cooldown.
4. **RP-01 mesa isolation:** resolve the basis of “2% Br2,” reagent stock concentration, preparation order, rinse/strip, and transfer capability on x≈0.30.
5. **RP-01 anodic oxide:** exact UWA recipe if recoverable; otherwise complete local transfer qualification of S012-family process.
6. **RIE conversion depth:** exact conditions/depth from S008 and the related LBIC junction-depth paper.
7. **Cr/Au contact deposition:** deposition and surface-preparation details from the same process lineage.
8. **Measurement closure:** full responsivity/noise calibration chain required to independently reproduce D*.

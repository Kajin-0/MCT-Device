# Source ledger

This file records the literature allowed to inform the controlled manual. Inclusion does not mean that every process condition in a source is compatible with RP-01. Quantitative process values are extracted into the relevant device/procedure document with provenance tags and compatibility notes.

## Source classes

- **Primary-A** — original peer-reviewed experimental paper.
- **Primary-B** — original proceedings/patent/source with useful technical detail requiring additional scrutiny.
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

**Why it matters:** Describes a high-detail horizontal-slider arrangement with explicit Hg-loss compensation and in-situ substrate meltback, together with charge-preparation information.

**Compatibility warning:** It is an LPE process candidate, not automatically the upstream half of RP-01. Target composition, final conductivity, anneal history, and electrical properties must be reconciled first.

**Audit status:** Partially extracted. Full process conditions still require source audit.

---

## S004 — Harman 1980

**Class:** Primary-A  
**Role:** Te-rich Hg-Cd-Te liquidus/solidus and horizontal-slider LPE growth-window constraints.  
**Citation:** T. C. Harman, “Liquidus isotherms, solidus lines and LPE growth in the Te-rich corner of the Hg-Cd-Te system,” *Journal of Electronic Materials* (1980).  
**DOI:** `10.1007/BF02822728`

**Why it matters:** Experimental phase-diagram and growth information spanning a broad HgCdTe composition range, including controlled horizontal-slider growth.

**Audit status:** Abstract-level process constraints extracted; full article audit pending.

---

## S005 — Tung et al. 1982

**Class:** Primary-A  
**Role:** High-priority x≈0.30 Te-rich horizontal-slider LPE source.  
**Citation:** “Liquid phase epitaxy of Hg1−xCdxTe,” *Journal of Crystal Growth* 56, 485–489 (1982).  
**DOI:** `10.1016/0022-0248(82)90468-7`

**Why it matters:** Reports controlled growth for x values including 0.30, directly overlapping the nominal composition of RP-01.

**Audit status:** Lead identified; full experimental details not yet extracted.

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

**Why it matters:** Directly compares mesa isolation of n-type x≈0.31 HgCdTe photoconductors using H2/CH4 RIE and wet chemical etching using bromine in hydrobromic acid. The published performance comparison supports preserving wet mesa isolation in RP-01 rather than replacing it with an all-dry flow.

**Important limitation:** The exact Br2/HBr formulation, bath temperature, etch rate, mask chemistry, depth, and rinse/strip details have not yet been recovered from the full experimental section. Do not infer them from unrelated Br2/HBr recipes.

**Audit status:** Bibliographic/abstract evidence verified; full quantitative process extraction pending.

---

## S008 — Musca et al. 1998 — RIE-induced n-type region / LBIC

**Class:** Primary-A  
**Role:** Same-UWA-lineage source for spatial characterization of RIE-induced n-type doping.  
**Citation:** C. A. Musca, J. F. Siliquini, E. P. G. Smith, J. M. Dell, and L. Faraone, “Laser Beam Induced Current Imaging of Reactive Ion Etching Induced n-Type Doping in HgCdTe,” *Journal of Electronic Materials* 27, 661–667 (1998).  
**DOI:** `10.1007/s11664-998-0032-4`

**Why it matters:** Demonstrates LBIC as a nondestructive method for confirming the presence, depth behavior, and lateral extent of the n+ region produced by RIE in HgCdTe. This source is directly cited by the later RP-01 paper and is therefore the correct lineage to audit for conversion-depth claims.

**Audit status:** Metadata and abstract verified; full quantitative junction-depth/RIE-condition extraction pending.

---

## S009 — Agnihotri, Musca, Faraone 1998 — passivation review

**Class:** Secondary-A  
**Role:** Same-UWA-lineage map of HgCdTe surface-passivation physics and technologies.  
**Citation:** O. P. Agnihotri, C. A. Musca, and L. Faraone, “Current status and issues in the surface passivation technology of mercury cadmium telluride infrared detectors,” *Semiconductor Science and Technology* 13, 839–847 (1998).  
**DOI:** `10.1088/0268-1242/13/8/002`

**Why it matters:** Surface passivation is a dominant determinant of HgCdTe detector leakage/noise. This source is useful for tracing the UWA group’s understanding of native anodic oxide, deposited films, interface charge, and process compatibility.

**Use restriction:** It is a review, so executable anodization setpoints should be traced to the primary experiments it cites rather than copied without lineage verification.

**Audit status:** Identified; primary references and exact anodic-oxide recipe still to be extracted.

---

## S010 — Nemirovsky and Bahir 1989 — passivation source lead

**Class:** Primary-A  
**Role:** High-priority primary source for HgCdTe surface-passivation methods and interface behavior.  
**Citation:** Y. Nemirovsky and G. Bahir, “Passivation of mercury cadmium telluride surfaces,” *Journal of Vacuum Science & Technology A* 7, 450–459 (1989).  
**DOI:** `10.1116/1.576202`

**Why it matters:** It is explicitly cited in the RP-01 paper’s passivation discussion and is a likely route to closing the anodic-oxide process and interface-physics requirements.

**Audit status:** Citation identified; full method extraction pending.

---

# Priority source gaps

1. **RP-01 mesa isolation:** exact Br2/HBr formulation, bath temperature, etch rate, target depth, mask compatibility, rinse/strip, and dimensional-control data from S007 or its immediate process references.
2. **RP-01 anodic oxide:** electrolyte, current/voltage mode, current density, temperature, time, endpoint, and thickness calibration from S009/S010 primary lineage.
3. **RIE conversion depth:** extract the exact RIE conditions and inferred depth/lateral profile from S008 and distinguish them from the RP-01 2001 contact-window recipe.
4. **x≈0.30 LPE process:** complete growth process compatible with CdZnTe and the RP-01 electrical state.
5. **Post-growth stoichiometry/anneal:** process consistent with the desired carrier density and cutoff.
6. **Cr/Au contact deposition:** deposition and surface-preparation details from the same process lineage.
7. **Measurement closure:** full responsivity/noise calibration chain required to reproduce D*, not merely detector fabrication.

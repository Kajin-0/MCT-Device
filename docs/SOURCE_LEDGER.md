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

**Audit status:** Equation identified; derivation/uncertainty module still to be added under `calculations/`.

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

# Priority source gaps

1. RP-01 mesa isolation chemistry and dimensional control.
2. RP-01 anodic-oxide formation method and thickness calibration.
3. Original source for plasma-induced conversion depth cited by Smith et al.
4. Complete x≈0.30 LPE growth process compatible with CdZnTe and the RP-01 electrical state.
5. Post-growth stoichiometry/anneal process consistent with the desired carrier density and cutoff.
6. Cr/Au contact deposition and surface-preparation details from the same process lineage.
7. Full responsivity/noise calibration chain required to reproduce D*, not merely detector fabrication.

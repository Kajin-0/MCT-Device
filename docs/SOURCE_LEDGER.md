# Source ledger

This is the controlled literature ledger for the MCT-Device manual. Inclusion means a source may inform the project; it does **not** mean all numerical conditions in that source are compatible with RP-01.

## Source classes

- **Primary-A** — original peer-reviewed experimental paper.
- **Primary-B** — original patent/proceedings/process disclosure with useful technical detail requiring transfer scrutiny.
- **Official-Metrology** — standards-laboratory or official measurement guidance.
- **Secondary-A** — authoritative monograph/review used for literature mapping and cross-checking.
- **Lead** — potentially useful source not yet sufficiently audited.

## Use rules

1. Process-critical setpoints should be traceable to Primary-A/Primary-B sources wherever possible.
2. A number from one source is not transferable merely because the material is “HgCdTe.” Composition, face, growth family, Hg chemical potential, reactor/boat geometry and thermal history must match or be qualified.
3. Derived values must be labeled `[D]` in procedure/calculation files.
4. Apparatus-specific quantities remain `[CAL]`; transfer experiments remain `[QUAL]`.
5. Unknown details remain open rather than being inferred from common practice.

---

## S001 — Smith et al. 2001 — RP-01 reference detector process

**Class:** Primary-A  
**Citation:** E. P. G. Smith, K. J. Winchester, C. A. Musca, J. M. Dell, L. Faraone, “A simplified fabrication process for HgCdTe photoconductive detectors using CH4/H2 reactive-ion-etching-induced blocking contacts,” *Semiconductor Science and Technology* 16, 455–462 (2001).  
**DOI:** `10.1088/0268-1242/16/6/306`

**Role:** Downstream fabrication/characterization anchor for RP-01. Gives starting material specification, RIE conditions, lithography preparation details, oxide/metal thicknesses, TLM geometry/contact resistance and detector performance.

**Critical audit note:** the Fermionics starting values `n=9.8×10^14 cm^-3` and `µ=4.0×10^4 cm²/V·s` are stated as supplier specifications but the measurement temperature is not stated. RIE-converted material was measured at 80 K and 300 K with variable magnetic field up to 2 T.

---

## S002 — Hansen, Schmit, Casselman 1982 — band gap relation

**Class:** Primary-A  
**Citation:** G. L. Hansen, J. L. Schmit, T. N. Casselman, “Energy gap versus alloy composition and temperature in Hg1−xCdxTe,” *Journal of Applied Physics* 53, 7099–7101 (1982).  
**DOI:** `10.1063/1.330018`

**Role:** `Eg(x,T)` consistency calculation.  
**Restriction:** band-gap-equivalent wavelength must not silently replace measured detector cutoff.

---

## S003 — Radhakrishnan, Sitharaman, Gupta 2003 — modified slider LPE

**Class:** Primary-A  
**Citation:** J. K. Radhakrishnan, S. Sitharaman, S. C. Gupta, “Liquid phase epitaxial growth of HgCdTe using a modified horizontal slider,” *Journal of Crystal Growth* 252, 79–86 (2003).  
**DOI:** `10.1016/S0022-0248(02)02530-7`

**Role:** Apparatus/charge-handling source: high-density graphite, 15×15×1 mm CdZnTe recess, 6N elements, 700 °C/8 h synthesis, ~4.8 g/run, 3 g HgTe, in-situ meltback, wipe-off engineering.

**Restriction:** typical material branch is around x≈0.20. Do not use its 4.8-g/3-g masses as direct RP-01 x≈0.30 values.

---

## S004 — Harman 1980 — Te-rich phase/growth window

**Class:** Primary-A  
**Citation:** T. C. Harman, “Liquidus isotherms, solidus lines and LPE growth in the Te-rich corner of the Hg-Cd-Te system,” *Journal of Electronic Materials* 9 (1980).  
**DOI:** `10.1007/BF02822728`

**Role:** Te-rich liquidus/growth bounds, horizontal-slider H2 process, typical equilibration, growth temperature/time and thickness ranges.

---

## S005 — Schmit, Hager, Wood 1982 — x≈0.30 Te-rich slider LPE

**Class:** Primary-A  
**Citation:** J. L. Schmit, R. J. Hager, R. A. Wood, “Liquid phase epitaxy of Hg1−xCdxTe,” *Journal of Crystal Growth* 56, 485–489 (1982).  
**DOI:** `10.1016/0022-0248(82)90468-7`

**Role:** High-priority same-lineage source demonstrating Te-rich atmospheric-pressure slider growth including x=0.2, 0.3 and 0.4.

**Correction:** previously misattributed in early project notes as “Tung et al.”

---

## S006 — Capper/Garland monograph

**Class:** Secondary-A  
**Title:** *Mercury Cadmium Telluride: Growth, Properties and Applications*.

**Role:** Literature map and cross-check. Process-critical values should be traced to original literature before release.

---

## S007 — Smith et al. 2000 — wet vs dry mesa

**Class:** Primary-A  
**Citation:** E. P. G. Smith, C. A. Musca, D. A. Redfern, J. M. Dell, L. Faraone, “H2-based dry plasma etching for mesa structuring of HgCdTe,” *Journal of Electronic Materials* 29, 853–858 (2000).  
**DOI:** `10.1007/s11664-000-0237-7`

**Role:** Same-UWA-lineage evidence for wet mesa isolation and against blanket H2/CH4 dry-mesa processing in the RP-01 photoconductor branch.

---

## S008 — Musca et al. 1998 — RIE-induced n-type region / LBIC

**Class:** Primary-A  
**Citation:** C. A. Musca, J. F. Siliquini, E. P. G. Smith, J. M. Dell, L. Faraone, “Laser Beam Induced Current Imaging of Reactive Ion Etching Induced n-Type Doping in HgCdTe,” *Journal of Electronic Materials* 27, 661–667 (1998).  
**DOI:** `10.1007/s11664-998-0032-4`

**Role:** Spatial characterization of RIE-induced n/n+ region. Full quantitative depth extraction remains pending.

---

## S009 — Agnihotri, Musca, Faraone 1998 — passivation review

**Class:** Secondary-A  
**Citation:** O. P. Agnihotri, C. A. Musca, L. Faraone, “Current status and issues in the surface passivation technology of mercury cadmium telluride infrared detectors,” *Semiconductor Science and Technology* 13, 839–847 (1998).  
**DOI:** `10.1088/0268-1242/13/8/002`

**Role:** Same-UWA-lineage map of HgCdTe passivation physics. Executable oxide setpoints must be traced to primary sources.

---

## S010 — Nemirovsky and Bahir 1989 — surface passivation

**Class:** Primary-A  
**Citation:** Y. Nemirovsky, G. Bahir, “Passivation of mercury cadmium telluride surfaces,” *Journal of Vacuum Science & Technology A* 7, 450–459 (1989).  
**DOI:** `10.1116/1.576202`

**Role:** HgCdTe surface/interface passivation behavior. Full method extraction remains pending.

---

## S011 — Srivastav et al. 2005 — wet mesa optimization

**Class:** Primary-A  
**Citation:** V. Srivastav et al., “Etching of Mesa Structures in HgCdTe,” *Journal of Electronic Materials* 34, 1440–1445 (2005).  
**DOI:** `10.1007/s11664-005-0203-5`

**Key anchors:** x=0.28; selected 2% Br2 in 3:1 EG:HBr; 21 °C mean rate 2.78 µm/min; anisotropy ~0.63; lower temperature improves dimensional control; best reported roughness ~2 nm.

**Release blocker:** concentration basis of “2% Br2” is not unambiguously closed in accessible primary text.

**Procedure:** `procedures/P01_WET_MESA_QUALIFICATION.md`.

---

## S012 — Texas Instruments native anodic oxide process

**Class:** Primary-B  
**Citation:** Texas Instruments Incorporated, “Passivation of mercury cadmium telluride semiconductor surfaces by anodic oxidation,” U.S. Patent 3,977,018.

**Key anchors:** 0.1 M KOH in 90% EG/10% DI water; constant current ~0.3 mA/cm²; ~15 V endpoint; ~2 min; ~800 Å oxide.

**Restriction:** numerical match to RP-01's 800 Å oxide does not prove identical UWA chemistry.

**Procedure:** `procedures/P02_ANODIC_OXIDE_QUALIFICATION.md`.

---

## S013 — Bowers and Schmit 1982 — Hg containment / x≈0.30 tie line

**Class:** Primary-B  
**Citation:** J. E. Bowers, J. L. Schmit, “Mercury containment for liquid phase growth of mercury cadmium telluride from tellurium-rich solution,” U.S. Patent 4,317,689 (1982).

**Key tie line:** `xL=0.082`, `yL=0.810`, `TL=507 °C` → `xS=0.29`, tabulated `xS/xL=3.54`.

**Role:** Composition-matched Te-rich charge plus covered-slider/Hg-source architecture.

**Procedure:** `procedures/P03_LPE_X030_QUALIFICATION.md`.

---

## S014 — Tranchart et al. 1985 — CdZnTe for x≈0.30

**Class:** Primary-A  
**Citation:** J. C. Tranchart, B. Latorre, C. Foucher, Y. Le Gouge, “LPE growth of Hg1−xCdxTe on Cd1−yZnyTe substrates,” *Journal of Crystal Growth* 72, 468–473 (1985).

**Role:** Demonstrates CdZnTe around y≈0.04 as an x≈0.30 Te-rich-LPE substrate family and device material.

**Restriction:** exact released Zn fraction should be measurement/mismatch based rather than treated as a universal 4% constant.

---

## S015 — Nagahama et al. 1984 — post-growth Hg anneal branch

**Class:** Primary-A  
**Citation:** K. Nagahama, R. Ohkata, K. Nishitani, T. Murotani, “LPE growth of Hg1−xCdxTe using conventional slider boat and effects of annealing on properties of the epilayers” (1984; complete journal metadata still pending).

**Key anchors:** x≈0.17–0.30; as-grown p-type; Hg-overpressure anneal 250–400 °C; 250–300 °C produced well-behaved n-type material without apparent composition change; 400 °C produced interface-region composition change.

---

## S016 — Hager and Wood 1986 — LPE wipe-off apparatus

**Class:** Primary-B  
**Citation:** R. J. Hager, R. A. Wood, “Apparatus for liquid phase epitaxy of mercury cadmium telluride,” U.S. Patent 4,592,304 (1986).

**Role:** Dedicated wipe-off well in covered graphite slider; loose CdTe pieces guided in vertical slots collect residual growth solution after LPE.

**Restriction:** slider velocity/contact force and final residual-melt acceptance remain apparatus qualification variables.

---

## S017 — Harman 1987 — pressure-controlled growth/anneal process

**Class:** Primary-B  
**Citation:** T. C. Harman, “Process for making mercury cadmium telluride,” U.S. Patent 4,642,142 (1987; priority 1982-05-19).

**Key anchors:** tightly controlled solution/Hg-source temperatures; source-wafer equilibration; Te-rich growth; controlled Hg-vapor anneal; broad anneal regime ~200–300 °C and Hg partial pressure ~0.1–250 Torr; example pseudo-isothermal Hg-saturated anneal ~250 °C/1 h.

**Restriction:** the example process typically yields carrier density in the low 10^16 cm^-3 range, so 250 °C/1 h is a screening anchor, not the RP-01 endpoint.

**Procedure:** `procedures/P04_HG_ANNEAL_QUALIFICATION.md`.

---

## S018 — Jones et al. 1982 — annealing/electrical defect control

**Class:** Primary-A  
**Citation:** C. L. Jones, M. J. T. Quelch, P. Capper, J. J. G. Gosney, “Effects of annealing on the electrical properties of CdxHg1−xTe,” *Journal of Applied Physics* 53, 9080–9092 (1982).  
**DOI:** `10.1063/1.330419`

**Role:** Distinguishes Hg-rich isothermal and two-temperature anneal states and links Hg chemical potential to electrical/native-defect behavior.

---

## S019 — Chandra, Schaake, Kinch 2003 — low-temperature anneal kinetics

**Class:** Primary-A  
**Citation:** D. Satish Chandra, H. F. Schaake, M. A. Kinch, “Low-temperature annealing of (Hg,Cd)Te,” *Journal of Electronic Materials* 32, 810–815 (2003).  
**DOI:** `10.1007/s11664-003-0075-5`

**Role:** Shows anneal kinetics depend strongly on vacancy concentration, x and T; rate falls with increasing Cd fraction. Warns that incomplete metal-vacancy ionization at 77 K complicates defect-state inference for x≳0.26.

---

## S020 — Tsen et al. 2007 — HgCdTe multicarrier Hall metrology

**Class:** Primary-A  
**Citation:** G. K. O. Tsen, C. A. Musca, J. M. Dell, J. Antoszewski, L. Faraone, “Magneto-Transport Characterization of p-Type HgCdTe,” *Journal of Electronic Materials* 36, 826–831 (2007).  
**DOI:** `10.1007/s11664-007-0103-y`

**Role:** Same-UWA-lineage variable-field/temperature Hall + iQMSA demonstration. Shows single-field Hall may average multiple populations and surface inversion can evolve after processing.

**Procedure:** `procedures/P05_HALL_VDP_MATERIAL_METROLOGY.md`.

---

## S021 — van der Pauw / NIST Hall guidance

**Class:** Official-Metrology + Primary method  
**Sources:** NIST Physical Measurement Laboratory Hall/resistivity guidance; L. J. van der Pauw, “A Method of Measuring Specific Resistivity and Hall Effect of Discs of Arbitrary Shapes,” *Philips Research Reports* 13, 1–9 (1958).

**Role:** Four-terminal van der Pauw equations, reversal/reciprocity checks, field/current reversal, practical error controls. P05 adopts ≤3% routine agreement, 3–5% conditional and >5% fail for the basic VdP redundancy gate.

---

## S022 — Hougen 1989 — LPE HgCdTe transmission model

**Class:** Primary-A  
**Citation:** C. A. Hougen, “Model for infrared absorption and transmission of liquid-phase epitaxy HgCdTe,” *Journal of Applied Physics* 66, 3763–3766 (1989).  
**DOI:** `10.1063/1.344038`

**Role:** Preferred P06 full-spectrum model lineage: composition profile, thickness, surface nonuniformity and back reflections; avoids arbitrary equality between one edge point and Eg.

**Procedure:** `procedures/P06_FTIR_COMPOSITION_THICKNESS_MAPPING.md`.

---

## S023 — HgCdTe IR transmission composition methods

**Class:** Primary-A  
**Sources:** “Compositional characterization of HgCdTe epilayers by infrared transmission,” *Infrared Physics* 33, 39–45 (1992), DOI `10.1016/0020-0891(92)90053-V`; “New method for the estimation of bulk HgCdTe composition by infrared transmission,” *Infrared Physics & Technology* 37, 445–450 (1996), DOI `10.1016/1350-4495(95)00125-5`.

**Role:** Supports traceable edge metrics, composition extraction and interference/fringe-based thickness characterization in P06.

---

## S024 — CdZnTe crystalline-quality comparison for x≈0.30 LPE

**Class:** Primary-A  
**Citation:** “Study of the crystalline quality of CdTe, CdZnTe and CdMnTe substrates used for liquid phase epitaxy of Cd0.7Hg0.3Te,” *Journal of Crystal Growth* 139, 6–14 (1994).  
**DOI:** `10.1016/0022-0248(94)90022-1`

**Key benchmark:** best reported Cd0.96Zn0.04Te substrate in the study had EPD ~`5×10^4 cm^-2` and X-ray rocking-curve linewidth ~`25 arcsec`; x≈0.30 HgCdTe layers were better on CdZnTe than CdTe.

**Procedure:** `procedures/P07_CZT_SUBSTRATE_QUALIFICATION.md`.

---

## S025 — Li et al. 1998 — substrate off-cut / crystallinity

**Class:** Primary-A  
**Citation:** B. Li, X. Zhang, J. Zhu, J. Chu, “Crystallinity improvement of Hg1−xCdxTe films grown by a liquid-phase epitaxial technique,” *Journal of Crystal Growth* 184–185, 1242–1246 (1998).  
**DOI:** `10.1016/S0022-0248(98)80260-1`

**Role:** Reports improved crystalline quality and fewer Te precipitates for epilayers grown on approximately 1.2–2° off `(111)A` substrates; also supports deliberate interface melt-etching.

**Restriction:** process geometry differs from the selected horizontal-slider RP-01 reconstruction; use for orientation DOE, not a universal miscut setpoint.

---

## S026 — vicinal-plane LPE study 1996

**Class:** Primary-A  
**Citation:** “Growth of Hg1−xCdxTe liquid phase epitaxial films on vicinal planes,” *Journal of Crystal Growth* 169, 480–484 (1996).  
**DOI:** `10.1016/S0022-0248(96)00418-6`

**Role:** Dipping-LPE study on differently misoriented facets; best crystal quality/fewer Te precipitates reported near `1.2° off (111)`.

**Restriction:** supports an orientation-screening range, not the final slider-LPE miscut.

---

## S027 — Everson et al. 1995 — CdTe/CdZnTe EPD screening

**Class:** Primary-A  
**Citation:** W. J. Everson, C. K. Ard, J. L. Sepich, B. E. Dean, G. T. Neugebauer, H. F. Schaake, “Etch Pit Characterization of CdTe and CdZnTe Substrates for Use in Mercury Cadmium Telluride Epitaxy,” *Journal of Electronic Materials* 24, 505–510 (1995).  
**DOI:** `10.1007/BF02657954`

**Role:** B-face `(111)/(211)` substrate-defect screening; pits roughly 10:1 wider than deep; provides manufacturing-oriented EPD screening framework.

---

## S028 — Tower et al. 1995 — CdZnTe substrate impurities

**Class:** Primary-A  
**Citation:** J. P. Tower, S. P. Tobin, M. Kestigian, P. W. Norton, A. B. Bollong, H. F. Schaake, C. K. Ard, “CdZnTe Substrate Impurities and Their Effects on Liquid Phase Epitaxy HgCdTe,” *Journal of Electronic Materials* 24 (1995).

**Role:** Tracks substrate impurities using GDMS and Zeeman-corrected graphite-furnace atomic absorption; identifies substrate Cu contamination as a cause of degraded lightly doped HgCdTe/device behavior and anomalous carrier-type conversion.

---

## S029 — Weiss et al. 2001 — substrate quality and carrier state

**Class:** Primary-A  
**Citation:** E. Weiss, O. Klin, E. Benory, E. Kedar, Y. Juravel, “Substrate quality impact on the carrier concentration of undoped annealed HgCdTe LPE layers,” *Journal of Electronic Materials* 30, 756–761 (2001).  
**DOI:** `10.1007/BF02665868`

**Role:** Shows Te precipitates and Cu-contaminated substrates can perturb annealed HgCdTe carrier state; Cu impact was strongly polarity dependent in the studied `(111)` material.

---

## S030 — Radhakrishnan et al. 2003 — LPE surface morphology / substrate orientation

**Class:** Primary-A  
**Citation:** J. K. Radhakrishnan, S. Sitharaman, S. C. Gupta, “Surface morphology of Hg0.8Cd0.2Te epilayers grown by LPE using horizontal slider,” *Applied Surface Science* 207, 33–39 (2003).  
**DOI:** `10.1016/S0169-4332(02)01227-8`

**Role:** Same horizontal-slider engineering family; uses Cd0.96Zn0.04Te near `(111)±0.5°` and documents morphology/process dependencies.

**Restriction:** x≈0.20 branch; use as substrate/process-family evidence, not exact RP-01 setpoint.

---

# Current priority source gaps

1. Full Schmit–Hager–Wood 1982 experimental section: charge synthesis, exact thermal trajectory, growth-time/thickness relation, electrical outputs.
2. Exact RP-01/Fermionics CdZnTe face, miscut, lattice mismatch and substrate surface-preparation lineage.
3. Full Nagahama 1984 bibliographic/method details: anneal time, Hg-source configuration, cooldown and final x≈0.30 n/µ.
4. Exact UWA wet-mesa formulation/preparation and post-etch rinse.
5. Exact UWA anodic-oxide formation recipe or completed local transfer qualification.
6. Quantitative RIE conversion-depth conditions from the Musca/Siliquini LBIC lineage.
7. Cr/Au deposition method, base pressure, rates and RIE-to-metal transfer delay.
8. Detector active geometry, die attach, wire bonding and package optical/thermal geometry.
9. Complete absolute responsivity/noise calibration chain required to reproduce D* independently.

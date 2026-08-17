# RP-01 full-text source acquisition and evidence integration — Round 62

**Date:** 2026-08-17 America/New_York  
**Status:** CONTROLLED DOCUMENTARY EVIDENCE INTEGRATION / POST-ROUND-61  
**Baseline artifact:** `RP01_HgCdTe_Exhaustive_Empirical_Fabrication_Protocol_Round61.pdf`

## 1. Purpose

Round 62 is a source-acquisition pass against the remaining consequential coordinates in the Round-61 Exhaustive Empirical Fabrication Protocol (EEFP).

The governing rule is unchanged:

- `RP` — direct Smith/RP-01 evidence;
- `SL` — same-laboratory/process-lineage primary evidence;
- `PT` — primary transfer evidence from another apparatus/process lineage;
- `DER` — transparent derivation;
- `SYN` — explicit locally executable synthesized implementation;
- `OPEN` — consequential coordinate for which no responsible numerical value is presently supported.

A newly recovered full paper may strengthen a `PT` branch or replace a weak `SYN` assumption. It may not be relabeled `RP` or `SL` merely because the apparatus looks similar.

Round 62 therefore asks only:

> Does the full text provide a physically consequential coordinate that is stronger than the evidence state carried in Round 61?

No publisher PDFs are committed to the repository. This record retains the bibliographic identity, extracted empirical coordinates, transfer restrictions, and the resulting protocol consequences.

---

# 2. Executive result

The full-text pass materially strengthens six parts of the EEFP:

1. **LPE graphite/slider/Hg-compensation implementation** — Astles, Chiang, Chen and Radhakrishnan provide real apparatus cleaning, surface-fit, Hg-delivery, reservoir-temperature, thermal-cycle, slide-out and post-separation observations.
2. **CdZnTe incoming qualification** — Everson, Tobin, Bruder and Tranchart provide an executable (111)B defect-screening route, lattice-match/crosshatch criteria, orientation practice and direct `y≈0.04 -> x≈0.30` substrate evidence.
3. **Hg-rich anneal kinetics** — Chandra/Schaake/Kinch provide an explicit diffusion-like scaling with composition, initial metal-vacancy state and temperature; Astles supplies a concrete 250 °C / 48 h Hg-rich transfer example.
4. **Native anodic oxide** — Stahle/Helms, Nemirovsky/Kidron and Ngoc/Nha provide primary chemistry/current-density/interface data and, importantly, a galvanostatic-then-constant-voltage completion branch.
5. **RIE/LBIC physical-state equivalence** — Siliquini et al. give the full reactor state and the depth-resolved LBIC experiment underlying the physical-etch/electrical-conversion distinction.
6. **Cryogenic package thermal dynamics** — Bartoli et al. 1976 give numerical bond-layer conductance-per-area values and a direct thermal-recovery fitting method for HgCdTe photoconductor arrays.

The full-text pass **does not close** the exact historical RP-01 LPE boat dimensions, source ampoule dimensions, anodization cell geometry, historical RIE electrode geometry/self-bias, historical evaporator geometry, or historical cryostat/package implementation.

---

# 3. LPE apparatus and Hg-loss control

## 3.1 Astles et al. 1992 — concrete graphite/slider transfer branch

Primary full-text observations:

- computer-controlled horizontal slider boat;
- high-purity **POCO DFP-2 graphite**;
- graphite acid etched;
- cleaned in **boiling deionized water for one week**;
- baked at **500 °C**;
- slider retained by two screwed rails with adjustable shims to compensate wear;
- slider/base/lid mating surfaces hand-polished on paper to a scratch-free finish;
- two separate HgTe source regions:
  - one supplying the solution wells through grooved channels;
  - one supplying the grown layer during cooldown through vertical channels into a chamber over the layer;
- Hg-loss rate measured with dummy pre-growth cycles: typically about **0.3 mg/min**;
- typical growth near **460 °C** with about **0.10 °C/min** cooling;
- lattice-matched CdZnTe or Cd(TeSe) `(111)B` substrates oriented within about `0.15°`;
- sealed evacuated silica ampoule Hg-rich anneal, typically **250 °C / 48 h** in that laboratory branch.

### Round-62 consequence

Round 61 stated that an acid graphite clean should not be inserted without HgCdTe-LPE evidence. That restriction is now refined:

- there **is** primary HgCdTe-LPE transfer evidence for an acid-etched/boiling-DI/500 °C-baked graphite route;
- the exact acid chemistry, durations other than the one-week DI step, surface roughness and historical RP-01 cleaning remain unrecovered;
- therefore this becomes a **PT qualification branch**, not an RP-01 historical recipe.

The exact historical graphite grade and numerical boat geometry remain `OPEN`.

## 3.2 Chiang et al. 1988 — independently controlled Hg reservoir

The two-arm cover (TAC) is a quartz-plate cover connected to liquid-Hg reservoirs through quartz-tube arms in a three-zone furnace.

Full-text transfer coordinates include:

- growth solution approximately **4 g** from >6N Te/HgTe/CdTe;
- CdTe `(111)B` substrate approximately **12 × 12 mm²**;
- pre-load etch: **3% Br2/methanol for a few seconds**;
- Pd-diffused H2 ambient;
- homogenization near **500 °C / 50 min**;
- saturation near **475 °C / 30 min**;
- example growth trajectory approximately **470 -> 460 °C / 30 min**;
- cooling rate about **0.15 °C/min**;
- nominal supercooling approximately **5–15 °C**;
- Hg-reservoir temperatures programmed independently from the growth zone;
- liquid-Hg consumption **<0.5 g per thermal cycle** in the reported system;
- near `x≈0.20`, a reported sensitivity of approximately `Δx≈0.007` per `+1 °C` Hg-reservoir-temperature change;
- run-to-run composition reproducibility approximately `±0.002` in the controlled-reservoir branch.

### Round-62 consequence

The Hg-source state is not adequately represented by source mass alone. The local LPE/Hg-compensation record should preserve at least:

`{source material, mass, exposed area, reservoir geometry, T_Hg(t), vapor path, vapor-space volume, pre/post mass}`.

`T_Hg(t)` is promoted from a useful optional descriptor to a **first-class PT transfer coordinate** whenever a separately heated reservoir architecture is used.

The reported `dx/dT_Hg` is composition/apparatus specific and must **not** be used as an x≈0.30 universal control law.

## 3.3 Chen et al. 1991 — separate compensating atmospheres

The same TAC lineage provides a second full experimental realization:

- three-temperature-zone furnace;
- graphite boat with three chambers;
- two growth-solution chambers aligned beneath separate TAC outlets;
- Pd-diffused H2 ambient;
- homogenization around **500 °C** and saturation around **450 °C**;
- first-layer supercooling approximately **5–10 °C** with about **0.16 °C/min** cooling;
- second-layer supercooling approximately **8–17 °C** with about **0.5–1.25 °C/min** cooling;
- explicit reservoir-zone examples: approximately `328 -> 310 °C` for one solution and `318 -> 298 °C` for the other;
- after growth, the wafer was shifted into an empty chamber and cooled under Hg vapor supplied by the reservoir.

### Round-62 consequence

Separate Hg reservoirs demonstrably act as independently programmable thermochemical boundary conditions. Modern apparatus transfer should therefore distinguish:

`T_growth(t)` from `T_Hg,reservoir(t)`

rather than treating a single furnace controller temperature as the complete Hg chemical-potential state.

## 3.4 Radhakrishnan et al. 2003 — wipe/slide-out morphology and post-separation temperature

This full paper is highly consequential because it concerns a horizontal-slider Te-rich HgCdTe/CdZnTe system.

Reported branch:

- Hg0.8Cd0.2Te on Cd0.96Zn0.04Te `(111)B ±0.5°`;
- substrate about **15 × 15 mm²**;
- grown layer about **10 × 10 mm²**;
- layer thickness about **20–40 µm**;
- growth approximately **480–460 °C**;
- cooling approximately **0.5 °C/min**;
- complete wipe-off normally left only one or two residual droplets at the last-drawn edge.

Observed failure physics:

- insufficient wipe clearance causes graphite rubbing and slider scratches;
- non-smooth slide-out can leave a region momentarily under graphite/growth solution and create an additional thin layer or meltback/re-growth texture;
- oxide, graphite particles, microprecipitates and poor wetting can produce voids/pinholes;
- after separation, holding the exposed layer above roughly **350 °C** produced Hg-evaporation points in this branch;
- moving the layer to very cool regions avoided those evaporation points but could deposit black HgTe dust/soot;
- incomplete wipe-off leaves Te-rich solution that rapidly freezes dendritically.

### Round-62 consequence

Round 61 already made wipe mechanics explicit. Round 62 adds two measurable transfer coordinates:

- **wipe clearance / graphite-to-layer interference state**;
- **post-separation layer temperature trajectory** before the surface is safely stabilized.

The approximately 350 °C observation is **PT branch evidence**, not an RP-01 universal limit.

## 3.5 Parker, Weirauch and Chandra 1988 — morphology is hydrodynamic

Although this is not a horizontal slider, it is primary HgCdTe Te-solution LPE evidence that:

- substrate-holder geometry;
- meltback;
- rotation/stirring;
- thermal gradients;
- growth rate;
- obstruction-driven flow

change terracing through the supersaturation and boundary-layer state.

A redesigned low-obstruction holder produced markedly reduced terracing, whereas holder features that disturbed the flow produced position-dependent morphology.

### Round-62 consequence

This does **not** transfer the paper's crucible dimensions into the slider process. It strengthens the requirement that any local slider CAD/recess/wipe study measure morphology against actual melt/wipe hydrodynamic geometry rather than optimizing dimensions independently.

## 3.6 Tranchart et al. 1985 — x≈0.30 substrate/LPE transfer

Directly relevant primary transfer evidence:

- Cd1-yZnyTe with `y≈0.04` used to lattice match Hg1-xCdxTe with `x≈0.30`;
- `(111)` substrate preparation;
- Te-rich LPE of `x≈0.30` material;
- a reported **3-mm liquid-solution thickness** in that apparatus;
- substrate pre-load **2% Br2/methanol** etch;
- liquid heated roughly **15 °C above equilibrium** before the reported branch.

Restriction: the cited process uses the `(111)A` face, not the Round-61 `(111)B` reference branch. The 3-mm liquid depth is an apparatus-specific PT datum and must not be promoted to the RP-01 slider.

---

# 4. CdZnTe substrate qualification

## 4.1 Everson et al. 1995 — executable B-face defect screen

This source closes a major practical substrate-screening ambiguity for `(111)B` CdTe/CdZnTe.

Reported B-face etch:

- `6 cm³ 48% HF : 24 cm³ HNO3 : 150 cm³ lactic acid`;
- ratio `1:4:25`;
- room temperature;
- **2.5 min** immersion;
- **moderate agitation**;
- triangular pits on `(111)B` with approximately **10:1 width:depth**.

The authors validated the pits against dislocations and used the method as a substrate manufacturing screen. An example screening threshold identified material with `EPD < 1×10^5 cm^-2` as high-quality substrate area in that program. Their production sampling concept screened approximately every third to fifth as-sawn slice before final substrate manufacture.

### Round-62 consequence

P29 may now carry an **explicit PT B-face defect-screening branch** rather than only generic EPD language. The `1×10^5 cm^-2` value is a transfer screening criterion, not an RP-01 incoming-material specification.

## 4.2 Tobin et al. 1995 — lattice matching must include growth temperature

Primary results show:

- crosshatch/misfit-dislocation morphology tracks HgCdTe/CdZnTe lattice mismatch;
- near-perfect room-temperature matching around `+0.003%` gives a strong minimum in crosshatch/EPD;
- the crosshatch-free region can lie around a small positive room-temperature mismatch (~`0.02%`) because room-temperature and growth-temperature matching differ;
- EPD values as low as about `1×10^4 cm^-2` were reported near ideal matching.

### Round-62 consequence

P29 should distinguish:

`mismatch_RT` from `mismatch_Tgrowth`.

A single room-temperature lattice parameter is not a complete growth-compatibility descriptor.

## 4.3 Bruder et al. 1990 — orientation and defect metrology transfer

Relevant PT evidence includes:

- CdZnTe vertical Bridgman substrate manufacture;
- `(111)` orientation using etch features followed by X-ray confirmation;
- routine orientation accuracy about **±0.3°**;
- lapping/polishing followed by Br2/methanol chemimechanical treatment;
- EPD mapping, X-ray topography and rocking-curve characterization.

Use as an incoming-substrate metrology lineage only; do not import the Bridgman growth apparatus into RP-01 fabrication.

## 4.4 Riedinger et al. 1992 — chemimechanical polishing mechanics

CdTe `(110)` transfer evidence shows:

- Br2/methanol chemimechanical etch rate approximately linear with bromine concentration in the investigated range;
- better surface morphology at low Br2 concentration with direct polishing-pad contact;
- defined mechanical removal before chemical-mechanical polish.

Because material face and apparatus differ, this remains a PT surface-preparation mechanics source rather than a direct `(111)B CdZnTe` recipe.

---

# 5. Hg-rich low-temperature anneal

## 5.1 Chandra, Schaake and Kinch 2003

This full paper materially strengthens the physical model used by P31/P23.

Primary results:

- Hg-saturated anneal kinetics depend strongly on:
  1. starting metal-vacancy/excess-Te concentration;
  2. alloy composition `x`;
  3. anneal temperature;
- experimentally measured converted/annealed skin depth is approximately proportional to `sqrt(t)`;
- the rate coordinate can be written in diffusion-like form using `x_B²/t`;
- at fixed temperature the rate decreases strongly with increasing CdTe fraction over the investigated range;
- the rate is approximately inverse in the starting metal-vacancy/excess-Te concentration in the reported treatment;
- x≈0.28 temperature-series data produced an activation energy of about **1.1 eV**, consistent with an earlier ~1-eV diffusion estimate for x≈0.2;
- systematic Hg-saturated studies included 225 °C and 270 °C branches and multiple compositions.

### Round-62 consequence

The protocol should explicitly preserve a diffusion-like development coordinate:

`K_ann ∝ x_B²/t`

with `K_ann = F(x, T, starting vacancy/excess-Te state, boundary condition)`.

A fixed dwell time is therefore not portable across composition or initial defect state.

No universal 250 °C time is created from this paper.

## 5.2 Astles 250 °C / 48 h branch

Astles provides a separate primary-transfer example of sealed evacuated silica ampoules containing liquid Hg, typically **250 °C / 48 h**, used to remove as-grown Hg vacancies before 77-K Hall characterization.

This broadens the empirical prior around the Round-61 250 °C screening center but does not replace the local anneal-state mapping program.

---

# 6. Native anodic oxide

## 6.1 Stahle/Helms et al. 1989

Primary conditions:

- HgCdTe `x≈0.20–0.22`;
- 0.1 M KOH in `90% ethylene glycol / 10% DI water`;
- constant current density **0.3 mA/cm²**;
- anodic oxide grown to approximately **700 Å** in the studied specimens.

Interface structure for an approximately 700-Å oxide:

- thin approximately **30–50 Å CdTeO3-rich layer** adjacent to HgCdTe;
- thicker mixed interfacial region containing Cd/Te/Hg oxide components and HgTe-like particles before the bulk oxide.

### Round-62 consequence

This strongly supports the Round-61 chemistry/current-density center and adds a physical-interface interpretation. It does not provide the missing RP-01 cell geometry.

## 6.2 Nemirovsky and Kidron 1979

Primary anodization branch:

- 0.1 M KOH;
- `90% EG / 10% H2O`;
- constant current density **0.5 mA/cm²**;
- **carbon counter electrode**;
- anodization completed at **constant voltage**, reported to improve dielectric quality and oxide-thickness control;
- studied oxide thicknesses roughly **250–1250 Å**.

The paper also reports positive fixed oxide/interface charge and shows strong sensitivity of surface properties to anodization conditions and final thermal treatment.

### Round-62 consequence

Protocol 10 should distinguish two electrical phases when this lineage is adopted:

1. galvanostatic oxide formation;
2. controlled constant-voltage completion/termination.

Round 61 already records `J(t), V(t), Q/A, d_ox`; Round 62 strengthens the rationale for treating the voltage trajectory/termination mode as part of the recipe.

## 6.3 Ngoc and Nha 1998

Primary transfer conditions:

- room-temperature anodization;
- `J=0.2–0.5 mA/cm²`;
- 0.1 M KOH / 90% EG / 10% water;
- **platinum** counter electrode in this branch;
- oxide thicknesses up to ~150 nm;
- 77-K C-V interface characterization.

Representative electrical results include midgap fast-state density on the order of `7×10^10 eV^-1 cm^-2` and positive fixed oxide/interface charge in the studied samples.

### Round-62 consequence

Counter-electrode material is demonstrably not unique across primary HgCdTe anodization lineages. Carbon remains the stronger transfer match for the Round-61 branch, while Pt is retained as PT evidence that electrode material/geometry must be recorded rather than assumed.

---

# 7. RIE conversion and LBIC

## 7.1 Siliquini et al. 1997 — full physical state

Primary same-UWA-lineage experiment:

- vacancy-doped p-type Hg0.69Cd0.31Te on CdZnTe;
- Plasma Technology parallel-plate reactor;
- sample mounted on cathode;
- cathode temperature held at **18 °C**;
- H2 **27 sccm**;
- CH4 **5 sccm**;
- pressure **410 mTorr**;
- RF power density **0.4 W/cm²**;
- dc bias approximately **180 V** in the paper's printed convention;
- RIE duration **1 min**;
- physical recession about **0.2 µm**.

LBIC implementation:

- diode-pumped Nd:YLF laser at **1.047 µm CW**;
- focused spot about **3 µm**;
- stage step about **2.5 µm**;
- two remote contacts about **5 mm** apart;
- measurements reported at room temperature in this paper;
- circular RIE region about **300 µm diameter**;
- sequential 0.1% Br2/methanol depth stripping gave disappearance of the LBIC junction signature after about **1.6 µm** total removal, placing the electrical conversion depth near **1.5 µm**;
- the best-fit converted-region model used a net donor-minus-acceptor density near **1×10^15 cm^-3** with electron mobility near **5×10^3 cm²/V·s at 300 K**.

### Round-62 consequence

This is strong `SL` evidence that forward power or nominal etch depth is not a sufficient transfer coordinate. It directly supports the P34 requirement for self-bias/thermal/gas/pressure state and the separation of:

`d_etch != d_conv`.

It also provides a full-method LBIC branch, but it must **not overwrite** P37's separate 80-K/1.047-µm same-lineage implementation from Musca et al. 1998. The two experiments are distinct and should be preserved as such.

---

# 8. Metallization/contact noise

## Beck, Davis and Goldberg 1990

Primary transfer findings:

- Au and Al contacts to ion-sputtered p-Hg0.79Cd0.21Te were ohmic across the studied temperature range, while Ge contacts on x≈0.30 material were partially rectifying;
- specific contact resistance varied strongly between contacts and remained comparatively weakly temperature dependent down to cryogenic temperatures in the reported samples;
- circular contact pads of **10, 30, 100 and 300 µm** diameter were studied;
- 1/f resistance-noise scaling differed strongly by metal/contact diameter;
- Au-contact noise behavior was consistent with a dominant interface/underlying-HgCdTe contribution, while Al showed a different surface-conduction scaling;
- measured contact 1/f noise was substantially above simple fundamental expectations.

### Round-62 consequence

P09/P12 should retain contact noise as a possible independent contributor even when DC contact resistance is acceptable. This paper is PT only: its ion-sputtered p-type Au contact is not the RP-01 RIE-converted n-type Cr/Au stack.

---

# 9. Cryogenic package thermal conductance

## Bartoli et al. 1976

This paper directly studies bonding-layer thermal conductance in HgCdTe photoconductor arrays.

Experimental example:

- twelve-element linear Hg0.8Cd0.2Te array;
- **200 × 200 µm** detector element;
- Irtran-2 substrate;
- **200 µs CO2-laser pulse** at **16.5 W/cm²**;
- detector temperature inferred from resistance during thermal recovery.

Thermal model/result:

- short-time response (milliseconds) is dominated by the detector-to-substrate epoxy layer;
- long-time response (tens to hundreds of milliseconds) is dominated by the substrate-to-sink varnish layer;
- fitted epoxy thermal conductance per area `k'/d1 ≈ 3.2 W cm^-2 K^-1`;
- fitted varnish conductance per area `k''/d2 ≈ 0.9 W cm^-2 K^-1`;
- the paper demonstrates that the two layers can be separately identified from different recovery-time regions;
- transverse conduction makes array elements depart from a simple 1-D single-element model.

### Round-62 consequence

Round 61 currently states only that HgCdTe PC package poles can lie on ms-to-hundreds-ms scales. Round 62 adds a **quantitative PT conductance prior and extraction method**.

Do not use the 3.2/0.9 values as Dow Corning 3110 or RP-01 package constants; the adhesives/substrate stack differ.

---

# 10. FTIR composition/thickness mapping

## 10.1 Gopal, Ashokan and Dhar 1992

For `0.2 < x < 0.3` HgCdTe epilayers, this source explicitly shows that the 50%-transmission edge coordinate depends on **layer thickness**. It uses the Hougen transmission model and compares composition inferred from two different edge descriptors as an index of composition uniformity.

### Round-62 consequence

This directly supports Round 57/61's rule that a scalar `lambda_50` cannot substitute for a full composition/thickness inversion and that edge descriptors must remain distinct outputs.

## 10.2 Chang et al. 2005

Primary metrology transfer implementation:

- infrared microscope connected to a Thermo Nicolet 870 FTIR;
- computerized x-y mapping stage;
- adjustable beam aperture, with the reported instrument capable of tens-of-micrometre-scale beam footprints and a 100-µm aperture used for large-area mapping;
- LN2-cooled LWIR HgCdTe detector;
- KBr beamsplitter and Ever-Glo source;
- interference-matrix optical model;
- Fourier-transformed spectral fit used for first thickness guesses;
- untransformed spectrum subsequently fit with Levenberg-Marquardt plus simulated annealing;
- composition and thickness solved self-consistently.

### Round-62 consequence

This is strong PT evidence for automated spatial FTIR mapping and self-consistent `x,d` inversion. It does not make the MBE-specific optical assumptions identical to the LPE/Hougen Round-57 forward model.

---

# 11. Evidence-state changes caused by Round 62

| Coordinate / issue | Round-61 state | Round-62 state |
|---|---|---|
| Historical RP-01 graphite grade | OPEN | **OPEN unchanged** |
| HgCdTe-LPE graphite cleaning example | weak/unspecified PT | **PT strengthened:** DFP-2, acid etch, 1-week boiling DI, 500 °C bake, scratch-free hand-polished mating faces |
| Historical LPE numerical dimension stack | OPEN | **OPEN unchanged** |
| Hg-compensation source mass alone | PT geometry-coupled | **PT strengthened:** source/reservoir temperature and vapor path are first-class coordinates |
| Hg loss measurement | qualitative/record mass loss | **PT strengthened:** dummy-cycle gravimetric method and ~0.3 mg/min branch example |
| Slide-out/wipe state | explicit SYN/local | **PT strengthened:** scratch/additional-growth/melt-retention failure mechanisms |
| Post-separation LPE thermal state | mostly implicit | **PT strengthened:** branch-specific Hg-evaporation/soot observations |
| `(111)B` CdZnTe EPD screening | generic metrology | **PT executable branch added** |
| RT lattice match vs growth-T match | implicit | **PT distinction explicit** |
| Anneal kinetics | empirical state map | **PT diffusion-like `x_B²/t` scaling added** |
| Anodization electrical endpoint | J/V/Q trajectory | **PT galvanostatic -> constant-voltage completion branch added** |
| Historical anodization cell geometry | OPEN | **OPEN unchanged** |
| RIE d_etch vs d_conv | SL concept | **SL full-method state strengthened** |
| Historical RP-01 RIE self-bias/electrode geometry | OPEN | **OPEN unchanged** |
| Contact noise | detector/noise decomposition | **PT contact-interface noise branch strengthened** |
| Package thermal pole | PT qualitative/time-scale | **PT numerical conductance prior + extraction method added** |
| FTIR mapping | controlled full-spectrum method | **PT spatial mapping/self-consistent inversion strengthened** |

---

# 12. Important non-promotions

Round 62 deliberately rejects the following tempting inferences:

1. Astles DFP-2 graphite is **not** identified as the historical Honeywell/Fermionics/UWA graphite.
2. Astles cleaning is a valid PT qualification branch, not a universal graphite-cleaning recipe.
3. Chiang/Chen reservoir temperatures are not x≈0.30 control temperatures.
4. Tranchart's 3-mm melt depth is not the RP-01 slider melt depth.
5. Radhakrishnan's ~350 °C post-separation observation is not a universal HgCdTe limit.
6. Everson's `EPD <1×10^5 cm^-2` is a transfer screening criterion, not an RP-01 purchase specification.
7. Chandra's activation energy is a kinetic transfer result, not a license to calculate a unique anneal time without initial vacancy/boundary information.
8. Nemirovsky's constant-voltage completion does not establish the exact TI/RP-01 termination voltage history.
9. Siliquini's `180 V` dc-bias state is not the RP-01 100-mTorr/50-W self-bias.
10. Bartoli's epoxy/varnish conductances are not Dow Corning 3110 or RP-01 package constants.
11. Beck's Au-contact noise scaling is not the same interface as Cr/Au on the RIE-converted RP-01 contact region.
12. Chang's MBE optical stack/model is not silently substituted for the controlled LPE/Hougen forward model.

---

# 13. Remaining highest-value documentary targets

After this acquisition pass, the documents most likely to change remaining `OPEN` coordinates are narrower than before:

1. Suh et al., slider LPE precise-composition-control paper — full apparatus/process text still not recovered in this batch.
2. Shinohara et al., Hg-loss compensation and wiping-off paper — already represented conceptually in the repository, but the full paper was not supplied in this batch.
3. Honeywell/Fermionics/UWA original boat machine drawings, laboratory notebooks or apparatus photographs with scale.
4. Original TI anodization-cell drawings/electrode-spacing records.
5. Historical UWA Plasma Technology reactor model/manual/run sheets giving electrode geometry and self-bias.
6. Original RP-01 evaporator/QCM/source geometry.
7. Original RP-01 cryostat/package/readout implementation.
8. Full same-UWA 1998 doping-density/LBIC and related depth-characterization papers where not already archived locally.

Another broad literature sweep is not justified before these targeted records are pursued.

---

# 14. Publication consequence

Round 61 remains the current **typeset publication artifact**. Round 62 is the controlling post-publication documentary evidence layer until a new typeset revision is generated.

A future Round-62/63 manuscript integration should change only the statements identified in this document and its gap/source-ledger companions. It should not re-open already closed Round-57/61 metrology definitions or reintroduce demoted synthetic apparatus dimensions.
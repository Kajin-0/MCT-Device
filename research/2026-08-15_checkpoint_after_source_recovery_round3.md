# Recovery checkpoint — source-recovery round 3 after P16

**Date:** 2026-08-15 America/New_York  
**Current checkpoint:** yes. Read after the through-P16, round-1 and round-2 checkpoints.

This file records the third targeted source-recovery round. Major outcomes are P01A (wet-mesa full experimental extraction), P02B (composition-matched x≈0.30 anodization lineage), and synchronized gap/source-ledger addenda.

## 1. P01 wet mesa — full primary experimental section audited

Primary source:

V. Srivastav et al., “Etching of Mesa Structures in HgCdTe,” *Journal of Electronic Materials* 34, 1440–1445 (2005), DOI `10.1007/s11664-005-0203-5`.

### Direct experimental details newly captured

Material/sample preparation:

- HgCdTe `x=0.28`;
- material sourced from SMALL Enterprises, Ukraine;
- diced using wire saw and mounted on sapphire;
- mechanical lapping/polishing using decreasing alumina grit;
- chemomechanical polishing;
- final nominal `0.1% Br2 in methanol` free etch for `1 min` before patterned studies;
- surface inspected with Nomarski microscopy and ellipsometry at `6328 Å`.

Test geometry:

- ~600-µm linear test structures with `50 µm` trenches;
- 2-D mesa structures separated by `30 µm` trenches.

Etchant study:

- Br2/HBr/ethylene-glycol family;
- nominal Br2 concentration varied from 1–3%;
- EG fraction in HBr varied 0→1;
- selected nominal optimum `2% Br2 in 3:1 EG:HBr`;
- process temperature studied `5–50 °C`;
- reference process near `21 °C`.

Metrology/performance:

- vertical depth/rate measured by Dektak profilometry;
- lateral undercut/rate measured by high-magnification phase-contrast microscopy;
- anisotropy `A=1-R_L/R_V`;
- mean source vertical rate near `2.78 µm/min`;
- source run/process variation about `±26%`;
- mean anisotropy about `0.63 ±11%`;
- RMS roughness about `2–7 nm`, best ~2 nm;
- activation energy ~`7.5 kcal/mol`;
- etch rate approximately doubles per +10 °C over investigated range;
- lower process temperature improves profile control and reduces photoresist attack;
- Br2 evaporation/concentration drift explicitly identified as a reproducibility problem.

### Critical negative result: “2% Br2” basis is genuinely absent

The full accessible primary text was audited. It repeatedly uses:

- nominal `0.1% Br2/methanol`;
- Br2 range `1–3%`;
- selected `2% Br2`;

but never defines:

- w/v;
- v/v;
- wt%;
- mol%;
- actual Br2 mass/volume and final solution mass/volume.

Thus P01’s concentration-basis blocker is a genuine omission in the available primary text, not merely an abstract/indexing problem.

Do not guess the convention.

### Derived RP-01 timing scale — diagnostic only

For RP-01's 9.5-µm HgCdTe layer and source mean rate:

`9.5/2.78 ≈ 3.42 min`.

Using the source ±26% rate spread:

- slow edge ~2.06 µm/min → ~4.62 min;
- fast edge ~3.50 µm/min → ~2.71 min.

This is strong evidence that a fixed timed etch without endpoint/local rate control is inadequate. These are **not** recipe setpoints.

Created:

- `procedures/P01A_SRIVASTAV_PRIMARY_EXPERIMENTAL_ADDENDUM.md`.

## 2. P02 native anodic oxide — composition-matched x≈0.30 lineage recovered

Primary source identified:

B. K. Janousek and R. C. Carscallen, “The mechanism of (Hg,Cd)Te anodic oxidation,” *Journal of Applied Physics* 53(3), 1720–1726 (1982).

Composition-explicit companion source:

B. K. Janousek and R. C. Carscallen, “Hg0.70Cd0.30Te anodic oxidation,” *Journal of Vacuum Science & Technology* 21, 442 (1982), DOI `10.1116/1.571674`.

### Direct primary mechanism conclusions

The x≈0.30 Janousek/Carscallen lineage establishes:

- initial anodic film formation by dissolution–precipitation;
- subsequent bulk oxide growth;
- mass transport/stirring materially affects whether initial film forms;
- at sufficiently low current density stirring can suppress oxidation by removing dissolved species before precipitation;
- increasing pH increases oxide solubility and permits sustained semiconductor dissolution to larger current density;
- starting surface / initial oxide formation affects final interface electronic properties;
- electroetch integrated into passivation can lower fixed oxide charge by removing the TeO2-rich layer associated with Br2/methanol preparation.

### Detailed x=0.30 conditions recovered through Talasek synthesis

Robert T. Talasek's 1992 technical chapter explicitly attributes the following experiment to Janousek/Carscallen reference 32:

- n-type slush-grown `x=0.30` material;
- extensive nominal `5% Br2 in methanol` etch;
- approximately `20 µm` semiconductor removed;
- electrolyte `0.1 N KOH in 90% ethylene glycol / 10% water`;
- constant-current anodization at multiple current densities;
- voltage-time behavior with an induction period;
- at sufficiently low current density the induction period can become effectively infinite;
- stirring can prevent oxidation at low current density.

Evidence grade for these detailed bullet values:

`SECONDARY-A explicitly attributed to a composition-matched primary experiment`.

Do **not** relabel them as directly read `[P]` until the complete 1982 experimental section is acquired.

The archived reproduction of the constant-current figure is too degraded to recover reliable current-density labels. No numerical values were inferred from it.

### Why this matters for RP-01 P02

The TI Catagnus/Baker direct process remains the strongest executable 800-Å disclosure:

- `0.1 M KOH`;
- `90% EG / 10% DI water`;
- constant current ~`0.3 mA/cm²`;
- endpoint ~`15 V`;
- ~`2 min`;
- ~`800 Å` oxide.

Independent x≈0.20 primary work brackets the same family at about `0.2–0.5 mA/cm²`.

The Janousek/Carscallen work now establishes that the same electrolyte family and constant-current mechanism were used on composition-matched `x=0.30` HgCdTe. This makes the TI process a substantially better-grounded local qualification center, while still **not proving it was the exact UWA RP-01 recipe**.

### New controlled P02 variables

P02 must explicitly log/qualify:

- complete voltage-time trace;
- induction time `t_ind`;
- growth-regime `dV/dt`;
- current density;
- integrated charge per area `Q/A`;
- terminal formation voltage;
- independent final oxide thickness;
- bath temperature;
- stirred/unstirred state and agitation rate if any;
- electrode/sample geometry;
- surface-preparation history;
- electrolyte batch/age;
- rinse/dry and elapsed time to next process;
- post-passivation electrical/interface behavior;
- compatibility with P08 oxide opening and final 1/f-noise behavior.

### Important surface-prep warning

The composition-matched x=0.30 mechanistic study's ~20-µm Br2/methanol material removal must **not** be transplanted to RP-01's 9.5-µm LPE epilayer. It is mechanistic evidence on bulk/slush material, not an RP-01 surface-prep recipe.

Created:

- `procedures/P02B_X030_ANODIZATION_LINEAGE_ADDENDUM.md`.

## 3. RIE state from round 2 remains important

P08B correction remains in force:

RP-01's `2.0×10^15 cm^-3` RIE density is explicitly averaged over converted thickness.

Conditional sheet-density scale:

- if d_conv=8 µm → `N_s≈1.6×10^12 cm^-2`;
- if full 9.5 µm → `N_s≈1.9×10^12 cm^-2`.

Qualify `{R_sheet/N_s, µ_H/multicarrier state, d_conv, L_conv, d_etch, rho_c}`, not volume density alone.

P08A gas-ratio evidence remains:

- direct RP-01 `CH4/5H2`, total 64 sccm;
- secondary same-lineage review supports `CH4:H2=1:5`;
- conditional derived split 10.6667 / 53.3333 sccm;
- primary individual MFC closure still open.

## 4. P13 same-UWA temporal source from round 2 remains important

Rajaduray 1998 UWA thesis, supervised John Dell with Redfern/Smith assistance:

- n-type x≈0.30 HgCdTe;
- ~77 K under vacuum;
- transient photoconductive decay;
- bias intentionally kept small to avoid sweeping photocarriers into high-recombination contacts.

This is direct same-lab support for the P13 low-field lifetime gate.

## 5. Repository synchronization completed in round 3

Created/updated:

- `procedures/P01A_SRIVASTAV_PRIMARY_EXPERIMENTAL_ADDENDUM.md`;
- `procedures/P02B_X030_ANODIZATION_LINEAGE_ADDENDUM.md`;
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND3.md`;
- `docs/SOURCE_LEDGER_ADDENDUM_ROUND3.md`;
- this checkpoint.

The round-3 gap addendum takes precedence for P01/P02/P08/P13 rows where the older monolithic matrix is stale.

## 6. Current highest-impact blockers

### Frontside chemistry

1. exact Br2 percentage basis for P01, or explicitly define/qualify a new local formulation;
2. exact UWA RP-01 anodization electrolyte/current/endpoint/rinse;
3. full Janousek/Carscallen experimental section / exact current-density/cell data;
4. exact Mask-1/Mask-2 resist, spin, exposure, developer and development time;
5. historical Cr/Au base pressure/rates, RIE-to-metal delay and lift-off sequence.

### RIE

6. primary confirmation of CH4:H2 ratio / individual MFCs;
7. exact Musca-1998 conditions tied to ~8-µm conversion depth;
8. reactor electrode geometry, RF frequency, self-bias and sample temperature.

### Upstream

9. x≈0.30 source synthesis/homogenization;
10. exact selected CdZnTe polarity/miscut and surface preparation;
11. x≈0.30 LPE thickness-versus-time relationship;
12. Hg anneal pHg/time/cooldown that reproduces RP-01 transport state.

### Historical characterization

13. exact contact pair/gap used for Figures 3/5/6/7;
14. historical low-noise preamplifier and RBW/ENBW settings;
15. package/interconnect construction.

## 7. Recommended next work

The next research pass should avoid metadata-only loops and prioritize one of:

1. patent/proceedings/source-family recovery for exact UWA lithography and Cr/Au deposition;
2. local P01/P02 qualification-DOE design where historical source closure has reached a practical ceiling;
3. full Janousek/Carscallen acquisition through an accessible archive if found;
4. same-lineage HgCdTe photoconductor papers that explicitly state inherited photoresist/developer/preamp details;
5. upstream LPE thickness-time and post-growth anneal closure.

If a new numerical process value is introduced, record its provenance immediately and update the appropriate Pxx module plus checkpoint/gap state.

## 8. Recovery order

A replacement agent should read:

1. `AGENTS.md`;
2. `research/2026-08-15_checkpoint_through_P16.md`;
3. round-1 checkpoint;
4. round-2 checkpoint;
5. **this round-3 checkpoint**;
6. `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND3.md`;
7. `docs/SOURCE_LEDGER_ADDENDUM_ROUND3.md`;
8. relevant Pxx/PxxA/PxxB files;
9. branch-specific dated research notes.

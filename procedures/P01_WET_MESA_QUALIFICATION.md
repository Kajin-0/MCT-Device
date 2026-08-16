# P01 — Wet HgCdTe mesa-isolation qualification

**Status:** `QUALIFICATION-CANDIDATE` — NOT released as the RP-01 production mesa recipe.

**Purpose:** Qualify a bromine/HBr/ethylene-glycol wet mesa process for an x≈0.30 n-HgCdTe photoconductor on an insulating CdZnTe substrate while preserving the as-grown electrical state of the active material.

## 1. Why this process family is being qualified

The RP-01 reference paper specifies wet-chemical mesa delineation before anodic-oxide passivation but does not disclose the wet-etch formulation. A same-group UWA comparison on x=0.31 n-HgCdTe photoconductors explicitly used bromine in hydrobromic acid for the wet-mesa branch and found background-limited detector performance for the wet-processed devices, whereas H2/CH4 RIE mesa processing strongly degraded D*.

A separate primary experimental study by Srivastav et al. systematically optimized Br2/HBr/ethylene-glycol wet mesa etching on x=0.28 HgCdTe. Because x=0.28 is close to RP-01 x≈0.30 and the process is explicitly designed for mesa dimensional control, it is the current strongest process-transfer candidate.

## 2. Provenance tags

- `[P-RP01]` — directly stated by Smith et al. 2001 RP-01.
- `[P-UWA]` — directly stated by the same UWA/Faraone HgCdTe process lineage.
- `[P-SRI]` — directly measured by Srivastav et al., J. Electron. Mater. 34, 1440–1445 (2005), DOI 10.1007/s11664-005-0203-5.
- `[D]` — derived from published quantities.
- `[CAL]` — must be calibrated on the actual apparatus/material lot.
- `[QUAL]` — must pass a qualification experiment before production use.
- `[OPEN]` — not yet closed.

## 3. Reference material state

### RP-01 target material

- detector material: n-type HgCdTe `[P-RP01]`
- nominal composition: x≈0.30 `[P-RP01]`
- epilayer thickness: 9.5 µm `[P-RP01]`
- incoming carrier density: 9.8×10^14 cm^-3 `[P-RP01]`
- incoming electron mobility: 4.0×10^4 cm^2 V^-1 s^-1 `[P-RP01]`
- substrate: electrically insulating CdZnTe `[P-RP01]`

### Qualification-source material

Srivastav et al. used x=0.28 HgCdTe wafers. `[P-SRI]`

**Transfer condition:** The wet etch must be requalified on x≈0.30 RP-01-like coupons. Published etch rate and anisotropy values must not be treated as exact production values before this transfer qualification.

## 4. Published Srivastav preparation sequence

The qualification-source wafers were:

1. diced with a wire saw; `[P-SRI]`
2. mounted/pasted on sapphire; `[P-SRI]`
3. mechanically lapped and polished using decreasing alumina grit sizes; `[P-SRI]`
4. chemomechanically polished; `[P-SRI]`
5. free-etched in 0.1% Br2 in methanol for 1 min; `[P-SRI]`
6. examined by Nomarski microscopy and ellipsometry at 6328 Å to verify a surface free from observable oxide, damage, and contamination. `[P-SRI]`

This is useful process context but is **not automatically the incoming-surface preparation for RP-01**. The final RP-01 substrate/epilayer cleaning SOP remains open.

## 5. Mask geometries used in the qualification-source study

Two diagnostic pattern families were reported:

- 600 µm long linear structures with 50 µm trench width; `[P-SRI]`
- two-dimensional mesas separated by 30 µm trenches. `[P-SRI]`

These patterns were intended to quantify vertical etch rate, lateral undercut, and anisotropy. The exact RP-01 detector mask dimensions remain open.

## 6. Candidate etchant

### Published optimum

Srivastav et al. selected:

- bromine concentration: **2% Br2** `[P-SRI]`
- solvent/reagent ratio: **3:1 ethylene glycol:HBr** `[P-SRI]`
- published characterization temperature: **21 °C** `[P-SRI]`

The corresponding formulation is also described as 2% Br2 in 75% EG / 25% HBr. `[P-SRI]`

### Critical unresolved preparation variable

**The accessible primary-paper text does not unambiguously define the concentration basis for “2% Br2.”** `[OPEN]`

Therefore this document deliberately does **not** convert the published 2% into grams, millilitres, molarity, or mass fraction. Before release, the original laboratory convention or an independent primary source using the identical formulation must establish the preparation basis.

This is a process-release blocker.

## 7. Published etch metrics at/near 21 °C

For the selected 2% Br2, 3:1 EG:HBr formulation:

- mean vertical etch rate: **2.78 µm/min** `[P-SRI]`
- reported run-to-run/process variation in mean etch rate: **±26%** `[P-SRI]`
- mean anisotropy: **0.63** `[P-SRI]`
- reported variation in anisotropy: **±11%** `[P-SRI]`

The paper defines

\[
A = 1 - \frac{R_L}{R_V},
\]

where `R_V` is vertical etch rate and `R_L` is lateral etch rate. `[P-SRI]`

The abstract reports an approximate optimum etch rate of ~2.5 µm/min, anisotropy ~0.6, and RMS surface roughness ~2 nm. `[P-SRI]`

## 8. Temperature sensitivity

Srivastav et al. varied process temperature from 5 °C to 50 °C. `[P-SRI]`

For the selected formulation:

- etch rate approximately doubled for every 10 °C increase; `[P-SRI]`
- measured activation energy was approximately 7.5 kcal/mol; `[P-SRI]`
- high-temperature processing produced poorer/ragged edge quality and increased attack on photoresist; `[P-SRI]`
- lower-temperature processing produced slower etching and better dimensional/profile control; `[P-SRI]`
- an SEM example at 10 °C showed improved feature control relative to the 21 °C example. `[P-SRI]`

**Implication:** Bath temperature is a critical process variable and must be measured at the wafer, not inferred from room temperature. `[QUAL]`

## 9. Required process-control metrology

### Before etch

Record for every coupon/wafer:

- material lot and epilayer run;
- nominal x and measured spectral/compositional metric;
- epilayer thickness map;
- carrier type, n, and mobility from a companion Hall coupon;
- mask/resist lot;
- resist thickness at ≥5 locations;
- pre-etch Nomarski images;
- pre-etch surface roughness on a representative coupon if available;
- bath temperature;
- etchant preparation time and elapsed time before immersion.

### During etch qualification

Because bromine loss by evaporation is identified by Srivastav et al. as a principal source of process drift, each qualification run must record:

- etchant preparation timestamp;
- solution temperature continuously or immediately before/after immersion;
- immersion start/stop time;
- agitation method and cadence `[OPEN/CAL]`;
- exposed HgCdTe area;
- bath volume `[OPEN/CAL]`;
- whether the vessel is open, covered, or otherwise configured `[OPEN/CAL]`.

Do not assume published etch rate is transferable without these controls.

### After etch

Measure:

1. vertical depth with a calibrated stylus profilometer at multiple locations;
2. lateral undercut under high-magnification optical/phase-contrast microscopy or SEM;
3. anisotropy using `A = 1 - R_L/R_V`;
4. RMS roughness with AFM or calibrated profilometry;
5. sidewall morphology by Nomarski and/or SEM;
6. residual epilayer continuity between mesas;
7. Hall/Van der Pauw electrical properties on a companion etched coupon;
8. optional ellipsometry relative to a pre-etch reference surface.

Srivastav et al. used a Veeco Dektak 3 profilometer for depth/roughness-related measurements and high-magnification phase-contrast microscopy for undercut. `[P-SRI]`

## 10. RP-01 electrical-isolation requirement

Because RP-01 uses a 9.5 µm HgCdTe layer on an insulating substrate, mesa isolation logically requires removal of the electrically conducting HgCdTe path between detector elements. `[D]`

The source does **not** specify an RP-01 production overetch depth or safety margin. `[OPEN]`

Therefore:

- the nominal 9.5 µm thickness is **not** to be converted into a fixed timed etch using 2.78 µm/min;
- endpoint must initially be established by measured etch depth on qualification coupons;
- an overetch fraction may only be released after confirming complete electrical isolation without unacceptable lateral loss or surface degradation. `[QUAL]`

A purely arithmetic 9.5 µm / 2.78 µm min^-1 ≈ 3.42 min is only a screening estimate and is explicitly **not a released process time**, especially given the published ±26% rate variation. `[D]`

## 11. Initial qualification matrix

The minimum useful transfer experiment should vary temperature while holding the candidate chemistry fixed after the concentration-basis problem is resolved.

Suggested temperatures to bracket the published behavior:

- 10 °C;
- 15 °C;
- 21 °C.

For each temperature, use at least three nominally equivalent x≈0.30 coupons and measure:

- vertical etch rate;
- lateral etch rate;
- anisotropy;
- RMS roughness;
- CD loss/undercut;
- electrical isolation;
- pre/post Hall properties on companion material.

This matrix is a proposed qualification design `[QUAL]`, not a claim that these temperatures are all acceptable production conditions.

## 12. Candidate acceptance metrics

No production acceptance window is released yet. Initial scientific criteria are:

- complete electrical isolation through the HgCdTe layer;
- no statistically significant degradation of n or mobility outside predefined measurement uncertainty;
- smooth, continuous mesa sidewalls without ragged resist attack;
- reproducible vertical etch depth;
- reproducible lateral undercut compatible with the mask bias;
- RMS surface roughness comparable to the ~2 nm best-case literature result where metrology permits;
- anisotropy near the ~0.6 literature reference unless a deliberately more isotropic profile is selected for metal coverage.

Numerical pass/fail tolerances must be set after the transfer DOE establishes actual process capability.

## 13. Failure modes to log

- excessive lateral undercut;
- edge trenching/notching;
- convex trench-floor profile;
- ragged sidewalls;
- photoresist attack/flow;
- nonuniform depth across the sample;
- rapid run-to-run rate drift;
- incomplete isolation;
- excessive roughness;
- measurable change in Hall carrier concentration/mobility;
- evidence of a Te-rich or otherwise altered surface state requiring additional surface preparation before anodization.

## 14. Safety hold point

Br2 and HBr are highly hazardous corrosive/toxic reagents, and the etched material contains Hg and Cd. This document defines scientific process variables only. Before laboratory execution, the exact formulation, vessel, exhaust, PPE, spill response, waste stream, and exposure controls must be approved under the institution's chemical-hygiene/EH&S procedures and reagent SDS requirements.

## 15. Release blockers

This module remains `QUALIFICATION-CANDIDATE` until all of the following are closed:

1. concentration basis of “2% Br2”;
2. reagent grades and HBr stock concentration;
3. etchant preparation order;
4. bath volume and wafer-area loading rule;
5. agitation rule;
6. exact rinse/quench sequence after mesa etch;
7. compatible Mask-1 resist and minimum thickness;
8. x≈0.30 transfer data;
9. depth/overetch window required for complete isolation of a 9.5 µm epilayer;
10. dimensional-control acceptance window;
11. electrical-property preservation acceptance window.

## 16. Primary sources

1. E. P. G. Smith, C. A. Musca, D. A. Redfern, J. M. Dell, L. Faraone, “H2-based dry plasma etching for mesa structuring of HgCdTe,” *Journal of Electronic Materials* 29, 853–858 (2000), DOI `10.1007/s11664-000-0237-7`.
2. V. Srivastav, R. Pal, B. L. Sharma, A. Naik, D. S. Rawal, V. Gopal, H. P. Vyas, “Etching of Mesa Structures in HgCdTe,” *Journal of Electronic Materials* 34, 1440–1445 (2005), DOI `10.1007/s11664-005-0203-5`.
3. E. P. G. Smith, K. J. Winchester, C. A. Musca, J. M. Dell, L. Faraone, “A simplified fabrication process for HgCdTe photoconductive detectors using CH4/H2 reactive-ion-etching-induced blocking contacts,” *Semiconductor Science and Technology* 16, 455–462 (2001), DOI `10.1088/0268-1242/16/6/306`.

# Source ledger addendum — Round 21 empirical wet-mesa recovery

**Date:** 2026-08-16 America/New_York  
**Scope:** P01/P01A/P28 wet chemical mesa isolation, formulation convention, bath drift, endpoint and post-etch surface state.

This ledger records direct evidence, transfer evidence and unresolved formulation fields. It deliberately does not assign a concentration basis where the primary source does not provide one.

---

## R21-S1 — canonical RP-01 paper

E. P. G. Smith, K. J. Winchester, C. A. Musca, J. M. Dell, L. Faraone, “A simplified fabrication process for HgCdTe photoconductive detectors using CH4/H2 reactive-ion-etching-induced blocking contacts,” *Semiconductor Science and Technology* 16 (2001) 455–462. DOI `10.1088/0268-1242/16/6/306`.

**Class:** `DIRECT-RP01`.

Directly supports:

- wet chemical mesa delineation is used;
- mesa is formed before anodic oxide;
- active HgCdTe thickness is approximately 9.5 µm.

Does **not** disclose:

- wet etchant composition;
- Br2/HBr/EG formulation;
- temperature/time;
- endpoint/overetch;
- rinse/dry;
- Mask-1 lithography details.

---

## R21-S2 — same-UWA x=0.31 wet-versus-dry mesa detector comparison

E. P. G. Smith, C. A. Musca, D. A. Redfern, J. M. Dell, L. Faraone, “H2-based dry plasma etching for mesa structuring of HgCdTe,” *Journal of Electronic Materials* 29 (2000) 853–858. DOI `10.1007/s11664-000-0237-7`.

**Class:** `SAME-UWA-WET-MESA`.

Recovered direct functional evidence:

- n-type x=0.31 HgCdTe photoconductive detectors;
- comparison of H2/CH4 RIE with wet chemical etching using bromine in HBr;
- at 80 K / 3 µm / stated 60° FOV, wet-processed devices reached background-limited performance;
- reported wet-device `D_lambda*≈2.5×10^11 cm Hz^1/2 W^-1`;
- dry-plasma branch approximately `1.0×10^10` under the reported comparison.

**Use:** strong same-UWA device-level support for wet mesa isolation near RP-01 composition.

**Restriction:** does not disclose exact wet formulation.

---

## R21-S3 — same-UWA electrical-damage comparison

E. P. G. Smith, C. A. Musca, D. A. Redfern, J. M. Dell, L. Faraone, “Reactive ion etching for mesa structuring in HgCdTe,” *Journal of Vacuum Science & Technology A* 17 (1999) 2503, DOI `10.1116/1.581988`.

**Class:** `SAME-UWA-WET-MESA`.

Recovered process conclusion:

- bromine-based wet chemical mesa profiles are isotropic relative to the RIE branch;
- LBIC found no significant electrical-property modification for chemically etched HgCdTe in the comparison;
- RIE produced strong doping/type-conversion effects.

**Use:** supports P28 electrical-preservation gate and wet-process selection.

---

## R21-S4 — Srivastav et al. 2005 x=0.28 systematic mesa study

V. Srivastav, R. Pal, B. L. Sharma, A. Naik, D. S. Rawal, V. Gopal, H. P. Vyas, “Etching of Mesa Structures in HgCdTe,” *Journal of Electronic Materials* 34 (2005) 1440–1445. DOI `10.1007/s11664-005-0203-5`.

**Class:** `PRIMARY-X028-MESA`.

Direct experimental details recovered from the primary article:

Starting material/preparation:

- x=0.28 HgCdTe;
- material from SMALL Enterprises, Ukraine;
- wire-saw dicing;
- mounted/pasted on sapphire;
- alumina lapping/polishing with decreasing grit;
- chemomechanical polish;
- nominal `0.1% Br2/methanol` free etch for `1 min`;
- Nomarski microscopy + Gartner ellipsometry at `6328 Å` used to assess oxide/damage/contamination.

Test geometry:

- ~600-µm linear structures, 50-µm trench width;
- 2D mesas separated by 30-µm trenches.

Phase-I/II variables:

- nominal Br2 from 1% to 3%;
- EG fraction in HBr from 0 to 1;
- T from 5 °C to 50 °C after selecting the chemistry.

Selected condition:

- nominal `2% Br2`;
- `3:1 EG:HBr`;
- figure caption also states `2% Br2 + 75% EG + 25% HBr`;
- 21 °C reference measurements.

Quantitative output:

- mean vertical rate ~2.78 µm/min in preliminary process-uniformity work;
- about ±26% rate variation;
- anisotropy ~0.63 with ~±11% variation;
- definition `A=1-R_L/R_V`;
- RMS roughness ~2–7 nm, lowest near ~2 nm for the selected/high-EG chemistry;
- apparent activation energy ~7.5 kcal/mol;
- rate approximately doubles per +10 °C over studied range;
- lower-T etch produces better geometric control and less resist attack;
- SEM at 10 °C demonstrates improved feature geometry compared with 21 °C example.

Mechanism/process-control findings:

- Br2 concentration increases etch rate;
- increasing EG lowers rate through viscosity/free-Br chemistry;
- HBr acts as acidic dissolution medium;
- Br2 evaporation is identified as a source of process drift;
- agitation/viscosity/mass transport are kinetic variables;
- agitation of viscous solution assists removal/transport of reaction products;
- actual reported agitation method/rate is not specified in accessible text;
- high temperature attacks photoresist and worsens edge quality;
- ellipsometry found negligible apparent composition change for Br2/EG/HBr under the study metric, while Br2/HBr without EG appeared probably Te-rich; authors treat this surface conclusion qualitatively.

**Critical missing fields in the full accessible article:**

- basis of `2% Br2`;
- basis of `3:1`/75:25 liquid preparation;
- HBr stock assay;
- reagent-addition order;
- actual agitation method/rate;
- post-etch quench/rinse/dry sequence.

---

## R21-S5 — Leech/Gwynn/Kibel explicit w/w Br:HBr convention

P. W. Leech, P. J. Gwynn, M. H. Kibel, “A selective etchant for Hg1−xCdxTe, CdTe and HgTe on GaAs,” *Applied Surface Science* 37 (1989) 291–298. DOI `10.1016/0169-4332(89)90491-1`.

**Class:** `PRIMARY-CONVENTION-TRANSFER`.

Directly reports comparison against:

`0.1% (w/w) Br:HBr`.

**Use:** direct primary proof that weight/weight bromine notation existed in HgCdTe/HBr etch literature.

**Restriction:** different etchant study/material architecture; does not establish Srivastav `2%` as w/w.

---

## R21-S6 — CN101740502B explicit volume-ratio Br2:HBr process

CN101740502B, “Photosensitive element array forming method of mercury cadmium telluride micro-mesa infrared detection chip.”

**Class:** `PRIMARY-CONVENTION-TRANSFER`.

Directly reports:

- photoresist mask 1–6 µm;
- Br2:HBr etchant with an explicitly stated **volume proportion** `0.1–1% : 1`;
- etchant delivered using a spin-coating-like process at 1000–4000 rpm for 10–40 s;
- etching time 5–150 s;
- DI-water cleaning after etch;
- acetone photoresist removal.

**Use:** direct primary evidence that a volume-defined Br2/HBr convention and DI-water rinse exist in HgCdTe processing.

**Restriction:** different micro-mesa architecture/application; not Srivastav/RP-01 formulation or rinse.

---

## R21-S7 — US6657194B2 / US20030160172A1 Br/HBr mesa branch

“Multispectral monolithic infrared focal plane array detectors.”

**Class:** `PRIMARY-CONVENTION/PROFILE-TRANSFER`.

Recovered practical process information:

- ~5-µm photoresist mask;
- Br/HBr mesa etch;
- preferred statement `4% bromine in HBr acid`;
- considerable lateral etch/undercut;
- mesa sidewall slope ~45° and desired 40–50° range for metal step coverage in that architecture;
- later cleaning branches include dilute Br/methanol and flowing DI water.

**Use:** confirms Br/HBr mesa process and thick-resist/sidewall-profile engineering in HgCdTe.

**Restriction:** concentration basis not explicit in recovered passage; different detector architecture.

---

## R21-S8 — US20030102432A1 timed Br/HBr transfer examples

“Monolithic infrared focal plane array detectors.”

**Class:** `PRIMARY-PROCESS-TRANSFER`.

Recovered examples include:

- `2% bromine in hydrobromic acid` for about `3–5 min` in one material-removal step;
- a later `4% bromine in HBr` treatment for a few seconds to form approximately 40–50° mesa sidewall/profile in that architecture;
- acetone photoresist removal followed by a separate 0.05% Br/methanol cleaning branch.

**Use:** demonstrates real HgCdTe Br/HBr processing times/profile control.

**Restriction:** different multilayer structure and unclosed concentration basis; do not transfer its 3–5 min as RP-01 mesa time.

---

## R21-S9 — US4436580A chemistry-specific bromine quench sequence

“Method of preparing a mercury cadmium telluride substrate for passivation and processing.”

**Class:** `PRIMARY-RINSE-TRANSFER`.

Directly reports for its bromine-methanol/DMF surface preparation:

- a `2% bromine / 98%` bromine-methanol example explicitly identified as `(V/V)`;
- etch ~20–45 s;
- methanol quench for bromine-methanol or DMF quench for bromine-DMF until bromine removed;
- acetone + methanol rinse;
- immediate dry nitrogen.

**Use:** demonstrates that bromine percentage basis can be explicitly v/v and that post-etch quench is chemistry-specific.

**Restriction:** not Br2/EG/HBr. Do not import its solvent quench to P28.

---

## R21-S10 — Sporken et al. 2009 surface/air-exposure study

R. Sporken, R. Kiran, T. Casselman, F. Aqariden, S. Velicu, Y. Chang, S. Sivananthan, “The effect of wet etching on surface properties of HgCdTe,” *Journal of Electronic Materials* 38 (2009) 1781–1789. DOI `10.1007/s11664-009-0844-x`.

**Class:** `PRIMARY-SURFACE-TRANSFER`.

Direct findings:

- MBE and LPE HgCdTe surfaces studied by AFM/XPS after Br:methanol and HBr:H2O2:H2O etches;
- minority-carrier lifetime/surface recombination measured;
- measurements repeated after air exposure from hours to days;
- Br-based etchants produced elemental Te which oxidized rapidly in air;
- elemental Te correlated with higher surface recombination velocity;
- surface recombination changed with air exposure;
- authors emphasize need for suitable passivation for stability.

The paper gives quantitative transfer examples for one LPE sample, including initially higher surface recombination for Br-based etchants than the HBr-based comparison.

**Use:** justifies recording P28-to-P25 air time and making surface/passivation outcome part of mesa release.

**Restriction:** different etchant chemistries; does not contradict Srivastav's qualitative ellipsometry observation for Br2/EG/HBr.

---

## R21-S11 — Shimanoe/Sakashita 1991 Br2/methanol surface study

K. Shimanoe, M. Sakashita, *Japanese Journal of Applied Physics* 30 (1991) 2723–2729. DOI `10.1143/JJAP.30.2723`.

**Class:** `PRIMARY-SURFACE-TRANSFER`.

Recovered primary/institutional conclusions:

- chemically etched HgCdTe after Br2/methanol can be Te-rich;
- surface oxide amount depends on Br2 concentration;
- surface electrochemical treatment can change/remove oxide/elemental-Te state.

**Use:** reinforces post-bromine surface-state control.

**Restriction:** bromine/methanol, not P28 chemistry.

---

## R21-S12 — Vanya Srivastav IISc thesis record

Vanya Srivastav, *Modelling, Fabrication and Characterization of HgCdTe Infrared Detectors for High Operating Temperatures*, IISc thesis repository record; file `G25544.pdf` (~19 MB).

**Class:** `PRIMARY-THESIS-IDENTIFIED / FULL-PROCESS-TEXT-NOT-RECOVERED`.

The institutional record and thesis file identity are recovered.

The current accessible search path did not expose the thesis experimental text needed to resolve:

- Br2 percentage basis;
- HBr stock concentration;
- mixing order;
- agitation;
- rinse/quench.

**Use:** high-priority future source-recovery target.

**Negative-evidence rule:** current non-recovery does not mean the thesis lacks these details.

---

# Round-21 central provenance conclusion

The concentration problem cannot be resolved by “standard HgCdTe convention.” Primary HgCdTe sources demonstrably use different explicit bases:

- `w/w` in a Br:HBr paper;
- `v/v` in bromine/methanol and a volume-ratio Br2:HBr patent.

Therefore the exact Srivastav `2% Br2` and `3:1 EG:HBr` preparation remain open until directly sourced.

The correct practical response is not to stop development. It is to:

1. create an explicitly defined **local** formulation branch;
2. preserve the published source notation separately;
3. calibrate actual vertical/lateral rate, bath-age drift, roughness, isolation and surface/passivation response;
4. never call the local branch the exact published formulation without direct basis closure.

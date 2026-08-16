# 2026-08-15 — Hall metrology and RP-01 electrical-specification audit

## Objective

Close enough of the Hall/van-der-Pauw measurement chain to use electrical state as a quantitative release gate for P03 LPE and P04 Hg-overpressure annealing.

A secondary objective was to determine whether the RP-01 starting-material values

- n = 9.8×10^14 cm^-3
- µe = 4.0×10^4 cm²/V·s

were explicitly measured at 77/80 K.

---

## 1. RP-01 source audit: starting-material measurement temperature remains unknown

The primary Smith et al. 2001 paper states that the experimental material was purchased from Fermionics Corporation and was **specified** as approximately x=0.3 n-type HgCdTe with:

- doping density 9.8×10^14 cm^-3;
- electron mobility 4.0×10^4 cm²/V·s.

The accessible primary-paper text does **not** attach a measurement temperature to those supplier-specified values.

Therefore:

- do not label the numbers “77 K”;
- do not label the numbers “80 K”;
- retain them as RP-01 supplier specifications with temperature `OPEN` unless Fermionics documentation or another direct source closes it.

This matters because HgCdTe carrier density and mobility are strongly temperature dependent.

---

## 2. RP-01 does explicitly disclose the RIE-converted Hall test conditions

For the RIE-converted material, Smith et al. state that measurements were performed:

- at both 80 K and 300 K;
- using a van der Pauw structure;
- with variable magnetic field up to 2 T.

The converted material was reported as:

- n-type density 2.0×10^15 cm^-3 averaged over the RIE-converted thickness;
- carrier mobility 3.3×10^4 cm²/V·s.

The text available in the current audit does not unambiguously assign these two summary values to one of the two measurement temperatures, so the numerical pair should not be relabeled without examining the corresponding plotted/data section.

The important methodological finding is that the UWA group already used **variable-field Hall**, not a single fixed field, in the same RP-01 process paper.

---

## 3. Same-lineage multicarrier warning

Tsen, Musca, Dell, Antoszewski, and Faraone, JEM 36, 826–831 (2007), DOI `10.1007/s11664-007-0103-y`, directly address magnetotransport characterization of LPE p-type HgCdTe.

Key conclusions relevant to the manual:

- a conventional single-field Hall result in mixed-conduction HgCdTe can represent an average of multiple carrier populations;
- variable magnetic field and temperature were used;
- iQMSA was used to separate carrier concentrations/mobilities;
- a discrepancy between van-der-Pauw Greek-cross and Hall-bar structures was attributed to formation of an n-type skin inversion layer within about a week after processing.

Process implication:

**surface age and processing history are metrology variables.** Record elapsed time between surface/contact processing and Hall measurement.

---

## 4. 77-K defect-state caveat for x≈0.30

Chandra, Schaake, and Kinch, JEM 32, 810–815 (2003), DOI `10.1007/s11664-003-0075-5`, note that electrical determination of the annealing interface is complicated by incomplete ionization of metal vacancies at 77 K when x exceeds approximately 0.26.

RP-01 nominal x≈0.30 lies in that regime.

Therefore:

- 77/80-K Hall is directly relevant to detector operation;
- 77/80-K Hall alone is not sufficient evidence for a unique native-defect concentration;
- P04 anneal development should include higher-temperature Hall/resistivity behavior or independent defect/composition evidence when defect chemistry is being inferred.

---

## 5. General van der Pauw control limits adopted from NIST guidance

NIST Hall-effect metrology guidance provides a strong general measurement-control framework.

Adopted numerical controls for P05:

- current-reversal / reciprocity agreement: investigate above 5%, with ≤3% preferred;
- P05 routine qualification gate: ≤3% PASS, 3–5% CONDITIONAL, >5% FAIL;
- magnetic field uniformity: approximately within 3%;
- perform both magnetic-field reversal and current reversal;
- sample in dark environment;
- sample temperature uniform and explicitly measured;
- verify ohmic contacts and inspect for contact damage;
- general electrical-power guidance: below 5 mW, preferably ~1 mW or lower, with HgCdTe-specific current-linearity/self-heating verification added by P05.

The NIST pages are archival guidance; the method foundation remains van der Pauw's original work and the associated semiconductor measurement standards.

---

## 6. Derived RP-01 electrical benchmark

Under a one-carrier, Hall-factor-one screening model:

Given:

- n = 9.8×10^14 cm^-3;
- µ = 4.0×10^4 cm²/V·s;
- t = 9.5 µm;

Derived:

- ρ = 0.15922 Ω·cm;
- R_s = 167.60 Ω/square;
- |R_H| = 6.3689×10^3 cm³/C.

Ideal Hall-voltage examples at B=0.10 T:

- I=10 µA → |V_H|≈0.670 mV;
- I=100 µA → |V_H|≈6.70 mV.

Thus the low-density RP-01 material gives a relatively large Hall signal; large drive currents are not required merely to obtain measurable voltage.

---

## 7. HgCdTe-specific P05 decisions

The new controlled metrology file `procedures/P05_HALL_VDP_MATERIAL_METROLOGY.md` adopts the following principles:

1. report Hall density `n_H/p_H` and Hall mobility `µ_H` unless a Hall-factor correction is explicitly justified;
2. retain raw current, voltage, field, temperature and timestamps;
3. use van der Pauw reciprocal/current-reversal redundancy;
4. use a symmetric variable-field sweep during process qualification;
5. antisymmetrize Hall voltage in B;
6. test current dependence/self-heating before selecting measurement current;
7. require linear Hall-vs-B behavior before claiming a simple one-carrier result;
8. escalate to multicarrier/mobility-spectrum analysis if Hall curvature, sign changes or unexplained magnetoresistance appear;
9. record contact/surface age;
10. do not infer native-defect concentration solely from an 80-K Hall number at x≈0.30.

---

## 8. Initial P05 field grid

For RP-01-like material, P05 proposes the qualification field grid:

`B = 0, ±0.01, ±0.025, ±0.05, ±0.10, ±0.20, ±0.50 T`.

This is a local qualification design, not a published RP-01 sequence.

The purpose is to resolve:

- low-field Hall slope;
- curvature;
- sign stability;
- magnetoresistance;
- repeatability.

For anomalous material, expand to higher field. RP-01 itself used variable field up to 2 T for RIE-converted material, while later HgCdTe multicarrier studies use still larger sweeps where necessary.

---

## 9. New unresolved questions

1. Can Fermionics data sheets or an earlier paper establish the temperature for the RP-01 supplier-specified n and µ?
2. What exact Hall-contact material/process did UWA use on the RP-01 van-der-Pauw structures?
3. Can the RIE-converted 80-K and 300-K numerical values be separately extracted from the plotted data?
4. What Hall factor should be expected for n-type x≈0.30 HgCdTe near 80 K at n≈10^15 cm^-3 under the dominant scattering regime?
5. What field-linearity threshold is experimentally achievable with the planned instrumentation?
6. What contact-size correction is needed for the chosen coupon geometry?

---

## 10. Sources

1. E. P. G. Smith et al., “A simplified fabrication process for HgCdTe photoconductive detectors using CH4/H2 reactive-ion-etching-induced blocking contacts,” *Semiconductor Science and Technology* 16, 455–462 (2001), DOI `10.1088/0268-1242/16/6/306`.
2. G. K. O. Tsen, C. A. Musca, J. M. Dell, J. Antoszewski, L. Faraone, “Magneto-Transport Characterization of p-Type HgCdTe,” *Journal of Electronic Materials* 36, 826–831 (2007), DOI `10.1007/s11664-007-0103-y`.
3. D. Satish Chandra, H. F. Schaake, M. A. Kinch, “Low-temperature annealing of (Hg,Cd)Te,” *Journal of Electronic Materials* 32, 810–815 (2003), DOI `10.1007/s11664-003-0075-5`.
4. NIST Physical Measurement Laboratory, Hall-effect/van-der-Pauw measurement guidance and references to van der Pauw and ASTM F76.

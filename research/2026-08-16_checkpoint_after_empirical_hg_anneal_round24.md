# Checkpoint — after empirical Hg-overpressure anneal Round 24

**Date:** 2026-08-16

## What changed

Round 24 added the empirical apparatus/control layer missing from P04/P23:

- `procedures/P31_HG_ANNEAL_APPARATUS_RESERVOIR_TRAJECTORY_EMPIRICAL_PROCESS_WINDOW.md`
- `travelers/P31_HG_ANNEAL_EMPIRICAL_QUALIFICATION_REGISTER.md`
- `docs/SOURCE_LEDGER_ADDENDUM_ROUND24.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND24.md`

P31 does not replace P04/P23. It makes their anneal state variables physically executable and traceable.

---

## Strongest empirical conclusions

### 1. `T_s` and `T_Hg` are independent process coordinates

Jones et al. directly distinguish:

- isothermal Hg anneal: reservoir temperature approximately equals sample temperature;
- two-temperature anneal: reservoir temperature lower than sample temperature.

The two branches can produce different carrier states. Therefore “anneal in Hg” is not an adequate recipe descriptor.

### 2. First RP-01 transfer branch remains low temperature

Strongest primary anchors:

- Harman: approximately 250 °C / 1 h / pseudo-isothermal Hg-saturated process-family example;
- Nagahama x≈0.17–0.30 LPE: 250–300 °C gave well-behaved n-type material without apparent composition change, while 400 °C produced composition change near the interface.

Thus the first x≈0.30 local transfer screen should stay below 300 °C unless a separate defect-control goal justifies higher temperature.

### 3. High-temperature defect-control anneals are separate process architectures

TI/Schaake/Tregilgas primary patents describe 350–650 °C Hg-controlled branches intended to reduce Te precipitates, dislocations or vacancy supersaturation before subsequent low-temperature stoichiometry control.

Do not silently prepend these to RP-01 P04.

### 4. Two-zone sealed ampoule is a real executable architecture

US5079192 provides a direct hardware model:

- long sealed ampoule;
- sample at one end;
- elemental Hg reservoir remote at the other;
- independent furnace zones;
- separate source/sample temperature histories.

Preferred example:

- sample ~400 °C;
- reservoir initially <200 °C;
- ~1 h;
- reservoir then ~390 °C while sample remains ~400 °C;
- ~1 h;
- then stoichiometric anneal below 325 °C for several hours to several days;
- cool to room temperature.

This is retained as high-T/dislocation-control transfer evidence only.

### 5. Hg condensation/dissolution is an apparatus risk

TI explicitly keeps the Hg reservoir cooler than the sample in part of the trajectory to prevent elemental Hg from depositing on and dissolving the HgCdTe.

P31 therefore requires the full source/sample cooldown relation, not just sample temperature.

### 6. Hg source mass remains OPEN

Primary literature often says “sufficient Hg to provide a saturated atmosphere” but does not provide an RP-01-independent mass.

Reservoir requirement depends on:

- free volume;
- T_Hg;
- source surface area;
- cold-wall condensation;
- leakage;
- duration;
- geometry.

No gram value is released.

### 7. Thin LPE time cannot be inferred from bulk times

Bulk TI examples at ~270 °C require days for deep conversion; Harman reports 1 h in an in-situ epitaxial branch. Chandra/Schaake/Kinch show anneal rate depends strongly on x, T and starting vacancy state.

P31 therefore requires a local time map on actual x≈0.30 ~9.5-µm material.

### 8. Final Hall sign alone is insufficient

Near the p/n transition, apparent one-carrier Hall density is singular. P31 inherits P23:

- use signed Hall/tensor information for carrier-state boundary;
- calculate n_H/mu_H only inside a validated stable one-carrier region.

### 9. Optical and defect preservation remain hard gates

A run reaching n≈10^15 cm^-3 fails if it causes:

- spectral/composition shift;
- surface deposits/attack;
- unacceptable Te-precipitate/dislocation response;
- invalid multicarrier transport;
- nonrepeatable cooldown sensitivity.

---

## Current strongest first-transfer P31 branch

`matched x≈0.30 P30 coupons`

`-> quantitatively Hg-controlled sealed/in-situ enclosure`

`-> independently calibrated T_s and Hg boundary`

`-> T_s near 250 °C`

`-> isothermal/Hg-saturated-like branch`

`-> first literature time point ~1 h`

`-> controlled cooldown retaining Hg boundary`

`-> P05 signed Hall/tensor + P06 same-site optical/thickness`

`-> P13/device proxy for selected conditions`.

This is a screening/qualification center only.

---

## What remains OPEN

### Historical RP-01

- whether the Fermionics material arrived already in the quoted annealed n/µ state;
- exact anneal architecture;
- Hg source identity/mass;
- sample/source geometry;
- sample temperature;
- reservoir temperature;
- dwell;
- cooldown;
- surface condition during anneal.

### Local qualification

- selected ampoule ID/length/free volume;
- reservoir vessel geometry;
- source/sample spacing;
- elemental-Hg saturation/reconstruction relation;
- thermometry uncertainty;
- exact x≈0.30 state boundary;
- time dependence on ~9.5-µm layers;
- cooldown sensitivity;
- defect/precipitate response;
- repeatability across P30 runs;
- detector-level optimum.

---

## Negative / rejected inferences retained

1. Do not infer RP-01 used 250 °C/1 h because Harman did.
2. Do not infer RP-01 used 270 °C for days because TI bulk slices did.
3. Do not infer elemental-Hg mass from a foreign ampoule.
4. Do not treat saturated Hg pressure as zero/ambient pressure.
5. Do not merge high-temperature dislocation reduction with low-temperature vacancy control.
6. Do not call a controller setpoint the sample temperature without calibration.
7. Do not treat cooldown as inactive.
8. Do not regress reciprocal Hall density through the conversion boundary.

---

## Next logical empirical target

After Round 24, the largest remaining practical fabrication gap is likely the **Mask-1 / mesa lithography and wet-etch mask-stack interface**, because P28 now has a strong chemistry/process-control layer but the actual RP-01 Mask-1 resist identity, thickness, bake, exposure, developer, selectivity, and strip sequence remain weak.

A strong Round 25 target is therefore:

- recover primary HgCdTe wet-etch photoresist-mask processes near 9.5-µm through-mesa depth;
- quantify resist/etch selectivity and undercut/profile interaction;
- recover Mask-1 thickness/bake/exposure/developer/strip from UWA or close process families;
- create P32 empirical Mask-1/wet-mesa lithography window and traveler if supported.

Alternative if Mask-1 source recovery is poor: pursue exact RP-01 noise/readout geometry or package/thermal interface, but do not invent lithography values.

# P08E — RIE multicarrier transport qualification

**Status:** CONTROLLED TRANSPORT ADDENDUM. Supplements P05 and P08/P08B/P08D.

## 1. Purpose

Prevent post-RIE HgCdTe transport from being reduced automatically to one uniform n+ slab when magnetic-field-dependent measurements indicate multiple carrier populations.

Same-UWA primary work shows that CH4/H2 RIE conversion can produce at least:

1. a thin damaged surface electron layer with moderate mobility;
2. a deeper, higher-mobility n-type converted region;
3. where conversion is incomplete, residual p-type bulk conduction.

Accordingly, a single low-field Hall coefficient can be an average of physically distinct channels.

## 2. Primary same-UWA transport source

T. Nguyen, J. Antoszewski, C. A. Musca, D. A. Redfern, J. M. Dell, L. Faraone, “Transport Properties of Reactive-Ion-Etching-Induced p-to-n Type Converted Layers in HgCdTe,” *Journal of Electronic Materials* 31(7), 652–659 (2002), DOI `10.1007/s11664-002-0214-4`.

The UWA institutional record directly states:

- LPE Hg1−xCdxTe with `x=0.23` and `x=0.31`;
- vacancy-doped and gold-doped p-type epilayers on lattice-matched CdZnTe;
- partial RIE conversion to n-type;
- magnetic-field-dependent differential Hall and resistivity measurements;
- quantitative mobility spectrum analysis (QMSA);
- a damaged surface layer with moderate-mobility electrons;
- a deeper bulk n-type region with higher electron mobility;
- surface-electron concentration/mobility comparatively insensitive to temperature over the measured range;
- deeper bulk electrons showing high-quality HgCdTe-like temperature dependence;
- differential Hall evidence consistent with a diffusion-distributed n-type dopant profile.

The proposed mechanism involves both neutralization of p-type dopants and diffusion of extrinsic n-type dopants from the surface.

## 3. Composition-matched companion result

J. Antoszewski, C. A. Musca, J. M. Dell, L. Faraone, “Characterization of Hg0.7Cd0.3Te n-on-p-type structures obtained by reactive ion etching induced p-to-n conversion,” *Journal of Electronic Materials* 29(6), 837–840 (2000), DOI `10.1007/s11664-000-0234-x`.

For 77-K x=0.30 samples in that different p-type conversion branch, reported carrier populations include approximately:

### Vacancy-doped sample

- residual holes: `p≈2×10^16 cm^-3`, `mu≈350 cm²/Vs`;
- deeper converted electrons: `n≈3×10^15 cm^-3`, `mu≈4×10^4 cm²/Vs`;
- surface electrons: `Ns≈9×10^12 cm^-2`, mobility within roughly `1.5×10^3–1.5×10^4 cm²/Vs`.

### Au-doped sample

- residual holes: `p≈6×10^15 cm^-3`, `mu≈400 cm²/Vs`;
- deeper converted electrons: `n≈1.5×10^15 cm^-3`, `mu≈6×10^4 cm²/Vs`;
- surface electrons: `Ns≈1×10^13 cm^-2`, again moderate mobility.

The converted layer in this study was described as about `2 µm` thick.

These values are **not RP-01 targets**. They are direct evidence that an x≈0.30 RIE-converted HgCdTe structure can contain a damaged 2-D surface channel plus a high-mobility deeper n region.

## 4. Consequence for RP-01 interpretation

RP-01 reports a converted density of approximately `2.0×10^15 cm^-3` and mobility `3.3×10^4 cm²/Vs`, with the density averaged over the converted thickness.

Because same-lab work demonstrates multichannel conduction, RP-01 transfer qualification shall not assume that those two scalar values uniquely describe a uniform layer.

The local data-analysis hierarchy is:

1. inspect `Rxx(B)` and `Rxy(B)` over a symmetric field sweep;
2. test whether one-carrier Hall behavior is statistically adequate;
3. if curvature/magnetoresistance/sign competition is present, apply a validated multicarrier model or mobility-spectrum analysis;
4. report sheet carrier populations directly where appropriate;
5. combine a deeper-layer volumetric density with `d_conv` only when the depth model is independently supported.

## 5. Required RIE transport dataset

For each P08D qualification condition acquire, preferably at multiple temperatures including the detector operating region:

- longitudinal resistivity/resistance versus B;
- Hall voltage/resistance versus B;
- current-reversal data;
- field-reversal data;
- zero-field VdP consistency;
- sample thickness and geometry;
- pre-RIE transport baseline;
- post-RIE transport;
- LBIC `d_conv`/`L_conv` from the matched condition;
- physical recession `d_etch`.

Where practical, extend B far enough that carrier populations with substantially different mobility are separable. The exact required field range depends on the local mobility spectrum and instrument capability.

## 6. Model-selection gate

A one-carrier reduction may be used only if:

- Hall response is sufficiently linear over the qualified B range;
- magnetoresistance is consistent with the model;
- fitted parameters are stable to fit-range changes;
- residuals do not indicate a second mobility population;
- the derived sheet/volume state is consistent with independent depth information.

Otherwise report a multicarrier state.

## 7. Preferred outputs

When resolvable, report separately:

- surface-sheet electron density `Ns,surf`;
- surface mobility `mu_surf`;
- deeper converted electron density/profile `n_bulk(z)` or effective `n_bulk`;
- deeper mobility `mu_bulk`;
- residual hole population if present;
- conversion depth `d_conv`;
- physical etch depth `d_etch`.

Do not merge a 2-D sheet density into a 3-D volume density by assigning an arbitrary thickness.

## 8. Relationship to P08B conditional sheet scale

P08B derives a conditional RP-01 sheet-density scale of approximately `1.6×10^12 cm^-2` if `2.0×10^15 cm^-3` is averaged over `8 µm`.

The same-UWA p-type studies report damaged surface sheet densities around `10^13 cm^-2`, an order of magnitude larger than that conditional RP-01 bulk-converted sheet scale.

This does **not** mean RP-01 necessarily contains the same ~10^13 cm^-2 surface sheet, because material type, pressure, exposure and process are different. It does show that a surface channel could substantially distort a simple Hall reduction and therefore must be tested rather than ignored.

## 9. Contact-process acceptance rule

The purpose of RP-01 RIE is a functional blocking/contact region, not merely a desired Hall number.

Final acceptance therefore remains multivariate:

`{transport decomposition, d_conv, L_conv, d_etch, TLM rho_c, detector I-V, responsivity, noise}`.

A process that produces a strong damaged surface channel but poor cryogenic TLM/noise performance fails even if an averaged Hall density resembles the historical scalar value.

## 10. Provenance restriction

The Nguyen/Antoszewski results are from p-to-n converted p-type material and are used here for transport physics and metrology design.

They must not be presented as direct RP-01 n-type blocking-contact setpoints.
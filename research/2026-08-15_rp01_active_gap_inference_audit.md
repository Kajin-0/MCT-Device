# RP-01 active-gap / active-area inference audit

**Date:** 2026-08-15 America/New_York  
**Status:** historical device gap remains `OPEN`; reverse inference from published scalar performance is underdetermined.

## 1. What is directly known

Smith et al. 2001 state that the experimental structure:

- is `9.5 µm` thick;
- contains a string of nine metal contacts;
- each contact is `300 µm × 300 µm`;
- first adjacent separation is `50 µm`;
- successive separations increase by `50 µm`, giving candidate adjacent gaps `50, 100, ..., 400 µm`;
- the structure allows both TLM/contact and photoconductor-performance measurements.

The paper further states that Figures 6 and 7 use the **same device** as Figures 3 and 5.

Thus the published field-dependent responsivity, noise spectrum, spectral responsivity and spectral D* all refer to one common detector/contact-pair selection.

What the paper does **not** state is which adjacent contact pair/gap was selected for that device.

## 2. Candidate active-area bounds if contact width defines optical width

If the active optical region is taken as the rectangular region between two full-width 300-µm contacts, candidate geometrical areas are:

| gap L (µm) | width w (µm) | A = wL (mm²) | A (cm²) |
|---:|---:|---:|---:|
| 50 | 300 | 0.015 | 1.5e-4 |
| 100 | 300 | 0.030 | 3.0e-4 |
| 150 | 300 | 0.045 | 4.5e-4 |
| 200 | 300 | 0.060 | 6.0e-4 |
| 250 | 300 | 0.075 | 7.5e-4 |
| 300 | 300 | 0.090 | 9.0e-4 |
| 350 | 300 | 0.105 | 1.05e-3 |
| 400 | 300 | 0.120 | 1.2e-3 |

This table is `[D]` from published contact dimensions/spacings. Actual illuminated/electrically active area may differ because of metal overlap, mesa geometry, RIE lateral conversion and optical aperture.

## 3. Why D* cannot uniquely select the gap

The paper defines

`D* = R_lambda sqrt(A) / e_n`

when noise is expressed as detector voltage ASD.

At 4 µm the paper reports approximately:

- `D* = 2.0×10^11 cm Hz^1/2 W^-1`;
- high-frequency generation–recombination noise level `e_gr≈24.5 nV/√Hz`;
- 1/f knee `~3 kHz`;
- spectral responsivity measurement at `1 kHz`.

The crucial problem is that `24.5 nV/√Hz` is the g-r plateau/high-frequency level, while `1 kHz` lies below the reported 3-kHz 1/f knee.

Therefore the paper does not close `e_n(1 kHz)` used in the spectral D* reduction.

Assuming the 24.5-nV/√Hz plateau was the D* noise would be an unsupported convention choice.

## 4. Conditional responsivity values under the g-r-only assumption

For diagnostic purposes only, if one assumes:

- `D*=2.0e11`;
- `e_n=24.5 nV/√Hz`;
- rectangular active area `A=(300 µm)L`;

then the responsivity required by the D* equation would be:

| gap (µm) | required R_4um (V/W) |
|---:|---:|
| 50 | 4.00e5 |
| 100 | 2.83e5 |
| 150 | 2.31e5 |
| 200 | 2.00e5 |
| 250 | 1.79e5 |
| 300 | 1.63e5 |
| 350 | 1.51e5 |
| 400 | 1.41e5 |

These values are `[D / CONDITIONAL]` and are **not** evidence selecting one gap.

If the true 1-kHz noise exceeds the 24.5-nV/√Hz g-r floor because of 1/f noise, every implied responsivity scales upward in direct proportion.

## 5. Why Figure 3 does not solve it analytically

The photoconductor responsivity expression used by Smith et al. contains detector length and effective lifetime:

`R_lambda ∝ (r_d µ_e E_b / l) tau_eff`.

Although geometry changes `l`, detector resistance and sweepout/effective lifetime also depend on geometry/contact effects. Therefore a single plotted responsivity point cannot be inverted for `l` without independent knowledge of:

- actual device resistance;
- effective lifetime at the operating field;
- contact resistance/loading;
- active illumination geometry.

The paper does not provide all of these for the Figure-3 device.

## 6. Historical conclusion

The exact contact pair used for Figures 3/5/6/7 remains `OPEN`.

The evidence narrows the active-gap possibilities to the published structure but does not select one uniquely.

Do not record `L=50 µm`, `L=100 µm`, or another value as RP-01 fact merely because it is plausible.

## 7. Correct recovery paths

The gap can be closed only by one of the following:

1. recover original mask/layout/device log or fuller UWA source that identifies the selected contact pair;
2. obtain a high-resolution original figure/image containing an explicit geometry label not preserved in OCR;
3. recover raw resistance/responsivity/noise data plus an independently closed noise convention and active-area definition sufficient to overdetermine the geometry;
4. for local reproduction, simply **measure the fabricated gap and area** and report performance for that explicit geometry rather than trying to emulate an unidentified historical contact pair.

## 8. Release implication

P10/P11/P12 must use measured local dimensions. Historical D* is a performance benchmark, not justification for assigning a historical active area that the paper did not state.

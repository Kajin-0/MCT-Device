# Controlled calculation — Hansen HgCdTe band-gap model

## Source

G. L. Hansen, J. L. Schmit, and T. N. Casselman, “Energy gap versus alloy composition and temperature in Hg1−xCdxTe,” *Journal of Applied Physics* 53, 7099–7101 (1982). DOI: `10.1063/1.330018`.

## Equation

For alloy fraction `x` and temperature `T` in kelvin,

`Eg(x,T) = -0.302 + 1.93x - 0.810x^2 + 0.832x^3 + 5.35e-4*T*(1 - 2x)` eV.

The source reports applicability over the full alloy composition range and temperatures from 4.2 K to 300 K, with a standard error of estimate of approximately 0.013 eV.

## Derived photon-equivalent wavelength

A photon wavelength corresponding to the band-gap energy can be calculated as

`lambda_Eg [µm] = 1.239841984 / Eg [eV]`.

This value is a **band-gap-equivalent wavelength**, not automatically the detector's experimental spectral cutoff.

## RP-01 consistency example

For the approximate nominal composition `x = 0.30` at `T = 80 K`:

- `Eg ≈ 0.243684 eV` `[D]`;
- `lambda_Eg ≈ 5.088 µm` `[D]`.

Smith et al. report an experimental detector cutoff of **4.4 µm at 80 K** for RP-01. This discrepancy is not to be “corrected” by forcing one quantity to equal the other because:

1. the starting composition is reported only as approximately x=0.30;
2. the Hansen fit itself has finite empirical uncertainty;
3. detector cutoff is defined from measured spectral response rather than directly from a single ideal Eg value;
4. doping and edge-response physics can affect the practical response edge.

The correct use is therefore:

- measured spectral cutoff = device acceptance/performance observable;
- Hansen Eg(x,T) = independent material-property consistency check.

## Inverse calculation rule

If a measured band-gap-equivalent energy is used to infer x, solve the full cubic temperature-dependent equation numerically rather than applying a linear approximation. Record:

- measured quantity used to infer Eg;
- cutoff/edge convention;
- temperature and uncertainty;
- numerical root selected;
- propagated uncertainty in x;
- whether the result is being treated as a true composition measurement or only an optical proxy.

## Controlled-use warning

Do not use this equation outside its cited validity range without a separate source. Do not silently mix it with a different empirical HgCdTe Eg relation within the same calculation chain.

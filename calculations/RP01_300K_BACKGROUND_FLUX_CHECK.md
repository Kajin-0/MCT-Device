# RP-01 300 K background-photon-flux consistency check

## Purpose

Test whether the RP-01 statement

- `300 K` background;
- `60°` field of view;
- background photon flux approximately `1.0×10^15 cm^-2 s^-1`;
- detector spectral cutoff approximately `4.4 µm` at 80 K

is internally consistent with a standard Planck blackbody calculation and, in particular, whether “60° FOV” is more likely to denote a **full cone angle** or a **half angle**.

This is a derived consistency calculation, not a replacement for the historical optical-layout documentation.

---

## 1. Photon spectral radiance

For an ideal blackbody at temperature `T`, the spectral photon radiance per unit wavelength is

`N_lambda(T) = [2c / lambda^4] / [exp(hc/(lambda k_B T)) - 1]`

with units

`photons s^-1 m^-2 sr^-1 m^-1`.

This follows by dividing Planck spectral radiance in power units by the photon energy `hc/lambda`.

Constants used:

- `h = 6.62607015×10^-34 J s`
- `c = 299792458 m/s`
- `k_B = 1.380649×10^-23 J/K`

---

## 2. Irradiance from a filled circular cone

For a Lambertian source that completely fills a circular cone of half-angle `theta`, the photon irradiance is

`Phi = integral[N_lambda d(lambda)] * integral[cos(theta') dOmega]`

and

`integral_cone cos(theta') dOmega = pi sin^2(theta)`.

Therefore

`Phi(lambda_1,lambda_2,T,theta) = pi sin^2(theta) * integral_(lambda_1)^(lambda_2) N_lambda(T) d(lambda)`.

For a **60° full field of view**, the half-angle is `theta=30°`, hence

`pi sin^2(30°) = pi/4`.

For a **60° half-angle**, the corresponding angular factor is

`pi sin^2(60°) = 3pi/4`,

which is exactly three times larger.

---

## 3. Numerical integration to the reported 4.4-µm detector cutoff

Using:

- `T = 300 K`;
- upper wavelength `lambda_c = 4.4 µm`;
- lower integration limit sufficiently short that omitted 300-K photon flux is negligible;

results are:

### Interpretation A — 60° is the full cone angle

`theta = 30°`

`Phi ≈ 1.1239×10^15 photons cm^-2 s^-1`.

### Interpretation B — 60° is the half angle

`theta = 60°`

`Phi ≈ 3.3717×10^15 photons cm^-2 s^-1`.

### Full hemisphere

`theta = 90°`

`Phi ≈ 4.4956×10^15 photons cm^-2 s^-1`.

---

## 4. Comparison with RP-01

RP-01 reports approximately

`Phi_RP01 = 1.0×10^15 cm^-2 s^-1`.

The ideal-blackbody result for a **60° full cone / 30° half-angle** is only about 12.4% higher:

`1.1239×10^15 / 1.0×10^15 = 1.124`.

The result for a 60° half-angle is about 3.37 times the reported flux.

This strongly suggests that the RP-01 “60° FOV” is most naturally interpreted as approximately a **60° full-angle cone**, i.e. approximately ±30° about the optical axis.

This is an inference, not direct documentary proof.

---

## 5. Sensitivity to the effective long-wavelength boundary

For a 60° full cone / 30° half-angle at 300 K:

| Upper integration wavelength | Photon flux |
|---:|---:|
| 4.30 µm | `9.095×10^14 cm^-2 s^-1` |
| 4.35 µm | `1.012×10^15 cm^-2 s^-1` |
| 4.40 µm | `1.124×10^15 cm^-2 s^-1` |
| 4.45 µm | `1.245×10^15 cm^-2 s^-1` |

Thus an effective response cutoff/weighting near `4.35 µm` reproduces the quoted `1.0×10^15 cm^-2 s^-1` almost exactly under the 60°-full-cone interpretation.

The difference between 4.35 and 4.4 µm is entirely plausible given that:

- RP-01 quotes spectral cutoff approximately;
- detector response falls continuously rather than as an ideal step function;
- window/optical transmission can weight the spectrum;
- blackbody emissivity and aperture geometry may differ from the ideal assumptions;
- the published background flux is itself given with limited significant figures.

Therefore no ad-hoc correction is needed to explain the RP-01 number.

---

## 6. Important limitation: step-function response approximation

The above calculation integrates all incident photons from short wavelength to `lambda_c` with unit spectral weighting.

A real detector background-generation rate should use

`G_bg/A = integral eta(lambda) tau_opt(lambda) N_lambda(T) d(lambda) dOmega_projection`

where:

- `eta(lambda)` is quantum efficiency;
- `tau_opt(lambda)` is window/filter/optical transmission;
- the detector spectral response is not an ideal rectangular band;
- the actual field stop may not generate a perfect filled circular cone.

Consequently, the calculation is best viewed as a **geometry/convention consistency test**, not the final background-generation calculation.

---

## 7. Consequence for P11 radiometry

Until historical optical drawings are recovered, P11 should adopt:

- `60° FOV` as **provisionally a full-angle value**;
- half-angle `theta≈30°` for consistency calculations;
- explicit tag `INFERRED-FROM-FLUX-CONSISTENCY`;
- actual solid angle/view factor measured from the released optical geometry rather than relying on the nominal 60° label.

The final radiometry traveler must report the physical aperture geometry and calculate the view factor/solid angle independently.

---

## 8. Reproducibility calculation pseudocode

```text
T = 300 K
lambda_c = 4.4e-6 m
theta = 30 deg

N_lambda(lambda) = 2*c/lambda^4 / (exp(h*c/(lambda*k*T)) - 1)

Phi_sr = numerical_integral(N_lambda, lambda=short_limit...lambda_c)
Phi_m2 = pi*sin(theta)^2 * Phi_sr
Phi_cm2 = Phi_m2 / 1e4
```

Numerical integration should be performed with sufficient precision that quadrature error is negligible compared with the experimental/radiometric uncertainty.

---

## 9. Provenance

Historical values are from:

E. P. G. Smith et al., “A simplified fabrication process for HgCdTe photoconductive detectors using CH4/H2 reactive-ion-etching-induced blocking contacts,” *Semiconductor Science and Technology* 16, 455–462 (2001), DOI `10.1088/0268-1242/16/6/306`.

The blackbody equations use standard Planck radiometry. Geometry treatment is consistent with the radiometric aperture/view-factor methods used by NIST's Low Background Infrared calibration program.

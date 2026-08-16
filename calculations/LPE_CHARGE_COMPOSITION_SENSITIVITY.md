# LPE charge-composition sensitivity for the x≈0.30 candidate tie line

## Purpose

Quantify how elemental weighing error propagates into the liquid-composition coordinates `(xL,yL)` for the current RP-01 Te-rich LPE candidate.

This module is intended to determine:

- required balance resolution/repeatability;
- minimum practical growth-charge mass;
- charge acceptance calculations;
- which elemental mass dominates composition uncertainty.

It does **not** yet assign a production balance tolerance because the allowed final solid-composition error `ΔxS` has not been released and the liquid-to-solid mapping is temperature/process dependent.

---

## 1. Published tie-line anchor

Bowers–Schmit U.S. Patent 4,317,689 tabulates the composition nearest RP-01:

- `xL = 0.082`
- `yL = 0.810`
- `TL = 507 °C`
- `xS = 0.29`
- tabulated ratio `k = xS/xL = 3.54`

The liquid notation is

`(Hg_(1−xL) Cd_xL)_(1−yL) Te_yL`.

Therefore the elemental atomic/molar fractions are

- `X_Hg = (1−xL)(1−yL) = 0.17442`
- `X_Cd = xL(1−yL) = 0.01558`
- `X_Te = yL = 0.81000`.

---

## 2. Atomic weights used

For the engineering mass conversion in this repository:

- Hg: 200.59 g/mol
- Cd: 112.414 g/mol
- Te: 127.60 g/mol

These constants must be frozen in the calculation implementation so a future update does not silently change charge masses.

---

## 3. Derived mass fractions

The mean mass per mole of elemental atoms in the normalized liquid composition is

`Mbar = X_Hg A_Hg + X_Cd A_Cd + X_Te A_Te`

which gives

`Mbar = 140.09431792 g per normalized mole of atoms`.

Thus the mass fractions are

- `w_Hg = 0.2497382358`
- `w_Cd = 0.01250164993`
- `w_Te = 0.7377601143`.

They sum to 1.0000000000 within rounding.

For an arbitrarily selected total charge mass `M_charge`:

`m_Hg = 0.2497382358 M_charge`

`m_Cd = 0.01250164993 M_charge`

`m_Te = 0.7377601143 M_charge`.

**Important:** `M_charge` is an apparatus variable. This relation does not authorize a particular total charge mass.

---

## 4. Example mass table — calculation examples only

| Total charge | Hg | Cd | Te |
|---:|---:|---:|---:|
| 1.000 g | 249.738 mg | 12.502 mg | 737.760 mg |
| 2.000 g | 499.476 mg | 25.003 mg | 1475.520 mg |
| 5.000 g | 1.248691 g | 62.508 mg | 3.688801 g |
| 10.000 g | 2.497382 g | 125.016 mg | 7.377601 g |

These examples are included only to expose the metrology scaling. They are **not** released LPE charge masses.

---

## 5. Reconstructing liquid composition from actual weighed masses

The manual must never assume the nominal liquid composition after weighing. Recalculate it from the recorded actual masses.

Let

`N_Hg = m_Hg/A_Hg`

`N_Cd = m_Cd/A_Cd`

`N_Te = m_Te/A_Te`.

Then

`xL_actual = N_Cd/(N_Hg+N_Cd)`

and

`yL_actual = N_Te/(N_Hg+N_Cd+N_Te)`.

These equations are the required charge-release calculation.

The recorded batch traveler should include both nominal and actual:

- masses;
- `xL`;
- `yL`;
- deviations `δxL`, `δyL`.

---

## 6. Local differential sensitivity

For small independent mass errors around the target composition, the composition sensitivity can be obtained from the partial derivatives of the equations above.

### 6.1 At a 5.000 g illustrative total charge

Nominal elemental masses are:

- `m_Hg = 1.24869118 g`
- `m_Cd = 0.06250825 g`
- `m_Te = 3.68880057 g`.

The local sensitivities of `xL` are approximately:

- `∂xL/∂m_Hg = −0.060284 g^-1`
- `∂xL/∂m_Cd = +1.204257 g^-1`
- `∂xL/∂m_Te = 0`.

Therefore, at this charge size:

- +0.1 mg Hg → `δxL ≈ −6.03×10^-6`
- +0.1 mg Cd → `δxL ≈ +1.20×10^-4`
- Te mass does not directly change `xL`, although it changes `yL` and thus the liquidus state.

The local sensitivities of `yL` are approximately:

- `∂yL/∂m_Hg = −0.113143 g^-1`
- `∂yL/∂m_Cd = −0.201890 g^-1`
- `∂yL/∂m_Te = +0.041721 g^-1`.

Thus every element matters for `yL`, while Cd strongly dominates the direct uncertainty in `xL`.

---

## 7. Charge-size scaling

For fixed composition, the derivatives with respect to elemental mass scale approximately as `1/M_charge`.

Therefore balance error becomes much more consequential as the charge becomes smaller.

For a +0.1 mg Cd error:

- at 1 g total charge: `|δxL| ≈ 6.02×10^-4`
- at 2 g: `|δxL| ≈ 3.01×10^-4`
- at 5 g: `|δxL| ≈ 1.20×10^-4`
- at 10 g: `|δxL| ≈ 6.02×10^-5`.

This gives a quantitative trade between:

- smaller melt volume / reduced material use;
- balance capability;
- composition reproducibility.

---

## 8. Approximate connection to solid composition

The Bowers–Schmit table gives the ratio

`k = xS/xL = 3.54`

at the selected tie line.

A **crude local screening proxy** is therefore

`δxS_proxy ≈ 3.54 δxL`.

This is not yet a valid production uncertainty transfer function because `k=xS/xL` is a tabulated ratio, not proof that the local differential derivative `dxS/dxL` equals 3.54. The actual solid composition also depends on liquidus temperature, Hg chemical potential, depletion, supercooling, and process history.

Still, as an order-of-magnitude screening metric:

for a 5 g charge and +0.1 mg Cd error,

`δxS_proxy ≈ 4.26×10^-4`.

For a 1 g charge and +0.1 mg Cd error,

`δxS_proxy ≈ 2.13×10^-3`.

This demonstrates why a 0.1 mg balance can be adequate for a several-gram charge yet potentially marginal for a ~1 g charge if the desired solid-composition repeatability is on the order of 10^-3.

---

## 9. RSS uncertainty propagation

If elemental mass errors are independent with standard uncertainties `u_mHg`, `u_mCd`, and `u_mTe`, first-order uncertainty is

`u_xL^2 = (∂xL/∂mHg)^2 u_mHg^2 + (∂xL/∂mCd)^2 u_mCd^2 + (∂xL/∂mTe)^2 u_mTe^2`

and

`u_yL^2 = (∂yL/∂mHg)^2 u_mHg^2 + (∂yL/∂mCd)^2 u_mCd^2 + (∂yL/∂mTe)^2 u_mTe^2`.

For a real process these terms should include more than display resolution:

- calibration uncertainty;
- repeatability;
- eccentricity/loading-position error;
- buoyancy correction if relevant at the required level;
- transfer loss from weighing vessel to charge container;
- oxidation/contamination or adhered residue;
- Hg loss between weighing and sealing/loading.

The process traveler must distinguish **balance indication uncertainty** from **actual delivered-mass uncertainty**.

---

## 10. Balance selection rule

A balance should not be specified only by readability.

Release should require:

1. readability small enough that the Cd contribution does not dominate the allowed liquid-composition uncertainty;
2. repeatability verified at the actual Cd mass range;
3. calibration traceability;
4. minimum sample weight satisfied for the required uncertainty;
5. environmental controls adequate for sub-milligram work;
6. a transfer protocol whose mass loss is characterized.

Because Cd is only ~1.25 wt% of the candidate charge, the balance must be qualified specifically near the **tens-of-milligrams Cd mass range**, not merely with a 100 g calibration weight.

---

## 11. Recommended balance qualification experiment

Before releasing a growth-charge mass:

### Repeatability

At representative masses for Hg, Cd, and Te:

- perform at least 10 repeated weighings;
- remove/reload the artifact between readings;
- compute mean, standard deviation, range, and drift.

### Transfer-loss test

For the intended weighing/transfer container:

- weigh container;
- add representative elemental material or safe surrogate of comparable handling behavior;
- transfer using the intended technique;
- reweigh container;
- determine residual mass and reproducibility.

### Time drift

Repeat representative weighing over the expected charge-preparation interval to quantify zero/drift/environmental contribution.

### Acceptance

The final balance/transfer system should be accepted based on propagated `u_xL` and `u_yL`, not a generic ±0.1 mg specification.

---

## 12. Remaining blocker for numerical tolerance release

To convert this calculation into an explicit balance requirement, the project still needs a released allowed liquid-composition uncertainty.

That requires:

1. define an allowable final solid-composition spread `u_xS` from the spectral/cutoff specification;
2. experimentally establish the local mapping `(xL,yL,T,process) → xS` around the candidate tie line;
3. allocate an uncertainty budget among weighing, temperature, Hg chemical potential, charge depletion, and spatial variation;
4. assign the fraction of that budget allowed to charge weighing.

Until those steps are complete, the calculation supports equipment selection and DOE design but not a final manufacturing tolerance.

---

## 13. Provenance

Published composition anchor:

J. E. Bowers and J. L. Schmit, “Mercury containment for liquid phase growth of mercury cadmium telluride from tellurium-rich solution,” U.S. Patent 4,317,689 (1982).

All mass fractions, differential sensitivities, example charge masses, and uncertainty equations in this file are derived calculations from that published tie line and the stated atomic weights.

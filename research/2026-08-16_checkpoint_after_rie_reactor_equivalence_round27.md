# Research checkpoint — after empirical RIE reactor equivalence Round 27

**Date:** 2026-08-16 America/New_York

## Round objective

Resolve whether the RP-01 blocking-contact RIE step can be made portable from its published controller values alone, or whether a reactor-equivalence layer is required.

## Result

A new empirical module was justified and created:

- `procedures/P34_RIE_REACTOR_EQUIVALENCE_EMPIRICAL_PROCESS_WINDOW.md`
- `travelers/P34_RIE_REACTOR_EQUIVALENCE_EMPIRICAL_QUALIFICATION_REGISTER.md`
- `docs/SOURCE_LEDGER_ADDENDUM_ROUND27.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND27.md`

P34 supplements P08D. It does not replace the direct RP-01 recipe anchors.

---

# Main scientific conclusion

The direct RP-01 condition:

`64 sccm / 100 mTorr / 50 W / 60 s / CH4/5H2`

is a **controller-space coordinate**, not a complete plasma-material state.

Primary HgCdTe evidence now directly demonstrates the need to retain at least:

- dc self-bias / ion-energy proxy;
- sample temperature;
- gas ratio;
- pressure;
- crystallographic face;
- physical semiconductor exposure after oxide clear;
- chamber/loading state;
- physical etch depth;
- electrical conversion depth.

Therefore another reactor may match all four RP-01 numeric controller values and still fail to reproduce the blocking-contact material state.

---

# Strongest new primary evidence

## Semu et al. 1991

Direct CH4/H2 HgCdTe RIE experiment:

- total flow `85 sccm`;
- pressure `20 mTorr`;
- temperature `35 °C`;
- RF `150 W`;
- dc bias about `-360` to `-440 V`.

Explicit example:

`CH4=15 sccm / H2=70 sccm / 20 mTorr / 150 W / -390 V / 35 °C`.

The paper directly associated the rough etched surface/sidewall with high RF-power-induced dc bias and showed gas-ratio dependence of etch rate.

### Consequence

`P_RF` cannot be used as a reactor-independent ion-energy coordinate.

The local P34 traveler now requires measured self-bias or a calibrated ion-energy proxy.

---

# Physical depth versus electrical depth remains a central invariant

Same-UWA 1997 evidence:

- physical recession ~`0.2 µm`;
- electrical conversion ~`1.5 µm`;

under `410 mTorr / CH4-H2 / 0.4 W cm^-2` on vacancy-doped p-type x≈0.31 material.

This permanently forbids:

`d_etch = d_conv`.

The cited ~8-µm n-type conversion relevant to the later photoconductor lineage remains a different result with incompletely recovered matched reactor conditions.

---

# Oxide-clear time is now separated from total RF time

RP-01 uses the RIE step both to open the anodic oxide and to modify the exposed HgCdTe.

P34 defines:

` t_sem = t_RF - t_clear `

where `t_clear` is locally measured on the actual P25 oxide.

This avoids silently treating all 60 s as semiconductor exposure.

---

# Same-manufacturer architecture evidence

A primary same-era Plasma Technology RIE80 publication on GaAs reports:

- RIE80;
- lower electrode driven at `13.56 MHz`;
- base pressure `<0.5 mTorr`;
- platform-temperature control.

This is retained as `PRIMARY-PLASMA-TECH-FAMILY`, not historical identification.

### Explicit rejected inference

Do not state that RP-01 used:

- RIE80;
- 13.56 MHz;
- <0.5 mTorr base pressure;
- 40 °C platform temperature.

None is directly recovered for the UWA process.

---

# Crystallographic state now follows the sample into RIE

Elkind & Orloff directly report strong HgCdTe orientation dependence in CH4/H2 RIE, including different short-time etch rates and morphologies for `(111)B`, `(100)` and `(111)A`.

P29 crystallographic genealogy must therefore persist into P34 rather than being discarded after LPE.

---

# New reactor-equivalence release vector

P34 defines:

`Y_RIE = {t_clear, self_bias(t), T_sample(t), d_etch, roughness, sheet_state, d_conv, L_conv, rho_c, blocking_response, detector_noise_delta}`.

A local process becomes `RP01-RIE-TRANSFER-QUALIFIED` only when repeated independently established chamber states reproduce a stable output vector and downstream P26/P09/P08F/device behavior.

Matching watts/pressure/flow/time is not enough.

---

# Source recovery result

John Kenion White's 2005 UWA thesis was confirmed in the current UWA repository and its PDF link identified, but the available retrieval route returned HTTP 403. This is preserved as `IDENTIFIED / FULL-TEXT-NOT-RECOVERED`, not treated as a negative source.

The thesis remains a high-value future target for exact UWA reactor/traveler details.

---

# Remaining high-priority RIE gaps

- exact Plasma Technology model;
- RF frequency;
- powered/grounded electrode areas;
- electrode spacing;
- sample holder/loading;
- base pressure;
- pump/throttle architecture;
- individual CH4/H2 MFC values;
- gas purity;
- chamber clean/seasoning history;
- self-bias;
- sample thermal state;
- RP-01 oxide-clear time;
- RP-01 physical HgCdTe recession;
- exact matched condition for ~8-µm n-type conversion.

---

# Next strongest empirical target

Proceed next with **Round 28: P11 absolute radiometry / blackbody / FOV apparatus reconstruction**, unless a newly recovered UWA source closes the RIE hardware first.

Why P11 is next:

- detector BLIP/D* claims depend directly on actual incident photon flux and optical geometry;
- RP-01 gives a stated 60° FOV and background condition, but package/aperture/window/source geometry is historically incomplete;
- P33 now makes package optical geometry explicit, so P11 is the natural downstream closure;
- absolute detector performance should not be declared reproduced until the radiometric reference plane, source temperature/emissivity, aperture geometry, spectral selection and modulation chain are empirically traceable.

Round 28 should first audit P11 to avoid duplicating already complete metrology, exactly as Round 26 audited P05.

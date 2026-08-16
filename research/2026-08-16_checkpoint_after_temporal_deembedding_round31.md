# Research checkpoint — after temporal-response / de-embedding Round 31

**Date:** 2026-08-16

## Objective

Audit P13/P13A against the now-mature P10A bias-network and P33 package-thermal layers, recover primary UWA transient-photoconductive-decay apparatus details, and determine whether a new top-level temporal module was required.

---

# Audit result

P13 was already method-complete in its core frequency/time-domain logic, so no duplicate top-level module was created.

However, the audit found three material defects/gaps:

1. P13's transfer equation omitted package thermal response despite direct HgCdTe-PC evidence in P33.
2. P13 mislabeled a 2004 Gopal/Devi/Pal/Kumar interface-trap paper as Musca/Faraone lineage.
3. P13A substantially under-recorded the detailed 1998 UWA apparatus and did not capture the thesis's own high-injection warning.

Round 31 therefore:

- revised `procedures/P13_TEMPORAL_FREQUENCY_RESPONSE_LIFETIME.md`;
- expanded `procedures/P13A_UWA_TRANSIENT_DECAY_LINEAGE_ADDENDUM.md`;
- added `travelers/P13A_TRANSIENT_RESPONSE_DEEMBEDDING_QUALIFICATION_REGISTER.md`;
- added Round31 source/gap ledgers;
- created this checkpoint.

---

# Strongest recovered UWA method branch

R. Rajaduray, UWA B.E. Honours thesis (1998), supervisor J. M. Dell, with acknowledged experimental assistance/advice from D. Redfern and E. P. G. Smith.

Directly recovered transient branch:

`Waterloo Scientific scanning laser microscope`

`1.047 µm / 25 ns optical pulse / 1 kHz repetition`

`-> n-HgCdTe x≈0.30 near 77 K under vacuum`

`-> Keithley variable-current bias, deliberately small to reduce sweepout`

`-> one analyzed bias state -1.05 V`

`-> AC-coupled voltage amplifier`

`-> HP54522A digital oscilloscope / PC`

`-> typically 128 waveform averages`

`-> 500 voltage samples at 20 ns spacing`

`-> Matlab transient analysis`.

This is the strongest same-UWA historical TPCD apparatus branch recovered so far.

It is **not** the RP-01 performance detector method unless a direct source later establishes that connection.

---

# Critical injection correction

The thesis itself estimates that a representative pulsed transient can create a localized initial excess-carrier population approaching the equilibrium majority-carrier scale.

Representative thesis calculation:

- sample active-layer volume estimate from ~`1 cm × 0.5 cm × 17 µm`;
- equilibrium electron count ~`4.25×10^11`;
- ~`0.17 V` transient at `-1.05 V` mapped to ~`8.2×10^10` generated carriers;
- generated carriers occupy a much smaller illuminated volume than the full layer.

Conclusion: local initial excitation may approach high-level injection; Auger recombination can alter early decay.

Permanent consequence:

**low average optical power + short pulse != low-injection lifetime measurement.**

P13 now requires pulse/modulation-level reduction, waveform/tau invariance and preferably an absorbed-carrier-density estimate before a low-injection interpretation.

---

# Optical-depth correction

The thesis estimates ~90% absorption of 1.047-µm photons within roughly 2.7 µm of x≈0.30 HgCdTe under its model.

Thus the historical TPCD branch is strongly near-surface weighted.

Do not assume:

`tau_TPCD(1.047 µm) = tau_response(4 µm)`.

A 4-µm RP-01 optical-response measurement samples a materially different absorption profile.

---

# Model-form correction

Rajaduray compared a simple exponential with a diffusion/recombination transient solution. The non-exponential model gave the better fit for the analyzed spatial-lifetime data.

P13 therefore treats a single exponential as a hypothesis requiring residual/fit-window/injection validation, not as the default physical model.

---

# Interface-trap provenance correction

P13 previously mislabeled:

V. Gopal, N. Devi, R. Pal, V. Kumar, JCG 265 (2004), DOI `10.1016/j.jcrysgro.2004.02.082`

as Musca/Faraone lineage.

That was wrong and is corrected.

Gopal 2004 and Pal 2001 remain primary **non-UWA transfer** evidence that:

- passivated/anodized HgCdTe can show delayed/non-simple TPCD structure;
- interface trapping can produce anomalous peaks/tails;
- DC bias can alter transient behavior.

This expands the mechanism set but does not establish anything specific about RP-01's anodic oxide transient behavior.

---

# Package-thermal integration

Bartoli et al. 1975 directly measured packaged HgCdTe-PC thermal recovery with:

- several-ms component;
- hundreds-ms component;
- both associated with thermally resistive bonding layers;
- response depending on irradiation power density/duration.

P13 now includes package context:

`H_meas = H_source H_optics H_detector H_bias H_preamp H_cable H_instrument H_pkg,thermal`

when a multiplicative representation is physically adequate; otherwise package thermal response is treated as a coupled/additive channel.

The rule is physical, not merely notational:

**a slow pole is not carrier lifetime until package heating is excluded or de-embedded.**

---

# AC-coupling issue now explicit

The 1998 UWA branch directly used an AC-coupled voltage amplifier.

Therefore a long decay/tail can be distorted by an undocumented high-pass transfer.

Historical values still open:

- amplifier circuit/model;
- capacitor/resistor values;
- gain;
- bandwidth;
- input impedance.

Local P13 uses measured detector-equivalent transfer rather than assuming flat gain.

---

# HP54522A state

Official HP/Keysight documentation supports apparatus capabilities around:

- 500-MHz analog bandwidth;
- up to 2 GSa/s;
- 32-k memory/channel.

These are manufacturer capability facts only.

Direct thesis acquisition facts remain:

- HP54522A;
- PC remote acquisition;
- 500 samples;
- 20-ns spacing;
- 128 waveform averages typical.

Input range/coupling/termination/trigger/internal filtering remain open.

---

# RP-01 historical temporal state after Round 31

Closed:

- RP-01 optical performance was measured at 1-kHz chopping;
- the same performance detector is used across Figures 3/5/6/7;
- field/bias state is handled by P10A.

Still open:

- RP-01 `tau`;
- RP-01 `f_3dB`;
- whether 1 kHz is on a flat detector-response plateau;
- any direct RP-01 transient apparatus;
- any direct linkage between Rajaduray 1998 TPCD samples and the RP-01 performance detector.

Do not infer `tau = 1/(2pi*1 kHz)` or any similar value.

---

# Redfern 1999 source status

Positively identified:

D. A. Redfern, C. Musca, E. P. G. Smith, J. Dell, L. Faraone, “On the Transient Photoconductive Decay Technique for Lifetime Extraction in HgCdTe,” conference proceedings, IEEE (1999), pp. 275–278.

This is the highest-value remaining same-UWA publication because its authors overlap directly with RP-01.

Full experimental text remains `IDENTIFIED-NOT-RECOVERED` through the current route.

Do not silently import Rajaduray details into the conference paper.

---

# P13A result classification

The new traveler forces temporal results into explicit evidence states:

- `SOURCE-LIMITED`
- `ELECTRICAL-LIMITED`
- `PACKAGE-THERMAL-CONTAMINATED`
- `HIGH-INJECTION`
- `TRAP/MULTICOMPONENT`
- `SWEEPOUT/TRANSPORT-CONTAMINATED`
- `EFFECTIVE-ONLY`
- `ONE-POLE-DEVICE-RESPONSE-QUALIFIED`
- `BULK-LIFETIME-JUSTIFIED`

`BULK-LIFETIME-JUSTIFIED` is deliberately the hardest classification.

---

# Permanent Round-31 rules

1. P13 includes P33 package thermal response in temporal interpretation.
2. Low average laser power does not prove low injection.
3. A 25-ns optical pulse does not prove a 25-ns-limited or small-signal detector measurement.
4. 1.047-µm near-surface decay is not automatically the same observable as 4-µm detector response.
5. Rajaduray `-1.05 V` is a same-UWA sample condition, not an RP-01 bias.
6. AC-coupled transient readout requires measured high-pass transfer.
7. HP54522A datasheet capabilities are not historical acquisition settings.
8. One-exponential fit is not a lifetime proof; inspect residuals/model alternatives and fit-window stability.
9. Time- and frequency-domain tau should agree before a one-pole interpretation is strong.
10. Slow ms/hundreds-ms HgCdTe-PC package poles cannot be labeled intrinsic lifetime without package discrimination.
11. Pal/Gopal interface-trap papers are non-UWA transfer evidence; preserve correct attribution.
12. RP-01 currently has no recovered historical lifetime or `f_3dB`.

---

# Strongest next action

Proceed with **Round 32: audit P06 FTIR composition/thickness apparatus and cutoff-definition closure**.

Why P06 next:

- P05, P10, P11, P12 and P13 are now method-mature with explicit historical/apparatus state layers;
- P06 remains a central material-to-device bridge because composition, physical thickness, optical absorption edge and detector cutoff can be silently conflated;
- an empirical apparatus audit can close FTIR spectral resolution, beam/aperture, substrate/background correction, fringe-based thickness, wavelength/wavenumber calibration, purge/background, and composition-model uncertainty.

Audit first:

- `procedures/P06_FTIR_COMPOSITION_THICKNESS_MAPPING.md`;
- relevant source ledgers/checkpoints for Hansen/Gopal composition models;
- any same-UWA/Fermionics/Honeywell optical characterization sources already present.

Priority questions:

1. exact FTIR/transmission/reflection apparatus classes and historical models where recoverable;
2. substrate/reference measurement and CdZnTe optical correction;
3. wavenumber/wavelength calibration and spectral resolution;
4. thickness from interference fringes versus independent profilometry;
5. `x` from optical gap/model versus detector spectral cutoff;
6. temperature associated with optical edge/model;
7. spatial mapping aperture/spot and wafer nonuniformity;
8. atmospheric purge/background and detector/beamsplitter changes across spectral bands;
9. uncertainty propagation from spectral calibration/thickness/model to composition.

Do not create a new top-level P06 replacement if the existing method is already operator-complete; add a lineage/apparatus transfer layer only if that is the genuine gap.

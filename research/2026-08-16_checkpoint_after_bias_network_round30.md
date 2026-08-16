# Research checkpoint — after bias/load-network Round 30

**Date:** 2026-08-16

## Round objective

Audit the existing P10 DC-bias/self-heating procedure and recover as much empirical information as possible about the UWA/RP-01 electrical network used to bias the HgCdTe photoconductor and feed the responsivity/noise instrumentation.

The key question was whether the remaining uncertainty justified a new top-level procedure or a narrower lineage/transfer addendum.

---

# Audit result

`procedures/P10_DEVICE_DC_BIAS_SELF_HEATING.md` is already operationally adequate.

It already contains:

- measured contact-gap metrology;
- `E=V_active/L`;
- active-area discipline;
- correction for contact/series/load voltage drops;
- symmetric I-V qualification;
- low-field ohmic gate;
- measured self-heating rather than universal power limit;
- R(T), pulsed/DC and duty-cycle thermal checks;
- sweepout-versus-heating discrimination;
- polarity testing;
- explicit load-circuit documentation requirements.

Therefore no duplicate top-level P35/P36/P37 was created.

Round 30 created:

- `procedures/P10A_UWA_BIAS_LOAD_NETWORK_LINEAGE_TRANSFER_ADDENDUM.md`
- `travelers/P10A_BIAS_LOAD_NETWORK_TRANSFER_REGISTER.md`
- `docs/SOURCE_LEDGER_ADDENDUM_ROUND30.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND30.md`
- this checkpoint.

---

# Strongest direct historical advance

The canonical Smith et al. 2001 paper explicitly describes the Figure-3 applied electric field as **voltage bias between the contacts**.

This sharpens the historical meaning of the quoted field:

`E = V_contact-contact / L_active`.

The correct reproduction target is therefore the voltage actually established across the selected detector contact pair, not a nominal supply setting divided by mask gap.

This remains compatible with P10's earlier physics, but Round 30 upgrades it from a local best-practice rule to a direct historical interpretation.

---

# Same-device performance chain remains important

Round 29 established:

`Figure 3 -> Figure 5 -> Figure 6 -> Figure 7 = same physical detector`.

Round 30 now ties that detector to one common electric-field definition.

Still unresolved:

- which of the nine contact gaps was used;
- current at 10 V/cm;
- detector resistance;
- source/load network;
- preamp input impedance;
- whether P11 and P12 used an unchanged bias/readout topology.

Do not turn same-device identity into an assumed active area.

---

# Same-UWA electronics lineage recovered

Hatch et al. 2011, DOI `10.1063/1.3540655`, directly states that UWA photoconductors were connected to a **low-noise voltage preamplifier specifically designed so a bias voltage could be applied to the device**.

Direct transfer details:

- continuous-flow cryostat with ZnSe window;
- chopping just below 1 kHz;
- fields 5–80 V/cm;
- 250 mV bias for temperature-dependent measurements;
- 250 mV corresponded to 9.2 V/cm in one device and 8.6 V/cm in another;
- preamplifier citation was J. F. Siliquini's 1995 UWA PhD thesis.

This is strong evidence that a bias-capable low-noise voltage-readout architecture persisted in the UWA photoconductor program.

It is **not proof** that RP-01 used the identical 2011 or 1995 circuit.

---

# Siliquini thesis priority increased again

The 1995 UWA PhD thesis remains the single highest-value archival electronics target because later UWA experimental work cites it directly for the preamplifier.

On recovery extract:

- schematic;
- component values;
- bias injection;
- supply rails;
- gain and bandwidth;
- input/output impedance;
- voltage/current noise;
- source-resistance assumptions;
- AC coupling/high-pass network;
- shielding/grounding;
- analyzer interface.

No circuit values were guessed in this round.

---

# Power/self-heating transfer evidence

Siliquini/Faraone's 1996 and 1997 UWA photoconductor-array work treats detector power dissipation as a major architecture constraint. The 1997 vertical-photoconductor analysis includes pulsed biasing in its low-power array concept.

This does not establish pulsed RP-01 operation.

It does establish an evidence-based reason to retain:

`u_bias = {V_contact(t), I(t), duty, pulse width, repetition rate, settling time}`

whenever self-heating is being separated from sweepout.

Equal peak field does not guarantee equal detector temperature or responsivity.

---

# Electrical transfer architecture formalized

P10A treats the measurement chain as:

`bias source -> source/load network -> HgCdTe contact pair -> coupling/readout -> preamplifier -> P11/P12 instrument`.

Required measured quantities include:

- source voltage;
- detector-contact voltage;
- detector current;
- static and differential resistance;
- source/load resistance;
- preamp input impedance;
- small-signal transfer `H_sig(f)`;
- detector-noise transfer `H_noise(f)`;
- source/network noise;
- thermal response.

The released vector is

`Y_bias={contact_pair,L,W,V_source,V_contact,I,E,P_det,R_static,R_diff,H_sig(f),H_noise(f),Z_pre(f),source_noise,T_detector_proxy,H_pkg,thermal,duty,polarity,sweepout_metric}`.

---

# Important local equations

## Actual field

`E = V_contact / L_active`.

## Reconstructed detector voltage when direct sense is unavailable

`V_contact = V_source - I R_series - V_other_drops`.

## Detector power

`P_det = V_contact I`.

## Simple steady thermal approximation

`Delta T ≈ P_det R_theta`

only where package thermal behavior is linear and steady-state. P33 requires time-domain thermal qualification because package bond layers can create slow poles.

## Simple linear load example

For a Thevenin source:

`V_d = V_TH R_d/(R_TH+R_d)`.

Do not use this fixed-R form when measured detector I-V or illumination makes `R_d` nonlinear.

---

# P11/P12 state identity strengthened

Round 29 already required matched detector/background/frequency state before D*.

Round 30 adds explicit **electrical topology identity**.

Before joint D* calculation compare:

- physical detector;
- contact pair;
- active gap;
- detector-terminal voltage/field;
- current and detector power;
- static/differential resistance;
- source/load topology;
- preamp loading;
- thermal state;
- package/window/FOV/background;
- signal-frequency convention.

Allowed disposition:

- `STATE-ELECTRICALLY-IDENTICAL`;
- `CORRECTED-TO-COMMON-ELECTRICAL-STATE`;
- `INCOMPATIBLE — DO NOT CALCULATE JOINT D*`.

---

# Negative searches / unresolved history

Targeted searches did not recover primary values for:

- RP-01 bias-source make/model;
- load/series resistor;
- resistor temperature;
- detector current at 10 V/cm;
- detector R at 10 V/cm;
- exact contact pair;
- AC-coupling components;
- preamp input impedance;
- 2001 signal/noise topology identity.

These remain `OPEN-HISTORICAL`.

The search also re-identified these useful primary sources:

- Siliquini et al. 1995 IEEE TED MWIR photoconductor paper, DOI `10.1109/16.398658`;
- Siliquini et al. 1994 optimized LWIR photoconductor paper, DOI `10.1016/1350-4495(94)90059-0`;
- Siliquini/Faraone 1996 array paper, DOI `10.1088/0268-1242/11/12/024`;
- Siliquini/Faraone 1997 vertical-PC paper, DOI `10.1016/S1350-4495(97)00016-9`.

No accessible primary text in Round 30 closed the exact 2001 circuit.

---

# Permanent Round-30 rules to carry forward

1. RP-01 field means contact-to-contact voltage bias divided by active gap.
2. Supply voltage is not detector field unless source/load/contact drops are shown negligible.
3. Same physical detector does not identify the selected contact gap.
4. P10's ~1.79-mA current is a derived screening value, not historical current.
5. A later UWA bias-capable low-noise voltage preamp is lineage evidence, not exact RP-01 circuit identity.
6. Bias/load resistor noise must be propagated through the actual network before subtraction from P12.
7. AC coupling/high-pass behavior must be measured, especially across 1 kHz and the 1/f-knee region.
8. Equal peak field under DC and pulsed bias does not imply equal thermal state.
9. P11/P12 joint D* requires electrical-state identity as well as optical/thermal identity.
10. No historical bias topology, source resistor, battery, pulse scheme or contact gap may be invented from a plausible circuit.

---

# Strongest next action

Proceed with **Round 31: P13 temporal-response apparatus / source / package de-embedding audit** unless a new route to the Siliquini thesis becomes available.

Audit first:

- `procedures/P13_TEMPORAL_FREQUENCY_RESPONSE_LIFETIME.md`
- `procedures/P13A_UWA_TRANSIENT_DECAY_LINEAGE_ADDENDUM.md`
- P33 package thermal procedure/checkpoint.

Priority historical recovery:

- optical modulation source type/wavelength;
- pulse/chopper waveform;
- source rise/fall time;
- detector field and exact bias topology during transient tests;
- preamp bandwidth and AC coupling;
- oscilloscope/analyzer model and termination;
- whether any historical lifetime was inferred from optical transient, frequency response, or noise;
- package thermal transients versus intrinsic carrier response;
- exact UWA transient-decay method in same-lineage HgCdTe material.

Create a new top-level module only if P13 is genuinely method-incomplete. Otherwise create a lineage/de-embedding addendum + register as in Rounds 28–30.

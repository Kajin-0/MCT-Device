# P08F — blocking-contact sweepout functional qualification

**Status:** CONTROLLED FUNCTIONAL ADDENDUM. Supplements P08/P08D/P08E and P10/P11/P12/P13.

## 1. Purpose

Define the functional detector-level acceptance test for the RP-01 RIE-induced n+/n blocking contact.

The blocking-contact process exists to do more than lower specific contact resistance. Its device-level purpose is to reduce loss of photogenerated minority carriers at the metal/contact region, suppress bias-dependent sweepout, and preserve detector responsivity without unacceptable noise or power penalty.

Therefore a transferred RIE/contact process cannot be released on Hall + TLM alone.

## 2. Same-UWA functional lineage

### Siliquini et al. 1994 — optimized LWIR photoconductors

J. F. Siliquini, C. A. Musca, B. D. Nener, L. Faraone, “Performance of optimized Hg1−xCdxTe long wavelength infrared photoconductors,” *Infrared Physics & Technology* 35(5), 661–671 (1994), DOI `10.1016/1350-4495(94)90059-0`.

This work describes a combined overlap-geometry/blocking-contact structure intended to reduce minority-carrier sweepout. Experimental comparisons indicate enhanced responsivity, low-frequency noise performance and detectivity relative to simpler blocking-contact structures in the LWIR devices studied.

Use: functional-physics lineage only; material/geometry differ from RP-01.

### Smith, Musca, Faraone 2000 — 2-D MWIR model

E. P. G. Smith, C. A. Musca, L. Faraone, “Two-dimensional modelling of HgCdTe photoconductive detectors,” *Infrared Physics & Technology* 41(3), 175–186 (2000), DOI `10.1016/S1350-4495(99)00054-7`.

This same-RP-01-team source demonstrates that practical top-contact photoconductor behavior is intrinsically two-dimensional. A practical MWIR device was fit using a modeled n+ region with:

- n+ density `1×10^16 cm^-3`;
- n+ depth `3 µm`.

Those are model parameters for the modeled detector, **not** RP-01 measured RIE targets.

The model shows that blocking-contact geometry/doping alters the spatial electric field and excess-minority-carrier distribution and therefore the responsivity/sweepout behavior.

## 3. Functional success criterion

The RIE/contact module should be considered successful only if the completed detector demonstrates, over its intended field range:

- ohmic/stable majority-carrier contact behavior;
- acceptable cryogenic TLM `rho_c`;
- reduced responsivity saturation/rolloff from minority-carrier sweepout;
- no unacceptable increase in 1/f, g-r or contact-related noise;
- no instability under bias polarity reversal/thermal cycling;
- no large parasitic optical loss attributable to the modified contact region.

## 4. Required control structures

During local qualification include matched devices that isolate blocking-contact functionality as far as practical.

Preferred comparison:

1. released-candidate RIE n+/n blocking-contact device;
2. otherwise identical control with a deliberately less-effective/nonblocking contact process, where safe and scientifically justified;
3. optional contact-geometry/depth splits around the selected RIE condition.

The control is a development structure, not a production architecture.

## 5. Bias-field sweepout test

Using P10 geometry/bias control, measure over a safe electric-field grid:

- detector current;
- active-region voltage;
- power dissipation;
- P11 responsivity at one or more wavelengths;
- P12 noise ASD at the same signal frequency;
- P13 frequency response/time constant where relevant.

Normalize field using actual fabricated contact separation:

`E = V_active / L_measured`.

Do not compare devices at equal terminal voltage if their gaps differ.

## 6. Responsivity sweepout metric

Define a low-field reference responsivity in the linear, self-heating-negligible region:

`R0 = R(E_ref)`.

Then define a normalized field response:

`S_R(E) = R(E) / R0`.

A blocking-contact process that maintains `S_R(E)` closer to unity over the intended field range is functionally superior, provided the comparison is made at matched optical state and temperature and is not confounded by heating.

The exact production limit for allowed responsivity rolloff remains `QUAL` and must be set from system/device requirements and local repeatability.

## 7. Separate sweepout from self-heating

For every field point record P10 thermal indicators.

If responsivity changes correlate with detector heating, the effect may be thermal rather than contact sweepout.

A sweepout interpretation should be supported by at least one of:

- response changes at constant detector temperature/power-controlled condition;
- contact-geometry dependence;
- P13 lifetime/time-response changes consistent with carrier extraction;
- spatial carrier modeling/LBIC evidence;
- agreement with a validated 2-D transport model.

## 8. Noise-functional gate

At the same field grid measure P12 detector-referred noise at the signal frequency.

Compute:

`NEP(E) = e_n(E,f) / R(E,f)`

and

`D*(E) = R(E,f) sqrt(A) / e_n(E,f)`.

A blocking contact that improves responsivity but introduces enough excess low-frequency/contact noise to degrade NEP/D* is not an acceptable optimization.

## 9. Temporal-response functional gate

P13 measurements can help distinguish recombination/contact effects.

Record `tau_eff(E)` alongside `R(E)`.

A strong field dependence of `tau_eff` together with responsivity rolloff may indicate carrier extraction/sweepout. A purely resistance/temperature-driven change must be separated by the P10 thermal controls.

Do not label `tau_eff` a bulk lifetime unless P13 criteria are satisfied.

## 10. Geometry/depth tradeoff

Increasing blocking-region depth or doping can reduce contact recombination but may also:

- alter active-volume electric field;
- increase free-carrier absorption;
- increase parasitic sheet conduction;
- change optical fill/active area;
- worsen surface-damage conduction if the process is too aggressive.

Therefore optimization target is not “maximum n+” or “maximum depth.”

Use a multi-objective response:

`J_contact = {rho_c, S_R(E), e_n(E,f), D*(E), optical loss, transport decomposition, stability}`.

## 11. Relationship to historical RP-01 targets

Historical direct benchmarks remain:

- RP-01 nominal RIE: `64 sccm / 100 mTorr / 50 W / 60 s`;
- historical reported averaged converted density `~2×10^15 cm^-3`;
- mobility `~3.3×10^4 cm²/Vs`;
- 80-K TLM `rho_c≈9×10^-4 Ω·cm²`;
- detector BLIP D* `~2×10^11 cm Hz^1/2/W` at 4 µm, 80 K, stated 60° FOV.

The 2000 model's `1×10^16 cm^-3 / 3 µm` n+ region is **not** substituted for the RP-01 RIE state.

## 12. Release rule

An RIE/contact condition may be promoted from `TRANSFER-QUALIFIED` to the local production candidate only after all of the following are demonstrated on repeated devices:

1. stable P08D plasma/process outputs;
2. physically credible P08E transport state;
3. P09 acceptable TLM/contact stability;
4. P10 self-heating-safe operation;
5. responsivity-versus-field consistent with adequate blocking-contact function;
6. P12 noise/NEP/D* not degraded by the contact process;
7. acceptable reproducibility across devices/runs.

This is the detector-level closure of the P08 process.
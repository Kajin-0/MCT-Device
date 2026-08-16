# Source ledger addendum — Round 30

## Scope

Round 30 audited P10 and searched for empirical/historical closure of the UWA HgCdTe photoconductor bias/load/readout network used around RP-01.

The audit found that `P10_DEVICE_DC_BIAS_SELF_HEATING.md` is already an operationally adequate DC-field/self-heating SOP. Round 30 therefore created P10A as a lineage/network-transfer addendum rather than a duplicate top-level procedure.

Evidence classes used below:

- `RP01-DIRECT` — direct canonical 2001 paper.
- `SAME-UWA-TRANSFER` — UWA photoconductor lineage, but different date/device.
- `PRIMARY-TRANSFER` — primary HgCdTe source with useful physical method but not RP-01 lineage identity.
- `IDENTIFIED-NOT-RECOVERED` — source positively identified, full experimental text not recovered.
- `NEGATIVE-RECOVERY` — targeted search performed without closure of the requested historical detail.

---

## S30-01 — Smith et al. 2001 canonical RP-01

**Citation**

E. P. G. Smith, K. J. Winchester, C. A. Musca, J. M. Dell, L. Faraone, “A simplified fabrication process for HgCdTe photoconductive detectors using CH4/H2 reactive-ion-etching-induced blocking contacts,” *Semiconductor Science and Technology* 16, 455–462 (2001), DOI `10.1088/0268-1242/16/6/306`.

**Class:** `RP01-DIRECT`

### Newly emphasized direct text

For the Figure-3 responsivity measurement the paper states that the response is measured as a function of applied electric field and parenthetically identifies that field as **voltage bias between the contacts**.

Direct performance coupling:

- Figure 3: responsivity versus electric field, 4 µm, 80 K, 60° FOV, 1-kHz chopping;
- Figure 5: averaged noise-voltage spectrum, 10 V/cm, 80 K, stated 60° FOV, low-noise preamplifier, HP35665A;
- Figures 6 and 7: spectral responsivity and D* at 10 V/cm, 80 K, 60° FOV;
- Figures 3, 5, 6 and 7 use the same physical detector.

### Round-30 consequence

Historical electric field is anchored to the selected detector contact pair:

`E = V_contact-contact / L_active`.

This does not establish the source/load topology.

### Still absent from RP-01

- supply/source model;
- source resistance;
- series/load resistor;
- detector current at 10 V/cm;
- detector resistance at 10 V/cm;
- detector-terminal sense method;
- AC coupling/bias tee;
- preamplifier input impedance;
- contact pair/gap used for performance figures;
- whether responsivity and noise shared one unchanged electrical network.

---

## S30-02 — Hatch et al. 2011 UWA photoconductor readout lineage

**Citation**

S. D. Hatch, C. A. Musca, C. R. Becker, J. M. Dell, L. Faraone, “Photoresponse in photoconductor devices fabricated from HgTe-HgCdTe superlattices,” *Applied Physics Letters* 98, 043505 (2011), DOI `10.1063/1.3540655`.

**Class:** `SAME-UWA-TRANSFER`

### Direct experimental details

The paper states:

- photoconductors mounted in continuous-flow cryostat with ZnSe window;
- photoconductor output connected to a **low-noise voltage preamplifier specifically designed so that a bias voltage could be applied to the device**;
- chopping frequency just below 1 kHz;
- fields varied approximately 5–80 V/cm;
- temperature-dependent runs used 250 mV bias;
- 250 mV corresponded to 9.2 V/cm in one device and 8.6 V/cm in another;
- preamplifier source citation: J. F. Siliquini, PhD thesis, UWA, 1995.

### Use

Strong evidence for a persistent UWA voltage-domain photoconductor readout/bias lineage and for the Siliquini thesis as the highest-value archival circuit source.

### Restriction

Different material/device generation and ten years after RP-01. Do not assign its exact circuit, cryostat, ZnSe window, 250-mV bias or device dimensions to RP-01.

---

## S30-03 — Siliquini & Faraone 1997 vertical photoconductor

**Citation**

J. F. Siliquini, L. Faraone, “The vertical photoconductor: A novel device structure suitable for HgCdTe two-dimensional infrared focal plane arrays,” *Infrared Physics & Technology* 38, 205–221 (1997), DOI `10.1016/S1350-4495(97)00016-9`.

**Class:** `SAME-UWA-TRANSFER`

### Direct relevant result

The paper treats detector impedance, applied bias field and power dissipation as coupled design quantities. Its proposed array operation uses pulsed biasing to obtain low total dissipation.

### Use

Empirical/engineering evidence that bias duty cycle and detector power are meaningful HgCdTe photoconductor operating coordinates.

### Restriction

Vertical photoconductor architecture, not RP-01 lateral planar device. It does not prove RP-01 was pulse biased.

---

## S30-04 — Siliquini & Faraone 1996 3×3 array

**Citation**

J. F. Siliquini, L. Faraone, “Two-dimensional infrared focal plane arrays based on HgCdTe photoconductive detectors,” *Semiconductor Science and Technology* 11, 1906–1911 (1996), DOI `10.1088/0268-1242/11/12/024`.

**Class:** `SAME-UWA-TRANSFER`

### Direct relevant result

The UWA photoconductor array architecture was explicitly motivated in part by reduced power dissipation and demonstrated BLIP performance at 80 K.

### Use

Supports P10/P33 treatment of electrical power and thermal state as performance variables.

### Restriction

Not the RP-01 test circuit and not evidence for any numerical power limit on RP-01.

---

## S30-05 — Siliquini et al. 1995 MWIR photoconductor performance

**Citation**

J. F. Siliquini, C. A. Musca, B. Nener, L. Faraone, “Temperature dependence of Hg0.68Cd0.32Te infrared photoconductor performance,” *IEEE Transactions on Electron Devices* 42, 1441–1448 (1995), DOI `10.1109/16.398658`.

**Class:** `PRIMARY-SAME-UWA / FULL-EXPERIMENTAL-TEXT-NOT-RECOVERED-IN-ROUND30`

### Why it matters

Compositionally close MWIR n-type HgCdTe, same laboratory lineage, and directly concerned with detector responsivity/noise/detectivity versus temperature.

Public indexing confirms publication identity but did not expose enough experimental text in this round to recover the bias/load circuit.

### Status

`IDENTIFIED-NOT-RECOVERED` for detailed electronics.

---

## S30-06 — J. F. Siliquini 1995 UWA PhD thesis

**Citation identity currently available**

J. F. Siliquini, PhD thesis, The University of Western Australia, 1995.

Later UWA APL work cites this thesis specifically for the bias-capable low-noise voltage preamplifier.

**Class:** `IDENTIFIED-NOT-RECOVERED / HIGHEST-PRIORITY-ARCHIVAL`

### Required extraction on acquisition

- thesis title/catalog ID;
- full preamplifier schematic;
- input device(s);
- resistor/capacitor values;
- detector bias injection;
- supply rails;
- gain;
- bandwidth;
- input/output impedance;
- voltage/current noise;
- source-resistance assumptions;
- AC coupling;
- shielding/grounding;
- measurement/analyzer interface.

No circuit values are inferred in P10A.

---

## S30-07 — 1994 optimized LWIR UWA photoconductor paper

**Citation**

J. F. Siliquini, C. A. Musca, B. D. Nener, L. Faraone, “Performance of optimized Hg1-xCdxTe long wavelength infrared photoconductors,” *Infrared Physics & Technology* 35, 661–671 (1994), DOI `10.1016/1350-4495(94)90059-0`.

**Class:** `SAME-UWA-TRANSFER`

### Recovered public primary content

The paper compares blocking-contact/overlap photoconductor performance and explicitly treats sweepout, responsivity, 1/f noise and detectivity as coupled device metrics.

### Round-30 use

Supports the separation of contact/sweepout physics from purely thermal responsivity saturation.

### Restriction

No executable bias/load schematic was recovered from accessible primary text in this round.

---

# Negative recovery record

Targeted searches were performed for combinations of:

- Siliquini / Faraone / Musca;
- HgCdTe photoconductor;
- bias resistor / load resistor;
- preamplifier;
- bias voltage;
- power dissipation;
- UWA 1994–2011 papers/thesis references.

No primary source recovered in Round 30 supplied the exact RP-01:

- bias-source model;
- series/load resistor value;
- coupling-capacitor value;
- preamp input impedance;
- detector current at 10 V/cm;
- performance contact gap;
- Figure-3/5/6/7 electrical schematic.

This is `NEGATIVE-RECOVERY`, not evidence that those details never existed.

---

# Derived/local items — not literature facts

The following are retained as calculations or local method constructs:

- P10 ideal one-carrier screening current `~1.79 mA` at 10 V/cm using supplier n/µ and nominal `W=300 µm`, `t=9.5 µm`;
- ideal gap-dependent voltage/power table;
- Thevenin/load-line equations in P10A;
- `H_sig(f)` and `H_noise(f)` transfer characterization;
- local duty-cycle/DC self-heating experiment;
- local P11/P12 electrical-state identity matrix.

None may be relabeled as historical RP-01 values.

---

# Round-30 evidence conclusion

The historical bias reconstruction advances from

`10 V/cm nominal applied field`

to the stronger statement

`10 V/cm = voltage bias between the selected detector contacts divided by active gap`,

while the source/load/preamp implementation remains open.

The strongest transfer lineage is:

`biased photoconductor -> bias-capable low-noise voltage preamplifier -> response/noise instrumentation`,

with the Siliquini 1995 thesis the key missing circuit source.

P10A therefore releases local reproduction by detector-terminal state and calibrated electrical transfer, not by an invented historical schematic.

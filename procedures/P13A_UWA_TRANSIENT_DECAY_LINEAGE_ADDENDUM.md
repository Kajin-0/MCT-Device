# P13A — UWA x≈0.30 HgCdTe transient-photoconductive-decay apparatus lineage

**Status:** `PRIMARY-THESIS / SAME-UWA-LAB — APPARATUS SUBSTANTIALLY CLOSED; SOURCE ENERGY AND READOUT CIRCUIT PARTLY OPEN`

**Parent:** `procedures/P13_TEMPORAL_FREQUENCY_RESPONSE_LIFETIME.md`

## 1. Purpose

Record the strongest recovered UWA experimental implementation of transient photoconductive decay (TPCD) in n-type `x≈0.30` HgCdTe from the immediate laboratory lineage surrounding RP-01, and distinguish those historical method details from the still-unpublished temporal response of the RP-01 detector itself.

This addendum is not an RP-01 lifetime specification. It is an empirical apparatus/methodology anchor for P13.

---

## 2. Primary source and laboratory lineage

Ramesh Rajaduray, *Investigation of Spatial Characterisation Techniques in Semiconductors*, B.E. (Honours) thesis, Department of Electrical and Electronic Engineering, The University of Western Australia, 1998. Supervisor: Dr John M. Dell.

The thesis acknowledges experimental assistance/advice from:

- David Redfern;
- E. P. G. Smith;
- Lorenzo Faraone and the UWA detector group.

This places the work directly in the UWA detector-characterisation lineage immediately preceding Smith et al. 2001.

A closely related conference paper is positively identified:

D. A. Redfern, C. Musca, E. P. G. Smith, J. Dell, L. Faraone, “On the Transient Photoconductive Decay Technique for Lifetime Extraction in HgCdTe,” *1998 Conference on Optoelectronic and Microelectronic Materials and Devices Proceedings*, IEEE (published 1999), pp. 275–278.

Its full experimental text remains `IDENTIFIED / NOT-RECOVERED` through the current route.

---

## 3. Material/sample branch

The Rajaduray transient experiments used:

- LPE-grown n-type HgCdTe;
- nominal `x≈0.30` active/top layer;
- wider-bandgap material beneath the active layer;
- wet-etched test structure using Br2/HBr chemistry;
- indium contacts pressed at opposite ends of the sample;
- liquid-nitrogen cryogenic operation near `77 K`;
- vacuum environment.

This is **not asserted to be the RP-01 wafer or detector geometry**.

The thesis sample and RP-01 differ in contact implementation and device purpose. Therefore no transient lifetime or voltage from this branch is an RP-01 production target.

---

## 4. Optical excitation — direct historical values

The transient branch used a Waterloo Scientific scanning laser microscope.

Recovered direct excitation values:

- wavelength: `1.047 µm`;
- pulsed operation;
- repetition frequency: `1 kHz`;
- pulse duration: `25 ns`;
- optical power deliberately limited to avoid sample damage.

### Still open

The recovered thesis text does not close:

- exact laser make/model beyond the Waterloo scanning-laser system context;
- pulse energy at the sample;
- calibrated peak optical power;
- pulse rise/fall time;
- pulse-to-pulse jitter;
- exact illuminated spot diameter/profile in the analyzed transient experiment;
- absolute absorbed photon density for every scan condition.

Do not invent these from typical Nd:YLF/YAG laser specifications.

---

## 5. Absorption-depth / excitation-profile consequence

The thesis estimated that approximately 90% of 1.047-µm photons are absorbed within roughly `2.7 µm` of `x≈0.30` HgCdTe under its absorption model.

This is important because a 1.047-µm TPCD experiment weights the near-surface carrier population much more strongly than an RP-01 in-band ~4-µm optical response.

Therefore:

`tau_TPCD(1.047 µm) != tau_detector(4 µm)`

in general.

They may agree in a bulk-recombination-dominated device, but equality must be demonstrated rather than assumed.

---

## 6. Bias/readout apparatus — direct historical values

The thesis directly documents:

- sample bias from a **Keithley variable-current source**;
- bias intentionally kept small to reduce sweepout of excess carriers toward high-recombination contact regions;
- analyzed sample bias reported as `-1.05 V`;
- photoconductive voltage change amplified using an **AC-coupled amplifier**;
- transient recorded by an **HP54522A digital oscilloscope**;
- oscilloscope remotely controlled by a PC;
- numerical analysis performed in Matlab.

### Evidence-safe interpretation

The explicit low-bias rationale is direct evidence that drift to contacts can shorten/distort a TPCD transient and must be separated from bulk recombination.

### Prohibited transfer

Do not use `-1.05 V` as an RP-01 field or bias value. The active geometry and circuit of the Rajaduray sample differ from RP-01.

### Still open

- Keithley model;
- current-source setting corresponding to the analyzed `-1.05 V`;
- source compliance/output impedance;
- detector current/resistance;
- AC-coupled amplifier model/circuit;
- coupling capacitor/resistor values;
- amplifier gain/noise/bandwidth/input impedance;
- cable/termination details;
- oscilloscope input coupling/range/termination/trigger settings.

These details require further archival recovery or local transfer calibration.

---

## 7. Digitization and averaging — direct historical values

For a typical transient scan coordinate the thesis directly gives:

- `128` waveform averages;
- `500` stored voltage samples per decay curve;
- `20 ns` spacing between samples.

This corresponds to a nominal sampled transient window of approximately `10 µs` depending on whether one counts 499 or 500 inter-sample intervals.

P13 shall preserve the direct values, but not copy them automatically into a new setup.

A local acquisition shall choose sample interval, analog bandwidth and record duration based on the expected detector dynamics and the calibrated source/readout response.

---

## 8. Official HP54522A capability — apparatus context only

Official HP/Keysight legacy documentation identifies the HP54522A as a two-channel digitizing oscilloscope with approximately:

- `500 MHz` analog bandwidth;
- up to `2 GSa/s` sample rate;
- `32 k` acquisition memory per channel;
- sequential single-shot capability.

These are instrument capabilities, not proof of the exact UWA settings beyond the thesis's explicitly reported `500 × 20 ns` stored waveform and typical `128` averages.

Do not infer UWA input range, trigger delay, termination or internal filtering from the instrument datasheet.

---

## 9. High-injection warning — direct thesis analysis

A critical result of the thesis is that **short pulse + low average optical power did not guarantee low injection**.

For one analyzed sample/calculation the thesis used approximately:

- active-layer dimensions `1 cm × 0.5 cm × 17 µm`;
- equilibrium electron population in that full volume ~`4.25×10^11`;
- representative photoconductive transient `~0.17 V` at `-1.05 V` bias;
- estimated generated carrier population ~`8.2×10^10`.

Because optical generation was confined to a much smaller illuminated volume, the thesis concluded that the local initial excess-carrier density could become comparable with the majority-carrier concentration, approaching **high-level injection**, where Auger recombination can materially alter the decay.

### Permanent P13 consequence

“Laser power was kept low” is not a sufficient small-signal criterion.

Every lifetime-oriented local TPCD measurement must test waveform/time-constant invariance as pulse fluence is reduced and, where possible, estimate the local excess-carrier density relative to equilibrium carrier density.

---

## 10. Decay-model evidence

The thesis did not simply assume a single exponential.

It compared:

- a single-exponential decay representation; and
- a diffusion/recombination solution that allows spatial redistribution of carriers.

For the analyzed spatial-lifetime data, the non-exponential model provided the better fit.

The thesis also showed that the apparent decay/lifetime can depend on:

- elapsed time after excitation;
- spatial position;
- diffusion;
- surface/contact recombination;
- excitation level.

### P13 consequence

Do not reduce an arbitrary TPCD waveform to one `tau` without:

1. raw-waveform retention;
2. fit-window sensitivity;
3. injection-level test;
4. residual inspection;
5. comparison of one- and multi-component/physical models;
6. field dependence check;
7. package/readout/source de-embedding.

---

## 11. Sample-specific numerical lifetimes are not RP-01 targets

The thesis reports spatial/elapsed-time-dependent lifetime analyses for its samples, including values in the several-microsecond range for portions of the HgCdTe region.

These values depend on its:

- sample geometry;
- 1.047-µm excitation profile;
- injection level;
- surface/buffer/contact boundary conditions;
- transient model;
- fit time.

They are retained as same-UWA empirical context only.

No Rajaduray lifetime is an RP-01 pass/fail threshold.

---

## 12. Interface-trap transient evidence — provenance correction

Two useful primary HgCdTe transient papers are **not UWA lineage**:

- R. Pal et al., “Study of interface traps from transient photoconductive decay measurements in passivated HgCdTe,” *Journal of Electronic Materials* 30, 103–108 (2001), DOI `10.1007/s11664-001-0108-x`;
- V. Gopal et al., “Study of the traps at a mercury cadmium telluride–anodic oxide interface using a transient photoconductive decay technique,” *Journal of Crystal Growth* 265, 530–536 (2004), DOI `10.1016/j.jcrysgro.2004.02.082`.

The previous P13 wording incorrectly associated the 2004 paper with Musca/Faraone lineage. That attribution is corrected.

Their value is **transfer physics**: delayed/non-simple transient structure and DC-bias dependence can arise from HgCdTe/passivant interface trapping.

---

## 13. Package thermal response — separate physical branch

Bartoli et al., *Applied Optics* 14, 2499–2507 (1975), DOI `10.1364/AO.14.002499`, directly measured thermal recovery in packaged HgCdTe photoconductors.

The package showed recovery scales of:

- several milliseconds; and
- hundreds of milliseconds,

attributed to thermally resistive bonding layers.

These slow package poles are physically different from the µs-class Rajaduray carrier-decay branch.

### Rule

Timescale separation can be useful evidence, but **timescale alone does not prove mechanism**. A slow pole must be tested against P33 package thermal response, optical/electrical heating dependence and package construction before it is assigned to carrier trapping or lifetime.

---

## 14. Historical branch summary

The direct 1998 UWA TPCD branch is:

`1.047-µm / 25-ns pulse / 1-kHz repetition`

`-> x≈0.30 n-HgCdTe near 77 K in vacuum`

`-> low Keithley current bias (one analyzed state -1.05 V)`

`-> photoconductive voltage`

`-> AC-coupled amplifier`

`-> HP54522A`

`-> 500 samples at 20 ns / 128 waveform averages typical`

`-> Matlab transient-model analysis`.

This is the strongest same-UWA historical lifetime-method branch currently recovered.

---

## 15. What this branch does not establish

It does not establish:

- any RP-01 detector `tau`;
- RP-01 `f_3dB`;
- RP-01 temporal response at 1 kHz;
- RP-01 use of the Waterloo laser microscope for lifetime testing;
- RP-01 use of a Keithley current source;
- RP-01 use of the HP54522A;
- RP-01 use of `-1.05 V`;
- equality between 1.047-µm decay and 4-µm response;
- low-injection operation merely because a 25-ns pulse was used.

All such transfers require new evidence or local qualification.

---

## 16. Release implication

P13 remains the canonical temporal-response SOP. P13A supplies a quantitative same-UWA apparatus lineage and strengthens four mandatory controls:

1. **low-field lifetime branch** before high-field sweepout interpretation;
2. **injection-level branch** before calling a decay small-signal lifetime;
3. **AC-readout/source de-embedding** before assigning waveform poles;
4. **non-exponential/package/interface alternatives** before identifying a bulk carrier lifetime.

The highest-value historical next source is the full Redfern/Musca/Smith/Dell/Faraone 1999 conference paper and any UWA apparatus/software record linked to it.

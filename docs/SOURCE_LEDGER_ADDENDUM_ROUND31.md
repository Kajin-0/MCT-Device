# Source ledger addendum — Round 31

## Scope

Round 31 audited P13/P13A against the P33 package-thermal evidence, recovered detailed UWA x≈0.30 HgCdTe transient-photoconductive-decay apparatus information, corrected a source-lineage error, and strengthened temporal de-embedding/injection controls.

Evidence classes:

- `RP01-DIRECT`
- `PRIMARY-THESIS / SAME-UWA-LAB`
- `SAME-UWA-CONFERENCE / IDENTIFIED-NOT-RECOVERED`
- `PRIMARY-HGCDTE-TRANSFER`
- `PRIMARY-HGCDTE-PC-PACKAGE-THERMAL`
- `OFFICIAL-INSTRUMENT-DOCUMENTATION`
- `NEGATIVE-RECOVERY`

---

## S31-01 — Smith et al. 2001 canonical RP-01

E. P. G. Smith et al., *Semiconductor Science and Technology* 16, 455–462 (2001), DOI `10.1088/0268-1242/16/6/306`.

**Class:** `RP01-DIRECT`

Direct dynamic operating context:

- spectral response/responsivity measured with 1-kHz optical chopping;
- detector performance at ~80 K and 10 V/cm for Figures 5–7;
- applied field is voltage bias between contacts.

### Negative/direct boundary

The audited RP-01 paper does **not** publish:

- a detector frequency-response curve;
- RP-01 `f_3dB`;
- RP-01 carrier lifetime;
- a transient-photoconductive-decay apparatus;
- a time-domain decay waveform.

Therefore historical RP-01 `tau` and `f_3dB` remain `OPEN`, not inferable from the 1-kHz characterization frequency.

---

## S31-02 — Rajaduray 1998 UWA honours thesis

R. Rajaduray, *Investigation of Spatial Characterisation Techniques in Semiconductors*, B.E. (Honours), University of Western Australia, 1998. Supervisor J. M. Dell. Archive DOI/copy: `10.13140/RG.2.2.29365.47848`.

**Class:** `PRIMARY-THESIS / SAME-UWA-LAB`

Laboratory-lineage evidence:

- acknowledges D. Redfern and E. P. G. Smith for experimental assistance/advice;
- UWA x≈0.30 n-HgCdTe transient/spatial-characterisation work immediately preceding RP-01.

### Direct material/apparatus anchors

- LPE n-type HgCdTe, nominal `x≈0.30`;
- ~77 K;
- vacuum;
- liquid-N2 cryogenic setup;
- Waterloo Scientific scanning laser microscope;
- `1.047 µm` optical excitation;
- pulsed operation at `1 kHz`;
- `25 ns` pulse duration;
- Keithley variable-current source;
- deliberately small bias to suppress carrier sweepout into high-recombination contacts;
- one analyzed sample state `-1.05 V`;
- AC-coupled voltage amplifier;
- HP54522A digital oscilloscope;
- PC-controlled acquisition;
- typically `128` waveform averages per coordinate;
- `500` stored voltage samples per decay;
- `20 ns` sample spacing;
- Matlab analysis.

### Direct analysis/method conclusions

- diffusion/recombination redistribution makes decay spatial/time dependent;
- a non-exponential model gave a better fit than a simple exponential for the analyzed spatial-lifetime data;
- short pulsed excitation can generate locally high excess-carrier density even when average optical power is kept low;
- thesis calculation for one analyzed state estimated equilibrium carrier count ~`4.25×10^11` over the full layer volume and generated carriers ~`8.2×10^10` from a representative transient, leading to concern that local initial excitation could approach high-level injection;
- Auger recombination can therefore influence early decay.

### Optical-profile context

The thesis estimated ~90% absorption of `1.047 µm` light within roughly `2.7 µm` of x≈0.30 HgCdTe under its model.

This makes the branch near-surface weighted and prohibits automatic equivalence to a ~4-µm RP-01 detector-response time.

### Still open

- exact laser model beyond the scanning-laser-system context;
- pulse energy/fluence at DUT;
- pulse rise/fall and jitter;
- exact spot profile for each transient;
- exact Keithley model/current setting;
- AC amplifier model/circuit/gain/bandwidth/input impedance;
- HP54522A input range/coupling/termination/trigger;
- absolute carrier-density calibration uncertainty.

### Restriction

No thesis lifetime, `-1.05 V`, pulse setting or 1.047-µm decay is an RP-01 acceptance target.

---

## S31-03 — Redfern et al. TPCD conference paper

D. A. Redfern, C. Musca, E. P. G. Smith, J. Dell, L. Faraone, “On the Transient Photoconductive Decay Technique for Lifetime Extraction in HgCdTe,” *1998 Conference on Optoelectronic and Microelectronic Materials and Devices Proceedings*, IEEE (1999), pp. 275–278.

**Class:** `SAME-UWA-CONFERENCE / IDENTIFIED-NOT-RECOVERED`

### Importance

Authors overlap directly with RP-01 and Rajaduray's thesis lineage. This is the highest-value remaining publication for closing the UWA transient method.

### Current state

Bibliographic identity is closed, but the full primary experimental text was not recovered in Round 31. Do not infer its apparatus from the thesis unless explicitly labeled `THESIS-LINEAGE-INFERENCE`.

---

## S31-04 — Pal et al. 2001 interface-trap TPCD

R. Pal et al., “Study of interface traps from transient photoconductive decay measurements in passivated HgCdTe,” *Journal of Electronic Materials* 30, 103–108 (2001), DOI `10.1007/s11664-001-0108-x`.

**Class:** `PRIMARY-HGCDTE-TRANSFER / NON-UWA`

Direct relevance:

- passivant/HgCdTe interface generation-recombination complicates transient photoconductive decay;
- delayed peaks can appear;
- transient structure attributed to electron/hole interface traps.

Reported sample-specific trap quantities are not RP-01 passivation specifications.

Use: establishes `TRAP/MULTICOMPONENT` as a physically real alternative to single-exponential bulk recombination.

---

## S31-05 — Gopal et al. 2004 anodic-oxide interface traps

V. Gopal, N. Devi, R. Pal, V. Kumar, “Study of the traps at a mercury cadmium telluride–anodic oxide interface using a transient photoconductive decay technique,” *Journal of Crystal Growth* 265, 530–536 (2004), DOI `10.1016/j.jcrysgro.2004.02.082`.

**Class:** `PRIMARY-HGCDTE-TRANSFER / NON-UWA`

### Provenance correction

Earlier P13 wording incorrectly described this as Musca/Faraone lineage. That attribution is false and was corrected in Round 31.

### Direct relevance

- non-simple transient behavior associated with HgCdTe/anodic-oxide interface traps;
- DC bias changes transient behavior;
- equivalent-circuit/physical treatment required beyond a naive one-exponential fit.

Use only as transfer physics.

---

## S31-06 — Bartoli et al. 1975 HgCdTe PC thermal recovery

F. J. Bartoli, L. Esterowitz, M. R. Kruer, R. E. Allen, “Thermal recovery processes in laser irradiated HgCdTe (PC) detectors,” *Applied Optics* 14, 2499–2507 (1975), DOI `10.1364/AO.14.002499`.

**Class:** `PRIMARY-HGCDTE-PC-PACKAGE-THERMAL`

Direct results:

- packaged HgCdTe PC thermal recovery depends strongly on detector construction;
- initial recovery on several-ms scale;
- slower recovery on hundreds-ms scale;
- two scales associated with two thermally resistive bonding layers;
- thermal signal magnitude/shape varies with irradiation power density and duration;
- optical heating can be replaced by electrical pulse heating in the related package-characterisation method.

### P13 consequence

Slow response in a packaged HgCdTe photoconductor is not automatically trapping/carrier lifetime. P33 `H_pkg,thermal` is now part of P13 de-embedding/discrimination.

---

## S31-07 — HP54522A official documentation

HP/Keysight legacy documentation for HP54522A digital oscilloscope.

**Class:** `OFFICIAL-INSTRUMENT-DOCUMENTATION`

Relevant capability facts:

- two channels;
- ~500-MHz analog bandwidth;
- up to 2 GSa/s sampling;
- 32-k acquisition memory/channel;
- sequential single-shot capability.

### Restriction

These are instrument capabilities, not Rajaduray historical acquisition settings unless the thesis directly states them. The directly closed thesis acquisition parameters are `500 points`, `20 ns spacing`, and `128` averages typical.

---

# Negative recovery record — Round 31

Targeted source recovery did not close:

- a published RP-01 detector lifetime;
- an RP-01 frequency-response curve;
- RP-01 transient apparatus;
- full Redfern et al. 1999 experimental text;
- exact Waterloo laser model/pulse-energy calibration;
- exact Rajaduray spot/fluence for each transient;
- Keithley source model/current;
- AC-coupled amplifier model/circuit/gain/bandwidth;
- HP54522A input/trigger/termination settings;
- any direct link proving the Rajaduray apparatus was used on the Figure-3/5/6/7 RP-01 detector.

`NOT RECOVERED` does not mean nonexistent.

---

# Derived/local method constructs — not historical facts

- extended transfer equation including `H_pkg,thermal`;
- local optical-reference deconvolution;
- excitation-series small-signal gate;
- `Delta n/n0` injection estimate;
- time/frequency-domain consistency gate;
- package thermal optical-versus-electrical impulse comparison;
- temporal-result classification (`SOURCE-LIMITED`, `HIGH-INJECTION`, etc.).

---

# Round-31 conclusion

Round 31 materially closes the **same-UWA temporal apparatus lineage**, not the temporal response of RP-01 itself.

The strongest historical UWA branch is now quantitatively recorded as:

`1.047 µm / 25 ns / 1 kHz -> x≈0.30 n-HgCdTe near 77 K in vacuum -> low Keithley current bias -> AC-coupled amplifier -> HP54522A -> 500×20-ns samples / 128 averages -> Matlab transient modeling`.

The project must preserve the distinction:

`UWA lifetime-method lineage != RP-01 detector lifetime`.

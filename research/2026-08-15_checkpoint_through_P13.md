# Research checkpoint — through P13

**Timestamp:** 2026-08-15 America/New_York  
**Purpose:** fast takeover checkpoint after completion of P13. Read this after `AGENTS.md` and before continuing new research.

## Current frontier

Controlled modules now exist through:

1. P01 wet mesa qualification
2. P02 anodic oxide qualification
3. P03 x≈0.30 Te-rich LPE qualification
4. P04 Hg-overpressure anneal qualification
5. P05 Hall / van der Pauw material metrology
6. P06 FTIR composition/thickness mapping
7. P07 CdZnTe substrate qualification
8. P08 RIE blocking-contact qualification
9. P09 Cr/Au metallization + TLM qualification
10. P10 device DC bias / self-heating
11. P11 absolute spectral responsivity / radiometry
12. P12 noise PSD / NEP / detectivity
13. P13 temporal response / frequency response / lifetime / bandwidth

There is still no end-to-end `REPRODUCIBLE-RELEASE` traveler. Each module distinguishes published anchors, derived values, apparatus calibration, local qualification and unresolved variables.

## P13 decisions that must survive context loss

- Never identify a measured system pole with detector lifetime until source/modulator, optical reference, bias network, preamplifier, cable and instrument transfer functions are de-embedded.
- A one-pole detector model is accepted only if amplitude and phase are jointly consistent with the same tau, residuals are non-systematic, fit-range changes do not materially move tau, and low-injection response is linear.
- Use `tau_eff` unless the physical experiment/model justifies calling it a bulk minority-carrier lifetime.
- Time-domain fits must record fit windows and exclude pulse-source/amplifier/high-injection distortion rather than forcing an exponential from t=0.
- Repeat temporal response versus electric field because sweepout/contact recombination can change apparent lifetime; check P10 self-heating simultaneously.
- P13 must determine empirically whether the historical 1-kHz P11/P12 operating point lies on the low-frequency detector plateau.

## Same-UWA transient source recovered after initial P13 draft

D. A. Redfern, C. A. Musca, E. P. G. Smith, J. M. Dell, and L. Faraone, “On the Transient Photoconductive Decay Technique for Lifetime Extraction in HgCdTe,” in *1998 Conference on Optoelectronic and Microelectronic Materials and Devices Proceedings*, IEEE, published 1999, pp. 275–278.

This source is especially important because it contains the same Smith/Musca/Dell/Faraone lineage as RP-01. Promote it into the permanent source ledger when that file is next consolidated.

A related UWA spatial-characterization thesis reports n-type x≈0.3 HgCdTe lifetime/LBIC measurements at 77 K under vacuum and explicitly keeps bias small to avoid sweeping excess carriers into high-recombination contact regions. This directly supports the P13 field/sweepout caution; audit primary thesis metadata before using numerical details as controlled setpoints.

## P13 broad historical benchmark

Kruse 1965 reported HgCdTe photoconductive response times no greater than approximately 10^-7 s at 77 K for the devices studied. Under an ideal one-pole model this corresponds to f_3dB ≳1.59 MHz.

Derived only: for tau=100 ns at 1 kHz, attenuation is approximately −1.7×10^-6 dB and phase lag approximately −0.036°. This makes it plausible that 1 kHz is far below the intrinsic pole for a fast HgCdTe PC, but it does not establish RP-01 tau.

## Immediate next branch

P14 = lithography, mask geometry and dimensional-control qualification.

Direct RP-01 anchors already known:

- two-mask simplified process architecture;
- Mask 1 defines wet-etched mesa;
- Mask 2 defines contact windows and is reused for RIE plus Cr/Au lift-off;
- Mask-2 resist thickness approximately 4–5 µm;
- prebake 80 °C for 30 min;
- chlorobenzene soak 30 min;
- then pattern/expose/develop/water rinse (exact resist/exposure/developer unresolved);
- nine metal contacts, each 300×300 µm;
- eight nominal gaps: 50, 100, 150, 200, 250, 300, 350 and 400 µm.

If those nine contacts form one sequential linear string, the nominal end-to-end patterned contact/gap length is derived as:

`9×300 µm + (50+100+...+400) µm = 4500 µm = 4.5 mm`.

Treat that as `[D]` and confirm actual mask topology before using it as a physical sample dimension.

## Lithography cautions already established

- Chlorobenzene single-layer lift-off is a known positive/diazo-resist profile-modification technique that creates an overhang after development.
- Hatzakis–Canavello–Shaw 1980 is the foundational single-step optical lift-off source.
- Collins–Halsted 1982 shows overhang/linewidth/resist height depend jointly on exposure, chlorobenzene soak, development and bake conditions; these are therefore coupled process variables.
- This literature does **not** identify the resist used in RP-01. Do not infer AZ4000/AZ4110 or any other product without direct lineage evidence.
- Do not assume Mask 1 and Mask 2 use identical resist coating/exposure/development conditions merely because both are photolithographic operations.

## Geometry issue still open

The RP-01 paper does not clearly state which of the 50–400 µm gaps was used for each “typical device” performance curve. Because active area enters D* and gap enters electric field, this must be closed or explicitly recorded for reconstructed measurements.

There is a tempting numerical inference that a 300×50 µm active area, a responsivity of order 4×10^5 V/W and a 24.5 nV/√Hz noise level would yield D* near 2×10^11 cm Hz^1/2/W. Do **not** promote this to a historical geometry fact until exact responsivity, noise-frequency convention and plotted device identity are all verified.

## Recovery discipline

After every material scientific advance:

1. update/create the relevant controlled procedure;
2. write a dated research note for source reasoning and rejected branches;
3. update closure/source continuity when feasible;
4. never leave a process-critical inference only in chat.

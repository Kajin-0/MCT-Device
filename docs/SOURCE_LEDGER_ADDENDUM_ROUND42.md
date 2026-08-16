# Source ledger addendum — Round 42 subsystem commissioning / acceptance architecture

**Date:** 2026-08-16 America/New_York  
**Repository:** `Kajin-0/MCT-Device`

## Scope

Round 42 did not reopen historical literature searches. It converted the already controlled evidence and Round-41 capability envelope into subsystem acceptance-test methods.

New controlled artifacts:

- `procedures/P36_LAB_SUBSYSTEM_COMMISSIONING_ACCEPTANCE.md`
- `procedures/P36A_SUPPORTING_METROLOGY_LITHOGRAPHY_WET_CHEMISTRY_ACCEPTANCE.md`
- `travelers/P16D_SUBSYSTEM_ACCEPTANCE_REGISTER.md`
- `travelers/P16D1_SUPPORTING_METROLOGY_MICROFAB_ACCEPTANCE_REGISTER.md`

No new external source is promoted by this round. All numerical process centers and measurement requirements below inherit their evidence class from the cited controlled repository modules.

---

## S42-01 — Round-41 capability specification

Controlled source:

- `docs/FIRST_QUALIFICATION_BUILD_MINIMUM_LAB_CAPABILITY_SPEC.md`
- `travelers/P16C_MINIMUM_LAB_CAPABILITY_IMPLEMENTATION_REGISTER.md`

**Class:** `CONTROLLED-CAPABILITY-INTEGRATION`.

Round-42 use:

- converted capability statements into IQ/OQ/surrogate-PQ/HgCdTe-residual acceptance layers;
- retained `HARD-MINIMUM` versus `FIRST-BUILD-ENGINEERING-ENVELOPE` distinctions;
- did not promote infrastructure capability into process readiness.

New rule:

`installed != calibrated != surrogate-commissioned != HgCdTe-qualified`.

---

## S42-02 — LPE acceptance basis

Controlled sources:

- P03/P03C/P03E;
- P30/P30A;
- P16B/P16C.

Inherited anchors:

- Honeywell-family covered horizontal slider;
- `xL=.082`, `yL=.810`, `TL=507 °C`;
- above-local-liquidus equilibration;
- below-liquidus contact;
- Round-41 engineering coverage approximately 495–520 °C;
- N2 purge -> H2 process family;
- literature-supported candidate supercooling scale beginning around ~2 °C in represented branches.

Round-42 derivation:

To distinguish a planned minimum process difference `DeltaX_decision`, measurement uncertainty must be small relative to that difference. P36 uses:

`U_X < DeltaX_decision/2`

as a logical minimum and

`U_X <= DeltaX_decision/4`

as a preferred engineering target where practical.

For a 2-°C candidate supercooling discrimination, this gives a design check of `U_DeltaT<1 °C`, preferably near `<=0.5 °C` if that 2-°C distinction is actually used.

**Class:** `DERIVED-MEASUREMENT-DISCRIMINATION`, not historical process tolerance.

No absolute `M_charge`, gas flow, hold time or contact time is introduced.

---

## S42-03 — Hg anneal acceptance basis

Controlled sources:

- P31/P04/P23;
- P16B/P16C.

Inherited first screen:

- approximately 250 °C / 1 h / Hg-saturated-isothermal-like;
- approximately 250–300 °C low-temperature mapping region;
- independent `T_s(t)` and `T_Hg(t)` state required.

Round-42 use:

- dual-temperature dummy-load thermal map;
- one-hour timing/stability commissioning;
- enclosure integrity commissioning with non-Hg surrogate where permitted;
- explicit Hg/HgCdTe residual gate.

No universal temperature stability or leak-rate number is invented.

---

## S42-04 — FTIR acceptance basis

Controlled sources:

- P06/P06A;
- P16C C04.

Inherited capability:

- approximately 500–5000 cm^-1;
- <=4 cm^-1 qualification resolution unless sensitivity validates coarser;
- minimum 9-point map;
- preferred 5×5+ development map;
- independent physical thickness reference around expected ~5–15 µm.

Round-42 use:

- spectral range/resolution OQ;
- baseline/repeatability PQ;
- stage-registration acceptance;
- independent thickness-reference acceptance;
- HgCdTe optical-model residual qualification.

No new cutoff convention is created.

---

## S42-05 — Hall/VdP acceptance basis

Controlled source:

- P05;
- P16C C05.

Inherited initial field grid:

`0, ±0.01, ±0.025, ±0.05, ±0.10, ±0.20, ±0.50 T`.

Inherited hard minimum:

- >=±0.50 T;
- ~±2 T remains preferred extended capability.

Round-42 use:

- field calibration at sample position;
- polarity/remanence/uniformity verification;
- current/voltage/reversal chain PQ;
- 80-K/300-K temperature OQ;
- Hall-reference surrogate PQ.

Actual HgCdTe contact/multicarrier/p-n transition response remains residual.

---

## S42-06 — RIE acceptance basis

Controlled sources:

- P08/P24/P34;
- P16B/P16C.

Inherited direct/candidate controller state:

- total 64 sccm;
- candidate CH4:H2=1:5 -> 10.6667/53.3333 sccm;
- 100 mTorr;
- 50 W;
- 60 s.

Inherited reactor-equivalence rule:

- watts are not ion energy;
- self-bias/sheath proxy is first-class;
- oxide clear and semiconductor exposure must be separated.

Round-42 use:

- gas-specific MFC OQ at/around candidate flows;
- process-pressure OQ;
- RF/reflected-power/self-bias OQ;
- sample-thermal dummy PQ;
- chamber-state PQ;
- actual P25 oxide/HgCdTe residual `t_clear`/conversion qualification.

No arbitrary base pressure or conversion depth is introduced.

---

## S42-07 — Cr/Au deposition acceptance basis

Controlled sources:

- P09/P26/P26A;
- P16B/P16C.

Inherited direct stack:

- Cr 30 nm;
- Au 270 nm.

Inherited local requirements:

- separate Cr/Au QCM/witness calibration unless equivalence is demonstrated;
- actual pressure/rate/source geometry/sample thermal state logged;
- no undocumented clean between RIE and Cr;
- no arbitrary base-pressure requirement.

Round-42 use:

- independent Cr and Au tooling-factor acceptance;
- witness thickness correlation;
- sequential Cr->Au deposition PQ;
- sample thermal PQ;
- HgCdTe TLM/contact residual gate.

---

## S42-08 — integrated detector-station acceptance basis

Controlled sources:

- P10/P10A;
- P11/P11A;
- P12/P12A/P12B/P12C;
- P13/P13A;
- P33;
- P16B/P16C.

Inherited states:

- detector around 77–80 K;
- canonical 10 V/cm;
- historical sweep toward ~50 V/cm;
- 4-µm absolute performance point;
- cutoff region ~4.4 µm;
- 1-kHz spectral modulation;
- historical noise region containing ~3-kHz knee and ~24.5-nV/sqrtHz high-frequency g-r level;
- temporal qualification through at least 1 MHz plus extension to >=5–10× observed f3dB where practical.

Round-42 derived design checks retained:

If electronics PSD receives fraction `beta` of the 24.5-nV/sqrtHz detector-plateau PSD:

`e_elec <= 24.5 sqrt(beta) nV/sqrtHz`.

For `beta=.10`, `e_elec<=7.75 nV/sqrtHz`.

If the 25-ns same-UWA pulse branch is implemented:

`BW~0.35/25 ns~14 MHz`.

Both remain engineering design checks, not historical RP-01 specifications.

New acceptance architecture:

- dummy cryogenic thermal/vacuum PQ;
- DC/load network PQ;
- calibrated radiometry/wavelength/view-factor PQ;
- modulation waveform/timebase OQ;
- electronics-floor PSD PQ;
- Johnson-noise absolute validation;
- temporal transfer-function PQ;
- package thermal-kernel PQ;
- matched-state metadata PQ;
- actual HgCdTe P10–P13 residual gate.

---

## S42-09 — source weighing / dimensional metrology basis

Controlled sources:

- `calculations/LPE_CHARGE_COMPOSITION_SENSITIVITY.md`;
- P03C/P30A;
- P14/P06/P25/P26/P35.

Authoritative atomic-weight convention remains:

- Hg 200.59;
- Cd 112.414;
- Te 127.60 g/mol.

Canonical mass fractions remain:

- Hg 0.2497382358;
- Cd 0.01250164993;
- Te 0.7377601143.

Round-42 use:

- balance acceptance at actual element mass scales, especially Cd;
- uncertainty propagated into `xL/yL` rather than assigning an arbitrary balance tolerance;
- dimensional metrology acceptance across contact gaps, resist/HgCdTe/oxide/metal and singulation scales.

---

## S42-10 — lithography acceptance basis

Controlled sources:

- P14/P14A/P27/P32;
- P16B/P16C.

Inherited Mask-2 direct functional state:

- measured 4–5 µm resist;
- 80 °C / 30 min bake;
- chlorobenzene 30 min;
- survives RIE;
- supports ~300-nm Cr/Au lift-off.

Round-42 use:

- spin-thickness mapping;
- substrate thermal calibration during bake;
- controlled chlorobenzene timing;
- exposure-dose calibration;
- development/profile PQ;
- representative plasma/metal lift-off surrogate challenge.

No resist/developer identity is invented.

---

## S42-11 — wet mesa acceptance basis

Controlled sources:

- P28/P28A/P32;
- P16B/P16C.

Inherited transfer center:

- `2% Br2`;
- `3:1 EG:HBr`;
- ~21 °C;
- ~2.78 µm/min represented vertical rate;
- `A≈0.63`;
- best roughness ~2 nm.

Critical ambiguity retained:

- Br2 percent basis;
- EG:HBr ratio basis;
- HBr assay;
- complete mixing/rinse/handoff implementation.

Round-42 acceptance first requires local mathematical/procedural definition before execution. Surrogates may qualify handling/resist compatibility but not HgCdTe rate/anisotropy.

---

## S42-12 — anodization acceptance basis

Controlled sources:

- P25/P25A;
- P16B/P16C.

Inherited TI transfer center:

- 0.1 mol KOH per stated 1 L solvent;
- stated 90% EG / 10% DI water;
- carbon cathode branch;
- ~0.3 mA/cm²;
- ~15 V;
- ~2 min;
- ~800 Å / 80 nm.

Derived pure-KOH mass remains `5.61056 g` before assay correction.

Round-42 use:

- explicit local solvent-ratio basis gate;
- dimensioned cell and measured `A_exposed`;
- calibrated `I=J A_exposed` current source;
- V(t) logger/timebase PQ;
- actual HgCdTe oxide/interface/RIE-clear residual gate.

---

## S42-13 — singulation/package acceptance basis

Controlled sources:

- P35;
- P33/P15/P17A/P18A;
- P16C C10/C11.

Round-42 use:

- mechanical surrogate singulation PQ;
- clean/release witness compatibility;
- dummy package thermal/mechanical/interconnect/optical/vacuum PQ;
- actual completed-stack/HgCdTe residual qualification.

The low-force wire-saw and compliant silicone-family choices remain candidate first screens, not released universal settings/products.

---

## S42-14 — evidence discipline conclusion

Round 42 adds **acceptance methodology**, not physical acceptance results.

All current acceptance rows remain unexecuted because no actual laboratory/tool identity has been instantiated in the repository.

Therefore:

- `P16D-SURROGATE-COMMISSIONING-COMPLETE = NO / NOT PHYSICALLY INSTANTIATED`;
- `P16C-INFRASTRUCTURE-READY = NO / NOT PHYSICALLY INSTANTIATED`;
- `TRACEABLE-FIRST-BUILD-READY = NO`;
- `HISTORICAL-RP01-REPRODUCED = NO`;
- `REPRODUCIBLE-RELEASE = NO`.

The scientific gain is that a future laboratory now has a controlled method for determining when each subsystem is trustworthy enough to begin material-specific qualification.
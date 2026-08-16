# Source ledger addendum — round 17 empirical blocking-contact recovery

**Date:** 2026-08-16 America/New_York

**Round objective:** shift the blocking-contact branch from theory-heavy placeholder work toward a practical, experimentally sourced fabrication/validation record.

The controlling empirical procedure is:

`procedures/P24_BLOCKING_CONTACT_EMPIRICAL_PROCESS_WINDOW.md`.

---

## S-R17-01 — Smith et al. 2001 canonical simplified n+/n blocking-contact detector

**Class:** `DIRECT-RP01 / Primary-A`  
**Citation:** E. P. G. Smith, K. J. Winchester, C. A. Musca, J. M. Dell, L. Faraone, “A simplified fabrication process for HgCdTe photoconductive detectors using CH4/H2 reactive-ion-etching-induced blocking contacts,” *Semiconductor Science and Technology* 16, 455–462 (2001).  
**DOI:** `10.1088/0268-1242/16/6/306`

### Direct fabrication anchors

- LPE n-HgCdTe on insulating CdZnTe;
- nominal `x≈0.30`;
- reported starting `n=9.8×10^14 cm^-3`;
- reported starting `mu=4.0×10^4 cm^2/V/s`;
- thickness `9.5 µm`;
- anodic oxide approximately `800 Å = 80 nm`;
- contact-window RIE in a Plasma Technology parallel-plate reactor;
- printed gas notation `CH4/5H2`;
- total flow `64 sccm`;
- pressure `100 mTorr`;
- RF power `50 W`;
- plasma time `60 s`.

### Direct converted-layer/metrology anchors

- patterned LBIC test square `300×300 µm`;
- Waterloo Scientific scanning laser microscope;
- Nd:YLF `1.047 µm` continuous-wave laser;
- approximately `400 mW/cm^2` illumination;
- LBIC at `80 K`;
- variable-field van der Pauw/Hall/resistivity at both `80 K` and `300 K`;
- magnetic field extended to `2 T`;
- converted-region average `n≈2.0×10^15 cm^-3` over the converted thickness;
- converted mobility `mu≈3.3×10^4 cm^2/V/s`.

The paper cites earlier similar-condition work showing n+ conversion to approximately `8 µm`; this is not reclassified as a directly measured depth of the exact canonical device run.

### Direct lithography/contact anchors

- resist approximately `4–5 µm`;
- `80 °C / 30 min` prebake;
- chlorobenzene `30 min`;
- Cr `300 Å = 30 nm`;
- Au `2700 Å = 270 nm`;
- nine contacts `300×300 µm`;
- gaps from `50–400 µm` in `50-µm` steps;
- reported `rho_c≈9×10^-4 ohm cm^2` at `80 K`.

### Direct detector-performance anchors

Responsivity/spectral system:

- Optronics Laboratories Spectral Response Measurement System;
- `80 K`;
- stated `60-degree` FOV;
- `1 kHz` chopping;
- field-response comparison near `4 µm`.

Noise:

- `80 K`;
- `10 V/cm`;
- low-noise preamplifier;
- HP 35665A analyzer;
- 1/f-to-g-r knee approximately `3 kHz`;
- high-frequency g-r level about `24.5 nV/sqrt(Hz)`.

Spectral/detectivity:

- cutoff approximately `4.4 µm`;
- BLIP `D*≈2.0×10^11 cm Hz^1/2/W` at `4 µm`;
- quoted QE approximately `70%`.

### Critical author conclusion

The reported blocking contact was not fully optimized. The authors specifically identify improved control/tuning of n+ carrier density and junction depth as the route to further improvement.

### Round-17 use

This paper is now treated as an experimentally successful **historical center condition**, not an optimum process window.

---

## S-R17-02 — Siliquini et al. 1997 LBIC depth vs physical etch

**Class:** `TRANSFER-P-TYPE-X030 / Primary-A`  
**Citation:** J. F. Siliquini, J. M. Dell, C. A. Musca, L. Faraone, “Scanning Laser Microscopy of Reactive Ion Etching Induced n-Type Conversion in Vacancy-Doped p-Type HgCdTe,” *Applied Physics Letters* 70, 3443–3445 (1997).  
**DOI:** `10.1063/1.119159`

### Direct conditions/results

- vacancy-doped p-type `Hg0.69Cd0.31Te`;
- `410 mTorr`;
- `CH4/H2`;
- `0.4 W/cm^2`;
- physical etch depth approximately `0.2 µm`;
- electrical n-type conversion approximately `1.5 µm` deep.

### Round-17 use

Direct empirical proof that physical etch depth can be much smaller than electrical conversion depth.

**Restriction:** p-type starting material and different pressure/process; do not use 1.5 µm as RP-01 target.

---

## S-R17-03 — Siliquini et al. 1998 LBIC effective doping-density extraction

**Class:** `TRANSFER-P-TYPE-X030 / Primary-A`  
**Citation:** J. F. Siliquini et al., “Estimation of doping density in HgCdTe p-n junctions using scanning laser microscopy,” *Applied Physics Letters* 72 (1998).  
**DOI:** `10.1063/1.120642`

### UWA institutional abstract values

- extrinsic As-doped p-type `Hg0.71Cd0.29Te`;
- prior Hg anneal to remove Hg vacancies;
- `340 mTorr`;
- `CH4/H2`;
- `0.4 W/cm^2`;
- LBIC over `80–300 K`;
- SEMICAD DEVICE fit;
- effective n-type converted-region doping density was the fitting parameter.

### Source conflict

Some public secondary/search snippets report a pressure near `390 mTorr` for this work. The UWA institutional primary record states **340 mTorr**. Do not average the values. Use 340 mTorr when citing the institutional record and preserve the conflict until the journal PDF is independently checked.

---

## S-R17-04 — Musca et al. 1998 n-type MWIR LBIC imaging

**Class:** `SAME-LINEAGE-N-TYPE / Primary-A`  
**Citation:** C. A. Musca et al., “Laser Beam Induced Current Imaging of Reactive Ion Etching Induced n-Type Doping in HgCdTe,” *Journal of Electronic Materials* 27, 661–667 (1998).  
**DOI:** `10.1007/s11664-998-0032-4`

### Direct role

The paper applies LBIC to RIE-processed n-type MWIR HgCdTe and demonstrates sensitivity to:

- presence of n+ conversion;
- junction/conversion depth;
- lateral extent;
- junction grading;
- temperature.

This is the strongest same-lineage method basis for treating LBIC as a required conversion-depth/lateral-spread measurement in P24.

The exact process values associated with the approximately 8-µm depth cited later by RP-01 remain unresolved in the presently recovered public record.

---

## S-R17-05 — Musca et al. 1999 quantitative junction-depth LBIC method

**Class:** `SAME-LINEAGE / Primary-A`  
**Citation:** C. A. Musca, D. A. Redfern, E. P. G. Smith, J. M. Dell, L. Faraone, J. Bajaj, “Junction Depth Measurement in HgCdTe Using Laser Beam Induced Current (LBIC),” *Journal of Electronic Materials* 28(6), 603–610 (1999).

### Round-17 role

Quantitative-method lineage for extracting junction/conversion depth from LBIC. P24 therefore requires that a local conversion depth be independently measured instead of inferred from plasma duration or physical recession.

---

## S-R17-06 — Smith et al. 1998 Hg anneal erases RIE conversion

**Class:** `TRANSFER-P-TYPE-X030 / Primary-A`  
**Citation:** E. P. G. Smith et al., Hg annealing of RIE-induced p-to-n conversion in extrinsically doped p-type HgCdTe, *Applied Physics Letters* 83, 5555–5557 (1998).  
**DOI:** `10.1063/1.367389`

### Direct conditions/results

- extrinsically doped p-type HgCdTe `x=0.31`;
- RIE `400 mTorr`, `CH4/H2`, `90 W`;
- RIE-induced n conversion verified by LBIC;
- sealed-tube Hg anneal `200 °C / 17 h`;
- after anneal no converted n-region was visible by LBIC;
- Hall returned to a uniform p-type state comparable with initial material;
- reported restored p-state scale `N_A-N_D≈2×10^16 cm^-3`, `mu≈350 cm^2/V/s`.

### Round-17 implication

The RIE-induced electrical state can be altered/erased by subsequent Hg-rich thermal processing in at least one x≈.31 branch.

**Restriction:** not an RP-01 treatment. Used only to impose post-RIE thermal-history control and to prohibit unqualified later anneals.

---

## S-R17-07 — White et al. 2001 H2/CH4 plasma conversion mechanisms

**Class:** `MECHANISM-SAME-GROUP / Primary-A`  
**Citation:** J. K. White et al., “p-to-n Type Conversion Mechanisms for HgCdTe Exposed H2/CH4 Plasmas,” *Journal of Electronic Materials* 30(6), 762–767 (2001).

### Role

Mechanistic support that H2/CH4 plasma conversion is a coupled defect/hydrogen process rather than a simple shallow chemical dopant layer. P24 therefore requires stability/thermal-history measurements and avoids assuming that one immediate Hall result defines a permanent material state.

No unverified mechanistic number from this source is promoted to a process limit.

---

## S-R17-08 — Park et al. 2007 process-parameter sensitivity

**Class:** `TRANSFER-P-TYPE-X030 / Primary-A`  
**Citation:** B. A. Park, C. A. Musca, J. Antoszewski, J. M. Dell, L. Faraone, “Effect of High-Density Plasma Process Parameters on Carrier Transport Properties in p-to-n Type Converted Hg0.7Cd0.3Te Layer,” *Journal of Electronic Materials* 36(8), 913–918 (2007).  
**DOI:** `10.1007/s11664-007-0132-6`

### Direct abstract-level finding

Using quantitative mobility-spectrum analysis of variable-field Hall/resistivity data in an ICPRIE process, the converted-layer transport properties and depth were:

- most sensitive to **process pressure and temperature**;
- also significantly influenced by RIE power and ICP power.

### Round-17 use

This experimentally supports prioritizing:

1. actual sample temperature;
2. pressure;
3. ion-energy/power state;

when transferring/optimizing the RP-01 parallel-plate process.

**Restriction:** different reactor and p-type starting material; no ICP setpoint becomes an RP-01 setpoint.

---

## S-R17-09 — Smith, Musca, Faraone 2000 2-D MWIR model

**Class:** `MODEL-ONLY / same team`  
**Citation:** E. P. G. Smith, C. A. Musca, L. Faraone, “Two-dimensional modelling of HgCdTe photoconductive detectors,” *Infrared Physics & Technology* 41, 175–186 (2000).  
**DOI:** `10.1016/S1350-4495(99)00054-7`

### Model values

A practical device fit used an n+ region of approximately:

- `1×10^16 cm^-3`;
- `3 µm` depth.

### Restriction

These are model inputs, not experimentally measured optimum RIE output values. They may be used for simulation bracketing only.

---

## S-R17-10 — Musca et al. 1997 heterojunction blocking contact

**Class:** `TRANSFER-OTHER-X/ARCH / Primary-A`  
**Citation:** C. A. Musca et al., heterojunction blocking-contact HgCdTe detector paper, *IEEE Transactions on Electron Devices* (1997).  
**DOI:** `10.1109/16.557711`

### Useful empirical/device scale

The work reports/interprets effective contact recombination velocities approximately:

- heterojunction blocking contact `~250 cm/s`;
- n+/n comparison `>10^4 cm/s`.

Heterojunction detector responsivity at `10 V/cm` was nearly twice that of the compared two-layer/nonblocking devices.

### Round-17 use

Provides a practical scale demonstrating why low majority-carrier `rho_c` is not equivalent to low minority-carrier contact loss.

**Restriction:** LWIR/heterojunction architecture; not an RP-01 `S_c` target.

---

## S-R17-11 — Siliquini et al. 1994 overlap-geometry LWIR photoconductors

**Class:** `TRANSFER-OTHER-X/ARCH / Primary-A`  
**Citation:** J. F. Siliquini et al., “Performance of optimized Hg1−xCdxTe long wavelength infrared photoconductors,” *Infrared Physics & Technology* 35(5), 661–671 (1994).  
**DOI:** `10.1016/1350-4495(94)90059-0`

### Direct role

n-type LPE HgCdTe around `x=0.23`; combined overlap geometry + blocking contact improved responsivity, low-frequency noise performance and detectivity relative to simpler blocking-contact structures.

### Round-17 implication

Geometry must be frozen in matched RIE-process comparisons; detector improvement cannot be attributed to contact conversion alone if overlap/contact geometry also changes.

---

## S-R17-12 — other-composition plasma-state room-temperature relaxation

**Class:** `TRANSFER-OTHER-X / Primary literature abstract`  
**Citation:** Belas/Grill/Franc/Sitter lineage, “Dynamics of native point defects in H2 and Ar plasma-etched narrow gap (HgCd)Te,” *Journal of Crystal Growth* (2001).

### Direct reported scale

For RIE-created n-HgCdTe around `x=0.21`:

- `sigma(77 K)` decreased to less than half of the initial value after roughly `2×10^5 s` room-temperature storage;
- storage at `323 K` accelerated relaxation by about `5×`.

### Restriction

Different x and plasma/material branch. Do not set RP-01 shelf life from these values.

### Round-17 implication

Require a local elapsed-time/storage-temperature stability study after RIE.

---

# Round-17 conclusions

1. The canonical RP-01 blocking-contact process is already more empirically specified than the prior theory-heavy branch implied.
2. The direct historical center is `100 mTorr / 64 sccm / 50 W / 60 s`, with multiple measured electrical/device outputs.
3. The canonical authors explicitly state that n+ depth/density still required optimization.
4. LBIC is the strongest same-lineage practical method for vertical/lateral conversion metrology.
5. `d_etch != d_conv` is experimentally demonstrated near x=.31.
6. Pressure and sample temperature receive high local DOE priority from later x=.30 experiments.
7. RIE conversion can be thermally reversed or relax in other HgCdTe branches, so post-RIE elapsed time/storage/thermal exposure must be logged and locally qualified.
8. `rho_c != S_c` remains experimentally consequential; detector-level responsivity/noise/bandwidth is required for blocking-contact release.

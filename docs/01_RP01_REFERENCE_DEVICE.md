# RP-01 — MWIR n-type HgCdTe photoconductor reference process

**Status:** downstream reference process selected; end-to-end closure incomplete.

**Primary anchor:** E. P. G. Smith, K. J. Winchester, C. A. Musca, J. M. Dell, and L. Faraone, *Semiconductor Science and Technology* **16**, 455–462 (2001), DOI: `10.1088/0268-1242/16/6/306`.

## 1. Why this device is RP-01

The first controlled reference process should be based on a detector that was actually fabricated and characterized. Smith et al. provide unusually dense process information for a photoconductive MCT device: starting material properties, a two-mask process concept, plasma conditions, passivation thickness, lift-off preparation, metallization, contact characterization, and detector performance.

The process is therefore a useful anchor even though it does not completely disclose all upstream growth, mesa, passivation-growth, packaging, and measurement-system details.

## 2. Architecture

Published architecture:

- n-type HgCdTe photoconductor `[P]`;
- HgCdTe epilayer on insulating CdZnTe substrate `[P]`;
- individual detector elements isolated by mesa delineation `[P]`;
- passivated semiconductor surface `[P]`;
- n+/n blocking-contact regions formed by CH4/H2 RIE beneath metal contacts `[P]`;
- Cr/Au planar metallization `[P]`.

The paper states that conventional photoconductor active areas are typically 25–100 µm in length and width with 10–15 µm absorbing-layer thickness, but that generic statement must **not** be mistaken for the exact geometry of the representative measured RP-01 device.

## 3. Incoming material specification

| Parameter | RP-01 value | Provenance | Status |
|---|---:|---|---|
| Growth method | LPE | [P] | fixed |
| Substrate | insulating CdZnTe | [P] | composition/orientation unknown |
| HgCdTe composition | x ≈ 0.30 | [P] | approximate |
| Conductivity | n-type | [P] | fixed |
| Electron concentration | 9.8×10^14 cm^-3 | [P] | fixed reference value |
| Electron mobility | 4.0×10^4 cm^2 V^-1 s^-1 | [P] | fixed reference value |
| Device-layer thickness | 9.5 µm | [P] | fixed reference value |

### 3.1 Derived resistivity

Using

`rho = 1/(q n mu)`

with q = 1.602176634×10^-19 C, n = 9.8×10^14 cm^-3, and µ = 4.0×10^4 cm^2 V^-1 s^-1 gives

`rho ≈ 0.159 ohm cm` `[D]`.

This is a consistency calculation, not a substitute for measured resistivity.

### 3.2 Composition/cutoff caution

A standard Hansen-type HgCdTe band-gap fit gives a composition-dependent intrinsic edge, but the RP-01 device's **measured** spectral cutoff was 4.4 µm at 80 K. The measured cutoff takes precedence over a naive composition-to-bandgap estimate because x is reported only approximately and experimental cutoff convention, doping, temperature, and spectral-response shape matter.

## 4. Process flow reported by Smith et al.

1. Start with n-type HgCdTe on insulating substrate.
2. Mask 1: wet-chemical mesa delineation for element isolation.
3. Form passivation.
4. Mask 2: pattern contact openings.
5. CH4/H2 RIE removes anodic oxide in the opening and converts exposed n-HgCdTe to n+.
6. Without requiring a third alignment mask, retain the resist for self-aligned metal deposition.
7. Deposit Cr/Au.
8. Lift off.
9. Characterize contact and detector performance.

The scientific advantage of the process is that one RIE operation performs two functions: passivation opening and formation of an n+/n blocking-contact region.

## 5. Passivation state

Experimental devices are stated to have:

- anodic oxide thickness: **800 Å = 80 nm** `[P]`.

Do not add a ZnS overlayer to RP-01 unless a source specifically establishes that the measured devices used it. The paper discusses anodic oxide + ZnS as a common photoconductor passivation technology, but its experimental device statement specifically identifies 800 Å anodic oxide.

### Missing passivation parameters

- electrolyte composition `[GAP]`;
- anodization current/voltage mode `[GAP]`;
- current density `[GAP]`;
- time `[GAP]`;
- temperature `[GAP]`;
- oxide-growth calibration `[GAP]`;
- rinse/dry sequence `[GAP]`.

These must be closed from the same process lineage or a separately qualified module before RP-01 can be called reproducible.

## 6. Contact-opening / n+ conversion RIE

**Reactor:** Plasma Technology parallel-plate reactor `[P]`.

Published process conditions:

| Variable | Value | Provenance |
|---|---:|---|
| Gas chemistry | CH4/5H2 | [P] |
| Total gas flow | 64 sccm | [P] |
| Process pressure | 100 mTorr | [P] |
| RF power | 50 W | [P] |
| Process time | 1 min | [P] |

### Required apparatus-calibration fields not supplied by the paper

- exact methane:hydrogen individual MFC flows corresponding to the mixture notation `[C/Q]`;
- gas purities `[Q]`;
- chamber base pressure `[Q]`;
- electrode diameter/spacing `[Q]`;
- RF frequency and power-delivery calibration `[Q]`;
- self-bias/DC bias `[Q]`;
- wafer chuck/electrode temperature `[Q]`;
- sample mounting and thermal contact `[Q]`;
- chamber seasoning/clean state `[Q]`;
- passivation-removal etch rate `[Q]`.

The nominal recipe is therefore **not portable between RIE systems without qualification**.

## 7. RIE-induced electrical state

Smith et al. measured Hall/resistivity on a separate processed sample at 80 K and 300 K using a Van der Pauw structure and magnetic field up to 2 T.

Reported RIE-converted properties:

- n+ concentration: **2.0×10^15 cm^-3** `[P]`;
- mobility: **3.3×10^4 cm^2 V^-1 s^-1** `[P]`.

Prior related work cited by the paper reported conversion extending approximately **8 µm** under similar RIE conditions. This value is a useful research constraint but is **not a directly measured RP-01 conversion-depth result** and should be tagged `[T]` until its original source is audited.

### Qualification gate proposed for a reproduction

Before device fabrication, a sacrificial test coupon processed with the intended RIE tool should demonstrate:

1. complete opening of the passivation in patterned windows;
2. induced n+/n electrical contrast by Hall/LBIC or equivalent;
3. measured converted carrier density within a predeclared acceptance band around the target;
4. no unacceptable plasma damage or surface leakage;
5. repeatable contact resistivity after metallization.

The numerical acceptance bands remain `[Q]` until process capability data exist.

## 8. Resist/lift-off preparation

Published successful lift-off preparation:

- photoresist thickness: **approximately 4–5 µm** `[P]`;
- prebake: **80 °C for 30 min** `[P]`;
- chlorobenzene soak: **30 min** `[P]`;
- then pattern, develop, and rinse in water `[P]`.

Missing:

- resist product `[GAP]`;
- spin program `[GAP]`;
- exposure wavelength/dose/contact mode `[GAP]`;
- developer identity/concentration `[GAP]`;
- develop time `[GAP]`;
- post-develop delay before RIE `[GAP]`.

These gaps are process-critical because resist profile determines successful self-aligned metal lift-off.

## 9. Metallization

Published stack:

- Cr: **300 Å = 30 nm** `[P]`;
- Au: **2700 Å = 270 nm** `[P]`.

Missing:

- deposition method `[GAP]`;
- source purity `[GAP]`;
- base pressure `[GAP]`;
- deposition rate `[GAP]`;
- substrate temperature `[GAP]`;
- vacuum break between RIE and metal deposition `[GAP]`;
- maximum surface exposure time `[GAP]`;
- lift-off solvent/time/agitation `[GAP]`.

The paper explicitly notes the advantage of linking RIE to metal deposition through a load-lock, but the exact experimental vacuum-transfer configuration must be established before treating vacuum continuity as a hard RP-01 requirement.

## 10. TLM control structure

Published contact-control structure:

- nine contacts `[P]`;
- each contact: **300 µm × 300 µm** `[P]`;
- first contact spacing: **50 µm** `[P]`;
- spacing increases by **50 µm increments** `[P]`.

Measured at 80 K:

- specific contact resistivity: **9×10^-4 Ω cm^2** `[P]`.

This becomes a natural process-control metric for contact-module qualification.

## 11. Optical/electrical characterization conditions

### Responsivity

Reported system/conditions:

- Optronics Laboratories Spectral Response Measurement System `[P]`;
- detector temperature: **80 K** `[P]`;
- field of view: **60°** `[P]`;
- chopping frequency: **1 kHz** `[P]`;
- representative responsivity-vs-field measurement wavelength: **4 µm** `[P]`.

The response begins to exhibit sweepout at elevated field because the RIE-created blocking contact was not fully optimized.

### Noise

Reported conditions:

- detector temperature: **80 K** `[P]`;
- applied electric field: **10 V cm^-1** `[P]`;
- low-noise preamplifier `[P]`;
- HP35665A spectrum analyzer `[P]`.

Reported representative results:

- 1/f knee: **~3 kHz** `[P]`;
- generation-recombination noise level: **~24.5 nV Hz^-1/2** `[P]`.

Missing measurement details include preamplifier model/gain/input noise, analyzer RBW/ENBW, averaging, window, load/bias circuit, grounding architecture, and electronics-floor subtraction methodology.

### Spectral performance

At 80 K, 10 V cm^-1, 60° FOV, 1 kHz chopping:

- measured cutoff wavelength: **4.4 µm** `[P]`;
- BLIP D*: **2.0×10^11 cm Hz^1/2 W^-1 at 4 µm** `[P]`;
- background photon flux: **1.0×10^15 cm^-2 s^-1** for 300 K background, 60° FOV `[P]`;
- quantum efficiency quoted: **70%** `[P]`.

## 12. RP-01 hard gaps before process release

The following prevent RP-01 from being an executable recipe today:

1. exact starting-wafer specification;
2. exact LPE/anneal history;
3. complete Mask-1 lithography;
4. mesa wet-etch chemistry/rate/depth;
5. anodic-oxide formation recipe;
6. complete Mask-2 exposure/development recipe;
7. RIE apparatus-transfer calibration;
8. metal deposition environment/rates;
9. exact measured detector dimensions;
10. packaging/wire-bond details;
11. complete electrical bias/load circuit;
12. traceable optical-power calibration;
13. full noise-analyzer settings and ENBW definition.

Until these are closed, RP-01 should be described as a **reference process skeleton with several experimentally demonstrated modules**, not a complete reproduction protocol.

## 13. Immediate next step

Search the UWA/Faraone process lineage and the references cited by Smith et al. for the missing mesa-etch, anodic-oxide, plasma-conversion-depth, and contact details. In parallel, audit Te-rich LPE primary literature for an x≈0.30 CdZnTe-compatible growth process with enough quantitative detail to attach upstream without changing the physical identity of RP-01.

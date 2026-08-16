# P24 — blocking-contact empirical process window / validation campaign

**Status:** CONTROLLED EMPIRICAL QUALIFICATION METHOD / PRE-RELEASE  
**Date:** 2026-08-16 America/New_York

## 1. Purpose

Convert the existing P08 blocking-contact physics and transfer architecture into a **literature-grounded, practical fabrication/measurement campaign** for the RP-01 CH4/H2 RIE-induced n+/n contact.

P24 deliberately gives priority to experimentally reported process values and measured outcomes over additional theoretical derivation.

The target chain is:

`published process condition -> measured converted-region state -> contact electrical result -> detector responsivity/noise/bandwidth result -> local replication -> bounded optimization`.

P24 does **not** claim that every value reported in related HgCdTe process families can be transplanted into RP-01. Each benchmark below carries a provenance class.

---

## 2. Provenance classes used in this module

### `DIRECT-RP01`

Experimentally reported in Smith et al. (2001), the canonical device paper.

### `SAME-LINEAGE-N-TYPE`

Same UWA group and n-type MWIR RIE/contact lineage, but not necessarily the exact RP-01 run.

### `TRANSFER-P-TYPE-X030`

Experimental HgCdTe near x≈0.30 but starting from p-type material; useful for process sensitivity/metrology, not direct n+/n-contact setpoints.

### `TRANSFER-OTHER-X/ARCH`

Experimentally useful but different composition, detector band, doping or contact architecture.

### `MODEL-ONLY`

Values used in a published model fit, not measured process targets.

No value below may change class by repetition in this repository.

---

# 3. Canonical RP-01 empirical baseline

## 3.1 Starting material — `DIRECT-RP01`

Canonical reported material:

- LPE n-HgCdTe on electrically insulating CdZnTe;
- nominal alloy composition `x≈0.30`;
- reported electron concentration `9.8×10^14 cm^-3`;
- reported electron mobility `4.0×10^4 cm^2/V/s`;
- active-layer thickness `9.5 µm`.

The publication does not state the measurement temperature for the supplier n/µ values. Preserve that ambiguity.

## 3.2 Oxide/contact-window RIE — `DIRECT-RP01`

Reported reactor/process:

- Plasma Technology parallel-plate RIE reactor;
- gas notation `CH4/5H2`;
- total gas flow `64 sccm`;
- chamber pressure `100 mTorr`;
- RF power `50 W`;
- plasma exposure `60 s`;
- purpose: remove the approximately `800 Å = 80 nm` anodic oxide in the opened contact region and simultaneously produce an n+ converted HgCdTe region.

The paper does not close:

- reactor model;
- RF frequency;
- powered-electrode area;
- electrode spacing;
- DC self-bias;
- sample/chuck temperature;
- exact individual historical CH4 and H2 MFC values.

P08A's 1:5 same-lineage interpretation can be used as a local candidate gas split only with its existing provenance label.

## 3.3 Direct/near-direct converted-region evidence

The RP-01 fabrication paper reports:

- converted-region average electron concentration `~2.0×10^15 cm^-3`, averaged over the converted depth;
- electron mobility `~3.3×10^4 cm^2/V/s`;
- Hall/resistivity measurements at `80 K` and `300 K`;
- van der Pauw + variable-magnetic-field measurement extending to `2 T`.

The paper also states that previous work using **similar** RIE conditions found n+ conversion extending approximately `8 µm` below the HgCdTe surface.

Continuity rule:

**Do not combine the 2.0×10^15 cm^-3 average density and 8-µm depth and label the resulting sheet density a single directly measured RP-01 quantity.** The depth is cited from earlier similar-condition work rather than demonstrated as the exact depth of the canonical device run.

## 3.4 LBIC validation — `DIRECT-RP01`

The paper fabricated patterned RIE test regions approximately:

- `300 µm × 300 µm`.

LBIC validation used:

- Waterloo Scientific scanning laser microscope;
- Nd:YLF laser;
- wavelength `1.047 µm`;
- continuous-wave illumination;
- irradiance approximately `400 mW/cm^2`;
- sample temperature `80 K`.

A bipolar LBIC signature across the patterned RIE boundary was used as evidence of the n+/n junction/electrically converted region.

This is a valuable practical replication target because it gives a concrete junction-presence test rather than relying solely on sheet Hall data.

## 3.5 Lithography/metallization/contact geometry — `DIRECT-RP01`

Reported contact-mask process and geometry:

- photoresist thickness approximately `4–5 µm`;
- prebake `80 °C / 30 min`;
- chlorobenzene treatment `30 min`;
- pattern/develop/water rinse;
- Cr `300 Å = 30 nm`;
- Au `2700 Å = 270 nm`;
- nine square contacts;
- each contact `300×300 µm`;
- adjacent gaps `50, 100, 150, 200, 250, 300, 350, 400 µm`.

At 80 K, the reported transmission-line result was approximately

`rho_c ≈ 9×10^-4 ohm cm^2`.

This is a majority-carrier contact metric and does not by itself establish minority-carrier blocking quality.

---

# 4. Canonical detector-level functional benchmarks

## 4.1 Responsivity-versus-field experiment — `DIRECT-RP01`

Reported conditions:

- detector temperature `80 K`;
- spectral-response system: Optronics Laboratories Spectral Response Measurement System;
- wavelength used for field-response comparison: approximately `4 µm`;
- chopping frequency `1 kHz`;
- stated field of view `60 degrees`;
- electric field varied using the fabricated detector geometry.

The paper reports that the RIE-contact detector still departed from ideal linear responsivity at sufficiently high electric field because of minority-carrier sweepout.

The authors explicitly state that the contact was **not optimized** and identify n+ carrier density and junction depth as variables requiring further optimization.

Therefore the canonical `100 mTorr / 64 sccm / 50 W / 60 s` RIE is a historically successful starting point, **not a demonstrated optimum**.

## 4.2 Conventional-contact comparison — `DIRECT-RP01`

A two-mask RIE-contact device was compared against a conventional-contact detector at approximately:

- wavelength `3 µm`;
- temperature `80 K`;
- stated `60-degree` FOV.

Starting wafer densities differed:

- RIE-device wafer approximately `9.8×10^14 cm^-3`;
- conventional-device wafer approximately `4.0×10^14 cm^-3`.

The RIE device showed improved sweepout behavior despite that material mismatch.

Use this as qualitative functional evidence, not as a clean matched-pair quantitative effect size.

## 4.3 Noise benchmark — `DIRECT-RP01`

Reported detector-noise condition:

- temperature `80 K`;
- electric field `10 V/cm`;
- low-noise preamplifier;
- HP 35665A dynamic signal analyzer;
- approximately `3 kHz` 1/f-to-g-r knee;
- high-frequency g-r noise level approximately `24.5 nV/sqrt(Hz)`.

Do not substitute this high-frequency plateau as the detector noise at 1 kHz without measured data because 1 kHz lies below the reported knee.

## 4.4 Spectral/detectivity benchmark — `DIRECT-RP01`

Reported conditions/results:

- temperature `80 K`;
- electric field `10 V/cm`;
- chopping frequency `1 kHz`;
- stated `60-degree` FOV;
- detector cutoff approximately `4.4 µm`;
- BLIP specific detectivity approximately `2.0×10^11 cm Hz^1/2/W` at `4 µm`;
- quoted quantum efficiency approximately `70%`;
- historical background photon flux approximately `1.0×10^15 photons cm^-2 s^-1` for the stated 300-K/60-degree condition.

P11/P12 remain authoritative for a modern absolute reconstruction and uncertainty budget.

---

# 5. Same-lineage empirical RIE conversion measurements

These sources are valuable because they show what must actually be measured after plasma exposure.

## 5.1 Siliquini et al. 1997 — vacancy-doped p-Hg0.69Cd0.31Te — `TRANSFER-P-TYPE-X030`

Reported RIE condition:

- material `Hg0.69Cd0.31Te`;
- initial vacancy-doped p-type state;
- pressure `410 mTorr`;
- `CH4/H2` plasma;
- power density `0.4 W/cm^2`;
- physical etch depth approximately `0.2 µm`.

Measured electrical conversion extended approximately

`1.5 µm`

into the semiconductor.

Practical implication:

`d_conv` can be many times larger than `d_etch`; profilometry/physical recession is not a junction-depth measurement.

This value is not transplanted into RP-01 because starting conductivity type and pressure differ.

## 5.2 Siliquini et al. 1998 — As-doped p-Hg0.71Cd0.29Te — `TRANSFER-P-TYPE-X030`

UWA institutional primary record reports:

- material `Hg0.71Cd0.29Te`;
- extrinsic As-doped p-type material;
- prior Hg anneal to eliminate Hg vacancies;
- pressure `340 mTorr`;
- `CH4/H2` plasma;
- power density `0.4 W/cm^2`.

The effective n-type converted-region doping density was extracted by fitting LBIC measurements over

`80–300 K`

using SEMICAD DEVICE, with effective n-type doping density as the fitting parameter.

A secondary/public snippet has circulated a different pressure value near 390 mTorr for this work. P24 adopts the UWA institutional record's **340 mTorr** as the stronger current source and preserves the discrepancy rather than averaging or silently choosing a midpoint.

## 5.3 Musca et al. 1998/1999 — n-type MWIR LBIC lineage — `SAME-LINEAGE-N-TYPE`

The UWA n-type MWIR LBIC work demonstrates that the method can provide:

- confirmation of n+ conversion;
- vertical conversion/junction depth information;
- lateral conversion extent;
- sensitivity to junction grading;
- temperature dependence.

The 1999 junction-depth paper is specifically a quantitative-method development for HgCdTe LBIC depth extraction.

The canonical RP-01 paper cites this same lineage when referring to approximately 8-µm n+ depth under similar conditions.

Until the exact earlier sample/process condition associated with that 8-µm result is recovered, keep it as `SAME-LINEAGE-N-TYPE`, not a direct RP-01 depth setpoint.

---

# 6. Plasma-process factor priority from later experiments

## Park et al. 2007 — p-Hg0.7Cd0.3Te ICPRIE — `TRANSFER-P-TYPE-X030`

A later UWA study varied high-density plasma parameters and used quantitative mobility-spectrum analysis of variable-field Hall/resistivity data.

Within that investigated parameter space:

1. converted-layer transport properties and depth were **most sensitive to process pressure and temperature**;
2. RIE power and ICP power also had significant influence.

The reactor architecture and starting material differ from RP-01, so no numerical ICP condition is transplanted.

However, this provides experimental support for local transfer priorities in P08D:

- measure/control sample temperature rather than ignoring it;
- pressure deserves explicit DOE/control priority;
- record ion-energy/power state;
- use variable-field transport rather than one-field Hall where multiple channels are plausible.

---

# 7. Post-RIE thermal/storage stability is a controlled process variable

## 7.1 Hg anneal can erase the converted state — `TRANSFER-P-TYPE-X030`

Smith et al. 1998 reported:

- extrinsically doped p-type HgCdTe, `x=0.31`;
- RIE condition `400 mTorr`, `CH4/H2`, `90 W`;
- clear RIE-induced p-to-n conversion by LBIC;
- sealed-tube Hg anneal `200 °C / 17 h`;
- after anneal, LBIC indicated that no n-type converted region remained;
- Hall returned to a uniform p-type state comparable with the initial material, reported as approximately `N_A-N_D=2×10^16 cm^-3`, `mu≈350 cm^2/V/s`.

This is not an RP-01 post-RIE treatment. It demonstrates that the electrically converted state is not guaranteed to survive arbitrary later Hg-rich thermal exposure.

### P24 handling rule

After blocking-contact RIE, record every subsequent thermal exposure. Do not introduce an unqualified anneal/bake after conversion.

## 7.2 Room-temperature relaxation observed in another narrow-gap branch — `TRANSFER-OTHER-X/ARCH`

Belas/Grill/Franc/Sitter-lineage work on RIE-created n-HgCdTe with approximately `x=0.21` reported:

- 77-K conductivity fell to less than half its initial value after roughly `2×10^5 s` room-temperature storage;
- raising storage temperature to `323 K` increased relaxation rate by about a factor of five.

The material and plasma architecture differ from RP-01.

Use this only to justify a local stability study and handling-time record.

### Local stability variables to record

- RIE end timestamp;
- time to Hall/LBIC/TLM;
- time to metallization;
- cumulative room-temperature storage;
- storage temperature;
- vacuum/inert/ambient storage condition;
- any bake or cleaning temperature/time;
- time to detector electrical characterization.

A local RIE state is not considered stable merely because it passes one immediate post-process measurement.

---

# 8. Functional blocking strength — empirical scales from other device architectures

## 8.1 Heterojunction blocking-contact experiment — `TRANSFER-OTHER-X/ARCH`

Musca et al. 1997 investigated LWIR HgCdTe heterojunction blocking contacts.

Reported model/experimental interpretation included approximate effective contact recombination velocities:

- heterojunction blocking contact: `~250 cm/s`;
- conventional n+/n blocking-contact case: `>10^4 cm/s`.

The heterojunction detector responsivity at `10 V/cm` was nearly twice that of the compared two-layer devices with nonblocking n+/n contacts.

This is not a target `S_c` for RP-01; it gives an empirical scale showing that contacts with similar majority-carrier electrical behavior can differ by orders of magnitude in minority-carrier recombination behavior.

## 8.2 Overlap-geometry LWIR experiment — `TRANSFER-OTHER-X/ARCH`

Siliquini et al. 1994 used n-type LPE HgCdTe near `x=0.23` and demonstrated experimentally that combining contact blocking with an overlap geometry improved responsivity, low-frequency noise performance and detectivity relative to simpler structures.

Practical implication:

contact geometry and optical/current-collection geometry must be frozen during an RIE-condition comparison. Do not attribute every responsivity change to converted-layer doping/depth.

---

# 9. Model value that must not become a process target

## Smith, Musca, Faraone 2000 — `MODEL-ONLY`

A two-dimensional MWIR photoconductor model used an n+ region with approximately:

- `n+ = 1×10^16 cm^-3`;
- depth `3 µm`.

Those values were model inputs used to fit a practical device. They are useful as evidence that the detector response is strongly influenced by n+ density/depth, but they are **not measured optimum RIE outputs** and shall not replace the RP-01 direct transport values.

---

# 10. Practical local replication sequence

The preferred first local objective is **reproduce the historical outcome chain**, not optimize it immediately.

## Phase A — before-RIE state

For every qualification coupon/device record:

- growth ID/wafer coordinates;
- P06 x/edge and thickness;
- P05 carrier state at declared temperature(s);
- sheet resistance;
- surface/oxide condition;
- oxide thickness;
- mask/window geometry;
- elapsed time since prior process.

Use matched coupons where possible.

## Phase B — reactor/process record

Mandatory local values:

- reactor make/model;
- RF frequency;
- electrode dimensions/spacing;
- sample position and fixture;
- CH4 actual flow;
- H2 actual flow;
- total flow;
- pressure trace;
- forward/reflected RF power;
- measured/calibrated DC self-bias or other ion-energy proxy;
- sample/chuck temperature and calibrated sample-temperature estimate;
- gas stabilization time;
- plasma ignition timestamp;
- RF-on duration;
- chamber clean/season history;
- base pressure.

Historical controller center:

`100 mTorr / 64 sccm total / 50 W / 60 s`

with locally documented gas split provenance.

## Phase C — oxide-clear and physical recession

On dedicated test structures determine:

- oxide-clear time for the actual ~80-nm anodic oxide;
- total physical HgCdTe recession after the complete process;
- roughness/morphology change.

Do not use physical recession as the electrical conversion depth.

## Phase D — electrical conversion

Acquire:

1. sheet resistance/conductance;
2. P05 variable-field Hall at `80 K` and `300 K` during qualification, with escalation to multicarrier analysis as required;
3. conversion-depth measurement by LBIC or independently validated depth method;
4. lateral-conversion measurement around patterned windows;
5. post-RIE storage-time stamps.

Historical comparison values:

- `n_avg≈2.0×10^15 cm^-3`;
- `mu≈3.3×10^4 cm^2/V/s`;
- previous similar-condition n+ depth `~8 µm`.

Treat them as separate comparison outputs with their exact evidence classes.

## Phase E — metallization/TLM

Use P09/P09A.

Historical stack:

- Cr 30 nm;
- Au 270 nm.

Historical 80-K contact-resistivity benchmark:

`rho_c≈9×10^-4 ohm cm^2`.

Record I-V linearity, TLM regression residual, geometry and thermal-cycle stability.

## Phase F — detector-level blocking function

Using P08F/P10/P11/P12/P13, measure the same completed device over a common field grid:

- current and active-region voltage;
- detector temperature/power;
- responsivity `R_v(E)` at defined wavelength/frequency;
- detector-referred noise `e_n(E,f)`;
- `NEP(E)`;
- `D*(E)`;
- temporal response / `tau_eff(E)` where available.

Historical replication anchor:

- `80 K`;
- include `10 V/cm`;
- include `1 kHz`;
- include approximately `4 µm` spectral point;
- retain actual fabricated gap in field normalization.

The exact production field sweep and pass bands remain local qualification items.

---

# 11. Practical first optimization order after successful replication

The historical paper itself identifies converted-region density and depth as incomplete/optimization variables. Later empirical plasma work identifies pressure and temperature as high-sensitivity factors.

Therefore, after a replicated historical-center condition exists, optimize in this order unless local evidence changes the priority:

1. **sample temperature / thermal state** — first establish whether it is controlled and reproducible;
2. **process pressure** around the local historical-center equivalent;
3. **semiconductor exposure after oxide clear / total effective RIE dose**;
4. **ion-energy/RF state** represented by measured self-bias or another calibrated reactor-specific coordinate rather than nominal watts alone;
5. **CH4:H2 ratio** only after MFC calibration and baseline equivalence are established.

For every split, retain the complete output vector:

`{d_etch, d_conv, lateral conversion, sheet transport, mu, rho_c, R_v(E), e_n(E), D*(E), tau_eff(E), stability}`.

Do not optimize `rho_c` alone.

Do not maximize depth or carrier density monotonically.

---

# 12. Minimum empirical acceptance hierarchy

A local blocking-contact process advances through four distinct gates.

## Gate 1 — plasma/material reproducibility

Repeated coupons reproduce:

- oxide clear;
- physical recession/morphology;
- sheet transport;
- electrical conversion depth/lateral spread.

## Gate 2 — majority-carrier contact

Repeated metallized structures demonstrate:

- ohmic I-V;
- stable TLM;
- contact resistivity compatible with the intended detector current/field.

Historical reference: `~9×10^-4 ohm cm^2 at 80 K`.

## Gate 3 — minority-carrier blocking function

Matched detectors demonstrate reduced responsivity sweepout over the intended field range relative to a justified control or process split, after self-heating is separated.

No TLM-only surrogate is accepted for this gate.

## Gate 4 — full detector performance

At the defined operating point:

- responsivity acceptable;
- noise acceptable;
- NEP/D* acceptable;
- bandwidth/temporal response acceptable;
- repeated-device stability acceptable.

P17 receives numerical release limits only after these gates have repeated local data and P20 requirements allocation.

---

# 13. Mandatory stability test before process freeze

Because related HgCdTe RIE states can relax or be erased thermally, characterize selected process candidates at multiple elapsed times.

At minimum design a local study containing:

- immediate/as-soon-as-practical measurement;
- one intermediate room-temperature storage interval;
- one longer interval relevant to actual fabrication queue time;
- post-metallization repeat;
- post-qualified thermal-cycle repeat.

Absolute intervals remain `LOCAL-QUAL` until actual fabrication scheduling is known.

Track changes in:

- sheet resistance;
- Hall state;
- LBIC extent where feasible;
- TLM contact result;
- detector responsivity/noise.

If measurable drift occurs, handling/storage time becomes a controlled process variable in P17/P16.

---

# 14. What is now empirically closed versus still OPEN

## Directly closed historical values

- 100 mTorr;
- 64 sccm total CH4/5H2 notation;
- 50 W;
- 60 s;
- ~80-nm oxide;
- ~2.0×10^15 cm^-3 average converted density;
- ~3.3×10^4 cm^2/V/s converted mobility;
- variable-field Hall to 2 T at 80/300 K;
- LBIC wavelength/irradiance/temperature;
- 30-nm Cr / 270-nm Au;
- 300×300-µm TLM pads with 50–400-µm gaps;
- ~9×10^-4 ohm cm^2 80-K specific contact resistivity;
- detector functional/noise/D* benchmarks above.

## Same-lineage but not exact RP-01

- ~8-µm n+ conversion depth under similar n-type RIE conditions.

## Still OPEN

- exact reactor model;
- RF frequency;
- electrode geometry;
- historical self-bias;
- historical sample temperature;
- exact individual gas flows;
- exact oxide-clear time;
- exact physical semiconductor recession of the canonical 60-s RP-01 run;
- exact vertical donor profile `n(z)`;
- exact lateral conversion distance;
- exact minority-carrier contact recombination velocity/effective boundary condition;
- exact detector contact-pair/gap used for the canonical figures;
- RP-01 converted-state storage/thermal stability;
- empirical process response surface from pressure/temperature/RF/time to `{d_conv,N_s,mu}`;
- process window that maximizes detector-level D* without unacceptable bandwidth/noise penalty.

---

# 15. References

Primary/direct or institutional-primary sources used by P24:

1. E. P. G. Smith et al., *Semiconductor Science and Technology* 16, 455–462 (2001), DOI `10.1088/0268-1242/16/6/306`.
2. J. F. Siliquini et al., *Applied Physics Letters* 70, 3443–3445 (1997), DOI `10.1063/1.119159`.
3. J. F. Siliquini et al., *Applied Physics Letters* 72 (1998), DOI `10.1063/1.120642`.
4. C. Musca et al., *Journal of Electronic Materials* 27, 661–667 (1998), DOI `10.1007/s11664-998-0032-4`.
5. C. Musca et al., *Journal of Electronic Materials* 28, 603–610 (1999), junction-depth LBIC paper.
6. E. P. G. Smith et al., *Applied Physics Letters* 83, 5555–5557 (1998), DOI `10.1063/1.367389`.
7. J. K. White et al., *Journal of Electronic Materials* 30, 762–767 (2001), p-to-n conversion mechanisms.
8. B. A. Park et al., *Journal of Electronic Materials* 36, 913–918 (2007), DOI `10.1007/s11664-007-0132-6`.
9. E. P. G. Smith, C. A. Musca, L. Faraone, *Infrared Physics & Technology* 41, 175–186 (2000), DOI `10.1016/S1350-4495(99)00054-7`.
10. C. Musca et al., *IEEE Transactions on Electron Devices* 44 (1997), DOI `10.1109/16.557711`, heterojunction blocking contacts.
11. J. F. Siliquini et al., *Infrared Physics & Technology* 35, 661–671 (1994), DOI `10.1016/1350-4495(94)90059-0`.

Related stability work from other HgCdTe branches is retained as transfer evidence only and does not define RP-01 handling limits.

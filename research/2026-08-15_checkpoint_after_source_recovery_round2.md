# Recovery checkpoint — source-recovery round 2 after P16

**Date:** 2026-08-15 America/New_York  
**Read after:** `AGENTS.md`, `research/2026-08-15_checkpoint_through_P16.md`, and `research/2026-08-15_checkpoint_after_source_recovery_round1.md`.

This checkpoint records the scientific advances made after source-recovery round 1. It exists specifically so the next agent does not need the conversation context to understand the current frontier.

## 1. Same-UWA transient-decay methodology — P13A

A thesis-level source was recovered:

Ramesh Rajaduray, *Investigation of Spatial Characterisation Techniques in Semiconductors*, B.E. (Hons) thesis, Department of Electrical and Electronic Engineering, University of Western Australia, 1998. Supervisor: John M. Dell. The acknowledgements identify assistance from David Redfern and Ed Smith and support from Lorenzo Faraone.

The experimental sample/method is directly relevant to the RP-01 research lineage:

- LPE-grown n-type HgCdTe active layer;
- nominal `x≈0.30`;
- wet Br2/HBr etched test region;
- indium contacts pressed at opposite ends;
- approximately 77-K operation under vacuum;
- Keithley variable-current bias source;
- HP54522A digital oscilloscope;
- computer-controlled transient acquisition;
- pulsed optical excitation.

### Most important physical statement

Bias was intentionally kept **small** to avoid sweeping excess photogenerated carriers toward the contacts, which were regions of substantially higher recombination.

This is direct same-laboratory support for the P13 rule that a transient decay constant is not automatically the bulk minority-carrier lifetime. At higher field, drift/sweepout can transport excess carriers into contact regions and shorten/distort the measured transient.

### P13 release implication

Before identifying `tau_eff` with a material lifetime:

1. operate in the low-injection regime;
2. establish a low-field regime where the extracted transient is insensitive to further bias reduction within uncertainty;
3. record a separate field-dependent dataset to quantify sweepout/contact effects;
4. retain raw transient and explicit fit window;
5. use `tau_eff` unless a bulk-lifetime interpretation is independently justified.

Created:

- `procedures/P13A_UWA_TRANSIENT_DECAY_LINEAGE_ADDENDUM.md`.

Do not import the thesis's sample-specific lifetime values as RP-01 production limits.

## 2. Critical RP-01 RIE metrology correction — P08B

A direct re-read of Smith et al. 2001 exposed an important wording that changes how the RIE Hall result must be interpreted.

RP-01 reports the RIE carrier density as approximately:

`2.0×10^15 cm^-3`

**averaged over the RIE-converted thickness**.

The mobility is approximately:

`3.3×10^4 cm²/V·s`.

The paper separately cites prior same-UWA n-type work indicating an RIE-induced n+ region extending approximately `8 µm` below the surface under similar conditions.

### Consequence

The reported volumetric density is not independent of the converted depth used in the Hall reduction.

For a uniform converted layer:

`N_s = n_vol * d_conv`.

If `d_conv=8 µm`, then the reported volume density corresponds conditionally to

`N_s≈1.6×10^12 cm^-2`.

If one instead assumed the full 9.5-µm layer, the same volume density would imply about

`1.9×10^12 cm^-2`.

These are derived consistency numbers, not directly published sheet densities.

### Revised RIE process state vector

Do not qualify P08 solely by reproducing `n≈2×10^15 cm^-3`.

Record/qualify separately:

- physical HgCdTe recession `d_etch`;
- oxide-clear time;
- sheet resistance;
- Hall sheet carrier density `N_s` or full sheet conductance state;
- Hall mobility / multicarrier flags;
- electrical conversion depth `d_conv`;
- lateral conversion `L_conv`;
- final TLM specific contact resistivity `rho_c`.

Only calculate converted-region volume density after `d_conv` has been independently measured or defensibly modeled.

For parallel conduction between an RIE-modified surface layer and underlying n-HgCdTe, use full variable-field data and multilayer/mobility-spectrum analysis rather than blindly applying a one-layer Hall formula.

Created:

- `procedures/P08B_RIE_HALL_DEPTH_COUPLING_ADDENDUM.md`.

This addendum takes precedence over earlier wording that treated the RP-01 converted volume density as an independent target.

## 3. Additional direct RP-01 process details recovered

The full RP-01 text also directly confirms:

- plain n-HgCdTe test material was anodically oxidized and patterned into approximately `300×300 µm` RIE-exposed squares;
- after RIE, some samples retained the oxide while others had the oxide stripped using **diluted HCl** for the LBIC comparison;
- Waterloo Scientific scanning-laser microscope;
- diode-pumped Nd:YLF laser;
- wavelength `1.047 µm`;
- continuous-wave intensity approximately `400 mW/cm²`;
- sample temperature `80 K`;
- Hall/resistivity measurements performed at `80 K` and `300 K` with magnetic field up to `2 T`;
- RIE summary density/mobility pair remains not uniquely assigned in accessible text to one measurement temperature;
- Mask-2 process directly gives ~4–5-µm resist, `80 °C / 30 min` prebake, `30 min` chlorobenzene treatment, then pattern/develop/water rinse before RIE and Cr/Au lift-off.

The diluted-HCl strip was part of a comparison/test sequence; do not automatically insert it into the production contact process unless the specific production flow requires it.

## 4. Exact ~8-µm RIE depth conditions remain unresolved

Correct primary source:

C. A. Musca, J. F. Siliquini, E. P. G. Smith, J. M. Dell, L. Faraone, “Laser Beam Induced Current Imaging of Reactive Ion Etching Induced n-Type Doping in HgCdTe,” *Journal of Electronic Materials* 27, 661–667 (1998), DOI `10.1007/s11664-998-0032-4`.

The UWA institutional record confirms this is the paper used for depth/lateral characterization of RIE-induced n-type doping.

However, publicly accessible metadata/search text still does **not** expose the exact pressure, RF power/power density, process time and gas settings attached to the approximately 8-µm n-type depth cited later by RP-01.

Therefore:

- retain `~8 µm` as `P-OTHER-SOURCE / SIMILAR-CONDITIONS`;
- do not call it a directly measured RP-01 depth;
- do not reverse-engineer the volumetric Hall density using 8 µm and then present the result as independent validation;
- qualification must measure `d_conv` locally.

Related UWA p-type studies show very different depths for different process/sample states, proving transfer is unsafe. Examples include ~1.5-µm electrical conversion after only ~0.2-µm physical etch in a different p-type CH4/H2 process.

## 5. Thesis/full-text source-recovery negative result

Targeted searches were performed for:

- David Redfern thesis/dissertation;
- Ed Smith thesis/dissertation;
- Kevin Winchester thesis/dissertation;
- full public text of the 2000 UWA paper “Dry plasma technology for in-situ vacuum processing of HgCdTe infrared photodetectors.”

No directly accessible thesis/full experimental text was recovered through the public index/search routes used.

The 2000 UWA/IEEE paper remains confirmed bibliographically and is likely the correct bridge for RIE-to-metal/in-situ vacuum processing, but public indexing exposes metadata rather than the omitted metal deposition/lithography parameters.

Do not repeatedly issue generic title searches expecting those missing parameters to appear.

## 6. Current RIE gas-ratio state from round 1 remains unchanged

Direct RP-01:

- printed `CH4/5H2`;
- total `64 sccm`;
- `100 mTorr`;
- `50 W`;
- `60 s`.

Secondary same-lineage review evidence supports:

`CH4:H2 = 1:5`.

Conditional derived split:

- CH4 `10.6667 sccm`;
- H2 `53.3333 sccm`.

This remains **secondary-source-supported/derived**, not direct primary UWA MFC closure.

## 7. Current highest-value unresolved variables after round 2

### RIE/contact

1. primary confirmation of the CH4:H2 1:5 ratio / individual MFC values;
2. exact Musca-1998 plasma conditions attached to ~8-µm `d_conv`;
3. actual converted-layer sheet Hall data / multilayer reduction used historically;
4. RIE reactor electrode area/spacing, RF frequency, self-bias and sample temperature;
5. exact RIE-to-metal transfer delay, base pressure and Cr/Au rates.

### Lithography/passivation

6. exact UWA resist product, spin, exposure dose, developer and development time;
7. exact UWA native-anodic-oxide electrolyte/current/endpoint/rinse;
8. Br2/HBr mesa concentration basis and final rinse/strip sequence.

### Upstream

9. x≈0.30 source synthesis/homogenization;
10. final CdZnTe face/miscut and exact surface prep;
11. growth-time/thickness relation for the selected x≈0.30 tie line;
12. Hg anneal chemical potential/time/cooldown to reproduce the RP-01 material state.

## 8. Recommended next work

Avoid another broad metadata-only search loop. Highest-value next paths are:

1. search later UWA full-text HgCdTe photoconductor/MEMS papers that explicitly inherit the same fabrication line and may state resist/developer/metal-process details;
2. search patents/proceedings by the exact UWA authors for passivation/contact processing;
3. if primary source closure fails, design statistically controlled local transfer DOEs for P01/P02/P08/P09 rather than guessing setpoints;
4. synchronize `AGENTS.md`, `docs/RP01_GAP_MATRIX.md`, and `docs/SOURCE_LEDGER.md` with P08A/P08B/P13A and this checkpoint.

## 9. Recovery order

A replacement agent should now read:

1. `AGENTS.md`;
2. `research/2026-08-15_checkpoint_through_P16.md`;
3. `research/2026-08-15_checkpoint_after_source_recovery_round1.md`;
4. this round-2 checkpoint;
5. `procedures/P08_RIE_BLOCKING_CONTACT_QUALIFICATION.md` + P08A + P08B;
6. `procedures/P13_TEMPORAL_FREQUENCY_RESPONSE_LIFETIME.md` + P13A;
7. `docs/RP01_GAP_MATRIX.md` and `docs/SOURCE_LEDGER.md`;
8. branch-specific research notes before continuing.

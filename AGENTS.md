# AGENTS.md — MCT-Device front-door continuity record

## Mission

Build a source-traceable, end-to-end HgCdTe photodetector fabrication and characterization **manual/booklet** that a competent researcher can execute without undocumented tribal knowledge.

Canonical first process: **RP-01**, E. P. G. Smith et al., *Semiconductor Science and Technology* 16, 455–462 (2001), DOI `10.1088/0268-1242/16/6/306`.

There is **no end-to-end `REPRODUCIBLE-RELEASE` yet**. The repository contains a controlled fabrication/measurement architecture plus explicit routes for closing literature gaps locally.

---

# Non-negotiable rules

1. **Never invent a missing number.** Use `OPEN`, `CAL`, `QUAL`, `PARTIAL`, `CANDIDATE-P`, explicit derivation, or an evidence class.
2. Never splice incompatible HgCdTe process families and call the result a published recipe.
3. Separate direct publication, same-lineage evidence, transfer-family evidence, model values, derived physics, apparatus calibration and local qualification.
4. Every critical process step requires output metrology and a pass/fail or qualification gate.
5. Preserve negative searches, rejected inferences, corrections and source conflicts.
6. Keep Hall quantities, optical-edge quantities, physical etch depth, electrical conversion depth, sheet density and measured geometry distinct.
7. Keep majority-carrier contact resistivity `rho_c` distinct from minority-carrier contact recombination velocity/effective loss boundary `S_c`.
8. Use measured fabricated geometry for field, area and D* normalization.
9. Treat passivation, post-RIE elapsed time/thermal exposure, anneal cooldown and packaging as detector-process variables.
10. A measured system bandwidth is not detector bandwidth until external transfer functions are de-embedded.
11. Engineering specifications come from required detector/material performance; observed process spread does not define its own passing limits.
12. Failure diagnosis uses competing hypotheses and discriminating tests; never force one cause from one symptom.
13. Every controlled process variable should trace forward to a detector requirement.
14. Repository scientific specifications do not replace institution-specific Hg/Cd/Br2/HBr/H2/CH4/high-temperature/vacuum/cryogenic EH&S authorization.
15. Every numerical sensitivity/tolerance must state protected output, input variable, operating point and evidence class. Proxy relations may size an experiment but cannot release a production specification.
16. A tabulated equilibrium ratio such as `xS/xL` is not a differential `dxS/dxL`; changing tie-line coordinates simultaneously does not produce an independent partial derivative.
17. A coded DOE result does not create a physical process tolerance. Physical perturbations require metrology/run variance, apparatus capability and same-regime bounds.
18. Repeated observations from one melt/source genealogy are not independent process replicates.
19. Never regress reciprocal Hall density through a p/n Hall-sign transition. Near the transition use signed Hall/tensor information and multicarrier analysis.
20. Anneal tolerances must satisfy both the detector/material-performance budget and margin to the carrier-state transition zone.
21. **Empirical/practical literature first.** Before creating another theoretical placeholder for a process variable, search primary papers, theses, patents and institutional repositories for actual times, temperatures, flows, pressures, concentrations, dimensions, apparatus, metrology settings, output values and failure observations.
22. Theory is used to connect genuine literature gaps, check consistency and allocate requirements — not to displace experimentally reported process information.
23. A successful historical process condition is not automatically an optimum. Preserve author statements identifying unoptimized variables.
24. For anodic passivation, equal oxide thickness does not imply equal interface state. Record bath chemistry, starting surface, cell geometry, current density, full `V(t)`, charge/area, physical oxide and downstream electrical/device response.
25. Color is secondary oxide metrology only. Never release anodic-oxide thickness or quality from color without a calibrated physical correlation.

---

# Current checkpoint — READ THIS FIRST

Latest recovery checkpoint:

`research/2026-08-16_checkpoint_after_empirical_passivation_round18.md`

Then read, in descending order as needed:

- `research/2026-08-16_checkpoint_after_empirical_blocking_contact_round17.md`
- `research/2026-08-16_checkpoint_after_hg_anneal_boundary_round16.md`
- `research/2026-08-16_checkpoint_after_information_design_round15.md`
- `research/2026-08-16_checkpoint_after_lpe_jacobian_round14.md`
- `research/2026-08-16_checkpoint_after_analytical_sensitivity_round13.md`

Latest empirical source/gap files:

- `docs/SOURCE_LEDGER_ADDENDUM_ROUND18.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND18.md`
- `docs/SOURCE_LEDGER_ADDENDUM_ROUND17.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND17.md`
- `docs/SOURCE_LEDGER_ADDENDUM_ROUND16.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND16.md`
- `docs/SOURCE_LEDGER_ADDENDUM_ROUND14.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND14.md`
- `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND15.md`

Older round-6/7/8/9 source and gap addenda retain important provenance and rejected inferences.

---

# Controlled module set

- P01 wet mesa + P01A
- P02 anodic oxide + P02A/P02B/P02C
- P03 x≈0.30 LPE + P03A/P03B/P03C/P03D/P03E
- P04 Hg anneal + P04A/P04B
- P05 Hall/VdP material metrology
- P06 FTIR composition/thickness mapping
- P07 CdZnTe substrate + P07A/P07B/P07C
- P08 RIE blocking contact + P08A–P08G
- P09 Cr/Au/TLM + P09A
- P10 DC bias/self-heating
- P11 absolute radiometry/responsivity
- P12 noise/PSD/NEP/D* + P12A/P12B
- P13 temporal/frequency response + P13A
- P14 lithography/CD + P14A
- P15 cryogenic package
- P16 master end-to-end traveler + blank traveler
- P17 statistical process capability/release + register
- P18 failure-analysis/CAPA + record
- P19 requirements traceability
- P20 analytical sensitivity / requirements allocation + register
- P21 LPE response-surface / empirical Jacobian + register
- P22 information-optimal DOE planning + register
- P23 Hg-anneal state-boundary / local Jacobian + register
- P24 blocking-contact empirical process window + empirical qualification register
- **P25 anodic-oxide empirical process window + empirical qualification register**

P24 and P25 are deliberately empirical/practical and supplement the earlier physics/provenance modules rather than replacing them.

---

# Canonical RP-01 direct anchors — do not drift

## Material

- LPE n-HgCdTe on electrically insulating CdZnTe
- nominal `x≈0.30`
- supplier-reported `n=9.8×10^14 cm^-3`
- supplier-reported `mu=4.0×10^4 cm²/V·s`
- active thickness `9.5 µm`
- supplier n/mu measurement temperature remains undisclosed

## Anodic oxide

- native anodic oxide
- nominal thickness `~800 Å = 80 nm`
- formed after mesa definition and before contact-window RIE

RP-01 does **not** directly close bath/current/electrodes/endpoint/time/rinse.

## Contact-window RIE

- Plasma Technology parallel-plate reactor
- printed `CH4/5H2`
- total `64 sccm`
- `100 mTorr`
- `50 W`
- `60 s`

Historical unknowns remain:

- reactor model
- RF frequency
- powered-electrode area/spacing
- self-bias
- sample temperature
- exact individual historical gas flows
- base pressure/seasoning details

P08A same-lineage evidence supports interpreting the notation as `CH4:H2=1:5`; the corresponding 10.6667/53.3333-sccm split is a **derived local candidate**, not direct historical MFC closure.

## Converted region

Direct RP-01 paper:

- converted average electron density `~2.0×10^15 cm^-3`, explicitly averaged over converted depth
- mobility `~3.3×10^4 cm²/V·s`
- Hall/resistivity at `80 K` and `300 K`
- variable magnetic field to `2 T`

Same-lineage earlier n-type work cited by RP-01:

- approximately `8 µm` n+ conversion depth under similar RIE conditions

**Do not combine 2e15 cm^-3 and 8 µm and call the derived sheet density a directly measured canonical RP-01 value.**

## RP-01 LBIC practical apparatus

- patterned RIE test square `300×300 µm`
- Waterloo Scientific scanning laser microscope
- Nd:YLF laser
- `1.047 µm`
- CW
- approximately `400 mW/cm²`
- measurement at `80 K`

LBIC is the same-lineage preferred nondestructive method for confirming n+ conversion and estimating vertical/lateral extent.

## Mask-2 / metal / TLM

- resist `~4–5 µm`
- prebake `80 °C / 30 min`
- chlorobenzene `30 min`
- pattern/develop/water rinse
- Cr `300 Å = 30 nm`
- Au `2700 Å = 270 nm`
- nine `300×300-µm` contacts
- adjacent gaps `50–400 µm` in 50-µm increments
- 80-K `rho_c≈9×10^-4 Ω·cm²`

The exact historical deposition method/rates/base pressure and RIE-to-metal delay remain open.

## Detector benchmark

- 80 K
- stated 60° FOV
- spectral response at 1 kHz
- responsivity-vs-field comparison near 4 µm
- representative noise field 10 V/cm
- low-noise preamp + HP35665A
- 1/f knee ~3 kHz
- high-frequency g-r plateau ~24.5 nV/√Hz
- cutoff ~4.4 µm
- BLIP D* ~`2.0×10^11 cm Hz^1/2 W^-1` at 4 µm
- quoted QE ~70%

Do not use the 24.5-nV/√Hz high-frequency plateau as the 1-kHz noise automatically.

The exact contact pair/gap of the canonical plotted device remains open.

---

# P25 — empirical native anodic-oxide/passivation state

P25 is now the controlling empirical front end for the P02 native-oxide branch.

## Strongest executable transfer center

Texas Instruments U.S. Patent 3,977,018 discloses an actual HgCdTe photoconductor anodization process:

- HgCdTe specimen = **anode**
- **carbon-rod cathode**
- electrolyte `0.1 M KOH`
- solvent `90% ethylene glycol / 10% DI water`
- galvanostatic constant current
- current density approximately `0.30 mA/cm²`
- formation/terminal region approximately `15 V`
- approximate formation time `2 min`
- oxide approximately `800 Å = 80 nm`
- reported visual appearance: uniform deep blue

This is the default **transfer center**, not the historical UWA/RP-01 anodization recipe.

Independent experimental HgCdTe work validates the same bath family at room temperature and approximately `0.2–0.5 mA/cm²`, including ~70-nm oxide examples.

## Cell/bath rules

Every P25 run records:

- KOH/EG/water batch and age
- reagent lots/grades
- exact locally adopted 90:10 preparation convention
- bath temperature
- anode-contact method
- cathode material/area
- electrode separation/orientation
- immersion depth
- electrochemically exposed area
- agitation state
- bubbles/abnormalities

Later Pt-cathode HgCdTe cells are separate process lineages. Do not merge them with the TI carbon-cathode process.

## V(t) is a process fingerprint

The x≈0.30 anodic-oxidation lineage shows an initial dissolution/precipitation/induction stage whose behavior depends on current density, pH, starting surface and mass transport.

Therefore record/reduce:

- raw `V(t)`
- induction time `t_ind`
- defined growth-region `dV/dt`
- terminal voltage
- total charge
- charge/area
- physical oxide thickness

`0.30 mA/cm² for ~2 min` is not a sufficient process record.

A final ~80-nm oxide reached after an abnormal V(t) trace is not automatically process-equivalent.

## Agitation and starting surface

Agitation is a controlled variable because it can change dissolution/precipitation kinetics. First transfer uses a static/unstirred bath unless a selected primary implementation requires otherwise.

Do not transplant aggressive Br2 surface-removal conditions from bulk/mechanism studies into the 9.5-µm RP-01 LPE layer.

## Physical and electrical oxide are separate outputs

Equal d_ox does not imply equal:

- oxide chemistry
- fixed charge
- interface-state density
- surface accumulation
- shunting
- recombination
- 1/f noise

Other-x native-oxide interface values are diagnostic scales only, not RP-01 specifications.

Same-UWA x≈0.23 gate-controlled photoconductor work proves the practical tradeoff: accumulation can suppress recombination but excessive accumulation can shunt the detector. That device's ~50-mV optimum, ~72-mV floating state and ~70% responsivity gain are **transfer-only** numbers.

## Sidewall / downstream closure

Because RP-01 anodizes after mesa formation, P02C sidewall/perimeter qualification is mandatory.

P25 release chain:

`incoming surface -> bath/cell/V(t) -> physical oxide -> sidewall/interface -> P08 oxide clear+n+ conversion -> P09 TLM -> P10 dark electrical -> P11 responsivity -> P12 noise/D* -> P13 dynamics -> stability`.

An 80-nm planar witness alone cannot release P25.

## P25 main blockers

- exact historical UWA anodization traveler
- local bath ratio convention/reagent grades
- local cathode geometry/separation
- exposed-area fixture definition
- RP-01-compatible final pre-anodization clean
- post-anodization rinse/dry
- repeated x≈0.30 LPE V(t)/Q/A/thickness data
- interface/noise acceptance metric
- sidewall closure
- P08 clear compatibility
- storage/thermal stability
- P17 capability

---

# P24 — empirical blocking-contact state

P24 is the controlling empirical front end for the RIE/contact branch.

## Physical etch is not electrical conversion depth

Siliquini et al. 1997, vacancy-doped p-Hg0.69Cd0.31Te:

- 410 mTorr
- CH4/H2
- 0.4 W/cm²
- ~0.2-µm physical etch
- ~1.5-µm electrical conversion

Therefore `d_etch != d_conv` is experimentally established as a process warning.

## x≈.29 extrinsic p-type LBIC/doping branch

UWA institutional record, Siliquini et al. 1998:

- As-doped p-Hg0.71Cd0.29Te
- prior Hg anneal
- 340 mTorr
- CH4/H2
- 0.4 W/cm²
- LBIC 80–300 K
- SEMICAD DEVICE fit for effective converted-region doping

Some public snippets give ~390 mTorr. Preserve the conflict; UWA institutional record states 340 mTorr.

## Plasma factor priority

Park et al. 2007, p-Hg0.7Cd0.3Te ICPRIE:

- converted transport/depth most sensitive to **pressure and temperature** in the investigated space
- RIE/ICP powers also significant

Different reactor/material branch; transfer factor priority, not numerical setpoints.

Local RP-01 optimization priority after historical-center replication:

1. actual sample thermal state
2. pressure
3. semiconductor exposure after oxide clear/effective dose
4. self-bias/ion-energy/RF state
5. gas-ratio refinement

## Post-RIE thermal/storage history

Transfer-family evidence shows the plasma-induced state can relax or be thermally reversed. These are not RP-01 stability limits.

Record:

- `t_RIE->Hall`
- `t_RIE->LBIC`
- `t_RIE->metal`
- storage temperature/ambient
- cumulative room-temperature exposure
- later thermal excursions

## Historical contact was not optimized

Smith et al. explicitly report remaining high-field sweepout and identify n+ density/junction depth as variables requiring further optimization.

Therefore `100 mTorr / 64 sccm / 50 W / 60 s` is a successful historical center, not a proven optimum.

## P24 four-gate release hierarchy

1. **plasma/material:** oxide clear, physical recession/morphology, sheet transport, LBIC vertical/lateral conversion
2. **majority contact:** ohmic I-V, TLM, stability
3. **minority blocking:** R(E) sweepout function with self-heating separated and matched controls
4. **full detector:** responsivity, noise/NEP/D*, bandwidth/time response, stability, repeated devices/runs

No contact process is released on TLM alone.

---

# LPE state — P03/P21/P22

Historical Honeywell tie line:

`xL=.082, yL=.810, TL=507 °C -> historical xS≈.29`.

Derived source mass fractions:

- Hg `.249738`
- Cd `.012502`
- Te `.737760`

`xS/xL=3.54` is **not** `dxS/dxL`. Adjacent table secants also change yL/TL and are not partial derivatives.

P03E controls actual supercooling as

`DeltaT_SC = TL_actual - T_contact`.

P21 maps

`{xL,yL,TL_actual,DeltaT_SC,t_contact,melt geometry/source use/Hg loss}`

into

`{x_opt,thickness,uniformity,optical edge,morphology}`.

P22 provides coded/Fisher-information DOE design but physical factor half-ranges remain local qualification values.

Do not release a balance/T/time tolerance from the historical tie line alone.

---

# Anneal state — P04/P23

Cooldown is part of the Hg-stoichiometry process. Record:

`T_sample(t), T_reservoir(t), pHg(t)`.

Use final measured state:

`{carrier state, n_H/multicarrier, mu_H, optical x/edge, thickness, morphology, lifetime/device proxy}`.

P23 state labels:

- `N-LIKE`
- `P-LIKE`
- `TRANSITION/MULTICARRIER`

For a two-carrier low-field model,

`R_H=(p mu_h²-n mu_e²)/{q(p mu_h+n mu_e)²}`

so Hall-sign reversal is not p=n and apparent reciprocal Hall density becomes singular near cancellation.

Do not fit one global `log10(n_H)` model through conversion.

No unique RP-01 dwell/T/pHg/cooldown is released.

---

# Substrate / wet mesa / surface

- CdZnTe is the correct substrate family.
- Exact RP-01 Zn fraction/orientation/miscut/final-surface history remain qualification variables.
- P07C releases final surface by removed depth + morphology/chemistry proxy + clean-to-load + resulting interface quality.
- Br2/MeOH branches are transfer methods unless direct RP-01 evidence exists.

Wet mesa near-x branch:

- nominal 2% Br2 in 3:1 EG:HBr
- ~2.78 µm/min at 21 °C
- anisotropy ~0.63
- roughness ~2 nm
- rate variation ~±26%
- source does not define percentage basis of “2% Br2”

Do not guess wt%, vol%, or wt/vol.

---

# Measurement state

## Hall — P05

Use current reversal, field reversal, van der Pauw redundancy, variable field and current-linearity/self-heating checks. Escalate to multicarrier/QMSA when curvature/sign changes/MR invalidate one-carrier interpretation.

RP-01 one-carrier screening consistency:

- rho ~0.159 Ω·cm
- Rs ~168 Ω/sq for 9.5 µm
- |RH| ~6.37×10^3 cm³/C

## FTIR — P06

At x=.30, 80 K, controlled Hansen model gives:

- Eg ~0.243684 eV
- lambda_Eg ~5.0879 µm

This is **not** the detector's ~4.4-µm measured cutoff. Do not force equality.

## Bias/self-heating — P10

Use measured gap and active voltage:

`E = V_active/L_measured`.

At fixed E, simple one-carrier screening gives Joule power proportional to E². This is a sensitivity, not a substitute for measured detector temperature.

## Radiometry — P11

Preferred absolute responsivity uses calibrated radiance/transfer detector and measured physical aperture/view factor.

Historical 300-K / 4.4-µm-step / 60-degree-full-cone reconstruction gives ~1.12×10^15 photons cm^-2 s^-1, near the quoted ~1e15 scale, but remains a reconstruction.

## Noise — P12

`NEP=e_n/R_v`

`D*=R_v sqrt(A)/e_n`.

Subtract independent contributions at PSD level, not ASD level.

## Temporal response — P13

`H_meas = H_source H_optics H_detector H_bias H_preamp H_cable H_instrument`.

De-embed external transfer before calling a rolloff detector bandwidth.

Use `tau_eff` unless bulk-lifetime interpretation is independently justified.

---

# P17/P18/P19/P20 control architecture

## P17 statistical release

Separate:

`measurement -> within-wafer spatial -> run-to-run -> source/substrate lot -> long-term tool/operator`.

No generic Cpk threshold. Current end-to-end process remains below `PILOT-RELEASE` because no local repeated fabrication dataset exists.

## P18 failure analysis

Use:

`signature -> competing mechanisms -> discriminating tests -> root cause -> containment/corrective action -> verification`.

Preserve failed/negative runs.

## P19 traceability

Link:

`final detector requirement -> physical characteristic -> intermediate metric -> controlling process -> P17 release -> P18 failure response`.

Requirement classes:

- `HISTORICAL-REFERENCE`
- `PHYSICS-REQUIREMENT`
- `LOCAL-SPEC-OPEN`
- `LOCAL-QUALIFIED`
- `RELEASED`

## P20 sensitivity/allocation

Evidence classes:

- `IDENTITY`
- `MODEL-CONDITIONAL`
- `PROXY-CONDITIONAL`
- `EMPIRICAL-REQUIRED`

Support results retained:

- D*: responsivity +1, noise ASD -1, area +0.5 normalized sensitivity
- ideal Joule power: field +2
- Hansen lambda_Eg near x=.30/80 K: ~-33.1 nm per +0.001 x, **not detector-cutoff sensitivity**
- one-pole f3dB vs tau: -1 normalized sensitivity

These are support tools, not substitutes for empirical process data.

---

# Current highest-priority OPEN practical details

## P09 metallization — next empirical target

RP-01 directly closes:

- Cr 30 nm
- Au 270 nm
- resulting TLM `rho_c≈9×10^-4 Ω·cm²` at 80 K

Still recover/qualify:

- thermal vs e-beam evaporation
- base pressure
- Cr deposition rate
- Au deposition rate
- source material/purity
- boat/crucible/source geometry
- substrate/chuck temperature
- rotation/fixture
- RIE-to-metal delay/storage/ambient
- in-situ vs air transfer
- thickness calibration/tooling factor
- lift-off solvent/time/agitation
- post-metal clean/anneal, if any
- adhesion and cryogenic-cycle stability
- contact aging

## Blocking contact

- exact Plasma Technology reactor model
- RF frequency
- electrode area/spacing
- historical self-bias
- historical sample temperature
- exact individual CH4/H2 flows
- oxide-clear time
- canonical physical HgCdTe recession
- exact process tied to ~8-µm n-type conversion depth
- canonical n(z) / lateral conversion
- RP-01 post-RIE aging/thermal budget

## Native oxide

- exact UWA/RP-01 bath/current/cell/rinse
- local bath ratio convention/reagent grades
- selected cathode geometry/separation
- final pre-anodization clean
- rinse/dry
- local V(t)/Q/A/thickness capability
- interface/noise limits
- sidewall closure
- P08 clear compatibility
- storage/thermal stability

## Other fabrication gaps

- exact lithography resist/spin/exposure/developer
- exact CdZnTe face/miscut/final clean
- complete Hg anneal architecture/trajectory
- full LPE source synthesis/charge mass/well geometry/growth trajectory

These gaps should trigger **literature recovery first**, not arbitrary local numbers.

---

# Active source-recovery targets / negative searches

Round 18 identified but did not recover full experimental text for:

- John Kenion White 2005 UWA thesis, “Mid-wave infrared HgCdTe photodiode technology based on plasma induced p-to-n type conversion” — institutional record and PDF endpoint found; current PDF retrieval returned access/403.
- Ryan Westerhout 2013 UWA thesis on passivation/dark current/1/f noise — institutional record and PDF endpoint found; current PDF retrieval returned access/403.
- Smith et al. 2000 “Dry plasma technology for in-situ vacuum processing of HgCdTe infrared photodetectors” — bibliographic record / IEEE document 939185 identified; full experimental text not recovered.
- same-UWA Musca/Smith/Dell/Faraone photoconductor passivation/contact proceedings paper — relevant bibliographic identity known, experimental traveler still unrecovered.

These are **not recovered by the current routes**, not evidence that the information does not exist.

---

# Next logical work

The user explicitly wants the manual to remain empirical/practical.

Proceed with **Round 19: empirical P09 Cr/Au metallization and lift-off recovery**.

1. Search exact RP-01/UWA papers, theses, proceedings, patents and archived records for deposition apparatus and actual numbers.
2. Recover if possible: evaporation method, base pressure, deposition rates, source purity, substrate temperature, RIE-to-metal delay, in-situ/air transfer, lift-off solvent/time/agitation, post-metal thermal treatment and cryogenic stability.
3. Build a P26 practical metallization process window and traveler using actual values with provenance classes.
4. Preserve 30-nm Cr / 270-nm Au / ~9e-4 Ω·cm² at 80 K as the direct RP-01 anchor.
5. If the exact UWA conditions remain inaccessible, use the strongest same-lineage/composition-matched primary process as a transfer center and mark it clearly.
6. Use theory only after empirical recovery is exhausted and only where a missing number materially blocks a process decision.

Do not populate production tolerances without local repeated-device data.

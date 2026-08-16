# RP-01 process-closure matrix

This file is the working checklist for deciding when RP-01 has enough information to become an executable process traveler.

Status codes:

- `CLOSED-P` — directly closed by published experimental source.
- `CLOSED-D` — closed by a documented derivation from published quantities.
- `CANDIDATE-P` — a primary-source process compatible enough to qualify, but not proven to be the exact RP-01 lineage/process.
- `CONTROLLED-QUAL` — a controlled qualification/metrology procedure now exists, but final production limits or historical-lineage details remain open.
- `CAL` — must be calibrated on the actual apparatus.
- `QUAL` — requires a qualification experiment before release.
- `PARTIAL` — only part of the required variable/evidence set is closed.
- `OPEN` — source/procedure not yet identified.
- `N/A` — not required for this architecture.

| Module | Variable / evidence required | Status | Current evidence / next action |
|---|---|---|---|
| Device definition | detector type | CLOSED-P | n-type photoconductor |
| Device definition | nominal alloy composition | CLOSED-P | x≈0.30; approximation must be retained |
| Device definition | operating temperature | CLOSED-P | 80 K for reported performance |
| Device definition | exact active length/width | OPEN | recover from paper lineage/mask information |
| Material | HgCdTe layer thickness | CLOSED-P | 9.5 µm |
| Material | incoming carrier density | CLOSED-P | Fermionics supplier specification stated by Smith et al. |
| Material | incoming mobility | CLOSED-P | Fermionics supplier specification stated by Smith et al. |
| Material | temperature of historical incoming n/µ values | OPEN | RP-01 does not state measurement temperature; do not relabel as 77/80 K |
| Material | incoming resistivity consistency value | CLOSED-D / QUAL | one-carrier benchmark gives ~0.159 Ω·cm and ~168 Ω/sq for 9.5 µm; measured state preferred |
| Substrate | material family | CLOSED-P | electrically insulating CdZnTe |
| Substrate | Zn fraction / lattice match | PARTIAL / QUAL | y≈0.04 successfully used for x≈0.30 LPE, while other lattice-parameter work gives values nearer ~0.03; release from measured lattice mismatch, not nominal y alone; P07 |
| Substrate | polarity | CONTROLLED-QUAL / OPEN | A/B is now a required measured variable; exact RP-01 production polarity remains unresolved; P07 |
| Substrate | miscut magnitude/azimuth | CONTROLLED-QUAL / OPEN | primary LPE work shows a process-dependent optimum around ~1.2–2° off (111), but exact horizontal-slider optimum remains to qualify; P07 |
| Substrate | XRD crystalline quality | CONTROLLED-QUAL / QUAL | historical high-quality Cd0.96Zn0.04Te benchmark ~25 arcsec; production limit must be detector-correlated; P07 |
| Substrate | EPD/dislocation metric | CONTROLLED-QUAL / QUAL | historical benchmark ~5×10^4 cm^-2; Everson B-face screening method identified; production limit still open; P07 |
| Substrate | Te inclusions/precipitates | CONTROLLED-QUAL / QUAL | IR microscopy + sacrificial etch-pit screening specified; numerical reject limit still open; P07 |
| Substrate | trace impurities / Cu | CONTROLLED-QUAL / QUAL | substrate Cu and Te-secondary phases can perturb lightly doped LPE carrier state; analytical method required, threshold still open; P07 |
| Substrate | electrical isolation | CONTROLLED-QUAL / QUAL | resistivity/leakage must be measured; minimum requirement must be derived from detector leakage sensitivity; P07 |
| Substrate | dimensions / TTV / bow | CONTROLLED-QUAL / OPEN | record defined; exact dimensions await released boat geometry; P07 |
| Substrate prep | polish history / roughness | CONTROLLED-QUAL / QUAL | full history and AFM/DIC surface gate defined; numerical roughness limit still open; P07 |
| Substrate prep | final Br2/methanol clean | CANDIDATE-P / OPEN | successful LPE families use short Br2/methanol treatments, but concentration/time vary; exact RP-01 recipe, concentration basis, removal depth and rinse remain open; P07 |
| Substrate prep | clean-to-LPE delay | OPEN / QUAL | must be minimized/logged and qualified against surface state; P07 |
| LPE | growth method | CLOSED-P | RP-01 states LPE; x≈0.30 Te-rich horizontal-slider growth demonstrated in Schmit–Hager–Wood lineage |
| LPE | candidate melt composition | CANDIDATE-P | Bowers–Schmit tie line xL=0.082, yL=0.810, TL=507 °C gives xS=0.29; P03 |
| LPE | elemental charge fractions | CLOSED-D / QUAL | mole fractions Hg 0.17442, Cd 0.01558, Te 0.81000; mass fractions Hg 0.249738, Cd 0.012502, Te 0.737760 |
| LPE | charge weighing uncertainty | CONTROLLED-QUAL / QUAL | sensitivity model shows Cd mass dominates xL error; balance must be qualified at tens-of-mg Cd loads; final tolerance awaits allowed Δx budget |
| LPE | total charge mass / melt depth | OPEN / CAL | select from actual growth-well geometry and depletion behavior; do not combine Radhakrishnan 4.8 g with Honeywell composition as a published recipe |
| LPE | charge synthesis / homogenization | PARTIAL / QUAL | 6N elements and 700 °C/8 h evacuated-ampoule synthesis exist in a different branch; transfer to x≈0.30 remains to qualify |
| LPE | furnace/boat architecture | CANDIDATE-P / CAL | covered graphite horizontal slider, separate Hg source, quartz tube, N2 purge/H2 atmosphere are primary-source anchored |
| LPE | Hg-loss compensation | CANDIDATE-P / CAL | HgTe or HgTe+Te auxiliary source demonstrated; source mass/area/free-volume capability must be qualified |
| LPE | growth temperature | CANDIDATE-P / QUAL | TL=507 °C tie line; ~500 °C is primary-source supported, derived ~7 °C supercooling center point |
| LPE | equilibration | OPEN / QUAL | independent Te-rich processes report ~60 min; selected x≈0.30 charge/boat requires equilibrium criterion |
| LPE | supercooling/cooling profile | PARTIAL / QUAL | heat above liquidus then grow below; exact ΔT/ramp/cooling trajectory remains to qualify |
| LPE | substrate meltback | CANDIDATE-P / QUAL | in-situ meltback demonstrated in related slider process; x≈0.30 chemistry/time/removed depth remain open |
| LPE | contact/growth time | OPEN / QUAL | must be calibrated against thickness at fixed composition/thermal condition |
| LPE | growth termination / wipe-off architecture | CANDIDATE-P / CAL | US4592304 gives dedicated CdTe-piece wipe-off well |
| LPE | wipe-off CdTe-piece spacing | CANDIDATE-P / QUAL | patent describes loose unpolished CdTe pieces in vertical slots ~1 mm apart |
| LPE | wipe-off translation speed | OPEN / CAL | not specified; determine by residual-melt vs scratch/damage DOE |
| LPE | residual-melt acceptance | QUAL | define droplet count/area/max size/usable-area thresholds |
| LPE | thickness uniformity measurement | CONTROLLED-QUAL / QUAL | P06 spatial FTIR/full-spectrum mapping plus independent thickness calibration |
| LPE | composition uniformity measurement | CONTROLLED-QUAL / QUAL | P06 separates transmission edge, optical x and detector-response cutoff; production Δx/edge limit open |
| Post-growth | Hg-overpressure anneal architecture | CANDIDATE-P / QUAL | pressure/temperature-controlled Hg-rich annealing is primary-source supported; P04 |
| Post-growth | candidate anneal temperature/time | CANDIDATE-P / QUAL | 250 °C/1 h is a primary-source screening anchor, not RP-01 endpoint |
| Post-growth | supported temperature window | CANDIDATE-P / QUAL | 250–300 °C n-type conversion without apparent composition change reported; ~400 °C composition-change warning |
| Post-growth | Hg partial pressure / chemical potential | PARTIAL / QUAL | broad 0.1–250 Torr primary process range; exact RP-01 state remains open |
| Post-growth | anneal time for RP-01 target | OPEN / QUAL | control by Hall state; kinetics are x-dependent |
| Post-growth | cooldown path | OPEN / QUAL | sample/source cooling trajectory is part of defect-state process |
| Post-growth | final carrier-density target | CLOSED-P / QUAL | historical target 9.8×10^14 cm^-3; P05 must verify local Hall state |
| Post-growth | final mobility target | CLOSED-P / QUAL | historical target 4.0×10^4 cm²/V·s; P05 must verify local Hall state |
| Post-growth | composition-preservation gate | CONTROLLED-QUAL / QUAL | P06 requires matched pre/post optical mapping; numerical allowed shift still open |
| Material metrology | Hall / van der Pauw sequence | CONTROLLED-QUAL | P05 defines geometry checks, current/field reversal, full VdP solution, raw-data retention and field sweep |
| Material metrology | VdP consistency threshold | CONTROLLED-QUAL | ≤3% routine PASS; >3–5% conditional; >5% fail, based on NIST guidance |
| Material metrology | Hall field range | CONTROLLED-QUAL / QUAL | project qualification grid 0, ±0.01, ±0.025, ±0.05, ±0.10, ±0.20, ±0.50 T; RP-01 used variable field up to 2 T for RIE material |
| Material metrology | single-carrier validity | CONTROLLED-QUAL | P05 requires Hall linearity/model check; escalate to multicarrier analysis on curvature/sign changes/MR |
| Material metrology | Hall factor | OPEN / QUAL | report nH/µH until explicit Hall-factor model and uncertainty are justified |
| Material metrology | Hall-contact recipe | OPEN | contact material/process and aging allowance still require closure |
| Material metrology | thickness metrology | CONTROLLED-QUAL / QUAL | P06 fits FTIR fringes/full spectrum and requires cross-calibration to profilometry/cross-section |
| Material metrology | transmission-edge metric | CONTROLLED-QUAL | P06 defines traceable edge descriptor separately from inferred Eg/x and detector cutoff |
| Material metrology | optical composition model | CONTROLLED-QUAL / QUAL | Hougen/full-spectrum lineage selected; implementation/model constants and systematic uncertainty remain to freeze |
| Material metrology | FTIR map density | CONTROLLED-QUAL / QUAL | minimum 9-point map; 5×5 or denser preferred during LPE development; production map density open |
| Material metrology | FTIR instrument method | CONTROLLED-QUAL / CAL | initial ~500–5000 cm^-1, ≤4 cm^-1 qualification method; exact hardware/coadds need freeze/calibration |
| Mask 1 | mesa geometry | OPEN | recover exact detector dimensions |
| Mask 1 | resist identity | OPEN | source search |
| Mask 1 | resist coating/bake | OPEN | source search |
| Mask 1 | exposure/develop | OPEN | source search |
| Mesa etch | process family | CLOSED-P | RP-01 states wet chemical; same UWA lineage explicitly uses bromine/HBr for x≈0.31 PCs |
| Mesa etch | candidate chemistry | CANDIDATE-P | 2% Br2 in 3:1 EG:HBr from x=0.28 study; P01 |
| Mesa etch | concentration basis | OPEN | source does not unambiguously define basis of “2% Br2” |
| Mesa etch | candidate temperature | CANDIDATE-P / QUAL | 21 °C characterized; lower T improves profile; transfer DOE required |
| Mesa etch | etch rate | CANDIDATE-P / QUAL | mean 2.78 µm/min ±26% source variation; must remeasure on x≈0.30 |
| Mesa etch | anisotropy | CANDIDATE-P / QUAL | A≈0.63 ±11% source reference |
| Mesa etch | surface roughness | CANDIDATE-P / QUAL | ~2 nm best-case source result |
| Mesa etch | final isolation depth/overetch | OPEN / QUAL | 9.5 µm film implies through-layer isolation; production overetch not published |
| Mesa etch | undercut/CD acceptance | QUAL | actual-mask/process-capability data required |
| Mesa etch | post-etch rinse/quench | OPEN | must close before release |
| Passivation | film identity | CLOSED-P | anodic oxide |
| Passivation | thickness | CLOSED-P | 800 Å |
| Passivation | candidate electrolyte | CANDIDATE-P | 0.1 M KOH in 90% EG / 10% DI water from independent HgCdTe primary sources |
| Passivation | candidate electrical condition | CANDIDATE-P / QUAL | constant current ~0.30 mA/cm²; ~15 V formation endpoint |
| Passivation | candidate time/temperature | CANDIDATE-P / QUAL | ~2 min for ~800 Å in TI process; transfer qualification required |
| Passivation | solvent-ratio preparation basis | OPEN | 90:10 convention must be explicitly closed |
| Passivation | counter-electrode/fixture | OPEN | source/transfer detail required |
| Passivation | rinse/dry sequence | OPEN | must close before release |
| Passivation | thickness calibration | CAL/QUAL | independent thickness measurement required |
| Passivation | voltage-time signature | QUAL | establish control envelope during transfer DOE |
| Mask 2 | resist thickness | CLOSED-P | ~4–5 µm |
| Mask 2 | prebake | CLOSED-P | 80 °C, 30 min |
| Mask 2 | solvent soak | CLOSED-P | chlorobenzene, 30 min |
| Mask 2 | resist identity | OPEN | source search |
| Mask 2 | exposure/develop | OPEN | source search |
| RIE | reactor class | CLOSED-P | parallel-plate system stated |
| RIE | gas chemistry | CLOSED-P | CH4/5H2 |
| RIE | flow/pressure/RF/time | CLOSED-P | 64 sccm / 100 mTorr / 50 W / 1 min |
| RIE | individual gas calibration | CAL | actual MFCs required |
| RIE | electrode geometry | OPEN/CAL | reactor-specific transfer variable |
| RIE | DC self-bias | OPEN/CAL | reactor-specific transfer variable |
| RIE | sample temperature | OPEN/CAL | reactor-specific transfer variable |
| RIE | oxide-clearing endpoint | QUAL | measure on actual passivation |
| RIE | converted n+ density | CLOSED-P / QUAL | 2.0×10^15 cm^-3 historical target; reproduce on coupon |
| RIE | converted mobility | CLOSED-P / QUAL | 3.3×10^4 cm²/V·s historical target; reproduce on coupon |
| RIE | conversion depth | OPEN | original LBIC source still needs full quantitative extraction |
| Metallization | Cr thickness | CLOSED-P | 300 Å |
| Metallization | Au thickness | CLOSED-P | 2700 Å |
| Metallization | deposition method | OPEN | source search |
| Metallization | base pressure | OPEN/CAL | source plus actual tool qualification |
| Metallization | deposition rates | OPEN/CAL | source plus actual tool qualification |
| Metallization | RIE-to-metal delay | OPEN/QUAL | surface-state sensitive |
| Lift-off | compatible resist profile | PARTIAL | published preparation exists |
| Lift-off | solvent/time/agitation | OPEN | source search |
| Contact QC | TLM geometry | CLOSED-P | nine-contact structure stated |
| Contact QC | contact resistivity target | CLOSED-P | ~9×10^-4 Ω·cm² at 80 K |
| Packaging | die attach | OPEN | paper does not close this |
| Packaging | wire bond | OPEN | paper does not close this |
| DC test | bias/load circuit | OPEN | recover or define controlled circuit |
| Responsivity | source/system class | CLOSED-P | Optronics system stated |
| Responsivity | detector T/FOV/chop | CLOSED-P | 80 K / 60° / 1 kHz |
| Responsivity | optical calibration | OPEN | traceability chain required |
| Noise | analyzer | CLOSED-P | HP35665A stated |
| Noise | low-noise preamp | OPEN | model/gain/noise not stated |
| Noise | bias field/T | CLOSED-P | representative 10 V/cm at 80 K |
| Noise | RBW/ENBW/averaging | OPEN | required for exact reproduction |
| Noise | electronics-floor method | OPEN | required |
| Spectral performance | measured detector cutoff | CLOSED-P | ~4.4 µm; convention must remain detector-response specific |
| Performance | D* condition/result | CLOSED-P | reported BLIP result |
| Performance | independent reproduction equation inputs | PARTIAL | exact active area and full bandwidth/radiometry chain remain open |

## Current controlled modules

- `procedures/P01_WET_MESA_QUALIFICATION.md`
- `procedures/P02_ANODIC_OXIDE_QUALIFICATION.md`
- `procedures/P03_LPE_X030_QUALIFICATION.md`
- `procedures/P04_HG_ANNEAL_QUALIFICATION.md`
- `procedures/P05_HALL_VDP_MATERIAL_METROLOGY.md`
- `procedures/P06_FTIR_COMPOSITION_THICKNESS_MAPPING.md`
- `procedures/P07_CZT_SUBSTRATE_QUALIFICATION.md`

Supporting controlled calculations:

- `calculations/HANSEN_BANDGAP_MODEL.md`
- `calculations/LPE_CHARGE_COMPOSITION_SENSITIVITY.md`

## Release rule

RP-01 cannot be labeled `REPRODUCIBLE-RELEASE` while any variable that materially affects device identity or performance remains `OPEN`. `CAL` and `QUAL` variables may remain apparatus-specific only if the manual contains an explicit calibration/qualification procedure and numerical acceptance rule. `CANDIDATE-P` must become either lineage-confirmed `CLOSED-P` or a statistically qualified local process before production release. `CONTROLLED-QUAL` means the experiment/metrology is now defined well enough to generate defensible data; it does not mean the final manufacturing tolerance has been established.

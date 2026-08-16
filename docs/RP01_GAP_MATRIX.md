# RP-01 process-closure matrix

This file is the working checklist for deciding when RP-01 has enough information to become an executable process traveler.

Status codes:

- `CLOSED-P` — directly closed by published experimental source.
- `CLOSED-D` — closed by a documented derivation from published quantities.
- `CANDIDATE-P` — a primary-source process compatible enough to qualify, but not proven to be the exact RP-01 lineage/process.
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
| Material | incoming carrier density | CLOSED-P | Smith et al. |
| Material | incoming mobility | CLOSED-P | Smith et al. |
| Material | incoming resistivity | CLOSED-D / QUAL | derived consistency value; measured value preferred |
| Substrate | material | CLOSED-P | insulating CdZnTe |
| Substrate | Zn fraction / lattice match | PARTIAL / QUAL | x≈0.30-compatible CdZnTe with a few mol% Zn is primary-source supported; y≈0.04 reported by Tranchart et al., while separate lattice-match work gives ~0.029 for Hg0.7Cd0.3Te; release from measured mismatch, not a universal nominal value |
| Substrate | crystal orientation/miscut | PARTIAL / OPEN | {111} family is strongly supported for Te-rich LPE; exact RP-01 face and permitted miscut still require closure |
| Substrate | thickness/planarity | OPEN | locate source or define qualification |
| Substrate prep | incoming clean | OPEN | same process-lineage source preferred |
| LPE | growth method | CLOSED-P | RP-01 states LPE; x≈0.30 Te-rich horizontal-slider growth is demonstrated in Schmit–Hager–Wood lineage |
| LPE | candidate melt composition | CANDIDATE-P | Bowers–Schmit tie line xL=0.082, yL=0.810, TL=507 °C gives xS=0.29; see P03 |
| LPE | elemental charge fractions | CLOSED-D / QUAL | for the candidate tie line: mole fractions Hg 0.17442, Cd 0.01558, Te 0.81000; derived mass fractions Hg 0.249738, Cd 0.012502, Te 0.737760 |
| LPE | total charge mass / melt depth | OPEN / CAL | must be selected from actual growth-well geometry and depletion behavior; do not combine Radhakrishnan 4.8 g with the Honeywell composition as a published recipe |
| LPE | charge synthesis / homogenization | PARTIAL / QUAL | Radhakrishnan demonstrates 6N elemental sources and 700 °C/8 h evacuated-ampoule synthesis for a different composition; transfer to x≈0.30 must be qualified |
| LPE | furnace/boat architecture | CANDIDATE-P / CAL | covered graphite horizontal slider, separate Hg source, quartz tube, N2 purge/H2 process atmosphere are primary-source anchored; exact dimensions are apparatus-specific |
| LPE | Hg-loss compensation | CANDIDATE-P / CAL | HgTe or HgTe+Te auxiliary vapor source demonstrated by Bowers–Schmit; source mass/area/free-volume capability must be qualified |
| LPE | growth temperature | CANDIDATE-P / QUAL | TL=507 °C tie line; growth near 500 °C is primary-source supported, giving a derived ~7 °C supercooling center point |
| LPE | equilibration | OPEN / QUAL | Harman reports ~1 h at 550 °C in a different process; equilibrium criterion for selected x≈0.30 charge/boat must be established |
| LPE | supercooling/cooling profile | PARTIAL / QUAL | primary source requires heating above liquidus and growth below it; exact ΔT, ramp and cooling trajectory remain to qualify |
| LPE | substrate meltback | CANDIDATE-P / QUAL | Radhakrishnan demonstrates in-situ meltback as an interface-cleaning method; x≈0.30 chemistry/time/removed depth remain open |
| LPE | contact/growth time | OPEN / QUAL | must be calibrated against thickness at fixed composition/thermal condition; literature times are process-specific |
| LPE | growth termination / wipe-off | PARTIAL / CAL | slider translation to separate melt/substrate is primary-source anchored; velocity, geometry and residual-melt control remain open |
| LPE | thickness uniformity metric | OPEN / QUAL | define spatial map, instrument, repeatability and numerical acceptance threshold |
| LPE | composition uniformity metric | OPEN / QUAL | define spatial FTIR/composition map and acceptable x/cutoff spread |
| Post-growth | Hg-overpressure anneal architecture | CANDIDATE-P / QUAL | primary work on x≈0.17–0.30 shows 250–300 °C Hg-overpressure annealing can produce n-type material without the composition change seen near 400 °C |
| Post-growth | anneal time/Hg chemical potential/cooldown | OPEN | full primary method still required before release |
| Post-growth | final carrier-density target | CLOSED-P / QUAL | RP-01 n≈9.8×10^14 cm^-3; anneal must be qualified to reproduce this state |
| Post-growth | final mobility target | CLOSED-P / QUAL | RP-01 µe≈4.0×10^4 cm² V^-1 s^-1; anneal/material process must reproduce it |
| Material metrology | thickness method | OPEN | establish FTIR/profilometry/cross-section procedure |
| Material metrology | x/cutoff mapping | OPEN | define instrument and cutoff convention |
| Material metrology | Hall/Van der Pauw | PARTIAL | paper reports Hall use; full measurement SOP still open |
| Mask 1 | mesa geometry | OPEN | recover exact detector dimensions |
| Mask 1 | resist identity | OPEN | source search |
| Mask 1 | resist coating/bake | OPEN | source search |
| Mask 1 | exposure/develop | OPEN | source search |
| Mesa etch | process family | CLOSED-P | RP-01 states wet chemical; same UWA lineage explicitly uses bromine in HBr for x=0.31 PCs |
| Mesa etch | candidate chemistry | CANDIDATE-P | 2% Br2 in 3:1 EG:HBr from Srivastav et al. x=0.28 study; see procedures/P01_WET_MESA_QUALIFICATION.md |
| Mesa etch | concentration basis | OPEN | paper does not unambiguously define basis of “2% Br2”; release blocker |
| Mesa etch | candidate temperature | CANDIDATE-P / QUAL | 21 °C characterized; lower temperature improves profile; transfer DOE required |
| Mesa etch | etch rate | CANDIDATE-P / QUAL | mean 2.78 µm/min with ±26% variation for source process; must remeasure on x≈0.30 |
| Mesa etch | anisotropy | CANDIDATE-P / QUAL | A≈0.63 ±11% source reference |
| Mesa etch | surface roughness | CANDIDATE-P / QUAL | ~2 nm best-case source result; 2–7 nm reported across conditions |
| Mesa etch | final isolation depth/overetch | OPEN / QUAL | RP-01 9.5 µm film implies through-layer isolation, but production overetch is not published |
| Mesa etch | undercut/CD acceptance | QUAL | requires actual-mask/process-capability data |
| Mesa etch | post-etch rinse/quench | OPEN | must be closed before release |
| Passivation | film identity | CLOSED-P | anodic oxide for experimental devices |
| Passivation | thickness | CLOSED-P | 800 Å |
| Passivation | candidate electrolyte | CANDIDATE-P | 0.1 M KOH in 90% EG / 10% DI water from independent HgCdTe primary sources; exact UWA recipe still unknown |
| Passivation | candidate electrical condition | CANDIDATE-P / QUAL | constant current ~0.30 mA/cm²; ~15 V formation endpoint from TI primary process disclosure |
| Passivation | candidate time/temperature | CANDIDATE-P / QUAL | ~2 min for ~800 Å in TI process; independent work uses room-temperature constant-current anodization |
| Passivation | solvent-ratio preparation basis | OPEN | 90:10 preparation convention must be explicitly closed |
| Passivation | counter-electrode/fixture | OPEN | primary process transfer detail required |
| Passivation | rinse/dry sequence | OPEN | must be closed before release |
| Passivation | thickness calibration | CAL/QUAL | actual anodization apparatus; independent thickness measurement required |
| Passivation | voltage-time signature | QUAL | log every run; establish control envelope during transfer DOE |
| Mask 2 | resist thickness | CLOSED-P | ~4–5 µm |
| Mask 2 | prebake | CLOSED-P | specified by source |
| Mask 2 | solvent soak | CLOSED-P | specified by source |
| Mask 2 | resist identity | OPEN | search source lineage |
| Mask 2 | exposure/develop | OPEN | search source lineage |
| RIE | reactor class | CLOSED-P | parallel-plate system stated |
| RIE | gas chemistry | CLOSED-P | stated |
| RIE | flow/pressure/RF/time | CLOSED-P | stated |
| RIE | individual gas calibration | CAL | actual MFCs required |
| RIE | electrode geometry | OPEN/CAL | reactor-specific transfer variable |
| RIE | DC self-bias | OPEN/CAL | reactor-specific transfer variable |
| RIE | sample temperature | OPEN/CAL | reactor-specific transfer variable |
| RIE | oxide-clearing endpoint | QUAL | derive/measure on actual passivation |
| RIE | converted n+ density | CLOSED-P / QUAL | published target; reproduce on coupon |
| RIE | converted mobility | CLOSED-P / QUAL | published target; reproduce on coupon |
| RIE | conversion depth | OPEN | original cited source must be audited |
| Metallization | Cr thickness | CLOSED-P | stated |
| Metallization | Au thickness | CLOSED-P | stated |
| Metallization | deposition method | OPEN | source search |
| Metallization | base pressure | OPEN/CAL | source plus actual tool qualification |
| Metallization | deposition rates | OPEN/CAL | source plus actual tool qualification |
| Metallization | RIE-to-metal delay | OPEN/QUAL | surface-state sensitive |
| Lift-off | compatible resist profile | PARTIAL | published preparation exists |
| Lift-off | solvent/time/agitation | OPEN | source search |
| Contact QC | TLM geometry | CLOSED-P | nine-contact structure stated |
| Contact QC | contact resistivity target | CLOSED-P | published result |
| Packaging | die attach | OPEN | paper does not close this |
| Packaging | wire bond | OPEN | paper does not close this |
| DC test | bias/load circuit | OPEN | recover or define controlled circuit |
| Responsivity | source/system class | CLOSED-P | Optronics system stated |
| Responsivity | detector T/FOV/chop | CLOSED-P | stated |
| Responsivity | optical calibration | OPEN | traceability chain required |
| Noise | analyzer | CLOSED-P | HP35665A stated |
| Noise | low-noise preamp | OPEN | model/gain/noise not stated |
| Noise | bias field/T | CLOSED-P | stated |
| Noise | RBW/ENBW/averaging | OPEN | required for exact reproduction |
| Noise | electronics-floor method | OPEN | required |
| Spectral performance | measured cutoff | CLOSED-P | 4.4 µm |
| Performance | D* condition/result | CLOSED-P | reported BLIP result |
| Performance | independent reproduction equation inputs | PARTIAL | exact active area/bandwidth chain still open |

## Current controlled qualification modules

- `procedures/P01_WET_MESA_QUALIFICATION.md`
- `procedures/P02_ANODIC_OXIDE_QUALIFICATION.md`
- `procedures/P03_LPE_X030_QUALIFICATION.md`

None is a released production procedure yet. Their release blockers are intentionally explicit.

## Release rule

RP-01 cannot be labeled `REPRODUCIBLE-RELEASE` while any variable that materially affects device identity or performance remains `OPEN`. `CAL` and `QUAL` variables may remain apparatus-specific only if the manual contains an explicit calibration/qualification procedure and numerical acceptance rule. `CANDIDATE-P` must be converted to either a lineage-confirmed `CLOSED-P` or a statistically qualified local process before production release.

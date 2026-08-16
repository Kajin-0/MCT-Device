# RP-01 process-closure matrix

This file is the working checklist for deciding when RP-01 has enough information to become an executable process traveler.

Status codes:

- `CLOSED-P` — directly closed by published experimental source.
- `CLOSED-D` — closed by a documented derivation from published quantities.
- `CAL` — must be calibrated on the actual apparatus.
- `QUAL` — requires a qualification experiment before release.
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
| Substrate | Zn fraction | OPEN | locate supplier/process source |
| Substrate | crystal orientation/miscut | OPEN | locate supplier/process source |
| Substrate | thickness/planarity | OPEN | locate source or define qualification |
| Substrate prep | incoming clean | OPEN | same process-lineage source preferred |
| LPE | growth method | CLOSED-P | LPE, but supplier recipe unknown |
| LPE | melt composition | OPEN | identify x≈0.30 compatible primary process |
| LPE | furnace/boat geometry | OPEN | evaluate Tung/Harman/Radhakrishnan lineage |
| LPE | growth temperature | OPEN | same |
| LPE | equilibration | OPEN | same |
| LPE | supercooling/cooling profile | OPEN | same |
| LPE | contact/growth time | OPEN | same |
| LPE | Hg-loss compensation | OPEN | determine compatible method |
| LPE | thickness uniformity metric | OPEN | define map and acceptance threshold |
| Post-growth | Hg stoichiometry anneal | OPEN | composition/electrical-state matched source needed |
| Material metrology | thickness method | OPEN | establish FTIR/profilometry/cross-section procedure |
| Material metrology | x/cutoff mapping | OPEN | define instrument and cutoff convention |
| Material metrology | Hall/Van der Pauw | PARTIAL | paper reports Hall use; full measurement SOP still open |
| Mask 1 | mesa geometry | OPEN | recover exact detector dimensions |
| Mask 1 | resist identity | OPEN | source search |
| Mask 1 | resist coating/bake | OPEN | source search |
| Mask 1 | exposure/develop | OPEN | source search |
| Mesa etch | chemistry | OPEN | highest-priority process gap |
| Mesa etch | concentration/temperature | OPEN | highest-priority process gap |
| Mesa etch | etch rate/depth | OPEN | highest-priority process gap |
| Mesa etch | undercut/CD acceptance | QUAL | requires actual-mask/tool data |
| Passivation | film identity | CLOSED-P | anodic oxide for experimental devices |
| Passivation | thickness | CLOSED-P | 800 Å |
| Passivation | electrolyte | OPEN | search UWA/Faraone lineage |
| Passivation | electrical growth condition | OPEN | search UWA/Faraone lineage |
| Passivation | time/temperature | OPEN | search UWA/Faraone lineage |
| Passivation | thickness calibration | CAL/QUAL | actual anodization apparatus |
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

## Release rule

RP-01 cannot be labeled `REPRODUCIBLE-RELEASE` while any variable that materially affects device identity or performance remains `OPEN`. `CAL` and `QUAL` variables may remain apparatus-specific only if the manual contains an explicit calibration/qualification procedure and numerical acceptance rule.

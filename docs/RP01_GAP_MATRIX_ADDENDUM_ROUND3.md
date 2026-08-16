# RP-01 gap-matrix addendum — source-recovery round 3

**Date:** 2026-08-15 America/New_York  
**Precedence:** For the rows below, this addendum supersedes older entries in `docs/RP01_GAP_MATRIX.md` until that large matrix is safely regenerated.

## P01 wet mesa — updated closure state

| Variable | Updated status | Evidence / next action |
|---|---|---|
| near-composition source material | CLOSED-P / TRANSFER | Srivastav et al. 2005 directly uses x=0.28 HgCdTe |
| source sample preparation | CLOSED-P / TRANSFER | wire-saw dice, sapphire mounting, mechanical lapping/polishing, chemomechanical polishing, then nominal 0.1% Br2/methanol free etch for 1 min before test-pattern work |
| test geometry | CLOSED-P / TRANSFER | ~600-µm linear structures with 50-µm trenches; 2-D mesas with 30-µm trenches |
| etchant family | CLOSED-P / TRANSFER | Br2/HBr/ethylene glycol |
| nominal optimum composition | CANDIDATE-P | source selects nominal 2% Br2 in 3:1 EG:HBr |
| Br2 percentage basis | **OPEN — confirmed genuine source omission** | full accessible primary text still does not define w/v, v/v, wt%, mol%, or preparation quantities; do not infer |
| room-temperature reference rate | CANDIDATE-P / QUAL | ~2.78 µm/min at 21 °C, with ~±26% source variation |
| anisotropy | CANDIDATE-P / QUAL | A≈0.63 ±11% source reference |
| roughness | CANDIDATE-P / QUAL | ~2–7 nm RMS, best ~2 nm in high-EG condition |
| activation energy / T sensitivity | CLOSED-P / TRANSFER | ~7.5 kcal/mol; rate approximately doubles per +10 °C over investigated range |
| bath age / Br2 loss | CONTROLLED-QUAL | Br2 evaporation is explicitly identified as a reproducibility mechanism; solution age, vessel state, exposed area, temperature and use history must be logged |
| vertical-depth metrology | CLOSED-P / TRANSFER | source uses Dektak profilometry |
| lateral-undercut metrology | CLOSED-P / TRANSFER | source uses high-magnification phase-contrast microscopy |
| RP-01 through-layer timed-etch estimate | CLOSED-D / NOT A RECIPE | 9.5 µm / 2.78 µm/min ≈ 3.42 min; source ±26% rate span implies ~2.71–4.62 min. Demonstrates that fixed time alone is insufficient |
| production endpoint/overetch | OPEN / QUAL | must be established from local x≈0.30 rate, through-layer isolation, CdZnTe interaction and CD/undercut capability |
| final rinse/quench | OPEN | source recovery still needed or local process must be explicitly qualified |

Procedure addendum: `procedures/P01A_SRIVASTAV_PRIMARY_EXPERIMENTAL_ADDENDUM.md`.

## P02 native anodic oxide — updated closure state

| Variable | Updated status | Evidence / next action |
|---|---|---|
| RP-01 oxide identity | CLOSED-P | native anodic oxide |
| RP-01 oxide thickness | CLOSED-P | 800 Å = 80 nm |
| exact UWA local anodization traveler | OPEN | same-team passivation/contact papers identified, but publicly indexed text still does not disclose electrolyte/current/endpoint/rinse |
| TI executable transfer family | CANDIDATE-P / DIRECT PROCESS DISCLOSURE | 0.1 M KOH in 90% EG/10% DI water; constant current ~0.3 mA/cm²; ~15 V endpoint; ~2 min; ~800 Å oxide |
| independent x≈0.20 experimental support | CANDIDATE-P | room-temperature constant current ~0.2–0.5 mA/cm² in 0.1 M KOH / 90% EG / 10% water |
| composition-matched x=0.30 mechanistic lineage | **PRIMARY-LINEAGE CLOSED** | Janousek & Carscallen, J. Appl. Phys. 53, 1720–1726 (1982), plus same-author Hg0.70Cd0.30Te anodic-oxidation paper, directly establish dissolution–precipitation initial growth and electrochemical/mass-transport control |
| x=0.30 detailed electrolyte / pre-etch | SECONDARY-A explicitly attributed to primary | Talasek's technical synthesis attributes n-type slush-grown x=0.30 experiment to Janousek/Carscallen: extensive nominal 5% Br2/methanol etch (~20 µm removed), 0.1 N KOH in 90% EG/10% water, constant-current voltage–time measurements |
| x=0.30 current-density labels | OPEN | archived Figure 26 labels are not legible enough to recover trustworthy numerical current densities; do not reconstruct |
| induction time `t_ind` | CONTROLLED-QUAL | composition-matched lineage shows a current/mass-transport-dependent induction period; log and use as a surface/chemistry diagnostic |
| agitation | CONTROLLED-QUAL | stirring can suppress oxide formation at low current density; stirred/unstirred state, geometry and rate must be explicit |
| bath pH / KOH concentration | CONTROLLED-QUAL | primary mechanism shows pH/oxide solubility strongly affects dissolution/passivation transition |
| voltage–time trace | CONTROLLED-QUAL | mandatory per-run record; endpoint cannot be treated as elapsed time alone |
| integrated charge/area | CONTROLLED-QUAL | calculate `Q/A = ∫J dt` during transfer qualification |
| final oxide thickness | CLOSED-P target / CAL | 80-nm RP-01 target; verify independently on actual apparatus |
| rinse/dry / clean-to-next-step | OPEN | still a release blocker |
| interface/noise acceptance | QUAL | correlate oxide process with electrical state, RIE opening compatibility and final 1/f noise |

Procedure addenda:

- `procedures/P02A_ANODIC_OXIDE_LINEAGE_ADDENDUM.md`
- `procedures/P02B_X030_ANODIZATION_LINEAGE_ADDENDUM.md`

## P08 RIE — updated closure state

| Variable | Updated status | Evidence / next action |
|---|---|---|
| gas notation | CLOSED-P | RP-01 prints CH4/5H2 |
| total flow | CLOSED-P | 64 sccm |
| pressure / RF / time | CLOSED-P | 100 mTorr / 50 W / 60 s |
| CH4:H2 ratio | CANDIDATE-SECONDARY / SAME-LINEAGE | later HgCdTe RIE review explicitly gives 1:5 for relevant UWA RF-parallel-plate branch |
| conditional individual flows | CLOSED-D / NOT PRIMARY | if 1:5 applies to RP-01 total: CH4 10.6667 sccm, H2 53.3333 sccm |
| primary individual MFC confirmation | OPEN | still required before historical recipe can be called closed |
| reported converted volume density | CLOSED-P but DEPTH-COUPLED | ~2.0×10^15 cm^-3, explicitly averaged over RIE-converted thickness |
| reported mobility | CLOSED-P / QUAL | ~3.3×10^4 cm²/V·s |
| historical conversion depth | PARTIAL / OPEN | ~8 µm cited from prior UWA n-type work under similar conditions; exact matched plasma parameters still not recovered |
| conditional sheet density scale | CLOSED-D / CONDITIONAL | if d_conv=8 µm, Ns≈1.6×10^12 cm^-2; if full 9.5 µm, ≈1.9×10^12 cm^-2 |
| proper transport qualification state | CONTROLLED-QUAL | qualify `{R_sheet/Ns, µ_H or multicarrier state, d_conv, L_conv, d_etch, rho_c}` rather than n_vol alone |
| multilayer Hall validity | CONTROLLED-QUAL | surface converted layer + underlying conducting epilayer may require variable-field / multilayer / mobility-spectrum treatment |

Procedure addenda:

- `procedures/P08A_RIE_GAS_RATIO_PROVENANCE_ADDENDUM.md`
- `procedures/P08B_RIE_HALL_DEPTH_COUPLING_ADDENDUM.md`

## P13 temporal response — updated closure state

| Variable | Updated status | Evidence / next action |
|---|---|---|
| same-lab x≈0.30 transient-decay methodology | PRIMARY-THESIS / SAME-LAB | 1998 UWA thesis supervised by John Dell with Redfern/Smith assistance uses n-type x≈0.30 HgCdTe near 77 K under vacuum |
| low-field lifetime condition | CONTROLLED-QUAL | thesis explicitly keeps bias small to avoid sweeping excess carriers into high-recombination contact regions |
| lifetime naming | CONTROLLED-QUAL | use tau_eff unless low-injection, low-field and physical-model conditions justify bulk lifetime |
| bias-dependence test | CONTROLLED-QUAL | demonstrate transient stability to further bias reduction before bulk-lifetime interpretation; study higher-field sweepout separately |

Procedure addendum: `procedures/P13A_UWA_TRANSIENT_DECAY_LINEAGE_ADDENDUM.md`.

## Immediate highest-priority unresolved items

1. exact Br2 percentage basis in P01 or an explicitly new local formulation;
2. exact UWA anodization recipe, especially rinse/dry and cell/electrode details;
3. primary full-text Janousek/Carscallen current-density/cell parameters if obtainable;
4. primary confirmation of RP-01 CH4:H2 split;
5. exact Musca-1998 plasma conditions tied to ~8-µm conversion depth;
6. historical Cr/Au deposition base pressure/rates and RIE-to-metal delay;
7. exact photoresist/exposure/developer for both masks;
8. upstream x≈0.30 LPE thickness-time relation and final anneal state.

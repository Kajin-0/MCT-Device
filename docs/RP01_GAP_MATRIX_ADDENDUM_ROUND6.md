# RP-01 gap-matrix addendum — source-recovery round 6

**Date:** 2026-08-15 America/New_York

This addendum overrides older RIE rows where the newer P08C/P08D/P08E evidence is more specific.

| Module | Variable / evidence required | Current status | Round-6 interpretation |
|---|---|---|---|
| RIE | individual CH4/H2 ratio | PARTIAL / QUAL | Secondary same-lineage review supports CH4:H2=1:5; direct RP-01 individual MFC values remain open. Conditional 64-sccm split is 10.6667/53.3333 sccm, derived only. |
| RIE | Plasma Technology reactor model | OPEN | Public RP-01 text says parallel-plate Plasma Technology reactor but no model recovered. |
| RIE | RF frequency | OPEN / CAL | Not recovered historically; must be recorded locally for transfer. |
| RIE | powered-electrode area | OPEN / CAL | 125-cm² algebraic inference from 50 W / 0.4 W cm^-2 is rejected because same reactor/area definition is unproven. |
| RIE | electrode spacing/sample placement | OPEN / CAL | Required by P08D. |
| RIE | DC self-bias / ion-energy proxy | OPEN / CAL | Required measured transfer coordinate; absolute forward power alone is insufficient. |
| RIE | sample temperature | OPEN / CAL | Required by P08D; no equivalence claim permitted with unknown thermal state. |
| RIE | chamber conditioning/history | CONTROLLED-QUAL | P08D requires clean/season/history logging and repeatability correlation. |
| RIE | oxide-clear time | CONTROLLED-QUAL | P08/P08D require split-time calibration on actual ~80-nm oxide; not assumed equal to 60-s total time. |
| RIE | physical HgCdTe recession | CONTROLLED-QUAL | Must be measured independently from conversion depth. |
| RIE | conversion depth | PARTIAL / CONTROLLED-QUAL | RP-01 cites ~8 µm from prior n-type work under similar conditions, but exact process condition remains unrecovered. P08D requires local LBIC/destructive correlation. |
| RIE | lateral conversion | CONTROLLED-QUAL | Required spatial output from LBIC; use P08C method lineage. |
| RIE | LBIC depth-model dependencies | CONTROLLED-QUAL | Musca et al. 1999 shows sensitivity to doping, illumination wavelength/direction and test geometry; model inputs/version must be retained. |
| RIE | p-type 410-mTorr depth reference | CLOSED-P / NONTRANSFER | Siliquini 1997: 410 mTorr, CH4/H2, 0.4 W/cm², ~0.2-µm physical etch, ~1.5-µm electrical conversion. Direct method benchmark only. |
| RIE | p-type arsenic branch pressure | CLOSED-P / NONTRANSFER | UWA institutional record gives 340 mTorr at 0.4 W/cm². Secondary 390-mTorr records are flagged as transcription discrepancy. |
| RIE transport | uniform one-layer model | CONDITIONAL | No longer default. Same-UWA QMSA/differential Hall work demonstrates damaged surface electron sheet + deeper high-mobility converted region. |
| RIE transport | surface sheet channel | CONTROLLED-QUAL | P08E requires testing for separate surface sheet density/mobility instead of assigning arbitrary thickness. |
| RIE transport | deeper converted region | CONTROLLED-QUAL | Report deeper carrier density/profile and mobility only after multicarrier model/depth support. |
| RIE transport | volumetric n+ target | PARTIAL / QUAL | Historical ~2.0×10^15 cm^-3 is averaged over converted thickness and is not independent of d_conv. Use sheet/multicarrier quantities first. |
| RIE transport | RP-01 conditional sheet scale | CLOSED-D / NONRELEASE | If n_avg=2×10^15 cm^-3 over 8 µm, Ns≈1.6×10^12 cm^-2; conditional consistency value only. |
| RIE/contact | final process acceptance | CONTROLLED-QUAL | P08D/P08E require multivariate vector including t_clear, d_etch, transport decomposition, d_conv, L_conv, TLM rho_c and detector/noise impact. |
| RIE-to-metal | in-situ archival bridge | PARTIAL / OPEN | Smith et al. 2000 SIMC-XI source identified; public record remains metadata-only. |

## Round-6 control rule

A transferred RIE process may not be declared equivalent because it matches `64 sccm / 100 mTorr / 50 W / 60 s` alone.

The local qualification must additionally close or measure:

`{gas split, RF frequency, electrode geometry, self-bias/ion-energy proxy, sample T, t_clear, d_etch, multicarrier transport, d_conv, L_conv, rho_c}`.

## Procedures governing these rows

- `P08_RIE_BLOCKING_CONTACT_QUALIFICATION.md`
- `P08A_RIE_GAS_RATIO_PROVENANCE_ADDENDUM.md`
- `P08B_RIE_HALL_DEPTH_COUPLING_ADDENDUM.md`
- `P08C_UWA_LBIC_CONVERSION_METHOD_LINEAGE.md`
- `P08D_RIE_REACTOR_EQUIVALENCE_DEPTH_QUALIFICATION.md`
- `P08E_RIE_MULTICARRIER_TRANSPORT_QUALIFICATION.md`

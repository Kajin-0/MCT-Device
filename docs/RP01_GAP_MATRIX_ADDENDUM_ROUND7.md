# RP-01 gap-matrix addendum — source-recovery round 7

**Date:** 2026-08-15 America/New_York

This addendum records the sidewall-passivation and blocking-contact functional overrides introduced after round 6.

| Module | Variable / evidence required | Current status | Round-7 interpretation |
|---|---|---|---|
| Passivation | planar oxide thickness | CLOSED-P / QUAL | Historical target remains ~800 Å; planar witness alone no longer sufficient for process release. |
| Passivation | mesa sidewall coverage | CONTROLLED-QUAL | P02C requires sidewall-sensitive physical or electrical qualification because same-UWA photoconductor work shows unpassivated sidewalls can materially reduce responsivity. |
| Passivation | perimeter sensitivity | CONTROLLED-QUAL | During development compare multiple measured P/A values; responsivity/noise/lifetime/leakage should not show significant residual perimeter-driven degradation within released geometry. |
| Passivation | coupling to P01 mesa profile | CONTROLLED-QUAL | Requalify sidewall passivation if wet-etch sidewall angle, undercut, roughness, depth or surface chemistry changes materially. |
| RIE/contact | TLM contact resistivity | CLOSED-P / QUAL | Historical ~9×10^-4 Ω·cm² at 80 K remains majority-carrier contact benchmark. |
| RIE/contact | minority-carrier contact recombination | OPEN / CONTROLLED-QUAL | RP-01 does not publish contact recombination velocity. P08F/P08G require detector-level sweepout/responsivity/noise/temporal validation rather than inferring minority-carrier blocking from TLM. |
| RIE/contact | functional sweepout suppression | CONTROLLED-QUAL | Measure responsivity versus field with P10 thermal controls; compare normalized response `S_R(E)=R(E)/R(E_ref)`. |
| RIE/contact | noise consequence | CONTROLLED-QUAL | P12 noise/NEP/D* must remain acceptable across the same field range; increased responsivity alone is not sufficient. |
| RIE/contact | bandwidth consequence | CONTROLLED-QUAL | Blocking can increase effective lifetime and lower rolloff frequency; P13 bandwidth/time response is part of contact optimization. |
| RIE/contact | contact-recombination velocity S_c | OPEN / MODEL-QUAL | Historical predecessor contacts show few-hundred-cm/s scales; RP-01 S_c not published. May only be inferred through validated spatial transport modeling plus field/responsivity/time data. |
| RIE/contact | predecessor technology identity | CLOSED-CONCEPT | Blocking contact is a functional concept, not one fabrication method. Accumulation, heterojunction, and RIE n+/n implementations are distinct. |
| RIE/contact | older n+ array formation method | OPEN / NONCRITICAL | 1996 UWA 3×3 arrays used n+ blocking contacts and achieved BLIP at 80 K, but accessible source does not state how n+ was formed. Do not infer RIE. |
| RIE/contact | 2000 2-D model n+ parameters | CLOSED-P / MODEL-ONLY | n+=1×10^16 cm^-3 and depth=3 µm are model-fit values for another practical MWIR detector, not RP-01 measured targets. |
| Detector optimization | contact objective | CONTROLLED-QUAL | Multi-objective gate now includes `rho_c`, sweepout suppression, detector-referred noise, D*/NEP, optical loss, temporal response, transport decomposition, and stability. |

## Round-7 release rule

A locally transferred blocking-contact process cannot be released solely because it reproduces the historical TLM specific contact resistivity or a nominal Hall density.

It must demonstrate the coupled detector outcome:

`contact process -> transport/depth -> low minority-carrier loss -> responsivity-vs-field -> noise/NEP/D* -> bandwidth/stability`.

## Governing files

- `procedures/P02C_MESA_SIDEWALL_PASSIVATION_QUALIFICATION.md`
- `procedures/P08F_BLOCKING_CONTACT_SWEEPOUT_FUNCTIONAL_QUALIFICATION.md`
- `procedures/P08G_BLOCKING_CONTACT_PREDECESSOR_TECHNOLOGIES.md`
- P08 through P08E
- P10/P11/P12/P13

# RP-01 gap matrix addendum — Round 28

**Topic:** spectral responsivity / Optronics apparatus / blackbody background / FOV / D* optical conventions

Status codes:

- `CLOSED-DIRECT`
- `CLOSED-SAME-UWA`
- `TRANSFER-CLOSED`
- `INFERRED-CONSISTENCY`
- `OPEN-HISTORICAL`
- `QUAL-LOCAL`

---

| Coordinate / question | Status after Round 28 | Evidence / control action |
|---|---|---|
| Spectral-response system manufacturer | `CLOSED-DIRECT` | Optronics Laboratories stated by RP-01 |
| Exact Optronics model | `OPEN-HISTORICAL` | Do not assign OL-735D from 1989 lead |
| Same-UWA Optronics lineage before RP-01 | `CLOSED-SAME-UWA` | Parish et al. 1997 uses Optronics Spectral Response Measurement System |
| Chopping frequency | `CLOSED-DIRECT` | 1 kHz |
| Detector temperature | `CLOSED-DIRECT` | 80 K |
| Spectral-response electric field | `CLOSED-DIRECT` | 10 V/cm |
| Single-wavelength responsivity point | `CLOSED-DIRECT` | 4 µm versus field |
| Stated FOV | `CLOSED-DIRECT` | 60° |
| 60° full-angle vs half-angle wording | `INFERRED-CONSISTENCY / OPEN-HISTORICAL` | 30° half-angle interpretation reproduces quoted background flux approximately; documentary proof absent |
| Physical aperture dimensions | `OPEN-HISTORICAL` | Measure/release local geometry; do not back-solve historical dimensions |
| Blackbody temperature for quoted flux | `CLOSED-DIRECT` | 300 K stated background |
| Quoted photon flux | `CLOSED-DIRECT` | ~1e15 photons cm^-2 s^-1 |
| Radiance temperature calibration | `OPEN-HISTORICAL / QUAL-LOCAL` | local system must use calibrated radiance, not contact T alone |
| Blackbody emissivity | `OPEN-HISTORICAL / QUAL-LOCAL` | measure/source traceably |
| Exact view factor | `OPEN-HISTORICAL / QUAL-LOCAL` | local geometry uses exact aperture/view-factor calculation |
| Diffraction correction | `OPEN-HISTORICAL / QUAL-LOCAL` | required where aperture scale makes it material |
| Spectral source | `OPEN-HISTORICAL` | unrecovered |
| Monochromator model | `OPEN-HISTORICAL` | OL-735D remains a quarantined lead only |
| Grating / slit settings | `OPEN-HISTORICAL` | unrecovered |
| Spectral bandpass / line shape | `OPEN-HISTORICAL / QUAL-LOCAL` | must be measured for new system |
| Wavelength calibration method | `OPEN-HISTORICAL / QUAL-LOCAL` | local traceable calibration required |
| Order-sorting filters | `OPEN-HISTORICAL / QUAL-LOCAL` | local stray-light validation required |
| Reference detector | `OPEN-HISTORICAL / QUAL-LOCAL` | local calibrated transfer detector required |
| Absolute calibration scale | `OPEN-HISTORICAL / TRANSFER-CLOSED` | modern comparator/blackbody methods controlled by P11/P11A |
| Chopper duty/waveform | `OPEN-HISTORICAL / QUAL-LOCAL` | must be recorded |
| Lock-in/preamp responsivity chain | `OPEN-HISTORICAL / QUAL-LOCAL` | exact gain/amplitude convention required |
| RMS/peak/fundamental convention | `OPEN-HISTORICAL / QUAL-LOCAL` | cannot compare absolute V/W without it |
| Beam diameter/profile | `OPEN-HISTORICAL / QUAL-LOCAL` | needed because PC HgCdTe nonlinearity can depend on irradiance |
| Detector optical active area | `OPEN-HISTORICAL / QUAL-LOCAL` | measure same area convention used for D* |
| Window/filter transmission | `OPEN-HISTORICAL / QUAL-LOCAL` | P33/P11A handoff |
| Irradiance linearity | `QUAL-LOCAL` | primary HgCdTe evidence requires test at actual beam/background state |
| Background-dependent responsivity drift | `QUAL-LOCAL` | monitor in calibration sequence |
| Historical cutoff definition for 4.4 µm | `OPEN-HISTORICAL` | new work reports explicit lambda50/lambda10/tangent/etc. |
| RP-01 QE ~70% definition/extraction | `OPEN-HISTORICAL` | preserve as quoted detector parameter; do not infer naively from PC voltage responsivity |
| BLIP D* at 4 µm | `CLOSED-DIRECT` | ~2e11 cm Hz^1/2 W^-1 |
| Exact area/noise convention used in historical D* | `OPEN-HISTORICAL` | recompute locally from matched P11/P12 state |
| Same FOV/background for responsivity and noise | `QUAL-LOCAL` | mandatory P11A/P12 consistency gate |

---

# Highest-value unresolved historical items

1. exact Optronics Laboratories system model/configuration;
2. Optronics source / monochromator / gratings / slits;
3. reference detector and absolute calibration chain;
4. physical aperture/cold-shield geometry producing 60° FOV;
5. window/filter transmission;
6. chopper duty/waveform and signal-amplitude convention;
7. responsivity preamplifier/lock-in chain;
8. optical active-area definition;
9. cutoff definition used for 4.4 µm;
10. area/noise/background conventions used to calculate the historical D*.

---

# What is now executable despite those gaps

A competent laboratory can now perform a traceable RP-01-comparison measurement by using:

- P11 as the canonical spectral-radiometry SOP;
- P11A for UWA-lineage provenance, FOV/background closure and irradiance-linearity controls;
- the P11A qualification register;
- P33 for package/window/thermal state;
- P10 for active electric field/self-heating;
- P12 for matched-background noise and D*.

This constitutes **transfer reproducibility**, not literal reconstruction of the historical UWA optical bench.

# RP-01 gap-matrix addendum — round 17 empirical blocking contacts

**Date:** 2026-08-16 America/New_York

**Purpose:** Record exactly which blocking-contact fabrication/measurement quantities were closed by literature recovery and which remain unresolved after P24.

---

# 1. Gap-status legend

- `CLOSED-DIRECT`: direct canonical RP-01 value recovered.
- `CLOSED-SAME-LINEAGE`: experimentally reported by the same UWA lineage but not proven identical to the canonical RP-01 run.
- `TRANSFER`: experimental evidence from a related HgCdTe branch; useful for method/factor priority only.
- `MODEL-ONLY`: published simulation/model parameter, not measured process output.
- `LOCAL-QUAL`: historical value missing or nontransferable; local qualification route defined.
- `OPEN`: neither historical closure nor sufficient local evidence exists.

---

# 2. Reactor/process gaps

| Item | Round-17 status | Current evidence / action |
|---|---|---|
| reactor family | `CLOSED-DIRECT` | Plasma Technology parallel-plate RIE |
| reactor exact model | `OPEN` | search source/thesis/equipment records |
| gas notation | `CLOSED-DIRECT` | `CH4/5H2` |
| total flow | `CLOSED-DIRECT` | 64 sccm |
| exact CH4 historical flow | `OPEN` | same-lineage 1:5 interpretation only; local MFC split must be explicit |
| exact H2 historical flow | `OPEN` | same restriction |
| pressure | `CLOSED-DIRECT` | 100 mTorr |
| RF power | `CLOSED-DIRECT` | 50 W |
| RF exposure | `CLOSED-DIRECT` | 60 s |
| RF frequency | `OPEN` | local reactor record mandatory |
| powered-electrode area | `OPEN` | rejected 125-cm² inference remains rejected |
| electrode spacing | `OPEN` | local reactor record mandatory |
| historical self-bias | `OPEN` | local self-bias/ion-energy proxy mandatory |
| historical sample temperature | `OPEN` | later empirical work makes sample temperature high priority |
| chamber clean/season | `OPEN` | local qualification mandatory |
| gas stabilization time | `OPEN` | local qualification mandatory |
| historical base pressure | `OPEN` | local qualification mandatory |

---

# 3. Oxide / physical etch gaps

| Item | status | Evidence / action |
|---|---|---|
| anodic oxide thickness | `CLOSED-DIRECT` | ~800 Å / 80 nm |
| RIE intended to clear oxide + create n+ in one step | `CLOSED-DIRECT` | canonical process architecture |
| exact oxide-clear time in 60-s run | `OPEN` | dedicated local time series required |
| canonical physical HgCdTe recession | `OPEN` | measure locally; do not infer from conversion depth |
| surface roughness/morphology after canonical RIE | `OPEN` | local AFM/optical/profilometry output |

Transferred x=.31 evidence demonstrates ~0.2-µm physical etch can coexist with ~1.5-µm electrical conversion, so `d_etch != d_conv` is experimentally closed as a general process warning.

---

# 4. Converted-region transport/depth gaps

| Item | status | Evidence / action |
|---|---|---|
| average converted n | `CLOSED-DIRECT` | ~2.0×10^15 cm^-3 over converted thickness |
| converted mobility | `CLOSED-DIRECT` | ~3.3×10^4 cm²/V/s |
| Hall temperatures | `CLOSED-DIRECT` | 80 K and 300 K |
| variable B extent | `CLOSED-DIRECT` | to 2 T |
| exact canonical d_conv | `OPEN` | RP-01 cites prior similar-condition ~8 µm, not exact canonical depth |
| ~8-µm depth existence in n-type same-lineage process | `CLOSED-SAME-LINEAGE` | retain separate from canonical average n |
| canonical n(z) profile | `OPEN` | LBIC/model/destructive correlation needed |
| canonical lateral conversion L_conv | `OPEN` | LBIC map required |
| canonical sheet density N_s | `OPEN` as direct value | may be derived only conditionally after matched d_conv |
| Hall-factor-corrected physical carrier density | `OPEN/LOCAL-QUAL` | P05 model required |
| multicarrier transport decomposition | `LOCAL-QUAL` | variable-field P05/QMSA when necessary |

---

# 5. LBIC metrology gaps

| Item | status | Evidence / action |
|---|---|---|
| RP-01 LBIC test square | `CLOSED-DIRECT` | 300×300 µm |
| laser wavelength | `CLOSED-DIRECT` | 1.047 µm Nd:YLF |
| illumination mode | `CLOSED-DIRECT` | CW |
| irradiance | `CLOSED-DIRECT` | ~400 mW/cm² |
| LBIC temperature | `CLOSED-DIRECT` | 80 K |
| historical spot diameter/NA | `OPEN` | recover if possible; local instrument records mandatory |
| historical scan step/speed | `OPEN` | local sampling chosen from junction-resolution need |
| exact RP-01 depth inversion model | `OPEN` | same-lineage 1999 quantitative method provides transfer basis |

---

# 6. Metallization/contact gaps

| Item | status | Evidence / action |
|---|---|---|
| Cr thickness | `CLOSED-DIRECT` | 30 nm |
| Au thickness | `CLOSED-DIRECT` | 270 nm |
| TLM pad size | `CLOSED-DIRECT` | 300×300 µm |
| TLM gap sequence | `CLOSED-DIRECT` | 50–400 µm in 50-µm steps |
| rho_c at 80 K | `CLOSED-DIRECT` | ~9×10^-4 Ω·cm² |
| historical deposition method/rate | `OPEN` | P09A local transfer |
| historical base pressure | `OPEN` | P09A local transfer |
| historical RIE-to-metal delay | `OPEN` | now mandatory local variable |
| minority-carrier effective S_c | `OPEN` | cannot infer from TLM |
| exact contact optical loss | `OPEN` | local device/spectral comparison |

---

# 7. Detector functional gaps

| Item | status | Evidence / action |
|---|---|---|
| 80-K detector operation | `CLOSED-DIRECT` | canonical |
| 1-kHz spectral response | `CLOSED-DIRECT` | canonical |
| responsivity field comparison near 4 µm | `CLOSED-DIRECT` | Optronics system |
| 10-V/cm noise benchmark | `CLOSED-DIRECT` | canonical |
| ~3-kHz 1/f knee | `CLOSED-DIRECT` | canonical |
| ~24.5-nV/√Hz g-r plateau | `CLOSED-DIRECT` | high-frequency level, not 1-kHz substitute |
| ~4.4-µm cutoff | `CLOSED-DIRECT` | cutoff convention still not fully reconstructed |
| D* ~2e11 at 4 µm | `CLOSED-DIRECT` | canonical historical comparison |
| QE ~70% | `CLOSED-DIRECT` | canonical historical quote |
| exact typical-device contact gap | `OPEN` | figures use same device but pair/gap not uniquely recovered |
| matched control effect size for RIE vs conventional | `PARTIAL` | published comparison uses different starting wafer densities |
| quantitative R(E) rolloff acceptance | `LOCAL-QUAL` | derive from detector/system requirement |
| contact-related noise increment | `OPEN/LOCAL-QUAL` | matched process split required |
| contact effect on tau/f3dB | `OPEN/LOCAL-QUAL` | P13 de-embedded measurement |
| detector-level optimum d_conv/n+ state | `OPEN` | authors explicitly state process not optimized |

---

# 8. Stability/thermal-budget gaps

| Item | status | Evidence / action |
|---|---|---|
| RP-01 immediate post-RIE stability | `OPEN` | no canonical time series recovered |
| RP-01 room-temperature shelf stability | `OPEN` | local study mandatory |
| RP-01 allowed later bake | `OPEN` | do not invent thermal budget |
| thermal reversibility of RIE conversion in HgCdTe | `TRANSFER-CLOSED` | x=.31 p-type branch: 200 °C/17 h Hg anneal erased RIE conversion |
| room-temperature relaxation exists in other RIE HgCdTe | `TRANSFER-CLOSED` | x=.21 branch: sigma(77K) < half after ~2e5 s RT storage |
| accelerated relaxation near 323 K in that branch | `TRANSFER-CLOSED` | ~5× faster |

Round-17 rule:

**post-RIE elapsed time, storage temperature/ambient and every subsequent thermal exposure are process variables until local stability is demonstrated.**

---

# 9. Process-factor priority gaps

Later x=.30 ICPRIE experiments report that converted-layer transport/depth are most sensitive to pressure and temperature, with RIE and ICP power also significant.

For RP-01 local transfer this produces the evidence-weighted sequence:

1. close actual sample temperature;
2. close pressure control/uncertainty;
3. separate oxide-clear time from semiconductor plasma exposure;
4. close self-bias/ion-energy proxy and RF transfer;
5. then refine gas ratio.

Absolute perturbation sizes remain `LOCAL-QUAL`.

---

# 10. Highest-value next source-recovery targets

Before adding more blocking-contact theory, search for:

1. full journal PDF or thesis record connecting the n-type ~8-µm conversion directly to its exact plasma condition;
2. UWA theses by Smith/Siliquini/Musca/Winchester that may contain:
   - reactor model;
   - RF frequency;
   - electrode area/spacing;
   - self-bias;
   - sample temperature;
   - individual gas flows;
   - LBIC spot/scan settings;
   - actual n+(z) / lateral-conversion plots;
3. RIE dose/pressure/temperature matrices for n-type MWIR material, not only p-type type-conversion studies;
4. post-RIE aging/storage measurements in n-type x≈.30 material;
5. process-to-detector matched experiments relating n+ depth/density to R(E), D* and bandwidth.

If direct records remain unavailable, P24 provides the local empirical closure route.

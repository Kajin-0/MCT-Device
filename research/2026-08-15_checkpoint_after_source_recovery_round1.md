# Recovery checkpoint — source-recovery round 1 after P16

**Date:** 2026-08-15 America/New_York

**Read after:** `AGENTS.md` and `research/2026-08-15_checkpoint_through_P16.md`.

This checkpoint records the targeted source-recovery work performed after the P01–P16 process architecture was completed.

## 1. RIE gas-ratio breakthrough — P08A

Direct RP-01 still states:

- `CH4/5H2`;
- total flow `64 sccm`;
- `100 mTorr`;
- `50 W`;
- `60 s`.

A 2005 HgCdTe RIE review by Srivastav, Pal and Vyas, *Opto-Electronics Review* 13(3), 197–211, Table 2, explicitly prints:

`CH4:H2 = 1:5`

for the relevant x≈0.31 LPE p-/n-HgCdTe RF parallel-plate mesa/type-conversion branch associated with the UWA Smith/Musca/Faraone lineage.

Evidence grade:

`CANDIDATE-SECONDARY / SAME-LINEAGE-SUMMARY`, not direct RP-01 primary data.

Derived from the RP-01 64-sccm total if the 1:5 decoding is correct:

- `Q_CH4 = 10.6667 sccm`;
- `Q_H2 = 53.3333 sccm`.

Tag as `[D from direct total flow + secondary-source-supported ratio]`.

Do **not** state that Smith et al. directly published those two MFC numbers.

No evidence was found supporting interpretations such as 5% H2 or CH4:H2=5:1.

Created:

- `research/2026-08-15_rie_gas_split_source_recovery.md`
- `procedures/P08A_RIE_GAS_RATIO_PROVENANCE_ADDENDUM.md`

### ~8-µm conversion depth remains open

Correct UWA primary source remains Musca et al. 1998, JEM 27, 661–667, DOI `10.1007/s11664-998-0032-4`.

The UWA record confirms that this paper contains depth/lateral information for RIE-induced n-type doping, but accessible source text still does not expose the exact conditions tied to the ~8-µm value cited by RP-01.

Keep `~8 µm` as `P-OTHER-SOURCE / SIMILAR-CONDITIONS`.

## 2. Same-UWA anodic-oxide lineage — P02A

Exact high-value same-team source recovered:

C. Musca, E. P. G. Smith, J. Dell, L. Faraone, “Performance and stability of HgCdTe photoconductive devices: A study of contact and passivation technology,” *1998 Conference on Optoelectronic and Microelectronic Materials and Devices Proceedings*, IEEE, published 1999, pp. 283–286, ISBN 0-7803-4513-4.

This source overlaps the RP-01 team directly and is likely the closest public passivation/contact bridge currently identified.

However, the publicly indexed UWA record exposes metadata only. No electrolyte/current density/endpoint/time sequence was recovered.

Earlier same-UWA source also identified:

C. A. Musca, J. F. Siliquini, B. Nener, L. Faraone, “Passivation and Surface Effects in Long Wavelength Infrared HgCdTe Photoconductors,” SPIE Vol. 2552, 158–169 (1995).

Again, indexed metadata does not reveal the executable anodization recipe.

Therefore:

- direct RP-01 closure = native anodic oxide, ~80 nm;
- exact UWA anodization recipe = `OPEN`;
- TI `0.1 M KOH / 90% EG + 10% DI / ~0.3 mA cm^-2 / ~15 V / ~2 min / ~80 nm` process remains a **non-UWA transfer candidate** only.

Created:

- `research/2026-08-15_anodic_oxide_same_lineage_recovery.md`
- `procedures/P02A_ANODIC_OXIDE_LINEAGE_ADDENDUM.md`

Do not add ZnS to RP-01 merely because same-UWA literature studies native oxide/ZnS and hydrogenated ZnS variants.

## 3. Honeywell x≈0.30 full-patent LPE re-audit — P03A

Bowers–Schmit US4317689A was re-audited at full text level.

Recovered directly:

- load substrate into graphite base recess;
- load Te-rich source into plugged slider well;
- separate HgTe source wafer in shallow source well;
- cover the assembly;
- place in quartz tube;
- thoroughly purge with N2 before heating;
- establish H2 flow;
- heat near 500 °C;
- after equilibration, translate slider to contact source and substrate;
- Hg-source/moat architecture maintains ~0.1-atm Hg environment near 500 °C;
- source first goes above liquidus, then below liquidus for growth;
- step cooling, slow continuous cooling, or combined mode are explicitly permitted;
- an example growth interval of about `0.5 h` is stated.

Full patent tie-line table:

| xL | yL | Tl | xS | xS/xL |
|---:|---:|---:|---:|---:|
| .100 | .825 | 508 °C | .40 | 4.00 |
| .095 | .820 | 508 °C | .37 | 3.89 |
| .082 | .810 | 507 °C | .29 | 3.54 |
| .060 | .800 | 510 °C | .22 | 3.67 |
| .050 | .800 | 499 °C | .195 | 3.90 |

The xS=.29 row remains the strongest composition match.

Critical limitation:

The ~30-min example is not explicitly connected to the xS=.29 row, 9.5-µm thickness or RP-01 transport state. It is a same-lineage qualification starting point, **not** a released growth time.

Same-lineage Wood/Hager 1983 horizontal-slider work reports composition reproducibility around `σx≈0.002` on 2×3-cm CdTe substrates; use as an achievable benchmark, not yet a specification.

Created:

- `research/2026-08-15_lpe_honeywell_full_patent_reaudit.md`
- `procedures/P03A_HONEYWELL_LPE_LINEAGE_ADDENDUM.md`

## 4. CdZnTe final pre-LPE surface candidate — P07A

A detector-oriented Te-rich LPE source using (111)B CdZnTe reports:

- CdZnTe around 4 mol% Zn;
- ~10×10×1-mm substrates;
- chemical + mechanical polish;
- final `2–3% Br2 in methanol` etch;
- immersion for a few seconds;
- load into graphite boat immediately after preparation.

This branch produces x≈0.20–0.22 LWIR HgCdTe, not x≈0.30 Honeywell material.

Therefore status is:

`CANDIDATE-P / LPE-CZT-SURFACE-PREP / DIFFERENT-COMPOSITION-BRANCH`.

Created:

- `procedures/P07A_CZT_PRE_LPE_SURFACE_PREP_ADDENDUM.md`.

Release still requires local qualification of concentration/time/removed depth/rinse/dry/clean-to-load against actual grown interface/morphology/P05/P06 outputs.

## 5. Lithography / metal exact-source recovery — negative result

Targeted searches of same-UWA Smith/Winchester/Musca/Dell/Faraone papers, including “Dry plasma technology for in-situ vacuum processing of HgCdTe infrared photodetectors” (2000), did not recover:

- resist manufacturer/product;
- spin program;
- exposure wavelength/dose;
- developer/time;
- historical metal base pressure;
- Cr/Au deposition rates;
- exact lift-off solvent/time.

The publicly indexed records remain metadata/abstract level. Do not repeat generic web queries and then infer these process variables from ordinary cleanroom practice.

## 6. Current highest-value unresolved variables after this round

1. exact primary confirmation of CH4:H2=1:5 / individual UWA MFC values;
2. exact conditions tied to the ~8-µm n+ conversion depth;
3. full 1999 UWA contact/passivation conference paper or author thesis;
4. exact x≈0.30 charge synthesis/homogenization and thickness-time relation;
5. exact x≈0.30 substrate final surface preparation / face / miscut;
6. exact lithography resist/dose/developer;
7. historical Cr/Au deposition/lift-off conditions;
8. historical package/preamp/device-gap identity.

## 7. Recommended next search strategy

Avoid repeatedly querying article titles already known to return metadata only.

Prefer:

- proceedings PDFs/IEEE archival access if directly available;
- author theses/dissertations or university library catalog records;
- patents by the same lab/company;
- cited primary process papers within accessible full texts;
- later same-lineage papers that explicitly describe inherited process recipes.

Continue recording negative source-recovery results as project knowledge.

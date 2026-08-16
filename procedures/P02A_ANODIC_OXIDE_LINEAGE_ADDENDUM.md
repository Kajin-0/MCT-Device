# P02A — anodic-oxide lineage provenance addendum

**Status:** CONTROLLED PROVENANCE UPDATE to `P02_ANODIC_OXIDE_QUALIFICATION.md`.

## 1. What RP-01 directly closes

Smith et al. 2001 directly establishes:

- passivant on the experimental devices: native anodic oxide;
- oxide thickness: approximately `800 Å = 80 nm`.

The audited paper does **not** disclose the anodization electrolyte/current/endpoint/time/fixture/rinse.

Therefore P02's direct historical closure remains limited to film type and thickness.

## 2. Exact same-laboratory passivation source now identified

C. Musca, E. P. G. Smith, J. Dell, L. Faraone, “Performance and stability of HgCdTe photoconductive devices: A study of contact and passivation technology,” *1998 Conference on Optoelectronic and Microelectronic Materials and Devices Proceedings*, IEEE, published 1999, pp. 283–286, ISBN 0-7803-4513-4.

This is the strongest same-laboratory bridge currently identified because it directly overlaps the RP-01 team and concerns HgCdTe photoconductor contact/passivation technology.

### Evidence limitation

The publicly indexed UWA record does not expose the experimental recipe.

Thus:

- paper identity/relevance = `CLOSED-P-BIBLIOGRAPHIC`;
- exact native-oxide recipe = still `OPEN`.

## 3. Earlier same-UWA photoconductor-passivation source

C. A. Musca, J. F. Siliquini, B. Nener, L. Faraone, “Passivation and Surface Effects in Long Wavelength Infrared HgCdTe Photoconductors,” SPIE Vol. 2552, 158–169 (1995).

This confirms a longer UWA photoconductor-passivation research lineage but does not presently supply an executable RP-01 anodization recipe in accessible text.

## 4. Status of the current detailed transfer candidate

The historical Texas Instruments native-oxide process remains a **transfer qualification candidate**, with approximately:

- `0.1 M KOH`;
- `90% ethylene glycol / 10% DI water`;
- constant-current anodization around `0.3 mA/cm²`;
- formation endpoint around `15 V`;
- approximately `2 min`;
- approximately `80 nm` resulting oxide.

These numbers remain **CANDIDATE-P / NON-UWA**.

They must not be rewritten as “the UWA process” or “the Smith et al. 2001 anodization recipe.”

## 5. Local release rule

Until the exact same-UWA recipe is recovered, P02 can become locally released only through qualification on RP-01-compatible x≈0.30 material demonstrating:

1. oxide thickness centered at the selected 80-nm target;
2. acceptable within-sample and run-to-run uniformity;
3. stable voltage-time/current-time anodization signature;
4. no unacceptable shift in P05 transport behavior caused by the surface process;
5. acceptable P10 dark electrical behavior;
6. acceptable P12 low-frequency/noise behavior;
7. compatibility with P08 oxide clearing + n+ conversion;
8. acceptable P09 contact/TLM performance after the complete contact sequence.

Thickness alone is insufficient because two 80-nm native oxides can differ in composition, interface charge, interface-state density and device noise.

## 6. ZnS caution

Same-UWA literature contains important ZnS and hydrogenated-ZnS passivation studies. These are **not** evidence that the actual RP-01 experimental devices used ZnS.

Do not add ZnS to RP-01 unless a direct device/process source supports it. Treat native oxide + ZnS as a separate process variant/reference process.

## 7. Search result / negative evidence

Repeated web searches for:

- the full 1999 same-UWA passivation/contact paper;
- IEEE DOI/full experimental text;
- Musca/Smith/Siliquini theses containing native-oxide recipes;

have not yet recovered an explicit UWA electrolyte/current-density/endpoint/time sequence.

This negative result is deliberate project knowledge. Future agents should not infer the recipe from common practice.

Detailed search record:

`research/2026-08-15_anodic_oxide_same_lineage_recovery.md`

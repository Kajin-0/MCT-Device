# Round 52 — integrated manuscript adversarial technical review

**Date:** 2026-08-16 America/New_York  
**Object reviewed:** `manuscript/RP01_HGCDTE_PHOTOCONDUCTOR_PROCESS_MANUAL_DRAFT.md`, Draft 0.1 / Round 51  
**Review mode:** adversarial technical/procedural audit against the controlled P01–P36A procedure set and calculation modules.

## Overall disposition

`RP01-MANUSCRIPT-ADVERSARIAL-REVIEW-PASSED = YES`, conditional on incorporation of the corrections listed below into Draft 0.2.

This is a document-quality state only. It does not imply `TRACEABLE-FIRST-BUILD-READY`, `HISTORICAL-RP01-REPRODUCED`, or `REPRODUCIBLE-RELEASE`.

The review found no need to replace the reference process architecture. The major scientific anchors remain internally consistent. The important defects were claim precision and state-definition defects rather than a failed physical model.

## Major findings and corrections

### R52-01 — title overclaimed reproducibility

Draft 0.1 was titled `Reproducible Fabrication and Characterization...` while the body correctly states that a reproducible local release has not been demonstrated.

**Correction:** retitle as a source-traceable qualification fabrication/characterization manual. Reserve `reproducible` for a demonstrated local process after P17 closure.

### R52-02 — reference center could be mistaken for an executable setpoint

Several chapters correctly label literature centers but still use imperative wording such as `use` before the local apparatus/process branch is instantiated.

**Correction:** add an irreversible-step preflight rule. A `[REF-CENTER]` may seed development but never fills a required `[LOCAL-CAL]` or `[LOCAL-QUAL]` field. Before irreversible execution, all step-specific local fields, required P36/P36A commissioning evidence, genealogy, and applicable EH&S authorization must be complete. `TBD`, `appropriate`, and blank fields are not executable instructions.

### R52-03 — P36/P36A omitted from manuscript crosswalk

Draft 0.1 integrated P01–P35 but omitted the later laboratory subsystem commissioning/acceptance modules P36 and P36A from the manuscript crosswalk.

**Correction:** make P36/P36A normative preflight references for tool acceptance, supporting metrology, lithography, wet chemistry and anodization.

### R52-04 — RIE carrier-density wording obscured conversion-depth dependence

P08B explicitly takes precedence over wording that treats the published `2.0×10^15 cm^-3` converted-region density as independent of conversion depth. RP-01 states the value was averaged over the RIE-converted thickness.

**Correction:** report `R_s`, Hall sheet state / `N_s`, mobility, independently justified `d_conv`, and only then `n_conv=N_s/d_conv`. Treat the blocking-contact qualification vector as at least `{N_s, mu_H, d_conv, L_conv, d_etch, rho_c, blocking response}`. Do not tune a reactor to `n_conv` alone.

### R52-05 — FOV angular convention remained under-specified

RP-01 states `60° FOV`, but the paper does not document whether 60° is a full cone or half-angle and does not provide the physical aperture geometry. P11A finds that a 60° full cone / 30° half-angle is consistent with the quoted 300-K photon-flux scale, but that is a consistency inference, not historical proof.

**Correction:** preserve `stated 60° FOV` for historical comparison, separately record the physical aperture/view-factor geometry for a new measurement, and label the 60°-full-cone interpretation as a derived consistency model only.

### R52-06 — D* area wording was too restrictive

Draft 0.1 said the area in `D*` must be the same physical area used to define incident power. P20A shows that detector normalization area and optical power/irradiance geometry may be distinct but correlated.

**Correction:** define `A_D*` explicitly as the detector normalization area and define optical beam/aperture/irradiance geometry separately. If incident power is derived using a shared area, retain covariance. The logarithmic area sensitivity is `0.5-gamma_A`, where `gamma_A = partial ln(P_inc)/partial ln(A_D*)` under the stated geometry convention.

### R52-07 — same-device closure for RP-01 Figures 3/5/6/7 was not exploited strongly enough

P12C closes that responsivity-vs-field, noise, spectral response and spectral D* are from the same representative device.

**Correction:** require a new D* closure to lock `{device, contact pair, measured gap/width, T, E, package, FOV/background, loading, frequency convention}` across P11/P12 unless an explicit measured correction is applied. `same process` is not an adequate substitute for `same state`.

### R52-08 — 24.5 nV/sqrt(Hz) remains a high-frequency diagnostic, not a 1-kHz substitution

No regression found. Draft 0.1 already preserved the critical fact that 1 kHz is below the reported ~3-kHz 1/f knee.

**Disposition:** retained and strengthened with P12C same-device/state language.

### R52-09 — authoritative LPE mass convention remains correct in manuscript

Draft 0.1 correctly uses the controlled calculation values:

- `w_Hg = 0.2497382358`
- `w_Cd = 0.01250164993`
- `w_Te = 0.7377601143`

using Hg 200.59, Cd 112.414 and Te 127.60 g/mol.

P30A still contains older rounded values in one section from the known ppm-scale numerical erratum. The manuscript is already correct.

**Disposition:** manuscript retains the authoritative calculation. P30A should be repaired separately or annotated as superseded by `calculations/LPE_CHARGE_COMPOSITION_SENSITIVITY.md`; do not copy its older rounded triplet back into the manuscript.

### R52-10 — no universal apparatus parameter should be invented to make the paper look complete

No evidence was found that the remaining local furnace offsets, MFC calibrations, QCM tooling factors, lithography doses, package bondline dimensions, or optical view factors have universal transferable values.

**Correction:** keep them as mandatory local instantiation fields with acceptance methods. Their absence in an unspecified laboratory is not a reason to fabricate a number or postpone the manuscript indefinitely.

## Numerical/equation sanity findings retained

The following integrated values/equations remain internally consistent after review:

- `rho≈0.15922 ohm cm`, `R_sheet≈167.60 ohm/square`, `|R_H|≈6.369e3 cm^3/C` under the stated one-carrier screening assumptions;
- ideal `I≈1.79 mA` at 10 V/cm for 300-um width and 9.5-um thickness under the same screening model;
- active voltage 0.05–0.40 V for 50–400-um gaps at 10 V/cm;
- xL=.082, yL=.810, TL=507 °C tie-line anchor and ~500 °C first contact as a ~7-K reference-center supercooling;
- pure-KOH arithmetic `5.61056 g` per stated 1-L / 0.1000-mol branch before reagent-assay correction;
- `t_sem=t_RF-t_clear`;
- `NEP=e_n/R_v`;
- `D*=R_v sqrt(A_D*)/e_n` under an explicitly stated area/power convention;
- PSD-level electronics subtraction `e_det=sqrt(e_meas^2-e_elec^2)` when independence/loading assumptions are satisfied;
- one-pole `f_3dB=1/(2 pi tau)` only after model validation;
- ~14-MHz source rise-time scale from `0.35/25 ns`, retained only as an apparatus sizing check.

## Remaining manuscript work after Draft 0.2

The next document work is no longer another broad process-source search. Priorities are:

1. complete bibliography generated from the controlled source ledger;
2. uncertainty/example-calculation appendix;
3. process-flow, LPE, anneal, RIE/contact and radiometry schematics;
4. operator checklists/travelers extracted from the main narrative;
5. terminology/symbol index;
6. professional typesetting and PDF/booklet production;
7. a final editorial/visual adversarial review.

Any new source search should be targeted to a specific unresolved claim that materially improves the final manual.
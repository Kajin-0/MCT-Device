# Passivation lineage research — 2026-08-15

## Objective

Close the 800 Å anodic-oxide passivation step used on RP-01 without assuming that a generic HgCdTe anodization recipe is identical to the UWA/Faraone process.

## What RP-01 itself establishes

Smith et al. (2001), DOI `10.1088/0268-1242/16/6/306`, explicitly states that the experimental photoconductive devices were passivated with **800 Å of anodic oxide**.

The paper does not state the electrolyte, anodization current density, formation-voltage criterion, cell geometry, temperature, or oxide-growth calibration.

Therefore:

- film identity/thickness = `[P]`;
- oxide-growth recipe = still `[OPEN]` for RP-01.

## Same-lineage review source

O. P. Agnihotri, C. A. Musca, and L. Faraone, *Semiconductor Science and Technology* 13, 839–847 (1998), DOI `10.1088/0268-1242/13/8/002`, is a high-priority review from the same UWA group.

Its role is to map the primary anodic-oxide literature and identify which native-oxide process the group regarded as established. It is not itself sufficient evidence that RP-01 used one exact recipe.

## Historical primary process candidate — Texas Instruments anodic oxide

A Texas Instruments photoconductor anodization process (US3977018A) reports a highly specific native-oxide process for HgCdTe:

- electrolyte: **0.1 M KOH in 90% ethylene glycol / 10% deionized water**;
- mode: **constant-current anodization**;
- current density: **0.3 mA cm^-2**;
- formation voltage: **approximately 15 V**;
- reported time: **approximately 2 min**;
- reported resulting oxide thickness: **800 Å**;
- process endpoint/visual observation: uniform deep-blue film;
- film-thickness verification described using profilometry/interference-type methods.

### Provenance status

These values are `[P-B]` for the historical TI process, meaning directly reported in a primary patent/process disclosure, **not `[P]` for RP-01**.

### Why the candidate is important

The output thickness is exactly the 800 Å thickness reported for RP-01, and the KOH/ethylene-glycol/water electrolyte family recurs in later HgCdTe anodic-oxide studies. This makes the process a strong candidate for a qualification branch.

### Why it cannot simply be copied into RP-01

1. The TI disclosure is not the UWA fabrication paper.
2. HgCdTe composition and starting surface state influence anodic oxide chemistry.
3. Cell geometry, exposed area, electrical contact, solution age, temperature, and current-density calibration affect growth.
4. The RP-01 material is nominally x≈0.30 n-type LPE material; historical anodization sources include other compositions and material histories.
5. Exact equality of final thickness does not establish equality of interface charge, composition, surface accumulation, or noise behavior.

## Independent experimental support for the same electrolyte family

Other HgCdTe anodic-oxide work reports constant-current anodization near room temperature in **0.1 M KOH / 90% ethylene glycol / 10% water**, including native films around the 70–80 nm scale. This supports the process family but still does not close the UWA-specific recipe.

A later study reports an 800 Å anodic oxide obtained in the same electrolyte family using 0.3 mA cm^-2 and termination at a 15 V voltage drop. That is notable independent corroboration of the thickness/formation-voltage relation, but it used different HgCdTe material and is not an RP-01 source.

## Qualification strategy proposed for RP-01

If the exact UWA anodization recipe cannot be recovered, the historical 800 Å process may be promoted from `OPEN` to `QUAL` only through a sacrificial-coupon study.

The qualification module should control/record at minimum:

1. HgCdTe wafer/coupon ID, x, conductivity type, carrier density, mobility, surface preparation, and time since final clean.
2. Electrolyte identity, KOH molarity, ethylene-glycol/water ratio, reagent grades, solution age, and solution temperature.
3. Electrochemical cell material and geometry, exposed MCT area, counter-electrode material/area/distance, and MCT electrical-contact method.
4. Constant-current density and calibrated source uncertainty.
5. Full voltage-versus-time trace during anodization.
6. Termination criterion: formation voltage and/or time.
7. Rinse and dry sequence.
8. Oxide thickness at multiple positions by an independent metrology method.
9. Thickness uniformity and run-to-run repeatability.
10. Surface/interface electrical characterization where possible.
11. Compatibility with the subsequent CH4/H2 contact-window RIE.
12. Finished-detector leakage, resistance stability, 1/f noise, g-r noise, responsivity, and thermal-cycle stability.

## Proposed acceptance hierarchy

The eventual process should not be accepted because the oxide is merely “blue” or nominally 800 Å. Release should require three nested closures:

- **geometrical closure:** correct film thickness/uniformity;
- **electrical/interface closure:** acceptable surface accumulation/interface charge/leakage behavior;
- **device closure:** no degradation of responsivity/noise/stability after the complete process.

Numerical acceptance bands remain `[Q]` until either the UWA process limits are recovered or sufficient reproduction data establish capability.

## Current conclusion

The anodic-oxide gap has moved from an unconstrained `OPEN` problem to a **well-defined process family with a strong 800 Å candidate recipe**, but RP-01 is not yet closed. The next literature target is the exact UWA/Faraone anodization practice or a thesis/process paper from that laboratory that explicitly links the KOH/ethylene-glycol constant-current method to the photoconductors used in the 2000–2001 device papers.

# Mesa-etch lineage research — 2026-08-15

## Objective

Determine the correct mesa-isolation branch for RP-01 and avoid substituting a convenient dry-etch process for the wet-chemical isolation used in the demonstrated high-performance photoconductors.

## Same-laboratory evidence

### Smith et al. 1999

E. P. G. Smith, C. A. Musca, D. A. Redfern, J. M. Dell, and L. Faraone, “Reactive ion etching for mesa structuring in HgCdTe,” *Journal of Vacuum Science & Technology A* 17(5), 2503–2509 (1999). DOI `10.1116/1.581988`.

This UWA paper compares wet chemical and CH4/H2 RIE mesa structuring in n- and p-type HgCdTe. The reported observations establish two important process facts:

1. bromine-based wet chemical mesa etching did not produce the large electrically active type-conversion/doping modification seen after RIE;
2. RIE of n-type material creates enhanced n-type/n+ behavior, while p-type material can convert to n-type.

A reported RIE comparison condition was approximately 400 mTorr, CH4/5H2, 0.4 W cm^-2. These are **mesa-etch study conditions**, not the later RP-01 contact-window recipe and must not be substituted for it.

The same study reports restoration of RIE-modified electrical properties after a low-temperature mercury anneal around 200 °C. This is useful mechanistic evidence but does not justify inserting a post-mesa Hg anneal into RP-01 without checking the complete thermal/process sequence.

### Smith et al. 2000

E. P. G. Smith, C. A. Musca, D. A. Redfern, J. M. Dell, and L. Faraone, “H2-based dry plasma etching for mesa structuring of HgCdTe,” *Journal of Electronic Materials* 29(6), 853–858 (2000). DOI `10.1007/s11664-000-0237-7`.

This paper directly evaluates **n-type x≈0.31 HgCdTe photoconductive detectors** fabricated with:

- wet chemical mesa etching using bromine in hydrobromic acid; versus
- H2/CH4 RIE mesa etching.

Reported detector comparison conditions include 80 K, 60° FOV, and 3 µm signal wavelength. The wet-chemical devices reached background-limited performance, whereas the dry-mesa devices showed substantially poorer detectivity in the reported comparison.

This is highly relevant because the material composition and photoconductor architecture closely match RP-01.

## Process decision for RP-01

**Mesa isolation remains a wet-chemical process branch.**

The purpose of the CH4/H2 RIE step in RP-01 is therefore kept narrow:

- patterned removal of the anodic oxide at the contact window;
- intentional formation of a higher-doped n+ contact region.

The RIE is **not** automatically extended over mesa sidewalls or the full active region.

This distinction is physically important because the active-region RIE-induced electrical modification that is beneficial under a contact can degrade photoconductor behavior when imposed over the mesa.

## What remains open

The exact wet-mesa recipe has not yet been recovered. Required fields remain:

- Br2 concentration;
- HBr concentration/grade;
- any water or other solvent fraction;
- solution preparation order;
- bath temperature;
- solution age;
- agitation;
- mask/resist identity and thickness;
- etch time;
- vertical etch rate;
- lateral undercut rate;
- target depth relative to the 9.5 µm epilayer;
- endpoint method;
- rinse sequence;
- post-etch surface treatment;
- resist strip;
- surface roughness and dimensional acceptance criteria.

No concentration from a different Br2/HBr, Br2/methanol, or Br2/ethylene-glycol paper should be inserted into RP-01 until the UWA experimental section or a directly linked process source is recovered.

## Mechanistic implication

The lineage evidence changes the process philosophy from “choose the most anisotropic etch” to:

> choose the mesa process that preserves the intended HgCdTe electrical state, then use geometry-aware mask bias/undercut control to compensate for the isotropic wet etch.

For a single-element or low-density photoconductor, electrical integrity can therefore dominate sidewall anisotropy as the primary mesa-process objective.

## Required qualification measurements once the exact wet chemistry is recovered

A release-quality mesa module should measure:

1. pre-etch and post-etch Hall/Van der Pauw properties on process monitors where geometry permits;
2. etched depth by profilometry or cross-sectional method;
3. lateral undercut and critical dimensions by calibrated microscopy/SEM;
4. surface roughness;
5. residual surface composition/Te-rich residue if relevant;
6. LBIC or equivalent spatial electrical response around the mesa edge;
7. detector dark resistance and bias symmetry;
8. responsivity/noise compared with an unetched control or established process baseline.

## Current status

- Process family: **closed — wet bromine/HBr mesa branch**.
- Exact executable chemistry: **OPEN**.
- Evidence against replacing the branch with blanket CH4/H2 RIE: **strong and same-laboratory/same-device-class**.

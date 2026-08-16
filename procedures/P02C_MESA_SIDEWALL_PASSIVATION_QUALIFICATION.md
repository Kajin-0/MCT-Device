# P02C — mesa-sidewall passivation qualification

**Status:** CONTROLLED PASSIVATION ADDENDUM. Supplements P01/P02/P02A/P02B.

## 1. Purpose

Ensure that RP-01's post-mesa anodic-oxide step passivates the electrically relevant exposed HgCdTe surfaces, including mesa sidewalls, rather than accepting a process solely because a horizontal witness indicates approximately 80 nm oxide thickness.

This module does **not** change the historical RP-01 film identity or thickness. It adds a surface-coverage/performance qualification requirement.

## 2. Why sidewalls matter

Same-UWA photoconductor work predating RP-01 established that photoconductor performance is strongly influenced by semiconductor surface recombination.

J. F. Siliquini, K. A. Fynn, B. D. Nener, L. Faraone, R. H. Hartley, “Improved device technology for epitaxial Hg1−xCdxTe infrared photoconductor arrays,” *Semiconductor Science and Technology* 9, 1515–1522 (1994), DOI `10.1088/0268-1242/9/8/013`, directly reports that leaving device sidewalls unpassivated can reduce responsivity by approximately a factor of two in the LWIR photoconductors studied.

A 1995 same-UWA SPIE paper, “Long-Wavelength Infrared Photoconductor Technology Based on Epitaxially Grown Hg1−xCdxTe,” Vol. 2552, pp. 98–109, further emphasizes surface and contact effects in epitaxial HgCdTe photoconductor technology.

These devices/materials differ from RP-01; the factor-of-two result is therefore a **surface-physics warning**, not an RP-01 numerical acceptance target.

## 3. Process-order consequence for RP-01

RP-01 architecture is:

`wet mesa -> anodic oxide -> contact-window lithography -> localized RIE -> Cr/Au`.

Because anodization occurs after mesa delineation, the exposed mesa top and sidewall surfaces are both present during the passivation step.

Therefore the desired process state is:

- top HgCdTe surface passivated;
- mesa sidewalls passivated;
- contact windows intentionally opened later by Mask-2/RIE;
- no unintended exposed HgCdTe perimeter remaining in the active region.

## 4. Why top-surface thickness alone is insufficient

A witness measurement of `~80 nm` on a planar region does not prove:

- oxide continuity on a sloped/undercut wet-etched sidewall;
- equivalent electrochemical access along the sidewall;
- absence of trapped gas/bubbles at the mesa perimeter;
- absence of localized oxide thinning at corners;
- acceptable interface state/recombination behavior on the crystallographic sidewall surfaces.

Accordingly P02 acceptance must include a sidewall-sensitive test.

## 5. Qualification structure

During P01/P02 process development include at least two geometry classes on the same or matched material:

1. planar anodization witness for top-surface oxide thickness/electrochemical trace;
2. mesa/perimeter test structures with representative depth, sidewall angle and corner geometry.

Prefer multiple perimeter-to-area ratios while holding material and active area class otherwise comparable.

## 6. Required sidewall characterization

Use one or more complementary methods capable of detecting sidewall coverage or its electrical consequence.

Candidate methods include:

### Physical/chemical coverage

- cross-sectional SEM/TEM on sacrificial structures where oxide contrast permits;
- focused-ion-beam cross section only where preparation damage is controlled/interpreted;
- conformality-sensitive optical/electron microscopy;
- surface/composition analysis on sacrificial angled structures if available.

### Electrical/device-sensitive methods

- responsivity versus perimeter-to-area ratio;
- noise versus perimeter-to-area ratio;
- resistance/I-V leakage versus perimeter;
- transient lifetime versus perimeter;
- spatial LBIC/photocurrent mapping near mesa boundaries;
- comparison of nominally identical devices with deliberately different exposed perimeter.

The electrical route is mandatory if physical film metrology cannot demonstrate actual interface quality.

## 7. Perimeter-sensitivity experiment

Define device active area `A` and exposed semiconductor perimeter `P` from measured fabricated geometry.

At fixed:

- material lot;
- thickness/composition;
- anneal state;
- contact process;
- operating T;
- electric field;
- optical condition;

fabricate/test structures spanning at least three distinct `P/A` values where practical.

Measure:

- dark resistance/I-V;
- low-frequency responsivity;
- 1/f and g-r noise;
- P13 effective time constant where practical.

A systematic dependence on `P/A` after geometric normalization is evidence that sidewall/interface effects remain electrically important.

## 8. Before/after sidewall-passivation control

During qualification, where material inventory allows, compare:

- mesa structures before final sidewall passivation;
- the same process family after anodization;
- optionally a deliberately interrupted/partial-passivation control.

This experiment is for process physics/qualification only; deliberately unpassivated controls are not production devices.

## 9. Acceptance principle

A released P02 process must demonstrate both:

1. reproducible planar oxide formation near the RP-01 historical 80-nm target; and
2. no statistically significant detector-performance degradation attributable to unpassivated/inadequately passivated mesa perimeter within the released geometry range.

Numerical perimeter-effect limits must be established from local measurement uncertainty and detector-performance requirements; they are not copied from the x≈0.23 LWIR factor-of-two result.

## 10. Interaction with P01 wet-etch geometry

P01 wet etching is isotropic/partly undercut and the sidewall profile depends strongly on chemistry and temperature.

Therefore P02 sidewall qualification must be repeated if P01 materially changes:

- sidewall angle;
- undercut;
- roughness;
- final mesa depth;
- crystallographic exposure;
- pre-passivation surface chemistry.

The etch and passivation modules are coupled.

## 11. Interaction with P13 lifetime

If sidewall recombination is important, P13 transients may show geometry-dependent effective lifetime.

A bulk-lifetime claim is therefore strengthened by demonstrating that extracted `tau_eff` becomes insensitive to perimeter/area after the released P02 process.

## 12. Interaction with P12 noise

Poor/unstable sidewall passivation can introduce surface-generation/recombination or 1/f contributions.

P12 qualification should therefore compare low-frequency noise across P/A test structures during passivation development.

## 13. Historical restriction

Do not claim that RP-01 itself measured sidewall oxide thickness or perimeter scaling unless a direct source is recovered.

P02C is a physically motivated **local qualification requirement** supported by same-UWA photoconductor evidence, not a reconstruction of an unpublished historical traveler.
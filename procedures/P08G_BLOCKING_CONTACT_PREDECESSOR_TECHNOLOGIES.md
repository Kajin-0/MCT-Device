# P08G — blocking-contact predecessor technologies and functional lineage

**Status:** HISTORICAL/PHYSICAL-LINEAGE ADDENDUM. Supplements P08F. Does not alter the RP-01 RIE recipe.

## 1. Purpose

Separate the distinct contact-engineering mechanisms that preceded the RP-01 RIE-induced n+/n blocking contact and identify which physical performance quantities are transferable as functional concepts.

The phrase **blocking contact** is not a unique fabrication process. Historical HgCdTe photoconductor literature contains at least three distinct implementations/mechanisms:

1. metal-contact accumulation induced by ion-cleaning/surface preparation;
2. epitaxial wider-bandgap HgCdTe heterojunction contacts;
3. plasma-induced n+/n contact regions such as RP-01.

Do not transfer process setpoints among these architectures merely because all reduce contact recombination/sweepout.

## 2. Ashley–Elliott 1982 — ion-cleaning / accumulation contact

T. Ashley and C. T. Elliott, “Accumulation effects at contacts to n-type cadmium-mercury-telluride photoconductors,” *Infrared Physics* 22(6), 367–376 (1982).

Direct abstract-level primary-source findings:

- n-type CdxHg1−xTe photoconductors were studied;
- contact deposition was **preceded by an ion-cleaning treatment**;
- measurements were consistent with contact-accumulation models;
- accumulation increased responsivity of small photoconductors by approximately a factor of five;
- detector response time became strongly field dependent;
- approximate contact recombination velocities were reported in the `~200–500 cm/s` range for samples including `x=0.30` and `x=0.21`.

### Interpretation

This contact is a surface/contact-accumulation mechanism created in conjunction with ion cleaning and metal deposition.

It is not evidence that RP-01's CH4/H2 RIE used the same physical mechanism or process condition.

Use the `~200–500 cm/s` scale only as a historical functional benchmark for strongly blocking HgCdTe contacts, not as a released RP-01 value.

## 3. Shacham-Diamand & Kidron 1981 — built-in-field/contact-blocking physics

Y. J. Shacham-Diamand and I. Kidron, “Contact and bulk effects in intrinsic photoconductive infrared detectors,” *Infrared Physics* 21(2), 105–115 (1981), DOI `10.1016/0020-0891(81)90018-X`.

Primary findings include:

- analysis of built-in electric fields and contact blocking in narrow-gap HgCdTe;
- partial blocking of excess minority carriers can enhance responsivity;
- contact/bulk transport changes detector temporal response;
- small-area x≈0.215 HgCdTe devices at 77 K were used for experimental comparison.

Use this source for contact-field/sweepout physics, not for RP-01 fabrication conditions.

## 4. Smith–Arch–Wood–Walter Scott 1984 — heterojunction contact photoconductor

D. L. Smith, D. K. Arch, R. A. Wood, M. Walter Scott, “HgCdTe heterojunction contact photoconductor,” *Applied Physics Letters* 45, 83–85 (1984).

Primary abstract-level result:

- a **higher-bandgap HgCdTe alloy layer** is placed between the metal contact and the normal-bandgap HgCdTe photoconductor;
- the heterojunction contact is predicted to nearly eliminate carrier sweepout and responsivity saturation;
- fabricated devices experimentally verified the principle;
- at 80 K, reported voltage responsivity was approximately `4.5×10^5 V/W` at `30 V/cm` and `>1.5×10^6 V/W` at `125 V/cm`.

### Architecture distinction

This is an epitaxial/material heterojunction blocking layer, not a plasma-damaged or RIE-doped contact region.

Do not use its layer composition/thickness or bias capability as RP-01 process values without a separate source/model comparison.

## 5. Arch–Wood–Smith 1985 — high-responsivity HCP follow-on

D. K. Arch, R. A. Wood, D. L. Smith, “High responsivity HgCdTe heterojunction photoconductor,” *Journal of Applied Physics* 58(6), 2360–2370 (1985), DOI `10.1063/1.335959`.

This is the detailed follow-on to the 1984 HCP concept and should be treated as the principal primary source for the heterojunction architecture if full text is acquired.

Later device/patent literature describes this class as an **isotype heterojunction blocking contact** formed by growing a wider-bandgap HgCdTe semiconductor layer epitaxially on the active HgCdTe layer.

Use restriction:

- useful for functional contact-recombination/sweepout targets;
- not a direct source for RP-01 RIE parameters.

## 6. D. L. Smith 1984 — theory of blocking contacts, noise and responsivity

D. L. Smith, “Effects of blocking contacts on generation-recombination noise and responsivity in intrinsic photoconductors,” *Journal of Applied Physics* 56(6), 1663–1669 (1984), DOI `10.1063/1.334155`.

Primary theory results:

- contact recombination is parameterized by a contact recombination velocity;
- stronger blocking increases responsivity;
- stronger blocking can push D* toward background-limited performance because responsivity/background-noise contribution grow faster than thermal contribution;
- blocking contacts also lower the frequency at which responsivity and g-r noise roll off;
- for modeled x≈0.2 HgCdTe, blocking contacts substantially enlarge the material-property window capable of meeting detector-performance targets.

### Important consequence for P08F/P13

A better blocking contact may increase low-frequency responsivity while **reducing detector bandwidth** because the effective excess-carrier lifetime increases when contact recombination is suppressed.

Therefore contact optimization is inherently a responsivity–noise–bandwidth tradeoff and cannot be judged by maximum responsivity alone.

## 7. Functional target hierarchy for RP-01

The predecessor literature suggests that a useful blocking contact should be evaluated in this order:

1. majority-carrier electrical contact remains adequately ohmic/stable;
2. minority-carrier contact recombination is reduced;
3. responsivity remains linear to higher electric field before sweepout saturation;
4. low-frequency excess/contact noise does not negate responsivity gain;
5. D* / NEP improve or at least remain acceptable;
6. temporal response/bandwidth remain compatible with the application.

This is the physical basis for P08F's multi-objective detector-level gate.

## 8. Contact recombination velocity as a useful latent quantity

Historical accumulation/heterojunction literature often reports or models contact recombination velocity `S_c`.

RP-01 does not directly publish `S_c` for its RIE n+/n contact.

Where a validated spatial drift-diffusion model and sufficient measurement data exist, `S_c` may be inferred by fitting:

- responsivity versus field;
- spatial carrier distribution;
- temporal response;
- device geometry;
- contact-region state.

Do not derive a unique `S_c` from TLM contact resistivity alone. Majority-carrier specific contact resistance and minority-carrier recombination velocity are different physical quantities.

## 9. Distinction table

| Contact concept | Physical mechanism | Historical example | Transfer to RP-01 |
|---|---|---|---|
| accumulation contact | surface/contact accumulation after ion cleaning | Ashley–Elliott 1982 | physics benchmark only |
| wider-gap HCP | epitaxial isotype wider-bandgap HgCdTe layer | Smith/Arch/Wood 1984–85 | functional/model benchmark only |
| RIE n+/n | plasma-induced electrical conversion beneath metal | Smith et al. RP-01 | canonical RP-01 process |
| heterojunction blocking cap | deliberately composition-engineered cap/contact region | later UWA LWIR HBC work | alternative architecture; not RP-01 |

## 10. Process-history conclusion

RP-01 should be understood as a **fabrication simplification of a pre-existing blocking-contact design principle**:

- the physical objective—reduce carrier loss at contacts—was established earlier;
- earlier implementations could require special contact surface conditions or separately grown wider-bandgap layers;
- RP-01 uses localized CH4/H2 RIE both to clear the native oxide contact window and create an electrically modified n+ region, enabling a two-mask self-aligned contact process.

This historical distinction should be preserved in the manual so future process changes are evaluated against the functional objective rather than merely reproducing the label “n+ blocking contact.”
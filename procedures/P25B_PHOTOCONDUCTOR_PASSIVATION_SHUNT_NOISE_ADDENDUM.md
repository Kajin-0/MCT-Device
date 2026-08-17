# P25B - photoconductor passivation, surface shunt and noise addendum

**Status:** `PT` PHOTOCONDUCTOR INTERFACE EVIDENCE. Supplements P02/P02A-P02C/P25/P25A/P12/P13.

## Purpose

Round 64 strengthens the link between native anodic oxide, surface accumulation, shunt resistance, effective minority-carrier lifetime, responsivity and detector noise. The central correction is that oxide thickness alone is not an adequate electrical passivation endpoint.

## Coupled passivation state

Where metrology permits, record the passivated detector/interface state as:

`Y_pass = {d_ox, Qss, Dit_fast, hysteresis/slow-trap metric, Rsh_surface, tau_eff, Rv(lambda), PSD/ASD}`.

No one coordinate is a universal optimization target.

## Pal 1999 gated-photoconductor branch

The PT experiment used an n-HgCdTe gated photoconductor with:

- 300 A anodic oxide;
- 2700 A ZnS;
- 300 A In gate;
- 77 K testing;
- gate sweep to deliberately alter surface potential.

The experiment demonstrates two competing consequences of positive surface accumulation:

1. reduced surface recombination can increase effective minority-carrier lifetime and responsivity;
2. the accumulation layer forms a lower-resistance surface path that can shunt the detector and reduce responsivity.

The best-fit interface-trap density in that test structure was of order 5-7e11 cm^-2 eV^-1. This is a PT example, not an RP-01 acceptance limit.

## Bhan 2004 noise consequence

Measurements/modeling of n-HgCdTe photoconductor arrays required a noise contribution associated with surface shunt resistances at anodic-oxide accumulation layers. Bulk generation-recombination noise alone did not reproduce the observed network behavior.

For diagnostic use, P12 shall consider a surface-shunt branch when one or more of the following occur:

- measured resistance is substantially below bulk-transport expectation;
- passivation changes resistance without a corresponding bulk Hall change;
- noise does not scale with the expected bulk g-r model;
- front/rear surface treatments change noise disproportionately;
- gate/illumination history changes detector resistance or noise.

Do not subtract a synthetic surface-noise term without an identified circuit/model. The point is model selection, not automatic correction.

## Schoolar 1982 x=.30 anodic-oxide memory

On anodized n-type Hg0.7Cd0.3Te, visible light and electric field can change oxide/interface charge state. Reported observations include:

- positive fixed charge of order 5e11 cm^-2 in the studied structure;
- optical threshold around 2.2 eV for charge-neutralization behavior;
- dark recovery from minutes at room temperature to weeks at 77 K;
- field-driven charge exchange and surface-potential relaxation;
- optical oxide gap of about 3.4 eV.

### New preconditioning record

Before comparing C-V, surface conductivity, photoconductor resistance, responsivity or noise, record:

- previous visible/UV exposure spectrum or source class;
- exposure duration and approximate irradiance where known;
- dark-rest duration;
- previous gate/electric-field state;
- time since field removal;
- measurement temperature;
- sequence order of repeated measurements.

A passivated coupon can have the same physical oxide thickness but a different electrical interface state because of prior light/field history.

## Thermal caution

Native oxide/interface charge can be thermally sensitive. Do not interpret an elevated-temperature bake as merely an adhesion or dehydration step; measure its electrical consequence where that bake is part of the process.

## Release logic

For an RP-01-like n-type photoconductor, passivation development is acceptable only when the selected oxide process jointly gives:

- stable physical coverage/thickness;
- no unacceptable hysteresis or history dependence within the defined measurement protocol;
- acceptable surface shunt;
- acceptable effective lifetime/responsivity;
- acceptable noise spectrum;
- no adverse downstream RIE/metallization interaction.

Historical RP-01 `Qss`, `Dit`, surface-shunt resistance and preconditioning sequence remain `OPEN` unless direct same-device evidence is recovered.
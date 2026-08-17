# Research checkpoint — full-text source acquisition Round 62

**Date:** 2026-08-17 America/New_York  
**State:** documentary evidence strengthened; no new end-to-end experimental evidence.

## Completed work

A targeted full-text pass was completed against the Round-61 EEFP using nineteen supplied primary papers covering LPE/Hg compensation, CdZnTe qualification, Hg-rich anneal, anodic oxide, UWA RIE/LBIC, contact noise, FTIR mapping and HgCdTe-PC package thermal dynamics.

Controlling records:

1. `docs/RP01_FULLTEXT_SOURCE_ACQUISITION_ROUND62.md`
2. `docs/SOURCE_LEDGER_ADDENDUM_ROUND62.md`
3. `docs/RP01_GAP_MATRIX_ADDENDUM_ROUND62.md`

## Highest-value recovered results

### LPE

- Astles: POCO DFP-2 graphite; acid etch; boiling DI water one week; 500 °C bake; scratch-free hand-polished mating faces; shimmed slider rails; dual HgTe source paths; ~0.3 mg/min measured Hg loss.
- Chiang/Chen: independently heated Hg reservoir is a first-class thermochemical coordinate; separate reservoir temperatures and vapor paths must be recorded.
- Radhakrishnan: wipe clearance/non-smooth slide-out directly produce scratches, transient meltback/re-growth texture and residual melt; post-separation temperature is also consequential.
- Parker: holder/flow geometry can dominate terracing through hydrodynamic/supersaturation fields.

### CdZnTe

- Everson: executable `(111)B` defect screen: `6 cm³ 48% HF + 24 cm³ HNO3 + 150 cm³ lactic acid`, 2.5 min at room temperature with moderate agitation.
- Tobin: room-temperature lattice match is not identical to growth-temperature match.
- Tranchart: direct `y≈0.04 CdZnTe -> x≈0.30 HgCdTe` LPE evidence.

### Hg anneal

Chandra/Schaake/Kinch show annealed skin depth approximately proportional to `sqrt(t)` and use `x_B²/t` as a diffusion-like response coordinate dependent on composition, temperature and starting vacancy/excess-Te state. The x≈0.28 temperature series gives ~1.1-eV activation energy.

### Anodic oxide

- Stahle/Helms support the `0.1 M KOH / 90% EG / 10% water / 0.3 mA cm^-2` transfer center and a two-region oxide/interface structure.
- Nemirovsky/Kidron add constant-current formation followed by constant-voltage completion.
- Ngoc/Nha provide a 0.2–0.5 mA/cm² range, Pt counter-electrode branch and 77-K C-V interface metrics.

### RIE/LBIC

Siliquini 1997 anchors a complete same-UWA state:

`H2 27 sccm / CH4 5 sccm / 410 mTorr / 0.4 W cm^-2 / cathode 18 °C / printed dc bias 180 V / 60 s`.

Physical recession is ~0.2 µm while electrical conversion extends ~1.5 µm. The LBIC branch uses 1.047-µm CW excitation, ~3-µm spot, 2.5-µm scan step and destructive depth stripping. This strengthens P34/P37 but does not establish RP-01's 100-mTorr/50-W self-bias.

### Package thermal dynamics

Bartoli 1976 fits bonding-layer thermal conductance in HgCdTe PC arrays. Example values are approximately `3.2 W cm^-2 K^-1` for the short-time epoxy path and `0.9 W cm^-2 K^-1` for the long-time varnish path. These are PT priors, not RP-01/Dow-3110 constants.

## Critical non-promotions

Still not recovered:

- exact RP-01 LPE numerical boat/recess/well dimensions;
- source-synthesis ampoule dimensions/free volume;
- historical anodization electrode geometry;
- RP-01 RIE model/electrode area/RF frequency/self-bias/sample temperature;
- original evaporator geometry;
- original RP-01 cryostat/package/readout implementation.

No such `OPEN` coordinate is converted to `RP` by apparatus similarity.

## Important Round-61 refinement

Round 61 warned against inserting an unsupported acid graphite clean. Astles now provides primary HgCdTe-LPE transfer evidence. New rule:

> Acid-etched/boiling-DI/500 °C-baked graphite is a supported `PT` qualification branch; it is neither mandatory nor historical RP-01 identity.

## Current state

- Round-61 PDF remains the current typeset artifact.
- `ROUND62-FULLTEXT-EVIDENCE-INTEGRATION = COMPLETE`.
- `TRACEABLE-FIRST-BUILD-READY = NO` for an uninstantiated laboratory.
- `HISTORICAL-RP01-REPRODUCED = NO`.
- `END-TO-END-EMPIRICALLY-VALIDATED = NO`.

## Next documentary targets

1. Suh full slider-LPE paper.
2. Shinohara full Hg-loss/wipe-off paper.
3. Honeywell/Fermionics/UWA apparatus drawings/notebooks.
4. TI anodization-cell drawings.
5. UWA Plasma Technology run sheets/manuals.
6. Original RP-01 evaporator/QCM and cryostat/package records.

Do not restart a broad literature sweep before these are attempted.

When the next typeset EEFP revision is generated, integrate only the deltas frozen in the three controlling Round-62 documents above. Preserve Round-57/61 metrology definitions unless a recovered primary source directly requires correction.
# Source ledger addendum — Round 33: HgCdTe/CdZnTe singulation and die-edge damage

**Date:** 2026-08-16 America/New_York  
**Scope:** empirical separation of completed RP-01-like HgCdTe/CdZnTe devices into package-ready die; mechanical/chemical/functional edge damage; integration to P15/P33.

---

## R33-S1 — canonical RP-01

E. P. G. Smith, K. J. Winchester, C. A. Musca, J. M. Dell, L. Faraone, “A simplified fabrication process for HgCdTe photoconductive detectors using CH4/H2 reactive-ion-etching-induced blocking contacts,” *Semiconductor Science and Technology* 16, 455–462 (2001), DOI `10.1088/0268-1242/16/6/306`.

**Class:** `DIRECT-RP01`.

### Use

Defines completed detector stack and performance lineage.

### Negative result

The currently recovered/audited paper does not disclose:

- singulation/dicing method;
- final die outline;
- cut street;
- blade/wire/scribe/laser;
- protection/support;
- coolant/slurry;
- post-cut clean;
- edge exclusion or damage criterion.

**Disposition:** exact RP-01 singulation remains `OPEN-HISTORICAL`.

---

## R33-S2 — Rockwell HgCdTe detector-array mechanical-saw / excimer dicing patent

P. I. Zappella, Rockwell International, US5214261, “Method and apparatus for dicing semiconductor substrates using an excimer laser beam,” filed 13 Nov 1991, issued 25 May 1993.

**Class:** `PRIMARY-HGCDTE-DICING-TRANSFER`.

### Directly useful facts

The patent describes the contemporary conventional method for substrates/circuitry such as **mercury cadmium telluride or sapphire wafers** as a diamond-grit blade dicing saw similar to silicon-wafer dicing.

Reported shortcomings of that mechanical branch include:

- chipping/fracturing;
- poor dimensional/parallel-edge control;
- local frictional heating;
- degradation of electrical components;
- difficulty fabricating buttable HgCdTe detector-array die.

Excimer branch:

- deep-UV ablative photodecomposition;
- preferred XeCl source near `308 nm`;
- wafer/beam tilted several degrees out of normal, preferred about `5°`, to compensate taper;
- illustrated cut about `25 µm` wide;
- optional partially cured polyimide protection in the patented sapphire/CdTe/HgCdTe stack.

The patent compares detector figure of merit before/after dicing versus distance from cut. Its interpretation gives roughly `9–19 µm` mechanical-saw clearance and `0–6 µm` excimer clearance for no measured edge-pixel degradation in that specific architecture.

### Allowed use

- prove functional damage may extend beyond visible kerf;
- justify pre/post detector-performance testing versus edge distance;
- establish direct HgCdTe historical use/problems of mechanical blade dicing;
- justify laser branch as a candidate to qualify.

### Prohibited inference

Do not import the `9–19 µm`, `0–6 µm`, `308 nm`, `5°`, `25 µm` or polyimide details as RP-01 setpoints. The device architecture differs materially from LPE HgCdTe/CdZnTe RP-01.

---

## R33-S3 — Rockwell II–VI excimer ablation / stoichiometry control

P. D. Brewer, J. J. Zinck, Rockwell International, US5018164, “Excimer laser ablation method and apparatus for microcircuit fabrication,” issued 1991.

**Class:** `PRIMARY-II-VI-LASER-SURFACE-TRANSFER`.

### Directly useful facts

- applies to CdTe and explicitly discusses applicability to HgCdTe/CdZnTe;
- material removal and remaining surface composition depend on laser fluence;
- CdTe example uses KrF `248 nm`, `30 ns` pulses;
- preferential Cd/Te removal changes residual stoichiometry with fluence/pulse count;
- cites earlier HgCdTe excimer work showing severe local damage/mercury-nodule formation under unsuitable conditions.

### Permanent implication

`laser/non-contact != chemically benign`.

A P35 laser branch must qualify near-edge composition/surface state and detector function, not merely chipping.

### Prohibited inference

CdTe fluence thresholds/stoichiometric settings are not HgCdTe/CdZnTe P35 recipes.

---

## R33-S4 — finished CdZnTe array wire-saw process

S. S. Yoo, G. Jennings, P. A. Montano, “CdZnTe Array Detectors for Synchrotron Radiation Applications,” *Journal of Synchrotron Radiation* 5, 1332–1336 (1998), DOI `10.1107/S0909049598007237`.

**Class:** `PRIMARY-CZT-SINGULATION-TRANSFER`.

Primary full text: IUCr journal site.

### Direct process facts

After metallization:

- approximately `1×1 cm` CdZnTe sample;
- mounted on graphite with low-melting-point wax;
- photoresist applied over entire surface for protection;
- `125 mm` diameter stainless-steel wire saw;
- `16 µm` boron nitride slurry;
- cut extremely slowly to reduce chipping/wall damage;
- approximately `1 h` for one complete cut.

Post-cut process in that CdZnTe array:

- `5% Br in methanol`, `5 min` to etch wall damage;
- subsequent trichloroethylene, acetone and methanol cleaning.

### Allowed use

- direct evidence for low-force/slurry wire-saw family on a finished/metallized CdZnTe detector structure;
- empirical protection/support/cut-time anchor;
- evidence that wall damage required explicit treatment.

### Prohibited inference

Do **not** apply the `5% Br/methanol / 5 min` treatment, wax, photoresist, BN slurry or solvent sequence to a completed RP-01 HgCdTe device without local compatibility qualification.

The ~9.5-µm HgCdTe active layer, anodic oxide, RIE-defined n+ regions and Cr/Au make the material-removal budget completely different.

---

## R33-S5 — production CdZnTe wire-saw versus blade subsurface-damage evidence

C. Szeles, D. Bale, J. Grosholz Jr., G. L. Smith, M. Blostein, J. Eger, “Fabrication of high performance CdZnTe quasi-hemispherical gamma-ray CAPture Plus detectors,” Proc. SPIE 6319, 631909 (2006), DOI `10.1117/12.683552`.

**Class:** `PRIMARY-CZT-SINGULATION-TRANSFER`.

Author-uploaded full text recovered through the authors' publication page / indexed full text.

### Directly useful facts

The device-fabrication section states:

- low-damage high-precision wire-saw slicing/dicing still motivated removal of about a `100 µm` surface layer to eliminate surface/subsurface saw damage in their bulk CdZnTe detector-crystal process;
- blade slicing/dicing was described as generating deeper damage for which **several hundred micrometres** of material removal may be needed.

### Allowed use

Use as evidence that visible edge morphology can badly underestimate subsurface damage and that cutting technology materially changes damage depth.

### Prohibited inference

These post-saw material-removal depths are not finished-RP-01 edge-etch allowances. A completed ~9.5-µm HgCdTe device cannot tolerate an assumed 100-µm post-dice removal process.

---

## R33-S6 — same-UWA singulation search

Searches were performed across UWA institutional records using combinations of:

- HgCdTe + dicing;
- HgCdTe + singulation;
- HgCdTe + diamond saw;
- HgCdTe + wire saw;
- HgCdTe/CdZnTe + cut/cleave;
- Faraone/Musca/Dell + relevant terms.

Relevant UWA device papers were identified, including small HgCdTe detector arrays and contact/passivation work, but the publicly indexed records did **not** expose an executable UWA/RP-01 die-separation traveler.

**Class:** `NEGATIVE-SEARCH / HISTORICAL-TRAVELER-NOT-RECOVERED`.

This does not establish that UWA had no internal singulation process.

---

# Round-33 evidence hierarchy

Strongest direct process evidence by question:

| question | strongest current source | evidence status |
|---|---|---|
| exact RP-01 singulation | none | OPEN-HISTORICAL |
| HgCdTe mechanical-saw edge degradation | Rockwell US5214261 | PRIMARY-HGCDTE-DICING-TRANSFER |
| HgCdTe excimer alternative | Rockwell US5214261 | PRIMARY-HGCDTE-DICING-TRANSFER |
| laser-induced II–VI stoichiometry risk | Rockwell US5018164 | PRIMARY-II-VI-LASER-SURFACE-TRANSFER |
| finished CdZnTe protected wire-saw execution | Yoo et al. 1998 | PRIMARY-CZT-SINGULATION-TRANSFER |
| CdZnTe subsurface damage scale / wire-vs-blade warning | Szeles et al. 2006 | PRIMARY-CZT-SINGULATION-TRANSFER |
| UWA/RP-01 tool/settings | not recovered | OPEN-HISTORICAL |

---

# New permanent source-use rules from Round 33

1. Mechanical singulation is a device process, not neutral handling.
2. Visible chipping is not a bound on subsurface or functional damage.
3. Preserve `d_visible`, `d_functional`, and locally qualified `d_release` separately.
4. Do not transplant bulk-CdZnTe deep bromine damage-removal etches onto a completed RP-01 HgCdTe device.
5. Wire-saw/slurry/protection values from Yoo 1998 are transfer anchors, not RP-01 settings.
6. Laser separation can reduce mechanical damage while introducing chemical/stoichiometric damage; qualify both axes.
7. Tool age/dressing/wire state and coolant/slurry genealogy are process variables.
8. Scribe/cleave qualification must inherit P29 crystallographic plane/polarity/miscut and defect state.
9. Final P35 release requires P33 cryogenic edge-survival feedback.
10. “No visible edge damage” alone cannot release singulation.

# P14A — chlorobenzene single-layer lift-off lineage and RP-01 qualification addendum

**Status:** PROCESS-MECHANISM CLOSED / RP-01 RESIST PRODUCT AND DEVELOPER STILL OPEN. Supplements `P14_LITHOGRAPHY_MASK_GEOMETRY_CD_QUALIFICATION.md` and P09.

## 1. Purpose

Define what is genuinely known about the RP-01 Mask-2 photoresist/lift-off process and separate that from generic historical chlorobenzene lift-off recipes.

The RP-01 paper gives an unusually specific process fingerprint but does not disclose the resist product or developer. The correct response is to preserve those fields as open while using primary/historical lift-off literature to identify the physical mechanism and the variables that must be controlled during local transfer.

## 2. Direct RP-01 Mask-2 sequence

Smith et al. 2001 directly state that the photoresist masking layer used for the RIE/metal step was:

- approximately `4–5 µm` thick;
- pre-baked at `80 °C` for `30 min`;
- soaked in chlorobenzene for a further `30 min`;
- then patterned;
- developed;
- rinsed in water;
- retained during the CH4/H2 RIE passivant-opening process;
- retained for lift-off of the multi-metal stack `Cr 300 Å / Au 2700 Å`.

The same resist pattern therefore has to satisfy several requirements simultaneously:

1. survive the RIE exposure;
2. maintain the contact-window critical dimension/profile;
3. provide sufficient sidewall discontinuity/undercut for ~300 nm total metal lift-off;
4. strip without damaging the freshly formed RIE-modified contact region or Cr/Au contact.

## 3. Important sequence caution

The wording in RP-01 places the 30-min chlorobenzene treatment **before the sample is described as being patterned and developed**.

Historical chlorobenzene lift-off processes exist with chlorobenzene treatment either before or after UV exposure, depending on the resist/process architecture.

Therefore:

- do not silently reorder the RP-01 sequence to match a familiar fab recipe;
- during local transfer explicitly record whether chlorobenzene exposure occurs before exposure, after exposure, or in another sequence;
- if a screening DOE tests both orderings, they are different process branches and require separate recipe IDs.

## 4. Historical process mechanism

Classic single-layer optical lift-off work by Hatzakis and related IBM process-control studies established that chlorobenzene treatment of a positive diazo/novolak photoresist modifies the near-surface dissolution behavior during alkaline development.

The chlorobenzene-modified surface region develops more slowly than the underlying exposed resist, producing a negative sidewall / overhang / undercut profile suitable for metal lift-off.

Later patents and process studies explicitly describe the method as a single-layer **positive photoresist** lift-off process and identify diazo-type/novolak resist chemistry as the relevant class.

This mechanism is consistent with the function of the RP-01 chlorobenzene step.

### Evidence limitation

Mechanistic consistency does **not** identify the RP-01 resist as AZ1350J, AZ4000/AZ4110, Shipley 1400-series, S18xx, or any other commercial product.

Those products appear in historical chlorobenzene lift-off literature, but no recovered UWA/RP-01 source names one of them.

Exact RP-01 resist product remains `OPEN`.

## 5. Historical variables shown to control overhang

Historical chlorobenzene lift-off literature identifies the following as important variables:

- resist resin/sensitizer formulation;
- coated film thickness;
- residual casting solvent after soft bake;
- soft-bake temperature and time;
- chlorobenzene soak duration;
- chlorobenzene temperature;
- chlorobenzene purity/contamination and water content;
- whether soak occurs before or after exposure;
- exposure dose;
- developer identity/concentration;
- developer temperature;
- development duration;
- agitation;
- post-development bake/hardening if used.

These variables control penetration depth of the aromatic solvent and the developed sidewall/overhang profile.

Accordingly they are **mandatory P14 process fields**, not optional operator notes.

## 6. Resist-to-metal thickness ratio

RP-01 directly gives:

- resist thickness `t_PR ≈ 4–5 µm`;
- total Cr/Au thickness `t_metal = 0.03 + 0.27 = 0.30 µm`.

Therefore the nominal resist:metal thickness ratio is

- `4/0.30 ≈ 13.3`;
- `5/0.30 ≈ 16.7`.

So RP-01 operated at roughly a `13:1–17:1` resist-to-metal thickness ratio.

This is a useful geometric consistency condition but **does not prove successful lift-off by itself**. Metal continuity along a vertical or positively sloped sidewall can still defeat lift-off even when resist is much thicker than the deposited film.

## 7. Required profile metrology

During P14 qualification, measure the developed Mask-2 profile rather than merely recording photoresist thickness.

For representative contact-window features record:

- top opening width `CD_top`;
- substrate opening width `CD_bottom`;
- resist thickness `t_PR`;
- sidewall angle(s);
- lateral undercut per side `u`;
- overhang length at the top surface if resolvable;
- edge roughness;
- within-wafer and feature-to-feature variation.

Preferred methods during process development:

- cleaved cross-sectional SEM on sacrificial test coupons;
- stylus/optical profilometry where geometry permits;
- calibrated focus/phase-contrast microscopy for lateral opening differences;
- AFM or SEM for local edge morphology where needed.

No Mask-2 resist process should be released from film-thickness data alone.

## 8. RIE-survival gate

The developed resist profile must be measured both **before and after** the P08 RIE process on qualification coupons.

Record:

- pre-RIE resist thickness;
- post-RIE resist thickness;
- thickness loss / etch rate;
- change in undercut/overhang;
- contact-window CD change;
- cracking, blistering, edge rounding or hardening;
- residue on oxide/HgCdTe.

A profile that lifts off metal successfully before RIE but collapses or hardens during the 60-s plasma is not acceptable.

## 9. Metal-deposition profile gate

After depositing the RP-01 nominal stack on test coupons:

- Cr `30 nm`;
- Au `270 nm`;

inspect a cross section or high-resolution edge region to establish whether the metal on the substrate is discontinuous from the metal on top of the resist.

Required observations:

- no continuous metal fence bridging the resist sidewall;
- no severe shadowing that reduces the contact metal footprint below its intended CD;
- no gross resist reflow during deposition;
- no sputtered/redeposited RIE residue blocking adhesion.

This gate must be repeated if deposition directionality/tool geometry changes, even when resist chemistry is unchanged.

## 10. Lift-off qualification variables

Exact RP-01 lift-off solvent/time/agitation are not published.

Therefore the local process must explicitly log:

- lift-off solvent identity and lot;
- bath temperature;
- immersion time;
- static/agitated/ultrasonic state;
- ultrasonic power/frequency if used;
- number of solvent exchanges;
- rinse sequence;
- dry method;
- time from metal deposition to lift-off;
- final inspection results.

### HgCdTe/contact caution

Historical lift-off examples on other substrates often use acetone and sometimes ultrasonic agitation. Those examples are **not automatically transferable** to RP-01 HgCdTe/Cr-Au/RIE-modified contacts.

Ultrasonic lift-off in particular must be qualified for:

- contact-metal delamination;
- mesa-edge damage;
- bond-pad damage;
- particle redeposition;
- passivation damage.

## 11. Initial local resist-screening strategy

If the exact historical resist remains unrecoverable, do not choose one product and call it RP-01.

Instead create a local qualification branch, e.g. `P14-LOCAL-PRxx`, using positive diazo/novolak resists capable of reproducibly producing a 4–5 µm film and surviving the P08 plasma.

Screen at least the following process dimensions:

1. resist product/formulation;
2. spin condition required for `4–5 µm` measured thickness;
3. `80 °C / 30 min` bake as the historical center point, plus bounded bake sensitivity if needed;
4. chlorobenzene treatment near the historical `30 min` center point;
5. treatment order relative to exposure;
6. exposure dose;
7. developer chemistry/time;
8. resulting undercut/profile;
9. RIE profile survival;
10. Cr/Au lift-off yield and TLM outcome.

The selection criterion is not resemblance to the name of a 1980s resist. It is reproduction of the **functional process state** required by RP-01.

## 12. Proposed qualification acceptance metrics

Numerical production limits remain `QUAL`, but the following must be quantified:

- resist thickness mean/variation;
- undercut mean/variation;
- contact-window CD error relative to mask;
- resist thickness loss during RIE;
- fraction of contact windows with complete oxide opening;
- metal-edge fence/flake defect rate;
- lift-off residue/bridge defect rate;
- final metal CD;
- final TLM contact resistivity and I–V linearity;
- detector 1/f-noise and stability after processing.

A photoresist recipe is not accepted merely because optical microscopy shows a visually clean metal pattern.

## 13. Current historical closure status

### Directly closed by RP-01

- `t_PR≈4–5 µm`;
- prebake `80 °C / 30 min`;
- chlorobenzene `30 min`;
- pattern/develop/water rinse;
- same resist retained through RIE and Cr/Au lift-off;
- Cr/Au `30/270 nm`.

### Mechanistically closed by historical lift-off literature

- chlorobenzene treatment is a well-established single-layer positive diazo/novolak resist profile-modification method;
- it generates undercut/overhang via differential dissolution;
- final profile is sensitive to bake/solvent/developer/exposure variables.

### Still open

- RP-01 resist manufacturer/product;
- resist dilution/solids;
- spin speed/time/acceleration;
- exposure wavelength/dose/contact/proximity mode;
- developer manufacturer/product/concentration;
- development time/temperature/agitation;
- exact chlorobenzene temperature/purity/agitation;
- post-development delay to RIE;
- exact lift-off solvent/time/agitation;
- historical metal deposition pressure/rates/tool geometry.

These remain release blockers or local qualification variables.

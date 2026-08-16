# P08A — RIE gas-ratio provenance addendum

**Status:** CONTROLLED PROVENANCE UPDATE to `P08_RIE_BLOCKING_CONTACT_QUALIFICATION.md`.

**Precedence:** Where P08 says the gas-ratio interpretation is completely unknown, this addendum supplies newer evidence. It does **not** convert the individual flows into `CLOSED-P` direct RP-01 data.

## 1. Direct RP-01 data remain unchanged

Smith et al. 2001 directly publishes:

- chemistry notation: `CH4/5H2`;
- total flow: `64 sccm`;
- pressure: `100 mTorr`;
- RF power: `50 W`;
- duration: `60 s`.

The primary paper as currently audited does not explicitly state separate CH4 and H2 MFC values.

## 2. Strong secondary-source decoding

Srivastav, Pal and Vyas, “Overview of etching technologies used for HgCdTe,” *Opto-Electronics Review* 13(3), 197–211 (2005), Table 2, summarizes RF parallel-plate HgCdTe RIE conditions and explicitly prints:

`CH4:H2 = 1:5`

for the x≈0.31 LPE p-/n-HgCdTe mesa-isolation/type-conversion branch associated with the Smith/Musca/Faraone UWA process lineage.

The surrounding review discussion cites Smith et al. 1999, “Reactive ion etching for mesa structuring in HgCdTe,” JVST A 17, 2503–2509, DOI `10.1116/1.581988`.

### Evidence grade

`CH4:H2 = 1:5` is currently:

**`CANDIDATE-SECONDARY / SAME-LINEAGE-SUMMARY`**

not `CLOSED-P`.

Reason: the review table is clear about the explicit ratio but the accessible text extraction has degraded column alignment for several neighboring numeric fields. A clean primary UWA experimental section or archival reactor record is still preferred.

## 3. Derived RP-01 candidate individual flows

If the 1:5 ratio is the intended meaning of RP-01's `CH4/5H2`, then with total flow 64 sccm:

`Q_CH4 = 64/6 = 10.6667 sccm`

`Q_H2 = 5×64/6 = 53.3333 sccm`.

Tag both values:

**`[D from CLOSED-P total flow + CANDIDATE-SECONDARY ratio]`**.

Do not write “Smith et al. used 10.67 sccm CH4 and 53.33 sccm H2” as a direct literature statement.

## 4. Qualification use

These derived flows may be used as the **first qualification center point** in a reactor-transfer DOE only if:

1. each MFC is calibrated for its actual gas;
2. actual flows are recorded independently;
3. total flow is verified;
4. sample temperature, self-bias, pressure and reactor geometry are recorded;
5. P08 outcome metrology is performed:
   - oxide clear;
   - physical recession;
   - n+/Hall state;
   - LBIC electrical footprint/depth proxy;
   - P09 TLM/contact resistivity.

The local process is released from measured outcomes, not from the ratio notation alone.

## 5. Alternative interpretations rejected/unsupported

No supporting HgCdTe/UWA source was recovered for interpretations such as:

- `5% H2`;
- `5:1 CH4:H2`;
- arbitrary equal flows.

Do not use these unless new primary evidence emerges.

## 6. ~8-µm conversion-depth status unchanged

RP-01 cites prior n-type work indicating approximately 8 µm of n+ conversion below the surface under similar RIE conditions.

Correct primary lineage:

C. A. Musca, J. F. Siliquini, E. P. G. Smith, J. M. Dell, L. Faraone, “Laser Beam Induced Current Imaging of Reactive Ion Etching Induced n-Type Doping in HgCdTe,” *Journal of Electronic Materials* 27, 661–667 (1998), DOI `10.1007/s11664-998-0032-4`.

The UWA repository confirms that this paper extracts information about conversion depth and lateral extent for n-type MWIR HgCdTe.

However, the exact experimental condition corresponding to the ~8-µm value has not yet been recovered from accessible primary text.

Therefore retain:

`d_conv ≈ 8 µm` → **`P-OTHER-SOURCE / SIMILAR-CONDITIONS`**.

Do not use 8 µm as a production acceptance target without either:

- recovering and matching the primary experimental conditions; or
- locally measuring conversion depth/footprint under the transferred P08 process.

## 7. Search record

See:

`research/2026-08-15_rie_gas_split_source_recovery.md`

for detailed source/search reasoning and rejected interpretations.

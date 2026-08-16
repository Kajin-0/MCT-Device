# RP-01 gap matrix addendum — Round 18 empirical anodic oxide/passivation

**Date:** 2026-08-16 America/New_York  
**Scope:** P02/P25 native anodic-oxide process and passivation closure.

Status vocabulary:

- `CLOSED-DIRECT` — directly established for RP-01;
- `CLOSED-TRANSFER` — executable process value recovered from a strong non-RP-01 source;
- `PARTIAL` — useful empirical evidence exists but exact RP-01/local value remains unresolved;
- `OPEN` — no adequate value/procedure recovered;
- `LOCAL-QUALIFICATION` — must be established on the actual process/material;
- `NOT-A-SPEC` — diagnostic/reference value only.

---

| Process element | Current state | Evidence / value | Remaining action |
|---|---|---|---|
| RP-01 passivant identity | `CLOSED-DIRECT` | native anodic oxide | none |
| RP-01 oxide thickness | `CLOSED-DIRECT` | ~800 Å = 80 nm | establish local detector-derived tolerance/capability |
| RP-01 anodization bath | `OPEN` | not stated by Smith et al. | continue UWA/thesis recovery |
| executable HgCdTe transfer bath | `CLOSED-TRANSFER` | TI: 0.1 M KOH in 90% EG / 10% DI water | locally reproduce on x≈0.30 LPE |
| sample polarity | `CLOSED-TRANSFER` | HgCdTe is anode in TI process | freeze locally |
| transfer counter-electrode | `CLOSED-TRANSFER` | TI: carbon-rod cathode | qualify material/geometry; do not merge Pt lineage |
| later alternate cathode lineage | `NOT-A-SPEC` | Pt cathode appears in later oxide-conversion process | reference only |
| transfer control mode | `CLOSED-TRANSFER` | galvanostatic / constant current | locally calibrate source/logger |
| transfer current density center | `CLOSED-TRANSFER` | ~0.30 mA/cm² TI; direct experimental HgCdTe supports ~0.2–0.5 mA/cm² family | replicate center; derive local window from device response |
| transfer formation voltage | `CLOSED-TRANSFER` | ~15 V TI preferred condition | calibrate local V(t)-thickness relation |
| transfer process time | `CLOSED-TRANSFER / NOT-A-TIMER-SPEC` | ~2 min TI preferred condition | use as expectation only; V(t), Q/A and thickness control transfer |
| transfer film color | `CLOSED-TRANSFER / SECONDARY-METROLOGY` | uniform deep blue near ~800 Å in TI lineage | standardize viewing only if used; quantitative thickness remains primary |
| cell vessel material | `PARTIAL` | later lineages include Teflon; original preferred cell details incomplete in controlled record | select/freeze chemically compatible local vessel |
| counter-electrode area/separation | `OPEN/LOCAL-QUALIFICATION` | not sufficiently closed for RP-01 or TI production equivalence | dimension and freeze local geometry |
| exact exposed HgCdTe area | `LOCAL-QUALIFICATION` | required for J=I/A | fixture geometry + dimensional record |
| bath ratio preparation basis | `OPEN` | 90/10 convention not yet proven by mass vs volume for final production traveler | recover source or define local controlled convention |
| KOH/EG/water reagent grades | `OPEN/LOCAL-QUALIFICATION` | primary sources do not close manufacturing grades | select/freeze supplier/grade/lot controls |
| bath age/reuse rule | `OPEN/LOCAL-QUALIFICATION` | no released shelf-life | characterize V(t)/film drift vs bath age/use |
| bath temperature | `PARTIAL` | direct experimental work uses room-temperature anodization | record actual T; derive tolerance locally |
| agitation | `PARTIAL / CONTROLLED` | x≈0.30 mechanism work shows strong mass-transport effect; static bath selected as first transfer condition | explicitly freeze and record; quantify only if needed |
| pre-anodization surface | `OPEN-RP01 / CRITICAL-LOCAL` | surface history changes induction/interface; literature etches differ and can be too aggressive | select P01/P07-compatible minimal-removal clean and qualify |
| pre-anodization Br2 chemistry | `NOT-A-SPEC` | 1% Br2/EG and aggressive Br2/MeOH appear in other studies | do not transplant into 9.5-µm RP-01 layer |
| induction time `t_ind` | `LOCAL-QUALIFICATION` | x≈0.30 anodization mechanism shows induction/dissolution stage | extract from every V(t) trace |
| V(t) growth fingerprint | `LOCAL-QUALIFICATION` | TI reports reproducible voltage rise; x≈0.30 work supports diagnostic value | establish reference envelope after center replication |
| charge/area `Q/A` | `LOCAL-QUALIFICATION` | exact calculable process record | record and correlate with thickness/interface outcome |
| post-anodization rinse | `OPEN` | exact RP-01/TI production sequence not closed | define/freeze local rinse after source recovery/qualification |
| post-anodization dry | `OPEN` | not closed | define/freeze locally |
| oxide thickness metrology | `PARTIAL-CLOSED` | TI lineage used profilometry/interference; modern ellipsometry also possible | choose calibrated local method and MSA |
| oxide optical/color metrology | `NOT-A-SPEC` | useful operator indicator only | correlate with measured d_ox; never release by color alone |
| oxide chemistry on x≈0.30 | `PARTIAL-CLOSED` | primary chemistry study shows strong pH/J/EG dependence | use as process-change warning; local chemistry characterization optional unless failures arise |
| interface-state density | `LOCAL-QUALIFICATION` | other-x native-oxide work gives scale ~5e11 cm^-2eV^-1 near midgap | do not copy numerical target; select electrical interface metric if needed |
| fixed oxide charge | `LOCAL-QUALIFICATION` | other-x scale ~6e11 cm^-2 positive | do not copy target; infer only with stated model |
| accumulation/shunting optimum | `LOCAL-QUALIFICATION` | same-UWA x≈0.23 gate study proves non-monotonic tradeoff; 50/72 mV and ~70% response gain are transfer-only | optimize detector response/noise on RP-01 geometry |
| mesa-sidewall coverage | `LOCAL-QUALIFICATION` | P02C; same-UWA photoconductor evidence shows sidewall importance | perimeter-sensitive/device test required |
| oxide-to-P08 clear compatibility | `LOCAL-QUALIFICATION` | 80-nm film is later RIE-opened | determine clear time/residual/recession for actual oxide/process |
| anodization-to-resist delay | `OPEN/LOCAL-QUALIFICATION` | not historical closed | record and freeze after stability study |
| passivation thermal/storage stability | `LOCAL-QUALIFICATION` | other architectures show aging/thermal sensitivity | characterize actual native oxide stack; no borrowed universal bake limit |
| exact UWA same-lineage native-oxide recipe | `OPEN` | bibliographic sources identified but experimental traveler still inaccessible | continue proceedings/thesis/archive recovery |
| White 2005 thesis full text | `PARTIAL / ACCESS-BLOCKED` | institutional record + PDF URL found; direct PDF access returned 403 | retry alternate institutional/archive route |
| Westerhout 2013 thesis full text | `PARTIAL / ACCESS-BLOCKED` | institutional record + PDF URL found; direct PDF access returned 403 | alternate archive route if useful |
| Smith et al. 2000 dry-plasma full text | `PARTIAL / OPEN` | same-UWA paper identified, IEEE document 939185 | recover before final P24 reactor closure |

---

# Highest-value remaining P25 closures

The process is now executable enough for a local transfer experiment, but final manual release still needs these practical items:

1. exact local bath preparation convention and reagent grades;
2. counter-electrode dimensions/separation and exposed-area definition;
3. RP-01-compatible final surface clean immediately before anodization;
4. post-anodization rinse/dry;
5. local V(t)/Q/A/thickness repeatability on x≈0.30 LPE;
6. sidewall functional closure;
7. electrical-interface/noise closure;
8. P08 oxide-clear compatibility;
9. storage/thermal-history stability;
10. P17 repeated-run capability.

# Consequence for manual readiness

Before Round 18, the native-oxide module contained an 80-nm historical target and a plausible transfer recipe.

After Round 18, it contains a **practical process architecture with actual cell polarity/cathode lineage, bath chemistry, current density, endpoint behavior, visual/thickness metrology, V(t) diagnostics, interface-device tradeoffs, sidewall requirements, and a full traveler**.

The primary unresolved question is no longer “how could one anodize HgCdTe?” It is “which exact implementation reproduces the required RP-01 detector surface state and remains statistically stable in the local apparatus?”

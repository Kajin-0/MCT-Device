# RP-01 gap matrix addendum — Round 26

**Date:** 2026-08-16 America/New_York  
**Scope:** P05 audit and empirical cryogenic package closure.

| Variable / evidence item | RP-01 historical status | Best current evidence | Evidence class | Current action |
|---|---|---|---|---|
| Hall/VdP execution sequence | RP-01 details partial | P05 already operationally complete | CONTROLLED-METROLOGY | Do not create redundant Hall module |
| Historical Hall-contact fabrication | OPEN | Indium common in HgCdTe literature; no exact RP-01 material-control traveler | OPEN / TRANSFER | Keep open; qualify locally if needed |
| Final Hall acceptance windows | OPEN | RP-01 reference n/µ only | QUAL | Derive from device sensitivity/capability |
| RP-01 die singulation | OPEN | P15 framework only | OPEN | Local empirical qualification |
| RP-01 die outline / CdZnTe carrier thickness | OPEN | No direct source recovered | OPEN | Record measured geometry |
| RP-01 die-attach identity | OPEN | Honeywell silicone-rubber family; NRL epoxy stack | PRIMARY-TRANSFER | Screen construction families, do not assign history |
| Silicone attachment family | Not RP-01-proven | Honeywell US4081819A: Dow Corning 3110/3112/3116 examples | PRIMARY-HONEYWELL | Strong compliant-attach transfer branch |
| Cryogenic cracking mechanism | Not specified in RP-01 | Honeywell controlled adhesive/abrasion/thermocompression experiment | PRIMARY-HONEYWELL | Attachment compliance/thermal path required gate |
| Honeywell 5-g / 40-g thermocompression values | Not RP-01 | Controlled cracking experiment | PRIMARY-TRANSFER | Experimental context only; not bond setpoints |
| Bondline thickness | OPEN | No directly matched RP-01 value | OPEN / LOCAL-QUAL | Measure actual thickness/voiding per build |
| Exact epoxy product for HgCdTe PC thermal stack | OPEN | US4012691A says epoxy, identity not given | PRIMARY-HGCDTE-PC | Keep product OPEN |
| HgCdTe photoconductor support | OPEN for RP-01 | NRL: Irtran 2 or sapphire | PRIMARY-HGCDTE-PC | Candidate support family only |
| Support-to-copper interface | OPEN for RP-01 | NRL: GE 7031 varnish | PRIMARY-HGCDTE-PC | Transfer architecture only |
| Cold heat sink temperature | RP-01 detector ~80 K | NRL photoconductor stack at 77 K | PRIMARY-HGCDTE-PC | Strong thermal-test reference |
| Package thermal time constants | Not disclosed | NRL/Bartoli: several ms + hundreds ms due to bonding layers | PRIMARY-HGCDTE-PC | Mandatory package transient characterization |
| Package thermal de-embedding from P13 | Not historical | Required by primary construction evidence | DERIVED-CONTROL | Add `H_pkg,thermal` / thermal kernel |
| Thin-HgCdTe CTE stress | Not disclosed | US5462882A 5–10-µm HgCdTe/epoxy/Si damage | PRIMARY-HYBRID-TRANSFER | Package thermal budget and CTE gate |
| Carrier CTE matching | OPEN | US5365088A sapphire buffer improves HgCdTe/Si thermal mismatch | PRIMARY-HYBRID-TRANSFER | Record carrier CTE/material; qualify cycling |
| RP-01 wire/ribbon metallurgy | OPEN | Other HgCdTe uses In solder/Mo/AuGe/etc. | TRANSFER ONLY | Do not transplant into Cr/Au chain |
| RP-01 bond method/force/ultrasonic/time | OPEN | No matched source recovered | OPEN | Local coupon DOE; record full bonder program |
| Contact/interconnect-induced cryogenic noise | OPEN | Other HgCdTe contact families show cryogenic contact/noise sensitivity | PRIMARY-TRANSFER | P12 pre/post package gate |
| RP-01 cold shield/aperture | OPEN | historical 60° FOV does not specify geometry | OPEN | Measure installed geometry and throughput |
| RP-01 window/filter | OPEN | no matched package source | OPEN | Trace installed transmission |
| RP-01 vacuum level | OPEN | no matched source | OPEN | Record pressure/pump history |
| RP-01 package bake | OPEN | UWA/HgCdTe literature warns thermal history can change device state | TRANSFER / QUAL | Keep inside detector-qualified thermal budget |
| RP-01 thermal-cycle history | OPEN | CTE-mismatch literature establishes cycle dependence | PRIMARY-TRANSFER | Track cycle genealogy and post-cycle metrics |

---

## Round-26 closure result

P15 now has an empirical execution supplement, P33, but no RP-01 package construction can yet be labeled historical.

The strongest experimentally supported package principle is:

`mechanical compliance / CTE compatibility <-> bondline thermal conductance <-> detector thermal/noise response`.

A construction must pass all three axes; optimizing only adhesive strength is not sufficient.

---

## Highest remaining package blockers

1. exact RP-01 die attach and carrier;
2. bondline thickness/coverage;
3. wire/ribbon and bond process;
4. Dewar/header/cold-shield/window geometry;
5. vacuum/bake history;
6. measured local package thermal response;
7. independent-build thermal-cycle capability.

These are explicit empirical qualification variables rather than undocumented assumptions.

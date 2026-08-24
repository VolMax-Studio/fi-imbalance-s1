# `fi-imbalance-s1`: Independent Open-Telemetry Verification of Finnish Imbalance Price Spikes

[![License: CC BY 4.0](https://img.shields.io/badge/Data_License-CC_BY_4.0-blue.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Audit Status: Verified with Limitations](https://img.shields.io/badge/Audit_Status-Verified_with_Limitations-brightgreen.svg)](#verdict-summary)
[![Pre-Registration: Frozen](https://img.shields.io/badge/Pre--Registration-Frozen_Pre--Ingestion-success.svg)](./PARAMS.md)

This repository contains the deterministic, independent open-telemetry verification instance for public claims regarding the **Finnish Imbalance Price Spikes of 3 and 5 August 2026** under Fingrid's 15-minute settlement mechanism (effective 1 June 2026).

The source claim analyzed is the market commentary published by **Dr. Priyanka Shinde** (PhD in energy markets | Montel Analytics) regarding price spikes, aFRR/mFRR balancing activations, intraday wind forecast errors, and aggregate Battery Energy Storage System (BESS) responses.

---

## 1. Governance & Epistemological Protocol

To eliminate post-hoc confirmation bias, this audit strictly adheres to the **Pre-Registration Prior to Telemetry Ingestion** protocol:
1. **Pre-Registration Commits (`c1`–`c4`):** Data licenses, parameters, 8 disambiguation time-window branches, mathematical pricing formulas, dataset ID mappings, and sub-claim decomposition were **committed and pushed to GitHub before pulling a single byte of telemetry data**.
2. **Fixed Outcome Vocabulary:** All verdicts map strictly to a formal 6-term ontology:
   $$\text{Ontology} \in \{\text{Verified}, \text{Verified with Limitations}, \text{Not Verified}, \text{Not Demonstrated}, \text{Unfalsifiable-as-Stated}, \text{Deferred}\}$$
3. **Escrow Integrity:** Raw API payloads are stored in local escrow under SHA-256 digests recorded in [`data_manifest.json`](./data_manifest.json).

---

## 2. Verdict Summary

| Claim ID | Verbatim Topic | Observed Telemetry | Benchmark Target | Verdict | Operational Note |
|:---:|---|:---:|:---:|:---:|---|
| **`FI-01`** | 3 Aug 09:15 EEST Imbalance Price | `600.00 EUR/MWh` | `600.00 EUR/MWh` | **`VERIFIED`** | Exact match on Fingrid Dataset 319 |
| **`FI-02a`** | 3 Aug mFRR Need | `469.0 MW` | `469.0 MW` | **`VERIFIED`** | Fingrid Dataset 377 (Need Estimate) |
| **`FI-02b`** | 3 Aug Upward Activation Sum | `424.0 MW` | `424.0 MW` | **`VERIFIED`** | Fingrid Dataset 375 (Quarter-hour peak power) |
| **`FI-02c`** | 3 Aug SE1/SE3 Cross-Border Import | `46.8 MW` import | `45.0 MW` residual | **`VERIFIED_WITH_LIMITATIONS`** | $\Delta = 1.8\text{ MW} \le 10.0\text{ MW}$ pre-registered instrument boundary |
| **`FI-03`** | 5 Aug 08:30 EEST Imbalance Price | `718.81 EUR/MWh` | `718.0 EUR/MWh` | **`VERIFIED`** | Integer rounding in source claim |
| **`FI-04a`** | 5 Aug Upward aFRR Non-Zero | `26.02 MW` | $> 0\text{ MW}$ | **`VERIFIED`** | Marginal (`24.23 MW`) + Local (`1.80 MW`) |
| **`FI-04b`** | 5 Aug mFRR Import from SE | `0.0 MW` | `0.0 MW` | **`VERIFIED`** | Datasets 378 & 379 confirm zero import |
| **`FI-05`** | 5 Aug Intraday Wind Forecast Error | `320.4 MW` | $\ge 300.0\text{ MW}$ | **`VERIFIED`** | Actual: `473.6 MW` vs Forecast: `794.0 MW` |
| **`FI-06`** | BESS Grid Discharge Response | 3 Aug: `117 → 233 MW`<br>5 Aug: `47 → 244 MW` | Peak $> \text{Med} + 20\text{ MW}$<br>Peak $\ge 1.5\times\text{Med}$ | **`VERIFIED`** | Measured aggregate physical grid injection |
| **`FI-07`** | Proprietary Forecast Early Warning | *Unrecorded in public data* | *N/A* | **`UNFALSIFIABLE-AS-STATED`** | Commercial forecast outputs are unrecorded |

**Overall Audit Status:** **`Verified with Limitations`** (8 Verified, 1 Verified with Limitations, 1 Unfalsifiable-as-Stated, 0 Discrepant).

---

## 3. Scope Boundaries & Epistemic Limitations

1. **Aggregate Grid Telemetry vs. Asset-Level Causation:**  
   The observed BESS discharge increase (rising from 47 MW to 244 MW on 5 Aug) measures **aggregate physical grid injection across Finland** (Dataset 398). It does **not** prove individual asset operator intent or price causation, and we make no causal assertion.
2. **Public Market Telemetry vs. Commercial Models:**  
   Claim `FI-07` asserts proprietary forecast advance warning. Because commercial private vendor forecasts are unrecorded in transmission telemetry, this claim is declared `UNFALSIFIABLE-AS-STATED`.
3. **Dataset Revisions:**  
   Telemetry hashes in `data_manifest.json` correspond to the data pulled on **2026-08-24 (UTC)**. If Fingrid executes post-hoc settlement recalculations, checksums may differ.

---

## 4. How to Independently Reproduce

Any third party can reproduce the full verification in 3 steps:

### Step 1: Clone & Configure API Access
Obtain a free API key from the [Fingrid Open Data Developer Portal](https://developer-data.fingrid.fi/):
```bash
git clone https://github.com/VolMax-Studio/fi-imbalance-s1.git
cd fi-imbalance-s1
export FINGRID_API_KEY="your_api_key_here"
```

### Step 2: Fetch Raw Telemetry
Pulls all 26 canonical datasets across the target evaluation range (`2026-08-02` to `2026-08-06`) into `data/` with rate-limit backoff:
```bash
python3 scripts/fetch_telemetry.py
```

### Step 3: Run Cold Verification
Executes the deterministic evaluation pipeline against pre-registered rules and verifies manifest integrity:
```bash
python3 reproduce.py
```
Output results will be written to `results.json` and `VERDICT.json`.

---

## 5. Primary Attribution & Data Sources

- **Telemetry Source:** [Fingrid Open Data](https://data.fingrid.fi) operated by Fingrid Oyj under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
- **Source Market Commentary:** Dr. Priyanka Shinde (PhD in energy markets | Montel Analytics), LinkedIn post published August 2026. Verbatim text preserved in [`SOURCE_POST.md`](./SOURCE_POST.md).
- **Audit Implementation:** VolMax Studio Open Verification Architecture (`fi-imbalance-s1`).

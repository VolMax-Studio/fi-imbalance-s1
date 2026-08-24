#!/usr/bin/env python3
"""
Canonical Pre-Registration Package Generator for fi-imbalance-s1.
Generates METHODOLOGY_PIN.md, PARAMS.md, claims.json, and SOURCE_POST.md.
"""

import os
import json

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

METHODOLOGY_CONTENT = """# Normative Methodology Pin (Fingrid Imbalance Pricing 1 June 2026)

> **Source Organization:** Fingrid Oyj  
> **Official Title:** *Change in determining the imbalance price for balance responsible parties in June 2026*  
> **Publication Date:** 2026-04-27  
> **Effective Date:** 2026-06-01  
> **Canonical URL:** `https://www.fingrid.fi/en/news/news/2026/change-in-determining-the-imbalance-price-for-balance-responsible-parties-in-june-2026/`  
> **Access Date (UTC):** 2026-08-24  

---

## 1. Exact Verbatim Text from Fingrid Release

```text
Imbalance pricing for balance responsible parties will be changed to volume-weighted 1 June 2026.

The imbalance price is volume-weighted when the activated mFRR and satisfied demand for aFRR in Finland are both in the dominating direction. The dominating direction remains unchanged, i.e. it is based only on mFRR activations.

If mFRR has not been activated in the dominating direction in Finland, the imbalance price will be formed as at present, i.e. the largest of the mFRR marginal price and the volume-weighted aFRR price. Correspondingly, if the dominating direction is downwards, the smaller of these components will determine the imbalance price.

If there is no decisive mFRR direction at all during a market time unit, the imbalance price will be the price based on the Day-ahead price, even if aFRR activations have been made during the period in question.
```

---

## 2. Mathematical Formalization of Pricing Rules

Let:
- $D \\in \\{-1, 0, 1\\}$ be the dominating direction (Dataset 369).
- $V_{\\text{mFRR, up}}$ (Dataset 375 - Maximum power of quarter hour), $V_{\\text{mFRR, down}}$ (Dataset 376) be activated mFRR power indicators.
- $V_{\\text{aFRR, up}} = \\text{DS\\_349} + \\text{DS\\_354}$ (Total satisfied demand for aFRR upwards: marginal price volume + local selection volume).
- $P_{\\text{mFRR, marginal}}$ (Dataset 400/401) be the marginal mFRR activation price.
- $P_{\\text{aFRR, VWAP}}$ (Dataset 347/348) be the volume-weighted average aFRR price.

### 2.1 Case 1: Dominating Direction Up ($D = 1$) and $V_{\\text{aFRR, up}} = 0$ (Event 1, 2026-08-03)
- **Branch A (Priyanka Interpretation):** $\\text{Price}_A = P_{\\text{mFRR, SA/DA}}$
- **Branch B (Literal Textual Rule):** $\\text{Price}_B = \\max(P_{\\text{mFRR, marginal}}, P_{\\text{aFRR, VWAP}})$

### 2.2 Case 2: Dominating Direction Up ($D = 1$) and $V_{\\text{aFRR, up}} > 0$ (Event 2, 2026-08-05)
- **Mathematical Volume-Weighted Formula (Theoretical):**
  $$\\text{Price} = \\frac{V_{\\text{mFRR, up}} \\cdot P_{\\text{mFRR}} + V_{\\text{aFRR, up}} \\cdot P_{\\text{aFRR, VWAP}}}{V_{\\text{mFRR, up}} + V_{\\text{aFRR, up}}}$$
- **Telemetry Operationalization Caveat:** Because Fingrid Dataset 375 publishes maximum power of the quarter hour (MW) rather than aggregate energy volume (MWh), the theoretical volume-weighted reconstruction is evaluated as an approximation against published Dataset 319.

---

## 3. Amendment Ledger

- **Amendment #1 (2026-08-24):** Replaced draft text with exact verbatim wording transcribed from the official Fingrid news release (URL: `https://www.fingrid.fi/en/news/news/2026/change-in-determining-the-imbalance-price-for-balance-responsible-parties-in-june-2026/`) and verified character-identical against source on 2026-08-24.
"""

PARAMS_CONTENT = """# Frozen Execution Parameters (fi-imbalance-s1)

> **Document Status:** SPREMNO ZA GEJT (Draft)  
> **Instance:** `fi-imbalance-s1`  
> **Target Event Dates:** 2026-08-03 and 2026-08-05  
> **Canonical Portal:** `https://data.fingrid.fi`  
> **Date of Pre-Registration (UTC):** 2026-08-24  

---

## 1. Target Event Matrix (8 Disambiguation Branches)

Because the source claim uses colloquial timezone phrasing ("EET") during summer daylight saving time (when Finland observes EEST / UTC+3) and does not state whether timestamp labels represent interval beginnings or endings, all 8 branches ($2\\text{ events} \\times 2\\text{ timezones} \\times 2\\text{ interval semantics}$) are pre-registered and evaluated:

### Event 1: 2026-08-03 (Declared "9:15 am EET")
- **Branch 1.1 (Primary Physical):** `EEST (UTC+3)` $\\times$ `Interval-Beginning` $\\to$ `[2026-08-03T06:15:00Z, 2026-08-03T06:30:00Z)`
- **Branch 1.2 (Alternative Physical):** `EEST (UTC+3)` $\\times$ `Interval-Ending` $\\to$ `[2026-08-03T06:00:00Z, 2026-08-03T06:15:00Z)`
- **Branch 1.3 (Author Literal EET):** `EET (UTC+2)` $\\times$ `Interval-Beginning` $\\to$ `[2026-08-03T07:15:00Z, 2026-08-03T07:30:00Z)`  
  *(Note: Finland was on EEST/UTC+3 on this date; this branch evaluates author mental reference without DST conversion)*
- **Branch 1.4 (Author Literal EET Ending):** `EET (UTC+2)` $\\times$ `Interval-Ending` $\\to$ `[2026-08-03T07:00:00Z, 2026-08-03T07:15:00Z)`  
  *(Note: Finland was on EEST/UTC+3 on this date; this branch evaluates author mental reference without DST conversion)*

### Event 2: 2026-08-05 (Declared "8:30 EET")
- **Branch 2.1 (Primary Physical):** `EEST (UTC+3)` $\\times$ `Interval-Beginning` $\\to$ `[2026-08-05T05:30:00Z, 2026-08-05T05:45:00Z)`
- **Branch 2.2 (Alternative Physical):** `EEST (UTC+3)` $\\times$ `Interval-Ending` $\\to$ `[2026-08-05T05:15:00Z, 2026-08-05T05:30:00Z)`
- **Branch 2.3 (Author Literal EET):** `EET (UTC+2)` $\\times$ `Interval-Beginning` $\\to$ `[2026-08-05T06:30:00Z, 2026-08-05T06:45:00Z)`  
  *(Note: Finland was on EEST/UTC+3 on this date)*
- **Branch 2.4 (Author Literal EET Ending):** `EET (UTC+2)` $\\times$ `Interval-Ending` $\\to$ `[2026-08-05T06:15:00Z, 2026-08-05T06:30:00Z)`  
  *(Note: Finland was on EEST/UTC+3 on this date)*

---

## 2. Canonical Fingrid Open Data Dataset Pinning & Primary Roles

All datasets are pinned to the single canonical portal `https://data.fingrid.fi`:

| Dataset ID | Verbatim Name | Resolution | Verbatim Unit | Operational Role & Hierarchy |
|:---:|---|:---:|:---:|---|
| **`319`** | `Imbalance price` | 15 min | `EUR/MWh` | **Primary:** Settlement price for FI-01 (600 €) and FI-03 (718 €) |
| **`75`** | `Wind power generation - 15 min data` | 15 min | `MW` | **Primary:** Actual wind production (interval-ending 15-min average) |
| **`245`** | `Wind power generation forecast - updated every 15 minutes` | 15 min | `MWh/h` | **Primary:** Rolling intraday wind forecast (consolidated published series) |
| **`246`** | `Wind power generation forecast - updated once a day` | 15 min | `MWh/h` | **Corroborating:** Day-ahead wind forecast reference |
| **`369`** | `Dominating direction in the mFRR energy market in Finland` | 15 min | `-1, 0, 1` | **Primary:** Direction signal (-1=down, 1=up, 0=none) |
| **`377`** | `mFRR need` | 15 min | `MW` | **Primary:** Fingrid estimate for mFRR need for FI-02a (469 MW claim) |
| **`375`** | `Activated mFRR balancing regulation upward sum` | 15 min | `MW` | **Primary:** Upward balancing power (SA + DA max power) for FI-02b (424 MW claim) |
| **`385`** | `Activated mFRR balancing regulation SA upward sum` | 15 min | `MW` | **Corroborating:** Scheduled activation upward breakdown |
| **`390`** | `Activated mFRR balancing regulation DA upward sum` | 15 min | `MW` | **Corroborating:** Direct activation upward breakdown (max power) |
| **`378`** | `mFRR flow FI-SE1` | 15 min | `MW` | **Primary:** Balancing flow on border FI-SE1 (+ export, - import) |
| **`379`** | `mFRR flow FI-SE3` | 15 min | `MW` | **Primary:** Balancing flow on border FI-SE3 (+ export, - import) |
| **`381`** | `Net export / import of mFRR energy` | 15 min | `MW` | **Corroborating:** Net cross-border mFRR flow |
| **`347`** | `aFRR energy volume weighted average price, up` | 15 min | `EUR/MWh` | **Primary:** aFRR upward VWAP price |
| **`348`** | `aFRR energy volume weighted average price, down` | 15 min | `EUR/MWh` | **Primary:** aFRR downward VWAP price |
| **`349`** | `aFRR energy activation volume with marginal price, up` | 15 min | `MW` | **Primary (Component 1):** aFRR upward marginal activation volume |
| **`350`** | `aFRR energy activation volume with marginal price, down` | 15 min | `MW` | **Primary (Component 1):** aFRR downward marginal activation volume |
| **`353`** | `aFRR energy activation volume local selection, down` | 15 min | `MW` | **Primary (Component 2):** aFRR downward local selection volume |
| **`354`** | `aFRR energy activation volume local selection, up` | 15 min | `MW` | **Primary (Component 2):** aFRR upward local selection volume |
| **`398`** | `Battery energy storage systems discharging power - real-time data` | 3 min | `MW` | **Primary:** Grid-directed aggregate BESS discharge power |
| **`399`** | `Battery energy storage systems charging power - real-time data` | 3 min | `MW` | **Corroborating:** Battery-directed aggregate BESS charge power |
| **`400`** | `mFRR Scheduled activation price - real-time` | 15 min | `€/MWh` | **Primary:** Scheduled activation price |
| **`401`** | `mFRR direct activation price up - real-time` | 15 min | `€/MWh` | **Primary:** Direct activation price up |
| **`402`** | `mFRR direct activation price down - real-time` | 15 min | `€/MWh` | **Primary:** Direct activation price down |
| **`403`** | `Transmission of electricity between Finland and Central Sweden...` | 15 min | `MWh` | **NOT_SUBSTITUTABLE_FOR: FI-02, FI-04** (Physical schedule flow $\\neq$ balancing flow) |
| **`404`** | `Transmission of electricity between Finland and Northern Sweden...` | 15 min | `MWh` | **NOT_SUBSTITUTABLE_FOR: FI-02, FI-04** (Physical schedule flow $\\neq$ balancing flow) |

### Dataset 369 Semantic Caveats
- **Temporal Unit Notice:** The textual description for Dataset 369 refers to dominating direction "for each hour", whereas the publication cadence is 15 minutes. The 15-minute resolution governs.
- **Direction Value Zero Notice:** `0` encodes both "no mFRR activation occurred" and "equal upward and downward activations occurred". Both conditions satisfy Fingrid's rule for Day-Ahead fallback.

---

## 3. Mathematical Formalization of Pricing Rules

### 3.1 Event 1 (2026-08-03): Zero-aFRR Branching
Total satisfied aFRR upward demand is defined as:
$$V_{\\text{aFRR, up}} = \\text{DS\\_349} + \\text{DS\\_354}$$

When $D = 1$ and $V_{\\text{aFRR, up}} = 0$:
- **Price Branch A (Priyanka Interpretation):** $\\text{Price}_A = P_{\\text{mFRR, SA/DA}}$
- **Price Branch B (Literal Textual Rule):** $\\text{Price}_B = \\max(P_{\\text{mFRR, marginal}}, P_{\\text{aFRR, VWAP}})$

### 3.2 Event 2 (2026-08-05): Non-Zero aFRR Upward Activation
When $D = 1$ and $V_{\\text{aFRR, up}} > 0$:
- **Theoretical Volume-Weighted Price:**
  $$\\text{Price} = \\frac{V_{\\text{mFRR, up}} \\cdot P_{\\text{mFRR}} + V_{\\text{aFRR, up}} \\cdot P_{\\text{aFRR, VWAP}}}{V_{\\text{mFRR, up}} + V_{\\text{aFRR, up}}}$$
- **Operationalization Notice:** Evaluated as an approximation against published Dataset 319 due to Dataset 375 publishing maximum MW power of the quarter hour rather than MWh energy volume.

---

## 4. Revision & Ingestion Rule (B-5)

- **Status:** `REVISION_RULE = UNRESOLVED_NORMATIVE_PIN`
- **Execution Rule:** All raw API responses are persisted under SHA-256 digests with exact `retrieved_at_utc` timestamps.
- **Evidence Policy:** Any future data modification observed from Fingrid will be published as an append-only revision record.

---

## 5. Wind Forecast Error Operationalization & Lower-Bound Bias (FI-05)

- **Target Forecast Horizon:** The 15-minute interval corresponding to Event 2.
- **Forecast Ingestion:** Dataset 245 publishes a single consolidated rolling series per target interval without explicit issuance/vintage timestamps.
- **Lower-Bound Bias Declaration:** Because later forecast vintages closer to real-time are monotonically more accurate than earlier vintages, the forecast error measured from the consolidated Dataset 245 constitutes a strict lower bound on the error relative to any pre-gate-closure vintage.
- **Unit Equivalence:** $1\\text{ MWh/h} \\equiv 1\\text{ MW}$ average power over a 15-minute interval.
- **Error Formula:** $\\text{Forecast Error (MW)} = |\\text{Forecast (DS 245)} - \\text{Actual (DS 75)}|$.
- **Evaluation Criterion:** $\\text{Forecast Error} \\ge 300.0\\text{ MW}$.

---

## 6. BESS Response Operationalization (FI-06)

- **Event Window:** $[T_{\\text{event}} - 30\\text{ min}, T_{\\text{event}} + 30\\text{ min}]$ (20 3-minute intervals).
- **Baseline Period:** Preceding 2 hours $[T_{\\text{event}} - 150\\text{ min}, T_{\\text{event}} - 30\\text{ min}]$ (40 3-minute intervals).
- **Baseline Metric:** $\\text{Median}(\\text{Discharge MW})$ from Dataset 398.
- **Spike Condition:** $\\max(\\text{Event Window Discharge}) \\ge \\text{Baseline Median} + 20.0\\text{ MW}$ AND $\\ge 1.50 \\times \\text{Baseline Median}$.
- **Charging Power:** Monitored descriptively via Dataset 399.
- **Scope Limit & Data Caveat:** Evaluates aggregate grid-level physical injection; does NOT infer asset-level intent or price causation. Dataset 398 carries an official notice that data may contain errors due to measurement freezing.

---

## 7. Instrument Dissonance Pre-Registration (FI-02 Series)

- **Identified Dissonance:** Dataset 377 is Fingrid's estimated need (MW), Dataset 375 is maximum power of the quarter hour (MW), and Datasets 378/379 are boundary flows (MW).
- **Interpretation Rule:** Because these three metrics measure distinct physical phenomena, exact algebraic closure ($\\text{DS\\_375} + |\\text{DS\\_378}| + |\\text{DS\\_379}| = \\text{DS\\_377}$) is not mathematically guaranteed across heterogeneous instruments. A failure of exact closure constitutes an instrument reconciliation finding, not a falsification of the author's narrative.

---

## 8. Discrepancy Tolerances

- **Price Matching:** Evaluated against precision present in Fingrid API response; published precision recorded in manifest.
- **Power Matching:** Evaluated against precision present in Fingrid API response ($\\pm 1.0\\text{ MW}$).
"""

CLAIMS_DATA = [
  {
    "claim_id": "FI-01",
    "target_event_date": "2026-08-03",
    "verbatim_claim": "Let’s take a look at 3rd Aug spike at 9:15 am EET... the imbalance price of 600 Eur/MWh were entirely set by mFRR activations.",
    "claim_type": "DIRECT_NUMERICAL",
    "primary_dataset": 319,
    "target_value": 600.0,
    "preregistered_status": "TESTABLE",
    "eval_branches": ["1.1", "1.2", "1.3", "1.4"]
  },
  {
    "claim_id": "FI-02a",
    "target_event_date": "2026-08-03",
    "verbatim_claim": "Out of the 469 MW of mFRR needed",
    "claim_type": "ESTIMATE_MATCHING",
    "primary_dataset": 377,
    "target_value": 469.0,
    "instrument_limit": "Dataset 377 is Fingrid's estimate for need, not physical metered volume",
    "preregistered_status": "TESTABLE",
    "eval_branches": ["1.1", "1.2", "1.3", "1.4"]
  },
  {
    "claim_id": "FI-02b",
    "target_event_date": "2026-08-03",
    "verbatim_claim": "424 MW was locally activated",
    "claim_type": "PEAK_POWER_MATCHING",
    "primary_dataset": 375,
    "target_value": 424.0,
    "instrument_limit": "Dataset 375 represents maximum power of the quarter hour (MW), not total energy (MWh)",
    "preregistered_status": "TESTABLE",
    "eval_branches": ["1.1", "1.2", "1.3", "1.4"]
  },
  {
    "claim_id": "FI-02c",
    "target_event_date": "2026-08-03",
    "verbatim_claim": "while the rest came in from SE1 and SE3",
    "claim_type": "DIRECTIONAL_AND_QUANTITY_IMPORT",
    "primary_dataset_se1": 378,
    "primary_dataset_se3": 379,
    "directional_condition": "DS_378 < 0 AND DS_379 < 0 (negative indicates cross-border import into FI)",
    "quantity_condition": "abs(DS_378) + abs(DS_379) >= 40.0 AND abs(DS_378) + abs(DS_379) <= 50.0",
    "instrument_caveat": "Exact closure with DS_377 - DS_375 is subject to instrument dissonance pre-registered in PARAMS.md Section 7",
    "preregistered_status": "TESTABLE",
    "eval_branches": ["1.1", "1.2", "1.3", "1.4"]
  },
  {
    "claim_id": "FI-03",
    "target_event_date": "2026-08-05",
    "verbatim_claim": "A similar story occurred on 5th Aug morning at 8:30 EET when the imbalance price spiked to 718 Eur/MWh.",
    "claim_type": "DIRECT_NUMERICAL",
    "primary_dataset": 319,
    "target_value": 718.0,
    "preregistered_status": "TESTABLE",
    "eval_branches": ["2.1", "2.2", "2.3", "2.4"]
  },
  {
    "claim_id": "FI-04a",
    "target_event_date": "2026-08-05",
    "verbatim_claim": "However, in this case, aFRR activations upward were non-zero",
    "claim_type": "ACTIVATION_NON_ZERO",
    "primary_dataset_marginal": 349,
    "primary_dataset_local": 354,
    "test_condition": "(DS_349 + DS_354) > 0",
    "preregistered_status": "TESTABLE",
    "eval_branches": ["2.1", "2.2", "2.3", "2.4"]
  },
  {
    "claim_id": "FI-04b",
    "target_event_date": "2026-08-05",
    "verbatim_claim": "There was no mFRR imports from Sweden in this case.",
    "claim_type": "DIRECTIONAL_IMPORT_ZERO",
    "primary_dataset_se1": 378,
    "primary_dataset_se3": 379,
    "test_condition": "DS_378 >= 0 AND DS_379 >= 0 (no negative import values)",
    "preregistered_status": "TESTABLE",
    "eval_branches": ["2.1", "2.2", "2.3", "2.4"]
  },
  {
    "claim_id": "FI-05",
    "target_event_date": "2026-08-05",
    "verbatim_claim": "The wind forecast error of more than 300 MW compared to the intraday forecast on 5th Aug was partly responsible for these activations",
    "claim_type": "DELTA_NUMERICAL",
    "primary_actual_dataset": 75,
    "primary_forecast_dataset": 245,
    "test_condition": "abs(DS_245 - DS_75) >= 300.0",
    "preregistered_status": "TESTABLE",
    "eval_branches": ["2.1", "2.2", "2.3", "2.4"],
    "scope_limit": "Measured error from consolidated DS 245 constitutes a strict lower bound on earlier vintage forecast error; causal attribution ('partly responsible') is non-computational"
  },
  {
    "claim_id": "FI-06",
    "target_event_date": "2026-08-03_and_2026-08-05",
    "verbatim_claim": "In the attached images, one can observe how BESS discharges spiked around these times of imbalance price spikes.",
    "claim_type": "AGGREGATE_DISCHARGE_SPIKE",
    "primary_dataset": 398,
    "corroborating_datasets": [399],
    "preregistered_status": "TESTABLE",
    "eval_rule": "Peak discharge in event window [T-30m, T+30m] >= baseline_median (2h) + 20 MW AND >= 1.5x baseline_median",
    "scope_limit": "Tests aggregate Finnish grid BESS discharge; does NOT test asset-level intent or price causation. Subject to DS 398 sensor freeze caveat."
  },
  {
    "claim_id": "FI-07",
    "target_event_date": "2026-08-03_and_2026-08-05",
    "verbatim_claim": "Our balancing market forecast warned in advance about both these spikes to act on it while there was still time to do so.",
    "claim_type": "PROPRIETARY_PRODUCT_ASSURANCE",
    "assigned_datasets": [],
    "preregistered_status": "UNFALSIFIABLE-AS-STATED",
    "rationale": "Private proprietary forecast model outputs are unrecorded in public transmission telemetry"
  }
]

SOURCE_POST_CONTENT = """# Source Post Metadata & Verbatim Content

> **Author:** Priyanka Shinde (PhD in energy markets | Montel Analytics)  
> **Source Platform:** LinkedIn  
> **Activity / Post ID:** `7491063244456050688`  
> **Date of Publication:** August 2026 (~2 weeks prior to 2026-08-24)  
> **Access Date (UTC):** 2026-08-24  
> **Formatting Note:** Paragraph breaks and unicode styling (bold characters) have been normalized to standard ASCII text.  
> **Scope Caveat:** Three accompanying image artifacts referenced in the post ("In the attached images, one can observe...") are unacquired. Verification evaluates textual statements against primary Fingrid open telemetry.

---

## Verbatim Post Text

```text
Imbalance price spikes in Finland this week!
In the past couple of days, we have observed the Finnish imbalance prices have spiked above 600-700 Eur/MWh in the morning hours. It is not so usual for the Finnish market. It is also a good chance to visualize the new imbalance pricing design in Finland. Let’s take a look at 3rd Aug spike at 9:15 am EET. In this case, both the dominating direction and mFRR activation direction were aligned. It meant that a VWAP of aFRR and mFRR in the quarter would set the price. As the aFRR activations were 0, the imbalance price of 600 Eur/MWh were entirely set by mFRR activations. Out of the 469 MW of mFRR needed, 424 MW was locally activated while the rest came in from SE1 and SE3. A similar story occurred on 5th Aug morning at 8:30 EET when the imbalance price spiked to 718 Eur/MWh. However, in this case, aFRR activations upward were non-zero which played a role in determining the VWAP which set the imbalance price. In both these cases, we can see declining wind generation playing a role in the need for upward activation from other sources. The wind forecast error of more than 300 MW compared to the intraday forecast on 5th Aug was partly responsible for these activations which were a combination of both scheduled and direct activations. There was no mFRR imports from Sweden in this case. The intraday market in both the cases started to act on this close to the domestic gate closure. This emphasises the need for allowing intraday trading close to the real time. Our balancing market forecast warned in advance about both these spikes to act on it while there was still time to do so. What makes the story furthermore interesting is the BESS response to these market opportunities. In the attached images, one can observe how BESS discharges spiked around these times of imbalance price spikes. It clearly shows that BESS has started to act on these price signals making use of the market volatility.
```
"""

def generate_all():
    with open(os.path.join(REPO_DIR, 'METHODOLOGY_PIN.md'), 'w') as f:
        f.write(METHODOLOGY_CONTENT)
    with open(os.path.join(REPO_DIR, 'PARAMS.md'), 'w') as f:
        f.write(PARAMS_CONTENT)
    with open(os.path.join(REPO_DIR, 'claims.json'), 'w') as f:
        json.dump(CLAIMS_DATA, f, indent=2)
    with open(os.path.join(REPO_DIR, 'SOURCE_POST.md'), 'w') as f:
        f.write(SOURCE_POST_CONTENT)
    print("Successfully generated all pre-registration artifacts in:", REPO_DIR)

if __name__ == '__main__':
    generate_all()

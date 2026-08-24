# Frozen Execution Parameters (fi-imbalance-s1)

> **Document Status:** SPREMNO ZA GEJT (Draft)  
> **Instance:** `fi-imbalance-s1`  
> **Target Event Dates:** 2026-08-03 and 2026-08-05  
> **Canonical Portal:** `https://data.fingrid.fi`  
> **Date of Pre-Registration (UTC):** 2026-08-24  
> **Static Source Post Hash (SHA-256):** `6f3c55102eaa3664b3d13d86e0e326343f3530b19b83748dafaad266d7cc1e73`  

---

## 1. Target Event Matrix (8 Disambiguation Branches)

Because the source claim uses colloquial timezone phrasing ("EET") during summer daylight saving time (when Finland observes EEST / UTC+3) and does not state whether timestamp labels represent interval beginnings or endings, all 8 branches ($2\text{ events} \times 2\text{ timezones} \times 2\text{ interval semantics}$) are pre-registered and evaluated:

### Event 1: 2026-08-03 (Declared "9:15 am EET")
- **Branch 1.1 (Primary Physical):** `EEST (UTC+3)` $\times$ `Interval-Beginning` $\to$ `[2026-08-03T06:15:00Z, 2026-08-03T06:30:00Z)`
- **Branch 1.2 (Alternative Physical):** `EEST (UTC+3)` $\times$ `Interval-Ending` $\to$ `[2026-08-03T06:00:00Z, 2026-08-03T06:15:00Z)`
- **Branch 1.3 (Author Literal EET):** `EET (UTC+2)` $\times$ `Interval-Beginning` $\to$ `[2026-08-03T07:15:00Z, 2026-08-03T07:30:00Z)`  
  *(Note: Finland was on EEST/UTC+3 on this date; this branch evaluates author mental reference without DST conversion)*
- **Branch 1.4 (Author Literal EET Ending):** `EET (UTC+2)` $\times$ `Interval-Ending` $\to$ `[2026-08-03T07:00:00Z, 2026-08-03T07:15:00Z)`  
  *(Note: Finland was on EEST/UTC+3 on this date; this branch evaluates author mental reference without DST conversion)*

### Event 2: 2026-08-05 (Declared "8:30 EET")
- **Branch 2.1 (Primary Physical):** `EEST (UTC+3)` $\times$ `Interval-Beginning` $\to$ `[2026-08-05T05:30:00Z, 2026-08-05T05:45:00Z)`
- **Branch 2.2 (Alternative Physical):** `EEST (UTC+3)` $\times$ `Interval-Ending` $\to$ `[2026-08-05T05:15:00Z, 2026-08-05T05:30:00Z)`
- **Branch 2.3 (Author Literal EET):** `EET (UTC+2)` $\times$ `Interval-Beginning` $\to$ `[2026-08-05T06:30:00Z, 2026-08-05T06:45:00Z)`  
  *(Note: Finland was on EEST/UTC+3 on this date)*
- **Branch 2.4 (Author Literal EET Ending):** `EET (UTC+2)` $\times$ `Interval-Ending` $\to$ `[2026-08-05T06:15:00Z, 2026-08-05T06:30:00Z)`  
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
| **`403`** | `Transmission of electricity between Finland and Central Sweden...` | 15 min | `MWh` | **NOT_SUBSTITUTABLE_FOR: FI-02, FI-04** (Physical schedule flow $\neq$ balancing flow) |
| **`404`** | `Transmission of electricity between Finland and Northern Sweden...` | 15 min | `MWh` | **NOT_SUBSTITUTABLE_FOR: FI-02, FI-04** (Physical schedule flow $\neq$ balancing flow) |

### Dataset 369 Semantic Caveats
- **Temporal Unit Notice:** The textual description for Dataset 369 refers to dominating direction "for each hour", whereas the publication cadence is 15 minutes. The 15-minute resolution governs.
- **Direction Value Zero Notice:** `0` encodes both "no mFRR activation occurred" and "equal upward and downward activations occurred". Both conditions satisfy Fingrid's rule for Day-Ahead fallback.

---

## 3. Mathematical Formalization of Pricing Rules

### 3.1 Event 1 (2026-08-03): Zero-aFRR Branching
Total satisfied aFRR upward demand is defined as:
$$V_{\text{aFRR, up}} = \text{DS\_349} + \text{DS\_354}$$

When $D = 1$ and $V_{\text{aFRR, up}} = 0$:
- **Price Branch A (Priyanka Interpretation):** $\text{Price}_A = P_{\text{mFRR, SA/DA}}$
- **Price Branch B (Literal Textual Rule):** $\text{Price}_B = \max(P_{\text{mFRR, marginal}}, P_{\text{aFRR, VWAP}})$

### 3.2 Event 2 (2026-08-05): Non-Zero aFRR Upward Activation
When $D = 1$ and $V_{\text{aFRR, up}} > 0$:
- **Theoretical Volume-Weighted Price:**
  $$\text{Price} = \frac{V_{\text{mFRR, up}} \cdot P_{\text{mFRR}} + V_{\text{aFRR, up}} \cdot P_{\text{aFRR, VWAP}}}{V_{\text{mFRR, up}} + V_{\text{aFRR, up}}}$$
- **Operationalization Notice:** Evaluated as an approximation against published Dataset 319 due to Dataset 375 publishing maximum MW power of the quarter hour rather than MWh energy volume.

---

## 4. Revision & Ingestion Rule (B-5)

- **Status:** `REVISION_RULE = UNRESOLVED_NORMATIVE_PIN`
- **Execution Rule:** All raw API responses are persisted under SHA-256 digests with exact `retrieved_at_utc` timestamps.
- **Evidence Policy:** Any future data modification observed from Fingrid will be published as an append-only revision record.

---

## 5. Wind Forecast Error Operationalization & Source Bias Declaration (FI-05)

- **Target Forecast Horizon:** The 15-minute interval corresponding to Event 2.
- **Forecast Ingestion:** Dataset 245 retains only the latest recorded forecast issue per target interval without explicit issuance timestamps.
- **Source Bias Boundary:** Because Dataset 245 does not expose issuance timestamps, its relation to any earlier pre-gate-closure vintage cannot be formally determined from this source alone. The verdict on FI-05 applies strictly to the latest recorded forecast issue retained in Fingrid Open Data.
- **Unit Equivalence:** $1\text{ MWh/h} \equiv 1\text{ MW}$ average power over a 15-minute interval.
- **Error Formula:** $\text{Forecast Error (MW)} = |\text{Forecast (DS 245)} - \text{Actual (DS 75)}|$.
- **Evaluation Criterion:** $\text{Forecast Error} \ge 300.0\text{ MW}$.

---

## 6. BESS Response Operationalization (FI-06)

- **Event Window:** $[T_{\text{event}} - 30\text{ min}, T_{\text{event}} + 30\text{ min}]$ (20 3-minute intervals).
- **Baseline Period:** Preceding 2 hours $[T_{\text{event}} - 150\text{ min}, T_{\text{event}} - 30\text{ min}]$ (40 3-minute intervals).
- **Baseline Metric:** $\text{Median}(\text{Discharge MW})$ from Dataset 398.
- **Spike Condition:** $\max(\text{Event Window Discharge}) \ge \text{Baseline Median} + 20.0\text{ MW}$ AND $\ge 1.50 \times \text{Baseline Median}$.
- **Charging Power:** Monitored descriptively via Dataset 399.
- **Scope Limit & Data Caveat:** Evaluates aggregate grid-level physical injection; does NOT infer asset-level intent or price causation. Dataset 398 carries an official notice that data may contain errors due to measurement freezing.

---

## 7. Instrument Dissonance & Quantitative Falsification Boundary (FI-02c)

- **Metrics:** Let $\Delta_{\text{import}} = |\text{DS\_378}| + |\text{DS\_379}|$ and $\Delta_{\text{residual}} = \text{DS\_377} - \text{DS\_375}$.
- **Residual Delta:** $\delta = |\Delta_{\text{import}} - \Delta_{\text{residual}}|$.
- **Quantitative Decision Boundary:**
  - If $\delta \le 10.0\text{ MW} \implies$ `CONFIRMED_SUBJECT_TO_INSTRUMENT_DISSONANCE` (discrepancy attributable to maximum-power vs average-flow metric definitions).
  - If $\delta > 10.0\text{ MW} \implies$ `DISCREPANT` (falsification boundary reached; cross-border flows fail to explain residual need).

---

## 8. Discrepancy Tolerances

- **Price Matching:** $\pm 0.01\text{ EUR/MWh}$ (or exact matching to published decimal precision).
- **Power Matching:** $\pm 1.0\text{ MW}$ for integer telemetry series (DS 75, 375, 377, 378, 379, 398); $\pm 0.1\text{ MW}$ for fractional forecast telemetry (DS 245).

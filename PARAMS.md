# Frozen Execution Parameters (fi-imbalance-s1)

> **Status:** RATIFIED & FROZEN PRIOR TO TELEMETRY INGESTION  
> **Instance:** `fi-imbalance-s1`  
> **Target Event Dates:** 2026-08-03 and 2026-08-05  
> **Canonical Portal:** `https://data.fingrid.fi`  
> **Date of Pre-Registration (UTC):** 2026-08-24  

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

## 2. Canonical Fingrid Open Data Dataset Pinning

All datasets are pinned to the single canonical portal `https://data.fingrid.fi`:

| Dataset ID | Verbatim Name | Resolution | Verbatim Unit | Operational Role |
|:---:|---|:---:|:---:|---|
| **`319`** | `Imbalance price` | 15 min | `EUR/MWh` | Primary settlement price (600 / 718 EUR/MWh claims) |
| **`75`** | `Wind power generation - 15 min data` | 15 min | `MW` | Actual wind production (interval-ending 15-min average) |
| **`245`** | `Wind power generation forecast - updated every 15 minutes` | 15 min | `MWh/h` | Intraday wind forecast (72h rolling horizon) |
| **`246`** | `Wind power generation forecast - updated once a day` | 15 min | `MWh/h` | Day-ahead wind forecast (reference baseline) |
| **`369`** | `Dominating direction in the mFRR energy market in Finland` | 15 min | `-1, 0, 1` | Direct Fingrid signal (-1=down, 1=up, 0=none) |
| **`377`** | `mFRR need` | 15 min | `MW` | Fingrid estimate for mFRR need (469 MW claim) |
| **`375`** | `Activated mFRR balancing regulation upward sum` | 15 min | `MW` | Local FI upward activation sum (SA + DA, 424 MW claim) |
| **`385`** | `Activated mFRR balancing regulation SA upward sum` | 15 min | `MW` | Scheduled activation upward sum |
| **`390`** | `Activated mFRR balancing regulation DA upward sum` | 15 min | `MW` | Direct activation upward sum |
| **`378`** | `mFRR flow FI-SE1` | 15 min | `MW` | Cross-border mFRR flow from SE1 (negative = import) |
| **`379`** | `mFRR flow FI-SE3` | 15 min | `MW` | Cross-border mFRR flow from SE3 (negative = import) |
| **`381`** | `Net export / import of mFRR energy` | 15 min | `MW` | Net cross-border mFRR energy flow |
| **`347`** | `aFRR energy volume weighted average price, up` | 15 min | `EUR/MWh` | aFRR upward VWAP price |
| **`348`** | `aFRR energy volume weighted average price, down` | 15 min | `EUR/MWh` | aFRR downward VWAP price |
| **`349`** | `aFRR energy activation volume with marginal price, up` | 15 min | `MW` | aFRR upward marginal activation volume |
| **`350`** | `aFRR energy activation volume with marginal price, down` | 15 min | `MW` | aFRR downward marginal activation volume |
| **`353`** | `aFRR energy activation volume local selection, down` | 15 min | `MW` | aFRR local selection volume down |
| **`354`** | `aFRR energy activation volume local selection, up` | 15 min | `MW` | aFRR local selection volume up |
| **`398`** | `Battery energy storage systems discharging power - real-time data` | 3 min | `MW` | Grid-directed aggregate BESS discharge power |
| **`399`** | `Battery energy storage systems charging power - real-time data` | 3 min | `MW` | Battery-directed aggregate BESS charge power |
| **`400`** | `mFRR Scheduled activation price - real-time` | 15 min | `€/MWh` | Scheduled activation price |
| **`401`** | `mFRR direct activation price up - real-time` | 15 min | `€/MWh` | Direct activation price up |
| **`402`** | `mFRR direct activation price down - real-time` | 15 min | `€/MWh` | Direct activation price down |
| **`403`** | `Transmission of electricity between Finland and Central Sweden...` | 15 min | `MWh` | **NOT_SUBSTITUTABLE_FOR: FI-02, FI-04** (Physical schedule flow $\neq$ balancing flow) |
| **`404`** | `Transmission of electricity between Finland and Northern Sweden...` | 15 min | `MWh` | **NOT_SUBSTITUTABLE_FOR: FI-02, FI-04** (Physical schedule flow $\neq$ balancing flow) |

---

## 3. Imbalance Pricing Tree on Zero-aFRR Activation (2026-08-03 Event)

Under Fingrid's 1 June 2026 pricing rule, when $\text{aFRR} = 0$, both rule interpretations are pre-registered and executed:
- **Price Branch A (Priyanka Interpretation):** $\text{aFRR} = 0 \implies$ Direction is aligned with mFRR $\implies \text{Price} = \text{VWAP}(\text{mFRR})$.
- **Price Branch B (Literal Textual Rule):** $\text{aFRR} = 0 \implies$ Satisfied aFRR demand has no direction $\implies \text{Price} = \max(\text{mFRR}_{\text{marginal}}, \text{VWAP}_{\text{aFRR}})$.

Both calculated values will be emitted in `results.json` and compared against published Dataset 319.

---

## 4. Revision & Settlement Rule (B-5)

- **Status:** `REVISION_RULE = UNRESOLVED_NORMATIVE_PIN`
- **Execution Rule:** All raw API responses are persisted under SHA-256 digests with `retrieved_at_utc` timestamps.
- **Evidence Model:** Because the target dates (2026-08-03 and 2026-08-05) are evaluated after the $D+13$ eSett preliminary settlement window on 2026-08-24 ($L \ge 19\text{ days}$), any subsequent revision by Fingrid or eSett will be recorded as a new evidence event rather than an in-place overwrite.

---

## 5. BESS Response Operationalization (FI-06)

- **Event Window:** $[T_{\text{event}} - 30\text{ min}, T_{\text{event}} + 30\text{ min}]$ (spanning 20 3-minute intervals).
- **Baseline Period:** Preceding 2 hours $[T_{\text{event}} - 150\text{ min}, T_{\text{event}} - 30\text{ min}]$ (spanning 40 3-minute intervals).
- **Baseline Metric:** $\text{Median}(\text{Discharge MW})$ from Dataset 398.
- **Spike Condition:** $\max(\text{Event Window Discharge}) \ge \text{Baseline Median} + 20.0\text{ MW}$ AND $\ge 1.50 \times \text{Baseline Median}$.
- **Charging Monitor:** Dataset 399 charging power is reported descriptively to monitor whether charging dropped simultaneously.
- **Scope Boundary:** Proves physical aggregate grid injection increase; does NOT prove operator intent or price causation.

---

## 6. Discrepancy Tolerances

- **Price Tolerances:** $\pm 0.01\text{ EUR/MWh}$ (exact matching to published precision).
- **Power Tolerances:** $\pm 1.0\text{ MW}$ (integer rounding matching published precision).
- **Forecast Error Delta:** $\text{Actual Wind (DS 75)} - \text{Intraday Forecast (DS 245)}$.


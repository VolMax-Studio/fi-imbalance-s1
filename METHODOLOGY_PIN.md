# Normative Methodology Pin (Fingrid Imbalance Pricing 1 June 2026)

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
- $D \in \{-1, 0, 1\}$ be the dominating direction (Dataset 369).
- $V_{\text{mFRR, up}}$ (Dataset 375 - Maximum power of quarter hour), $V_{\text{mFRR, down}}$ (Dataset 376) be activated mFRR power indicators.
- $V_{\text{aFRR, up}} = \text{DS\_349} + \text{DS\_354}$ (Total satisfied demand for aFRR upwards: marginal price volume + local selection volume).
- $P_{\text{mFRR, marginal}}$ (Dataset 400/401) be the marginal mFRR activation price.
- $P_{\text{aFRR, VWAP}}$ (Dataset 347/348) be the volume-weighted average aFRR price.

### 2.1 Case 1: Dominating Direction Up ($D = 1$) and $V_{\text{aFRR, up}} = 0$ (Event 1, 2026-08-03)
- **Branch A (Priyanka Interpretation):** $\text{Price}_A = P_{\text{mFRR, SA/DA}}$
- **Branch B (Literal Textual Rule):** $\text{Price}_B = \max(P_{\text{mFRR, marginal}}, P_{\text{aFRR, VWAP}})$

### 2.2 Case 2: Dominating Direction Up ($D = 1$) and $V_{\text{aFRR, up}} > 0$ (Event 2, 2026-08-05)
- **Mathematical Volume-Weighted Formula (Theoretical):**
  $$\text{Price} = \frac{V_{\text{mFRR, up}} \cdot P_{\text{mFRR}} + V_{\text{aFRR, up}} \cdot P_{\text{aFRR, VWAP}}}{V_{\text{mFRR, up}} + V_{\text{aFRR, up}}}$$
- **Telemetry Operationalization Caveat:** Because Fingrid Dataset 375 publishes maximum power of the quarter hour (MW) rather than aggregate energy volume (MWh), the theoretical volume-weighted reconstruction is evaluated as an approximation against published Dataset 319.

---

## 3. Amendment Ledger

- **Amendment #1 (2026-08-24):** Replaced draft text with exact verbatim wording transcribed from the official Fingrid news release (URL: `https://www.fingrid.fi/en/news/news/2026/change-in-determining-the-imbalance-price-for-balance-responsible-parties-in-june-2026/`) and verified character-identical against source on 2026-08-24.

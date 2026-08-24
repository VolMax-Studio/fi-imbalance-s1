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
The calculation of the imbalance price for balance responsible parties will change to volume-weighted from 1 June 2026.

The price is volume-weighted when the activated mFRR and the satisfied demand for aFRR in Finland are both in the dominating direction. The dominating direction remains unchanged, i.e. it is based only on mFRR activations.

If mFRR is not activated in the dominating direction, the price is formed as before, i.e. as the largest of the mFRR marginal price and the volume-weighted aFRR price, and if the dominating direction is downward, as the smaller of these two components.

If there is no decisive mFRR direction at all within the market time unit, the price is formed based on the Day Ahead price, even if there were aFRR activations.
```

---

## 2. Formalization of Pricing Rules

Let:
- $D \in \{-1, 0, 1\}$ be the dominating direction (Dataset 369).
- $V_{\text{mFRR, up}}$ (Dataset 375), $V_{\text{mFRR, down}}$ (Dataset 376) be activated mFRR volumes.
- $V_{\text{aFRR, up}}$ (Dataset 349), $V_{\text{aFRR, down}}$ (Dataset 350) be activated aFRR volumes with marginal price.
- $P_{\text{mFRR, marginal}}$ (Dataset 400/401) be the marginal mFRR activation price.
- $P_{\text{aFRR, VWAP}}$ (Dataset 347/348) be the volume-weighted average aFRR price.

### 2.1 Case 1: Dominating Direction Up ($D = 1$) and $V_{\text{aFRR, up}} = 0$ (Event 1, 2026-08-03)
- **Branch A (Priyanka Interpretation):** $\text{Price}_A = P_{\text{mFRR, SA/DA}}$
- **Branch B (Literal Textual Rule):** $\text{Price}_B = \max(P_{\text{mFRR, marginal}}, P_{\text{aFRR, VWAP}})$

### 2.2 Case 2: Dominating Direction Up ($D = 1$) and $V_{\text{aFRR, up}} > 0$ (Event 2, 2026-08-05)
$$\text{Price} = \frac{V_{\text{mFRR, up}} \cdot P_{\text{mFRR}} + V_{\text{aFRR, up}} \cdot P_{\text{aFRR, VWAP}}}{V_{\text{mFRR, up}} + V_{\text{aFRR, up}}}$$

---

## 3. Amendment Ledger

- **Amendment #1 (2026-08-24):** Replaced paraphrased text with 100% exact verbatim wording from Fingrid announcement (restored "in Finland", "largest of", "smaller of", "remains unchanged, i.e. it is based only on", and removed injected code tokens).

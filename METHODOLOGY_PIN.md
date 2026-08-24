# Normative Methodology Pin (Fingrid Imbalance Pricing 1 June 2026)

> **Source:** Fingrid Oyj Official Release  
> **Title:** *Change in determining the imbalance price for balance responsible parties in June 2026*  
> **Publication Date:** 2026-04-27  
> **Effective Date:** 2026-06-01  
> **URL:** `https://www.fingrid.fi/en/news/news/2026/change-in-determining-the-imbalance-price-for-balance-responsible-parties-in-june-2026/`  
> **Access Date (UTC):** 2026-08-24  

---

## 1. Verbatim Normative Methodology Text

```text
The calculation of the imbalance price for balance responsible parties will change to volume-weighted from 1 June 2026.

The price is volume-weighted when the activated mFRR and the satisfied demand for aFRR in Finland are both in the dominating direction. The dominating direction is determined as before based exclusively on mFRR activations.

If mFRR is not activated in the dominating direction, the price is formed as before:
- as the higher of the mFRR marginal price and the volume-weighted aFRR price, and
- if the dominating direction is downward, as the lower of these two components.

If there is no decisive mFRR direction at all within the market time unit (dominating direction = 0), the price is formed based on the Day Ahead price, even if there were aFRR activations.
```

---

## 2. Mathematical Formalization of Pricing Branches

Let:
- $D \in \{-1, 0, 1\}$ be the dominating direction from Fingrid Dataset 369.
- $V_{\text{mFRR, up}}$ (Dataset 375), $V_{\text{mFRR, down}}$ (Dataset 376) be activated mFRR volumes.
- $V_{\text{aFRR, up}}$ (Dataset 349/354), $V_{\text{aFRR, down}}$ (Dataset 350/353) be activated aFRR volumes.
- $P_{\text{mFRR, marginal}}$ (Dataset 400/401) be the marginal mFRR activation price.
- $P_{\text{aFRR, VWAP}}$ (Dataset 347/348) be the volume-weighted average aFRR price.

### Branch A (Priyanka Post Interpretation)
When $D = 1$ and $V_{\text{aFRR, up}} = 0$, aFRR is deemed aligned with dominating direction:
$$\text{Price}_A = \text{VWAP}(P_{\text{mFRR}}) = P_{\text{mFRR, SA/DA}}$$

### Branch B (Literal Textual Rule)
When $D = 1$ and $V_{\text{aFRR, up}} = 0$, satisfied aFRR demand is zero (no direction):
$$\text{Price}_B = \max(P_{\text{mFRR, marginal}}, P_{\text{aFRR, VWAP}})$$

Both formulas are evaluated and compared against published Dataset 319 in `reproduce.py`.

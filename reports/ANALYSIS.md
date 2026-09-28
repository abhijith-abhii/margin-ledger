# Margin Ledger — measured example

Synthetic retail case. These queries describe observed order lines, not causal drivers. Returned lines fully reverse revenue/cost; shipping, tax and processing fees are excluded.

## Results

- **orders:** 500
- **customers:** 147
- **revenue_usd:** 81893.75
- **margin_usd:** 30110.42

## Interpretation
SELECT category,COUNT(*) line_count,SUM(net_revenue_cents)/100.0 revenue_usd,SUM(margin_cents)/100.0 margin_usd,ROUND(100.0*SUM(margin_cents)/NULLIF(SUM(net_revenue_cents),0),2) margin_pct FROM facts GROUP BY category ORDER BY margin_usd DESC;


## Business recommendation
In this synthetic sample, Home contributes the most category margin ($10,867.27). Review its return mix and unit economics before reallocating inventory. This descriptive ranking does not establish the effect of additional stock or marketing.
Cross-check category and monthly revenue with the reconciliation tests. Cohort analysis is bounded by the six-month observation window.

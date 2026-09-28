# Margin Ledger — learning guide

## What it does

Find product and return patterns with SQL. The intended user is retail analysts. Browser controls → validated Flask API → project analysis/workflow → results and export.

## Run and demonstrate

Follow the README installation block, then: Compare category margin, monthly revenue and cumulative revenue. Verify totals agree, then inspect the returns and cohort reports and generated business findings.

## Important files

- `app.py` — local HTTP interface and request/error handling.
- `core.py` — project-specific logic.
- `tests/` — regression and correctness checks.
- `reports/` — recorded outputs and verification evidence.

## Three engineering decisions

1. Keep order-line grain explicit and validate order-level fields before aggregation.
2. Represent money in integer cents and reverse returned lines consistently.
3. Use reusable SQL files, including CTEs and window functions, with cross-report reconciliation tests.

## Five interview questions

1. **Why is the unit of analysis explicit?** Orders, order lines and customers have different grains. Joining them carelessly can duplicate revenue or overcount repeat customers, so SQL reports preserve and reconcile the intended grain.

2. **How do returns affect margin?** Returned line values reverse the relevant revenue and cost contributions. Tests verify these adjustments and aggregate totals instead of treating every shipped line as retained revenue.

3. **Why use integer cents?** Exact integer values keep monetary reconciliation stable. Formatting into currency is a presentation step, not the basis of the calculations.

4. **What do the window queries add?** They calculate ordered running values and cohort-style comparisons without losing the underlying row context. They demonstrate analysis beyond simple group-by totals.

5. **Can the report guide a real retailer?** Its findings describe a synthetic fixture. The business questions and SQL are reusable, but actual recommendations require validated real data and operating context.

## Independent exercise

Add a customer lifetime-value proxy with a clear observation window and no future-value claim.

Write down the expected behavior before editing. Add a meaningful regression check, run the existing suite, and describe what changed in your own words.

## Contribution and resume guidance

The implementation was developed with substantial AI assistance under Abhijith Viswanathan's direction. The verified contribution is the working artifact and the learning work actually completed, not invented employment or adoption.

Suggested factual bullet after personally validating the demo:

- Created eight SQLite business reports with order/line grain controls, return reversals and monetary reconciliation; published reproducible synthetic-data findings.

Use [VERIFICATION.md](VERIFICATION.md) to add only measured numbers. Do not claim production traffic, users, savings, upstream acceptance or cloud deployment without corresponding evidence.

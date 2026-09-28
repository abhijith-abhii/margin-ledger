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

1. **What problem does this project solve, and what is its unit of work?** Explain find product and return patterns with sql, identify retail analysts as the audience, and trace one concrete example through the files above. Use the demonstration output rather than hypothetical impact.
2. **Why did you choose the first design decision?** Keep order-line grain explicit and validate order-level fields before aggregation. Show the corresponding implementation and a test that would fail if that property were removed.
3. **How do you protect correctness when inputs or execution change?** Represent money in integer cents and reverse returned lines consistently. Explain the relevant invalid-input or edge-case test and distinguish a checked property from an untested assumption.
4. **How do you make results inspectable and reproducible?** Use reusable SQL files, including CTEs and window functions, with cross-report reconciliation tests. Point to actual outputs and recorded commands. Explain why a successful example is weaker evidence than a tested boundary or independently reconciled total.
5. **What would you improve before real deployment or real-data use?** Synthetic six-month retail data. Simplified full-line returns, no shipping/tax/fees, no causal conclusions. Repeat-customer and cohort analyses use only the observed window and may misclassify pre-window customers. Choose one limitation, describe the missing evidence, and propose a measurable acceptance check rather than promising production readiness.

## Independent exercise

Add a customer lifetime-value proxy with a clear observation window and no future-value claim.

Write down the expected behavior before editing. Add a meaningful regression check, run the existing suite, and describe what changed in your own words.

## Contribution and resume guidance

The implementation was developed with substantial AI assistance under Abhijith Viswanathan's direction. The verified contribution is the working artifact and the learning work actually completed, not invented employment or adoption.

Suggested factual bullet after personally validating the demo:

- Implemented and validated find product and return patterns with sql using SQLite · Python · Flask, with star schema and documented correctness checks and limitations.

Use [VERIFICATION.md](VERIFICATION.md) to add only measured numbers. Do not claim production traffic, users, savings, upstream acceptance or cloud deployment without corresponding evidence.

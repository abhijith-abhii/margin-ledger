SELECT product,SUM(quantity) gross_units,SUM(net_revenue_cents)/100.0 revenue_usd,SUM(margin_cents)/100.0 margin_usd FROM facts GROUP BY product ORDER BY margin_usd DESC LIMIT 10;

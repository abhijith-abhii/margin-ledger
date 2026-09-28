SELECT SUBSTR(date,1,7) month,COUNT(DISTINCT order_id) orders,SUM(net_revenue_cents)/100.0 revenue_usd FROM facts GROUP BY month ORDER BY month;

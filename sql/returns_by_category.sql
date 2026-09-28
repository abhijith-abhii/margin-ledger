SELECT category,COUNT(*) lines,SUM(returned) returned_lines,ROUND(100.0*AVG(returned),2) return_line_pct FROM facts GROUP BY category;

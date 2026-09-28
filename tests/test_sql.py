import pytest
from core import connect,analyze

def test_category_month_reconcile():
 a=analyze({'report':'category_margin'});b=analyze({'report':'monthly_sales'})
 assert sum(r['revenue_usd'] for r in a['rows'])==pytest.approx(sum(r['revenue_usd'] for r in b['rows']))
 assert sum(r['margin_usd'] for r in a['rows'])==pytest.approx(a['metrics']['margin_usd'])
def test_all_queries():
 from core import ROOT
 for p in (ROOT/'sql').glob('*.sql'):assert analyze({'report':p.stem})['rows']
def test_return_reversal():
 with connect() as c:assert c.execute('SELECT SUM(net_revenue_cents) FROM facts WHERE returned=1').fetchone()[0]==0
def test_bad_report():
 with pytest.raises(ValueError):analyze({'report':'../../secret'})

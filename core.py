import sqlite3,csv,json
from pathlib import Path
ROOT=Path(__file__).parent

def connect():
 c=sqlite3.connect(':memory:');c.row_factory=sqlite3.Row
 c.executescript('CREATE TABLE lines(line_id INTEGER PRIMARY KEY,order_id INTEGER,customer_id INTEGER,date TEXT,product TEXT,category TEXT,quantity INTEGER CHECK(quantity>0),unit_price_cents INTEGER CHECK(unit_price_cents>=0),unit_cost_cents INTEGER CHECK(unit_cost_cents>=0),returned INTEGER CHECK(returned IN(0,1)));')
 rows=list(csv.DictReader(open(ROOT/'data/lines.csv')))
 for r in rows:
  for k in ['line_id','order_id','customer_id','quantity','unit_price_cents','unit_cost_cents','returned']:r[k]=int(r[k])
  c.execute('INSERT INTO lines VALUES(:line_id,:order_id,:customer_id,:date,:product,:category,:quantity,:unit_price_cents,:unit_cost_cents,:returned)',r)
 c.execute('CREATE VIEW facts AS SELECT *,quantity*unit_price_cents*(1-returned) net_revenue_cents,quantity*(unit_price_cents-unit_cost_cents)*(1-returned) margin_cents FROM lines')
 # Order-level fields must remain constant across order lines.
 assert c.execute('SELECT COUNT(*) FROM (SELECT order_id FROM lines GROUP BY order_id HAVING COUNT(DISTINCT customer_id)>1 OR COUNT(DISTINCT date)>1)').fetchone()[0]==0
 return c

def analyze(p):
 name=p.get('report','category_margin');path=ROOT/'sql'/f'{name}.sql'
 if name not in {x.stem for x in (ROOT/'sql').glob('*.sql')}:raise ValueError('Unknown analysis')
 with connect() as c:
  rows=[dict(x) for x in c.execute(path.read_text())];m=dict(c.execute('SELECT COUNT(DISTINCT order_id) orders,COUNT(DISTINCT customer_id) customers,SUM(net_revenue_cents)/100.0 revenue_usd,SUM(margin_cents)/100.0 margin_usd FROM facts').fetchone())
 return dict(metrics={k:round(v,2) if isinstance(v,float) else v for k,v in m.items()},rows=rows,answer=path.read_text(),notice='Synthetic retail case. These queries describe observed order lines, not causal drivers. Returned lines fully reverse revenue/cost; shipping, tax and processing fees are excluded.',details={'grain':'one product line within an order','report':name,'source':'data/lines.csv'})

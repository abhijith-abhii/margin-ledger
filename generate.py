from pathlib import Path
import csv,random
r=random.Random(21);root=Path(__file__).parent;(root/'data').mkdir(exist_ok=True)
with (root/'data/lines.csv').open('w') as f:
 w=csv.writer(f);w.writerow(['line_id','order_id','customer_id','date','product','category','quantity','unit_price_cents','unit_cost_cents','returned'])
 line=0
 for order in range(1,501):
  customer=r.randint(1,150);date=f'2026-{r.randint(1,6):02}-{r.randint(1,28):02}'
  for _ in range(r.randint(1,4)):
   line+=1;product=r.randint(1,12);price=1000+product*375;qty=r.randint(1,3)
   w.writerow([line,order,customer,date,f'Product {product:02}',['Home','Tech','Books'][product%3],qty,price,round(price*r.uniform(.45,.82)),int(r.random()<.08)])

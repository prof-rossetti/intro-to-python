import os
import pandas as pd

def to_usd(my_price):
  # return "${0:,.2f}".format(my_price)
  return f"${my_price:,.2f}"

def month_lookup(month):
	year_month={'01':'January','02':'February','03':'March','04':'April',
	'05':'May','06':'June','07':'July','08':'August','09':'September','10':'October',
	'11':'November', '12':'December'}
	return year_month[month]

#
# INFO INPUTS
#

CSV_FILENAME = "sales-201803.csv"

csv_filepath = os.path.join("data", CSV_FILENAME)

sales = pd.read_csv(csv_filepath)

# print(sales.head())
#>          date            product  unit price  units sold  sales price
#> 0  2018-03-01  Button-Down Shirt       65.05           2       130.10
#> 1  2018-03-01   Vintage Logo Tee       15.95           1        15.95
#> 2  2018-03-01       Sticker Pack        4.50           1         4.50
#> 3  2018-03-02  Super Soft Hoodie       75.00           2       150.00
#> 4  2018-03-02  Button-Down Shirt       65.05           7       455.35

# print(sales.columns)
#> Index(['date', 'product', 'unit price', 'units sold', 'sales price'], dtype='object')

# total_sales = 12000.71
# total_sales = sum(sales["sales price"].tolist())
total_sales = sales["sales price"].sum()

month = month_lookup(CSV_FILENAME[-6:-4]) # TODO: get from file name or date values
year = int(CSV_FILENAME[6:10]) # TODO: get from file name or date values

products=sales['product'].unique()
products.sort()
sales_price=sales.groupby(sales['product']).sum()
sales_price_col=list(sales_price['sales price'])
total_price_by_prod=pd.DataFrame({'products':products,'sales_price':sales_price_col})
total_price_by_prod=total_price_by_prod.sort_values(by=['sales_price'],ascending=False)
#
# INFO OUTPUTS
#
for i in range(3):
	print(str(i+1)+') '+str(total_price_by_prod.iloc[i][0])+' ' "${0:,.2f}".format(total_price_by_prod.iloc[i][1]))

print("-------------------------")
print(f"SALES REPORT!")
print("-------------------------")
print(f"MONTH: {month} {year}")
print(f"TOTAL SALES: {to_usd(total_sales)}")

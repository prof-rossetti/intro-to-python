import os
import pandas as pd

# utility function to convert float or integer to usd-formatted string (for printing)
def to_usd(my_price):
  # return "${0:,.2f}".format(my_price)
  return f"${my_price:,.2f}"

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

month = "MARCH" # TODO: get from file name or date values
year = 2018 # TODO: get from file name or date values

#
# INFO OUTPUTS
#

print("-------------------------")
print(f"SALES REPORT!")
print("-------------------------")
print(f"MONTH: {month} {year}")
print(f"TOTAL SALES: {to_usd(total_sales)}")

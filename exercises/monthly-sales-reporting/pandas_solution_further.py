# monthly_sales.py

import os
import pandas

# utility function to convert float or integer to usd-formatted string (for printing)
def to_usd(my_price):
    return "${0:,.2f}".format(my_price)  # > $12,000.71

#
# INPUTS
#

csv_filename = "sales-201803.csv"

# reference a file in the "data" directory
# ... adapted from: https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/modules/os.md#file-operations
csv_filepath = os.path.join(os.path.dirname(__file__), "data", csv_filename)

# read csv file into a pandas dataframe object
# ... this and other pandas operations adapted from: https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/packages/pandas.md
csv_data = pandas.read_csv(csv_filepath)

#
# CALCULATIONS
#

monthly_total = csv_data["sales price"].sum()

# google search for "pandas group by" leads to...
# ... https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html
product_totals = csv_data.groupby(["product"]).sum()

# google search for "pandas dataframe order rows" leads to ...
# ... http://pandas.pydata.org/pandas-docs/version/0.19/generated/pandas.DataFrame.sort.html
product_totals = product_totals.sort_values("sales price", ascending=False)

# google search for "pandas loop through each row in a dataframe" results in ...
# ... https://stackoverflow.com/questions/16476924/how-to-iterate-over-rows-in-a-dataframe-in-pandas
# ... http://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.iterrows.html

top_sellers = []
rank = 1
for i, row in product_totals.iterrows():
    d = {"rank": rank, "name": row.name, "monthly_sales": row["sales price"]}
    top_sellers.append(d)
    rank = rank + 1

#
# OUTPUTS
#

print("-----------------------")
print("MONTH: March 2018")

print("-----------------------")
print("CRUNCHING THE DATA...")

print("-----------------------")
print(f"TOTAL MONTHLY SALES: {to_usd(monthly_total)}")

print("-----------------------")
print("TOP SELLING PRODUCTS:")
for d in top_sellers:
    print("  " + str(d["rank"]) + ") " + d["name"] +
          ": " + to_usd(d["monthly_sales"]))

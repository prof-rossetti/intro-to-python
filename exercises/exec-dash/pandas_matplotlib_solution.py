# monthly_sales.py

import operator
import os
import pandas
import matplotlib.pyplot as plt

# utility function to convert float or integer to usd-formatted string (for printing)
# ... adapted from: https://github.com/s2t2/shopping-cart-screencast/blob/30c2a2873a796b8766e9b9ae57a2764725ccc793/shopping_cart.py#L56-L59


def to_usd(my_price):
    return "${0:,.2f}".format(my_price)  # > $12,000.71

#
# INPUTS
#


csv_filename = "sales-201803.csv"  # TODO: allow user to specify

# reference a file in the "data" directory
# ... adapted from: https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/notes/python/modules/os.md#file-operations
csv_filepath = os.path.join(os.path.dirname(__file__), "data", csv_filename)

# read csv file into a pandas dataframe object
# ... this and other pandas operations adapted from: https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/notes/python/packages/pandas.md
csv_data = pandas.read_csv(csv_filepath)

#
# CALCULATIONS
#

monthly_total = csv_data["sales price"].sum()

# top_sellers = [
#     {"name": "Button-Down Shirt", "monthly_sales": 6960.34},
#     {"name": "Super Soft Hoodie", "monthly_sales": 1875.0},
#     {"name": "Khaki Pants", "monthly_sales": 1602.0},
#     {"name": "Vintage Logo Tee", "monthly_sales": 941.05},
#     {"name": "Brown Boots", "monthly_sales": 250.0},
#     {"name": "Sticker Pack", "monthly_sales": 216.0},
#     {"name": "Baseball Cap", "monthly_sales": 156.31}
# ]

# breakpoint()
# (Pdb) print(type(csv_data)) #> <class 'pandas.core.frame.DataFrame'>
#
# (Pdb) csv_data.head(3)
#>          date            product  unit price  units sold  sales price
#> 0  2018-03-01  Button-Down Shirt       65.05           2       130.10
#> 1  2018-03-01   Vintage Logo Tee       15.95           1        15.95
#> 2  2018-03-01       Sticker Pack        4.50           1         4.50
#
# Get unique products
#
product_names = csv_data["product"]
# ... what kind of datatype is this?
# (Pdb) print(type(product_names)) #> <class 'pandas.core.series.Series'>
# ... google search for "pandas.core.series.Series unique values" yields: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.unique.html
unique_product_names = product_names.unique()  # :-D
# (Pdb) print(unique_product_names) #> ['Button-Down Shirt' 'Vintage Logo Tee' 'Sticker Pack' 'Super Soft Hoodie' 'Baseball Cap' 'Khaki Pants' 'Brown Boots']
# ... looks like a list, but what kind of datatype is this?
# (Pdb) print(type(unique_product_names)) #> <class 'numpy.ndarray'>
# ... numpy.ndarray WAT? let's try to convert it to a list, if possible, so we can be working with familiar datatypes...
# ... google search for "how to convert numpy.ndarray to list" yields:
#  + https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.ndarray.tolist.html
#  + https://stackoverflow.com/questions/1966207/converting-numpy-array-into-python-list-structure
# convert numpy.ndarray to list
unique_product_names = unique_product_names.tolist()

# Accumulate total sales per product

top_sellers = []

for product_name in unique_product_names:
    # filering approach adapted from: https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/notes/python/packages/pandas.md
    # ... matching_rows = stats[stats["games"] > 150]
    matching_rows = csv_data[csv_data["product"] == product_name]
    #(Pdb) print(type(matching_rows)) #> <class 'pandas.core.frame.DataFrame'>
    #(Pdb) matching_rows.head(3)
    #>         date            product  unit price  units sold  sales price
    #> 0  2018-03-01  Button-Down Shirt       65.05           2       130.10
    #> 4  2018-03-02  Button-Down Shirt       65.05           7       455.35
    #> 9  2018-03-03  Button-Down Shirt       65.05           8       520.40
    product_monthly_sales = matching_rows["sales price"].sum()
    # print(type(product_monthly_sales)) #> FYI: <class 'numpy.float64'> which is like a normal float. possible to convert, but maybe not necessary...
    top_sellers.append(
        {"name": product_name, "monthly_sales": product_monthly_sales})

# sort the list of dictionaries to make sure they are looped through and charted in the right order
# ... adapted from: https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/notes/python/datatypes/lists.md#sorting
# sort in descending order, google search for "python sorted function sort descending" yields:
#  + https://www.programiz.com/python-programming/methods/built-in/sorted
#  + https://docs.python.org/3/howto/sorting.html
top_sellers = sorted(top_sellers, key=operator.itemgetter(
    "monthly_sales"), reverse=True)

#
# OUTPUTS
#

print("-----------------------")
print("MONTH: March 2018")  # TODO: get month and year

print("-----------------------")
print("CRUNCHING THE DATA...")

print("-----------------------")
print(f"TOTAL MONTHLY SALES: {to_usd(monthly_total)}")

print("-----------------------")
print("TOP SELLING PRODUCTS:")

rank = 1
for d in top_sellers:
    print("  " + str(rank) + ") " +
          d["name"] + ": " + to_usd(d["monthly_sales"]))
    rank = rank + 1

print("-----------------------")
print("VISUALIZING THE DATA...")

# adapted from code posted to matplotlib Slack channel: https://georgetown-opim-py.slack.com/archives/CFZDKNKA4/p1549494877005200
# google search for "matplotlib chart title" yields:
#  + https://matplotlib.org/api/_as_gen/matplotlib.pyplot.title.html
#  + https://matplotlib.org/gallery/subplots_axes_and_figures/figure_title.html
#  + https://matplotlib.org/users/pyplot_tutorial.html

chart_title = "Top Selling Products (March 2018)"  # TODO: get month and year

sorted_products = []
sorted_sales = []

for d in top_sellers:
    sorted_products.append(d["name"])
    sorted_sales.append(d["monthly_sales"])

plt.bar(sorted_products, sorted_sales)
plt.title(chart_title)
plt.xlabel("Product")
plt.ylabel("Monthly Sales (USD)")
plt.show()

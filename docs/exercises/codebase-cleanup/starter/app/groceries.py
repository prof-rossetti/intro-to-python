
# READ INVENTORY OF PRODUCTS

#products_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "products.csv")
#products_df = read_csv(products_filepath)
#products = products_df.to_dict("records")

import os

# checks to see if a products.csv file exists. If not, it uses the default
if os.path.isfile(os.path.join(os.path.dirname(__file__), "..", "data", "products.csv")) == True:
    print("USING CUSTOM PRODUCTS CSV FILE...")
    csv_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "products.csv")
else:
    print("USING DEFAULT PRODUCTS CSV FILE...")
    csv_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "default_products.csv")



from pandas import read_csv

#reads the csv file into products variable
products = read_csv(csv_filepath)
#pandas transforms the data into a list of dictionaries
products = products.to_dict('records')



# PRINTED INVENTORY REPORT

print("---------")
print("THERE ARE", len(products), "PRODUCTS:")
print("---------")

for p in products:
    print("..." + p["name"] + "   " + '${:,.2f}'.format(p["price"]))


all_prices = []
for p in products:
    all_prices.append(float(p["price"]))

import statistics
avg_price = statistics.median(all_prices)

print("---------")
print("AVERAGE PRICE:", '${:,.2f}'.format(avg_price))





# EMAIL INVENTORY REPORT

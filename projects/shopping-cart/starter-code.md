# Shopping Cart - Starter Code


## Image Display

Image display examples:

```py
#
# IMAGE DISPLAY
# ... run this cell to display some example images
# ... (and feel free to adapt the approach if you'd like to display the product images later)
#

from IPython.display import Image, display

print("-----------")
print("EXAMPLE IMAGE DISPLAY:")

print("-----------")
#image_url = "https://smartdesignworldwide.com/wp-content/uploads/2018/05/nyu-logo.jpg"
image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Georgetown_Hoyas_logo.svg/64px-Georgetown_Hoyas_logo.svg.png"
display(Image(url=image_url, height=100))

print("-----------")
display(Image(url="https://www.python.org/static/community_logos/python-powered-w-200x80.png"))

print("-----------")
display(Image(url="https://www.shareicon.net/data/128x128/2016/05/04/759867_food_512x512.png", height=100))
```

## Formatter Functions

Price formatting function:

```py
#
# DOLLAR FORMATTING FUNCTION
# ... use this function later if you find it helpful :-)
#

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71



assert to_usd(4.5) == "$4.50"
assert to_usd(1234567890.98765) == "$1,234,567,890.99"
```




## Inventory Options

Choose just one of the inventory options (A, B, or C, based on your desired difficulty level). Whichever you choose we should wind up with a `products` variable as a list of dictionaries.

### Inventory Option A (Hard Coded)

This is the easiest inventory option. If you use this inventory option, there is no need to use other inventory options.

```py
#
# PRODUCTS INVENTORY (OPTION A - HARD CODED)
# ... use this variable as a default products inventory
# ... or comment it out / remove if you end up choosing a different option
#

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

print(type(products))
print(len(products))
print(products)
```

### Inventory Option B (CSV File)

This is one possible inventory option. If you use this inventory option, there is no need to use other inventory options.

Choose one of these two possible hosted CSV files:
  + ["products.csv"](https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products.csv) -- the basic list of products, matches the hard-coded list provided in Inventory Option A
  + ["products-default.csv"](https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products-default.csv) -- contains additional custom products, as well as an additional column of product image URLs

> HINT: see also the pandas [`read_csv` function docs](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html)

```py
#
# PRODUCTS INVENTORY (OPTION B - HOSTED CSV FILE)
# ... use this code to obtain an inventory of products
# ... or comment it out / remove if you end up choosing a different inventory option
#

from pandas import read_csv

products_csv_file = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products.csv"

products_df = read_csv(products_csv_file)
#products_df.index = products_df["id"]
products_df
```

Converting the dataframe to list of dictionaries:

```py
products = products_df.to_dict("records")
```

### Inventory Option C (Google Sheet)

This is perhaps the most real world applicable inventory option. If you use this inventory option, there is no need to use other inventory options.

Here is a link to the [Google Sheet document](https://docs.google.com/spreadsheets/d/1ItN7Cc2Yn4K90cMIsxi2P045Gzw0y2JHB_EkV4mXXpI/edit#gid=1430039847). Choose one of these two sheets:

  + ["products-default" sheet](https://docs.google.com/spreadsheets/d/1ItN7Cc2Yn4K90cMIsxi2P045Gzw0y2JHB_EkV4mXXpI/edit#gid=837633200) -- contains the basic products, with a column of image URLs (same as similarly named CSV Inventory option)
  + ["products-custom" sheet](https://docs.google.com/spreadsheets/d/1ItN7Cc2Yn4K90cMIsxi2P045Gzw0y2JHB_EkV4mXXpI/edit#gid=139638459) -- contains even more products, including ones with barcode identifiers


> HINT: see the [`gspread` package notes](https://github.com/prof-rossetti/intro-to-python/blob/main/notes/python/packages/gspread.md) for starter code (use the colab credentials option, not the local credentials file option)
> 
```py
#
# PRODUCTS INVENTORY (OPTION C - GOOGLE SHEET)
# ... use this code to obtain an inventory of products
# ... or comment it out / remove if you end up choosing a different inventory option
#

```

```py
%%capture

# !pip install gspread==5.5.0

# installing the newest version of the gspread package:
!pip uninstall gspread -y
!pip install gspread --upgrade
```

```py
from google.colab import auth

# asks you to login
auth.authenticate_user()
```

```py
from google.auth import default

# uses your login credentials
creds, _ = default()
print(creds)
```

```py
import gspread

# authorizes the gspread package to use your login credentials (in case we were using a private document)
client = gspread.authorize(creds)
```

```py
# see: https://docs.google.com/spreadsheets/d/1ItN7Cc2Yn4K90cMIsxi2P045Gzw0y2JHB_EkV4mXXpI/edit?usp=sharing
DOCUMENT_ID = "1ItN7Cc2Yn4K90cMIsxi2P045Gzw0y2JHB_EkV4mXXpI" # identifier of the public access database (see document URL)
#SHEET_NAME = "products-default"
SHEET_NAME = "products-custom"

doc = client.open_by_key(DOCUMENT_ID)
sheet = doc.worksheet(SHEET_NAME)

print("DOC:", doc)
print("SHEET:", sheet)
```

```py
# get all rows from the sheet (will need to re-run to re-fetch if the inventory gets updated)

products = sheet.get_all_records(numericise_ignore=[1])
print(type(products))
print(len(products))
print(products)
```

## Product Lookup Function

```py
def lookup_product(product_id):
    """Assumes the "products" variable is in memory as a list of dictionaries.

        Params: product_id (int or string) the identifier or bar code of the product you want to look up.

        Returns: a product dictionary, or None if not found.
    """
    try:
        matching_products = [p for p in products if str(p["id"]) == str(product_id)]
        product = matching_products[0] # triggers IndexError if there are no matches / no first item in the list
        return product
    except IndexError as err:
        return None


assert lookup_product(2)["name"] == "All-Seasons Salt"
assert lookup_product(18)["name"] == "Pizza for One Suprema Frozen Pizza"
assert lookup_product(999) == None
assert lookup_product("OOPS") == None
print("TESTS PASS")
```

## Email Sending Function

This code uses the `sendgrid` Python package to interface with the [SendGrid](https://sendgrid.com/) email sending service.

In order to use this code, you'll first need to create a SendGrid account, verify your single sender address, and obtain an API Key. You will be asked to supply your sender address and API Key via the `getpass` secure input cell below.

> HINT: see the [sendgrid package docs](https://github.com/prof-rossetti/intro-to-python/blob/main/notes/python/packages/sendgrid.md#setup) for more info

```py
#
# EMAIL SENDING (optional)
# ... use this code to send receipt via email
# ... or comment it out / remove if you end up not sending email receipts
#
```

```py
%%capture

# install sendgrid package (specific version that will work with the email sending function provided below)
!pip install sendgrid==6.5.0
```

```py
from getpass import getpass

SENDGRID_API_KEY = getpass("Please input your Sendgrid API Key: ")
SENDER_ADDRESS = getpass("Please input your Sender Email Address: ")
```

```py
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_email(subject="[Shopping Cart App] This is a test", html="<p>Hello World</p>", recipient_address=SENDER_ADDRESS):
    """
        Sends an email with the specified subject and html contents to the specified recipient,

        If recipient is not specified, sends to the admin's sender address by default.
    """
    client = SendGridAPIClient(SENDGRID_API_KEY) #> <class 'sendgrid.sendgrid.SendGridAPIClient>
    print("CLIENT:", type(client))
    print("SUBJECT:", subject)
    #print("HTML:", html)

    message = Mail(from_email=SENDER_ADDRESS, to_emails=recipient_address, subject=subject, html_content=html)
    try:
        response = client.send(message)
        print("RESPONSE:", type(response)) #> <class 'python_http_client.client.Response'>
        print(response.status_code) #> 202 indicates SUCCESS
        return response
    except Exception as e:
        print("OOPS", type(e), e)
        return None

```

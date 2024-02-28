# "Shopping Cart" Further Exploration Challenges

This document provides optional project challenges for students seeking a greater level of difficulty. 
 
## Configuring Sales Tax Rate

> BONUS POINTS: 3-4% (RECOMMENDED)

The store owner likes your work and wants to use your app in all their regional locations. But different municipalities use different sales tax rates. Instead of hard-coding a single sales tax rate, allow each user to configure their own tax rate via an environment variable called `TAX_RATE`.

> NOTE: Use a ".env" file approach for managing environment variables. Your "README.md" file must contain instructions for how the user can set up their own local ".env" file, including an example of the variable assignment:
> 
>      # this is the ".env" file...
>      
>      TAX_RATE=0.0875

> NOTE: The ".env" file must be ignored from version control, by using a corresponding entry in the ".gitignore" file. 
>
>     # this is the ".gitignore" file...
>    
>     # ignore environment variables in the ".env" file:
>     .env
    

> HINT: use [the `os` module](/notes/python/modules/os.md) in conjunction with [the `dotenv` package](/notes/python/packages/dotenv.md)

> HINT: you might need to use the `float()` function to convert the environment variable value to a float datatype, so you can perform numeric calculations with it



## Handling Pricing per Pound

> BONUS POINTS: 0 (FOR FUN ONLY)

Add a new product called "Organic Bananas" to the products inventory. Assign it a price of `0.79`, but add another attribute called something like `price_per` to indicate the item is priced per "pound". Update all the other product dictionaries to match the new structure, indicating they are priced per "item".

When running the program, if the clerk inputs the identifier of the bananas (or any other item that is priced by pound), the program should ask the clerk to input the number of pounds (e.g. `2.2`), then the program should calculate the price accordingly.

## Writing Receipts to File

> BONUS POINTS: 0 (FOR FUN ONLY)

In addition to displaying a receipt at the end of the checkout process, the program should write the receipt information into a new ".txt" file saved in a new "receipts" directory inside the project repository. The clerk's printer-connected computer should be able to actually print a paper receipt from the information contained in this file.

Each text file should be named according to the date and time the checkout process started (e.g. "/receipts/2019-07-04-15-43-13-579531.txt", where the numbers represent the year, month, day, 24-hour-style hour, minute, second, and milliseconds/microseconds, respectively).

> HINT: consult the notes on [file management](/notes/python/file-management.md) for examples of how to write to file in Python

> NOTE: to prevent clutter, exclude these receipt files from being tracked in version control by adding a new entry to the ".gitignore" file:
>
>     # this is the ".gitignore" file...
>
>     # ...
>     
>     # ignore all TXT files written to the receipts directory:
>     receipts/*.txt
>

## Sending Receipts via Email

> BONUS POINTS: 6-8% (RECOMMENDED)

In addition to displaying a receipt at the end of the checkout process, the program should prompt the checkout clerk or the customer to indicate whether the customer would like to receive the receipt by email. And if so, it should prompt the checkout clerk or the customer to input the customer's email address, and then it should send the receipt information to the customer by email. The clerk's network-connected computer should be able to send these emails.

At the very least, the email should display the checkout timestamp and the total price. But ideally it should contain all the receipt information described in the basic requirements.

> HINT: leverage the email-sending capabilities of [the `sendgrid` package](/notes/python/packages/sendgrid.md), and optionally use [SendGrid Email Templates](/notes/python/packages/sendgrid.md#email-templates) to further control the formatting of email contents.

> NOTE: your README file must contain instructions for how someone can obtain their own credentials and set up a local ".env" file. If you use a template, your README must include instructions for how someone could re-create that template (including sample HTML and sample data).


## Integrating with a CSV File Datastore

> BONUS POINTS: 3-5%

Instead of using a hard-coded `products` variable, download or copy the contents of the provided ["products.csv" file](https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products.csv) into your project directory in a new subdirectory called "data" (so the path to the CSV file should be "data/products.csv"). Then update your code to read the `products` from this CSV file.

> HINT: leverage the capabilities of [the `csv` module](/notes/python/modules/csv.md) (not recommended) or [the `pandas` package](/notes/python/packages/pandas.md) (recommended) for CSV file management.

> NOTE: ideally also use the `os` module to assemble [OS-agnostic relative filepaths](https://github.com/prof-rossetti/intro-to-python/blob/main/notes/python/modules/os.md#constructing-filepaths) instead of hard-coded string filepaths:
>
>     # this is the "app/shopping_cart.py file...
>     
>     # HINT: this might be something like the filepath you are looking for!
>     csv_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "products.csv")
>     

Ideally we'll allow the user to use their own custom CSV file inventory. To acheive this, save a copy of the provided "products.csv" file in your repo as "data/default_products.csv" and provide instructions in the README telling someone to copy this provided file into their local repo as "data/products.csv", where the program will be looking for it. 


Finally, before making any commits, exclude the "data/products.csv" file from being tracked in version control by using an entry like this in the ".gitignore" file:
>
>     # this is the ".gitignore" file...
>
>     # ...
>
>     # ignore the products CSV file inventory (but not the default):
>     data/products.csv
>     !data/default_products.csv
>
> NOTE: to clarify, the "data/default_products.csv" file should be INCLUDED in version control, while the "data/products.csv" should be IGNORED. 

This allows each user to use their own custom inventory of products, and change those items without the changes getting tracked in version control. This allows many developers with different inventories to share the same code base.



## Integrating with a Google Sheets Datastore

> BONUS POINTS: 6-8%

Instead of using a hard-coded `products` variable or a "products.csv" file as the application's datastore, use a Google Sheet like this provided [products Google Sheet document](https://docs.google.com/spreadsheets/d/1ItN7Cc2Yn4K90cMIsxi2P045Gzw0y2JHB_EkV4mXXpI/edit#gid=1014123801) instead. Update your code to read the `products` from this Google Sheet, or a similar one you create. If you create your own, the document permissions should be public so evaluators can run your app using their own credentials.

> HINT: leverage the capabilities of [the `gspread` package](/notes/python/packages/gspread.md).

> NOTE: you'll need to download a google credentials JSON file into your repo, but this file must ABSOLUTELY be ignored from version control. HINT: you can use an entry like the following in your ".gitignore" file:
> 
>     # this is the .gitignore file
>
>     # ignore environment variables:
>     .env
>     
>     # ignore google credentials:
>     # if you want to name your credentials "google-credentials.json":
>     google-credentials.json 
>     # otherwise use this catch-all to ignore all JSON files:
>     *.json   


## Integrating with a Barcode Scanner

> BONUS POINTS: 0 (FOR FUN, NO WAY TO VERIFY)

Assemble a handful of real products that have barcodes.

Ask to borrow the professor's barcode scanner during class or office hours, or feel free to [purchase a barcode scanner from Amazon](https://www.amazon.com/UNIDEEPLY-Barcode-Scanner-Handheld-Scanning/dp/B07GYLKX4J/ref=sr_1_1_sspa). Some barcode scanners have a normal USB-A connection, so new Mac users without these ports may also need a [USB-A to USB-C adapter](https://www.amazon.com/nonda-Adapter-Thunderbolt-MacBook-Devices/dp/B083DRSWKR/?th=1).


Connect the barcode scanner to your computer's USB port, and practice scanning a few of the items, and record the resulting product identifiers.

Adapt the program's `products` variable (or CSV file or Google Sheet, or whatever datastore you're using) to reflect the real products and their identifiers. For example:

```py
# shopping_cart.py
# ...
products = [
    {"id": "99482452704", "name": "Organic Black Beans", "price": 0.99},
    {"id": "99482434182", "name": "Organic Almonds Roasted Unsalted", "price": 7.33},
    {"id": "99482418939", "name": "Jug of Spring Water", "price": 0.99},
    {"id": "898248001107", "name": "Siggi's Strawberry Yogurt", "price": 1.45},
    {"id": "898248001114", "name": "Siggi's Peach Yogurt", "price": 1.45},
    {"id": "290295004269", "name": "Whole Foods Guacamole - Small", "price": 6.50},
    {"id": "012000161155", "name": "LIFE Water", "price": 2.15},
] # NOTE: these products are abbreviated for display. yours should also include some "department" and "aisle" values of choice
# ...
```

> NOTE: for real life products, we'll probably want to change the identifier values to strings, in case any contain alphabetic characters or leading zeros (e.g. "LIFE water" identifier above).

After modifying the product list, try re-running the program, using the barcode scanner to scan the real items. It should work!

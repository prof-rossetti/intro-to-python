# Stocks Dashboard - Starter Code

Feel free to use any of this code in your solution.

## Setup

Secure / masked input for AlphaVantage API Key:

```py
#
# SETUP CELL (run and leave as-is)
#

from getpass import getpass

API_KEY = getpass("Please input your AlphaVantage API Key: ")
```

## Helper Functions

USD Formatter function:

```py
#
# SETUP CELL (run and leave as-is, and feel free to use this function as needed later)
#

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}"


# example invocations and unit tests:
assert to_usd(4.5) == "$4.50"
assert to_usd(200000.9999) == "$200,001.00"
```


Percent sign formatting function:

```py
#
# SETUP CELL (run and leave as-is, and feel free to use this function as needed later)
#

def to_pct(my_number):
    """
    Formats a decimal number as a percentage, rounded to 4 decimal places, with a percent sign.

    Param my_number (float) like 0.95555555555

    Returns (str) like '95.5556%'
    """
    return f"{(my_number * 100):.2f}%"


# example invocations and unit tests:
assert to_pct(0.5) == "50.00%"
assert to_pct(.955555555) == "95.56%"
```



### Example of Fetching Data


```py
from pandas import read_csv

symbol = "NFLX" # "OOPS"
request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={API_KEY}&datatype=csv"

df = read_csv(request_url)
print("timestamp" in df.columns) # example VALIDATION LOGIC
df.head()
```

### Report Generation Function


```py
# as a matter of practice, for quicker development and testing:
# ... it is probably easier to first arrive at your solution code
# ... and then at the very end when you are satisfied with your solution code,
# ... you can package up all the necessary parts into this stand-alone function

from pandas import read_csv

def generate_stocks_report(symbol="NFLX"):
    print(symbol)

    # TODO: compile request URL

    # TODO: fetch the data

    # TODO: validate the response

    # TODO make a chart (and show it)

    # TODO: analyze the data and print the results


```

### Dashboard

Colab dropdown menu, for invoking the report generation function and passing in the selected symbol:

```py
# @title Stock Selection Form

selected_symbol = "NFLX" # @param ['MSFT', 'GOOGL', 'AAPL', 'NFLX', "SBUX", "TSLA", "DIS", "NVDA"]

generate_stocks_report(selected_symbol)
```

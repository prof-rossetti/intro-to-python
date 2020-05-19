# "Exec Dash" Further Exploration Challenges

## Functionality Challenges

### Validating CSV Headers

If the user selects a data file which contains invalid/unexpected header rows, the program should stop execution and display a friendly error message like "Oh, the selected file contains unexpected headers. Please try again."

### Comparing Sales Across Months

Create a separate script in your project repository called "multi_month.py". When executed, this program should import data from at least three of the monthly sales CSV files and compare the results. Which months have the highest sales? Lowest? What is the trend of sales over time?

Visualize the sales over time using a column or bar chart with time on the x axis and sales on the y axis.

> HINT: for processing all CSV files, try using the `os` module to detect the names of all CSV files which exist in the "data" directory, and loop through each one at a time, processing its data and either storing the results in memory or to a separate CSV file.

### Normalizing Data Across Months

Different months can contain a different numbers of days. Is it totally accurate to compare sales for a 28-day month against sales for a 31-day month? And what about the proportion of weekend days vs weekdays?

Your program should somehow take these and other irregularities into account when comparing sales across months, smoothing them as much as possible to facilitate accurate comparisons.

### Predicting Monthly Sales

See the ["Monthly Sales Predictions" Exercise](/exercises/monthly-sales-predictions/README.md) for instructions.

## Automated Testing Challenges

### Formatting Prices

Refactor price-formatting logic into a function called something like `to_usd()`, and implement a corresponding test called something like `test_to_usd()`.

Test various scenarios to ensure the price formatting function displays a dollar sign, two decimal places, and a thousands separator.

### Identifying Top Sellers

Refactor top-selling product identification logic into a function called something like `get_top_sellers()`, and implement a corresponding test called something like `test_top_sellers()`.

Include an example valid monthly sales CSV file somewhere in your test directory, and have your test read the sales data from this file.

Test to ensure the function converts the example sales data into a list of top selling products. What should the resulting data structure look like?

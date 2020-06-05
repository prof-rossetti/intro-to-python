# "Exec Dash" Further Exploration Challenges

## Validating CSV Headers

If the user selects a data file which contains invalid/unexpected header rows, the program should stop execution and display a friendly error message like "Oh, the selected file contains unexpected headers. Please try again."

## Comparing Sales Across Months

Create a separate script in your project repository called "multi_month.py". When executed, this program should import data from at least three of the monthly sales CSV files and compare the results. Which months have the highest sales? Lowest? What is the trend of sales over time?

Visualize the sales over time using a column or bar chart with time on the x axis and sales on the y axis.

> HINT: for processing all CSV files, try using the `os` module to detect the names of all CSV files which exist in the "data" directory, and loop through each one at a time, processing its data and either storing the results in memory or to a separate CSV file.

## Normalizing Data Across Months

Different months can contain a different numbers of days. Is it totally accurate to compare sales for a 28-day month against sales for a 31-day month? And what about the proportion of weekend days vs weekdays?

Your program should somehow take these and other irregularities into account when comparing sales across months, smoothing them as much as possible to facilitate accurate comparisons.


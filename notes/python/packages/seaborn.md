# The `seaborn` Package

**Created by Kuran Malhotra**

> Seaborn is a library for making statistical graphics in Python. It is built on top of matplotlib and closely integrated with pandas data structures. — [Seaborn website](https://seaborn.pydata.org/)

## Reference

+ https://seaborn.pydata.org/
+ https://github.com/mwaskom/seaborn
+ https://seaborn.pydata.org/tutorial.html
+ https://seaborn.pydata.org/examples/index.html
+ https://www.datacamp.com/community/tutorials/seaborn-python-tutorial
+ Styles: https://seaborn.pydata.org/generated/seaborn.set.html

## What's the difference between `seaborn` and `matplotlib`?

Seaborn is designed to be more user-friendly and to work better with `pandas` dataframes. For more information on dataframes and the `pandas` package see [here](https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/packages/pandas.md). It is also easier to customize plot colors, formats, etc. with Seaborn. Because seaborn is built on top of matplotlib, you will have to use commands from both packages for many operations.

Before diving into seaborn, make sure you brush up on your matplotlib skills! [Click here for more information on matplotlib.](https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/packages/matplotlib.md)

## Installation

First install the package using Pip, if necessary:

```sh
pip install seaborn
```

## Usage

**Constructing a Scatterplot:**

```py
# adapted from https://seaborn.pydata.org/tutorial/relational.html

import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="darkgrid")

# .set() function changes the plot's aesthetics. 

# For more information and specific styles see: https://seaborn.pydata.org/generated/seaborn.set.html

tips = sns.load_dataset("tips")

# .load_dataset() function pulls data in.

sns.relplot(x="total_bill", y="tip", hue="smoker", data=tips);

# the .relplot() function creates a relational plot using an x-axis / y-axis basis. this function allows you to change the markers, colors, sizes, etc. that you're working with. 

plt.show() # need to explicitly "show" the chart window
```
![the resulting scatterplot - two axes, two data sets](https://raw.githubusercontent.com/kmalhotra13/intro-to-python/master/notes/python/packages/seaborn_screenshot.png)

> NOTE: once you "show" the chart, you'll see the chart open in native window on your computer. You'll be able to view your chart, but when you're done you'll need to close the chart window in order to regain the ability to type commands in your terminal window.

Consult the documentation and examples for a variety of chart customization options.


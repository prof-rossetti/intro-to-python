# The `matplotlib` Package

> Matplotlib is a Python 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms... Matplotlib tries to make easy things easy and hard things possible. You can generate plots, histograms, power spectra, bar charts, errorcharts, scatterplots, etc., with just a few lines of code. - [Matplotlib website](https://matplotlib.org/)

## Reference

  + https://github.com/matplotlib/matplotlib
  + https://matplotlib.org/
  + https://matplotlib.org/gallery/index.html
  + https://matplotlib.org/tutorials/introductory/sample_plots.html
  + https://matplotlib.org/gallery/showcase/anatomy.html
  + https://pythonspot.com/matplotlib-gallery/
  + https://pythonspot.com/matplotlib-bar-chart/

## Installation

First install the package using Pip, if necessary:

```sh
pip install matplotlib
```

## Usage

To display a new chart, construct it by specifying certain chart configuration options, including the type of chart (e.g. pie chart), and the data to visualize:

```py
# adapted from: https://matplotlib.org/gallery/pie_and_polar_charts/pie_features.html

import matplotlib.pyplot as plt

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = ["Product A", "Product B", "Product C", "Product D"]
sizes = [15, 30, 45, 10]

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show() # need to explicitly "show" the chart window
```

![the resulting chart - a pie chart with four slices](https://user-images.githubusercontent.com/1328807/52388791-0aeb5c80-2a5e-11e9-820a-ee23541ace93.png)

> NOTE: once you "show" the chart, you'll see the chart open in native window on your computer. You'll be able to view your chart, but when you're done you'll need to close the chart window in order to regain the ability to type commands in your terminal window.

Consult the documentation and examples for a variety of chart customization options.

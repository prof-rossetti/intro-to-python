# The `plotly` Package

> Plotly is an open-source, interactive graphing library for Python - [Plotly GitHub repo](https://github.com/plotly/plotly.py)

## Reference

  + https://github.com/plotly/plotly.py
  + https://plot.ly/python/
  + https://plot.ly/python/reference/
  + https://plot.ly/python/reference/#layout
  + https://plot.ly/python/getting-started/
  + https://plot.ly/python/user-guide/
  + https://plot.ly/python/static-image-export/#write-image-file
  + https://plot.ly/python/setting-graph-size/
  + https://plot.ly/python/bar-charts/
  + https://plot.ly/python/horizontal-bar-charts/

## Installation

First install the package using Pip, if necessary:

```sh
pip install plotly
```

## Usage

For learning purposes, prefer to construct charts using the ["offline" versions](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) which don't require a Plotly account or API key.

To display a new chart, construct it by specifying certain chart configuration options, including the type of chart (e.g. scatterplot), and the data to visualize:

```py
# adapted from: https://plot.ly/python/getting-started/#initialization-for-offline-plotting

import plotly
import plotly.graph_objs as go

plotly.offline.plot({
    "data": [go.Scatter(x=[1, 2, 3, 4], y=[4, 3, 2, 1])],
    "layout": go.Layout(title="hello world")
}, auto_open=True)
```

![the resulting chart - a boring straight line with four points](https://user-images.githubusercontent.com/1328807/52389188-37a07380-2a60-11e9-9bbf-433dafa12886.png)


> NOTE: after a few seconds, the chart will automatically open in your web browser.

Consult the documentation and examples for a variety of chart customization options.

### More Examples

A pie chart example:

```py
# adapted from: https://plot.ly/python/pie-charts/

import plotly
import plotly.graph_objs as go

labels = ["Oxygen", "Hydrogen", "Carbon_Dioxide", "Nitrogen"]
values = [4500, 2500, 1053, 500]

trace = go.Pie(labels=labels, values=values)

plotly.offline.plot([trace], filename="basic_pie_chart.html", auto_open=True)
```

### Charting Multiple Graph Objects


```py

# assuming df is some DataFrame with columns of "timestamp", "closing_price", and "trendline"...

from plotly.graph_objects import Figure, Scatter

closing_prices = Scatter(x=df["timestamp"], y=df["closing_price"], name='Closing Prices')
    
trendline = Scatter(x=df["timestamp"], y=df["trendline"], name='50 day Moving Average')

fig = Figure(data=[closing_prices, trendline]) 
fig.update_layout(title="My Chart Title")
fig.show()
```

![the resulting chart - a pie chart with four slices](https://user-images.githubusercontent.com/1328807/52388830-38380a80-2a5e-11e9-8e7b-6951e083a265.png)

## Plotly Express

See also [the `plotly.express` package](https://plotly.com/python/plotly-express/), which allows you to construct graphs from pandas DataFrames.




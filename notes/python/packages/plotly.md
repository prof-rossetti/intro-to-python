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
  + https://plotly.com/python/plotly-express/

## Installation

First install the package using Pip, if necessary:

```sh
pip install plotly
```

## Usage

When using the Plotly package, we can use the high-level "plotly express" interface (RECOMMENDED), or the lower level "graph objects" interface (see corresponding sections below).

### Plotly Express

When using Plotly Express, we choose a charting function, like `bar` (see [docs](https://plotly.com/python-api-reference/generated/plotly.express.bar)), and pass in some data along with some chart customization options, like adding a title, axis labels, etc.


We can pass the data to the charting function using a `pandas.DataFrame` object, or raw data (lists). See corresponding sections below.


#### Plotly Express with Raw Data


Basic bar:

```py
from plotly.express import bar

# FYI: these lists are related based on their order (e.g. assume Romantic Comedy has 121212 viewers)
genres = ['Romantic Comedy', 'Thriller', 'Mystery', 'Documentary', 'Action', 'Fantasy', 'Sci-Fi']
viewers = [121212, 123456, 234567, 283105, 544099, 876543, 987654]

fig = bar(x=genres, y=viewers)
fig.show()
```
![newplot (2)](https://user-images.githubusercontent.com/1328807/180882858-d6c9b4e7-423e-4da7-af46-3e7a7c5fb53f.png)


With title and axis labels:

```py
fig = bar(x=genres, y=viewers, title="Viewers per Genre", labels={"y": "Genre", "x": "Viewers"})
fig.show()
```

![newplot (3)](https://user-images.githubusercontent.com/1328807/180882866-f2ef7af3-0679-4d66-b276-a83014137d08.png)


Horizontal bar:

```py
# NOTE: for horizontal orientation, need to switch x and y 
fig = bar(x=viewers, y=genres, orientation="h", title="Viewers per Genre", labels={"y": "Genre", "x": "Viewers"})
fig.show()
```

![newplot (4)](https://user-images.githubusercontent.com/1328807/180882871-adb973a9-4474-47b7-8c2d-a09b25809257.png)


With [colors](https://plotly.com/python/builtin-colorscales/):

```py
fig = bar(x=viewers, y=genres, orientation="h", title="Viewers per Genre", labels={"y": "Genre", "x": "Viewers"},
          color=viewers, color_continuous_scale="Pinkyl"
)
fig.show()
```
![newplot (5)](https://user-images.githubusercontent.com/1328807/180882876-9d09606d-8ab8-454b-8f54-fe9353c01a5e.png)


#### Plotly Express with Data Frames

Once you learn about `pandas.DataFrame` objects, we can chart them similarly, but we reference the column names of the `DataFrame`:

```py
from pandas import DataFrame
from plotly.express import bar

df = DataFrame([
    {"genre": "Thriller", "viewers": 123456},
    {"genre": "Mystery", "viewers": 234567},
    {"genre": "Sci-Fi", "viewers": 987654},
    {"genre": "Fantasy", "viewers": 876543},
    {"genre": "Documentary", "viewers": 283105},
    {"genre": "Action", "viewers": 544099},
    {"genre": "Romantic Comedy", "viewers": 121212}
])

fig = bar(data_frame=df, x="genre", y="viewers")
fig.show()

# ... etc.
```

```py
fig = bar(data_frame=df, x="genre", y="viewers"
            
    # from the docs: "The keys of this dict should correspond to column names, 
    # and the values should correspond to the desired label to be displayed.
    labels={"genre": "Movie Genre", "viewers": "Viewers"},

    color="viewers"
)
fig.show()
```















### Graph Objects

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

#### More Examples

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

![the resulting chart - a pie chart with four slices](https://user-images.githubusercontent.com/1328807/52388830-38380a80-2a5e-11e9-8e7b-6951e083a265.png)

#### Charting Multiple Graph Objects


```py

# assuming df is some DataFrame with columns of "timestamp", "closing_price", and "trendline"...

from plotly.graph_objects import Figure, Scatter

closing_prices = Scatter(x=df["timestamp"], y=df["closing_price"], name='Closing Prices')
    
trendline = Scatter(x=df["timestamp"], y=df["trendline"], name='50 day Moving Average')

fig = Figure(data=[closing_prices, trendline]) 
fig.update_layout(title="My Chart Title")
fig.show()
```

<img width="705" alt="Screen Shot 2022-02-16 at 2 58 18 PM" src="https://user-images.githubusercontent.com/1328807/154346057-09fe84e6-423b-4f8a-93b8-a11111e3a75e.png">







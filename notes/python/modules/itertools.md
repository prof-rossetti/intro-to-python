# The `itertools` Module

Reference: https://docs.python.org/3/library/itertools.html.

## Usage

### Combinations and Permutations

```py
from itertools import combinations

vals = ["M", "C", "P", "Z"]
combos = combinations(vals, 2) # choose 2
list(combos) #> [('M', 'C'), ('M', 'P'), ('M', 'Z'), ('C', 'P'), ('C', 'Z'), ('P', 'Z')]
```

### Grouping

Use the `itertools` module to perform advanced operations on iterable objects such as lists.

Group a list of dictionaries by key:

```python
import itertools
from operator import itemgetter

teams = [
    {"city": "New York", "name": "Yankees"},
    {"city": "New York", "name": "Mets"},
    {"city": "Boston", "name": "Red Sox"},
    {"city": "New Haven", "name": "Ravens"}
]

sorted_teams = sorted(teams, key=itemgetter("city")) # sort by some attribute

teams_by_city = itertools.groupby(sorted_teams, key=itemgetter("city")) # group by the sorted attribute
#> <itertools.groupby object at 0x10339dc50>

for city, teams in teams_by_city:
    print("----------------------------")
    print(city.upper() + ":")
    for team in teams:
        print("  + " + team["name"])

#> ----------------------------
#> BOSTON:
#>   + Red Sox
#> ----------------------------
#> NEW HAVEN:
#>   + Ravens
#> ----------------------------
#> NEW YORK:
#>   + Yankees
#>   + Mets
```

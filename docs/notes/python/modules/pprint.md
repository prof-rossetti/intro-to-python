# The `pprint` Module

The `pprint` module provides a way to "pretty print", or customize the formatting of print statements.

## Usage

Pretty-print:

```py
from pprint import pprint

pprint({"id": 1, "name": "Chocolate Sandwich Cookies", "aisle": "cookies cakes", "department": "snacks", "price": 3.5})
#> {'aisle': 'cookies cakes',
#>   'department': 'snacks',
#>   'id': 1,
#>   'name': 'Chocolate Sandwich Cookies',
#>   'price': 3.5}
```

Pretty-print using custom indentation settings:

```py
import pprint

pp = pprint.PrettyPrinter(indent=4)

pp.pprint({"id": 1, "name": "Chocolate Sandwich Cookies", "aisle": "cookies cakes", "department": "snacks", "price": 3.5})
#> {   'aisle': 'cookies cakes',
#>     'department': 'snacks',
#>     'id': 1,
#>     'name': 'Chocolate Sandwich Cookies',
#>     'price': 3.5}
```

# The `statistics` Module

Reference: https://docs.python.org/3/library/statistics.html.

Once you have learned about lists, you can perform statistics-related operations on them:

```python
import statistics # load the module to avoid `NameError: name 'statistics' is not defined`

arr = [1, 2, 2, 3, 4, 6, 7, 8, 9]

statistics.mean(arr) #> 4.666666666666667

statistics.median(arr) #> 4

statistics.mode(arr) #> 2
```

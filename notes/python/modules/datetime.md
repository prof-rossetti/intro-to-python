# The `datetime` Module

Reference:

  + https://docs.python.org/3/library/datetime.html
  + https://docs.python.org/3/library/datetime.html#date-objects
  + https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior

Use the `datetime` module to handle dates and times:

```python
import datetime

today = datetime.date.today()
print(str(today)) #> '2017-07-02'

now = datetime.datetime.now()
print(str(now)) #> '2017-07-02 23:43:25.915816'
print(now.strftime("%Y-%m-%d")) #> '2017-07-02'

july_fourth = datetime.date(2017, 7, 4)
print(str(july_fourth)) #> '2017-07-04'
print(july_fourth.year) #> 2017
print(july_fourth.month) #> 7
print(july_fourth.day) #> 4
print(july_fourth.weekday()) #> 1
print(july_fourth.strftime("%Y-%m-%d")) #> "2017-07-04"

some_day = datetime.datetime.strptime("2020, 12, 31", "%Y, %m, %d")
str(some_day) #> '2020-12-31 00:00:00'
```

```python
from datetime import datetime

now = datetime.now()
print(now) #> 2021-01-29 15:44:30.073718
print(now.strftime("%Y-%m-%d")) #> 2021-01-29
print(now.strftime("%H:%M:%S")) #> 15:44:30
print(now.strftime("%Y-%m-%d %H:%M:%S")) #> 2021-01-29 15:44:30
```




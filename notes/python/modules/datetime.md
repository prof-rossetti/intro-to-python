# The `datetime` Module

Reference:

  + https://docs.python.org/3/library/datetime.html
  + https://docs.python.org/3/library/datetime.html#date-objects
  + https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior

The `datetime` module provides capabilities for handling dates and times. See the "Date Parsing" section below for some ways we can create official datetime objects, and the "Date Formatting" section for some ways to format or display these objects.

> NOTE: the difference between a `datetime.date` object and a `datetime.datetime` object is that only the latter has information about hours, minutes, and seconds.

## Date Parsing

We can create our own date or datetime objects by passing in some hard-coded info (not the most common):

```py
import datetime

my_date = datetime.date(2021, 7, 4) 
print(type(my_date)) #> <class 'datetime.date'>
print(my_date) #> 2017-07-04

my_datetime = datetime.datetime(2017, 7, 4, 10, 59, 59)
print(type(my_datetime)) #> <class 'datetime.datetime'>
print(my_datetime) #> 2017-07-04 10:59:59
```

Alternatively, we can reference some built-in methods to get objects representing the current date and/or time:

```py
import datetime

today = datetime.date.today()
print(type(today)) #> <class 'datetime.date'>
print(today) #> 2021-03-08

now = datetime.datetime.now()
print(type(now)) #> <class 'datetime.datetime'>
print(now) #> 2021-03-08 18:26:47.259366
```

Alternatively, we can convert a datetime-like string to an official datetime object, either by specifying the string's date format template to the `.strptime()` method, or by using a separate parsing method provided by the `dateutil` module:


```py
import datetime

start_time = '2021-03-04T19:00:00-05:00' # this is the given string we want to parse
template = '%Y-%m-%dT%H:%M:%S%z' # this is the format code corresponding with the given string we want to parse

dt = datetime.datetime.strptime(start_time, template)
print(type(dt)) #> <class 'datetime.datetime'>
print(dt) #> 2021-03-04 19:00:00-05:00
```

```py
import dateutil.parser

start_time = '2021-03-04T19:00:00-05:00'
dt = dateutil.parser.parse(start_time)

print(type(dt)) #> <class 'datetime.datetime'>
print(dt) #> 2021-03-04 19:00:00-05:00
```


## Date Formnatting

Unlike strings, these date and datetime objects are aware of their own datetime-related properties (like year or day of week):

```py
print(my_date.year) #> 2021
print(my_date.month) #> 7
print(my_date.day) #> 4
print(my_date.weekday()) #> 1
```

And we can customize the formatting of any date or datetime object by passing a format code to the `strftime()` method:

```py
print(my_datetime.strftime("%Y-%m-%d")) #> 2017-07-04
print(my_datetime.strftime("%H:%M:%S")) #> 10:59:59
print(my_datetime.strftime("%Y-%m-%d %H:%M:%S")) #> 2017-07-04 10:59:59
```

> NOTE: here is the [list of official "format codes"](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes) we can use in conjunction with the `.strptime()` and `strftime()` methods.



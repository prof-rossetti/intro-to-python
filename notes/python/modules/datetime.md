# The `datetime` Module

Reference:

  + https://docs.python.org/3/library/datetime.html
  + https://docs.python.org/3/library/datetime.html#date-objects
  + https://docs.python.org/3/library/datetime.html#datetime-objects
  + https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
  + https://docs.python.org/3/library/datetime.html#timedelta-objects

The `datetime` module provides capabilities for handling dates and times. See the "Date Parsing" section below for some ways we can create official datetime objects, and the "Date Formatting" section for some ways to format or display these objects.

> NOTE: the difference between a `datetime.date` object and a `datetime.datetime` object is that only the latter has information about hours, minutes, and seconds.

## Creating Datetime Objects

We can create our own date or datetime objects by passing in some hard-coded info representing the year, month, day, etc.:

```py
from datetime import date, datetime

my_date = date(2021, 7, 4) 
print(type(my_date)) #> <class 'datetime.date'>
print(my_date) #> 2017-07-04

my_datetime = datetime(2017, 7, 4, 10, 59, 59)
print(type(my_datetime)) #> <class 'datetime.datetime'>
print(my_datetime) #> 2017-07-04 10:59:59
```

Alternatively, we can create objects representing the current date and/or time:

```py
from datetime import date, datetime

today = date.today()
print(type(today)) #> <class 'datetime.date'>
print(today) #> 2021-03-08

now = datetime.now()
print(type(now)) #> <class 'datetime.datetime'>
print(now) #> 2021-03-08 18:26:47.259366
```

### From Strings

To convert a string into a datetime object, try one of the following approaches...

Option 1, using the `datetime` module and a known / expected string format template:

```py
from datetime import datetime

start_time = '2021-03-04T19:00:00-05:00' # this is the given string we want to parse
template = '%Y-%m-%dT%H:%M:%S%z' # this is the format code corresponding with the given string we want to parse

datetime.strptime(start_time, template)
#> datetime.datetime(2021, 3, 4, 19, 0, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=68400)))
```

Option 2, using the `python-dateutil` package:

```py
# first install package via: pip install python-dateutil 
import dateutil.parser

dateutil.parser.parse('2021-03-04T19:00:00-05:00')
#> datetime.datetime(2021, 3, 4, 19, 0, tzinfo=tzoffset(None, -18000))
```

Option 3, using the awesome `arrow` third party package:

```py
# first install pacakge via: pip install arrow
import arrow

arrow.get('2021-03-04T19:00:00-05:00').datetime
#> datetime.datetime(2021, 3, 4, 19, 0, tzinfo=tzoffset(None, -18000))
```

### With Time Zones

Time zones are one of the tricker parts to working with datetimes. By default time zones are not specified. But we can specify which time zone our dates and times should be in:

Option 1, using the `datetime` module (only for UTC timezone though maybe):

```py
from datetime import timezone

datetime(2030, 1, 1, tzinfo=timezone.utc)
#> datetime.datetime(2030, 1, 1, 0, 0, tzinfo=datetime.timezone.utc)

datetime.now(timezone.utc)
#> datetime.datetime(2022, 8, 23, 15, 50, 54, 349802, tzinfo=datetime.timezone.utc)
```

Option 2, using time zone objects from the `pytz` module (see `pytz.all_timezones` for a list of all time zone names):

```py
import pytz 

tz = pytz.timezone("America/New_York")

datetime(2020, 1, 1, 10, 30, 0, tzinfo=tz)
#> datetime.datetime(2020, 1, 1, 10, 30, tzinfo=<DstTzInfo 'America/New_York' LMT-1 day, 19:04:00 STD>)

datetime.datetime.now(tz)
#> datetime.datetime(2022, 8, 23, 11, 42, 12, 471881, tzinfo=<DstTzInfo 'America/New_York' EDT-1 day, 20:00:00 DST>)
```


Option 3, using the awesome `arrow` package:

```py
import arrow

arrow.get("2020-01-01 13:00", tzinfo="America/New_York").datetime
#> datetime.datetime(2020, 1, 1, 13, 0, tzinfo=tzfile('/usr/share/zoneinfo/America/New_York'))
```



## Formatting Datetime Objects

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

## Time Deltas

Can add or subtract seconds, minutes, hours, days, etc, using `timedelta`:

```py
from datetime import datetime, timedelta

now = datetime.now()
#> datetime.datetime(2022, 8, 23, 11, 19, 34, 769191)

tomorrow = now + timedelta(days=1)
#> datetime.datetime(2022, 8, 24, 11, 19, 34, 769191)

yesterday = now - timedelta(days=1)
#> datetime.datetime(2022, 8, 22, 11, 19, 34, 769191)
```






# APIs

**Application Programming Interfaces (APIs)** provide programmatic access to data. To use them, we request data from specified URLs provided by the API.

For example, we could manually login to Twitter.com, and manually fill out and submit a web form to create a new Tweet. But alternatively we could develop a Python program to do this.

## Fetching Data from APIs vs Web Pages

We can request data from web pages, so why would we use APIs?

Mainly because APIs are **less fragile**. APIs provide guarantees about the data, whereas a web developer can change the structure and markup of their web page at any time - if they do it could break our programs.


## API Investigation Process

After searching the Internet for an API of interest, you MUST **consult the API documentation** to learn:
  + how it wants you to authenticate (as necessary), 
  + which URLs (i.e. "endpoints") to make requests to, and   
  + what the response data structures look like.

Often, the response data will be a nested JSON object which may be hard, or intimidating to parse. Don't worry, just follow this process:

  1. First, identify which **URL "endpoint"** you'd like to make a request to.
  2. Second, make a preliminary **request in the browser**, if possible. The goal is to visually observe the response data structure. 
  3. Optionally copy the data into a [JSON pretty-formatting tool](https://jsonformatter.org/json-pretty-print) to help you visually inspect it, and learn its structure. 
  4. Write Python to make a **programmatic request** for the data.
  5. Write more Python to **explore and process the data**. JSON data is like a nested combination of list and dictionary objects. Work your way down one step at a time, starting from the top level.


## API Response Data Formats

We use different request and parsing strategies, based on what format the expected response data is in.

### JSON Data


1. Make a request for the data using the [`requests` package](https://github.com/prof-rossetti/intro-to-python/blob/main/notes/python/packages/requests.md). Pass the url to the `requests.get` function, and the result will be a string datatype.
2. Use the [`json` module](https://github.com/prof-rossetti/intro-to-python/blob/main/notes/python/modules/json.md
 ) to parse the resulting JSON-looking string.

### CSV Data

1. Make a request for the data using the [`pandas` package](https://github.com/prof-rossetti/intro-to-python/blob/main/notes/python/packages/pandas.md). Pass the url to the `pandas.read_csv` function, and the result will be a `pandas.DataFrame` object, which is easy to work with.
2. That's it! No need to process any nested structures.

### HTML Data

1. Make a request for a web page using [`requests` package](https://github.com/prof-rossetti/intro-to-python/blob/main/notes/python/packages/requests.md). Pass the url to the `requests.get` function, and the result will be a string datatype.
2. Use the [`BeautifulSoup` package](https://github.com/prof-rossetti/intro-to-python/blob/main/notes/python/packages/beautifulsoup.md
 ) to parse the resulting HTML-looking string.


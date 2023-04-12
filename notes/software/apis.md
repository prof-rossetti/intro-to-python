# Application Programming Interfaces (APIs)

> Prerequisite: [Computer Networks](/notes/info-systems/networks.md)

Today, the way most humans are familiar with interacting with computer-based information systems is through visually- and spatially-oriented interfaces known as **Graphical User Interfaces (GUI)**. GUI interactions include clicking, dragging, tapping, and other gestures.

But many systems additionally or alternatively allow programmatic usage through textually-oriented interfaces known as **Application Programming Interfaces (APIs)**. APIs provide the instructions and mechanisms for a human or computer to programmatically interact with the system.















## Web Services

**Web Services** are APIs which facilitate the transmission of a system's data across the Internet. Web services provide one or more servers which accept HTTP requests at specified URLs and return HTTP responses containing textual information in a machine-readable format.

Some notable example web services and providers are listed below. If you find a fun API, you are encouraged to add it to the list.

General Purpose:

  + [Google APIs](https://developers.google.com/apis-explorer/#p/)
 
News and Information:

  + [New York Times APIs](https://developer.nytimes.com/apis)
  + [Alpha Vantage (Stock Market) API](https://www.alphavantage.co/documentation/)
  + [Weather.gov API](https://www.weather.gov/documentation/services-web-api)
  + [ESPN APIs](http://www.espn.com/apis/devcenter/docs/)
  
Music, Movies, and Images:

  + [Spotify API](https://developer.spotify.com/documentation/web-api/)
  + [IMBD (Movies) API](https://developer.imdb.com/documentation)
  + [YouTube API](https://developers.google.com/youtube/v3)
  + [Flickr API](https://www.flickr.com/services/api/)


Social Networks:

  + [Twitter APIs](https://dev.twitter.com/rest/public)
  + [Facebook Social Graph API](https://developers.facebook.com/docs/graph-api)
  + [Instagram API](https://developers.facebook.com/docs/instagram-basic-display-api)
  + [Foursquare API](https://developer.foursquare.com/docs/)
  + [GitHub API](https://developer.github.com/v3/)

Games:

  + [Pokemon API](https://pokeapi.co/)
  + [Dungeons and Dragons API](http://www.dnd5eapi.co/docs/)

Food and Drink:

  + [Yelp API](https://www.yelp.com/developers/documentation/)
  + [Cocktail DB (Drinks) API](https://www.thecocktaildb.com/api.php)

Government:

  + [US Federal Elections Commission API](https://api.open.fec.gov/developers)
  + [NASA APIs](https://api.nasa.gov/)

For Fun:

  + [Cats API](https://developers.thecatapi.com/)
  + [Quiz API](https://quizapi.io/docs/1.0/overview)
  + [Trivia API](https://the-trivia-api.com/)

Other:
  + [Open AI API](https://platform.openai.com/)
 
 
### Requests

#### Authentication

Many web services require developers to first register to obtain valid credentials in the form of an **API Key** (i.e. a secret token string) and subsequently authenticate by providing the key alongside each API request. This allows the service provider to understand who is issuing each request, and can help prevent or mitigate abuse of the service.

#### Request Parameters

Many APIs allow you to specify URL parameters along with your HTTP request. These URL parameters are appended to the end of the API's base URL, starting with a single question mark (`?`) to denote the rest of the URL contains parameters. Then each parameter follows a convention where the name of the parameter is followed by an equal sign (`=`), which is followed by the desired parameter value. If there are multiple parameters, subsequent parameters after the first are separated by the ampersand character (`&`).

Example request URL with parameters, where `https://www.alphavantage.co/query` is the base URL and `function`, `symbol`, `outputsize`, and `apikey` are the parameter names:

```
https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&outputsize=compact&apikey=demo
```

> Note: you might have to register and specify your own API key if you are seeing a message like "The demo API key is for demo purposes only."


### Responses

The most common format for API response data is JSON, but some APIs alternatively or additionally provide response data in XML or CSV format.

Example CSV:

```csv
city,name,league
New York,Mets,Major
New York,Yankees,Major
Boston,Red Sox,Major
Washington,Nationals,Major
New Haven,Ravens,Minor
```

Example JSON:

```js
[
  {"city": "New York", "name": "Yankees", "league":"Major"},
  {"city": "New York", "name": "Mets", "league":"Major"},
  {"city": "Boston", "name": "Red Sox", "league":"Major"},
  {"city": "Washington", "name": "Nationals", "league":"Major"},
  {"city": "New Haven", "name": "Ravens", "league":"Minor"}
]
```

Example XML:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<teams>
  <team>
    <city>New York</city>
    <league>Major</league>
    <name>Yankees</name>
  </team>
  <team>
    <city>New York</city>
    <league>Major</league>
    <name>Mets</name>
  </team>
  <team>
    <city>Boston</city>
    <league>Major</league>
    <name>Red Sox</name>
  </team>
  <team>
    <city>Washington</city>
    <league>Major</league>
    <name>Nationals</name>
  </team>
  <team>
    <city>New Haven</city>
    <league>Minor</league>
    <name>Ravens</name>
  </team>
</teams>
```






### Representational State Transfer (REST)

Most of today's web services follow an architectural pattern called "REST", which involves performing one or more operations (e.g. "create", "read", "update", "destroy") on one or more resources (usually records in a database).

> One of the key characteristics of a RESTful Web service is the explicit use of HTTP methods in a way that follows the protocol as defined by RFC 2616. HTTP GET, for instance, is defined as a data-producing method that's intended to be used by a client application to retrieve a resource, to fetch data from a Web server, or to execute a query with the expectation that the Web server will look for and respond with a set of matching resources.
>
> REST asks developers to use HTTP methods explicitly and in a way that's consistent with the protocol definition. This basic REST design principle establishes a one-to-one mapping between create, read, update, and delete (CRUD) operations and HTTP methods. According to this mapping:
>  + To create a resource on the server, use POST.
>  + To retrieve a resource, use GET.
>  + To change the state of a resource or to update it, use PUT.
>  + To remove or delete a resource, use DELETE.
>
> ... - [IBM website ](https://www.ibm.com/developerworks/library/ws-restful/)

Each web service URL, sometimes also referred to as an **API Endpoint**, corresponds to a given operation and resource. For example, take these [URL naming conventions for an example "photos" resource](http://guides.rubyonrails.org/routing.html#crud-verbs-and-actions):

HTTP Verb | Path | Operation | Used for
---	| ---	| ---	| ---
GET | /photos | List | display a list of all photos
POST | /photos | Create | create a new photo
GET	| /photos/:id | Show | display a specific photo
PATCH/PUT | /photos/:id | Update | update a specific photo
DELETE | /photos/:id | Destroy | delete a specific photo

> FYI: The `:id` variable represents a given resource's unique identifier.




























# Working with APIs

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


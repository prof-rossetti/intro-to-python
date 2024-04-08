# The `BeautifulSoup` Package

> Prerequisite: [the `requests` package](requests.md)

The `BeautifulSoup` package provides a simple way of parsing a website's HTML contents.

Reference: https://www.crummy.com/software/BeautifulSoup/bs4/doc/.

## Installation

First install the package, if necessary:

```sh
pip install beautifulsoup4 # note the 4 at the end - this is the latest version
```

## Usage

You can use this package from the command line or from within a Python program. The examples below depict usage from within a Python program.

### Obtaining Soup Objects

We can obtain a soup object from a page on the internet, or from a local HTML file.

#### HTML from the Internet

When you make a request that returns some HTML string, you can parse it like this:

```py
import requests
from bs4 import BeautifulSoup # note that the import package command is `bs4`

# fetch the webpage HTML

response = requests.get("https://www.gutenberg.org/ebooks/author/65")
response_html = response.text

soup = BeautifulSoup(response_html)

# ...
```

#### Parsing HTML from File

If you have the HTML file locally (for example "index.html"), you can read it using the following approach:

```py
from bs4 import BeautifulSoup # note that the import package command is `bs4`

html_filepath = 'index.html' # or choose a path to your file

# using a "context manager" approach to open the file for reading ("r") and auto-close it afterwards
with open(html_filepath, 'r') as html_file:
    contents = html_file.read()

    soup = BeautifulSoup(contents, 'lxml')

    # ...
```


### Querying / Parsing the Page Contents

Once have access to the soup object, it allows us to query / find certain contents on the page. 

We use `find()` to find a single element (whichever element matches the criteria first), or `find_all()` to find multiple items that match the criteria. We specify which criteria by passing the name of the element as the first parameter. If we need to identify elements by their class, we can pass the class name as the default second parameter. Otherwise if we need to access elements by their identifiers, we pass a named parameter of "id" as the second parameter:

```py
# find syntax:
soup.find("ELEMENT_NAME")
soup.find("ELEMENT_NAME", "CLASS_NAME")
soup.find("ELEMENT_NAME", id="ID_NAME")
#> Tag

# find all syntax:
soup.find_all("ELEMENT_NAME")
soup.find_all("ELEMENT_NAME", "CLASS_NAME")
soup.find_all("ELEMENT_NAME", id="ID_NAME")
#> ResultsSet
```

The `find` method will return a `Tag` object, while the `find_all()` method will return a `ResultsSet` object (which is essentially a list of tags). Each tag has a `.text` property, as well as the ability to query / find its child elements.

In practice, which elements we search for depends entirely on the structure of the page in question. For example:

```py
# parse the HTML

# find all <span> elements that have a class of "title":
titles = soup.find_all("span", "title")
print(type(titles)) #> <class 'bs4.element.ResultSet'> (like a list)

tag = titles[5] # grab the sixth item, for example
print(tag) #> <span class="title">Romeo and Juliet</span>
print(tag.text) #> "Romeo and Juliet"
```

Example of querying child elements (`<span>` elements that exist inside of a parent `li` element):

```py
# find all <li> elements that have a class of "booklink":
booklinks = soup.find_all("li", "booklink")

books = []
for list_item in booklinks:
    try:
        title = list_item.find("span", "title").text #> "Shakespeare's Sonnets"
        author = list_item.find("span", "subtitle").text #> "William Shakespeare"
        downloads = list_item.find("span", "extra").text #> '830 downloads'
        downloads_count = int(downloads.replace(" downloads", "")) #> 830
        book = {"title": title, "author": author, "downloads": downloads_count}
        print(book)
        books.append(book)
    except Exception as err:
        print("OOPS", type(err), err, "SKIPPING...")

print(books[2]["title"]) #> Romeo and Juliet
```

It's easier to parse HTML once you know the document structure. Try using your browser's developer tools to examine the document structure of any web page. For example, in Google Chrome you can right-click on a webpage and select "Inspect".

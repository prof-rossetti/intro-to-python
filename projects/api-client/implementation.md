# "API Client" Project - Implementation

> See: [The "API Client" Project](README.md)

## Instructions

Here are some general suggestions and guidelines:

  1. Search the Internet for one or more APIs or open data sources you are interested in.
  2. Investigate your ability to write Python to request and process the data, and do something interesting and helpful with it. 
  3. Refactor / simplify your code into one or more custom functions, as applicable. Write unit tests and docstrings for your custom functions. 
  4. Consider providing a single cell at the bottom which captures user inputs as necessary, and invokes the function(s) to produce the desired outputs.

### Data Requirements

Your app should fetch data from one or more APIs, web pages, or other open datasets.

### Function Requirements

Simplify and organize your code, perhaps using custom functions, as appropriate. For example, perhaps all the data fetching logic can go inside a function which returns the data in a clean and easy to use format. Or perhaps all the data processing logic can go in a separate function that accepts the clean data as a parameter input. Or perhaps you may have formatter / helper functions that have a very specific, small role to play (e.g. formatting numbers as USD).

Check your function parameters. Ensure any variables needed by the function (except for constants like API Keys) are passed in as parameter inputs.

Your custom function(s) should ideally be documented using ["docstrings"](/notes/python/docstrings.md). 

Your custom function(s) should ideally be accompanied by one or more unit tests, using example data and simple assertions.

### Security Requirements

If your program requires sensitive information like secret passwords, API keys, or other credentials, those secret values should absolutely not be included in the source code.

If working in Colab, configure any API key(s) or other credentials using notebook secrets.

## Submission Instructions

Upload your completed notebook in .IPYNB format to Canvas.

## Evaluation

Project implementations will be evaluated according to the requirements set forth above, as summarized by the rubric below:

Category | Requirement | Weight
--- | --- | ---
Data Source Documentation | Provides links to the source data and/or API documentation, and instructions for how someone can obtain an API key, as necessary. | 10%
API Usage | Processes data from one or more APIs, web pages or other open data sources. | 20%
Function Usage | Performs data processing using one or more custom functions, with accompanying unit tests. | 15%
Uniqueness and Individuality | Exhibits creativity, and a unique set of functionality. | 20%
User Experience | Provides a simple, pleasant, and intuitive experience for the user, without "bugs" or errors. | 15%
Security | Excludes sensitive information and credentials from the source code, and protects user data, as necessary. | 20%

This rubric is tentative, and may be subject to slight adjustments during the grading process.

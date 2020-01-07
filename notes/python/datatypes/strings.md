# Strings

Reference: https://docs.python.org/3/library/string.html.

Strings represent textual information, including words and alpha-numeric characters.

```python
"Hello World"
"username123"
```

Don't be confused if you see multi-line strings:

```python
str = """
Some
Multi-line
String
"""

str #> '\nSome\nMulti-line\nString\n'

print(str)
#>
#> Some
#> Multi-line
#> String
#>
```

Example string functions:

```python
# string concatenation
"Hello" + " " + "World" #> "Hello World"

# string formatting
"{0} {1}".format("Hello", "World") #> "Hello World"
"My Message is: {0}".format("Hello World") #> "My message is: Hello World"

# string interpolation (note the preceding `f`)
greeting = "Hello"
audience = "World"
f"My message is: {greeting} {audience}" #> "My message is: Hello World"

# string manipulation
"hello world".upper() #> "HELLO WORLD"
"Hello World".lower() #> "hello world"
"hello world".title() #> "Hello World"
"   Hello World   ".strip() #> "Hello World"
"Hello World".replace("Hello", "Goodbye") #> "Goodbye World"
```

Strings also support equality, inclusion, and matching operators:

```python
"Hello World" == "Hello World" #> True
"Hello World" == "hello world" #> False

"Hello" in "Hello World" #> True
"hello" in "Hello World" #> False

"Hello World".count("l") #> 3
```

Strings are iterable objects comprised of multiple characters. Once you have learned about lists, you can perform additional list-related operations:

```python
"Hello World"[0] #> "H"
"Hello World"[6] #> "W"
"Hello World"[-1] #> "d"
"Hello World"[-3] #> "r"

for character in "Hello World":
    print(character)
#>
#> H
#> e
#> l
#> l
#> o
#>
#> W
#> o
#> r
#> l
#> d

"Hello World".split() #> ["Hello", "World"]
"My Title - My Subtitle".split(" - ") #> ['My Title', 'My Subtitle']
"a, b, c, d".split(", ") #> ['a', 'b', 'c', 'd']

str = """
Some
Multi-line
String
"""
str.strip().split("\n") #> ['Some', 'Multi-line', 'String']
```

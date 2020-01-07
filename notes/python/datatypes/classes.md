# Classes

Reference:

  + https://docs.python.org/3/tutorial/classes.html
  + https://docs.python.org/3/tutorial/classes.html#class-objects
  + https://www.tutorialspoint.com/python/python_classes_objects.htm

A **Class** is a representation of one or more objects which share the same or similar properties. Each class is like its own custom data type with properties defined by the developer.

In Python, class definition requires a specific function called `__init__()` to initialize, or create a new member of the object class.

## Definition

To setup this example, create a new directory on your Desktop called `class-time` or something. Inside it, create a new file called `baseball_team.py` and place inside the following contents:

```python
class BaseballTeam():
  """
  bt = BaseballTeam({"city": "Little Town", "name": "Tots", "league":"little", "players": ["JJ", "Zhang", "Margaret", "Ryan", "Joey"]})
  """ # optional docstring

  def __init__(self, params):
    self.city = params["city"]
    self.name = params["name"]
    self.league = params["league"]
    self.players = params["players"]

  def full_name(self):
    return self.city + " " + self.name

  #
  # ... probably more instance methods down here ...
  #

```

## Initialization

After defining an object class, create a new member of that object class. This is called "instantiating", or "initializing", or creating an "instance" of the object class.

Normally we would reference the class from another file by importing it (e.g. `from baseball_team import BaseballTeam`), but for example purposes, place the following contents at the bottom of the `baseball_team.py` script:

```python
attributes = {
    "city": "New York",
    "name": "Yankees",
    "league": "major",
    "players": ["Jeter", "Mariano", "Mantle", "Babe"]
}
type(attributes) #> <class 'dict'>

bt = BaseballTeam(attributes)
type(bt) #> __main__.BaseballTeam

bt.name #> 'Yankees'

bt.city #> 'New York'

bt.players #> ['Jeter', 'Mariano', 'Mantle', 'Babe']

bt.full_name() #> 'New York Yankees'
```

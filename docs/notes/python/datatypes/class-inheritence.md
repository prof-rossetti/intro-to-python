
# Class Inheritance

> Prerequisite: [Classes](classes.md)

Reference: https://docs.python.org/3.1/tutorial/classes.html#inheritance

It is possible for a class to "inherit" its properties and functionality from its "parent" class while at the same time retaining its own specific characteristics.

## Parent Class

```python

class Team():
    # each class has this specific "init" function 
    #... which allows us to pass attribute values when initializing a new member of that class
    def __init__(self, city, name):
        self.city = city
        self.name = name
 
    # each class has this specific "representation" function 
    #... which allows us to specify what should be displayed when we print this object
    def __repr__(self):
        return f"<Team '{self.name}'>"
 
    # FYI: @property is a decorator that allows us to reference this method
    # ... without trailing parentheses (like team.full_name instead of team.full_name())
    # ... basically just a stylistic choice on our part
    # ... use properties for nouns / calculated attributes
    # ... otherwise just use a normal method
    @property
    def full_name(self):
        return self.city + " " + self.name
 
    # this is a normal instance method. 
    # NOTE: all instance methods within a class take "self" as their first required parameter
    # ... which references the instance itself
    def advertise(self):
        print("COME TO", self.city.upper(), "TO SEE OUR GAMES!")

```

Parent Class Initialization:

```python
yanks = Team("New York", "Yankees")
print("-----------")
print(type(yanks))
print(yanks)
print(yanks.full_name)
yanks.advertise()

nats = Team(city="Washington", name="Nationals")
print("-----------")
print(type(nats))
print(nats)
print(nats.full_name)
nats.advertise()

mets = Team(name="Mets", city="New York")
print("-----------")
print(type(mets))
print(mets)
print(mets.full_name)
mets.advertise()
```

## Child Class

Child Class Definition:

```py

class BaseballTeam(Team):

    def __init__(self, city, name, short_stop=None, closing_pitcher=None):

        # initialize the parent class with any of its params
        # `super` references the parent class, so this is equivalent to: Team.__init__(self, city=city, name=name)
        super().__init__(city=city, name=name) 

        # then initialize some baseball specific params (like these players for example):
        self.short_stop = short_stop 
        self.closing_pitcher = closing_pitcher 
        # etc.

    # note: the full_name property is inherited from the parent class, and we can omit it here!

    # note: here we are overriding a method from the parent class
    def advertise(self):
        print("COME TO", self.city.upper(), "TO SEE OUR BASEBALL GAMES, INCLUDING:")
        print("...", self.short_stop)
        print("...", self.closing_pitcher)

    # note: here is some baseball-specific functionality
    def warm_up_bullpen(self):
        print("NOW WARMING UP:", self.closing_pitcher)
 

```

Child Class Initialization:

```py
bt = BaseballTeam(name="Yanks", city="New York", short_stop="Derek Jeter", 
                  closing_pitcher="Mariano Rivera")

print("-----------")
print(type(bt))
print(bt)
print(bt.city) # this property is inherited from the parent class!
print(bt.name) # this property is inherited from the parent class!
print(bt.full_name) # this property is inherited from the parent class!
print("-----------")
bt.advertise() # this method is overridden in the child class
print("-----------")
bt.warm_up_bullpen() # this is a method specific to the child class only
```


In this inheritance example, the reason why an instance of the `BaseballTeam` class has the `full_name` property is because that property was defined in the parent class `Team`.

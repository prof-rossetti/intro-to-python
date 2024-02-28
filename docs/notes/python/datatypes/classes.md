# Classes

Reference:

  + https://docs.python.org/3/tutorial/classes.html
  + https://docs.python.org/3/tutorial/classes.html#class-objects
  + https://www.tutorialspoint.com/python/python_classes_objects.htm
  + https://realpython.com/instance-class-and-static-methods-demystified/


A **Class** is a representation of one or more objects which share the same or similar properties. Each class is like its own custom data type with properties defined by the developer.

In Python, class definition requires a specific function called `__init__()` to initialize, or create a new member of the object class.

## Definition

Like a function, we first define the object class, including its parameters, properties (i.e. attributes), and methods (i.e. capabilities):

```py

class Polo():
    def __init__(self, color, size, price=99.00, style=None):
        self.color = color
        self.size = size
        self.price = price
        self.style = style
    
    def fold(self):
        print("FOLDING THE " + self.color.upper() + " POLO!")
    
    def transfer_to(self, store_name):
        print(f"TRANSFERING THE {self.color.upper()} POLO TO STORE: '{store_name.upper()}'")

```

## Initialization

After defining an object class, create a new member of that object class. This is called "instantiating", or "initializing", or creating an "instance" of the object class.


```python
polo_1 = Polo(color="Blue", size="Large", price=4.99) 
print("-----------")
print(type(polo_1)) #> <class '__main__.Polo'>
print(polo_1.color) #> Blue
print(polo_1.price) #> 4.99
polo_1.fold() #> FOLDING THE BLUE POLO!

polo_2 = Polo(color="Yellow", size="Small")
print("-----------")
print(type(polo_2)) #> <class '__main__.Polo'>
print(polo_2.color) #> Yellow
print(polo_2.price) #> 99.0
polo_2.fold() #> FOLDING THE YELLOW POLO!

polo_3 = Polo(color="Red", size="Large", price=65.00, style="Slim")
print("-----------") 
print(type(polo_3)) #> <class '__main__.Polo'>
print(polo_2.color) #> Red
print(polo_2.price) #> 99.0
polo_3.fold() #> FOLDING THE RED POLO!
polo_3.transfer_to("Boston, MA") #> TRANSFERING THE RED POLO TO STORE: 'BOSTON, MA'
```

## [Inheritence](class-inheritence.md)

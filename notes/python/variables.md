# Variables

Use a variable to store some value in the program's temporary memory. Declare a variable using a name and assign its value by using a single equal sign (`=`) followed by the value. Any object can be stored in a variable:

```python
my_bool = True
my_int = 10
my_float = 0.45
my_str = "My Message"
my_list = [1,2,3,4]
my_dict = {"a":1, "b":2, "c":3}
```

If you try to reference a variable that has not yet been defined, you will see an error like `NameError: name 'my_var' is not defined`.

Don't be surprised if a variable's value changes. It is common to overwrite a variable's value by re-assigning it or manipulating it in some way:

```python
a = 1
print(a) #> 1

a = 2
print(a) #> 2

a = a+1
print(a) #> 3
```


# "Modules and Imports" Exercise - Further Exploration

> See: [exercise setup and description](README.md)

## Modules in Subdirectories

Make a subdirectory of the "modules-overview" directory called "things" and place inside a file called "robot.py", with the following contents:

``` python
# this is the "modules-overview/things/robot.py" file...

def robot_message():
    print("HELLO I'M A ROBOT")
```

If a Python module is located in a subdirectory like this, we can reference it using dot notation, like `[directory_name].[file_name]`. For example, add the following contents to the "my_script.py" file:

``` python
# this is the "modules-overview/my_script.py" file...

# ...

from things.robot import robot_message

robot_message()
```

Run the script again to see the new imports working:

```sh
python my_script.py
```

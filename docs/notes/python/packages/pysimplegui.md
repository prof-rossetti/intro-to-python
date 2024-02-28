# The `PySimpleGUI` Package

> Thanks to @windy030 and @oaw6 for surfacing the capabilities of this package

The `PySimpleGUI` package provides a graphical user interface (GUI) for your applications.

## Demo

![](https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/ex1-tkinter.jpg)

## Reference

  + https://pypi.org/project/PySimpleGUI/
  + https://github.com/PySimpleGUI/PySimpleGUI
  + https://github.com/PySimpleGUI/PySimpleGUI/blob/master/PySimpleGUI.py
  + https://pysimplegui.readthedocs.io/en/latest/tutorial/
  + https://pysimplegui.readthedocs.io/en/latest/cookbook/
  + https://pysimplegui.readthedocs.io/en/latest/#high-level-api-calls-popups
  + https://pysimplegui.readthedocs.io/en/latest/#listbox-element
  + https://pysimplegui.readthedocs.io/en/latest/#button-element
  + https://pysimplegui.readthedocs.io/en/latest/#input-elements
  + etc...


## Installation

Install the `PySimpleGUI` package:

```py
pip install PySimpleGUI
```

## Usage

Usage examples (adapted from the official documentation):

```py
import PySimpleGUI as sg

sg.Popup("Hello From PySimpleGUI!", "This is the shortest GUI program ever!")
```

```py
import PySimpleGUI as sg

layout = [
    [sg.Text("Enter your name"), sg.InputText()],
    [sg.OK()]
]

window = sg.Window("My first GUI").Layout(layout)

button, values = window.Read()

#print(type(values)) #> dict
#print(values) #> {0: 'Polly Professor'}
name = values[0] #> Polly Professor
print("NAME:", name)
```


```py
import PySimpleGUI as sg

sg.ChangeLookAndFeel("GreenTan")

column1 = [[sg.Text("Column 1", background_color="#d3dfda", justification="center", size=(10, 1))],
           [sg.Spin(values=("Spin Box 1", "2", "3"), initial_value="Spin Box 1")],
           [sg.Spin(values=("Spin Box 1", "2", "3"), initial_value="Spin Box 2")],
           [sg.Spin(values=("Spin Box 1", "2", "3"), initial_value="Spin Box 3")]]
layout = [
    [sg.Text("All graphic widgets in one window!", size=(30, 1), font=("Helvetica", 25))],
    [sg.Text("Here is some text.... and a place to enter text")],
    [sg.InputText("This is my text")],
    [sg.Checkbox("My first checkbox!"), sg.Checkbox("My second checkbox!", default=True)],
    [sg.Radio("My first Radio!     ", "RADIO1", default=True), sg.Radio("My second Radio!", "RADIO1")],
    [sg.Multiline(default_text="This is the default Text should you decide not to type anything", size=(35, 3)),
     sg.Multiline(default_text="A second multi-line", size=(35, 3))],
    [sg.InputCombo(("Combobox 1", "Combobox 2"), size=(20, 3)),
     sg.Slider(range=(1, 100), orientation="h", size=(34, 20), default_value=85)],
    [sg.Listbox(values=("Listbox 1", "Listbox 2", "Listbox 3"), size=(30, 3)),
     sg.Slider(range=(1, 100), orientation="v", size=(5, 20), default_value=25),
     sg.Slider(range=(1, 100), orientation="v", size=(5, 20), default_value=75),
     sg.Slider(range=(1, 100), orientation="v", size=(5, 20), default_value=10),
     sg.Column(column1, background_color="#d3dfda")],
    [sg.Text("_"  * 80)],
    [sg.Text("Choose A Folder", size=(35, 1))],
    [sg.Text("Your Folder", size=(15, 1), auto_size_text=False, justification="right"),
     sg.InputText("Default Folder"), sg.FolderBrowse()],
    [sg.Submit(), sg.Cancel()]
]

window = sg.Window("Everything bagel", default_element_size=(40, 1)).Layout(layout)
button, values = window.Read()
sg.Popup(button, values)
```

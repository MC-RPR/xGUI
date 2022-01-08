# xGUI

xGUI (pronounced "ex-gooey" or "ex-gee-you-eye") is a wrapper for the Tkinter package built in to most Python distributations. It allows you to create windows in XML, then load them and use them in your programs. This makes it a lot easier to visualize your programs, and helps simplify the learning curve for the Tk library.

## Features

- [ ] Full support for ttk (Themed tk) widgets.
- [ ] Easy configuration both globally (through code classes) and specifically (XML `<config>`).
- [ ] Adjust each individual widget with all supported options
- [ ] Use a templating engine (like Jinja2!) for simpler and more efficient windows
- [ ] Supporting both pack and grid geometry managers
- [ ] Extremely extensible, OOB code
- [ ] Best practices and type hinting (yay readable code!)

## Installation

You can install xGUI through multiple different methods.

|Type|Command|
|-|-|
|PIP|`python -m pip install -U xgui`|
|Source (may have bugs!)|`python -m pip install -U git+https://github.com/MC-RPR/xGUI.git@main`|
|Poetry|`poetry add xgui`|

## Get Started

Create screen.xml. This is where you will design your new app.

```xml
<root title="My New App">
    <Frame>
        <Label>Hello, world!</Label>
        <Button>Click me</Button>
    </Frame>
</root>
```

Now, create you main Python script. This can be named anything, but in this quick guide we'll call it app.py.

```python
import xgui

app = xgui.load("screen.xml")
app.mainloop()
```

Congrats! You just created your first xGUI project!


# Gooey - Simplify GUI Creation for CLI Tools

**Gooey** is a Python library that transforms command-line applications into user-friendly GUIs, making it perfect for adding graphical interfaces to scripts without complex GUI development.

## Overview

- **Description**: Gooey is a decorator-based library that wraps around Python’s `argparse` library, transforming command-line applications into interactive GUIs. With Gooey, you can add a graphical interface with forms, checkboxes, dropdowns, and file choosers based on the parameters in `argparse`.
  
## Features

- **Automatic GUI Creation**: Gooey generates a GUI that reflects all `argparse` options with a single decorator.
- **Customizable Components**: Supports dropdowns, checkboxes, file choosers, sliders, and color pickers.
- **Easy Setup**: Quick to integrate with existing CLI programs.
- **Cross-Platform**: Works on Windows, Mac, and Linux.
- **Appearance Customization**: Customize the window title, icon, layout, and theme.

## Use Cases

- **Ideal for**: Quickly adding a GUI to Python scripts with command-line options.
- **Limitations**: Best suited for `argparse`-compatible apps and limited customizability compared to frameworks like Tkinter or PyQt.

## Installation

```bash
pip install Gooey
```

## Documentation

- [Official Documentation](https://gooey.readthedocs.io/)
- [GitHub Repository](https://github.com/chriskiehl/Gooey)

## Basic Example

Here’s a minimal example demonstrating how Gooey turns a CLI tool into a GUI by decorating the main function:

```python
from gooey import Gooey, GooeyParser

@Gooey(program_name="Example App", description="A simple GUI for a CLI script")
def main():
    parser = GooeyParser(description="Sample Gooey Application")
    parser.add_argument('--name', type=str, help='Enter your name')
    parser.add_argument('--age', type=int, help='Enter your age')
    parser.add_argument('--gender', choices=['Male', 'Female', 'Other'], help='Select your gender')
    args = parser.parse_args()
    
    print(f"Name: {args.name}, Age: {args.age}, Gender: {args.gender}")

if __name__ == "__main__":
    main()
```

Running this script with Gooey will generate a GUI, making the tool accessible to non-technical users.

---

## Alternatives to Gooey

If you’re exploring other options for creating GUIs for command-line tools, here are some popular frameworks:

### 1. PySimpleGUI
   - **Description**: A simple, cross-platform GUI framework that wraps around Tkinter, Qt, or WxPython.
   - **Documentation**: [PySimpleGUI Docs](https://pysimplegui.readthedocs.io/)

   ```bash
   pip install pysimplegui
   ```

### 2. Tkinter
   - **Description**: The standard GUI library for Python, widely used for simple applications.
   - **Documentation**: [Tkinter Docs](https://docs.python.org/3/library/tk.html)

   ```python
   # Tkinter is included in Python's standard library.
   ```

### 3. PyQt / PySide
   - **Description**: Bindings for the Qt library, offering advanced widgets and professional UI capabilities.
   - **Documentation**: [PyQt](https://riverbankcomputing.com/software/pyqt/intro) / [PySide](https://doc.qt.io/qtforpython/)

   ```bash
   pip install pyqt5  # or
   pip install pyside2
   ```

### 4. Kivy
   - **Description**: A modern, cross-platform framework designed for touch applications.
   - **Documentation**: [Kivy Docs](https://kivy.org/doc/stable/)

   ```bash
   pip install kivy
   ```

### 5. Dear PyGui
   - **Description**: A high-performance GUI library using Dear ImGui, suited for real-time visualizations.
   - **Documentation**: [Dear PyGui Docs](https://dearpygui.readthedocs.io/)

   ```bash
   pip install dearpygui
   ```

### 6. Toga
   - **Description**: A native GUI toolkit for Python that is part of the BeeWare project.
   - **Documentation**: [Toga Docs](https://toga.readthedocs.io/)

   ```bash
   pip install toga
   ```

Each framework has unique strengths, so the best choice depends on your project needs—whether it's customizability, platform compatibility, or ease of setup.
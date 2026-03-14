# tomwidgets

Toolkit for developing graphical interfaces

# Pypi

[tomwidgets · PyPI](https://pypi.org/project/tomwidgets/)

# Source

[ThomasStudio/tomwidgets: Toolkit for developing graphical interfaces](https://github.com/ThomasStudio/tomwidgets)

# Usage:

## Pip install

* pip install tomwidgets
* create a new python file to use it. Example:
  * Tool.py
* ```
  from tomwidgets import ToolWin

  if __name__ == "__main__":
      ToolWin().show()

  ```

## Source code

* Download code
* run main.py


## tools.ini

* ToolWin() will automatically generate a tools.ini
* ToolWin has a parameter toolsFile, which can specify tools.ini
  * For example: use temp\\\tools.ini
  * ```
    from tomwidgets import ToolWin

    if __name__ == "__main__":
        ToolWin(toolsFile="temp\\tools.ini").show()
    ```

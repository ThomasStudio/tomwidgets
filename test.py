import tkinter as tk

import tomwidgets.examples
from tomwidgets import ModuleUtil
from tomwidgets import Theme
from tomwidgets import Tk, WrapBox, Button


def test():
    Theme.init()

    root = Tk()
    root.geometry("600x380")
    root.title("tomwidgets Examples Test")

    box = WrapBox(root)
    box.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    btnInfo = ModuleUtil.getCallable(tomwidgets.examples)

    for name, attr in btnInfo.items():
        btn = Button(box, text=name.split("_example")[0], command=attr)
        box.addWidget(btn)

    root.mainloop()


if __name__ == "__main__":
    test()

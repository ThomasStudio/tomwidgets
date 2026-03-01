from typing import Optional
from tkinter import TclError


from .basic.Tk import Tk
from .basic.Toplevel import Toplevel
from .Theme import Theme, ColorTheme


class WinManager:
    def __init__(self):
        self._root: Tk = None

    def createWin(self, parent=None, mode: str = None, theme: str = None) -> Tk | Toplevel:
        Theme.init(mode, theme)

        if not self._has_root_window():
            print(f"create root window")
            window = self._create_root_window()
        else:
            print(f"create child window with parent {parent}")
            window = self._create_child_window(parent)

        return window

    def _has_root_window(self) -> bool:
        if self._root is None:
            return False

        try:
            return self._root.winfo_exists()
        except TclError:
            self._root = None
            return False

    def _create_root_window(self) -> Tk:
        self._root = Tk()

        return self._root

    def _create_child_window(self, parent=None) -> Toplevel:
        parent = self._root if parent is None else parent

        child = Toplevel(parent)
        return child

    def getRoot(self) -> Optional[Tk]:
        return self._root if self._has_root_window() else None


WinMgr = WinManager()


def test():
    from .basic.Button import Button
    root = WinMgr.createWin()

    def showWin(event=None):
        win = WinMgr.createWin()
        win.mainloop()

    btn = Button(root, text="Click me", command=showWin)
    btn.pack()

    root.mainloop()

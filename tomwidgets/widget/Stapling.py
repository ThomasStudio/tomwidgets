from functools import partial

from .basic.Toplevel import Toplevel
from .basic.Tk import Tk

xStapling = None
yStapling = None

TopLeft = "\uF5A1"
TopRight = "\uF5A2"
BottomLeft = "\uF5A3"
BottomRight = "\uF5A4"
# TopLeft = "↖"       # (U+2196)
# TopRight = "↗"      # (U+2197)
# BottomLeft = "↙"    # (U+2199)
# BottomRight = "↘"   # (U+2198)


class Stapling:
    def __init__(self, win: Toplevel | Tk, **kwargs):
        self.win = win

    def getStaplingMenu(self) -> list:
        f = self.stapling

        cmds = [
            (BottomRight, partial(f, '-0', '-0')),
            (TopRight, partial(f, '-0', '+0')),
            (BottomLeft, partial(f, '+0', '-0')),
            (TopLeft, partial(f, '+0', '+0')),
        ]

        return cmds

    def stapling(self, xPos: str, yPos: str):
        win = self.win
        if win is None:
            return

        global xStapling, yStapling
        xStapling, yStapling = xPos, yPos

        if yPos == '-0':
            yPos = '-40'

        yOffset = 40

        x, y, w, h, sw, sh = win.winfo_rootx(), win.winfo_rooty(), win.winfo_width(
        ), win.winfo_height(), win.winfo_screenwidth(), win.winfo_screenheight()

        if xPos.lower() == 'l':
            xPos = '+0'
        elif xPos.lower() == 'r':
            xPos = f'+{sw - x}'
        elif xPos.lower() == 'm':
            xPos = f'+{int(sw / 2 - w / 2)}'

        if yPos.lower() == 't':
            yPos = '+0'
        elif yPos.lower() == 'b':
            yPos = f'{sh - h}'
        elif yPos.lower() == 'm':
            yPos = f'+{int(sh / 2 - h / 2)}'

        win.wm_geometry(f'{xPos}{yPos}')

    def reStapling(self):
        win = self.win
        if win is None:
            return

        global xStapling, yStapling

        if not xStapling or not yStapling:
            return

        win.update()
        self.stapling(xStapling, yStapling)


def test():
    from .basic.Tk import Tk
    from .PopMenu import PopMenu

    root = Tk()
    root.geometry("300x200")
    root.title("Stapling Test")

    stapling = Stapling(root)

    menu_data = stapling.getStaplingMenu()

    popup_menu = PopMenu(root, menu_data)

    def show_menu(event):
        popup_menu.show()

    root.bind("<Button-3>", show_menu)  # Right-click to show menu

    root.mainloop()


if __name__ == "__main__":
    test()

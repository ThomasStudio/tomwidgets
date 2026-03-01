import tkinter as tk
from .Theme import Theme, CTkOptionMenu


class PopMenu(tk.Menu):
    def __init__(self, parent, cmds: list, font='Arial 15', tearoff=0, **kw) -> None:
        bg_color = Theme.get(CTkOptionMenu.fg_color)
        text_color = Theme.get(CTkOptionMenu.text_color)

        super().__init__(parent, font=font, bg=bg_color,
                         fg=text_color, tearoff=tearoff, **kw)
        self.addCmds(cmds)

    def addCmds(self, cmds: list):
        """Add commands to the menu"""
        for cmd in cmds:
            if cmd is None:
                self.add_separator()
            elif isinstance(cmd[1], list):
                # submenu
                submenu = PopMenu(self, cmd[1])
                self.add_cascade(label=cmd[0], menu=submenu)
            else:
                # normal command
                self.add_command(label=cmd[0], command=cmd[1])

    def show(self):
        # get current mouse position
        x = self.winfo_pointerx()
        y = self.winfo_pointery()
        self.tk_popup(x, y)

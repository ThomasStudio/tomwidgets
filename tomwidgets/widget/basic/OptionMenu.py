import customtkinter as ctk
from .BaseWidget import BaseWidget


class OptionMenu(ctk.CTkOptionMenu, BaseWidget):
    def __init__(self, master, resizing=True, **kw):
        if "width" not in kw:
            kw["width"] = 0

        kw["dynamic_resizing"] = resizing

        super().__init__(master, **kw)
        BaseWidget.__init__(self)

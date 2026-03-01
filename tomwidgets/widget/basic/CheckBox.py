import customtkinter as ctk
from .BaseWidget import BaseWidget


class CheckBox(ctk.CTkCheckBox, BaseWidget):
    def __init__(self, master, **kw):
        super().__init__(master, width=20, height=10, **kw)
        BaseWidget.__init__(self)

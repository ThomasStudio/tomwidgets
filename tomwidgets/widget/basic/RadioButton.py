import customtkinter as ctk

from .BaseWidget import BaseWidget


class RadioButton(ctk.CTkRadioButton, BaseWidget):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        BaseWidget.__init__(self)

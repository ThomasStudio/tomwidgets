import customtkinter as ctk
from .BaseWidget import BaseWidget


class ComboBox(ctk.CTkComboBox, BaseWidget):
    def __init__(self, master, **kw):
        if 'values' not in kw:
            kw['values'] = []
        super().__init__(master, **kw)
        BaseWidget.__init__(self)

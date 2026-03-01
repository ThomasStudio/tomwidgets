import customtkinter as ctk
from .BaseWidget import BaseWidget

class Label(ctk.CTkLabel, BaseWidget):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        BaseWidget.__init__(self)

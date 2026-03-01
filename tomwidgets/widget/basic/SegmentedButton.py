import customtkinter as ctk
from .BaseWidget import BaseWidget


class SegmentedButton(ctk.CTkSegmentedButton, BaseWidget):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        BaseWidget.__init__(self)

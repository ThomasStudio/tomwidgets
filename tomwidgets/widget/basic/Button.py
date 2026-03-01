import customtkinter as ctk

from .BaseWidget import BaseWidget


class Button(ctk.CTkButton, BaseWidget):
    def __init__(self, master, **kw):
        if 'width' not in kw:
            kw['width'] = 5
        if 'height' not in kw:
            kw['height'] = 5
        super().__init__(master, **kw)
        BaseWidget.__init__(self)

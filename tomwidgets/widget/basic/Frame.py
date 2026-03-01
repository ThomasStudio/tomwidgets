import customtkinter as ctk
from .EventHandler import EventHandler
from .Dragging import Dragging
from .BaseWidget import BaseWidget


class Frame(ctk.CTkFrame, BaseWidget, EventHandler, Dragging):
    def __init__(self, master, **kw):
        if 'height' not in kw:
            kw['height'] = 0
        if 'width' not in kw:
            kw['width'] = 0

        super().__init__(master, **kw)
        BaseWidget.__init__(self)
        EventHandler.__init__(self)
        Dragging.__init__(self)

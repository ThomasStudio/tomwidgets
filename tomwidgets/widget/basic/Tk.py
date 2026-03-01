from typing import Optional, Tuple, Union
import customtkinter as ctk


class Tk(ctk.CTk):
    def __init__(self, fg_color: Optional[Union[str, Tuple[str, str]]] = None, **kw):
        super().__init__(fg_color=fg_color, **kw)

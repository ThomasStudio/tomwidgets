from typing import Optional, Tuple, Union
import customtkinter as ctk


class Toplevel(ctk.CTkToplevel):
    def __init__(self, *args, fg_color: Optional[Union[str, Tuple[str, str]]] = None, **kwargs):
        super().__init__(*args, fg_color=fg_color, **kwargs)

        x = self.winfo_pointerx()
        y = self.winfo_pointery()
        self.geometry(f"+{x}+{y}")

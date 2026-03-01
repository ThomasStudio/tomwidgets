import customtkinter as ctk


class InputDialog(ctk.CTkInputDialog):
    def __init__(self, **kw):
        super().__init__(**kw)

        x = self.winfo_pointerx()
        y = self.winfo_pointery()
        self.geometry(f"+{x}+{y}")

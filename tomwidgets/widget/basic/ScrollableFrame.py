import customtkinter as ctk

from .BaseWidget import BaseWidget


class ScrollableFrame(ctk.CTkScrollableFrame, BaseWidget):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        BaseWidget.__init__(self)


def test():
    root = ctk.CTk()
    frame = ScrollableFrame(root)
    frame.pack()

    for i in range(20):
        btn = ctk.CTkButton(frame, text=f"button {i}")
        btn.pack()

    root.mainloop()

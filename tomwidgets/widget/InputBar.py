import tkinter as tk
from tkinter import StringVar

from .basic.Frame import Frame
from .basic.Entry import Entry
from .basic.Label import Label


class InputBar(Frame):
    def __init__(self, parent, title: str = "input:", default: str = "", **kwargs):
        super().__init__(parent, **kwargs)
        self.eventName = "<<InputEnter>>"

        self.title = title
        self.default = default

        self.initUi()

    def initUi(self):
        self.addTitleLabel()
        self.addInput()

    def addTitleLabel(self):
        self.titleLabel = Label(self, text=self.title)
        self.titleLabel.pack(side=tk.LEFT, padx=[0, 5])

    def addInput(self):
        self.value = StringVar(master=self, value=self.default)
        self.input = Entry(self, textvariable=self.value)
        self.input.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.input.bind(sequence='<Return>', command=self.onEnter, add=True)

    def configInput(self, **kwargs):
        self.input.configure(**kwargs)

    def configLabel(self, **kwargs):
        self.titleLabel.configure(**kwargs)

    def getValue(self):
        return self.value.get()

    def setValue(self, value: str):
        self.value.set(value)

    def getTitle(self):
        return self.title

    def setTitle(self, title: str):
        self.title = title
        self.configLabel(text=self.title)

    def bindReturn(self, func):
        self.input.bind(sequence='<Return>', command=func, add=True)

    def onEnter(self, event=None):
        self.generateEvent()

    def clear(self) -> None:
        """Clear the entry field."""
        self.setValue("")

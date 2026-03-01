from functools import partial
from ..widget.BaseWin import BaseWin
from ..widget.basic.Tabview import Tabview
from ..widget.DictView import DictView
from ..model.Emoji import Emoji
from ..model.Segoe import Segoe
from ..util.ClassUtil import ClassUtil
import tkinter as tk


class IconTool(BaseWin):
    def __init__(self, master=None, title="Icon Tool", showTitleBar=True, showFolderBar=False, asWin=True, **kwargs):
        super().__init__(master=master, title=title, showTitleBar=showTitleBar,
                         showFolderBar=showFolderBar, asWin=asWin, **kwargs)

        # Create the UI components
        self.createTabview()

    def createTabview(self):
        # Create tabview with two tabs
        self.tabView = Tabview(self.contentFrame)
        self.tabView.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

    def createUi(self):
        # Create TextBars for each tab
        for name, data in [
            ("Segoe", ClassUtil.getValues(Segoe)),
            ("Emoji.Position", ClassUtil.getValues(Emoji.Position)),
            ("Emoji.Flat", ClassUtil.getValues(Emoji.Flat)),
            ("Emoji", ClassUtil.getValues(Emoji)),
        ]:
            self.createTab(name, data)

    def createTab(self, tabName: str, data: dict):
        tab = self.tabView.add(tabName)
        view = DictView(tab, title=tabName, showTitleBar=True,
                        keyColor="white", valueColor="gold", valueSize=30,
                        splitChar=" ", lineChar="  ")
        view.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        self.after(100, partial(view.setDictionary, data))

    def show(self):
        self.after(100, self.createUi)
        super().show()

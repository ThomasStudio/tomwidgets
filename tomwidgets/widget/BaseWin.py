import tkinter as tk
from functools import partial

from .basic.Frame import Frame

from .Settings import Settings
from .TitleBar import TitleBar
from .Theme import Theme, Mode, ColorTheme

SettingsFile = 'settings.ini'


class BaseWin(Frame, Settings):

    def __init__(self, master=None, title="Base Win", showTitleBar=True, showFolderBar=False, asWin=True, settingsFile: str = SettingsFile, **kwargs):
        """
        A base window class with TitleBar and window management controls.
        if asWin == False:
            it works as a Frame
        if asWin == True:
            it works as a Tk or Toplevel window

        Args:
            master: The parent widget
            title: The window title
            showTitleBar: Whether to show the TitleBar initially
            **kwargs: Additional arguments for Frame
        """
        self.parent = master
        self.asWin = asWin
        self.title = title
        self.titleBarVisible = showTitleBar
        self.folderBarVisible = showFolderBar
        self.isMaximized = False
        self.isMinimized = False
        self.isOnTop = False
        self.systemTitleVisible = True

        # Theme configuration
        self.currentMode = Mode.Dark
        self.currentColorTheme = ColorTheme.Gold

        # Initialize the base frame
        super().__init__(self.getParent(), **kwargs)
        Settings.__init__(self, settingsFile, self.parent)

        self.grid_columnconfigure(0, weight=1)

        self.currentRow = 0

        # Create TitleBar
        self.createTitleBar(title)
        bar = self.folderBar = self.createFolderBar(self)
        bar.grid(row=self.useRow(), column=0, sticky="ew")

        self.createFrames()

        # Apply initial TitleBar visibility
        self.updateTitleBarVisibility()
        self.updateFolderBarVisibility()

        self.bindWin()

    def createWin(self):
        from .WinMgr import WinMgr
        from .Stapling import Stapling

        self.win = WinMgr.createWin(self.parent)
        self.win.title(self.title)

        self.stapling = Stapling(self.win)

        self.parent = self.win

        return self.win

    def getParent(self):
        return self.createWin() if self.asWin else self.parent

    def bindWin(self):
        if self.asWin:
            self.pack(fill=tk.BOTH, expand=True)

    def getCmds(self):
        from .ConfigWin import openConfigWin

        """ override it to show custom menu commands """
        menu = [
            ("Theme", [
                *[(k, partial(self.setMode, v)) for k, v in Theme.modeList()],
                None,
                *[(k, partial(self.setMode, None, v))
                  for k, v in Theme.colorThemeList()],
            ]),
            ("Window", [
                ("Maximize", self.toggleMaximize),
                ("Minimize", self.toggleMinimize),
                ("Always on Top", self.toggleOnTop),
                ("System Title", self.toggleSystemTitle),
                ("Hide all", self.titleBar.hideAllWidgets),
                ("Show all", self.titleBar.showAllWidgets),
                ("Toggle FolderBar", self.toggleFolderBar),
            ])
        ]

        if self.asWin:
            menu = [
                ("Stapling", self.stapling.getStaplingMenu()),
                *menu,
                ("Folder Bar", [
                    ("Show/Hide", self.toggleFolderBar),
                ]),
                ("Config", [
                    ("settings.ini", lambda: openConfigWin(
                        self.win, title="settings.ini", configFile=self.settingsFile)),
                ]),
                ("Exit", self.onClose),
            ]

        return menu

    def useRow(self):
        self.currentRow += 1
        return self.currentRow - 1

    def createFrames(self):
        # create top and bottom frame
        self.topFrame = Frame(self)
        self.topFrame.grid(row=self.useRow(), column=0, sticky="ew",)

        # Create content area
        contentRow = self.useRow()
        self.contentFrame = Frame(self)
        self.contentFrame.grid(
            # CHANGED to sticky="nsew" for full expansion
            row=contentRow, column=0, sticky="nsew")

        self.grid_rowconfigure(contentRow, weight=100)  # bottomFrame row

        self.bottomFrame = Frame(self)
        self.bottomFrame.grid(row=self.useRow(), column=0, sticky="ew")

        for f in [self.topFrame, self.contentFrame, self.bottomFrame]:
            self.titleBar.addVisible(f)

    def createTitleBar(self, title):
        """Create the TitleBar with menu commands."""
        bar = self.titleBar = TitleBar(self, title=title)
        bar.grid(row=self.useRow(), column=0, sticky="ew")

        bar.setMenuCommands(self.getCmds())

    def updateTitleBarVisibility(self):
        """Update the TitleBar visibility based on current state."""
        if self.titleBarVisible:
            self.titleBar.show()
        else:
            self.titleBar.hide()

    def updateFolderBarVisibility(self):
        """Update the FolderBar visibility based on current state."""
        if self.folderBarVisible:
            self.folderBar.show()
        else:
            self.folderBar.hide()

    def toggleFolderBar(self):
        """Toggle the FolderBar visibility."""
        self.folderBarVisible = not self.folderBarVisible
        self.updateFolderBarVisibility()

    def toggleTitleBar(self):
        """Toggle the TitleBar visibility."""
        self.titleBarVisible = not self.titleBarVisible
        self.updateTitleBarVisibility()

    def toggleMaximize(self):
        """Toggle window maximize state."""
        if self.isMaximized:
            self.master.state("normal")
            self.isMaximized = False
        else:
            self.master.state("zoomed")
            self.isMaximized = True

    def toggleMinimize(self):
        """Toggle window minimize state."""
        if self.isMinimized:
            self.master.state("normal")
            self.isMinimized = False
        else:
            self.master.state("iconic")
            self.isMinimized = True

    def toggleOnTop(self):
        """Toggle always on top state."""
        self.isOnTop = not self.isOnTop
        self.master.attributes("-topmost", self.isOnTop)

    def toggleSystemTitle(self):
        """Toggle system title bar visibility."""
        self.systemTitleVisible = not self.systemTitleVisible
        self.master.overrideredirect(not self.systemTitleVisible)

    def showStaplingMenu(self):
        """Show the stapling menu for window positioning."""
        if self.stapling:
            menuData = self.stapling.getStaplingMenu()
            from .PopMenu import PopMenu
            popupMenu = PopMenu(self, menuData)
            popupMenu.show()

    def mainFrame(self):
        """Get the content frame for adding widgets."""
        return self.contentFrame

    def setTitle(self, title):
        """Set the window title."""
        self.titleBar.setTitle(title)

    def getTitle(self):
        """Get the current window title."""
        return self.titleBar.getTitle()

    def addMenuCommand(self, label, command, prepend=False):
        """Add a custom menu command to the TitleBar."""
        self.titleBar.addMenuCommand(label, command, prepend)

    def addSeparator(self):
        """Add a separator line to the menu."""
        self.titleBar.addSeparator()

    def setMenuCommands(self, menuCommands):
        """Set custom menu commands for the TitleBar."""
        self.titleBar.setMenuCommands(menuCommands)

    def getMenuCommands(self):
        """Get the current menu commands."""
        return self.titleBar.getMenuCommands()

    def isTitleBarVisible(self):
        """Check if TitleBar is visible."""
        return self.titleBarVisible

    def isWindowMaximized(self):
        """Check if window is maximized."""
        return self.isMaximized

    def isWindowMinimized(self):
        """Check if window is minimized."""
        return self.isMinimized

    def isWindowOnTop(self):
        """Check if window is always on top."""
        return self.isOnTop

    def isSystemTitleVisible(self):
        """Check if system title bar is visible."""
        return self.systemTitleVisible

    def show(self):
        if self.asWin:
            self.win.mainloop()
        else:
            super().show()

    def setMode(self, mode=None, colorTheme=None):
        if mode is None:
            mode = self.currentMode
        else:
            self.currentMode = mode

        if colorTheme is None:
            colorTheme = self.currentColorTheme
        else:
            self.currentColorTheme = colorTheme

        Theme.init(mode, colorTheme)

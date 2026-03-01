"""
TitleBar Widget
===============

A customizable title bar widget that includes a menu button on the left,
a label in the middle, and a visibility button on the right.
"""
import tkinter as tk

from .basic.Frame import Frame
from .MenuBtn import MenuBtn
from .basic.Label import Label
from .VisibleBtn import VisibleBtn
from .basic.Font import Font
from .basic.Dragging import Dragging
from .BtnBar import BtnBar  # Add import for BtnBar


class TitleBar(Frame):
    """A customizable title bar widget with menu, title, and visibility controls."""

    def __init__(self, master, title="", menuCommands=None, **kwargs):
        """
        Initialize the TitleBar.

        Args:
            master: The parent widget
            title: The title text to display in the center
            menuCommands: List of menu commands for the menu button
            **kwargs: Additional arguments for Frame
        """
        # Set default height for title bar
        if 'height' not in kwargs:
            kwargs['height'] = 40

        # Initialize the base frame
        super().__init__(master, **kwargs)

        # Configure grid layout
        self.grid_columnconfigure(0, weight=0)  # Menu button (fixed width)
        self.grid_columnconfigure(1, weight=1)  # Title label (expands)
        # Visibility button (fixed width)
        self.grid_columnconfigure(2, weight=0)
        self.grid_columnconfigure(3, weight=0)  # BtnBar (fixed width)
        self.grid_rowconfigure(0, weight=1)

        # Store components
        self.menuBtn = None
        self.titleLabel = None
        self.visibleBtn: VisibleBtn = None
        self.btnBar: BtnBar = None  # Add BtnBar reference

        # Create the components
        self.createMenuButton(menuCommands)
        self.createTitleLabel(title)
        self.createBtnBar()  # Create BtnBar
        self.createVisibleButton()

        dragging = self.dragging = Dragging()
        dragging.bindDraggable(self)
        dragging.bindDraggable(self.titleLabel)

    def createMenuButton(self, menuCommands):
        """Create the menu button on the left side."""
        if menuCommands:
            self.menuBtn = MenuBtn(self, menuCommands=menuCommands)
            self.menuBtn.grid(row=0, column=0, sticky="w")

    def createTitleLabel(self, title):
        """Create the title label in the middle."""
        self.titleLabel = Label(self, text=title,
                                font=Font(size=16, weight="bold"))
        self.titleLabel.grid(row=0, column=1, padx=5, sticky=tk.W)

    def createVisibleButton(self):
        """Create the visibility button on the right side."""
        self.visibleBtn = VisibleBtn(self)
        self.visibleBtn.grid(row=0, column=3, sticky="e")

    def createBtnBar(self):
        """Create the BtnBar to the right of the visible button."""
        self.btnBar = BtnBar(self, pady=0, padx=2, button_style={
                             "font": ("Arial", 24)})
        self.btnBar.grid(row=0, column=2, sticky="e")

    def addBtnToBar(self, name: str, callback, style=None, group=None, tooltip=None):
        """
        Add a button to the BtnBar.

        Args:
            name: Button text
            callback: Function to call when button is clicked
            style: Optional button styling
            group: Optional button group name
            tooltip: Optional tooltip text
        """
        if self.btnBar:
            from .BtnBar import BtnConfig
            config = BtnConfig(name=name, callback=callback,
                               style=style, group=group, tooltip=tooltip)
            return self.btnBar.addBtn(config)
        return None

    def addBtnsToBar(self, btnConfigs):
        """
        Add multiple buttons to the BtnBar.

        Args:
            btnConfigs: List of BtnConfig objects
        """
        if self.btnBar:
            self.btnBar.addBtns(btnConfigs)

    def removeBtnFromBar(self, name: str):
        """
        Remove a button from the BtnBar by name.

        Args:
            name: Button text to remove
        """
        if self.btnBar:
            return self.btnBar.removeBtn(name)
        return False

    def clearBtnBar(self):
        """Clear all buttons from the BtnBar."""
        if self.btnBar:
            self.btnBar.clearBtns()

    def getBtnBar(self):
        """
        Get the BtnBar instance.

        Returns:
            BtnBar instance
        """
        return self.btnBar

    def setTitle(self, title):
        """
        Set the title text.

        Args:
            title: The new title text
        """
        if self.titleLabel:
            self.titleLabel.configure(text=title)

    def getTitle(self):
        """
        Get the current title text.

        Returns:
            The current title text
        """
        return self.titleLabel.cget("text") if self.titleLabel else ""

    def setMenuCommands(self, menuCommands):
        """
        Set or update the menu commands.

        Args:
            menuCommands: List of menu commands
        """
        if self.menuBtn:
            self.menuBtn.setMenuCommands(menuCommands)
        elif menuCommands:
            # Create menu button if it doesn't exist
            self.createMenuButton(menuCommands)

    def addMenuCommand(self, label=None, command=None, prepend=False):
        """
        Add a single menu command to the menu button.

        Args:
            label: The menu item label
            command: The function to call when the menu item is selected
        """
        if self.menuBtn:
            self.menuBtn.addMenuCommand(label, command, prepend)
        else:
            # Create menu button with the single command
            self.createMenuButton([(label, command)])

    def addSeparator(self):
        """Add a separator line to the menu."""
        if self.menuBtn:
            self.menuBtn.addSeparator()
        else:
            # Create menu button with a separator
            self.createMenuButton([None])

    def getMenuCommands(self):
        """
        Get the current menu commands.

        Returns:
            List of menu commands
        """
        return self.menuBtn.getMenuCommands() if self.menuBtn else []

    def bindVisible(self, widgets):
        """
        Bind widgets to the visibility button.

        Args:
            widgets: List of widgets to bind for visibility control
        """
        if self.visibleBtn:
            self.visibleBtn.bindWidgets(widgets)

    def addVisible(self, widget):
        """
        Add a single widget to the visibility button.

        Args:
            widget: Widget to add for visibility control
        """
        if self.visibleBtn:
            self.visibleBtn.addWidget(widget)

    def removeVisibilityWidget(self, widget):
        """
        Remove a widget from the visibility button.

        Args:
            widget: Widget to remove from visibility control
        """
        if self.visibleBtn:
            self.visibleBtn.removeWidget(widget)

    def clearVisibilityWidgets(self):
        """Clear all widgets bound to the visibility button."""
        if self.visibleBtn:
            self.visibleBtn.clearWidgets()

    def getVisibilityWidgets(self):
        """
        Get the widgets bound to the visibility button.

        Returns:
            List of bound widgets
        """
        return self.visibleBtn.getBoundWidgets() if self.visibleBtn else []

    def setMenuButtonText(self, text):
        """
        Set the menu button text.

        Args:
            text: The new menu button text
        """
        if self.menuBtn:
            self.menuBtn.configure(text=text)

    def setVisibleButtonText(self, showText=None, hideText=None):
        """
        Set the visibility button text.

        Args:
            showText: Text when widgets are visible
            hideText: Text when widgets are hidden
        """
        if self.visibleBtn:
            if showText:
                self.visibleBtn.setShowText(showText)
            if hideText:
                self.visibleBtn.setHideText(hideText)

    def setVisibleButtonColors(self, showColor=None, hideColor=None):
        """
        Set the visibility button colors.

        Args:
            showColor: Color when widgets are visible
            hideColor: Color when widgets are hidden
        """
        if self.visibleBtn:
            if showColor:
                self.visibleBtn.setShowColor(showColor)
            if hideColor:
                self.visibleBtn.setHideColor(hideColor)

    def showAllWidgets(self):
        """Show all widgets bound to the visibility button."""
        if self.visibleBtn:
            self.visibleBtn.showAll()

    def hideAllWidgets(self):
        """Hide all widgets bound to the visibility button."""
        if self.visibleBtn:
            self.visibleBtn.hideAll()

    def isMenuVisible(self):
        """
        Check if the menu is currently visible.

        Returns:
            True if menu is visible, False otherwise
        """
        return self.menuBtn.isMenuVisible() if self.menuBtn else False

    def showMenu(self):
        """Show the menu."""
        if self.menuBtn:
            self.menuBtn.showMenu()

    def hideMenu(self):
        """Hide the menu."""
        if self.menuBtn:
            self.menuBtn.hideMenu()

    def toggleMenuVisibility(self):
        """Toggle the menu visibility."""
        if self.menuBtn:
            self.menuBtn.toggleMenuVisibility()

    def toggleWidgetVisibility(self):
        """Toggle the visibility of bound widgets."""
        if self.visibleBtn:
            self.visibleBtn.toggleVisibility()


def createTitleBar(master, title="", menuCommands=None, **kwargs):
    """
    Convenience function to create a TitleBar.

    Args:
        master: The parent widget
        title: The title text to display
        menuCommands: List of menu commands
        **kwargs: Additional arguments for TitleBar

    Returns:
        A new TitleBar instance
    """
    return TitleBar(master, title=title, menuCommands=menuCommands, **kwargs)

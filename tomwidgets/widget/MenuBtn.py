"""
MenuBtn Widget
==============

A button that shows a popup menu when clicked. Combines the functionality
of a CustomTkinter button with a popup menu system.
"""

import tkinter as tk
from .basic.Button import Button
from .PopMenu import PopMenu

MenuIcon = "☰"


class MenuBtn(Button):
    """A button that shows a popup menu when clicked."""

    def __init__(self, master, menuCommands=None, **kwargs):
        """
        Initialize the MenuBtn.
        default text of button is MenuIcon

        Args:
            master: The parent widget
            menuCommands: List of menu commands (format: [(label, command), ...])
            **kwargs: Additional arguments for Button
        """
        # Initialize the button
        super().__init__(master, **kwargs)

        if 'text' not in kwargs:
            self.configure(text=MenuIcon)

        # Store menu commands
        self.menuCommands = menuCommands or []

        # Create the popup menu
        self.popupMenu = None
        self.createPopupMenu()

        # Bind click event to show menu
        self.bind("<Button-1>", self.onButtonClick)

    def createPopupMenu(self):
        """Create the popup menu with the specified commands."""
        if self.menuCommands:
            self.popupMenu = PopMenu(self, self.menuCommands)

    def onButtonClick(self, event):
        """Handle button click to show the popup menu."""
        if self.popupMenu:
            self.popupMenu.show()
        return "break"  # Prevent event propagation

    def setMenuCommands(self, menuCommands):
        """Update the menu commands and recreate the popup menu."""
        self.menuCommands = menuCommands
        self.createPopupMenu()

    def addMenuCommand(self, label, command, prepend=False):
        """Add a single command to the menu."""
        if prepend:
            self.menuCommands.insert(0, (label, command))
        else:
            self.menuCommands.append((label, command))

        self.createPopupMenu()

    def addSeparator(self):
        """Add a separator line to the menu."""
        self.menuCommands.append(None)
        self.createPopupMenu()

    def clearMenuCommands(self):
        """Clear all menu commands."""
        self.menuCommands = []
        self.popupMenu = PopMenu(self, self.menuCommands)

    def getMenuCommands(self):
        """Get the current menu commands."""
        return self.menuCommands.copy()

    def showMenu(self):
        """Programmatically show the menu."""
        if self.popupMenu:
            self.popupMenu.show()

    def hideMenu(self):
        """Programmatically hide the menu."""
        if self.popupMenu:
            try:
                self.popupMenu.unpost()
            except tk.TclError:
                pass  # Menu might not be posted

    def isMenuVisible(self):
        """Check if the menu is currently visible."""
        if self.popupMenu:
            try:
                return self.popupMenu.winfo_viewable()
            except tk.TclError:
                return False
        return False


def createMenuButton(master, text, menuCommands=None, **kwargs):
    """
    Convenience function to create a MenuBtn.

    Args:
        master: The parent widget
        text: Button text
        menuCommands: List of menu commands
        **kwargs: Additional arguments for MenuBtn

    Returns:
        MenuBtn: The created menu button
    """
    return MenuBtn(master, text=text, menuCommands=menuCommands, **kwargs)

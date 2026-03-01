"""
ConfigWin Widget
================

A configuration window class that extends BaseWin and contains a ConfigEditor widget.
Provides a complete window for viewing and editing configuration files.
"""

import tkinter as tk
from .BaseWin import BaseWin
from .ConfigEditor import ConfigEditor
from .BtnBar import BtnBar, BtnConfig
from .basic.InputDialog import InputDialog


class ConfigWin(BaseWin):
    """A configuration window with ConfigEditor for file management"""

    def __init__(self, master=None, title="Configuration Window", configFile="tools.ini", **kwargs):
        """
        Initialize the ConfigWin

        Args:
            master: Parent widget
            title: Window title
            configFile: Path to configuration file (default: tools.ini)
            showTitleBar: Whether to show title bar
            **kwargs: Additional arguments for BaseWin
        """
        # Initialize BaseWin first (but configEditor will be created later)
        super().__init__(master, title, **kwargs)

        # Add window-specific buttons FIRST
        self.addWindowButtons()

        # Create config editor after BaseWin is initialized
        self.configFile = configFile
        self.configEditor = ConfigEditor(self.contentFrame, self.configFile)
        self.configEditor.pack(fill="both", expand=True, padx=10, pady=10)

    def addWindowButtons(self):
        """Add configuration-specific buttons to the window"""
        # Create button bar for window-level operations
        self.windowBtnBar = BtnBar(self.contentFrame)
        self.windowBtnBar.pack(fill="x", padx=10, pady=(0, 10))

        # Add window control buttons
        self.windowBtnBar.addBtns([
            BtnConfig(name="New Config", callback=self.newConfigFile),
            BtnConfig(name="Open Config", callback=self.openConfigFile),
            BtnConfig(name="Save As", callback=self.saveConfigAs),
            BtnConfig(name="About", callback=self.showAbout),
        ])

    def newConfigFile(self):
        """Create a new configuration file"""
        try:
            # Prompt for new config file name
            dialog = InputDialog(
                title="New Config File",
                text="Enter new configuration file name:"
            )
            newFileName = dialog.get_input()

            if newFileName:
                # Ensure .ini extension
                if not newFileName.endswith('.ini'):
                    newFileName += '.ini'

                # Create empty config file
                import os
                if os.path.exists(newFileName):
                    self.showMessage(
                        "Warning", f"File {newFileName} already exists!")
                    return

                # Create empty config
                from .Config import Config
                config = Config(newFileName)
                if config.write():
                    self.configFile = newFileName
                    self.configEditor.setConfigFile(self.configFile)
                    self.setTitle(f"Configuration Window - {self.configFile}")
                    self.showMessage(
                        "Success", f"New configuration file {newFileName} created!")
                else:
                    self.showMessage(
                        "Error", "Failed to create new configuration file!")

        except Exception as e:
            self.showMessage("Error", f"Error creating new config file: {e}")

    def openConfigFile(self):
        """Open a different configuration file"""
        try:
            from tkinter import filedialog
            filePath = filedialog.askopenfilename(
                title="Open Configuration File",
                filetypes=[("INI files", "*.ini"), ("All files", "*.*")]
            )

            if filePath:
                self.configFile = filePath
                self.configEditor.setConfigFile(self.configFile)
                self.setTitle(f"Configuration Window - {self.configFile}")

        except Exception as e:
            self.showMessage("Error", f"Error opening config file: {e}")

    def saveConfigAs(self):
        """Save current configuration to a new file"""
        try:
            from tkinter import filedialog
            filePath = filedialog.asksaveasfilename(
                title="Save Configuration As",
                defaultextension=".ini",
                filetypes=[("INI files", "*.ini"), ("All files", "*.*")]
            )

            if filePath:
                # Get current values from editor
                currentValues = self.configEditor.getCurrentValues()

                # Create new config with current values
                from .Config import Config
                newConfig = Config(filePath)

                # Add all sections and options
                for section in currentValues:
                    for key, value in currentValues[section].items():
                        newConfig.add_option(section, key, value)

                # Write to new file
                if newConfig.write():
                    self.configFile = filePath
                    self.configEditor.setConfigFile(self.configFile)
                    self.setTitle(f"Configuration Window - {self.configFile}")
                    self.showMessage(
                        "Success", f"Configuration saved as {filePath}!")
                else:
                    self.showMessage(
                        "Error", "Failed to save configuration file!")

        except Exception as e:
            self.showMessage("Error", f"Error saving config file: {e}")

    def showAbout(self):
        """Show about dialog"""
        aboutText = """Configuration Window

A comprehensive tool for viewing and editing configuration files.

Features:
• View and edit INI configuration files
• Create new configuration files
• Save configurations with different names
• Real-time editing with immediate feedback
• Section and key management

Built with tomwidgets library."""

        self.showMessage("About", aboutText)

    def getConfigFile(self):
        """Get the current configuration file path"""
        return self.configFile

    def setConfigFile(self, configFile):
        """Set a new configuration file"""
        self.configFile = configFile
        self.configEditor.setConfigFile(self.configFile)
        self.setTitle(f"Configuration Window - {self.configFile}")

    def setTitle(self, title):
        """Set window title"""
        self.win.title(title)

    def showMessage(self, title, message):
        """Show message dialog"""
        from .InfoBox import InfoBox
        InfoBox(self, title, message)

    def getCmds(self):
        """Override to add window-specific menu commands"""
        # Build file menu
        fileMenu = [
            ("New Config", self.newConfigFile),
            ("Open Config", self.openConfigFile),
            ("Save As", self.saveConfigAs),
            ("---", None),
            ("Exit", self.onClose),
        ]

        # Build edit menu (only if configEditor exists)
        editMenu = []
        if hasattr(self, 'configEditor'):
            editMenu = [
                ("Reload Config", self.configEditor.reloadConfig),
                ("Save Config", self.configEditor.saveChanges),
            ]

        # Build help menu
        helpMenu = [
            ("About", self.showAbout),
        ]

        # Combine menus
        menu = [
            ("File", fileMenu),
        ]

        # Add edit menu if available
        if editMenu:
            menu.append(("Edit", editMenu))

        # Add help menu
        menu.append(("Help", helpMenu))

        # Add parent menus except the first one (to avoid duplicate Exit)
        parentMenus = super().getCmds()
        if len(parentMenus) > 1:
            menu.extend(parentMenus[1:])

        return menu


def openConfigWin(root, title: str = "Configuration Window", configFile: str = None):
    """Open a new ConfigWin window"""
    ConfigWin(root, title, configFile).show()

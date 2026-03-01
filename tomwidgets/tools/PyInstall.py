from ..widget.BaseWin import BaseWin
from ..widget.basic.Textbox import Textbox
from ..widget.BtnBar import BtnBar, BtnConfig
import tkinter as tk
import os


class PyInstall(BaseWin):
    def __init__(self, master=None, title="PyInstall", showTitleBar=True, showFolderBar=False, asWin=True, **kwargs):
        super().__init__(master=master, title=title, showTitleBar=showTitleBar,
                         showFolderBar=showFolderBar, asWin=asWin, **kwargs)

        # Create the UI components
        self.createUi()

    def createUi(self):
        """Create the main UI components."""
        # Create BtnBar with 2 buttons
        self.btnBar = BtnBar(self.contentFrame)
        self.btnBar.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

        # Configure grid weights for proper expansion
        self.contentFrame.grid_columnconfigure(0, weight=1)
        self.contentFrame.grid_rowconfigure(0, weight=0)
        self.contentFrame.grid_rowconfigure(1, weight=1)

        # Add buttons to BtnBar
        self.btnBar.addBtn(
            BtnConfig("Create pyproject.toml", self.createPyProjectFile))
        self.btnBar.addBtn(
            BtnConfig("Create install.bat", self.createInstallBatFile))

        # Create status display area
        self.statusText = Textbox(self.contentFrame, wrap=tk.WORD)
        self.statusText.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

    def createPyProjectFile(self):
        """Create pyproject_example.toml file with basic Python project configuration."""
        try:
            # Define the content for pyproject.toml
            pyprojectContent = """[build-system]
requires = ["hatchling >= 1.26"]
build-backend = "hatchling.build"

[project]
name = "example-package"
version = "0.1.0"
description = "An example Python package"
authors = [{name = "Your Name", email = "your.email@example.com"}]
readme = "README.md"
license = {text = "MIT"}
requires-python = ">=3.7"
dependencies = ["customtkinter"]

[project.optional-dependencies]
dev = []
"""

            # Write the file
            with open("pyproject_example.toml", "w", encoding="utf-8") as f:
                f.write(pyprojectContent)

            # Update status
            self.updateStatus(f"✅ Created pyproject_example.toml file successfully!\n"
                              f"File location: {os.path.abspath('pyproject_example.toml')}")

        except Exception as e:
            self.updateStatus(
                f"❌ Error creating pyproject_example.toml: {str(e)}")

    def createInstallBatFile(self):
        """Create install_pkg_example.bat file with pip install command."""
        try:
            # Define the content for install.bat
            batContent = """@echo off
echo Installing package in development mode...
pip install -e .
echo Installation complete!
pause
"""

            # Write the file
            with open("install_pkg_example.bat", "w", encoding="utf-8") as f:
                f.write(batContent)

            # Update status
            self.updateStatus(f"✅ Created install_pkg_example.bat file successfully!\n"
                              f"File location: {os.path.abspath('install_pkg_example.bat')}\n"
                              f"Content: pip install -e .")

        except Exception as e:
            self.updateStatus(
                f"❌ Error creating install_pkg_example.bat: {str(e)}")

    def updateStatus(self, message):
        """Update the status display with a message."""
        # Enable text widget for editing
        self.statusText.configure(state=tk.NORMAL)

        # Clear previous content and add new message
        self.statusText.delete(1.0, tk.END)
        self.statusText.insert(tk.END, message)

        # Scroll to the end
        self.statusText.see(tk.END)

        # Disable text widget to make it read-only
        self.statusText.configure(state=tk.DISABLED)

    def getCmds(self):
        """Override to add custom menu commands for PyInstall."""
        # Get base menu commands
        baseCmds = super().getCmds()

        # Add PyInstall specific commands
        pyinstallCmds = [
            ("PyInstall", [
                ("Create pyproject.toml", self.createPyProjectFile),
                ("Create install.bat", self.createInstallBatFile),
                ("Clear Status", lambda: self.updateStatus("Status cleared."))
            ])
        ]

        # Insert PyInstall commands at the beginning
        baseCmds = pyinstallCmds + baseCmds

        return baseCmds

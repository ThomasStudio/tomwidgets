"""
FolderBar widget for tomwidgets library.

A specialized OptionBar for folder selection with add/remove folder capabilities.
Extends OptionBar to provide folder-specific functionality.
"""

import os
import tkinter as tk
from .OptionBar import OptionBar
from .basic import Button
from typing import List, Callable, Any


class FolderBar(OptionBar):
    """
    FolderBar widget for folder selection and management.

    Features:
    - Extends OptionBar with folder-specific functionality
    - Shows list of folders in OptionMenu
    - Add button to add folders to the list
    - Delete button to remove folders from the list
    - Changes current directory when folder is selected
    """

    def __init__(self, master: Any, title: str = "Select Folder:", folders: List[str] = [], **kwargs):
        """
        Initialize the FolderBar widget.

        Args:
            master: The parent widget
            title: The title text for the label
            folders: List of folder paths to display
            **kwargs: Additional arguments for OptionBar
        """
        # Handle folders parameter
        if folders is None:
            folders = []

        # Store parameters before calling super
        self.titleText = title
        self.folderList = folders

        # Call parent constructor with options as folder names
        folderNames = [os.path.basename(
            folder) if folder else "" for folder in folders]
        super().__init__(master, title=title, options=folderNames, **kwargs)

        # Store full paths for folder operations
        self.folderPaths = folders

        # Current working directory
        self.currentDirectory = os.getcwd()

        # Initialize selected value
        self.selectedValue = self.getSelectedOption()

        # Initialize UI with buttons
        self.initFolderBarUi()

    def initFolderBarUi(self):
        """Setup the folder bar user interface components."""
        # Reconfigure grid to accommodate buttons
        self.grid_columnconfigure(0, weight=0)  # Label column
        self.grid_columnconfigure(1, weight=1)  # OptionMenu column
        self.grid_columnconfigure(2, weight=0)  # Add button column
        self.grid_columnconfigure(3, weight=0)  # Delete button column
        self.grid_rowconfigure(0, weight=1)     # Single row

        # Remove existing widgets and recreate with new layout
        self.titleLabel.grid_forget()
        self.optionMenu.grid_forget()

        # Title label
        self.titleLabel = self.titleLabel
        self.titleLabel.grid(row=0, column=0, padx=(
            10, 5), pady=10, sticky="w")

        # OptionMenu
        self.optionMenu = self.optionMenu
        self.optionMenu.grid(row=0, column=1, padx=(5, 5),
                             pady=10, sticky="ew")

        # Add folder button
        self.addButton = Button(self, text="＋", command=self.onAddButtonClick)
        self.addButton.grid(row=0, column=2, padx=(5, 5), pady=10, sticky="e")

        # Delete folder button
        self.delButton = Button(self, text="－", command=self.onDelButtonClick)
        self.delButton.grid(row=0, column=3, padx=(5, 10), pady=10, sticky="e")

        # Update button states
        self.updateButtonStates()

    def onOptionSelect(self, selectedValue: str):
        """Handle OptionMenu selection and change current directory."""
        self.selectedValue = selectedValue

        # Find the corresponding folder path
        folderPath = selectedValue

        if folderPath and os.path.exists(folderPath):
            try:
                # Change current directory
                os.chdir(folderPath)
                self.currentDirectory = folderPath
                print(f"Changed directory to: {folderPath}")
            except Exception as e:
                print(f"Error changing directory: {e}")

        # Update button states
        self.updateButtonStates()

        # Generate event
        self.generateEvent()

    def onAddButtonClick(self):
        """Handle add folder button click."""
        # Open folder selection dialog
        folderPath = tk.filedialog.askdirectory(
            title="Select Folder to Add",
            initialdir=self.currentDirectory
        )

        if folderPath and folderPath not in self.folderPaths:
            self.addFolder(folderPath)

    def onDelButtonClick(self):
        """Handle delete folder button click."""
        selectedValue = self.getSelectedOption()
        if selectedValue:
            self.removeFolderByName(selectedValue)

    def addFolder(self, folderPath: str):
        """
        Add a folder to the folder list.

        Args:
            folderPath: The full path of the folder to add
        """
        if folderPath and folderPath not in self.folderPaths:
            self.folderPaths.append(folderPath)
            folderName = os.path.basename(folderPath)

            # Update OptionMenu values
            currentOptions = self.getOptions()
            currentOptions.append(folderName)
            self.setOptions(currentOptions)

            # Select the newly added folder
            self.setSelectedOption(folderName)

            print(f"Added folder: {folderPath}")

    def removeFolderByName(self, folderName: str) -> bool:
        """
        Remove a folder from the folder list by name.

        Args:
            folderName: The name of the folder to remove

        Returns:
            True if folder was removed, False if not found
        """
        folderPath = self.getFolderPathByName(folderName)
        if folderPath and folderPath in self.folderPaths:
            self.folderPaths.remove(folderPath)

            # Update OptionMenu values
            currentOptions = self.getOptions()
            if folderName in currentOptions:
                currentOptions.remove(folderName)
                self.setOptions(currentOptions)

            # Clear selection if removed folder was selected
            if self.selectedValue == folderName:
                self.clearSelection()

            self.updateButtonStates()
            print(f"Removed folder: {folderPath}")
            return True
        return False

    def removeFolderByPath(self, folderPath: str) -> bool:
        """
        Remove a folder from the folder list by path.

        Args:
            folderPath: The full path of the folder to remove

        Returns:
            True if folder was removed, False if not found
        """
        if folderPath in self.folderPaths:
            folderName = os.path.basename(folderPath)
            self.folderPaths.remove(folderPath)

            # Update OptionMenu values
            currentOptions = self.getOptions()
            if folderName in currentOptions:
                currentOptions.remove(folderName)
                self.setOptions(currentOptions)

            # Clear selection if removed folder was selected
            if self.selectedValue == folderName:
                self.clearSelection()

            self.updateButtonStates()
            print(f"Removed folder: {folderPath}")
            return True
        return False

    def getFolderPathByName(self, folderName: str) -> str:
        """
        Get the full folder path by folder name.

        Args:
            folderName: The name of the folder

        Returns:
            The full path of the folder, or empty string if not found
        """
        for folderPath in self.folderPaths:
            if os.path.basename(folderPath) == folderName:
                return folderPath
        return ""

    def getFolderList(self) -> List[str]:
        """
        Get the list of folder paths.

        Returns:
            List of folder paths
        """
        return self.folderPaths

    def setFolderList(self, folders: List[str]):
        """
        Set the list of folder paths.

        Args:
            folders: List of folder paths
        """
        self.folderPaths = folders
        self.setOptions(folders)

    def getCurrentDirectory(self) -> str:
        """
        Get the current working directory.

        Returns:
            The current directory path
        """
        return self.currentDirectory

    def setCurrentDirectory(self, directory: str):
        """
        Set the current working directory.

        Args:
            directory: The directory path to set
        """
        if os.path.exists(directory):
            try:
                os.chdir(directory)
                self.currentDirectory = directory
                print(f"Set current directory to: {directory}")
            except Exception as e:
                print(f"Error setting directory: {e}")

    def updateButtonStates(self):
        """Update the enabled/disabled state of buttons based on current selection."""
        # Enable delete button only if there's a selection
        if self.getSelectedOption():
            self.delButton.configure(state="normal")
        else:
            self.delButton.configure(state="disabled")

    def clearSelection(self):
        """Clear the current selection."""
        # OptionBar doesn't have clearSelection, so we implement it here
        if self.optionMenu:
            # Set selection to empty string or first option if available
            currentOptions = self.getOptions()
            if currentOptions:
                self.setSelectedOption(currentOptions[0])
            else:
                # If no options, set to empty string and update options
                self.setOptions([])
                self.setSelectedOption("")
        self.updateButtonStates()

    def setSelectedOption(self, value: str):
        """
        Set the selected value in the OptionMenu.

        Args:
            value: The value to select
        """
        super().setSelectedOption(value)
        self.updateButtonStates()

    def bindFolderChanged(self, callback: Callable):
        """
        Bind a callback to the folder changed event.

        Args:
            callback: The function to call when folder selection changes
        """
        self.bindEvent(callback)
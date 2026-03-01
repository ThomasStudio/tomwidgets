"""
OptionBar Widget
===============

A customizable option bar widget that includes a title label and an option menu.
"""

import customtkinter as ctk

from ..model.Cmd import Cmd
from .CmdMgr import CmdMgr
from .basic.Frame import Frame
from .basic.Label import Label
from .basic.OptionMenu import OptionMenu
from .basic.Font import Font


class OptionBar(Frame):
    """A customizable option bar widget with title and option menu."""

    def __init__(self, master, title="Options", options=[], defaultOption=None, titleFont=None, optionFont=None, **kwargs):
        """
        Initialize the OptionBar.

        Args:
            master: The parent widget
            title: The title text
            options: List of options for the option menu
            defaultOption: Default selected option
            titleFont: Font for the title text
            optionFont: Font for the option menu text
            **kwargs: Additional arguments for Frame
        """
        # Initialize the base frame
        super().__init__(master, **kwargs)

        # Configure grid layout
        self.grid_columnconfigure(0, weight=0)  # Title column
        self.grid_columnconfigure(1, weight=1)  # Option menu column
        self.grid_rowconfigure(0, weight=1)

        # Store components
        self.titleLabel = None
        self.optionMenu = None

        # Store configuration
        self.titleFont = titleFont or Font(size=20)
        self.optionFont = optionFont

        # Create the components
        self.createTitleLabel(title)
        self.createOptionMenu(options, defaultOption)

    def createTitleLabel(self, title):
        """Create the title label."""
        self.titleLabel = Label(self, text=title,
                                font=self.titleFont)
        self.titleLabel.grid(row=0, column=0, padx=[0, 5], sticky="w")

    def createOptionMenu(self, options, defaultOption):
        """Create the option menu."""
        # Set default option if not provided
        if defaultOption is None and options:
            defaultOption = options[0]

        # Create option menu
        self.optionMenu = OptionMenu(self,
                                     values=options,
                                     variable=ctk.StringVar(
                                         value=defaultOption),
                                     font=self.optionFont)
        self.optionMenu.grid(row=0, column=1, sticky="ew")

        # Bind the selection event
        self.optionMenu.configure(command=self.onOptionSelect)

    def onOptionSelect(self, selectedOption):
        """Handle option selection event.

        Args:
            selectedOption: The selected option
        """
        self.generateEvent()

    def setTitle(self, title):
        """Set the title text.

        Args:
            title: The new title text
        """
        if self.titleLabel:
            self.titleLabel.configure(text=title)

    def getTitle(self):
        """Get the current title text.

        Returns:
            The current title text
        """
        return self.titleLabel.cget("text") if self.titleLabel else ""

    def setTitleFont(self, font):
        """Set the title font.

        Args:
            font: The new title font
        """
        self.titleFont = font
        if self.titleLabel:
            self.titleLabel.configure(font=font)

    def getTitleFont(self):
        """Get the current title font.

        Returns:
            The current title font
        """
        return self.titleFont

    def setOptions(self, options, defaultOption=None, generateEvent=True):
        """Set or update the options list.

        Args:
            options: New list of options
            defaultOption: Default selected option
        """
        if defaultOption is None and self.getSelectedOption():
            defaultOption = self.getSelectedOption()

        if self.optionMenu:
            # Update the option menu values
            self.optionMenu.configure(values=options)

            # Set default option if provided or use the first option
            if defaultOption is not None:
                self.optionMenu.set(defaultOption)
            elif options:
                self.optionMenu.set(options[0])

            if generateEvent:
                self.generateEvent()

    def getOptions(self):
        """Get the current options list.

        Returns:
            The current options list
        """
        return self.optionMenu.cget("values") if self.optionMenu else []

    def getSelectedOption(self):
        """Get the currently selected option.

        Returns:
            The currently selected option
        """
        return self.optionMenu.get() if self.optionMenu else ""

    def setSelectedOption(self, option):
        """Set the selected option.

        Args:
            option: The option to select
        """
        if self.optionMenu:
            self.optionMenu.set(option)

    def setOptionFont(self, font):
        """Set the option menu font.

        Args:
            font: The new option menu font
        """
        self.optionFont = font
        if self.optionMenu:
            self.optionMenu.configure(font=font)

    def getOptionFont(self):
        """Get the current option menu font.

        Returns:
            The current option menu font
        """
        return self.optionFont

    def bindCmdMgr(self, cmdMgr: CmdMgr, withIndex=False):
        """Bind a CmdMgr instance to the OptionBar.
        This allows the OptionBar to update its options based on the CmdMgr.
        The CmdMgr instance should be initialized with commands before binding.
        If the CmdMgr is not initialized with commands, the OptionBar will be empty.
        If the CmdMgr is initialized with commands, the OptionBar will display them.
        If the CmdMgr is updated with new commands after binding, the OptionBar will reflect the changes.


        Args:
            cmdMgr: CmdMgr instance for command management
        """
        if not cmdMgr:
            return

        def updateWithIndex(event=None):
            cmds = self.cmdMgr.getAllCmds()
            self.setOptions([f"{i}{self.cmdSpliter()}{c.cmd}" for i, c in enumerate(cmds)],
                            defaultOption=self.getSelectedOption(), generateEvent=False)

        def updateWithoutIndex(event=None):
            cmds = self.cmdMgr.getAllCmds()
            self.setOptions(
                [c.cmd for c in cmds], defaultOption=self.getSelectedOption(), generateEvent=False)

        self.cmdMgr = cmdMgr

        cmds = self.cmdMgr.getAllCmds()
        self.setOptions([c.cmd for c in cmds])

        cmdMgr.bindEvent(updateWithIndex if withIndex else updateWithoutIndex)

    def cmdSpliter(self):
        return " : "

    def getSelectedCmd(self) -> Cmd:
        """Get the currently selected command.

        Returns:
            The currently selected command
        """
        if not self.cmdMgr:
            return None

        try:
            index = int(self.getSelectedOption().split(self.cmdSpliter())[0])
            return self.cmdMgr.cmdHistory[index]
        except ValueError:
            return None

    def setDict(self, options: dict):
        self.optionsDict = options

    def getSelectedDict(self) -> tuple:
        if not self.optionsDict:
            return None

        key = self.getSelectedOption()

        if key in self.optionsDict:
            return (key, self.optionsDict[key])
        else:
            return None

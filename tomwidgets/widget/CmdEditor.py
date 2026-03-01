import tkinter as tk
from tkinter import StringVar
import re
from functools import partial
from typing import Dict, List, Optional

from .basic.Frame import Frame
from .InputBar import InputBar


class CmdEditor(Frame):
    """
    A command editor widget that allows editing commands with parameter support.

    Features:
    - Edit command text with parameter placeholders marked with {}
    - Dynamic input fields for each parameter
    - Format command with parameter values
    - Run and clear functionality
    - Focus navigation between input bars
    """

    def __init__(self, master, **kwargs):
        """
        Initialize the CmdEditor widget.

        Args:
            master: The parent widget
            **kwargs: Additional arguments for Frame
        """
        super().__init__(master, **kwargs)

        # Command text variable
        self.cmdVar = StringVar(master=self)

        # Formatted command variable
        self.formattedCmdVar = StringVar(master=self)

        # Dictionary to store parameter values
        self.parameters: Dict[str, str] = {}

        # List to store InputBar widgets for parameters
        self.parameterInputs: List[InputBar] = []

        # InputBar for command entry
        self.cmdInputBar: Optional[InputBar] = None

        # InputBar for formatted command display
        self.formattedCmdInputBar: Optional[InputBar] = None

        # Initialize UI
        self.initUi()

    def initUi(self):
        """Initialize the user interface components."""
        # Command entry InputBar
        self.createCmdInputBar()

        # Formatted command InputBar
        self.createFormattedCmdInputBar()

        # Frame for parameter inputs
        self.createParameterFrame()

    def createCmdInputBar(self):
        """Create the InputBar for command entry."""
        self.cmdInputBar = InputBar(self, title="Cmd:", default="")
        self.cmdInputBar.pack(side=tk.TOP, fill=tk.X, padx=5, pady=(5, 0))

        # Set the command variable
        self.cmdVar = self.cmdInputBar.value

        # Bind to detect changes in command text
        self.cmdVar.trace_add('write', self.onCmdChanged)

        # Bind Enter key to move focus to next input bar
        self.cmdInputBar.input.bind('<Return>', self.moveFocusToNextInputBar)

    def createFormattedCmdInputBar(self):
        self.formattedFrame = Frame(self)
        self.formattedFrame.pack(side=tk.TOP, fill=tk.X, padx=5, pady=(0, 5))
        """Create the InputBar for formatted command display."""
        self.formattedCmdInputBar = InputBar(
            self.formattedFrame, title="Formatted", default="")
        self.formattedCmdInputBar.pack(
            side=tk.TOP, fill=tk.X)

        # Set the formatted command variable
        self.formattedCmdVar = self.formattedCmdInputBar.value

        # Make the formatted command input bar read-only
        self.formattedCmdInputBar.input.configure(state="readonly")

        # Bind Enter key to move focus to next input bar
        self.formattedCmdInputBar.input.bind(
            '<Return>', self.moveFocusToNextInputBar)

        # Initially hide the formatted command InputBar
        self.formattedCmdInputBar.pack_forget()

    def showFormattedCmdInputBar(self):
        """Show the formatted command InputBar."""
        self.formattedCmdInputBar.pack(side=tk.TOP, fill=tk.X)

    def hideFormattedCmdInputBar(self):
        """Hide the formatted command InputBar."""
        self.formattedCmdInputBar.pack_forget()
        self.formattedFrame.resize()

    def createParameterFrame(self):
        """Create the frame for parameter inputs."""
        # Frame to contain parameter inputs
        self.parameterFrame = Frame(self)
        self.parameterFrame.pack(
            side=tk.TOP, fill=tk.BOTH, expand=True, padx=5, pady=5)

    def setCmd(self, cmd: str):
        """Set the command text."""
        self.cmdVar.set(cmd)
        self.detectParameters()
        self.showParameterInputs()
        self.updateFormattedCommand()

    def getCmd(self) -> str:
        """Get the current command text."""
        return self.cmdVar.get()

    def getFormattedCmd(self) -> str:
        """Get the formatted command with parameter values."""
        return self.formatCmdWithParameters()

    def detectParameters(self):
        """Detect parameters in the command text marked with {}."""
        cmd = self.cmdVar.get()
        # Find all parameters marked with {parameter_name}
        parameters = re.findall(r'\{(\w+)\}', cmd)

        # Clear existing parameters
        self.parameters.clear()

        # Initialize parameter values
        for param in parameters:
            self.parameters[param] = ""

    def showParameterInputs(self):
        """Show InputBar widgets for each detected parameter."""
        # Clear existing parameter inputs
        if len(self.parameterInputs) != 0:
            for input_bar in self.parameterInputs:
                input_bar.destroy()
            self.parameterInputs.clear()

            self.parameterFrame.resize()

        if len(self.parameters.keys()) > 0:
            self.showFormattedCmdInputBar()
        else:
            self.hideFormattedCmdInputBar()

        index = 0
        # Create InputBar for each parameter
        for param_name in self.parameters.keys():
            input_bar = InputBar(self.parameterFrame,
                                 title=f"{param_name}:", default="")
            input_bar.pack(side=tk.TOP, fill=tk.X, padx=5, pady=2)

            # Bind to parameter value changes
            input_bar.value.trace_add('write', self.onParameterChanged)

            # Bind Enter key to move focus to next input bar
            input_bar.input.bind(
                '<Return>', partial(self.moveFocusToNextInputBar, index=index))

            self.parameterInputs.append(input_bar)
            index += 1

    def updateFormattedCmdInputBarVisibility(self):
        """Show or hide the formatted command InputBar based on whether parameters exist."""
        if self.formattedCmdInputBar:
            if self.parameters:
                # Show formatted command InputBar if parameters exist
                self.formattedCmdInputBar.show()
            else:
                # Hide formatted command InputBar if no parameters
                self.formattedCmdInputBar.hide()

    def onCmdChanged(self, *args):
        """Handle changes to the command text."""
        self.detectParameters()
        self.showParameterInputs()
        self.updateFormattedCommand()
        # Update formatted command InputBar visibility
        self.updateFormattedCmdInputBarVisibility()

    def onParameterChanged(self, *args):
        """Handle changes to parameter values."""
        # Update parameter values from input bars
        for i, param_name in enumerate(self.parameters.keys()):
            if i < len(self.parameterInputs):
                self.parameters[param_name] = self.parameterInputs[i].value.get()

        self.updateFormattedCommand()

    def formatCmdWithParameters(self) -> str:
        """Format the command by replacing parameters with their values."""
        cmd = self.cmdVar.get()

        # Replace each parameter placeholder with its value
        for param_name, param_value in self.parameters.items():
            placeholder = f"{{{param_name}}}"
            cmd = cmd.replace(placeholder, param_value)

        return cmd

    def updateFormattedCommand(self):
        """Update the formatted command display."""
        formatted_cmd = self.formatCmdWithParameters()
        self.formattedCmdVar.set(formatted_cmd)

    def moveFocusToNextInputBar(self, event=None, index=-1):
        print(f"index: {index}")
        """Move focus to the next parameter input bar when Enter is pressed."""
        # Get all parameter input bars
        focusable_widgets = [bar.input for bar in self.parameterInputs]
        
        if len(focusable_widgets) == 0:
            return

        if index < 0 or index >= len(focusable_widgets):
            index = 0
            focusable_widgets[index].focus_set()
        elif index == len(focusable_widgets) - 1:
            # after input last parameter, move focus to command input bar
            self.cmdInputBar.input.focus_set()
        else:
            next_index = (index + 1) % len(focusable_widgets)
            focusable_widgets[next_index].focus_set()

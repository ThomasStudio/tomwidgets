"""
CmdBar Widget
=============

A command execution widget that combines an OptionBar for command selection,
CmdEditor for command input, BtnBar with Run/Cancel buttons, and TextBar for output display.
"""
import subprocess
import threading
import tkinter as tk

from ..model import Cmd
from .CmdMgr import CmdMgr

from .basic.Frame import Frame

from .BaseWin import BaseWin
from .OptionBar import OptionBar
from .BtnBar import BtnBar, BtnConfig
from .TextBar import TextBar
from .CmdEditor import CmdEditor


class CmdWin(BaseWin):
    """A command execution widget with command selection, input, and output display."""

    def __init__(self, master=None, cmdMgr=None, title="Cmd Win", **kwargs):
        """
        Initialize the CmdBar.

        Args:
            master: The parent widget
            cmdMgr: CmdMgr instance for command management (default: creates new instance)
            **kwargs: Additional arguments for Frame
        """
        # Set default size for command bar
        if 'width' not in kwargs:
            kwargs['width'] = 800
        if 'height' not in kwargs:
            kwargs['height'] = 500

        # Initialize the base frame
        super().__init__(master, title=title, showFolderBar=True, **kwargs)

        mainF = self.mainFrame()
        self.currentRow = 0

        mainF.grid_columnconfigure(0, weight=1)

        # Store components
        self.cmdMgr = cmdMgr if cmdMgr else CmdMgr()
        self.historyMgr = CmdMgr()
        self.optionBar = None
        self.entry = None
        self.btnBar = None
        self.textBar = None
        self.currentProcess = None
        self.isRunning = False

        # Create the components
        self.createOptionBar(mainF)
        self.createEntry(mainF)

        btnF = self.btnFrame = Frame(mainF)
        btnF.grid(row=self.useRow(), column=0, sticky="ew", padx=5, pady=5)

        self.createBtnBar(btnF)
        self.createHistoryBar(btnF)
        self.createTextBar(mainF)

        self.after(100, self.focusCmd)

    def createOptionBar(self, parent):
        """Create the option bar for command selection."""
        self.optionBar = OptionBar(parent, title="Commands")
        self.optionBar.grid(row=self.useRow(), column=0,
                            sticky="ew", padx=5, pady=5)

        # Bind selection event
        self.optionBar.bindEvent(self.onOptionSelected)
        self.optionBar.bindCmdMgr(self.cmdMgr)

    def createEntry(self, parent):
        """Create the CmdEditor widget for command input."""
        self.entry = CmdEditor(parent)
        self.entry.grid(row=self.useRow(), column=0,
                        sticky="ew", padx=5, pady=5)

        # Set initial placeholder command
        self.entry.setCmd("")

        # Bind Enter key in the command input bar to execute command
        if self.entry.cmdInputBar:
            self.entry.cmdInputBar.input.bind(
                "<Return>", lambda event: self.runClicked())

    def createBtnBar(self, parent):
        """Create the button bar with Run and Cancel buttons."""
        self.btnBar = BtnBar(parent)
        self.btnBar.grid(row=0, column=0, sticky="w")

        # Add Run button
        runConfig = BtnConfig(
            name="Run",
            callback=lambda: self.runClicked(),
            tooltip="Execute the command"
        )
        self.btnBar.addBtn(runConfig)

        # Add Cancel button
        cancelConfig = BtnConfig(
            name="Clear",
            callback=lambda: self.clearCommand(),
            tooltip="Clear output and cancel current command"
        )
        self.btnBar.addBtn(cancelConfig)

    def createHistoryBar(self, parent):
        """Create the history bar for command output display."""
        bar = self.historyBar = OptionBar(parent, title="History")
        bar.grid(row=0, column=1, sticky="w")

        def onSelected(event=None):
            """Handle history selection event."""
            selected = bar.getSelectedCmd()
            if selected:
                self.showCmdOutput(selected)

        # Bind selection event
        bar.bindEvent(onSelected)
        bar.bindCmdMgr(self.historyMgr, withIndex=True)

    def createTextBar(self, parent):
        """Create the text bar for command output display."""
        row = self.useRow()

        self.textBar = TextBar(parent, title="Output", showTitleBar=True)
        self.textBar.grid(row=row, column=0,
                          sticky="nsew", padx=5, pady=5)

        parent.grid_rowconfigure(row, weight=1)

        # Set text bar to read-only mode
        self.textBar.setReadOnly(True)

    def updateCommandList(self):
        """Update the option bar with commands from CmdMgr."""
        commands = self.cmdMgr.getAllCmds()
        commandTexts = [cmd.cmd for cmd in commands]
        self.optionBar.setOptions(commandTexts)

    def onOptionSelected(self, event=None):
        """Handle option selection event."""
        selectedOption = self.optionBar.getSelectedOption()
        self.entry.setCmd(selectedOption)

        if len(self.entry.parameters.keys()) == 0:
            self.runClicked()

    def runClicked(self):
        """Execute the command from the CmdEditor widget."""
        if self.isRunning:
            self.appendOutput("Command is already running. Please wait...\n")
            return

        commandText = self.entry.getFormattedCmd().strip()
        if not commandText:
            commandText = self.optionBar.getSelectedOption()
            self.entry.setCmd(self.optionBar.getSelectedOption())

        if not commandText:
            self.appendOutput("Please enter a command to execute.\n")
            return

        # Clear previous output
        self.textBar.clearText()

        # Execute command in a separate thread
        self.isRunning = True
        thread = threading.Thread(target=self.runCommand, args=(commandText,))
        thread.daemon = True
        thread.start()

    def runCommand(self, commandText):
        """Execute the command in a separate thread."""
        try:
            self.appendOutput(f"Executing: ")
            self.appendOutput(f"{commandText}\n", "gold")

            # Execute command with timeout
            process = subprocess.Popen(
                commandText,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )

            self.currentProcess = process

            # Wait for process to complete with timeout
            try:
                stdout, stderr = process.communicate(timeout=30)

                self.historyMgr.addCmd(
                    commandText, commandText, stdout, stderr)

                # Update output in thread-safe manner
                self.after(0, self.updateOutput, stdout,
                           stderr, process.returncode)

            except subprocess.TimeoutExpired:
                process.kill()
                self.after(0, self.appendOutput,
                           "Command timed out after 30 seconds.\n")

        except Exception as e:
            self.after(0, self.appendOutput,
                       f"Error executing command: {str(e)}\n")
        finally:
            self.isRunning = False
            self.currentProcess = None

    def updateOutput(self, stdout, stderr, returncode=None):
        """Update the output display with command results."""
        if stdout:
            self.appendOutput(f"\n--- STDOUT ---\n", "lime")
            self.appendOutput(f"{stdout}\n")
        if stderr:
            self.appendOutput(f"\n--- STDERR ---\n", "pink")
            self.appendOutput(f"{stderr}\n")

        if returncode is not None:
            self.appendOutput(
                f"\nCommand completed with exit code: {returncode}\n")

    def appendOutput(self, text, color=None):
        """Append text to the output display."""
        self.textBar.append(text, color)

    def showEnd(self):
        self.textBar.textBox.see(tk.END)

    def showTop(self):
        self.textBar.textBox.see("1.0")

    def showCmdOutput(self, cmd: Cmd):
        """Show the command in the CmdEditor widget.

        Args:
            cmd: The command to show
        """
        self.entry.setCmd(cmd.cmd)

        self.clearOutput()
        self.appendOutput(f"{cmd.cmd}", "gold")
        self.appendOutput(f"\nExecuted at {cmd.timestamp}\n")

        self.updateOutput(cmd.stdout, cmd.stderr)

        self.textBar.textBox.see("1.0")

    def clearCommand(self):
        """Cancel the current command and clear output."""
        if self.currentProcess and self.currentProcess.poll() is None:
            self.currentProcess.terminate()
            self.appendOutput("\nCommand canceled by user.\n")

        # Clear the output
        self.textBar.clearText()

        # Reset running state
        self.isRunning = False
        self.currentProcess = None

    def addCommand(self, name, command):
        """Add a command to the command manager."""
        self.cmdMgr.addCmd(name, command)
        self.updateCommandList()

    def clearCommands(self):
        """Clear all commands from the command manager."""
        self.cmdMgr.clearHistory()
        self.updateCommandList()

    def getCommandText(self):
        """Get the current command text from the entry."""
        return self.entry.get()

    def setCommandText(self, text):
        """Set the command text in the entry."""
        self.entry.delete(0, tk.END)
        self.entry.insert(0, text)

    def getOutputText(self):
        """Get the current output text."""
        return self.textBar.getText()

    def clearOutput(self):
        """Clear the output text."""
        self.textBar.clearText()

    def selectCmd(self, cmd):
        self.optionBar.setSelectedOption(cmd)
        self.onOptionSelected(cmd)
        self.focusCmd()

    def focusCmd(self):
        input = self.entry.cmdInputBar.input
        input.focus_set()
        input.icursor(tk.END)
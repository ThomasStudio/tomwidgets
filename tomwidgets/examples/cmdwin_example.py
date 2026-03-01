from tomwidgets.widget import CmdMgr
from tomwidgets.widget.CmdWin import CmdWin
from tomwidgets.widget import Theme
import tkinter as tk
import customtkinter as ctk
import sys
import os

# Add the parent directory to the path to import tomwidgets
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))


class CmdBarExample(CmdWin):
    """Example application demonstrating CmdBar functionality."""

    def __init__(self):
        # Create command manager with some sample commands
        cmdMgr = CmdMgr()

        """Initialize the example application."""
        super().__init__(cmdMgr=cmdMgr)

        self.addSampleCommands()
        # Add some instructions
        self.addInstructions()

    def addSampleCommands(self):
        """Add sample commands to the command manager."""
        sampleCommands = [
            ("List Files", "dir" if os.name == 'nt' else "ls"),
            ("Current Directory", "cd"),
            ("Python Version", "python --version"),
            ("Pip List", "pip list"),
            ("System Info", "systeminfo" if os.name == 'nt' else "uname -a"),
            ("Network Info", "ipconfig" if os.name == 'nt' else "ifconfig"),
            ("Disk Space", "wmic logicaldisk get size,freespace,caption" if os.name ==
             'nt' else "df -h"),
            ("Process List", "tasklist" if os.name == 'nt' else "ps aux"),
            ("Environment Variables", "set" if os.name == 'nt' else "env"),
            ("Calendar", "cal" if os.name !=
             'nt' else "echo 'Calendar not available on Windows'"),
        ]

        for name, cmd in sampleCommands:
            self.cmdMgr.addCmd(name, cmd)

        print("✓ Sample commands added to CmdBar")

    def addInstructions(self):
        """Add usage instructions to the CmdBar output."""
        instructions = """
=== CmdBar Usage Instructions ===

1. SELECT COMMAND: Choose a command from the dropdown list to populate the input field
2. EXECUTE: Click 'Run' or press Enter to execute the command
3. OUTPUT: View command output in the text area below
4. CANCEL: Click 'Cancel' to clear the output area
5. CUSTOM COMMANDS: You can also type custom commands directly

Sample commands have been pre-loaded. Try selecting one from the dropdown!
"""
        self.appendOutput(instructions)


def main():
    """Main function to run the example."""
    # Set customtkinter appearance

    Theme.init()

    # Create and run the example
    app = CmdBarExample()
    app.show()


if __name__ == "__main__":
    main()

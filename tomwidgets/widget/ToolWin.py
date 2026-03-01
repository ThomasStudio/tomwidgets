from functools import partial
import tkinter as tk

import os
from typing import Dict, List

from .CmdMgr import CmdMgr

from .BaseWin import BaseWin
from .basic.Tabview import Tabview
from .Config import Config
from .WrapBtnBar import WrapBtnBar, WrapBtnConfig
from .CmdWin import CmdWin


class ToolWin(BaseWin):
    """A window class with tabbed interface for tool commands."""

    def __init__(self, master=None, title="ToolWin", toolsFile: str = "tools.ini", **kwargs):
        """
        Initialize ToolWin with tools configuration.

        Args:
            master: Parent window
            title: Window title
            showTitleBar: Whether to show title bar
            toolsFile: Path to tools.ini file
            **kwargs: Additional arguments for BaseWin
        """

        self.toolsFile = toolsFile
        self.tabview = None
        self.toolsData = {}
        self.cmdMgr = CmdMgr(distinct=True)

        # Initialize BaseWin
        super().__init__(master, title, showFolderBar=False, **kwargs)

        # Load tools and create UI
        self.loadTools()
        self.createToolInterface()

    def getCmds(self):
        from .ConfigWin import openConfigWin

        cmds = super().getCmds()

        for item in cmds:
            if item[0] == "Config":
                item[1].append(("tools.ini", lambda: openConfigWin(
                    self.win, title="tools.ini", configFile=self.toolsFile)),
                )

        return cmds

    def loadTools(self) -> Dict[str, Dict[str, str]]:
        if not os.path.exists(self.toolsFile):
            self.createDefaultToolsFile(self.toolsFile)

        config = Config(self.toolsFile)

        for section in config.sections():
            self.toolsData[section] = dict(config.items(section))

        print(
            f"Loaded {len(self.toolsData)} tool sections from {self.toolsFile}")

        return self.toolsData

    def createToolInterface(self):
        """Create the tabbed interface for tools."""
        # Create Tabview
        self.tabview = Tabview(self.contentFrame, anchor="nw")
        self.tabview.pack(fill=tk.BOTH, expand=True)

        self.addToolsSection()

        # Create tabs for each section
        for sectionName, commands in self.toolsData.items():
            self.createTab(sectionName, commands)

    def createTab(self, sectionName: str, commands: Dict[str, str]):
        """
        Create a tab with buttons for each command in the section.

        Args:
            sectionName: Name of the section/tab
            commands: Dictionary of command names and their commands
        """
        # Add tab to tabview
        tab = self.tabview.add(sectionName.capitalize())

        # Create WrapBtnBar for the tab
        wrapBtnBar = WrapBtnBar(tab, padx=0, pady=2)
        wrapBtnBar.pack(fill=tk.BOTH, expand=True)

        wrapBtnBar.addBtn(WrapBtnConfig(
            name="All", callback=partial(self.runAllCommands, commands)))

        # Create buttons for each command
        for commandName, command in commands.items():
            self.createCommandButton(wrapBtnBar, commandName, command)

    def createCommandButton(self, parent: WrapBtnBar, commandName: str, command: str):
        """
        Create a button for a command.

        Args:
            parent: Parent WrapBtnBar widget
            commandName: Name of the command (displayed on button)
            command: The actual command to execute
        """
        # Create button configuration
        btnConfig = WrapBtnConfig(
            name=commandName,
            callback=lambda cmd=command: self.runCommand(cmd, commandName)
        )

        # Add button to WrapBtnBar
        parent.addBtn(btnConfig)

    def runCommand(self, command: str, commandName: str):
        """
        Execute a command.

        Args:
            command: The command to execute
        """
        self.cmdMgr.addCmd(commandName, command)
        self.launchCmdWin(command)

    def runAllCommands(self, commands: Dict[str, str]):
        """
        Execute all commands in the section.

        Args:
            commands: Dictionary of command names and their commands
        """
        for commandName, command in commands.items():
            self.cmdMgr.addCmd(commandName, command)

        self.launchCmdWin(list(commands.values())[0])

    def launchCmdWin(self, command: str = ""):
        """Launch a CmdWin instance, ensuring only one instance exists."""
        # Check if we already have a CmdWin instance
        if hasattr(self, '_cmdWinInstance') and self._cmdWinInstance:
            # Check if the window still exists
            try:
                # Try to access the window to see if it's still alive
                if hasattr(self._cmdWinInstance.win, 'winfo_exists') and self._cmdWinInstance.win.winfo_exists():
                    # Window exists, bring it to front
                    cmdWin: CmdWin = self._cmdWinInstance
                    cmdWin.win.lift()
                    cmdWin.win.focus_force()
                    cmdWin.selectCmd(command)
                    print("Existing CmdWin instance brought to front")
                    return
                else:
                    # Window no longer exists, clear the reference
                    self._cmdWinInstance = None
            except (tk.TclError, AttributeError):
                # Window was destroyed, clear the reference
                self._cmdWinInstance = None

        # Create new CmdWin instance
        cmdWin = self._cmdWinInstance = CmdWin(
            title="Cmd Win",
            cmdMgr=self.cmdMgr,
        )
        cmdWin.selectCmd(command)

        # Show the window
        cmdWin.show()
        print("New CmdWin instance created")

    def addToolsSection(self):
        tab = self.tabview.add("Tools")

        # Create WrapBtnBar for the tab
        bar = WrapBtnBar(tab, padx=0, pady=2)
        bar.pack(fill=tk.BOTH, expand=True)

        # Create buttons for each command
        for commandName, command in self.tools().items():
            bar.addBtn(
                WrapBtnConfig(
                    name=commandName,
                    callback=lambda tool=command: tool().show()
                )
            )

    def addToolSection(self, sectionName: str, commands: Dict[str, str]):
        """
        Add a new tool section dynamically.

        Args:
            sectionName: Name of the new section
            commands: Dictionary of command names and their commands
        """
        if sectionName not in self.toolsData:
            self.toolsData[sectionName] = commands
            self.createTab(sectionName, commands)
            print(f"Added new tool section: {sectionName}")
        else:
            print(f"Section '{sectionName}' already exists")

    def removeToolSection(self, sectionName: str):
        """
        Remove a tool section.

        Args:
            sectionName: Name of the section to remove
        """
        if sectionName in self.toolsData:
            # Remove from data
            del self.toolsData[sectionName]

            # Remove tab from tabview
            if sectionName in self.tabview._tab_dict:
                self.tabview.delete(sectionName)

            print(f"Removed tool section: {sectionName}")
        else:
            print(f"Section '{sectionName}' not found")

    def getToolSections(self) -> List[str]:
        """
        Get list of available tool sections.

        Returns:
            List of section names
        """
        return list(self.toolsData.keys())

    def getCommandsForSection(self, sectionName: str) -> Dict[str, str]:
        """
        Get commands for a specific section.

        Args:
            sectionName: Name of the section

        Returns:
            Dictionary of command names and their commands
        """
        return self.toolsData.get(sectionName, {})

    def refreshTools(self):
        """Reload tools from configuration file."""
        # Clear existing tabs
        if self.tabview:
            for tabName in list(self.tabview._tab_dict.keys()):
                self.tabview.delete(tabName)

        # Reload tools
        self.toolsData.clear()
        self.loadTools()

        # Recreate interface
        self.createToolInterface()

        print("Tools refreshed")

    def tools(self) -> dict[str, BaseWin]:
        from ..util import ModuleUtil
        from . import ConfigWin
        from .. import tools

        return {
            "ConfigWin": ConfigWin,
            **ModuleUtil.getCallable(tools)
        }

    def show(self):
        """Show the ToolWin window."""
        print("ToolWin started")
        print(f"Tools file: {self.toolsFile}")
        print(f"Available sections: {', '.join(self.getToolSections())}")
        super().show()

    def createDefaultToolsFile(self, toolsFile: str = None):
        """
        Create a default tools.ini file with sample tool sections and commands.

        Args:
            toolsFile: Path to the tools file (defaults to self.toolsFile)
        """
        if toolsFile is None:
            toolsFile = self.toolsFile

        # Create default tools configuration
        default_tools = """# Default Tools Configuration
# This file contains tool sections and commands for the ToolWin interface.
# Each section represents a tab, and each key-value pair represents a command button.

[Sys]
# System administration commands
dir = dir
cd = cd
systeminfo = systeminfo
tasklist = tasklist
ipconfig = ipconfig

[Dev]
# Development and programming tools
py_version = python --version
pip_list = pip list

[Git]
# Git version control commands
git_status = git status
git_log = git log --oneline
git_branch = git branch
git_pull = git pull
git_push = git push
git_commit = git commit -m {comment}

[Network]
# Network and connectivity tools
tracert = tracert
nslookup = nslookup
netstat = netstat -an
"""

        # Create directory if it doesn't exist
        tools_dir = os.path.dirname(toolsFile)
        if tools_dir and not os.path.exists(tools_dir):
            os.makedirs(tools_dir)

        # Write the default tools configuration to file
        with open(toolsFile, 'w', encoding='utf-8') as f:
            f.write(default_tools)

        print(f"Created default tools file: {toolsFile}")

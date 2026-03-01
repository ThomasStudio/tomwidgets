"""
CmdHistory Model
================

A model class to manage a list of Cmd objects with history functionality.
Supports adding, removing, clearing, and navigating through command history.
"""

import time
from typing import List, Optional
from dataclasses import dataclass, field
from .Cmd import Cmd


@dataclass
class CmdHistory:
    """A class to manage command history with navigation and persistence."""

    # List of command history
    history: List[Cmd] = field(default_factory=list)

    # Current position in history (for navigation)
    currentPosition: int = -1

    # Maximum number of history entries to keep
    maxHistorySize: int = 100

    def addHistory(self, name: str, cmd: str, stdout: str = "", stderr: str = "") -> Cmd:
        """
        Add a new command to the history.

        Args:
            name: The name/description of the command
            cmd: The command string
            stdout: The standard output of the command
            stderr: The standard error of the command

        Returns:
            The created Cmd object
        """
        # Create new Cmd object
        newCmd = Cmd(name=name, cmd=cmd, stdout=stdout, stderr=stderr)

        self.addCmd(newCmd)

        return newCmd

    def addCmd(self, cmd: Cmd):
        """
        Add a command to the history.

        Args:
            cmd: The command object to add
        """
        if not cmd:
            return

        if not cmd.timestamp:
            cmd.timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

        self.history.append(cmd)

        # Update current position to the end
        self.currentPosition = len(self.history) - 1

        # Trim history if it exceeds max size
        if len(self.history) > self.maxHistorySize:
            self.history = self.history[-self.maxHistorySize:]
            self.currentPosition = len(self.history) - 1

    def getPrevious(self) -> Optional[Cmd]:
        """
        Get the previous command in history.

        Returns:
            The previous Cmd object, or None if at the beginning
        """
        if not self.history or self.currentPosition <= 0:
            return None

        self.currentPosition -= 1
        return self.history[self.currentPosition]

    def getNext(self) -> Optional[Cmd]:
        """
        Get the next command in history.

        Returns:
            The next Cmd object, or None if at the end
        """
        if not self.history or self.currentPosition >= len(self.history) - 1:
            return None

        self.currentPosition += 1
        return self.history[self.currentPosition]

    def getCurrent(self) -> Optional[Cmd]:
        """
        Get the current command in history.

        Returns:
            The current Cmd object, or None if no history
        """
        if not self.history or self.currentPosition < 0:
            return None

        return self.history[self.currentPosition]

    def getRecent(self, count: int = 5) -> List[Cmd]:
        """
        Get the most recent commands.

        Args:
            count: Number of recent commands to return

        Returns:
            List of recent Cmd objects
        """
        if not self.history:
            return []

        return self.history[-count:]

    def clearHistory(self) -> None:
        """Clear all command history."""
        self.history.clear()
        self.currentPosition = -1

    def removeCmd(self, index: int) -> bool:
        """
        Remove a command from history by index.

        Args:
            index: The index of the command to remove

        Returns:
            True if removed successfully, False otherwise
        """
        if 0 <= index < len(self.history):
            removedCmd = self.history.pop(index)

            # Adjust current position if needed
            if self.currentPosition >= index:
                self.currentPosition -= 1

            # Ensure current position is valid
            if not self.history:
                self.currentPosition = -1
            elif self.currentPosition < 0:
                self.currentPosition = 0
            elif self.currentPosition >= len(self.history):
                self.currentPosition = len(self.history) - 1

            return True
        return False

    def searchByName(self, name: str) -> List[Cmd]:
        """
        Search commands by name.

        Args:
            name: The name to search for (case-insensitive)

        Returns:
            List of matching Cmd objects
        """
        return [cmd for cmd in self.history if name.lower() in cmd.name.lower()]

    def searchByCmd(self, cmdText: str) -> List[Cmd]:
        """
        Search commands by command text.

        Args:
            cmdText: The command text to search for (case-insensitive)

        Returns:
            List of matching Cmd objects
        """
        return [cmd for cmd in self.history if cmdText.lower() in cmd.cmd.lower()]

    def getSize(self) -> int:
        """Get the current size of the history."""
        return len(self.history)

    def isEmpty(self) -> bool:
        """Check if history is empty."""
        return len(self.history) == 0

    def setMaxHistorySize(self, size: int) -> None:
        """
        Set the maximum history size.

        Args:
            size: New maximum size (must be positive)
        """
        if size > 0:
            self.maxHistorySize = size
            # Trim history if it exceeds new max size
            if len(self.history) > self.maxHistorySize:
                self.history = self.history[-self.maxHistorySize:]
                self.currentPosition = len(self.history) - 1

    def resetPosition(self) -> None:
        """Reset the current position to the end of history."""
        if self.history:
            self.currentPosition = len(self.history) - 1
        else:
            self.currentPosition = -1

    def __len__(self) -> int:
        """Get the number of commands in history."""
        return len(self.history)

    def __getitem__(self, index: int) -> Cmd:
        """Get a command by index."""
        return self.history[index]

    def __iter__(self):
        """Iterate through the command history."""
        return iter(self.history)

    def __str__(self) -> str:
        """String representation of the command history."""
        if not self.history:
            return "CmdHistory (empty)"

        result = [f"CmdHistory ({len(self.history)} commands):"]
        for i, cmd in enumerate(self.history):
            marker = " ->" if i == self.currentPosition else "   "
            result.append(
                f"{marker} [{i}] {cmd.timestamp} - {cmd.name}: {cmd.cmd}")

        return "\n".join(result)

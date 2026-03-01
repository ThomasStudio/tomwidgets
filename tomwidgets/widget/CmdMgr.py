import time

from typing import List
from ..model import Cmd, CmdHistory
from .basic.EventBus import EventBus


class CmdMgr(EventBus):
    def __init__(self, distinct: bool = False) -> None:
        self.distinct = distinct
        EventBus.__init__(self, defaultEvent='cmdAdded')
        self.cmdHistory: CmdHistory = CmdHistory()

    def addCmd(self, name: str, cmd: str, stdout: str = "", stderr: str = "", timestamp: str = None, distinct: bool = None) -> None:
        if distinct is None:
            distinct = self.distinct
        if distinct and self.cmdHistory.searchByCmd(cmd):
            return

        if timestamp is None:
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

        newCmd = Cmd(name=name, cmd=cmd, stdout=stdout,
                     stderr=stderr, timestamp=timestamp)
        self.cmdHistory.addCmd(newCmd)
        # Generate default event after adding command
        self.generateEvent()

    def getCurrentCmd(self) -> Cmd:
        return self.cmdHistory.getCurrent()

    def getPreviousCmd(self) -> Cmd:
        return self.cmdHistory.getPrevious()

    def getNextCmd(self) -> Cmd:
        return self.cmdHistory.getNext()

    def searchCmdByName(self, name: str) -> List[Cmd]:
        return self.cmdHistory.searchByName(name)

    def searchCmdByText(self, text: str) -> List[Cmd]:
        return self.cmdHistory.searchByCmd(text)

    def getHistorySize(self) -> int:
        return self.cmdHistory.getSize()

    def isHistoryEmpty(self) -> bool:
        return self.cmdHistory.isEmpty()

    def getRecentCmds(self, count: int = 5) -> List[Cmd]:
        return self.cmdHistory.getRecent(count)

    def removeCmd(self, index: int) -> bool:
        return self.cmdHistory.removeCmd(index)

    def clearHistory(self) -> None:
        self.cmdHistory.clearHistory()

    def setMaxHistorySize(self, size: int) -> None:
        self.cmdHistory.setMaxHistorySize(size)

    def resetPosition(self) -> None:
        self.cmdHistory.resetPosition()

    def getHistoryAsString(self) -> str:
        return str(self.cmdHistory)

    def getAllCmds(self) -> List[Cmd]:
        return [self.cmdHistory[i] for i in range(len(self.cmdHistory))]

    def getCmdByIndex(self, index: int) -> Cmd:
        if 0 <= index < len(self.cmdHistory):
            return self.cmdHistory[index]
        return None

    def updateCmdStdout(self, index: int, stdout: str) -> bool:
        cmd = self.getCmdByIndex(index)
        if cmd:
            cmd.stdout = stdout
            return True
        return False

    def updateCmdStderr(self, index: int, stderr: str) -> bool:
        cmd = self.getCmdByIndex(index)
        if cmd:
            cmd.stderr = stderr
            return True
        return False

    def updateCmdTimestamp(self, index: int, timestamp: str) -> bool:
        cmd = self.getCmdByIndex(index)
        if cmd:
            cmd.timestamp = timestamp
            return True
        return False
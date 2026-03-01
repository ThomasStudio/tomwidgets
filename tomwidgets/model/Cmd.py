from dataclasses import dataclass
import time


@dataclass
class Cmd:
    name: str
    cmd: str
    stdout: str = ""
    stderr: str = ""
    timestamp: str = time.strftime("%Y-%m-%d %H:%M:%S")
    isError: bool = False

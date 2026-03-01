import sys
import os

# Add the parent directory to the path to import tomwidgets
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tomwidgets.model import CmdHistory


def basic_usage():
    """Demonstrate basic usage of CmdHistory."""
    print("=== Basic Usage ===")
    
    # Create a new CmdHistory instance
    history = CmdHistory()
    
    # Add some commands to the history with separate stdout and stderr
    history.addHistory("List Files", "ls -la", "file1.txt\nfile2.txt\nREADME.md", "")
    history.addHistory("Check Python", "python --version", "Python 3.13.0", "")
    history.addHistory("Directory Info", "pwd", "/home/user/projects", "")
    history.addHistory("Git Status", "git status", "On branch main\nYour branch is up to date", "")
    
    # Display the history
    print("Command History:")
    print(history)
    print()
    
    # Get current command
    current = history.getCurrent()
    print(f"Current command: {current.name} - {current.cmd}")
    print()


def navigation_demo():
    """Demonstrate navigation through command history."""
    print("=== Navigation Demo ===")
    
    history = CmdHistory()
    
    # Add commands
    commands = [
        ("List Files", "ls -la"),
        ("Check Disk", "df -h"),
        ("Memory Info", "free -m"),
        ("Process List", "ps aux"),
        ("Network Info", "netstat -tuln")
    ]
    
    for name, cmd in commands:
        history.addHistory(name, cmd)
    
    print("Initial history:")
    print(history)
    print()
    
    # Navigate backwards
    print("Navigating backwards:")
    for i in range(3):
        cmd = history.getPrevious()
        if cmd:
            print(f"Previous {i+1}: {cmd.name} - {cmd.cmd}")
    print()
    
    # Navigate forwards
    print("Navigating forwards:")
    for i in range(2):
        cmd = history.getNext()
        if cmd:
            print(f"Next {i+1}: {cmd.name} - {cmd.cmd}")
    print()


def search_demo():
    """Demonstrate search functionality."""
    print("=== Search Demo ===")
    
    history = CmdHistory()
    
    # Add various commands
    commands = [
        ("Python Version", "python --version"),
        ("Python Help", "python -h"),
        ("List Files", "ls -la"),
        ("List Directory", "ls -l"),
        ("Git Status", "git status"),
        ("Git Log", "git log --oneline"),
        ("Disk Usage", "du -sh .")
    ]
    
    for name, cmd in commands:
        history.addHistory(name, cmd)
    
    # Search by name
    print("Search by name 'Python':")
    python_cmds = history.searchByName("Python")
    for cmd in python_cmds:
        print(f"  - {cmd.name}: {cmd.cmd}")
    print()
    
    # Search by command text
    print("Search by command text 'git':")
    git_cmds = history.searchByCmd("git")
    for cmd in git_cmds:
        print(f"  - {cmd.name}: {cmd.cmd}")
    print()
    
    # Search by command text 'ls'
    print("Search by command text 'ls':")
    ls_cmds = history.searchByCmd("ls")
    for cmd in ls_cmds:
        print(f"  - {cmd.name}: {cmd.cmd}")
    print()


def management_demo():
    """Demonstrate history management features."""
    print("=== Management Demo ===")
    
    history = CmdHistory()
    
    # Add commands with separate stdout and stderr
    for i in range(8):
        history.addHistory(f"Command {i+1}", f"cmd{i+1}", f"Output for command {i+1}", "")
    
    print("Initial history (8 commands):")
    print(f"Size: {history.getSize()}")
    print(f"Is empty: {history.isEmpty()}")
    print()
    
    # Get recent commands
    print("Recent 3 commands:")
    recent = history.getRecent(3)
    for cmd in recent:
        print(f"  - {cmd.name}: {cmd.cmd}")
    print()
    
    # Remove a command
    print("Removing command at index 2:")
    history.removeCmd(2)
    print(f"New size: {history.getSize()}")
    print()
    
    # Set max history size
    print("Setting max history size to 5:")
    history.setMaxHistorySize(5)
    print(f"Size after limiting: {history.getSize()}")
    print()
    
    # Clear history
    print("Clearing history:")
    history.clearHistory()
    print(f"Size after clearing: {history.getSize()}")
    print(f"Is empty: {history.isEmpty()}")
    print()


def iteration_demo():
    """Demonstrate iteration and indexing."""
    print("=== Iteration Demo ===")
    
    history = CmdHistory()
    
    # Add commands
    commands = [
        ("First Command", "cmd1"),
        ("Second Command", "cmd2"),
        ("Third Command", "cmd3"),
        ("Fourth Command", "cmd4")
    ]
    
    for name, cmd in commands:
        history.addHistory(name, cmd)
    
    # Using len()
    print(f"Number of commands: {len(history)}")
    print()
    
    # Using indexing
    print("Access by index:")
    for i in range(len(history)):
        cmd = history[i]
        print(f"  [{i}] {cmd.name}: {cmd.cmd}")
    print()
    
    # Using iteration
    print("Iterating through history:")
    for i, cmd in enumerate(history):
        print(f"  {i}. {cmd.name}: {cmd.cmd}")
    print()


def advanced_features():
    """Demonstrate advanced features."""
    print("=== Advanced Features ===")
    
    history = CmdHistory()
    
    # Add commands with different stdout and stderr
    history.addHistory("Successful Command", "echo 'Hello World'", "Hello World", "")
    history.addHistory("Error Command", "invalid-command", "", "command not found: invalid-command")
    history.addHistory("Long Running", "sleep 5", "Process completed", "")
    
    print("Command history with stdout and stderr:")
    for cmd in history:
        print(f"  {cmd.timestamp} - {cmd.name}")
        print(f"    Command: {cmd.cmd}")
        print(f"    Stdout: {cmd.stdout}")
        print(f"    Stderr: {cmd.stderr}")
        print()
    
    # Reset position
    print("Resetting position to end:")
    history.resetPosition()
    current = history.getCurrent()
    print(f"Current command: {current.name}")
    print()


def main():
    """Run all demos."""
    print("CmdHistory Example")
    print("==================")
    print()
    
    basic_usage()
    navigation_demo()
    search_demo()
    management_demo()
    iteration_demo()
    advanced_features()
    
    print("=== All demos completed ===")


if __name__ == "__main__":
    main()
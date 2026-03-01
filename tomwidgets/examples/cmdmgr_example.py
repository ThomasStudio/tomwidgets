import time
from tomwidgets.widget import CmdMgr
from tomwidgets.model import Cmd


def demonstrateSingletonPattern():
    """Demonstrate that CmdMgr is a singleton."""
    print("=== Singleton Pattern Demonstration ===")
    
    # Get first instance
    mgr1 = CmdMgr()
    print(f"First instance ID: {id(mgr1)}")
    
    # Get second instance - should be the same object
    mgr2 = CmdMgr()
    print(f"Second instance ID: {id(mgr2)}")
    
    print(f"Are they the same object? {mgr1 is mgr2}")
    print()


def demonstrateBasicUsage():
    """Demonstrate basic CmdMgr functionality."""
    print("=== Basic Usage Demonstration ===")
    
    mgr = CmdMgr()
    
    # Add some commands with separate stdout and stderr
    mgr.addCmd("ls", "ls -la", "total 16\ndrwxr-xr-x  4 user  staff   128 Jan 15 10:30 .\ndrwxr-xr-x  5 user  staff   160 Jan 15 10:30 ..", "")
    mgr.addCmd("pwd", "pwd", "/Users/user/projects", "")
    mgr.addCmd("git status", "git status", "On branch main\nYour branch is up to date with 'origin/main'.", "")
    
    print(f"History size: {mgr.getHistorySize()}")
    print(f"Is history empty? {mgr.isHistoryEmpty()}")
    print()


def demonstrateNavigation():
    """Demonstrate command history navigation."""
    print("=== Navigation Demonstration ===")
    
    mgr = CmdMgr()
    
    # Add some commands with timestamps and separate stdout/stderr
    currentTime = time.strftime("%Y-%m-%d %H:%M:%S")
    mgr.addCmd("Command 1", "echo 'Hello World'", "Hello World", "", currentTime)
    mgr.addCmd("Command 2", "python --version", "Python 3.11.0", "", currentTime)
    mgr.addCmd("Command 3", "pip list", "Package    Version\n---------- -------\nrequests   2.28.0", "", currentTime)
    
    # Navigate through history
    print("Navigating through history:")
    
    # Start at current position (end)
    current = mgr.getCurrentCmd()
    print(f"Current: {current.name if current else 'None'}")
    
    # Go back
    previous = mgr.getPreviousCmd()
    print(f"Previous: {previous.name if previous else 'None'}")
    
    # Go back again
    previous2 = mgr.getPreviousCmd()
    print(f"Previous 2: {previous2.name if previous2 else 'None'}")
    
    # Try to go back beyond beginning
    previous3 = mgr.getPreviousCmd()
    print(f"Previous 3: {previous3.name if previous3 else 'None'}")
    
    # Go forward
    nextCmd = mgr.getNextCmd()
    print(f"Next: {nextCmd.name if nextCmd else 'None'}")
    
    print()


def demonstrateSearch():
    """Demonstrate command search functionality."""
    print("=== Search Demonstration ===")
    
    mgr = CmdMgr()
    
    # Add various commands with separate stdout and stderr
    mgr.addCmd("Find Files", "find . -name '*.py'", "main.py\nutils.py\ntest.py", "")
    mgr.addCmd("Python Script", "python main.py", "Hello from main.py", "")
    mgr.addCmd("List Python Files", "ls *.py", "main.py\nutils.py\ntest.py", "")
    mgr.addCmd("Git Python", "git add *.py", "", "")
    
    # Search by name
    pythonResults = mgr.searchCmdByName("Python")
    print(f"Commands with 'Python' in name: {len(pythonResults)}")
    for cmd in pythonResults:
        print(f"  - {cmd.name}: {cmd.cmd}")
    
    # Search by command text
    pyResults = mgr.searchCmdByText("*.py")
    print(f"Commands with '*.py' in command: {len(pyResults)}")
    for cmd in pyResults:
        print(f"  - {cmd.name}: {cmd.cmd}")
    
    print()


def demonstrateHistoryManagement():
    """Demonstrate history management features."""
    print("=== History Management Demonstration ===")
    
    mgr = CmdMgr()
    
    # Add some commands with separate stdout and stderr
    for i in range(10):
        mgr.addCmd(f"Test Command {i}", f"echo 'Test {i}'", f"Test {i}", "")
    
    print(f"Initial history size: {mgr.getHistorySize()}")
    
    # Get recent commands
    recent = mgr.getRecentCmds(3)
    print(f"Recent 3 commands: {[cmd.name for cmd in recent]}")
    
    # Remove a command
    removed = mgr.removeCmd(2)
    print(f"Removed command at index 2: {removed}")
    print(f"History size after removal: {mgr.getHistorySize()}")
    
    # Set max history size
    mgr.setMaxHistorySize(5)
    print(f"Set max history size to 5")
    
    # Add more commands to test size limit
    for i in range(10, 15):
        mgr.addCmd(f"Extra Command {i}", f"echo 'Extra {i}'", f"Extra {i}", "")
    
    print(f"History size after adding more commands: {mgr.getHistorySize()}")
    print()


def demonstrateAdvancedFeatures():
    """Demonstrate advanced CmdMgr features."""
    print("=== Advanced Features Demonstration ===")
    
    mgr = CmdMgr()
    
    # Add commands with separate stdout and stderr
    mgr.addCmd("Database Query", "SELECT * FROM users", "id | name | email\n1  | John | john@example.com", "")
    mgr.addCmd("API Call", "curl https://api.example.com/data", '{"status": "success", "data": [...]}', "")
    
    # Get all commands
    allCmds = mgr.getAllCmds()
    print(f"Total commands: {len(allCmds)}")
    
    # Get command by index
    cmd = mgr.getCmdByIndex(0)
    if cmd:
        print(f"Command at index 0: {cmd.name}")
    
    # Update command stdout using the new method
    updated = mgr.updateCmdStdout(0, "Updated output with more details")
    print(f"Updated command stdout: {updated}")
    
    # Get history as string
    historyStr = mgr.getHistoryAsString()
    print("History as string (first 200 chars):")
    print(historyStr[:200] + "..." if len(historyStr) > 200 else historyStr)
    
    print()


def demonstrateIteration():
    """Demonstrate iterating through command history."""
    print("=== Iteration Demonstration ===")
    
    mgr = CmdMgr()
    
    # Add some commands with separate stdout and stderr
    mgr.addCmd("Iteration Test 1", "test1", "output1", "")
    mgr.addCmd("Iteration Test 2", "test2", "output2", "")
    mgr.addCmd("Iteration Test 3", "test3", "output3", "")
    
    # Iterate using len() and indexing
    print("Iterating through commands:")
    for i in range(len(mgr.cmdHistory)):
        cmd = mgr.getCmdByIndex(i)
        if cmd:
            print(f"  {i}: {cmd.name} - {cmd.cmd}")
    
    print()


def demonstrateClearAndReset():
    """Demonstrate clearing history and resetting position."""
    print("=== Clear and Reset Demonstration ===")
    
    mgr = CmdMgr()
    
    # Add some commands with separate stdout and stderr
    mgr.addCmd("Pre-clear 1", "cmd1", "out1", "")
    mgr.addCmd("Pre-clear 2", "cmd2", "out2", "")
    
    print(f"History size before clear: {mgr.getHistorySize()}")
    
    # Clear history
    mgr.clearHistory()
    print(f"History size after clear: {mgr.getHistorySize()}")
    print(f"Is history empty? {mgr.isHistoryEmpty()}")
    
    # Add new commands with separate stdout and stderr
    mgr.addCmd("Post-clear 1", "new1", "newout1", "")
    mgr.addCmd("Post-clear 2", "new2", "newout2", "")
    
    # Reset position
    mgr.resetPosition()
    current = mgr.getCurrentCmd()
    print(f"Current command after reset: {current.name if current else 'None'}")
    
    print()


def demonstrateEventBusFunctionality():
    """Demonstrate CmdMgr's EventBus functionality."""
    print("=== EventBus Functionality Demonstration ===")
    
    mgr = CmdMgr()
    
    # Event handler functions - updated to handle EventBus keyword arguments
    def onCmdAdded(**kwargs):
        cmd = kwargs.get('cmd')
        name = kwargs.get('name', 'Unknown')
        if cmd:
            print(f"Event: Command '{name}' added - cmd: {cmd.cmd[:20]}...")
    
    def onCmdAddedWithDetails(**kwargs):
        cmd = kwargs.get('cmd')
        name = kwargs.get('name', 'Unknown')
        stdout = kwargs.get('stdout', '')
        stderr = kwargs.get('stderr', '')
        if cmd:
            print(f"Event Details: {name} -> {cmd.cmd} (stdout: {len(stdout)} chars, stderr: {len(stderr)} chars)")
    
    def onCmdAddedWithTimestamp(**kwargs):
        name = kwargs.get('name', 'Unknown')
        timestamp = kwargs.get('timestamp')
        if timestamp:
            print(f"Event Timestamp: {name} added at {timestamp}")
        else:
            print(f"Event Timestamp: {name} added (no timestamp)")
    
    # Bind event handlers to the default 'cmdAdded' event
    print("Binding event handlers...")
    mgr.bindEvent(onCmdAdded)
    mgr.bindEvent(onCmdAddedWithDetails)
    mgr.bindEvent(onCmdAddedWithTimestamp)
    
    print(f"Number of handlers for default event: {mgr.getHandlerCount()}")
    print(f"Has default event? {mgr.hasEvent('cmdAdded')}")
    
    # Add commands - this should trigger the event handlers
    print("\nAdding commands (should trigger events):")
    currentTime = time.strftime("%Y-%m-%d %H:%M:%S")
    mgr.addCmd("Event Test 1", "echo 'Hello EventBus'", "Hello EventBus", "", currentTime)
    mgr.addCmd("Event Test 2", "python --version", "Python 3.11.0", "")
    
    # Test unbinding
    print("\nUnbinding one handler...")
    mgr.unbindEvent(onCmdAddedWithDetails)
    print(f"Number of handlers after unbinding: {mgr.getHandlerCount()}")
    
    # Add another command - should only trigger remaining handlers
    print("\nAdding another command (should trigger remaining handlers):")
    mgr.addCmd("Event Test 3", "ls -la", "total 16\ndrwxr-xr-x", "")
    
    # Test unbinding all handlers
    print("\nUnbinding all handlers...")
    mgr.unbindEvent(eventName="cmdAdded")
    print(f"Number of handlers after unbinding all: {mgr.getHandlerCount()}")
    
    # Add final command - should not trigger any events
    print("\nAdding final command (should not trigger events):")
    mgr.addCmd("Event Test 4", "pwd", "/home/user", "")
    
    print("EventBus functionality demonstration completed!")
    print()


def main():
    """Run all demonstration functions."""
    print("CmdMgr Example - Singleton Command Manager")
    print("=" * 50)
    print()
    
    # Run all demonstrations
    demonstrateSingletonPattern()
    demonstrateBasicUsage()
    demonstrateNavigation()
    demonstrateSearch()
    demonstrateHistoryManagement()
    demonstrateAdvancedFeatures()
    demonstrateIteration()
    demonstrateClearAndReset()
    demonstrateEventBusFunctionality()
    
    print("=" * 50)
    print("Example completed successfully!")


if __name__ == "__main__":
    main()
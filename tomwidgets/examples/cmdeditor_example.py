import tkinter as tk
from tkinter import messagebox

from tomwidgets.widget import CmdEditor, Button, Tk, Frame, BtnBar, BtnConfig


def main():
    from tomwidgets.widget import Theme
    Theme.init()
    """Main function to demonstrate CmdEditor functionality."""
    # Create main window
    root = Tk()
    root.title("CmdEditor Example")
    root.geometry("600x500")

    # Create CmdEditor widget
    cmd_editor = CmdEditor(root)
    cmd_editor.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    # Set example commands
    def setExampleCommand1():
        """Set example command 1: Python script with arguments."""
        cmd_editor.setCmd(
            "python {script} --input {input_file} --output {output_file}")

    def setExampleCommand2():
        """Set example command 2: Git command with repository and branch."""
        cmd_editor.setCmd("git clone {repo_url} --branch {branch_name}")

    def setExampleCommand3():
        """Set example command 3: Directory listing with path."""
        cmd_editor.setCmd("dir {path}")

    def setExampleCommand4():
        """Set example command 4: File copy with source and destination."""
        cmd_editor.setCmd("copy {source} {destination}")

    # Add example buttons
    example_frame = Frame(root)
    example_frame.pack(fill=tk.X, padx=10, pady=5)

    bar = BtnBar(example_frame)
    bar.pack(side=tk.LEFT, padx=5)
    bar.addBtns(
        [
            BtnConfig("dir", lambda: cmd_editor.setCmd("dir")),
            BtnConfig("Python Script", setExampleCommand1),
            BtnConfig("Git Clone", setExampleCommand2),
            BtnConfig("Dir Command", setExampleCommand3),
            BtnConfig("Copy Command", setExampleCommand4),
        ]
    )

    # Set initial example command
    setExampleCommand1()

    # Run the application
    root.mainloop()


if __name__ == "__main__":
    main()

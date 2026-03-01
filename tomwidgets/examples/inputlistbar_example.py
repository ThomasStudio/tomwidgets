from tomwidgets import Theme, WrapBtnBar, WrapBtnConfig
from tomwidgets.widget.InputListBar import InputListBar
import customtkinter as ctk
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))


from tomwidgets.widget.InputListBar import OptionInput


def main():
    """Main function to demonstrate InputListBar functionality."""
    Theme.init()

    app = ctk.CTk()
    app.title("InputListBar Example")
    app.geometry("600x500")

    # Create main frame
    mainFrame = ctk.CTkFrame(app)
    mainFrame.pack(fill="both", expand=True, padx=20, pady=20)

    # Create InputListBar
    inputListBar = InputListBar(mainFrame, inputs={}, showRemoveBtn=True, showBtnBar=True)
    inputListBar.pack(fill="x", pady=(0, 20))

    # Create control panel
    controlFrame = ctk.CTkFrame(mainFrame)
    controlFrame.pack(fill="x", pady=(0, 20))

    btnBar = WrapBtnBar(controlFrame)
    btnBar.pack(fill="x")

    btnBar.addBtns([
        WrapBtnConfig("Set", lambda: inputListBar.setArguments({
            "name": "John Doe",
            "email": "john@example.com",
            "age": "30",
            "status": OptionInput("status", ["Active", "Inactive", "Pending"], "Active"),
            "role": OptionInput("role", ["Admin", "User", "Guest"], "User")
        })),
        WrapBtnConfig("Add", lambda: inputListBar.addArguments({
            "city": "New York",
            "country": "USA",
            "theme": OptionInput("theme", ["Light", "Dark", "System"], "Dark")
        })),
        WrapBtnConfig("Remove 'age'",
                  lambda: inputListBar.removeArguments(["age"])),
        WrapBtnConfig("Clear All", lambda: inputListBar.clearAllArguments()),
        WrapBtnConfig("Show info", lambda: logAction(inputListBar.getArguments())),
        WrapBtnConfig("toggle btnBar", lambda: inputListBar.toggleBtnBar()),
        WrapBtnConfig("toggle removeBtn", lambda: inputListBar.toggleRemoveBtn()),
    ])

    # Create action log
    logLabel = ctk.CTkLabel(mainFrame, text="Action Log:")
    logLabel.pack(anchor="w")

    logText = ctk.CTkTextbox(mainFrame, height=150)
    logText.pack(fill="both", expand=True)

    def logAction(message):
        """Add a message to the action log."""
        logText.insert("end", f"{message}\n")
        logText.see("end")

    # Bind event handlers
    def onConfirm(event=None):
        arguments = inputListBar.getArguments()
        logAction(f"Confirm: {arguments}")

    def onCancel(event=None):
        logAction("Cancel")

    inputListBar.onConfirm(onConfirm)
    inputListBar.onCancel(onCancel)

    # Log initial state
    logAction("🚀 InputListBar Example Started")
    logAction("Click 'Set Arguments' to populate the InputListBar with both regular inputs and OptionInputs")

    app.mainloop()


if __name__ == "__main__":
    main()
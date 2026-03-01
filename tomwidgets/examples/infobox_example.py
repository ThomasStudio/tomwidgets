import customtkinter as ctk
from tomwidgets.widget import InfoBox, showMessageBox
from tomwidgets.widget.basic import Button, Label, Frame


class MessageBoxExample(ctk.CTk):
    """Main application class for MessageBox example."""

    def __init__(self):
        """Initialize the application."""
        super().__init__()

        self.title("MessageBox Example - tomwidgets")
        self.geometry("600x500")

        # Configure grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)  # Title
        self.grid_rowconfigure(1, weight=0)  # Description
        self.grid_rowconfigure(2, weight=0)  # Demo buttons
        self.grid_rowconfigure(3, weight=1)  # Log area

        self.setupUi()

    def setupUi(self):
        """Setup the user interface."""
        # Title label
        titleLabel = Label(self, text="MessageBox Widget Example",
                           font=ctk.CTkFont(size=20, weight="bold"))
        titleLabel.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

        # Description
        descriptionLabel = Label(self,
                                 text="This example demonstrates the MessageBox widget - a customizable dialog with title, message, and confirm button.",
                                 font=ctk.CTkFont(size=12),
                                 justify="left",
                                 wraplength=560)
        descriptionLabel.grid(row=1, column=0, padx=20,
                              pady=(0, 20), sticky="ew")

        # Demo buttons frame
        self.setupDemoButtons()

        # Log area
        self.setupLogArea()

    def setupDemoButtons(self):
        """Setup demo buttons for different MessageBox scenarios."""
        demoFrame = Frame(self)
        demoFrame.grid(row=2, column=0, padx=20, pady=20, sticky="ew")

        # Configure demo frame grid
        for i in range(3):
            demoFrame.grid_columnconfigure(i, weight=1)

        # Basic message box
        basicBtn = Button(demoFrame, text="Basic MessageBox",
                          command=self.showBasicMessageBox)
        basicBtn.grid(row=0, column=0, padx=10, pady=10)

        # Custom title and message
        customBtn = Button(demoFrame, text="Custom MessageBox",
                           command=self.showCustomMessageBox)
        customBtn.grid(row=0, column=1, padx=10, pady=10)

        # With callback
        callbackBtn = Button(demoFrame, text="MessageBox with Callback",
                             command=self.showCallbackMessageBox)
        callbackBtn.grid(row=0, column=2, padx=10, pady=10)

        # Second row of buttons
        errorBtn = Button(demoFrame, text="Error Dialog",
                          command=self.showErrorMessageBox)
        errorBtn.grid(row=1, column=0, padx=10, pady=10)

        warningBtn = Button(demoFrame, text="Warning Dialog",
                            command=self.showWarningMessageBox)
        warningBtn.grid(row=1, column=1, padx=10, pady=10)

        successBtn = Button(demoFrame, text="Success Dialog",
                            command=self.showSuccessMessageBox)
        successBtn.grid(row=1, column=2, padx=10, pady=10)

        # Third row - dynamic examples
        dynamicBtn = Button(demoFrame, text="Dynamic MessageBox",
                            command=self.showDynamicMessageBox)
        dynamicBtn.grid(row=2, column=0, padx=10, pady=10)

        customButtonBtn = Button(demoFrame, text="Custom Button Text",
                                 command=self.showCustomButtonMessageBox)
        customButtonBtn.grid(row=2, column=1, padx=10, pady=10)

        convenienceBtn = Button(demoFrame, text="Convenience Function",
                                command=self.showConvenienceMessageBox)
        convenienceBtn.grid(row=2, column=2, padx=10, pady=10)

    def setupLogArea(self):
        """Setup the log text area."""
        logFrame = Frame(self)
        logFrame.grid(row=3, column=0, padx=20, pady=20, sticky="nsew")

        # Log title
        logTitle = Label(logFrame, text="Event Log:",
                         font=ctk.CTkFont(weight="bold"))
        logTitle.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        # Log text area
        self.logText = ctk.CTkTextbox(logFrame, height=200)
        self.logText.grid(row=1, column=0, padx=10,
                          pady=(0, 10), sticky="nsew")

        # Configure log frame grid
        logFrame.grid_rowconfigure(1, weight=1)
        logFrame.grid_columnconfigure(0, weight=1)

    def logMessage(self, message: str):
        """
        Add a message to the log area.

        Args:
            message: The message to log
        """
        self.logText.insert("end", f"{message}\n")
        self.logText.see("end")

    # Demo functions
    def showBasicMessageBox(self):
        """Show a basic message box with default settings."""
        self.logMessage("📝 Showing basic MessageBox...")

        def confirmed():
            self.logMessage("✅ Basic MessageBox confirmed")

        showMessageBox(None,
                       title="Basic Message",
                       message="This is a basic message box with default settings.",
                       buttonCallback=confirmed)

    def showCustomMessageBox(self):
        """Show a message box with custom title and message."""
        self.logMessage("🎨 Showing custom MessageBox...")

        messageBox = InfoBox(self,
                                title="Custom Dialog",
                                message="This message box has a custom title and message. You can customize the appearance and behavior as needed.")
        messageBox.show()

        result = messageBox.getResult()

        if result:
            self.logMessage("✅ Custom MessageBox confirmed")

    def showCallbackMessageBox(self):
        """Show a message box with a callback function."""
        self.logMessage("🔗 Showing MessageBox with callback...")

        def onConfirm():
            self.logMessage("🎯 Callback executed: MessageBox confirmed!")

        messageBox = InfoBox(self,
                                title="Callback Example",
                                message="This message box will execute a callback function when confirmed.",
                                buttonCallback=onConfirm)
        messageBox.show()

    def showErrorMessageBox(self):
        """Show an error-style message box."""
        self.logMessage("❌ Showing error MessageBox...")

        messageBox = InfoBox(self,
                                title="Error Occurred",
                                message="An unexpected error has occurred. Please try again or contact support if the problem persists.",
                                buttonText="Close")
        messageBox.show()

        result = messageBox.getResult()

        if result:
            self.logMessage("✅ Error dialog closed")

    def showWarningMessageBox(self):
        """Show a warning-style message box."""
        self.logMessage("⚠️ Showing warning MessageBox...")

        messageBox = InfoBox(self,
                                title="Warning",
                                message="This action cannot be undone. Are you sure you want to proceed?",
                                buttonText="Proceed")
        messageBox.show()

        result = messageBox.getResult()

        if result:
            self.logMessage("✅ Warning acknowledged, proceeding...")

    def showSuccessMessageBox(self):
        """Show a success-style message box."""
        self.logMessage("✅ Showing success MessageBox...")

        messageBox = InfoBox(self,
                                title="Success!",
                                message="Your operation has been completed successfully.",
                                buttonText="Great!")
        messageBox.show()

        result = messageBox.getResult()

        if result:
            self.logMessage("✅ Success dialog acknowledged")

    def showDynamicMessageBox(self):
        """Show a message box with dynamic content."""
        self.logMessage("🔄 Showing dynamic MessageBox...")

        messageBox = InfoBox(self,
                                title="Dynamic Content",
                                message="This message box demonstrates dynamic content updates.")

        # Update content after creation
        messageBox.setTitle("Updated Title")
        messageBox.setMessage(
            "The title and message have been dynamically updated!")
        messageBox.setButtonText("Got it!")
        messageBox.show()
        result = messageBox.getResult()

        if result:
            self.logMessage("✅ Dynamic MessageBox confirmed")

    def showCustomButtonMessageBox(self):
        """Show a message box with custom button text."""
        self.logMessage("🔘 Showing MessageBox with custom button...")

        messageBox = InfoBox(self,
                                title="Custom Button",
                                message="This message box has a custom button text instead of the default 'OK'.",
                                buttonText="Custom Action")
        messageBox.show()

        result = messageBox.getResult()

        if result:
            self.logMessage("✅ Custom button action confirmed")

    def showConvenienceMessageBox(self):
        """Show a message box using the convenience function."""
        self.logMessage("⚡ Showing MessageBox via convenience function...")

        from tomwidgets.widget.InfoBox import showMessageBox

        def onConvenienceConfirm():
            self.logMessage("🎯 Convenience function callback executed!")

        messageBox = showMessageBox(self,
                                    title="Convenience Function",
                                    message="This message box was created using the showMessageBox convenience function.",
                                    buttonCallback=onConvenienceConfirm)
        messageBox.show()

        result = messageBox.getResult()

        if result:
            self.logMessage("✅ Convenience MessageBox confirmed")


def main():
    """Main function to run the MessageBox example."""
    # Create and run the application
    app = MessageBoxExample()
    app.mainloop()


if __name__ == "__main__":
    main()

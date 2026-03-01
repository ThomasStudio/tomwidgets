import customtkinter as ctk
from tomwidgets.widget.EditBar import EditBar


class EditBarExample(ctk.CTk):
    """Main application class for EditBar example."""

    def __init__(self):
        """Initialize the application."""
        super().__init__()

        self.title("EditBar Example - tomwidgets")
        self.geometry("700x500")

        # Configure grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)  # Title
        self.grid_rowconfigure(1, weight=0)  # EditBars
        self.grid_rowconfigure(2, weight=0)  # Control buttons
        self.grid_rowconfigure(3, weight=1)   # Log area

        self.setupUi()

    def setupUi(self):
        """Setup the user interface."""
        # Title label
        titleLabel = ctk.CTkLabel(self, text="EditBar Widget Example",
                                  font=ctk.CTkFont(size=20, weight="bold"))
        titleLabel.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

        # EditBars frame
        inputFrame = ctk.CTkFrame(self)
        inputFrame.grid(row=1, column=0, padx=20, pady=10, sticky="ew")
        inputFrame.grid_columnconfigure(0, weight=1)

        # Create EditBar widgets
        self.createEditBars(inputFrame)

        # Control buttons
        self.addControlButtons()

        # Log area
        self.setupLogArea()

    def createEditBars(self, parent):
        """Create and configure EditBar widgets."""
        # EditBar 1: Basic usage
        self.editBar1 = EditBar(parent, title="Name:", defaultValue="John Doe",
                                editCallback=lambda value: self.logMessage(
                                    f"📝 Name updated to: {value}"),
                                removeCallback=lambda: self.confirmRemoval("Name"))
        self.editBar1.grid(row=0, column=0, padx=20, pady=10, sticky="ew")

        # EditBar 2: With custom styling
        self.editBar2 = EditBar(parent, title="Email:", defaultValue="john@example.com",
                                editCallback=lambda value: self.logMessage(
                                    f"📧 Email updated to: {value}"),
                                removeCallback=lambda: self.confirmRemoval("Email"))
        self.editBar2.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

        # Configure custom styling
        self.editBar2.configInput(width=200)
        self.editBar2.configTitle(font=ctk.CTkFont(weight="bold"))

        # EditBar 3: Empty initially
        self.editBar3 = EditBar(parent, title="Phone:",
                                editCallback=lambda value: self.logMessage(
                                    f"📞 Phone updated to: {value}"),
                                removeCallback=lambda: self.confirmRemoval("Phone"))
        self.editBar3.grid(row=2, column=0, padx=20, pady=10, sticky="ew")

        # EditBar 4: Empty initially
        self.editBar4 = EditBar(parent, title="Phone:",
                                editCallback=lambda value: self.logMessage(
                                    f"📞 Phone updated to: {value}"))
        self.editBar4.grid(row=3, column=0, padx=20, pady=10, sticky="ew")

        # EditBar 5: Empty initially
        self.editBar5 = EditBar(parent, title="Phone:", readonly=False)
        self.editBar5.grid(row=4, column=0, padx=20, pady=10, sticky="ew")

    def confirmRemoval(self, fieldName: str) -> bool:
        """
        Confirm removal of an item.

        Args:
            fieldName: Name of the field being removed

        Returns:
            True to proceed with removal, False to cancel
        """
        self.logMessage(f"⚠️ {fieldName} marked for removal (callback)")
        return True  # Return True to allow removal

    def addControlButtons(self):
        """Add control buttons for dynamic operations."""
        buttonFrame = ctk.CTkFrame(self)
        buttonFrame.grid(row=2, column=0, padx=20, pady=20, sticky="ew")

        # Configure button frame grid
        for i in range(3):
            buttonFrame.grid_columnconfigure(i, weight=1)

        # Get values button
        getValuesButton = ctk.CTkButton(buttonFrame, text="Get All Values",
                                        command=self.getAllValues)
        getValuesButton.grid(row=0, column=0, padx=5, pady=5)

        # Add new EditBar button
        addNewButton = ctk.CTkButton(buttonFrame, text="Add New EditBar",
                                     command=self.addNewEditBar)
        addNewButton.grid(row=0, column=1, padx=5, pady=5)

        # Clear all button
        clearAllButton = ctk.CTkButton(buttonFrame, text="Clear All",
                                       command=self.clearAllInputs)
        clearAllButton.grid(row=0, column=2, padx=5, pady=5)

    def setupLogArea(self):
        """Setup the log text area."""
        logFrame = ctk.CTkFrame(self)
        logFrame.grid(row=3, column=0, padx=20, pady=20, sticky="nsew")

        # Log title
        logTitle = ctk.CTkLabel(logFrame, text="Event Log:",
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

    # Event handlers
    def onEditBar1Edit(self, value: str):
        """Handle EditBar 1 edit event."""
        self.logMessage(f"📝 Name updated: '{value}'")

    def onEditBar2Edit(self, value: str):
        """Handle EditBar 2 edit event."""
        self.logMessage(f"📧 Email updated: '{value}'")

    def onEditBar3Edit(self, value: str):
        """Handle EditBar 3 edit event."""
        self.logMessage(f"📞 Phone updated: '{value}'")

    # Control button handlers
    def getAllValues(self):
        """Get and display all current values."""
        values = {
            self.editBar1.getTitle(): self.editBar1.getValue(),
            self.editBar2.getTitle(): self.editBar2.getValue(),
            self.editBar3.getTitle(): self.editBar3.getValue()
        }

        self.logMessage("📊 Current values:")
        for title, value in values.items():
            self.logMessage(f"   {title}: {value}")

    def clearAllInputs(self):
        """Clear all input fields."""
        self.editBar1.setValue("")
        self.editBar2.setValue("")
        self.editBar3.setValue("")

        self.logMessage("🧹 All input fields cleared")

    def addNewEditBar(self):
        """Add a new EditBar dynamically."""
        # In a real implementation, you'd create a new EditBar and add it to the parent
        self.logMessage("➕ Adding new EditBar (implementation example)")

    def onClosing(self):
        """Handle window closing."""
        self.destroy()


def main():
    app = EditBarExample()
    app.mainloop()

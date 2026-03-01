import customtkinter as ctk
from tomwidgets import ComboBar


class ComboBarExample(ctk.CTk):
    """Main application class for ComboBar example."""

    def __init__(self):
        """Initialize the application."""
        super().__init__()

        self.title("ComboBar Example - tomwidgets")
        self.geometry("600x500")

        # Configure grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)  # Title
        self.grid_rowconfigure(1, weight=0)  # Control panel
        self.grid_rowconfigure(2, weight=1)  # Log area

        self.setupUi()

    def setupUi(self):
        """Setup the user interface."""
        # Title label
        titleLabel = ctk.CTkLabel(self, text="ComboBar Widget Example",
                                  font=ctk.CTkFont(size=20, weight="bold"))
        titleLabel.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

        # Control panel frame
        controlFrame = ctk.CTkFrame(self)
        controlFrame.grid(row=1, column=0, padx=20, pady=10, sticky="ew")
        controlFrame.grid_columnconfigure(0, weight=1)

        # Create ComboBar widgets
        self.createComboBars(controlFrame)

        # Log area
        self.setupLogArea()

    def createComboBars(self, parent):
        """Create and configure ComboBar widgets."""
        # ComboBar 1: Basic usage
        self.comboBar1 = ComboBar(parent, title="Select Country:",
                                  values=["USA", "Canada", "UK", "Germany", "France", "Japan"])
        self.comboBar1.grid(row=0, column=0, padx=20, pady=10, sticky="ew")

        # ComboBar 2: With custom styling
        self.comboBar2 = ComboBar(parent, title="Choose Color:",
                                  values=["Red", "Green", "Blue", "Yellow", "Purple", "Orange"])
        self.comboBar2.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

        # ComboBar 3: Empty initially, values added dynamically
        self.comboBar3 = ComboBar(parent, title="Programming Language:")
        self.comboBar3.grid(row=2, column=0, padx=20, pady=10, sticky="ew")

        # Add values to ComboBar 3
        self.comboBar3.setValues(
            ["Python", "JavaScript", "Java", "C++", "Go", "Rust"])
        self.comboBar3.setSelectedValue("Python")

        bar4 = self.comboBar4 = ComboBar(parent, title="Select Number:", values=[
                                         "1", "2", "3", "4", "5", "6"])
        bar4.grid(row=3, column=0, padx=20, pady=10, sticky="ew")
        bar4.readOnly()
        

        # Bind event handlers
        self.bindEventHandlers()

        # Add control buttons
        self.addControlButtons(parent)

    def bindEventHandlers(self):
        """Bind event handlers to ComboBar widgets."""
        # ComboBar 1: Basic event handling
        self.comboBar1.bindSelectionChanged(self.onComboBar1Select)

        # ComboBar 2: Event with priority
        self.comboBar2.bindSelectionChanged(self.onComboBar2Select)
        self.comboBar2.bindSelectionChanged(self.onComboBar2Log)

        # ComboBar 3: One-time event handler
        self.comboBar3.bindSelectionChanged(self.onComboBar3FirstSelect)
        self.comboBar3.bindSelectionChanged(self.onComboBar3Select)

    def addControlButtons(self, parent):
        """Add control buttons for dynamic operations."""
        buttonFrame = ctk.CTkFrame(parent)
        buttonFrame.grid(row=4, column=0, padx=20, pady=20, sticky="ew")

        # Configure button frame grid
        for i in range(4):
            buttonFrame.grid_columnconfigure(i, weight=1)

        # Add value button
        addButton = ctk.CTkButton(buttonFrame, text="Add Value",
                                  command=self.addValueToComboBar1)
        addButton.grid(row=0, column=0, padx=5, pady=5)

        # Remove value button
        removeButton = ctk.CTkButton(buttonFrame, text="Remove Value",
                                     command=self.removeValueFromComboBar1)
        removeButton.grid(row=0, column=1, padx=5, pady=5)

        # Clear selection button
        clearButton = ctk.CTkButton(buttonFrame, text="Clear All Selections",
                                    command=self.clearAllSelections)
        clearButton.grid(row=0, column=2, padx=5, pady=5)

        # Disable/Enable toggle
        self.toggleButton = ctk.CTkButton(buttonFrame, text="Disable ComboBar 2",
                                          command=self.toggleComboBar2)
        self.toggleButton.grid(row=0, column=3, padx=5, pady=5)

    def setupLogArea(self):
        """Setup the log text area."""
        logFrame = ctk.CTkFrame(self)
        logFrame.grid(row=2, column=0, padx=20, pady=20, sticky="nsew")

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
    def onComboBar1Select(self, event):
        """Handle ComboBar 1 selection."""
        newValue = self.comboBar1.getSelectedValue()
        title = self.comboBar1.getTitle()

        self.logMessage(
            f"📊 {title} Selection changed: '{newValue}'")

    def onComboBar2Select(self, event):
        """Handle ComboBar 2 selection (priority 1)."""
        newValue = self.comboBar2.getSelectedValue()
        title = self.comboBar2.getTitle()

        self.logMessage(f"🎨 {title} Color selected: '{newValue}' (Priority 1)")

    def onComboBar2Log(self, event):
        """Handle ComboBar 2 selection (priority 2)."""
        newValue = self.comboBar2.getSelectedValue()

        self.logMessage(
            f"   → Additional logging for color: '{newValue}' (Priority 2)")

    def onComboBar3FirstSelect(self, event):
        """Handle ComboBar 3 first selection (one-time)."""
        newValue = self.comboBar3.getSelectedValue()

        self.logMessage(
            f"🚀 First selection made: '{newValue}' (One-time event!)")

    def onComboBar3Select(self, event):
        """Handle ComboBar 3 selection."""
        newValue = self.comboBar3.getSelectedValue()

        self.logMessage(f"💻 Language changed: '{newValue}'")

    # Control button handlers
    def addValueToComboBar1(self):
        """Add a new value to ComboBar 1."""
        currentValues = self.comboBar1.getValues()
        newValue = f"Country_{len(currentValues) + 1}"

        self.comboBar1.addValue(newValue)
        self.logMessage(f"➕ Added new value to ComboBar 1: '{newValue}'")

    def removeValueFromComboBar1(self):
        """Remove the last value from ComboBar 1."""
        currentValues = self.comboBar1.getValues()
        if currentValues:
            valueToRemove = currentValues[-1]
            if self.comboBar1.removeValue(valueToRemove):
                self.logMessage(
                    f"➖ Removed value from ComboBar 1: '{valueToRemove}'")
            else:
                self.logMessage("❌ Failed to remove value from ComboBar 1")
        else:
            self.logMessage("⚠️ No values to remove from ComboBar 1")

    def clearAllSelections(self):
        """Clear selections from all ComboBars."""
        self.comboBar1.clearSelection()
        self.comboBar2.clearSelection()
        self.comboBar3.clearSelection()

        self.logMessage("🧹 Cleared all selections")

    def toggleComboBar2(self):
        """Toggle ComboBar 2 between enabled and disabled states."""
        currentState = self.comboBar2.cget("state")

        if currentState == "normal":
            self.comboBar2.disable()
            self.toggleButton.configure(text="Enable ComboBar 2")
            self.logMessage("🔒 ComboBar 2 disabled")
        else:
            self.comboBar2.enable()
            self.toggleButton.configure(text="Disable ComboBar 2")
            self.logMessage("🔓 ComboBar 2 enabled")


def main():
    """Main function to run the example."""
    app = ComboBarExample()
    app.mainloop()


if __name__ == "__main__":
    main()

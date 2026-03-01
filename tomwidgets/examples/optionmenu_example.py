import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import customtkinter as ctk
from tomwidgets.widget.basic.OptionMenu import OptionMenu


class OptionMenuExample(ctk.CTk):
    """Main application class for OptionMenu example."""

    def __init__(self):
        """Initialize the application."""
        super().__init__()

        self.title("OptionMenu Example - tomwidgets")
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
        titleLabel = ctk.CTkLabel(self, text="OptionMenu Widget Example",
                                  font=ctk.CTkFont(size=20, weight="bold"))
        titleLabel.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

        # Control panel frame
        controlFrame = ctk.CTkFrame(self)
        controlFrame.grid(row=1, column=0, padx=20, pady=10, sticky="ew")
        controlFrame.grid_columnconfigure(0, weight=1)

        # Create OptionMenu widgets
        self.createOptionMenus(controlFrame)

        # Log area
        self.setupLogArea()

    def createOptionMenus(self, parent):
        """Create and configure OptionMenu widgets."""
        # OptionMenu 1: Basic usage
        self.optionMenu1 = OptionMenu(parent, 
                                     values=["Option 1", "Option 2", "Option 3", "Option 4", "Option 5"])
        self.optionMenu1.grid(row=0, column=0, padx=20, pady=10, sticky="ew")
        self.optionMenu1.set("Option 1")  # Set default value

        # OptionMenu 2: With custom styling
        self.optionMenu2 = OptionMenu(parent, 
                                     values=["Red", "Green", "Blue", "Yellow", "Purple"],
                                     fg_color="#2b2b2b",
                                     button_color="#3b8ed0",
                                     button_hover_color="#36719f")
        self.optionMenu2.grid(row=1, column=0, padx=20, pady=10, sticky="ew")
        self.optionMenu2.set("Green")  # Set default value

        # OptionMenu 3: Empty initially, values added dynamically
        self.optionMenu3 = OptionMenu(parent)
        self.optionMenu3.grid(row=2, column=0, padx=20, pady=10, sticky="ew")

        # Add values to OptionMenu 3
        self.optionMenu3.configure(values=["Python", "JavaScript", "Java", "C++", "Go", "Rust"])
        self.optionMenu3.set("Python")  # Set default value

        # OptionMenu 4: Read-only style (custom colors)
        self.optionMenu4 = OptionMenu(parent, 
                                     values=["Low", "Medium", "High", "Critical"],
                                     fg_color="#1e1e1e",
                                     button_color="#d63031",
                                     button_hover_color="#b71540")
        self.optionMenu4.grid(row=3, column=0, padx=20, pady=10, sticky="ew")
        self.optionMenu4.set("Medium")  # Set default value

        # Bind event handlers
        self.bindEventHandlers()

        # Add control buttons
        self.addControlButtons(parent)

    def bindEventHandlers(self):
        """Bind event handlers to OptionMenu widgets."""
        # OptionMenu 1: Basic event handling
        self.optionMenu1.configure(command=self.onOptionMenu1Select)

        # OptionMenu 2: Event with custom handling
        self.optionMenu2.configure(command=self.onOptionMenu2Select)

        # OptionMenu 3: Dynamic value handling
        self.optionMenu3.configure(command=self.onOptionMenu3Select)

        # OptionMenu 4: Priority level handling
        self.optionMenu4.configure(command=self.onOptionMenu4Select)

    def addControlButtons(self, parent):
        """Add control buttons for dynamic operations."""
        buttonFrame = ctk.CTkFrame(parent)
        buttonFrame.grid(row=4, column=0, padx=20, pady=20, sticky="ew")

        # Configure button frame grid
        for i in range(4):
            buttonFrame.grid_columnconfigure(i, weight=1)

        # Add value button
        addButton = ctk.CTkButton(buttonFrame, text="Add Value",
                                  command=self.addValueToOptionMenu1)
        addButton.grid(row=0, column=0, padx=5, pady=5)

        # Remove value button
        removeButton = ctk.CTkButton(buttonFrame, text="Remove Value",
                                     command=self.removeValueFromOptionMenu1)
        removeButton.grid(row=0, column=1, padx=5, pady=5)

        # Clear selection button
        clearButton = ctk.CTkButton(buttonFrame, text="Clear All Selections",
                                    command=self.clearAllSelections)
        clearButton.grid(row=0, column=2, padx=5, pady=5)

        # Disable/Enable toggle
        self.toggleButton = ctk.CTkButton(buttonFrame, text="Disable OptionMenu 2",
                                          command=self.toggleOptionMenu2)
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
    def onOptionMenu1Select(self, choice):
        """Handle OptionMenu 1 selection."""
        self.logMessage(f"📊 OptionMenu 1 selection changed: '{choice}'")

    def onOptionMenu2Select(self, choice):
        """Handle OptionMenu 2 selection."""
        self.logMessage(f"🎨 OptionMenu 2 color selected: '{choice}'")

    def onOptionMenu3Select(self, choice):
        """Handle OptionMenu 3 selection."""
        self.logMessage(f"💻 OptionMenu 3 language changed: '{choice}'")

    def onOptionMenu4Select(self, choice):
        """Handle OptionMenu 4 selection."""
        self.logMessage(f"⚠️  OptionMenu 4 priority level: '{choice}'")

    # Control button handlers
    def addValueToOptionMenu1(self):
        """Add a new value to OptionMenu 1."""
        currentValues = self.optionMenu1.cget("values")
        newValue = f"Option {len(currentValues) + 1}"
        
        # Update values
        newValues = list(currentValues) + [newValue]
        self.optionMenu1.configure(values=newValues)
        
        self.logMessage(f"➕ Added new value to OptionMenu 1: '{newValue}'")

    def removeValueFromOptionMenu1(self):
        """Remove the last value from OptionMenu 1."""
        currentValues = self.optionMenu1.cget("values")
        if len(currentValues) > 1:  # Keep at least one option
            removedValue = currentValues[-1]
            newValues = list(currentValues)[:-1]
            self.optionMenu1.configure(values=newValues)
            self.logMessage(f"➖ Removed value from OptionMenu 1: '{removedValue}'")
        else:
            self.logMessage("❌ Cannot remove the last option from OptionMenu 1")

    def clearAllSelections(self):
        """Clear selections from all OptionMenus."""
        # Get current values to reset to first option
        values1 = self.optionMenu1.cget("values")
        values2 = self.optionMenu2.cget("values")
        values3 = self.optionMenu3.cget("values")
        values4 = self.optionMenu4.cget("values")
        
        if values1:
            self.optionMenu1.set(values1[0])
        if values2:
            self.optionMenu2.set(values2[0])
        if values3:
            self.optionMenu3.set(values3[0])
        if values4:
            self.optionMenu4.set(values4[0])
            
        self.logMessage("🔄 All OptionMenu selections cleared and reset to first option")

    def toggleOptionMenu2(self):
        """Toggle OptionMenu 2 enabled/disabled state."""
        currentState = self.optionMenu2.cget("state")
        if currentState == "normal":
            self.optionMenu2.configure(state="disabled")
            self.toggleButton.configure(text="Enable OptionMenu 2")
            self.logMessage("🔒 OptionMenu 2 disabled")
        else:
            self.optionMenu2.configure(state="normal")
            self.toggleButton.configure(text="Disable OptionMenu 2")
            self.logMessage("🔓 OptionMenu 2 enabled")


def main():
    """Main function to run the OptionMenu example."""
    app = OptionMenuExample()
    app.mainloop()


if __name__ == "__main__":
    main()
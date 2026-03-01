import customtkinter as ctk
from tomwidgets import InputBar


class InputBarExample(ctk.CTk):
    """Main application class for InputBar example."""

    def __init__(self):
        """Initialize the application."""
        super().__init__()

        self.title("InputBar Example - tomwidgets")
        self.geometry("600x500")

        # Configure grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)  # Title
        self.grid_rowconfigure(1, weight=0)  # InputBars
        self.grid_rowconfigure(2, weight=0)  # Control buttons
        self.grid_rowconfigure(3, weight=1)   # Log area

        self.setupUi()

    def setupUi(self):
        """Setup the user interface."""
        # Title label
        titleLabel = ctk.CTkLabel(self, text="InputBar Widget Example",
                                  font=ctk.CTkFont(size=20, weight="bold"))
        titleLabel.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

        # InputBars frame
        inputFrame = ctk.CTkFrame(self)
        inputFrame.grid(row=1, column=0, padx=20, pady=10, sticky="ew")
        inputFrame.grid_columnconfigure(0, weight=1)

        # Create InputBar widgets
        self.createInputBars(inputFrame)

        # Control buttons
        self.addControlButtons()

        # Log area
        self.setupLogArea()

    def createInputBars(self, parent):
        """Create and configure InputBar widgets."""
        # InputBar 1: Basic usage
        self.inputBar1 = InputBar(parent, title="Name:", default="John Doe")
        self.inputBar1.grid(row=0, column=0, padx=20, pady=10, sticky="ew")

        # InputBar 2: With custom styling
        self.inputBar2 = InputBar(parent, title="Email:", default="example@email.com")
        self.inputBar2.grid(row=1, column=0, padx=20, pady=10, sticky="ew")
        
        # Configure custom styling
        self.inputBar2.configInput(width=200, placeholder_text="Enter email address")
        self.inputBar2.configLabel(font=ctk.CTkFont(weight="bold"))

        # InputBar 3: Empty initially
        self.inputBar3 = InputBar(parent, title="Message:")
        self.inputBar3.grid(row=2, column=0, padx=20, pady=10, sticky="ew")
        self.inputBar3.configInput(placeholder_text="Type your message here...")

        # Bind event handlers
        self.bindEventHandlers()

    def bindEventHandlers(self):
        """Bind event handlers to InputBar widgets."""
        # InputBar 1: Basic event handling
        self.inputBar1.bindReturn(self.onInputBar1Enter)

        # InputBar 2: Multiple event handlers
        self.inputBar2.bindReturn(self.onInputBar2Enter)
        self.inputBar2.bindReturn(self.onInputBar2Log)

        # InputBar 3: Event with data processing
        self.inputBar3.bindReturn(self.onInputBar3Enter)

    def addControlButtons(self):
        """Add control buttons for dynamic operations."""
        buttonFrame = ctk.CTkFrame(self)
        buttonFrame.grid(row=2, column=0, padx=20, pady=20, sticky="ew")

        # Configure button frame grid
        for i in range(4):
            buttonFrame.grid_columnconfigure(i, weight=1)

        # Get values button
        getValuesButton = ctk.CTkButton(buttonFrame, text="Get All Values",
                                       command=self.getAllValues)
        getValuesButton.grid(row=0, column=0, padx=5, pady=5)

        # Clear all button
        clearAllButton = ctk.CTkButton(buttonFrame, text="Clear All",
                                      command=self.clearAllInputs)
        clearAllButton.grid(row=0, column=1, padx=5, pady=5)

        # Set default values button
        setDefaultsButton = ctk.CTkButton(buttonFrame, text="Set Defaults",
                                          command=self.setDefaultValues)
        setDefaultsButton.grid(row=0, column=2, padx=5, pady=5)

        # Update title button
        updateTitleButton = ctk.CTkButton(buttonFrame, text="Update Title",
                                         command=self.updateInputBar1Title)
        updateTitleButton.grid(row=0, column=3, padx=5, pady=5)

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
    def onInputBar1Enter(self, event=None):
        """Handle InputBar 1 Enter key press."""
        value = self.inputBar1.getValue()
        title = self.inputBar1.getTitle()
        
        self.logMessage(f"📝 {title} Enter pressed: '{value}'")

    def onInputBar2Enter(self, event=None):
        """Handle InputBar 2 Enter key press (priority 1)."""
        value = self.inputBar2.getValue()
        
        self.logMessage(f"📧 Email entered: '{value}' (Priority 1)")

    def onInputBar2Log(self, event=None):
        """Handle InputBar 2 Enter key press (priority 2)."""
        value = self.inputBar2.getValue()
        
        self.logMessage(f"   → Additional logging for email: '{value}' (Priority 2)")

    def onInputBar3Enter(self, event=None):
        """Handle InputBar 3 Enter key press."""
        value = self.inputBar3.getValue()
        
        if value:
            self.logMessage(f"💬 Message submitted: '{value}'")
            # Clear after submission
            self.inputBar3.clear()
        else:
            self.logMessage("⚠️ Please enter a message before submitting")

    # Control button handlers
    def getAllValues(self):
        """Get and display all current values."""
        values = {
            self.inputBar1.getTitle(): self.inputBar1.getValue(),
            self.inputBar2.getTitle(): self.inputBar2.getValue(),
            self.inputBar3.getTitle(): self.inputBar3.getValue()
        }
        
        self.logMessage("📊 Current values:")
        for title, value in values.items():
            self.logMessage(f"   {title} {value}")

    def clearAllInputs(self):
        """Clear all input fields."""
        self.inputBar1.clear()
        self.inputBar2.clear()
        self.inputBar3.clear()
        
        self.logMessage("🧹 All input fields cleared")

    def setDefaultValues(self):
        """Set default values for all input fields."""
        self.inputBar1.setValue("John Doe")
        self.inputBar2.setValue("example@email.com")
        self.inputBar3.setValue("")
        
        self.logMessage("🔄 Default values set")

    def updateInputBar1Title(self):
        """Update the title of InputBar 1."""
        import random
        new_titles = ["Full Name:", "Your Name:", "Name Input:", "Personal Name:"]
        new_title = random.choice(new_titles)
        
        self.inputBar1.setTitle(new_title)
        self.logMessage(f"🏷️ InputBar 1 title updated to: '{new_title}'")


def main():
    """Main function to run the example."""
    app = InputBarExample()
    app.mainloop()


if __name__ == "__main__":
    main()

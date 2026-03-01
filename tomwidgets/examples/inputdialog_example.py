import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import customtkinter as ctk
from tomwidgets.widget.basic.InputDialog import InputDialog


class InputDialogExample(ctk.CTk):
    """Main application class for InputDialog example."""

    def __init__(self):
        """Initialize the application."""
        super().__init__()

        self.title("InputDialog Example - tomwidgets")
        self.geometry("600x500")

        # Configure grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)  # Title
        self.grid_rowconfigure(1, weight=0)  # Button panel
        self.grid_rowconfigure(2, weight=1)  # Log area

        self.setupUi()

    def setupUi(self):
        """Setup the user interface."""
        # Title label
        titleLabel = ctk.CTkLabel(self, text="InputDialog Widget Example",
                                  font=ctk.CTkFont(size=20, weight="bold"))
        titleLabel.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

        # Button panel frame
        buttonFrame = ctk.CTkFrame(self)
        buttonFrame.grid(row=1, column=0, padx=20, pady=10, sticky="ew")
        buttonFrame.grid_columnconfigure(0, weight=1)

        # Create demo buttons
        self.createDemoButtons(buttonFrame)

        # Log area
        self.setupLogArea()

    def createDemoButtons(self, parent):
        """Create buttons for different InputDialog demonstrations."""
        # Configure button frame grid
        for i in range(3):
            parent.grid_columnconfigure(i, weight=1)

        # Basic input dialog
        basicButton = ctk.CTkButton(parent, text="Basic Input Dialog",
                                   command=self.showBasicDialog)
        basicButton.grid(row=0, column=0, padx=10, pady=10)

        # Password dialog
        passwordButton = ctk.CTkButton(parent, text="Password Dialog",
                                      command=self.showPasswordDialog)
        passwordButton.grid(row=0, column=1, padx=10, pady=10)

        # Number input dialog
        numberButton = ctk.CTkButton(parent, text="Number Input Dialog",
                                    command=self.showNumberDialog)
        numberButton.grid(row=0, column=2, padx=10, pady=10)

        # Custom title dialog
        customTitleButton = ctk.CTkButton(parent, text="Custom Title Dialog",
                                         command=self.showCustomTitleDialog)
        customTitleButton.grid(row=1, column=0, padx=10, pady=10)

        # Validation dialog
        validationButton = ctk.CTkButton(parent, text="Validation Dialog",
                                        command=self.showValidationDialog)
        validationButton.grid(row=1, column=1, padx=10, pady=10)

        # Custom buttons dialog
        customButtonsButton = ctk.CTkButton(parent, text="Custom Buttons Dialog",
                                           command=self.showCustomButtonsDialog)
        customButtonsButton.grid(row=1, column=2, padx=10, pady=10)

        # Styled dialog
        styledButton = ctk.CTkButton(parent, text="Styled Dialog",
                                    command=self.showStyledDialog)
        styledButton.grid(row=2, column=0, padx=10, pady=10)

        # Multi-line dialog
        multilineButton = ctk.CTkButton(parent, text="Multi-line Dialog",
                                       command=self.showMultilineDialog)
        multilineButton.grid(row=2, column=1, padx=10, pady=10)

        # Error handling dialog
        errorButton = ctk.CTkButton(parent, text="Error Handling Dialog",
                                   command=self.showErrorHandlingDialog)
        errorButton.grid(row=2, column=2, padx=10, pady=10)

    def setupLogArea(self):
        """Setup the log text area."""
        logFrame = ctk.CTkFrame(self)
        logFrame.grid(row=2, column=0, padx=20, pady=20, sticky="nsew")

        # Log title
        logTitle = ctk.CTkLabel(logFrame, text="Dialog Results:",
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

    # Dialog demonstration methods
    def showBasicDialog(self):
        """Show a basic input dialog."""
        dialog = InputDialog(text="Please enter your name:",
                            title="Basic Input Dialog")
        result = dialog.get_input()
        
        if result:
            self.logMessage(f"✅ Basic Dialog: User entered '{result}'")
        else:
            self.logMessage("❌ Basic Dialog: User cancelled")

    def showPasswordDialog(self):
        """Show a password input dialog."""
        dialog = InputDialog(text="Enter your password:",
                            title="Password Dialog")
        result = dialog.get_input()
        
        if result:
            self.logMessage(f"🔒 Password Dialog: Password entered (length: {len(result)})")
        else:
            self.logMessage("❌ Password Dialog: User cancelled")

    def showNumberDialog(self):
        """Show a number input dialog with validation."""
        dialog = InputDialog(text="Enter a number between 1 and 100:",
                            title="Number Input")
        result = dialog.get_input()
        
        if result:
            try:
                number = int(result)
                if 1 <= number <= 100:
                    self.logMessage(f"🔢 Number Dialog: Valid number '{number}'")
                else:
                    self.logMessage(f"⚠️  Number Dialog: Number '{number}' out of range")
            except ValueError:
                self.logMessage(f"❌ Number Dialog: Invalid number '{result}'")
        else:
            self.logMessage("❌ Number Dialog: User cancelled")

    def showCustomTitleDialog(self):
        """Show a dialog with custom title and text."""
        dialog = InputDialog(text="This is a custom dialog with a longer description text that explains what information we need from the user.",
                            title="Custom Title Dialog - User Information")
        result = dialog.get_input()
        
        if result:
            self.logMessage(f"📝 Custom Title Dialog: User entered '{result}'")
        else:
            self.logMessage("❌ Custom Title Dialog: User cancelled")

    def showValidationDialog(self):
        """Show a dialog with input validation."""
        dialog = InputDialog(text="Enter an email address:",
                            title="Email Validation")
        result = dialog.get_input()
        
        if result:
            if "@" in result and "." in result:
                self.logMessage(f"📧 Validation Dialog: Valid email '{result}'")
            else:
                self.logMessage(f"⚠️  Validation Dialog: Invalid email format '{result}'")
        else:
            self.logMessage("❌ Validation Dialog: User cancelled")

    def showCustomButtonsDialog(self):
        """Show a dialog with custom button labels."""
        # Note: CTkInputDialog doesn't support custom button labels by default
        # This is a demonstration of how it would work if supported
        dialog = InputDialog(text="Do you want to proceed?",
                            title="Confirmation Dialog")
        result = dialog.get_input()
        
        if result:
            self.logMessage(f"✅ Custom Buttons Dialog: User confirmed with '{result}'")
        else:
            self.logMessage("❌ Custom Buttons Dialog: User cancelled")

    def showStyledDialog(self):
        """Show a styled input dialog."""
        dialog = InputDialog(text="Enter your favorite color:",
                            title="Styled Dialog",
                            fg_color="#2b2b2b",
                            button_fg_color="#3b8ed0",
                            button_hover_color="#36719f")
        result = dialog.get_input()
        
        if result:
            self.logMessage(f"🎨 Styled Dialog: Favorite color is '{result}'")
        else:
            self.logMessage("❌ Styled Dialog: User cancelled")

    def showMultilineDialog(self):
        """Show a dialog for multi-line input."""
        dialog = InputDialog(text="Enter a multi-line description:",
                            title="Multi-line Input")
        result = dialog.get_input()
        
        if result:
            lines = result.split('\n')
            line_count = len(lines)
            self.logMessage(f"📄 Multi-line Dialog: {line_count} lines entered")
            if line_count > 1:
                self.logMessage(f"   → First line: '{lines[0]}'")
        else:
            self.logMessage("❌ Multi-line Dialog: User cancelled")

    def showErrorHandlingDialog(self):
        """Show a dialog with error handling."""
        try:
            dialog = InputDialog(text="This demonstrates error handling:",
                                title="Error Handling Demo")
            result = dialog.get_input()
            
            if result:
                self.logMessage(f"✅ Error Handling Dialog: Success with '{result}'")
            else:
                self.logMessage("❌ Error Handling Dialog: User cancelled")
                
        except Exception as e:
            self.logMessage(f"💥 Error Handling Dialog: Exception occurred - {str(e)}")

    def showAllDialogsSequence(self):
        """Show a sequence of different dialogs (for demonstration)."""
        self.logMessage("🚀 Starting dialog sequence...")
        
        # This would be called programmatically to demonstrate multiple dialogs
        # In a real application, you might chain dialogs based on user input


def main():
    """Main function to run the InputDialog example."""
    app = InputDialogExample()
    app.mainloop()


if __name__ == "__main__":
    main()
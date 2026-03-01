import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import customtkinter as ctk
from tomwidgets.widget.InputBox import InputBox, showTextInput, showPasswordInput, showNumberInput


class InputBoxExample(ctk.CTk):
    """Main application class for InputBox example."""

    def __init__(self):
        """Initialize the application."""
        super().__init__()

        self.title("InputBox Example - tomwidgets")
        self.geometry("700x600")
        self.minsize(600, 500)

        # Configure grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)  # Title
        self.grid_rowconfigure(1, weight=0)  # Description
        self.grid_rowconfigure(2, weight=0)  # Button panel
        self.grid_rowconfigure(3, weight=1)  # Log area

        self.setupUi()

    def setupUi(self):
        """Setup the user interface."""
        # Title label
        titleLabel = ctk.CTkLabel(self, text="InputBox Widget Example",
                                  font=ctk.CTkFont(size=22, weight="bold"))
        titleLabel.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="ew")

        # Description label
        descLabel = ctk.CTkLabel(self, 
                                text="Enhanced input dialog with support for text, password, number inputs and validation",
                                font=ctk.CTkFont(size=12))
        descLabel.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="ew")

        # Button panel frame
        buttonFrame = ctk.CTkFrame(self)
        buttonFrame.grid(row=2, column=0, padx=20, pady=10, sticky="ew")
        buttonFrame.grid_columnconfigure(0, weight=1)

        # Create demo buttons
        self.createDemoButtons(buttonFrame)

        # Log area
        self.setupLogArea()

    def createDemoButtons(self, parent):
        """Create buttons for different InputBox demonstrations."""
        # Configure button frame grid
        for i in range(3):
            parent.grid_columnconfigure(i, weight=1)

        # Row 1: Basic input types
        basicButton = ctk.CTkButton(parent, text="Basic Text Input",
                                   command=self.showBasicTextInput)
        basicButton.grid(row=0, column=0, padx=10, pady=10)

        passwordButton = ctk.CTkButton(parent, text="Password Input",
                                      command=self.showPasswordInput)
        passwordButton.grid(row=0, column=1, padx=10, pady=10)

        numberButton = ctk.CTkButton(parent, text="Number Input",
                                    command=self.showNumberInput)
        numberButton.grid(row=0, column=2, padx=10, pady=10)

        # Row 2: Advanced features
        rangeButton = ctk.CTkButton(parent, text="Number Range Validation",
                                   command=self.showNumberRangeInput)
        rangeButton.grid(row=1, column=0, padx=10, pady=10)

        customValidationButton = ctk.CTkButton(parent, text="Custom Validation",
                                              command=self.showCustomValidation)
        customValidationButton.grid(row=1, column=1, padx=10, pady=10)

        emptyValidationButton = ctk.CTkButton(parent, text="Required Field",
                                             command=self.showRequiredField)
        emptyValidationButton.grid(row=1, column=2, padx=10, pady=10)

        # Row 3: Convenience functions
        convenienceTextButton = ctk.CTkButton(parent, text="Convenience Text",
                                            command=self.showConvenienceText)
        convenienceTextButton.grid(row=2, column=0, padx=10, pady=10)

        conveniencePasswordButton = ctk.CTkButton(parent, text="Convenience Password",
                                                 command=self.showConveniencePassword)
        conveniencePasswordButton.grid(row=2, column=1, padx=10, pady=10)

        convenienceNumberButton = ctk.CTkButton(parent, text="Convenience Number",
                                               command=self.showConvenienceNumber)
        convenienceNumberButton.grid(row=2, column=2, padx=10, pady=10)

        # Row 4: Advanced usage
        styledButton = ctk.CTkButton(parent, text="Styled InputBox",
                                    command=self.showStyledInputBox)
        styledButton.grid(row=3, column=0, padx=10, pady=10)

        errorHandlingButton = ctk.CTkButton(parent, text="Error Handling",
                                           command=self.showErrorHandling)
        errorHandlingButton.grid(row=3, column=1, padx=10, pady=10)

        sequenceButton = ctk.CTkButton(parent, text="Input Sequence",
                                      command=self.showInputSequence)
        sequenceButton.grid(row=3, column=2, padx=10, pady=10)

    def setupLogArea(self):
        """Setup the log text area."""
        logFrame = ctk.CTkFrame(self)
        logFrame.grid(row=3, column=0, padx=20, pady=20, sticky="nsew")

        # Log title
        logTitle = ctk.CTkLabel(logFrame, text="InputBox Results:",
                                font=ctk.CTkFont(weight="bold"))
        logTitle.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        # Clear log button
        clearButton = ctk.CTkButton(logFrame, text="Clear Log", 
                                   command=self.clearLog, width=80)
        clearButton.grid(row=0, column=1, padx=10, pady=10, sticky="e")

        # Log text area
        self.logText = ctk.CTkTextbox(logFrame, height=250)
        self.logText.grid(row=1, column=0, columnspan=2, padx=10,
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

    def clearLog(self):
        """Clear the log area."""
        self.logText.delete("1.0", "end")

    # InputBox demonstration methods
    def showBasicTextInput(self):
        """Show a basic text input dialog using InputBox."""
        dialog = InputBox(title="Basic Text Input", 
                         text="Please enter your name:",
                         inputType='text')
        result = dialog.showInputBox()
        
        if result is not None:
            self.logMessage(f"✅ Basic Text: User entered '{result}'")
        else:
            self.logMessage("❌ Basic Text: User cancelled")

    def showPasswordInput(self):
        """Show a password input dialog."""
        dialog = InputBox(title="Password Input",
                         text="Enter your password:",
                         inputType='password')
        result = dialog.showInputBox()
        
        if result is not None:
            masked_password = '*' * len(result)
            self.logMessage(f"🔒 Password: Password entered '{masked_password}({result})' (length: {len(result)})")
        else:
            self.logMessage("❌ Password: User cancelled")

    def showNumberInput(self):
        """Show a number input dialog."""
        dialog = InputBox(title="Number Input",
                         text="Enter a number:",
                         inputType='number')
        result = dialog.showInputBox()
        
        if result is not None:
            self.logMessage(f"🔢 Number: User entered {result} (type: {type(result).__name__})")
        else:
            self.logMessage("❌ Number: User cancelled")

    def showNumberRangeInput(self):
        """Show a number input dialog with range validation."""
        dialog = InputBox(title="Number Range Validation",
                         text="Enter a number between 1 and 100:",
                         inputType='number',
                         minValue=1,
                         maxValue=100)
        result = dialog.showInputBox()
        
        if result is not None:
            self.logMessage(f"🎯 Range Validation: Valid number '{result}' (1-100)")
        else:
            self.logMessage("❌ Range Validation: Invalid number or cancelled")

    def showCustomValidation(self):
        """Show input with custom validation."""
        def validateEmail(email):
            return '@' in email and '.' in email and len(email) > 5
        
        dialog = InputBox(title="Email Validation",
                         text="Enter your email address:",
                         inputType='text',
                         validationCallback=validateEmail)
        result = dialog.showInputBox()
        
        if result is not None:
            self.logMessage(f"📧 Custom Validation: Valid email '{result}'")
        else:
            self.logMessage("❌ Custom Validation: Invalid email format or cancelled")

    def showRequiredField(self):
        """Show a required field input (empty not allowed)."""
        dialog = InputBox(title="Required Field",
                         text="This field is required:",
                         inputType='text',
                         allowEmpty=False)
        result = dialog.showInputBox()
        
        if result is not None:
            self.logMessage(f"⭐ Required Field: User entered '{result}'")
        else:
            self.logMessage("❌ Required Field: Field cannot be empty")

    def showConvenienceText(self):
        """Show text input using convenience function."""
        result = showTextInput(title="Convenience Text", 
                              text="Enter some text using convenience function:")
        
        if result is not None:
            self.logMessage(f"🚀 Convenience Text: '{result}'")
        else:
            self.logMessage("❌ Convenience Text: Cancelled")

    def showConveniencePassword(self):
        """Show password input using convenience function."""
        result = showPasswordInput(title="Convenience Password",
                                  text="Enter password using convenience function:")
        
        if result is not None:
            masked = '*' * len(result)
            self.logMessage(f"🚀 Convenience Password: '{masked}' (length: {len(result)})")
        else:
            self.logMessage("❌ Convenience Password: Cancelled")

    def showConvenienceNumber(self):
        """Show number input using convenience function."""
        result = showNumberInput(title="Convenience Number",
                                text="Enter number (10-50) using convenience function:",
                                minValue=10,
                                maxValue=50)
        
        if result is not None:
            self.logMessage(f"🚀 Convenience Number: {result} (10-50)")
        else:
            self.logMessage("❌ Convenience Number: Invalid or cancelled")

    def showStyledInputBox(self):
        """Show a styled InputBox."""
        dialog = InputBox(title="Styled InputBox",
                         text="Enter your favorite color:",
                         inputType='text',
                         fg_color="#2b2b2b",
                         button_fg_color="#3b8ed0",
                         button_hover_color="#36719f")
        result = dialog.showInputBox()
        
        if result is not None:
            self.logMessage(f"🎨 Styled InputBox: Favorite color is '{result}'")
        else:
            self.logMessage("❌ Styled InputBox: User cancelled")

    def showErrorHandling(self):
        """Demonstrate error handling with InputBox."""
        try:
            dialog = InputBox(title="Error Handling Demo",
                             text="This demonstrates robust error handling:",
                             inputType='number',
                             minValue=0,
                             maxValue=1000)
            result = dialog.showInputBox()
            
            if result is not None:
                self.logMessage(f"✅ Error Handling: Success with value {result}")
            else:
                self.logMessage("❌ Error Handling: User cancelled or invalid input")
                
        except Exception as e:
            self.logMessage(f"💥 Error Handling: Exception occurred - {str(e)}")

    def showInputSequence(self):
        """Show a sequence of different input types."""
        self.logMessage("🚀 Starting input sequence...")
        
        # Simulate a user registration sequence
        name = showTextInput("User Registration", "Enter your full name:")
        if name is None:
            self.logMessage("❌ Registration cancelled at name step")
            return
            
        email = showTextInput("User Registration", "Enter your email:")
        if email is None:
            self.logMessage("❌ Registration cancelled at email step")
            return
            
        age = showNumberInput("User Registration", "Enter your age:", 1, 120)
        if age is None:
            self.logMessage("❌ Registration cancelled at age step")
            return
            
        password = showPasswordInput("User Registration", "Create a password:")
        if password is None:
            self.logMessage("❌ Registration cancelled at password step")
            return
            
        self.logMessage(f"🎉 Registration Complete!")
        self.logMessage(f"   👤 Name: {name}")
        self.logMessage(f"   📧 Email: {email}")
        self.logMessage(f"   🔢 Age: {age}")
        self.logMessage(f"   🔒 Password: {'*' * len(password)}")


def main():
    """Main function to run the InputBox example."""
    app = InputBoxExample()
    app.mainloop()


if __name__ == "__main__":
    main()
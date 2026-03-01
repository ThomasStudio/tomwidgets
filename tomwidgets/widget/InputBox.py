"""
InputBox Widget
================

A enhanced input dialog widget based on basic.InputDialog with support for
various input types including string, number, password, and validation.

Features:
- Support for different input types (text, password, number)
- Input validation and error handling
- Customizable input constraints
- Enhanced user experience with better feedback
"""

from dataclasses import dataclass

from .basic import InputDialog


@dataclass
class Type:
    Password = "password"
    Number = "number"
    Text = "text"


class InputBox(InputDialog):
    """Enhanced input dialog with support for various input types and validation."""

    def __init__(self, **kwargs):
        """
        Initialize the InputBox.

        Args:
            master: Parent widget
            **kwargs: Additional arguments including:
                - inputType: Type of input ('text', 'password', 'number')
                - minValue: Minimum value for number input
                - maxValue: Maximum value for number input
                - allowEmpty: Whether empty input is allowed
                - validationCallback: Custom validation function
        """
        self.inputType = kwargs.pop('inputType', Type.Text)
        self.minValue = kwargs.pop('minValue', None)
        self.maxValue = kwargs.pop('maxValue', None)
        self.allowEmpty = kwargs.pop('allowEmpty', True)
        self.validationCallback = kwargs.pop('validationCallback', None)

        super().__init__(**kwargs)

        # Configure based on input type
        self.after(20, self.configureInputType)

    def configureInputType(self):
        self.entry = self._entry

        """Configure the input field based on the input type."""
        if self.inputType == Type.Password:
            # Configure for password input (show asterisks)
            self.entry.configure(show='*')
        elif self.inputType == Type.Number:
            # Configure for number input
            self.entry.configure(validate='key')
            self.entry.configure(validatecommand=(
                self.register(self.validateNumberInput), '%P'))

    def validateNumberInput(self, value):
        """Validate number input."""
        if value == "":
            return self.allowEmpty

        try:
            number = float(value)
            if self.minValue is not None and number < self.minValue:
                return False
            if self.maxValue is not None and number > self.maxValue:
                return False
            return True
        except ValueError:
            return False

    def getInputValue(self):
        """
        Get the input value with proper type conversion.

        Returns:
            The input value with appropriate type (str, int, float)
        """
        result = self.get_input()

        if result is None:
            return None

        if self.inputType == 'number' and result:
            try:
                if '.' in result:
                    return float(result)
                else:
                    return int(result)
            except ValueError:
                return result  # Return as string if conversion fails

        return result

    def showInputBox(self):
        """
        Show the input box and return the validated result.

        Returns:
            Validated input value or None if cancelled
        """
        result = self.getInputValue()

        # Apply custom validation if provided
        if result is not None and self.validationCallback:
            if not self.validationCallback(result):
                return None

        return result

    def setInputType(self, inputType):
        """
        Set the input type.

        Args:
            inputType: Type of input ('text', 'password', 'number')
        """
        self.inputType = inputType
        self.configureInputType()

    def setNumberRange(self, minValue=None, maxValue=None):
        """
        Set the valid range for number input.

        Args:
            minValue: Minimum allowed value
            maxValue: Maximum allowed value
        """
        self.minValue = minValue
        self.maxValue = maxValue

    def setValidationCallback(self, callback):
        """
        Set a custom validation callback.

        Args:
            callback: Function that takes input value and returns boolean
        """
        self.validationCallback = callback


# Convenience functions for common use cases
def showTextInput(title="Input", text="Enter text:", **kwargs):
    """Show a text input dialog."""
    dialog = InputBox(title=title, text=text, inputType='text', **kwargs)
    return dialog.showInputBox()


def showPasswordInput(title="Password", text="Enter password:", **kwargs):
    """Show a password input dialog."""
    dialog = InputBox(title=title, text=text,
                      inputType=Type.Password, **kwargs)
    return dialog.showInputBox()


def showNumberInput(title="Number", text="Enter number:", minValue=None, maxValue=None, **kwargs):
    """Show a number input dialog."""
    dialog = InputBox(title=title, text=text, inputType=Type.Number,
                      minValue=minValue, maxValue=maxValue, **kwargs)
    return dialog.showInputBox()

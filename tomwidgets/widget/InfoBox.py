import customtkinter as ctk
from .basic import Toplevel, Button, Label, Frame, Textbox
from typing import Optional, Callable


class InfoBox(Toplevel):
    """
    A customizable message box dialog widget.

    Features:
    - Custom title and message
    - Confirm button with customizable text
    - Modal dialog behavior
    - Custom styling options
    - Callback support for button actions
    """

    def __init__(self, master=None, title: str = "Message", message: str = "",
                 buttonText: str = "OK", buttonCallback: Optional[Callable] = None,
                 **kwargs):
        """
        Initialize the MessageBox widget.

        Args:
            master: The parent widget
            title: The dialog title
            message: The message text to display
            buttonText: Text for the confirm button
            buttonCallback: Callback function for button click
            **kwargs: Additional arguments for Toplevel
        """
        super().__init__(master, **kwargs)

        self.titleText = title
        self.messageText = message
        self.buttonText = buttonText
        self.buttonCallback = buttonCallback

        # Dialog state
        self.result = None

        # Configure the dialog window
        self.setupDialog()

        # Create UI
        self.setupUi()

    def setupDialog(self):
        """Configure the dialog window properties."""
        self.title(self.titleText)
        self.geometry("400x200")
        self.resizable(False, False)

        # Make dialog modal
        self.transient(self.master)
        self.grab_set()

    def setupUi(self):
        """Setup the message box user interface."""
        # Main frame
        self.mainFrame = Frame(self)
        self.mainFrame.pack(fill="both", expand=True, padx=20, pady=20)

        # Configure grid weights
        self.mainFrame.grid_columnconfigure(0, weight=1)
        self.mainFrame.grid_rowconfigure(1, weight=1)  # Message area

        # Title label
        self.titleLabel = Label(self.mainFrame, text=self.titleText,
                                font=ctk.CTkFont(size=16, weight="bold"))
        self.titleLabel.grid(row=0, column=0, padx=10,
                             pady=(0, 10), sticky="w")

        # Message label
        self.messageLabel = Textbox(self.mainFrame, height=4,
                                    font=ctk.CTkFont(size=12),
                                    wrap="word")
        self.messageLabel.insert("1.0", self.messageText)
        self.messageLabel.configure(state="disabled")  # Make it read-only like a label
        self.messageLabel.grid(row=1, column=0, padx=10,
                               pady=10, sticky="nsew")

        # Button frame
        self.buttonFrame = Frame(self.mainFrame)
        self.buttonFrame.grid(row=2, column=0, padx=10,
                              pady=(10, 0), sticky="e")

        # Confirm button
        self.confirmButton = Button(self.buttonFrame, text=self.buttonText,
                                    command=self.onConfirmButtonClick)
        self.confirmButton.pack(side="right", padx=(10, 0))

    def onConfirmButtonClick(self):
        """Handle confirm button click."""
        self.result = True

        if self.buttonCallback:
            self.buttonCallback()

        self.destroy()

    def show(self):
        """Show the message box dialog."""
        self.wait_window()

    def setTitle(self, title: str):
        """
        Set the dialog title.

        Args:
            title: New title text
        """
        self.titleText = title
        self.title(title)
        self.titleLabel.configure(text=title)

    def setMessage(self, message: str):
        """
        Set the message text.

        Args:
            message: New message text
        """
        self.messageText = message
        # Enable textbox to modify content, then disable again
        self.messageLabel.configure(state="normal")
        self.messageLabel.delete("1.0", "end")
        self.messageLabel.insert("1.0", message)
        self.messageLabel.configure(state="disabled")

    def setButtonText(self, buttonText: str):
        """
        Set the confirm button text.

        Args:
            buttonText: New button text
        """
        self.buttonText = buttonText
        self.confirmButton.configure(text=buttonText)

    def setButtonCallback(self, callback: Optional[Callable]):
        """
        Set the button click callback.

        Args:
            callback: Callback function
        """
        self.buttonCallback = callback

    def getResult(self) -> Optional[bool]:
        """
        Get the dialog result.

        Returns:
            True if confirmed, None if not shown or cancelled
        """
        return self.result


def showMessageBox(master=None, title: str = "Message", message: str = "",
                   buttonText: str = "OK", buttonCallback: Optional[Callable] = None,
                   **kwargs) -> InfoBox:
    """
    Convenience function to create and show a message box.

    Args:
        master: The parent widget
        title: The dialog title
        message: The message text to display
        buttonText: Text for the confirm button
        buttonCallback: Callback function for button click
        **kwargs: Additional arguments for MessageBox

    Returns:
        The created MessageBox instance
    """
    messageBox = InfoBox(master, title, message,
                            buttonText, buttonCallback, **kwargs)
    messageBox.show()
    return messageBox
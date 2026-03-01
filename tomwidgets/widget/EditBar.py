import customtkinter as ctk
from .basic import Frame, Label, Entry, InputDialog, Toplevel
from .BtnBar import BtnBar, BtnConfig
from typing import Optional, Callable

ChangeIcon = "✏"
DelIcon = "✕"


class EditBar(Frame):
    """
    A widget that displays a labeled input field with edit and remove buttons.

    Features:
    - Title label
    - Configurable read-only input field
    - Edit button to modify the value
    - Remove button to delete the entry
    - Callback support for edit and remove actions
    """

    def __init__(self, master, title: str = "", defaultValue: str = "",
                 readonly: bool = True,
                 editCallback: Optional[Callable[[str], None]] = None,
                 removeCallback: Optional[Callable[[], bool]] = None,
                 **kwargs):
        """
        Initialize the EditBar widget.

        Args:
            master: The parent widget
            title: The title text for the label
            defaultValue: Initial value for the input field
            readonly: Whether the input field should be read-only (default True)
            editCallback: Callback function called when edit is completed (receives new value)
            removeCallback: Callback function called when remove is completed
            **kwargs: Additional arguments for Frame
        """
        super().__init__(master, **kwargs)

        self.history = []

        self.title = title
        self.readonly = readonly
        self.editCallback = editCallback
        self.removeCallback = removeCallback
        self.currentValue = defaultValue

        # Configure the layout
        self.grid_columnconfigure(1, weight=1)

        # Create UI components
        self.titleLabel = Label(self, text=self.title)
        self.titleLabel.grid(row=0, column=0, padx=(0, 10), pady=5, sticky="w")

        # Create input field
        self.inputEntry = Entry(self, width=200)
        self.inputEntry.insert(0, defaultValue)

        # Set readonly state based on parameter
        if readonly:
            self.inputEntry.configure(state="readonly")
        else:
            self.inputEntry.configure(state="normal")

        self.inputEntry.grid(row=0, column=1, sticky="ew", padx=(0, 5))

        # Create button bar with edit and remove buttons
        self.btnBar = BtnBar(self)
        self.btnBar.grid(row=0, column=2, padx=0, pady=5)

        # Configure buttons
        self.setupButtons()

        # Set initial value
        self.setValue(defaultValue)
        self.logValue()

    def logValue(self):
        """Log the current value to history."""
        self.history.append(self.getValue())

    def setupButtons(self):
        self.btnBar.clearBtns()

        """Setup the edit and remove buttons."""
        if self.editCallback:
            removeBtnConfig = BtnConfig(
                name=ChangeIcon,
                callback=self.onEditClick
            )
            self.btnBar.addBtn(removeBtnConfig)

        if self.removeCallback:
            removeBtnConfig = BtnConfig(
                name=DelIcon,
                callback=self.onRemoveClick
            )
            self.btnBar.addBtn(removeBtnConfig)

    def setTitle(self, title: str):
        """
        Set the title of the EditBar.

        Args:
            title: New title text
        """
        self.title = title
        self.titleLabel.configure(text=title)

    def getTitle(self) -> str:
        """
        Get the title of the EditBar.

        Returns:
            Current title text
        """
        return self.title

    def setValue(self, value: str):
        """
        Set the value in the input field.

        Args:
            value: Value to set
        """
        self.currentValue = value
        # Temporarily make the entry writable to update the value
        currentState = self.inputEntry.cget("state")
        self.inputEntry.configure(state="normal")
        self.inputEntry.delete(0, "end")
        self.inputEntry.insert(0, value)
        # Restore the appropriate state
        self.inputEntry.configure(state=currentState)

        self.logValue()

    def getValue(self) -> str:
        """
        Get the current value from the input field.

        Returns:
            Current value in the input field
        """
        return self.currentValue

    def getHistory(self) -> list:
        """Get the history of values set."""
        return self.history

    def setReadonly(self, readonly: bool):
        """Set whether the input field should be readonly."""
        self.readonly = readonly
        if readonly:
            self.inputEntry.configure(state="readonly")
        else:
            self.inputEntry.configure(state="normal")

    def onEditClick(self):
        """Handle the edit button click."""
        # Show input dialog to get new value
        dialog = InputDialog(
            text=f"Enter new value for {self.title}", title="Edit Value")
        newValue = dialog.get_input()

        if newValue is not None and newValue.strip() != "":
            self.setValue(newValue)

            # Call the edit callback if provided
            if self.editCallback:
                self.editCallback(newValue)

    def onRemoveClick(self):
        """Handle the remove button click."""
        # Create a custom confirmation dialog
        confirmWindow = Toplevel(self)
        confirmWindow.title("Confirm Removal")
        confirmWindow.geometry("300x150")
        confirmWindow.resizable(False, False)

        # Center the dialog over parent
        confirmWindow.transient(self)
        confirmWindow.grab_set()

        # Add message
        messageLabel = ctk.CTkLabel(confirmWindow, text="Are you sure you want to remove this item?",
                                    wraplength=250)
        messageLabel.pack(pady=20)

        # Add buttons frame
        buttonFrame = ctk.CTkFrame(confirmWindow)
        buttonFrame.pack(pady=10)

        # Yes and No buttons
        def onYes():
            confirmWindow.destroy()
            self.performRemoval()

        def onNo():
            confirmWindow.destroy()

        yesButton = ctk.CTkButton(buttonFrame, text="Yes", command=onYes)
        yesButton.pack(side="left", padx=5)

        noButton = ctk.CTkButton(buttonFrame, text="No", command=onNo)
        noButton.pack(side="left", padx=5)

        # Focus and bind Enter/Esc keys
        yesButton.focus()
        confirmWindow.bind("<Return>", lambda e: onYes())
        confirmWindow.bind("<Escape>", lambda e: onNo())

    def performRemoval(self):
        """Perform the actual removal action."""
        # Call the remove callback if provided
        shouldRemove = True
        if self.removeCallback:
            shouldRemove = self.removeCallback()

        # If callback returns True or doesn't exist, remove the widget
        if shouldRemove:
            self.destroy()

    def configTitle(self, **kwargs):
        """
        Configure the title label.

        Args:
            **kwargs: Arguments to pass to the label configure method
        """
        self.titleLabel.configure(**kwargs)

    def configInput(self, **kwargs):
        """
        Configure the input entry.

        Args:
            **kwargs: Arguments to pass to the entry configure method
        """
        self.inputEntry.configure(**kwargs)

    def configBtnBar(self, **kwargs):
        """
        Configure the button bar.

        Args:
            **kwargs: Arguments to pass to the button bar configure method
        """
        self.btnBar.configure(**kwargs)

    def isChanged(self) -> bool:
        """
        Check if the current value has changed from the last logged value.

        Returns:
            True if changed, False otherwise
        """
        if not self.history:
            return False

        if len(self.history) < 2:
            return False

        return self.history[-1] != self.history[-2]

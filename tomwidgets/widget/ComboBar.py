"""
ComboBar widget for tomwidgets library.

A combination widget that includes a label as title and a ComboBox.
Generates events when items are selected in the ComboBox.
"""

from .basic import Frame, Label, ComboBox
from typing import List, Callable, Any


class ComboBar(Frame):
    """
    ComboBar widget with title label and ComboBox.

    Features:
    - Title label for identification
    - ComboBox for item selection
    - Event generation on item selection
    - Customizable appearance
    """

    def __init__(self, master: Any, title: str = "", values: List[str] = None, **kwargs):
        """
        Initialize the ComboBar widget.

        Args:
            master: The parent widget
            title: The title text for the label
            values: List of values for the ComboBox
            **kwargs: Additional arguments for Frame
        """
        # Handle values parameter
        if values is None:
            values = []

        # Store parameters before calling super
        self.titleText = title
        self.comboValues = values

        super().__init__(master, **kwargs)
        self.eventName = "selection_changed"

        self.selectedValue = ""

        self.initUi()

    def initUi(self):
        """Setup the user interface components."""
        # Configure grid weights for proper resizing
        self.grid_columnconfigure(0, weight=0)  # Label column
        self.grid_columnconfigure(1, weight=1)  # ComboBox column
        self.grid_rowconfigure(0, weight=1)     # Single row

        # Title label
        self.titleLabel = Label(self, text=self.titleText)
        self.titleLabel.grid(row=0, column=0, padx=(
            10, 5), pady=10, sticky="w")

        # ComboBox
        self.comboBox = ComboBox(self, values=self.comboValues)
        self.comboBox.grid(row=0, column=1, padx=(5, 10), pady=10, sticky="ew")

        # Bind ComboBox selection event
        self.comboBox.configure(command=self.onComboBoxSelect)

    def onComboBoxSelect(self, selectedValue: str):
        """Handle ComboBox selection and generate selection_changed event."""
        oldValue = self.selectedValue
        self.selectedValue = selectedValue

        # Generate event
        self.generateEvent()

    def setTitle(self, title: str):
        """
        Set the title text.

        Args:
            title: The new title text
        """
        self.titleText = title
        self.titleLabel.configure(text=title)

    def getTitle(self) -> str:
        """
        Get the current title text.

        Returns:
            The current title text
        """
        return self.titleText

    def setValues(self, values: List[str]):
        """
        Set the values for the ComboBox.

        Args:
            values: List of values for the ComboBox
        """
        self.comboValues = values
        self.comboBox.configure(values=values)

    def getValues(self) -> List[str]:
        """
        Get the current ComboBox values.

        Returns:
            List of current values
        """
        return self.comboValues

    def setSelectedValue(self, value: str):
        """
        Set the selected value in the ComboBox.

        Args:
            value: The value to select
        """
        if value in self.comboValues:
            self.comboBox.set(value)
            self.selectedValue = value

    def getSelectedValue(self) -> str:
        """
        Get the currently selected value.

        Returns:
            The selected value
        """
        return self.selectedValue

    def getText(self):
        return self.comboBox.get()

    def clearSelection(self):
        """Clear the current selection."""
        self.comboBox.set("")
        self.selectedValue = ""

    def addValue(self, value: str):
        """
        Add a value to the ComboBox.

        Args:
            value: The value to add
        """
        if value not in self.comboValues:
            self.comboValues.append(value)
            self.comboBox.configure(values=self.comboValues)

    def removeValue(self, value: str) -> bool:
        """
        Remove a value from the ComboBox.

        Args:
            value: The value to remove

        Returns:
            True if value was removed, False if not found
        """
        if value in self.comboValues:
            self.comboValues.remove(value)
            self.comboBox.configure(values=self.comboValues)

            # If removed value was selected, clear selection
            if self.selectedValue == value:
                self.clearSelection()

            return True
        return False

    def bindSelectionChanged(self, callback: Callable):
        """
        Bind a callback to the selection changed event.

        Args:
            callback: The function to call when selection changes
        """
        self.bindEvent(callback)

    def enable(self):
        """Enable the ComboBar (both label and ComboBox)."""
        self.titleLabel.configure(state="normal")
        self.comboBox.configure(state="normal")

    def disable(self):
        """Disable the ComboBar (both label and ComboBox)."""
        self.titleLabel.configure(state="disabled")
        self.comboBox.configure(state="disabled")

    def readOnly(self, readonly: bool = True):
        if readonly:
            self.comboBox.configure(state="readonly")
        else:
            self.comboBox.configure(state="normal")

    def setLabelWidth(self, width: int):
        """
        Set the width of the title label.

        Args:
            width: The width in pixels
        """
        self.titleLabel.configure(width=width)

    def setComboBoxWidth(self, width: int):
        """
        Set the width of the ComboBox.

        Args:
            width: The width in pixels
        """
        self.comboBox.configure(width=width)

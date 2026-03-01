import tkinter as tk
import customtkinter as ctk
from typing import Any

from .basic.Textbox import Textbox


class WrapBox(Textbox):
    """
    A container widget that automatically wraps widgets using basic.Textbox as base class.
    All methods and variables use camelCase naming convention.
    """

    def __init__(self, master: Any, **kwargs):
        super().__init__(master, **kwargs)

        # Track inserted widgets with unique tags
        self._widgets = []
        self._widgetCounter = 0

        # Configure widget appearance based on theme
        self._configureTheme()

    def _configureTheme(self):
        """Configure appearance based on current theme."""
        theme = ctk.get_appearance_mode()
        if theme == "Dark":
            self.configure(
                fg_color="#2c2c2c",
                text_color="#ffffff"
            )
        else:
            self.configure(
                fg_color="#f0f0f0",
                text_color="#000000"
            )

    def addWidget(self, widget: Any, padx: int = 2, pady: int = 2) -> str:
        """
        Add a widget to the end of WrapBox.

        Args:
            widget: Widget to add
            padding: Padding around widget in pixels

        Returns:
            String index where widget was inserted
        """
        return self.insertWidget(tk.END, widget, padx, pady)

    def delWidget(self, widget: Any) -> bool:
        """
        Delete a widget from WrapBox.

        Args:
            widget: Widget to delete

        Returns:
            True if widget was found and deleted, False otherwise
        """

        for i, (tag, w) in enumerate(self._widgets):
            if w == widget:
                # Find the position of this widget in the text widget
                box = self.box()

                # Search through the text widget for the widget
                startPos = "1.0"
                endPos = box.index(tk.END)

                # Look for the widget in the text content
                currentPos = startPos
                while box.compare(currentPos, "<", endPos):
                    # Check if this position contains a window
                    try:
                        window = box.window_cget(currentPos, "window")
                        if window == str(widget):
                            # Found the widget, delete it
                            box.delete(currentPos)
                            print(
                                f"Deleted widget {tag} at position {currentPos}")
                            break
                    except:
                        pass
                    # Move to next position
                    currentPos = box.index(f"{currentPos} + 1 char")

                # Remove from tracking list
                del self._widgets[i]

                return True

        return False

    def insertWidget(self, index: str, widget: Any, padx: int = 2, pady: int = 2) -> str:
        """
        Insert a widget at specified index.

        Args:
            index: Position to insert widget
            widget: Widget to insert
            padx: Padding around widget in pixels horizontally
            pady: Padding around widget in pixels vertically

        Returns:
            String index where widget was actually inserted
        """
        # Insert widget into text widget using parent's addWidget method
        # We need to access the underlying text widget for window operations
        box = self.box()

        # Save current state
        currentState = self.state()
        if currentState == tk.DISABLED:
            self.enable()

        # Create a unique tag for this widget
        widgetTag = f"widget_{self._widgetCounter}"
        self._widgetCounter += 1

        # Insert widget at the specified position with the unique tag
        box.window_create(index, window=widget, padx=padx, pady=pady)

        # Add space after widget for spacing
        box.insert(tk.END, " ")

        # Track widget with its unique tag
        self._widgets.append((widgetTag, widget))

        # Restore original state
        if currentState == tk.DISABLED:
            self.disable()

        return widgetTag

    def getWidgets(self) -> list:
        """
        Get all widgets in WrapBox.

        Returns:
            List of tuples containing (index, widget) pairs
        """
        return self._widgets.copy()

    def clearWidgets(self) -> None:
        """
        Remove all widgets from WrapBox.
        """
        # Get the text widget
        box = self.box()

        # Search through the text widget for all widgets
        startPos = "1.0"
        endPos = box.index(tk.END)

        # Look for widgets in the text content
        currentPos = startPos
        while box.compare(currentPos, "<", endPos):
            # Check if this position contains a window
            try:
                window = box.window_cget(currentPos, "window")
                if window:
                    # Found a widget, delete it
                    box.delete(currentPos)
                    # Don't advance position since we deleted a character
                    continue
            except:
                pass
            # Move to next position
            currentPos = box.index(f"{currentPos} + 1 char")

        # Clear text content
        self.delete("1.0", tk.END)

        # Clear tracking list
        self._widgets.clear()

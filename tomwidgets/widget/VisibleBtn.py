"""
VisibleBtn Widget
=================

A button widget that can bind and toggle visibility for groups of widgets.
Extends basic.Button with enhanced functionality for managing widget visibility.

Features:
- Bind multiple widgets to a single button
- Toggle visibility of bound widget groups
- Customizable toggle states (show/hide)
- Visual feedback for current state
- Event handling for visibility changes
"""

from .basic import Button, BaseWidget

CollapseIcon = "－"
ExploreIcon = "＋"
BorderWidth = 3
BorderColor = "gold"


class VisibleBtn(Button):
    """Button widget that can toggle visibility of bound widget groups."""

    def __init__(self, master=None, **kwargs):
        """
        Initialize the VisibleBtn.

        Args:
            master: Parent widget
            **kwargs: Additional arguments including:
                - boundWidgets: List of widgets to bind for visibility control
                - defaultState: Initial visibility state ('show' or 'hide')
                - showText: Text to display when widgets are visible
                - hideText: Text to display when widgets are hidden
                - showColor: Button color when showing widgets
                - hideColor: Button color when hiding widgets
        """
        self.boundWidgets: list[BaseWidget] = kwargs.pop('boundWidgets', [])
        self.defaultState = kwargs.pop('defaultState', 'show')
        self.showText = kwargs.pop('showText', CollapseIcon)
        self.hideText = kwargs.pop('hideText', ExploreIcon)
        self.showColor = kwargs.pop('showColor', 'gold')
        self.hideColor = kwargs.pop('hideColor', 'red')

        if "border_width" not in kwargs:
            kwargs["border_width"] = BorderWidth

        # Initialize the base button
        super().__init__(master, **kwargs)

        # Set initial state
        self.isVisible = self.defaultState == 'show'
        self.updateButtonAppearance()

        # Bind the toggle functionality to button click
        self.configure(command=self.toggleVisibility)

    def bindWidgets(self, widgets: list[BaseWidget]):
        """
        Bind a list of widgets to this button for visibility control.

        Args:
            widgets: List of widgets to bind
        """
        self.boundWidgets = widgets
        self.applyVisibilityState()

    def addWidget(self, widget: BaseWidget):
        """
        Add a single widget to the bound widgets list.

        Args:
            widget: Widget to add
        """
        if widget not in self.boundWidgets:
            self.boundWidgets.append(widget)
            self.applyVisibilityState()

    def removeWidget(self, widget: BaseWidget):
        """
        Remove a widget from the bound widgets list.

        Args:
            widget: Widget to remove
        """
        if widget in self.boundWidgets:
            self.boundWidgets.remove(widget)

    def clearWidgets(self):
        """Clear all bound widgets."""
        self.boundWidgets = []

    def toggleVisibility(self):
        """Toggle the visibility state of bound widgets."""
        self.isVisible = not self.isVisible
        self.applyVisibilityState()
        self.updateButtonAppearance()

    def applyVisibilityState(self):
        """Apply the current visibility state to all bound widgets."""
        for widget in self.boundWidgets:
            if widget and widget.winfo_exists():
                if self.isVisible:
                    widget.show()
                else:
                    widget.hide()

    def updateButtonAppearance(self):
        """Update button text and color based on current state."""
        if self.isVisible:
            self.configure(text=self.showText, text_color=self.showColor)
        else:
            self.configure(text=self.hideText, text_color=self.hideColor)

    def showAll(self):
        """Show all bound widgets."""
        self.isVisible = True
        self.applyVisibilityState()
        self.updateButtonAppearance()

    def hideAll(self):
        """Hide all bound widgets."""
        self.isVisible = False
        self.applyVisibilityState()
        self.updateButtonAppearance()

    def setVisibility(self, visible):
        """
        Set the visibility state explicitly.

        Args:
            visible: Boolean indicating whether to show (True) or hide (False)
        """
        self.isVisible = visible
        self.applyVisibilityState()
        self.updateButtonAppearance()

    def getVisibilityState(self):
        """
        Get the current visibility state.

        Returns:
            Boolean indicating if widgets are visible
        """
        return self.isVisible

    def getBoundWidgets(self):
        """
        Get the list of bound widgets.

        Returns:
            List of bound widgets
        """
        return self.boundWidgets

    def setShowText(self, text):
        """
        Set the text to display when widgets are visible.

        Args:
            text: Text to display
        """
        self.showText = text
        self.updateButtonAppearance()

    def setHideText(self, text):
        """
        Set the text to display when widgets are hidden.

        Args:
            text: Text to display
        """
        self.hideText = text
        self.updateButtonAppearance()

    def setShowColor(self, color):
        """
        Set the button color when widgets are visible.

        Args:
            color: Color value
        """
        self.showColor = color
        self.updateButtonAppearance()

    def setHideColor(self, color):
        """
        Set the button color when widgets are hidden.

        Args:
            color: Color value
        """
        self.hideColor = color
        self.updateButtonAppearance()


# Convenience functions for common use cases
def createVisibilityGroup(master, widgets, **kwargs):
    """
    Create a VisibleBtn bound to a group of widgets.

    Args:
        master: Parent widget
        widgets: List of widgets to bind
        **kwargs: Additional arguments for VisibleBtn

    Returns:
        VisibleBtn instance
    """
    btn = VisibleBtn(master, boundWidgets=widgets, **kwargs)
    return btn


def createToggleButton(master, targetWidget, **kwargs):
    """
    Create a VisibleBtn for a single widget.

    Args:
        master: Parent widget
        targetWidget: Widget to toggle
        **kwargs: Additional arguments for VisibleBtn

    Returns:
        VisibleBtn instance
    """
    btn = VisibleBtn(master, boundWidgets=[targetWidget], **kwargs)
    return btn

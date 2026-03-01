from dataclasses import dataclass
from typing import List, Callable, Dict, Optional, Union, Any
from .WrapBox import WrapBox
from .basic.Button import Button


@dataclass
class WrapBtnConfig:
    name: str
    callback: Callable = None
    style: Optional[Dict] = None
    group: Optional[str] = None
    tooltip: Optional[str] = None
    enabled: bool = True


class WrapBtnBar(WrapBox):
    """
    A widget that manages a list of buttons and their callbacks, built on WrapBox.
    Buttons automatically wrap to new lines when space is insufficient.
    All methods and variables use camelCase naming convention.

    Enhanced Features:
    - Button styling and customization
    - Button state management (enabled/disabled)
    - Button grouping and organization
    - Event handling and callbacks with parameters
    - Button validation and error handling
    - Dynamic button updates
    - Automatic wrapping of buttons
    """

    def __init__(self, master: Any, buttonStyle: Optional[Dict] = None,
                 padx: int = 2, pady: int = 2, **kwargs):
        """
        Initialize the WrapBtnBar widget.

        Args:
            master: The parent widget
            buttonStyle: Default style for all buttons (optional)
            buttonPadding: Padding around buttons
            buttonSpacing: Spacing between buttons
            **kwargs: Additional arguments for WrapBox
        """
        # Initialize base class
        super().__init__(master, **kwargs)

        # Initialize button management attributes
        self.buttons: List[Button] = []
        self.buttonData: List[WrapBtnConfig] = []
        self.defaultButtonStyle = buttonStyle or {}
        self.padx = padx
        self.pady = pady
        # Group name to button indices
        self.buttonGroups: Dict[str, List[int]] = {}

    def addBtn(self, config: WrapBtnConfig) -> Button:
        """
        Add a button to the WrapBtnBar.

        Args:
            config: Button configuration object

        Returns:
            The created button widget
        """
        # Merge default style with custom style
        style = {**self.defaultButtonStyle, **(config.style or {})}

        # Create the button with enhanced styling
        button = Button(self, text=config.name,
                        command=config.callback, **style)

        # Add button to WrapBox with spacing
        self.addWidget(button, padx=self.padx, pady=self.pady)

        # Store button metadata
        buttonIndex = len(self.buttons)
        self.buttons.append(button)
        self.buttonData.append(config)

        # Add to group if specified
        if config.group:
            if config.group not in self.buttonGroups:
                self.buttonGroups[config.group] = []
            self.buttonGroups[config.group].append(buttonIndex)

        # Set initial state
        if not config.enabled:
            button.configure(state="disabled")

        return button

    def addBtns(self, btnInfos: List[WrapBtnConfig]) -> None:
        """
        Add a list of buttons with their respective callbacks.

        Args:
            btnInfos: List of button configuration objects
        """
        for config in btnInfos:
            self.addBtn(config)

    def removeBtn(self, name: str) -> bool:
        """
        Remove a button by its name.

        Args:
            name: The name of the button to remove.

        Returns:
            True if button was found and removed, False otherwise
        """
        for i, button in enumerate(self.buttons):
            if button.cget("text") == name:
                # Remove from WrapBox
                self.delWidget(button)

                # Remove from tracking lists
                self.buttons.pop(i)
                self.buttonData.pop(i)

                # Update group indices
                for groupName, indices in self.buttonGroups.items():
                    if i in indices:
                        indices.remove(i)
                        # Update indices greater than the removed index
                        for j in range(len(indices)):
                            if indices[j] > i:
                                indices[j] -= 1

                return True
        return False

    def removeBtns(self, names: List[str]) -> None:
        """
        Remove a list of buttons by their names.

        Args:
            names: List of button names to remove.
        """
        for name in names:
            self.removeBtn(name)

    def modifyBtn(self, oldName: str, newName: str) -> bool:
        """
        Modify the text of a button.

        Args:
            oldName: The current name of the button.
            newName: The new name for the button.

        Returns:
            True if button was found and modified, False otherwise
        """
        for i, button in enumerate(self.buttons):
            if button.cget("text") == oldName:
                button.configure(text=newName)
                # Update button data
                self.buttonData[i].name = newName
                return True
        return False

    def enableBtn(self, name: str) -> bool:
        """
        Enable a button by its name.

        Args:
            name: The name of the button to enable.

        Returns:
            True if button was found and enabled, False otherwise
        """
        for i, button in enumerate(self.buttons):
            if button.cget("text") == name:
                button.configure(state="normal")
                self.buttonData[i].enabled = True
                return True
        return False

    def disableBtn(self, name: str) -> bool:
        """
        Disable a button by its name.

        Args:
            name: The name of the button to disable.

        Returns:
            True if button was found and disabled, False otherwise
        """
        for i, button in enumerate(self.buttons):
            if button.cget("text") == name:
                button.configure(state="disabled")
                self.buttonData[i].enabled = False
                return True
        return False

    def enableGroup(self, groupName: str) -> None:
        """
        Enable all buttons in a group.

        Args:
            groupName: The name of the button group.
        """
        if groupName in self.buttonGroups:
            for index in self.buttonGroups[groupName]:
                if index < len(self.buttons):
                    self.buttons[index].configure(state="normal")
                    self.buttonData[index].enabled = True

    def disableGroup(self, groupName: str) -> None:
        """
        Disable all buttons in a group.

        Args:
            groupName: The name of the button group.
        """
        if groupName in self.buttonGroups:
            for index in self.buttonGroups[groupName]:
                if index < len(self.buttons):
                    self.buttons[index].configure(state="disabled")
                    self.buttonData[index].enabled = False

    def getBtn(self, name: str) -> Optional[Dict]:
        """
        Get detailed information about a button.

        Args:
            name: The name of the button.

        Returns:
            Dictionary with button information, or None if not found
        """
        for i, button in enumerate(self.buttons):
            if button.cget("text") == name:
                return {
                    'button': button,
                    'data': self.buttonData[i]
                }
        return None

    def getAllBtns(self) -> List[Dict]:
        """
        Get information about all buttons.

        Returns:
            List of dictionaries with button information
        """
        result = []
        for i, button in enumerate(self.buttons):
            result.append({
                'button': button,
                'data': self.buttonData[i]
            })
        return result

    def getGroupBtns(self, groupName: str) -> List[Dict]:
        """
        Get all buttons in a specific group.

        Args:
            groupName: The name of the button group.

        Returns:
            List of dictionaries with button information
        """
        result = []
        if groupName in self.buttonGroups:
            for index in self.buttonGroups[groupName]:
                if index < len(self.buttons):
                    result.append({
                        'button': self.buttons[index],
                        'data': self.buttonData[index]
                    })
        return result

    def clearBtns(self) -> None:
        """
        Remove all buttons from the WrapBtnBar.
        """
        # Clear all widgets from WrapBox
        self.clearWidgets()

        # Clear tracking lists
        self.buttons.clear()
        self.buttonData.clear()
        self.buttonGroups.clear()

    def updateBtnStyle(self, name: str, style: Dict) -> bool:
        """
        Update the style of a specific button.

        Args:
            name: The name of the button.
            style: Dictionary with style properties to update.

        Returns:
            True if button was found and updated, False otherwise
        """
        for i, button in enumerate(self.buttons):
            if button.cget("text") == name:
                button.configure(**style)
                # Update stored style
                if self.buttonData[i].style is None:
                    self.buttonData[i].style = {}
                self.buttonData[i].style.update(style)
                return True
        return False

    def setDefaultBtnStyle(self, style: Dict) -> None:
        """
        Set the default button style for all new buttons.

        Args:
            style: Dictionary with default style properties.
        """
        self.defaultButtonStyle.update(style)

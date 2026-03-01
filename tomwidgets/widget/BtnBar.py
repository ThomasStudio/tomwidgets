from dataclasses import dataclass
import tkinter as tk
from tkinter.ttk import Separator
from typing import List, Callable, Dict, Optional
from .basic.Button import Button
from .basic.Frame import Frame
from .basic.Label import Label


@dataclass
class BtnConfig:
    name: str = ""
    callback: Callable = None
    style: Optional[Dict] = None
    group: Optional[str] = None
    tooltip: Optional[str] = None
    enabled: bool = True
    isLabel: bool = False
    isSeparator: bool = False


class BtnBar(Frame):
    """
    A widget that manages a list of buttons and their callbacks, built on a Frame.

    Enhanced Features:
    - Button styling and customization
    - Button state management (enabled/disabled)
    - Button grouping and organization
    - Event handling and callbacks with parameters
    - Button validation and error handling
    - Dynamic button updates
    """

    def __init__(self, master, button_style: Optional[Dict] = None, pady: int = 5, padx: int = 5, orient=tk.HORIZONTAL, title="", **kwargs):
        """
        Initialize the BtnBar widget.

        Args:
            master: The parent widget
            button_style: Default style for all buttons (optional)
            pady: Padding around buttons
            padx: Padding around buttons
            **kwargs: Additional arguments for Frame
        """
        super().__init__(master, **kwargs)
        self.title = title
        self.orient = orient

        self.buttons: List[Button] = []
        # Store additional button metadata
        self.button_data: List[BtnConfig] = []
        self.default_button_style = button_style or {}
        self.pady = pady
        self.padx = padx
        # Group name to button indices
        self.button_groups: Dict[str, List[int]] = {}

        self.addTitle()

    def addTitle(self):
        if self.title and not self.titleLabel:
            self.titleLabel = Label(self, text=self.title)
            self.titleLabel.pack(side=tk.LEFT, padx=self.padx,
                                 pady=self.pady)

    def setTitle(self, title: str):
        self.title = title
        self.titleLabel.configure(text=self.title)

    def getTitle(self) -> str:
        return self.title

    def addBtn(self, config: BtnConfig) -> Button:
        # Merge default style with custom style
        style = {**self.default_button_style, **(config.style or {})}

        side = tk.LEFT if self.orient == tk.HORIZONTAL else tk.TOP

        if config.isSeparator:
            if self.orient == tk.HORIZONTAL:
                button = Separator(self, orient=tk.VERTICAL)
                button.pack(side=side, fill=tk.Y)
            else:
                button = Separator(self, orient=tk.HORIZONTAL)
                button.pack(side=side, fill=tk.X)
        elif config.isLabel:
            button = Label(self, text=config.name)
            button.pack(side=side, padx=self.padx, pady=self.pady)
        else:
            # Create the button with enhanced styling
            button = Button(self, text=config.name,
                            command=config.callback, **style)
            button.pack(side=side, padx=self.padx, pady=self.pady)

        # Store button metadata
        button_index = len(self.buttons)
        self.buttons.append(button)
        self.button_data.append(config)

        # Add to group if specified
        if config.group:
            if config.group not in self.button_groups:
                self.button_groups[config.group] = []
            self.button_groups[config.group].append(button_index)

        # Set initial state
        if not config.enabled:
            button.configure(state="disabled")

        return button

    def addBtns(self, btnInfos: List[BtnConfig]) -> None:
        """
        Add a list of buttons with their respective callbacks.

        Args:
            button_dict: Dictionary mapping button names to their callbacks,
                        or list of button configuration dictionaries
            group: Button group name for organization
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
                button.destroy()
                self.buttons.pop(i)
                self.button_data.pop(i)

                # Update group indices
                for group_name, indices in self.button_groups.items():
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
                self.button_data[i].name = newName
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
                self.button_data[i].enabled = True
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
                self.button_data[i].enabled = False
                return True
        return False

    def enableGroup(self, group_name: str) -> None:
        """
        Enable all buttons in a group.

        Args:
            group_name: The name of the button group.
        """
        if group_name in self.button_groups:
            for index in self.button_groups[group_name]:
                if index < len(self.buttons):
                    self.buttons[index].configure(state="normal")
                    self.button_data[index].enabled = True

    def disableGroup(self, group_name: str) -> None:
        """
        Disable all buttons in a group.

        Args:
            group_name: The name of the button group.
        """
        if group_name in self.button_groups:
            for index in self.button_groups[group_name]:
                if index < len(self.buttons):
                    self.buttons[index].configure(state="disabled")
                    self.button_data[index].enabled = False

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
                    'data': self.button_data[i]
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
                'data': self.button_data[i]
            })
        return result

    def getGroupBtns(self, group_name: str) -> List[Dict]:
        """
        Get all buttons in a specific group.

        Args:
            group_name: The name of the button group.

        Returns:
            List of dictionaries with button information
        """
        result = []
        if group_name in self.button_groups:
            for index in self.button_groups[group_name]:
                if index < len(self.buttons):
                    result.append({
                        'button': self.buttons[index],
                        'data': self.button_data[index]
                    })
        return result

    def clearBtns(self) -> None:
        """
        Remove all buttons from the BtnBar.
        """
        for button in self.buttons:
            button.destroy()
        self.buttons.clear()
        self.button_data.clear()
        self.button_groups.clear()

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
                if self.button_data[i].style is None:
                    self.button_data[i].style = {}
                self.button_data[i].style.update(style)
                return True
        return False

    def setDefaultBtnStyle(self, style: Dict) -> None:
        """
        Set the default button style for all new buttons.

        Args:
            style: Dictionary with default style properties.
        """
        self.default_button_style.update(style)

    def refreshLayout(self) -> None:
        """
        Refresh the button layout (useful after dynamic changes).
        """
        # Clear current layout
        for button in self.buttons:
            button.pack_forget()

        # Re-pack all buttons
        for button in self.buttons:
            button.pack(side="left", padx=self.padx,
                        pady=self.pady)

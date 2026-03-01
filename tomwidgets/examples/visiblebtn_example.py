from tomwidgets.widget.basic import Frame, Label, Button, Entry, Switch, ScrollableFrame
from tomwidgets.widget.VisibleBtn import VisibleBtn, createVisibilityGroup, createToggleButton
import customtkinter as ctk
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class VisibleBtnExample(ctk.CTk):
    """Main application class for VisibleBtn example."""

    def __init__(self):
        """Initialize the application."""
        super().__init__()

        self.title("VisibleBtn Example - tomwidgets")
        self.geometry("900x750")
        self.minsize(800, 650)

        # Configure grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)  # Title
        self.grid_rowconfigure(1, weight=0)  # Description
        self.grid_rowconfigure(2, weight=0)  # Control panel
        self.grid_rowconfigure(3, weight=1)  # Demo area

        self.visibleBtns = {}  # Store references to VisibleBtn instances
        self.demoWidgets = {}  # Store references to demo widgets

        # Common widget configurations
        self._setupCommonConfigs()
        self.setupUi()

    def _setupCommonConfigs(self):
        """Setup common widget configurations to reduce code duplication."""
        self.titleFont = ctk.CTkFont(size=22, weight="bold")
        self.subtitleFont = ctk.CTkFont(size=12)
        self.boldFont = ctk.CTkFont(weight="bold")
        self.smallFont = ctk.CTkFont(size=12)

        # Common colors
        self.colors = {
            'success': "#27ae60",
            'danger': "#d9534f",
            'warning': "#f39c12",
            'info': "#5bc0de",
            'primary': "#3b8ed0",
            'secondary': "#34495e"
        }

    def setupUi(self):
        """Setup the user interface."""
        # Title label
        titleLabel = Label(self, text="VisibleBtn Widget Example",
                           font=self.titleFont)
        titleLabel.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="ew")

        # Description label
        descLabel = Label(self,
                          text="Button widget that can bind and toggle visibility for groups of widgets",
                          font=self.subtitleFont)
        descLabel.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="ew")

        # Control panel
        self.setupControlPanel()

        # Demo area
        self.setupDemoArea()

    def setupControlPanel(self):
        """Setup the control panel with demo selection buttons."""
        controlFrame = Frame(self)
        controlFrame.grid(row=2, column=0, padx=20, pady=10, sticky="ew")
        controlFrame.grid_columnconfigure(0, weight=1)

        # Create control buttons
        self.createControlButtons(controlFrame)

    def createControlButtons(self, parent):
        """Create buttons for different VisibleBtn demonstrations."""
        # Configure button frame grid
        for i in range(3):
            parent.grid_columnconfigure(i, weight=1)

        # Demo configurations
        demos = [
            # Row 1: Basic demonstrations
            ("Single Widget Toggle", self.showSingleWidgetToggle),
            ("Widget Group Toggle", self.showWidgetGroupToggle),
            ("Multiple Groups", self.showMultipleGroups),

            # Row 2: Advanced features
            ("Custom Appearance", self.showCustomAppearance),
            ("Dynamic Binding", self.showDynamicBinding),
            ("Nested Groups", self.showNestedGroups),

            # Row 3: Utility functions
            ("Clear Demo Area", self.clearDemoArea, {
             "fg_color": self.colors['danger'], "hover_color": "#c9302c"}),
            ("Reset All", self.resetAll, {
             "fg_color": self.colors['info'], "hover_color": "#46b8da"}),
            ("All Features", self.showAllFeatures)
        ]

        # Create buttons dynamically
        for i, demo in enumerate(demos):
            row = i // 3
            col = i % 3

            if len(demo) == 2:
                text, command = demo
                kwargs = {}
            else:
                text, command, kwargs = demo

            button = Button(parent, text=text, command=command, **kwargs)
            button.grid(row=row, column=col, padx=10, pady=10)

    def setupDemoArea(self):
        """Setup the demo area where VisibleBtn demonstrations will be shown."""
        self.demoArea = ScrollableFrame(self, fg_color="transparent")
        self.demoArea.grid(row=3, column=0, padx=20, pady=20, sticky="nsew")

        # Configure demo area grid
        self.demoArea.grid_columnconfigure(0, weight=1)

        # Status label
        self.statusLabel = Label(self.demoArea, text="Select a demo to begin...",
                                 font=self.boldFont)
        self.statusLabel.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    def updateStatus(self, message):
        """Update the status label."""
        self.statusLabel.configure(text=message)

    def clearDemoArea(self):
        """Clear all widgets from the demo area."""
        # Clear VisibleBtn instances
        self.visibleBtns.clear()
        self.demoWidgets.clear()

        widgets = self.demoArea.winfo_children()
        for widget in widgets:
            if widget != self.statusLabel:
                widget.destroy()

        self.updateStatus("Demo area cleared")

    def resetAll(self):
        """Reset the demo area to initial state."""
        self.clearDemoArea()
        self.updateStatus("Select a demo to begin...")

    # Helper methods for widget creation
    def _createDemoWidget(self, parent, row, text, bg_color, height=60, widget_id=None):
        """Helper method to create demo widgets with consistent styling."""
        frame = Frame(parent, fg_color=bg_color,
                      corner_radius=6, height=height)
        frame.grid(row=row, column=0, padx=10, pady=2, sticky="ew")

        label = Label(frame, text=text, font=self.boldFont)
        label.pack(padx=10, pady=10)

        widget_id = widget_id or f"widget_{row}"
        self.demoWidgets[widget_id] = frame

        return frame

    def _createButtonGroup(self, parent, buttons_config, row_start=0):
        """Helper method to create button groups dynamically."""
        for i, (text, command, kwargs) in enumerate(buttons_config):
            row = row_start + (i // 2)
            col = i % 2

            button = Button(parent, text=text, command=command, **kwargs)
            button.grid(row=row, column=col, padx=5, pady=5)

    # VisibleBtn demonstration methods
    def showSingleWidgetToggle(self):
        """Demonstrate VisibleBtn for a single widget."""
        self.clearDemoArea()
        self.updateStatus(
            "Single Widget Toggle - Toggle visibility of individual widgets")

        # Create a target widget to toggle
        targetFrame = self._createDemoWidget(self.demoArea, 1,
                                             "This frame can be toggled on/off",
                                             "#3a3a3a", height=100,
                                             widget_id='single_target')

        # Create VisibleBtn using convenience function
        toggleBtn = createToggleButton(self.demoArea, targetFrame)
        toggleBtn.grid(row=2, column=0, padx=10, pady=10)
        self.visibleBtns['single_toggle'] = toggleBtn

        # Add info text
        infoText = Label(self.demoArea,
                         text="Click the button above to toggle the frame's visibility",
                         font=self.smallFont)
        infoText.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.demoWidgets['single_info'] = infoText

    def showWidgetGroupToggle(self):
        """Demonstrate VisibleBtn for a group of widgets."""
        self.clearDemoArea()
        self.updateStatus(
            "Widget Group Toggle - Toggle visibility of multiple widgets")

        # Create a group of widgets to toggle
        groupWidgets = []

        for i in range(3):
            color_value = (i + 3) * 10
            bg_color = f"#{color_value}{color_value}{color_value}"

            widgetFrame = self._createDemoWidget(self.demoArea, i+1,
                                                 f"Widget {i+1} in group",
                                                 bg_color, height=80,
                                                 widget_id=f'group_widget{i+1}')
            groupWidgets.append(widgetFrame)

        # Create VisibleBtn for the group
        groupBtn = createVisibilityGroup(self.demoArea, groupWidgets,
                                         showText="Hide Widget Group",
                                         hideText="Show Widget Group",
                                         showColor=self.colors['success'],
                                         hideColor="#e74c3c")
        groupBtn.grid(row=4, column=0, padx=10, pady=10)
        self.visibleBtns['group_toggle'] = groupBtn

        # Add info text
        infoText = Label(self.demoArea,
                         text="Click the button to toggle all 3 widgets simultaneously",
                         font=self.smallFont)
        infoText.grid(row=5, column=0, padx=10, pady=5, sticky="w")
        self.demoWidgets['group_info'] = infoText

    def showMultipleGroups(self):
        """Demonstrate multiple VisibleBtn instances managing different groups."""
        self.clearDemoArea()
        self.updateStatus(
            "Multiple Groups - Manage multiple visibility groups independently")

        currentRow = 1
        group_configs = [
            ("Form Section", "#2c3e50", 2, "form"),
            ("Settings Section", "#34495e", 3, "setting"),
            ("Information Section", "#16a085", 1, "info")
        ]

        for section_name, color, widget_count, prefix in group_configs:
            # Section label
            sectionLabel = Label(self.demoArea, text=f"{section_name}:",
                                 font=self.boldFont)
            sectionLabel.grid(row=currentRow, column=0,
                              padx=10, pady=(10, 5), sticky="w")
            currentRow += 1

            # Create widgets for this section
            sectionWidgets = []
            for i in range(widget_count):
                if prefix == "form":
                    widgetFrame = self._createDemoWidget(self.demoArea, currentRow,
                                                         "", color, height=60,
                                                         widget_id=f'{prefix}_field{i+1}')
                    # Add form field
                    formEntry = Entry(
                        widgetFrame, placeholder_text=f"Form field {i+1}")
                    formEntry.pack(padx=10, pady=10, fill="x")
                elif prefix == "setting":
                    widgetFrame = self._createDemoWidget(self.demoArea, currentRow,
                                                         "", color, height=50,
                                                         widget_id=f'{prefix}{i+1}')
                    # Add setting switch
                    settingSwitch = Switch(widgetFrame, text=f"Setting {i+1}")
                    settingSwitch.pack(padx=10, pady=10, anchor="w")
                else:  # info section
                    widgetFrame = self._createDemoWidget(self.demoArea, currentRow,
                                                         "This is an information panel\nthat can be toggled independently",
                                                         color, height=80,
                                                         widget_id=f'{prefix}_panel')

                sectionWidgets.append(widgetFrame)
                currentRow += 1

            # Create visibility button for this section
            sectionBtn = createVisibilityGroup(self.demoArea, sectionWidgets,
                                               showText=f"▲ Hide {section_name.split()[0]}",
                                               hideText=f"▼ Show {section_name.split()[0]}")
            sectionBtn.grid(row=currentRow, column=0, padx=10, pady=5)
            self.visibleBtns[f'{prefix}_group'] = sectionBtn
            currentRow += 1

    def showCustomAppearance(self):
        """Demonstrate customizing VisibleBtn appearance."""
        self.clearDemoArea()
        self.updateStatus(
            "Custom Appearance - Customize button text, colors, and behavior")

        # Create target widgets
        targetWidgets = []
        for i in range(2):
            targetFrame = self._createDemoWidget(self.demoArea, i+1,
                                                 f"Custom styled target {i+1}",
                                                 "#8e44ad", height=70,
                                                 widget_id=f'custom_target{i+1}')
            targetWidgets.append(targetFrame)

        # Create VisibleBtn with custom appearance
        customBtn = VisibleBtn(self.demoArea,
                               boundWidgets=targetWidgets,
                               showText="🔒 Lock Section",
                               hideText="🔓 Unlock Section",
                               showColor=self.colors['warning'],
                               hideColor="#9b59b6",
                               width=200,
                               height=40,
                               corner_radius=20,
                               font=self.boldFont)
        customBtn.grid(row=3, column=0, padx=10, pady=10)
        self.visibleBtns['custom_btn'] = customBtn

        # Control panel for dynamic customization
        controlFrame = Frame(
            self.demoArea, fg_color="#2b2b2b", corner_radius=8)
        controlFrame.grid(row=4, column=0, padx=10, pady=10, sticky="ew")

        controlLabel = Label(controlFrame, text="Dynamic Customization:",
                             font=self.boldFont)
        controlLabel.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        # Customization buttons configuration
        buttons_config = [
            ("Update Show Text", self._updateShowText, {"width": 120}),
            ("Update Hide Text", self._updateHideText, {"width": 120}),
            ("Update Show Color", self._updateShowColor, {"width": 120}),
            ("Update Hide Color", self._updateHideColor, {"width": 120})
        ]

        self._createButtonGroup(controlFrame, buttons_config, row_start=1)
        self.demoWidgets['custom_control'] = controlFrame

    def _updateShowText(self):
        """Update show text for custom button."""
        if 'custom_btn' in self.visibleBtns:
            self.visibleBtns['custom_btn'].setShowText("🚫 Hide Section")
            self.updateStatus("Show text updated")

    def _updateHideText(self):
        """Update hide text for custom button."""
        if 'custom_btn' in self.visibleBtns:
            self.visibleBtns['custom_btn'].setHideText("✅ Show Section")
            self.updateStatus("Hide text updated")

    def _updateShowColor(self):
        """Update show color for custom button."""
        if 'custom_btn' in self.visibleBtns:
            self.visibleBtns['custom_btn'].setShowColor("#e74c3c")
            self.updateStatus("Show color updated")

    def _updateHideColor(self):
        """Update hide color for custom button."""
        if 'custom_btn' in self.visibleBtns:
            self.visibleBtns['custom_btn'].setHideColor(self.colors['success'])
            self.updateStatus("Hide color updated")

    def showDynamicBinding(self):
        """Demonstrate dynamic widget binding and unbinding."""
        self.clearDemoArea()
        self.updateStatus("Dynamic Binding - Add/remove widgets dynamically")

        # Create a pool of widgets that can be bound
        widgetPool = []
        for i in range(4):
            poolFrame = self._createDemoWidget(self.demoArea, i+1,
                                               f"Widget {i+1} (Available for binding)",
                                               "#3498db", height=60,
                                               widget_id=f'pool_widget{i+1}')
            widgetPool.append(poolFrame)

        # Create VisibleBtn with empty initial binding
        dynamicBtn = VisibleBtn(self.demoArea,
                                boundWidgets=[],
                                showText="Hide Bound Widgets",
                                hideText="Show Bound Widgets")
        dynamicBtn.grid(row=5, column=0, padx=10, pady=10)
        self.visibleBtns['dynamic_btn'] = dynamicBtn

        # Binding control panel
        bindFrame = Frame(self.demoArea, fg_color="#2b2b2b", corner_radius=8)
        bindFrame.grid(row=6, column=0, padx=10, pady=10, sticky="ew")

        bindLabel = Label(bindFrame, text="Dynamic Binding Controls:",
                          font=self.boldFont)
        bindLabel.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        # Binding buttons configuration
        bind_buttons = []
        for i in range(4):
            def make_bind_func(index):
                def bind_func():
                    if index < len(widgetPool):
                        dynamicBtn.addWidget(widgetPool[index])
                        self.updateStatus(
                            f"Bound {len(dynamicBtn.getBoundWidgets())} widgets")
                return bind_func

            bind_buttons.append(
                (f"Bind Widget {i+1}", make_bind_func(i), {"width": 100}))

        bind_buttons.append(("Unbind All", self._unbindAll, {
            "width": 100, "fg_color": self.colors['danger'], "hover_color": "#c9302c"
        }))

        self._createButtonGroup(bindFrame, bind_buttons, row_start=1)
        self.demoWidgets['bind_control'] = bindFrame

    def _unbindAll(self):
        """Unbind all widgets from dynamic button."""
        if 'dynamic_btn' in self.visibleBtns:
            self.visibleBtns['dynamic_btn'].clearWidgets()
            self.updateStatus("All widgets unbound")

    def showNestedGroups(self):
        """Demonstrate nested visibility groups with hierarchical control."""
        self.clearDemoArea()
        self.updateStatus("Nested Groups - Hierarchical visibility control")

        # Main container
        mainFrame = Frame(self.demoArea, fg_color="#2b2b2b", corner_radius=10)
        mainFrame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        # Main group button
        mainWidgets = []

        # Subgroup 1
        subgroup1Frame = Frame(mainFrame, fg_color="#34495e", corner_radius=8)
        subgroup1Frame.pack(padx=10, pady=5, fill="x")

        subgroup1Label = Label(subgroup1Frame, text="Subgroup 1 Content",
                               font=self.boldFont)
        subgroup1Label.pack(padx=10, pady=10)
        mainWidgets.append(subgroup1Frame)

        # Subgroup 2 with its own nested widgets
        subgroup2Frame = Frame(mainFrame, fg_color="#2c3e50", corner_radius=8)
        subgroup2Frame.pack(padx=10, pady=5, fill="x")

        subgroup2Label = Label(subgroup2Frame, text="Subgroup 2 with Nested Items",
                               font=self.boldFont)
        subgroup2Label.pack(padx=10, pady=5)

        # Nested items in subgroup 2
        nestedWidgets = []
        for i in range(2):
            nestedFrame = Frame(
                subgroup2Frame, fg_color="#16a085", corner_radius=6, height=40)
            nestedFrame.pack(padx=20, pady=2, fill="x")

            nestedLabel = Label(nestedFrame, text=f"Nested Item {i+1}")
            nestedLabel.pack(padx=10, pady=5)
            nestedWidgets.append(nestedFrame)

        # Create nested VisibleBtn for subgroup 2 items
        nestedBtn = createVisibilityGroup(subgroup2Frame, nestedWidgets,
                                          showText="▲ Hide Nested",
                                          hideText="▼ Show Nested",
                                          width=120)
        nestedBtn.pack(padx=20, pady=5)
        self.visibleBtns['nested_btn'] = nestedBtn

        mainWidgets.append(subgroup2Frame)

        self.demoWidgets['nested_main'] = mainFrame

        # Main group button
        mainBtn = createVisibilityGroup(self.demoArea, mainWidgets,
                                        showText="▲ Hide Entire Section",
                                        hideText="▼ Show Entire Section")
        mainBtn.grid(row=2, column=0, padx=10, pady=10)
        self.visibleBtns['main_btn'] = mainBtn

    def showAllFeatures(self):
        """Demonstrate all VisibleBtn features in one comprehensive example."""
        self.clearDemoArea()
        self.updateStatus(
            "All Features - Comprehensive VisibleBtn demonstration")

        # Show the multiple groups example as it demonstrates most features
        self.showMultipleGroups()
        self.updateStatus(
            "All Features - Multiple independent visibility groups")


def main():
    """Main function to run the VisibleBtn example."""
    app = VisibleBtnExample()
    app.mainloop()


if __name__ == "__main__":
    main()

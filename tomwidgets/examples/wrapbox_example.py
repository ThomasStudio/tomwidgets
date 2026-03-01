import customtkinter as ctk
import tkinter as tk
from tomwidgets.widget import WrapBox, Button


def testAllFunctions():
    """Comprehensive test of all WrapBox functions."""

    # Create main window
    root = ctk.CTk()
    root.title("WrapBox Comprehensive Test")
    root.geometry("600x400")

    # Create WrapBox
    wrapBox = WrapBox(root, width=500, height=300)
    wrapBox.pack(pady=20, padx=20, fill="both", expand=True)

    # Create control frame
    controlFrame = ctk.CTkFrame(root)
    controlFrame.pack(fill=tk.X, expand=True)

    # Widget counter
    widgetCounter = 0

    def addWidget():
        """Add a new widget."""
        nonlocal widgetCounter
        widgetCounter += 1

        widget_types = [
            lambda: ctk.CTkButton(
                wrapBox, text=f"Button {widgetCounter}", width=100, height=30),
            lambda: ctk.CTkCheckBox(wrapBox, text=f"Check {widgetCounter}"),
            lambda: ctk.CTkSwitch(wrapBox, text=f"Switch {widgetCounter}"),
            lambda: ctk.CTkLabel(wrapBox, text=f"Label {widgetCounter}"),
            lambda: ctk.CTkRadioButton(wrapBox, text=f"Radio {widgetCounter}"),
            lambda: ctk.CTkProgressBar(wrapBox, width=120),
            lambda: ctk.CTkSegmentedButton(
                wrapBox, values=[f"Seg1-{widgetCounter}", f"Seg2-{widgetCounter}"]),
            lambda: ctk.CTkComboBox(
                wrapBox, values=[f"Option A-{widgetCounter}", f"Option B-{widgetCounter}"]),
            lambda: ctk.CTkOptionMenu(
                wrapBox, values=[f"Menu A-{widgetCounter}", f"Menu B-{widgetCounter}"]),
            lambda: ctk.CTkEntry(
                wrapBox, placeholder_text=f"Entry {widgetCounter}", width=120),
            lambda: ctk.CTkSlider(
                wrapBox, from_=0, to=widgetCounter*10, number_of_steps=5)
        ]
        import random
        widget = random.choice(widget_types)()
        result = wrapBox.addWidget(widget)
        print(f"Added widget {widgetCounter} with tag: {result}")
        print(f"Total widgets: {len(wrapBox.getWidgets())}")

    def addFormGroup():
        """Add a form-style group of widgets"""
        nonlocal widgetCounter
        widgetCounter += 1
        formLabel = ctk.CTkLabel(
            wrapBox, text="📋 Form Group:", font=ctk.CTkFont(weight="bold", size=14))
        wrapBox.addWidget(formLabel)

        nameEntry = ctk.CTkEntry(
            wrapBox, placeholder_text="Enter name...", width=200)
        wrapBox.addWidget(nameEntry, padding=5)

        emailEntry = ctk.CTkEntry(
            wrapBox, placeholder_text="Enter email...", width=200)
        wrapBox.addWidget(emailEntry, padding=5)

        ageSlider = ctk.CTkSlider(
            wrapBox, from_=18, to=100, number_of_steps=82, width=200)
        ageLabel = ctk.CTkLabel(wrapBox, text="Age:")
        wrapBox.addWidget(ageLabel, padding=5)
        wrapBox.addWidget(ageSlider, padding=5)

        submitBtn = ctk.CTkButton(
            wrapBox, text="Submit", command=lambda: print("Form submitted"))
        wrapBox.addWidget(submitBtn, padding=5)

        print(f"Added form group widgets")

    def addSettingsPanel():
        """Add a settings-style panel with various controls"""
        nonlocal widgetCounter
        widgetCounter += 1
        settingsLabel = ctk.CTkLabel(
            wrapBox, text="⚙️ Settings:", font=ctk.CTkFont(weight="bold", size=14))
        wrapBox.addWidget(settingsLabel)

        darkMode = ctk.CTkSwitch(
            wrapBox, text="Dark Mode", command=lambda: print("Dark mode toggled"))
        wrapBox.addWidget(darkMode, padding=5)

        notifications = ctk.CTkCheckBox(
            wrapBox, text="Enable Notifications", command=lambda: print("Notifications toggled"))
        wrapBox.addWidget(notifications, padding=5)

        themeMenu = ctk.CTkOptionMenu(
            wrapBox, values=["Light", "Dark", "Auto"], command=lambda x: print(f"Theme: {x}"))
        themeLabel = ctk.CTkLabel(wrapBox, text="Theme:")
        wrapBox.addWidget(themeLabel, padding=5)
        wrapBox.addWidget(themeMenu, padding=5)

        volumeSlider = ctk.CTkSlider(
            wrapBox, from_=0, to=100, number_of_steps=100, width=150)
        volumeLabel = ctk.CTkLabel(wrapBox, text="Volume:")
        wrapBox.addWidget(volumeLabel, padding=5)
        wrapBox.addWidget(volumeSlider, padding=5)

        print(f"Added settings panel widgets")

    def addProgressGroup():
        """Add a group of progress-related widgets"""
        nonlocal widgetCounter
        widgetCounter += 1
        progressLabel = ctk.CTkLabel(
            wrapBox, text="📊 Progress Indicators:", font=ctk.CTkFont(weight="bold", size=14))
        wrapBox.addWidget(progressLabel)

        progress1 = ctk.CTkProgressBar(wrapBox, width=200)
        progress1.set(0.3)
        progress2 = ctk.CTkProgressBar(wrapBox, width=200)
        progress2.set(0.7)
        progress3 = ctk.CTkProgressBar(wrapBox, width=200)
        progress3.set(1.0)

        wrapBox.addWidget(progress1, padding=5)
        wrapBox.addWidget(progress2, padding=5)
        wrapBox.addWidget(progress3, padding=5)

        statusBtn = ctk.CTkSegmentedButton(
            wrapBox, values=["Pending", "In Progress", "Completed"])
        wrapBox.addWidget(statusBtn, padding=5)

        print(f"Added progress group widgets")

    def insertWidget():
        """Insert a widget at the beginning."""
        nonlocal widgetCounter
        widgetCounter += 1

        button = ctk.CTkButton(
            wrapBox,
            text=f"Inserted {widgetCounter}",
            width=100,
            height=30
        )
        result = wrapBox.insertWidget("1.0", button)
        print(f"Inserted widget {widgetCounter} with tag: {result}")
        print(f"Total widgets: {len(wrapBox.getWidgets())}")

    def deleteLastWidget():
        """Delete the last widget."""
        widgets = wrapBox.getWidgets()
        if widgets:
            tag, widget = widgets[-1]
            result = wrapBox.delWidget(widget)
            print(f"Deleted widget with tag {tag}: {result}")
            print(f"Total widgets: {len(wrapBox.getWidgets())}")
        else:
            print("No widgets to delete")

    def deleteFirstWidget():
        """Delete the first widget."""
        widgets = wrapBox.getWidgets()
        if widgets:
            tag, widget = widgets[0]
            result = wrapBox.delWidget(widget)
            print(f"Deleted widget with tag {tag}: {result}")
            print(f"Total widgets: {len(wrapBox.getWidgets())}")
        else:
            print("No widgets to delete")

    def clearAllWidgets():
        """Clear all widgets."""
        wrapBox.clearWidgets()
        print("Cleared all widgets")
        print(f"Total widgets: {len(wrapBox.getWidgets())}")

    def showWidgetInfo():
        """Show information about all widgets."""
        widgets = wrapBox.getWidgets()
        print(f"\n=== Widget Information ===")
        print(f"Total widgets: {len(widgets)}")
        for i, (tag, widget) in enumerate(widgets):
            print(f"  Widget {i+1}: (tag: {tag})")
        print("========================\n")

    # Create control buttons
    box = WrapBox(controlFrame)
    box.pack(fill=tk.X, expand=True)

    box.addWidget(Button(box, text="Add Widget",
                  command=addWidget, width=120))
    box.addWidget(Button(box, text="Insert Widget",
                  command=insertWidget, width=120))
    box.addWidget(Button(box, text="Delete First",
                  command=deleteFirstWidget, width=120))
    box.addWidget(Button(box, text="Delete Last",
                  command=deleteLastWidget, width=120))
    box.addWidget(Button(box, text="Add Form",
                  command=addFormGroup, width=120))
    box.addWidget(Button(box, text="Add Settings",
                  command=addSettingsPanel, width=120))
    box.addWidget(Button(box, text="Add Progress",
                  command=addProgressGroup, width=120))
    box.addWidget(Button(box, text="Clear All",
                  command=clearAllWidgets, width=120))
    box.addWidget(Button(box, text="Show Info",
                  command=showWidgetInfo, width=120))

    # Add some initial widgets
    for i in range(3):
        addWidget()

    print("=== WrapBox Comprehensive Test Started ===")
    print("Use the buttons to test different functions:")
    print("- Add Widget: Adds a widget at the end")
    print("- Insert Widget: Inserts a widget at the beginning")
    print("- Delete First/Last: Deletes specific widgets")
    print("- Clear All: Removes all widgets")
    print("- Show Info: Displays current widget information")

    # Run the application
    root.mainloop()


def main():
    testAllFunctions()


if __name__ == "__main__":
    main()

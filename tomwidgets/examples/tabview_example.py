from tomwidgets.widget.basic import Tabview, Frame, Label, Button, Textbox, Entry, CheckBox
import customtkinter as ctk
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TabviewExample:
    """Example application demonstrating Tabview functionality."""

    def __init__(self):
        """Initialize the example application."""
        # Create main window
        self.root = ctk.CTk()
        self.root.title("Tabview Example - tomwidgets")
        self.root.geometry("800x600")
        self.root.minsize(600, 400)

        # Configure grid
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=0)  # Title
        self.root.grid_rowconfigure(1, weight=1)  # Tabview
        self.root.grid_rowconfigure(2, weight=0)  # Controls

        # Create UI
        self.createUi()

    def createUi(self):
        """Create the user interface."""
        # Title
        titleFrame = Frame(self.root)
        titleFrame.grid(row=0, column=0, padx=20, pady=10, sticky="ew")

        titleLabel = Label(titleFrame, text="Tabview Widget Example",
                           font=ctk.CTkFont(size=18, weight="bold"))
        titleLabel.pack(pady=10)

        # Create main tabview
        self.tabview = Tabview(self.root)
        self.tabview.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")

        # Add tabs
        self.addBasicTab()
        self.addDynamicTab()
        self.addStyledTab()
        self.addContentTab()

        # Control panel
        self.createControlPanel()

    def addBasicTab(self):
        """Add basic tab with simple content."""
        tab = self.tabview.add("Basic")

        # Add content to basic tab
        label = Label(tab, text="This is the Basic tab",
                      font=ctk.CTkFont(size=14))
        label.pack(pady=20)

        description = Label(
            tab, text="This tab demonstrates basic Tabview functionality with simple content.")
        description.pack(pady=10)

    def addDynamicTab(self):
        """Add dynamic tab with interactive content."""
        tab = self.tabview.add("Dynamic")

        # Add interactive content
        label = Label(tab, text="Dynamic Tab Content",
                      font=ctk.CTkFont(size=14, weight="bold"))
        label.pack(pady=20)

        # Entry for dynamic content
        self.dynamicEntry = Entry(
            tab, placeholder_text="Enter text to display below")
        self.dynamicEntry.pack(pady=10, padx=20, fill="x")

        # Display area
        self.dynamicDisplay = Label(tab, text="Enter text above to see it here",
                                    wraplength=400)
        self.dynamicDisplay.pack(pady=10, padx=20, fill="x")

        # Update button
        updateBtn = Button(tab, text="Update Display",
                           command=self.updateDynamicDisplay)
        updateBtn.pack(pady=10)

    def updateDynamicDisplay(self):
        """Update the dynamic display with entered text."""
        text = self.dynamicEntry.get()
        if text:
            self.dynamicDisplay.configure(text=f"You entered: {text}")
        else:
            self.dynamicDisplay.configure(
                text="Enter text above to see it here")

    def addStyledTab(self):
        """Add styled tab with custom appearance."""
        tab = self.tabview.add("Styled")

        # Configure tab styling
        self.tabview.configure(
            segmented_button_fg_color="#2b2b2b",
            segmented_button_selected_color="#1f6aa5",
            segmented_button_selected_hover_color="#144870",
            text_color="white"
        )

        # Add styled content
        label = Label(tab, text="Styled Tab",
                      font=ctk.CTkFont(size=16, weight="bold"),
                      text_color="#1f6aa5")
        label.pack(pady=20)

        # Color options
        colorFrame = Frame(tab)
        colorFrame.pack(pady=10)

        self.colorVars = {}
        colors = [
            ("Blue", "#1f6aa5"),
            ("Green", "#2e7d32"),
            ("Purple", "#7b1fa2"),
            ("Orange", "#f57c00")
        ]

        for i, (color_name, color_value) in enumerate(colors):
            var = ctk.StringVar(value="blue" if color_name == "Blue" else "")
            self.colorVars[color_name] = var

            checkbox = CheckBox(colorFrame, text=color_name, variable=var,
                                onvalue=color_value, offvalue="")
            checkbox.grid(row=0, column=i, padx=10, pady=5)

        # Apply button
        applyBtn = Button(tab, text="Apply Color", command=self.applyTabColor)
        applyBtn.pack(pady=10)

    def applyTabColor(self):
        """Apply selected color to tab."""
        selected_color = ""
        for color_name, var in self.colorVars.items():
            if var.get():
                selected_color = var.get()
                break

        if selected_color:
            self.tabview.configure(
                segmented_button_selected_color=selected_color)

    def addContentTab(self):
        """Add tab with rich content."""
        tab = self.tabview.add("Content")

        # Add text content
        textbox = Textbox(tab, height=15)
        textbox.pack(pady=20, padx=20, fill="both", expand=True)

        # Sample content
        sample_text = """This is the Content tab with a Textbox widget.

Features demonstrated:
• Tab switching
• Text input and display
• Scrollable content
• Rich text formatting

Try switching between tabs to see different functionalities.

You can also:
- Type in this textbox
- Switch to Dynamic tab for interactive features
- Use Styled tab to customize appearance
- Add/remove tabs using the control panel"""

        textbox.insert("1.0", sample_text)

    def createControlPanel(self):
        """Create control panel for tab management."""
        controlFrame = Frame(self.root)
        controlFrame.grid(row=2, column=0, padx=20, pady=10, sticky="ew")

        # Control buttons
        buttonFrame = Frame(controlFrame)
        buttonFrame.pack(pady=10)

        # Add tab button
        addBtn = Button(buttonFrame, text="Add New Tab",
                        command=self.addCustomTab)
        addBtn.grid(row=0, column=0, padx=5)

        # Remove tab button
        removeBtn = Button(buttonFrame, text="Remove Current Tab",
                           command=self.removeCurrentTab)
        removeBtn.grid(row=0, column=1, padx=5)

        # Get tab info button
        infoBtn = Button(buttonFrame, text="Tab Info",
                         command=self.showTabInfo)
        infoBtn.grid(row=0, column=2, padx=5)

        # Tab name entry
        self.tabNameEntry = Entry(
            controlFrame, placeholder_text="Enter tab name")
        self.tabNameEntry.pack(pady=5, fill="x")

    def addCustomTab(self):
        """Add a custom tab with user-specified name."""
        tab_name = self.tabNameEntry.get().strip()
        if not tab_name:
            tab_name = f"Tab {len(self.tabview._tab_dict) + 1}"

        if tab_name not in self.tabview._tab_dict:
            tab = self.tabview.add(tab_name)

            # Add simple content
            label = Label(tab, text=f"This is the '{tab_name}' tab")
            label.pack(pady=50)

            # Clear entry
            self.tabNameEntry.delete(0, "end")

            # Switch to new tab
            self.tabview.set(tab_name)

    def removeCurrentTab(self):
        """Remove the currently selected tab."""
        current_tab = self.tabview.get()
        if current_tab and current_tab not in ["Basic", "Dynamic", "Styled", "Content"]:
            self.tabview.delete(current_tab)

    def showTabInfo(self):
        """Display information about current tabs."""
        current_tab = self.tabview.get()
        tab_count = len(self.tabview._tab_dict)
        tab_names = list(self.tabview._tab_dict.keys())

        info_text = f"""Tab Information:
• Current tab: {current_tab}
• Total tabs: {tab_count}
• Tab names: {', '.join(tab_names)}"""

        # Create info dialog
        info_window = ctk.CTkToplevel(self.root)
        info_window.title("Tab Information")
        info_window.geometry("400x200")

        info_label = Label(info_window, text=info_text, justify="left")
        info_label.pack(pady=20, padx=20, fill="both", expand=True)

        close_btn = Button(info_window, text="Close",
                           command=info_window.destroy)
        close_btn.pack(pady=10)

    def run(self):
        """Run the example application."""
        print("🚀 Tabview Example Started")
        print("💡 Try switching between tabs")
        print("💡 Use the control panel to add/remove tabs")
        print("💡 Experiment with different tab styles")
        self.root.mainloop()


def main():
    """Main function to run the example."""
    # Set appearance mode
    ctk.set_appearance_mode("Dark")
    ctk.set_default_color_theme("blue")

    # Create and run example
    example = TabviewExample()
    example.run()


if __name__ == "__main__":
    main()

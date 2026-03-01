"""
ConfigEditor Widget
===================

A configuration file editor widget that allows viewing and editing all settings
in a configuration file using a user-friendly interface.
"""

import tkinter as tk
from tkinter import filedialog

from .basic import Frame, Entry, Label, ScrollableFrame, Toplevel
from .Config import Config
from .BtnBar import BtnBar, BtnConfig
from .InfoBox import InfoBox
from .InputBox import InputBox
from .OptionBar import OptionBar
from .InputBar import InputBar


class ConfigEditor(Frame):
    """Configuration file editor widget"""

    def __init__(self, master, configFile=None, **kwargs):
        """
        Initialize the ConfigEditor widget

        Args:
            master: Parent widget
            configFile: Path to configuration file (default: tools.ini)
            **kwargs: Additional arguments for Frame
        """
        super().__init__(master, **kwargs)

        self.configFile = configFile or 'config.ini'
        self.config = Config(self.configFile)
        self.widgets = {}  # Store references to UI widgets

        self.setupUi()
        self.loadConfig()

    def setupUi(self):
        """Setup the user interface"""
        # Create main container
        self.mainFrame = Frame(self)
        self.mainFrame.pack(fill="both", expand=True, padx=10, pady=10)

        # Title
        self.titleLabel = Label(self.mainFrame, text=f"{self.configFile}",
                                font=("Arial", 26, "bold"))
        self.titleLabel.pack(pady=10)

        # Scrollable frame for configuration items - FIXED expansion
        self.scrollFrame = ScrollableFrame(self.mainFrame)
        self.scrollFrame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Configure the scrollable frame to expand properly
        self.scrollFrame.configure(fg_color="transparent")  # Allow background to show
        
        # Ensure the scrollable frame expands properly by configuring its internal structure
        # Use grid_rowconfigure and grid_columnconfigure for proper expansion
        self.scrollFrame.grid_rowconfigure(0, weight=1)
        self.scrollFrame.grid_columnconfigure(0, weight=1)

        # Control buttons frame
        self.buttonFrame = Frame(self.mainFrame)
        self.buttonFrame.pack(fill="x", padx=10, pady=10)

        # Button bar
        bar = BtnBar(self.buttonFrame)
        bar.pack(side="right", padx=5)
        bar.addBtns([
            BtnConfig(name="Add Section", callback=self.addSectionDialog),
            BtnConfig(name="Add Option", callback=self.addOptionDialog),
            BtnConfig(name="Open ", callback=self.open),
            BtnConfig(name="Reload", callback=self.reloadConfig),
            BtnConfig(name="Save", callback=self.saveChanges),
        ])

    def loadConfig(self):
        """Load configuration and populate the UI"""
        # Clear existing widgets
        for widget in self.scrollFrame.winfo_children():
            widget.destroy()

        self.widgets = {}

        # Load sections
        sections = self.config.sections()

        if not sections:
            # No sections found
            noConfigLabel = Label(self.scrollFrame, text="No configuration sections found",
                                  font=("Arial", 12))
            noConfigLabel.pack(pady=20)
            return

        # Create UI for each section
        for section in sections:
            self.createSectionUi(section)

    def createSectionUi(self, section):
        """Create UI for a configuration section"""
        # Section frame - CHANGED to fill both and expand
        sectionFrame = Frame(self.scrollFrame)
        sectionFrame.pack(fill="both", expand=True, padx=5, pady=10)

        # Section title
        sectionLabel = Label(sectionFrame, text=f"[{section}]",
                             font=("Arial", 22, "bold"))
        sectionLabel.pack(anchor="w", padx=10, pady=5)

        # Get section items
        items = self.config.items(section)

        # Initialize widgets dict for this section
        if section not in self.widgets:
            self.widgets[section] = {}

        if not items:
            # No items in section
            emptyLabel = Label(sectionFrame, text="No configuration items",
                               font=("Arial", 10))
            emptyLabel.pack(anchor="w", padx=20, pady=5)
            return

        # Create UI for each item
        for key, value in items:
            self.createItemUi(sectionFrame, section, key, value)

    def createItemUi(self, parent, section, key, value):
        """Create UI for a configuration item"""
        # Item frame
        itemFrame = Frame(parent)
        itemFrame.pack(fill="x", padx=20, pady=5)

        # Key label
        keyLabel = Label(itemFrame, text=f"{key} =", font=("Arial", 22))
        keyLabel.pack(side="left", padx=(0, 5))

        # Value entry
        valueEntry = Entry(itemFrame)
        valueEntry.insert(0, value)
        valueEntry.pack(side="left", padx=[0, 5], fill=tk.X, expand=True)

        # Store widget reference
        if section not in self.widgets:
            self.widgets[section] = {}
        self.widgets[section][key] = valueEntry

    def getCurrentValues(self):
        """Get current values from UI widgets"""
        currentValues = {}

        for section in self.widgets:
            currentValues[section] = {}
            for key, widget in self.widgets[section].items():
                currentValues[section][key] = widget.get()

        return currentValues

    def saveChanges(self):
        """Save changes to configuration file"""
        try:
            currentValues = self.getCurrentValues()

            # Update configuration
            for section in currentValues:
                for key, value in currentValues[section].items():
                    self.config.add_option(section, key, value)

            # Write to file
            if self.config.write():
                print(f"Configuration saved successfully to {self.configFile}")
                # Show success message
                self.showMessage(
                    "Success", "Configuration saved successfully!")
            else:
                print(f"Failed to save configuration to {self.configFile}")
                self.showMessage("Error", "Failed to save configuration!")

        except Exception as e:
            print(f"Error saving configuration: {e}")
            self.showMessage("Error", f"Error saving configuration: {e}")

    def reloadConfig(self):
        """Reload configuration from file"""
        try:
            # Reload configuration
            self.config = Config(self.configFile)
            self.loadConfig()
            print(f"Configuration reloaded from {self.configFile}")
            self.showMessage("Info", "Configuration reloaded!")
        except Exception as e:
            print(f"Error reloading configuration: {e}")
            self.showMessage("Error", f"Error reloading configuration: {e}")

    def showMessage(self, title, message):
        """Show a simple message dialog"""
        InfoBox(self, title, message)

    def setConfigFile(self, configFile):
        """Set a new configuration file"""
        self.configFile = configFile
        self.config = Config(self.configFile)
        self.titleLabel.configure(
            text=f"Configuration Editor: {self.configFile}")
        self.loadConfig()

    def getConfigFile(self):
        """Get the current configuration file"""
        return self.configFile

    def addSection(self, sectionName):
        """
        Add a new section to the configuration file
        
        Args:
            sectionName (str): Name of the section to add
        """
        try:
            # Add section to config
            result = self.config.add_section(sectionName)
            if result:
                # Reload the UI to show the new section
                self.loadConfig()
                print(f"Section '{sectionName}' added successfully")
                self.showMessage("Success", f"Section '{sectionName}' added successfully!")
                return True
            else:
                print(f"Failed to add section '{sectionName}'")
                self.showMessage("Error", f"Failed to add section '{sectionName}'!")
                return False
        except Exception as e:
            print(f"Error adding section: {e}")
            self.showMessage("Error", f"Error adding section: {e}")
            return False

    def addOption(self, section, option, value=""):
        """
        Add a new option to a section in the configuration file
        
        Args:
            section (str): Name of the section
            option (str): Name of the option to add
            value (str): Value for the option (default: "")
        """
        try:
            # Add option to config
            if self.config.add_option(section, option, value):
                # Reload the UI to show the new option
                self.loadConfig()
                print(f"Option '{option}' added to section '{section}' successfully")
                self.showMessage("Success", f"Option '{option}' added to section '{section}' successfully!")
                return True
            else:
                print(f"Failed to add option '{option}' to section '{section}'")
                self.showMessage("Error", f"Failed to add option '{option}' to section '{section}'!")
                return False
        except Exception as e:
            print(f"Error adding option: {e}")
            self.showMessage("Error", f"Error adding option: {e}")
            return False

    def addSectionDialog(self):
        """Show dialog to add a new section using InputBox"""
        # Use InputBox for a cleaner, more consistent dialog
        dialog = InputBox(
            title="Add New Section",
            text="Section name:",
            inputType='text',
            allowEmpty=False
        )
        
        # Get the section name from the dialog
        section_name = dialog.showInputBox()
        
        # If user provided a section name (not cancelled and not empty)
        if section_name:
            self.addSection(section_name)

    def addOptionDialog(self):
        """Show dialog to add a new option using basic.Toplevel, OptionBar, and InputBar"""
        # Get available sections
        sections = self.config.sections()
        if not sections:
            self.showMessage("Error", "No sections available. Please add a section first!")
            return
        
        # Create dialog window using basic.Toplevel
        dialog = Toplevel(self)
        dialog.title("Add New Option")
        dialog.geometry("400x300")
        dialog.resizable(False, False)
        dialog.transient(self)
        dialog.grab_set()
        
        # Center dialog
        dialog.update_idletasks()
        x = self.winfo_rootx() + (self.winfo_width() // 2) - (dialog.winfo_width() // 2)
        y = self.winfo_rooty() + (self.winfo_height() // 2) - (dialog.winfo_height() // 2)
        dialog.geometry(f"+{x}+{y}")
        
        # Create main frame for content
        main_frame = Frame(dialog)
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Section selection using OptionBar
        section_bar = OptionBar(main_frame, title="Select Section:", options=sections, 
                               defaultOption=sections[0], titleFont=("Arial", 14, "bold"))
        section_bar.pack(fill="x", pady=(0, 20))
        
        # Option name using InputBar
        option_bar = InputBar(main_frame, title="Option Name:")
        option_bar.pack(fill="x", pady=(0, 20))
        option_bar.configInput(placeholder_text="Enter option name...", font=("Arial", 12))
        
        # Option value using InputBar
        value_bar = InputBar(main_frame, title="Option Value:", default="")
        value_bar.pack(fill="x", pady=(0, 20))
        value_bar.configInput(placeholder_text="Enter option value...", font=("Arial", 12))
        
        # Focus on option name input
        option_bar.focus()
        
        def on_ok():
            section = section_bar.getSelectedOption()
            option_name = option_bar.getValue().strip()
            option_value = value_bar.getValue().strip()
            
            if option_name:
                if self.addOption(section, option_name, option_value):
                    dialog.destroy()
            else:
                self.showMessage("Error", "Please enter an option name!")
        
        def on_cancel():
            dialog.destroy()
        
        # Buttons frame using BtnBar
        button_frame = Frame(main_frame)
        button_frame.pack(fill="x", pady=20)
        
        btn_bar = BtnBar(button_frame)
        btn_bar.pack(side="right")
        btn_bar.addBtns([
            BtnConfig(name="OK", callback=on_ok),
            BtnConfig(name="Cancel", callback=on_cancel)
        ])
        
        # Bind Enter key to OK
        dialog.bind('<Return>', lambda e: on_ok())
        dialog.bind('<Escape>', lambda e: on_cancel())
        
        # Bind Enter key to InputBars
        option_bar.bindReturn(lambda e: on_ok())
        value_bar.bindReturn(lambda e: on_ok())

    def open(self):
        """Open another config file"""
        """Open another config file"""
        try:
            path = filedialog.askopenfilename(
                title="Select Configuration File",
                filetypes=[("INI files", "*.ini"), ("All files", "*.*")]
            )
            if path:
                self.setConfigFile(path)
        except Exception as e:
            print(f"Error opening configuration file: {e}")
            self.showMessage("Error", f"Error opening configuration file: {e}")
import tkinter as tk
import json
from .basic import Frame, Entry, Label, ScrollableFrame, Toplevel
from .BtnBar import BtnBar, BtnConfig
from .InfoBox import InfoBox
from .InputBox import InputBox
from .OptionBar import OptionBar
from .InputBar import InputBar
from ..util.JsonFile import JsonFile


class JsonEditor(Frame):
    """JSON file editor widget"""

    def __init__(self, master, jsonFile=None, **kwargs):
        """
        Initialize the JsonEditor widget

        Args:
            master: Parent widget
            jsonFile: Path to JSON file (default: example.json)
            **kwargs: Additional arguments for Frame
        """
        super().__init__(master, **kwargs)

        self.jsonFile = jsonFile or 'example.json'
        self.jsonData = JsonFile(self.jsonFile)
        self.widgets = {}  # Store references to UI widgets

        self.setupUi()
        self.loadJson()

    def setupUi(self):
        """Setup the user interface"""
        # Create main container
        self.mainFrame = Frame(self)
        self.mainFrame.pack(fill="both", expand=True, padx=10, pady=10)

        # Title
        self.titleLabel = Label(self.mainFrame, text=f"{self.jsonFile}",
                                font=("Arial", 26, "bold"))
        self.titleLabel.pack(pady=10)

        # Scrollable frame for JSON items - FIXED expansion
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
            BtnConfig(name="Add Item", callback=self.addItemDialog),
            BtnConfig(name="Open", callback=self.open),
            BtnConfig(name="Reload", callback=self.reloadJson),
            BtnConfig(name="Save", callback=self.saveChanges),
        ])

    def loadJson(self):
        """Load JSON data and populate the UI"""
        # Clear existing widgets
        for widget in self.scrollFrame.winfo_children():
            widget.destroy()

        self.widgets = {}

        # Load JSON items
        items = list(self.jsonData.items())

        if not items:
            # No items found
            noJsonLabel = Label(self.scrollFrame, text="No JSON items found",
                                font=("Arial", 12))
            noJsonLabel.pack(pady=20)
            return

        # Create UI for each item
        for key, value in items:
            self.createItemUi(key, value)

    def createItemUi(self, key, value):
        """Create UI for a JSON item"""
        # Item frame
        itemFrame = Frame(self.scrollFrame)
        itemFrame.pack(fill="x", padx=5, pady=5)

        # Key label
        keyLabel = Label(itemFrame, text=f"{key} =", font=("Arial", 16))
        keyLabel.pack(side="left", padx=(0, 5))

        # Value entry - use json.dumps to properly display complex values
        valueEntry = Entry(itemFrame)
        valueEntry.insert(0, json.dumps(value, ensure_ascii=False))
        valueEntry.pack(side="left", padx=[0, 5], fill=tk.X, expand=True)

        # Remove button
        removeBtn = BtnConfig(name="Remove", callback=lambda: self.remove(key))
        removeBtnBar = BtnBar(itemFrame)
        removeBtnBar.pack(side="right", padx=5)
        removeBtnBar.addBtn(removeBtn)

        # Store widget reference
        self.widgets[key] = valueEntry

    def getCurrentValues(self):
        """Get current values from UI widgets"""
        currentValues = {}

        for key, widget in self.widgets.items():
            try:
                # Try to parse the value as JSON
                currentValues[key] = json.loads(widget.get())
            except json.JSONDecodeError:
                # If parsing fails, treat as string
                currentValues[key] = widget.get()

        return currentValues

    def saveChanges(self):
        """Save changes to JSON file"""
        try:
            currentValues = self.getCurrentValues()

            # Update JSON data
            for key, value in currentValues.items():
                self.jsonData.set(key, value)

            # Save to file
            self.jsonData.save()
            print(f"JSON data saved successfully to {self.jsonFile}")
            # Show success message
            self.showMessage(
                "Success", "JSON data saved successfully!")
        except Exception as e:
            print(f"Error saving JSON data: {e}")
            self.showMessage("Error", f"Error saving JSON data: {e}")



    def reloadJson(self):
        """Reload JSON data from file"""
        try:
            # Reload JSON data
            self.jsonData = JsonFile(self.jsonFile)
            self.loadJson()
            print(f"JSON data reloaded from {self.jsonFile}")
            self.showMessage("Info", "JSON data reloaded!")
        except Exception as e:
            print(f"Error reloading JSON data: {e}")
            self.showMessage("Error", f"Error reloading JSON data: {e}")

    def showMessage(self, title, message):
        """Show a simple message dialog"""
        InfoBox(self, title, message)

    def setJsonFile(self, jsonFile):
        """Set a new JSON file"""
        self.jsonFile = jsonFile
        self.jsonData = JsonFile(self.jsonFile)
        self.titleLabel.configure(
            text=f"JSON Editor: {self.jsonFile}")
        self.loadJson()

    def getJsonFile(self):
        """Get the current JSON file"""
        return self.jsonFile

    def add(self, key, value):
        """
        Add a new item to the JSON file
        
        Args:
            key (str): Key for the new item
            value: Value for the new item
        """
        try:
            # Add item to JSON data
            self.jsonData.set(key, value)
            # Reload the UI to show the new item
            self.loadJson()
            print(f"Item '{key}' added successfully")
            self.showMessage("Success", f"Item '{key}' added successfully!")
            return True
        except Exception as e:
            print(f"Error adding item: {e}")
            self.showMessage("Error", f"Error adding item: {e}")
            return False

    def update(self, key, value):
        """
        Update an existing item in the JSON file
        
        Args:
            key (str): Key of the item to update
            value: New value for the item
        """
        try:
            # Update item in JSON data
            self.jsonData.set(key, value)
            # Reload the UI to show the updated item
            self.loadJson()
            print(f"Item '{key}' updated successfully")
            self.showMessage("Success", f"Item '{key}' updated successfully!")
            return True
        except Exception as e:
            print(f"Error updating item: {e}")
            self.showMessage("Error", f"Error updating item: {e}")
            return False

    def remove(self, key):
        """
        Remove an item from the JSON file
        
        Args:
            key (str): Key of the item to remove
        """
        try:
            # Remove item from JSON data
            del self.jsonData[key]
            # Reload the UI to show the removed item
            self.loadJson()
            print(f"Item '{key}' removed successfully")
            self.showMessage("Success", f"Item '{key}' removed successfully!")
            return True
        except Exception as e:
            print(f"Error removing item: {e}")
            self.showMessage("Error", f"Error removing item: {e}")
            return False

    def addItemDialog(self):
        """Show dialog to add a new item using InputBox and InputBar"""
        # Create dialog window using basic.Toplevel
        dialog = Toplevel(self)
        dialog.title("Add New Item")
        dialog.geometry("400x200")
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
        
        # Key input using InputBar
        key_bar = InputBar(main_frame, title="Key:")
        key_bar.pack(fill="x", pady=(0, 10))
        key_bar.configInput(placeholder_text="Enter key name...", font=("Arial", 12))
        
        # Value input using InputBar
        value_bar = InputBar(main_frame, title="Value:")
        value_bar.pack(fill="x", pady=(0, 20))
        value_bar.configInput(placeholder_text="Enter value...", font=("Arial", 12))
        
        # Focus on key input
        key_bar.focus()
        
        def on_ok():
            key = key_bar.getValue().strip()
            value = value_bar.getValue().strip()
            
            if key and value:
                try:
                    # Try to parse value as JSON
                    converted_value = json.loads(value)
                except json.JSONDecodeError:
                    # If parsing fails, treat as string
                    converted_value = value
                
                if self.add(key, converted_value):
                    dialog.destroy()
            else:
                self.showMessage("Error", "Please enter both key and value!")
        
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
        key_bar.bindReturn(lambda e: on_ok())
        value_bar.bindReturn(lambda e: on_ok())

    def open(self):
        """Open another JSON file"""
        from tkinter import filedialog
        try:
            path = filedialog.askopenfilename(
                title="Select JSON File",
                filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
            )
            if path:
                self.setJsonFile(path)
        except Exception as e:
            print(f"Error opening JSON file: {e}")
            self.showMessage("Error", f"Error opening JSON file: {e}")
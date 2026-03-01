import tkinter as tk
import customtkinter as ctk
from tomwidgets.widget.basic import Textbox


class TextboxExample(ctk.CTk):
    """Main application class for Textbox widget example."""

    def __init__(self):
        """Initialize the application."""
        super().__init__()

        self.title("Textbox Widget Example - tomwidgets")
        self.geometry("900x700")

        # Configure grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)  # Title
        self.grid_rowconfigure(1, weight=0)  # Description
        self.grid_rowconfigure(2, weight=1)  # Textbox widget
        self.grid_rowconfigure(3, weight=0)  # Controls

        self.setupUi()

    def setupUi(self):
        """Setup the user interface."""
        # Title label
        title_label = ctk.CTkLabel(self, text="Text Widget Example",
                                   font=ctk.CTkFont(size=20, weight="bold"))
        title_label.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

        # Description
        description_label = ctk.CTkLabel(self,
                                         text="This example demonstrates the Textbox widget - a customtkinter CTkTextbox with enhanced styling capabilities including per-text color and size formatting, state management, and widget insertion.",
                                         font=ctk.CTkFont(size=12),
                                         justify="left",
                                         wraplength=860)
        description_label.grid(row=1, column=0, padx=20,
                               pady=(0, 20), sticky="ew")

        # Create the Textbox widget
        self.textbox = Textbox(self, wrap="word", width=80, height=20)
        self.textbox.grid(row=2, column=0, padx=20,
                          pady=(0, 20), sticky="nsew")

        # Add scrollbar to textbox
        scrollbar = ctk.CTkScrollbar(self, command=self.textbox.yview)
        scrollbar.grid(row=2, column=1, padx=(
            0, 20), pady=(0, 20), sticky="ns")
        self.textbox.configure(yscrollcommand=scrollbar.set)

        # Controls frame
        self.setupControls()

        # Populate with sample content
        self.populateSampleContent()

        # Test all methods
        self.testAllMethods()

    def setupControls(self):
        """Setup control buttons and inputs."""
        controls_frame = ctk.CTkFrame(self)
        controls_frame.grid(row=3, column=0, padx=20, pady=20, sticky="ew")
        controls_frame.grid_columnconfigure(0, weight=1)

        # Control buttons - Row 1
        button_frame1 = ctk.CTkFrame(controls_frame)
        button_frame1.grid(row=0, column=0, padx=10, pady=5, sticky="ew")

        # Configure button grid for row 1
        for i in range(6):
            button_frame1.grid_columnconfigure(i, weight=1)

        # Clear button
        clear_btn = ctk.CTkButton(button_frame1, text="Clear Text",
                                  command=self.clearText)
        clear_btn.grid(row=0, column=0, padx=5, pady=5)

        # Enable/Disable button
        self.toggle_btn = ctk.CTkButton(button_frame1, text="Disable",
                                        command=self.toggleState)
        self.toggle_btn.grid(row=0, column=1, padx=5, pady=5)

        # Get Text button
        get_text_btn = ctk.CTkButton(button_frame1, text="Get Text",
                                     command=self.getText)
        get_text_btn.grid(row=0, column=2, padx=5, pady=5)

        # Insert at position button
        insert_pos_btn = ctk.CTkButton(button_frame1, text="Insert at Line 1",
                                       command=self.insertAtPosition)
        insert_pos_btn.grid(row=0, column=3, padx=5, pady=5)

        # Insert at specific position button
        insert_specific_btn = ctk.CTkButton(button_frame1, text="Insert at 2.5",
                                            command=self.insertAtSpecificPosition)
        insert_specific_btn.grid(row=0, column=4, padx=5, pady=5)

        # Add widget button
        add_widget_btn = ctk.CTkButton(button_frame1, text="Add Button",
                                       command=self.addWidgetToTextbox)
        add_widget_btn.grid(row=0, column=5, padx=5, pady=5)

        # Styling controls frame
        style_frame = ctk.CTkFrame(controls_frame)
        style_frame.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

        # Configure style frame grid
        for i in range(4):
            style_frame.grid_columnconfigure(i, weight=1)

        # Text input
        text_label = ctk.CTkLabel(style_frame, text="Text:")
        text_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.text_entry = ctk.CTkEntry(
            style_frame, placeholder_text="Enter text to add")
        self.text_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        # Color selection
        color_label = ctk.CTkLabel(style_frame, text="Color:")
        color_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        self.color_var = ctk.StringVar(style_frame, value="black")
        color_combo = ctk.CTkComboBox(style_frame,
                                      values=["black", "red", "blue",
                                              "green", "purple", "orange", "brown",
                                              "yellow", "cyan", "magenta"],
                                      variable=self.color_var)
        color_combo.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        # Size selection
        size_label = ctk.CTkLabel(style_frame, text="Size:")
        size_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")

        self.size_var = ctk.StringVar(style_frame, value="12")
        size_combo = ctk.CTkComboBox(style_frame,
                                     values=["8", "10", "12", "14",
                                             "16", "18", "20", "24", "28", "32"],
                                     variable=self.size_var)
        size_combo.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

        # Insert position input
        pos_label = ctk.CTkLabel(style_frame, text="Position:")
        pos_label.grid(row=0, column=2, padx=5, pady=5, sticky="w")

        self.pos_var = ctk.StringVar(style_frame, value="end")
        pos_combo = ctk.CTkComboBox(style_frame,
                                    values=["1.0", "2.0", "3.0", "4.0", "5.0", "end"],
                                    variable=self.pos_var)
        pos_combo.grid(row=0, column=3, padx=5, pady=5, sticky="ew")

        # Add text button
        add_text_btn = ctk.CTkButton(style_frame, text="Add Text",
                                     command=self.addStyledText)
        add_text_btn.grid(row=1, column=2, rowspan=2, padx=10, pady=10)

        # Insert with position button
        insert_pos_btn = ctk.CTkButton(style_frame, text="Insert at Position",
                                       command=self.insertWithPosition)
        insert_pos_btn.grid(row=1, column=3, rowspan=2, padx=10, pady=10)

        # Advanced controls frame
        advanced_frame = ctk.CTkFrame(controls_frame)
        advanced_frame.grid(row=2, column=0, padx=5, pady=5, sticky="ew")

        # Configure advanced frame grid
        for i in range(4):
            advanced_frame.grid_columnconfigure(i, weight=1)

        # State info button
        state_info_btn = ctk.CTkButton(advanced_frame, text="Check State",
                                       command=self.checkState)
        state_info_btn.grid(row=0, column=0, padx=5, pady=5)

        # Box info button
        box_info_btn = ctk.CTkButton(advanced_frame, text="Box Info",
                                     command=self.checkBoxInfo)
        box_info_btn.grid(row=0, column=1, padx=5, pady=5)

        # Enable button
        enable_btn = ctk.CTkButton(advanced_frame, text="Enable",
                                   command=self.enableTextbox)
        enable_btn.grid(row=0, column=2, padx=5, pady=5)

        # Disable button
        disable_btn = ctk.CTkButton(advanced_frame, text="Disable",
                                    command=self.disableTextbox)
        disable_btn.grid(row=0, column=3, padx=5, pady=5)

    def populateSampleContent(self):
        """Populate the textbox with sample content."""
        # Clear any existing content
        self.textbox.delete("1.0", tk.END)

        # Add sample content demonstrating different features
        self.textbox.append("Textbox Widget Demonstration\n", "black", 20)
        self.textbox.append("=" * 60 + "\n\n", "black", 12)

        # Basic text with different colors
        self.textbox.append("1. Basic Text Styling:\n", "black", 16)
        self.textbox.append("This is normal black text. ", "black")
        self.textbox.append("This is red text. ", "red")
        self.textbox.append("This is blue text. ", "blue")
        self.textbox.append("This is green text. ", "green")
        self.textbox.append("This is purple text. ", "purple")
        self.textbox.append("This is orange text. ", "orange")
        self.textbox.append("This is brown text.\n\n", "brown")

        # Text with different sizes
        self.textbox.append("2. Font Size Variations:\n", "black", 16)
        self.textbox.append("Tiny text (8pt) ", "black", 8)
        self.textbox.append("Small text (10pt) ", "black", 10)
        self.textbox.append("Normal text (12pt) ", "black", 12)
        self.textbox.append("Medium text (16pt) ", "black", 16)
        self.textbox.append("Large text (20pt) ", "black", 20)
        self.textbox.append("Very large text (24pt) ", "black", 24)
        self.textbox.append("Huge text (28pt) ", "black", 28)
        self.textbox.append("Giant text (32pt)\n\n", "black", 32)

        # Combined color and size
        self.textbox.append("3. Combined Color and Size:\n", "black", 16)
        self.textbox.append("Small red text ", "red", 10)
        self.textbox.append("Medium blue text ", "blue", 16)
        self.textbox.append("Large green text ", "green", 20)
        self.textbox.append("Huge purple text ", "purple", 24)
        self.textbox.append("Giant orange text\n\n", "orange", 32)

        # Multi-line text with styling
        self.textbox.append("4. Multi-line Styled Text:\n", "black", 16)
        self.textbox.append("Line 1: Normal text\n", "black")
        self.textbox.append("Line 2: ", "black")
        self.textbox.append("Red bold text\n", "red", 14)
        self.textbox.append("Line 3: ", "black")
        self.textbox.append("Blue large text\n", "blue", 18)
        self.textbox.append("Line 4: Mixed ", "black")
        self.textbox.append("styles ", "purple", 16)
        self.textbox.append("in one line\n", "orange", 12)
        self.textbox.append("Line 5: ", "black")
        self.textbox.append("Yellow ", "yellow", 14)
        self.textbox.append("Cyan ", "cyan", 16)
        self.textbox.append("Magenta text\n\n", "magenta", 18)

        # Insert at specific positions
        self.textbox.append(
            "5. Insert at Specific Positions:\n", "black", 16)
        self.textbox.append("Original text line.\n", "black")

        # Insert at beginning of line 1
        self.textbox.insertTo("1.0", "[START] ", "purple", 14)

        # Insert in the middle
        self.textbox.insertTo("8.15", "[MIDDLE] ", "orange", 16)

        # Insert at end
        self.textbox.insertTo(tk.END, "[END] ", "brown", 14)

        self.textbox.append(
            "\nUse the controls below to test all Textbox widget functionality.\n", "black", 12)

    def testAllMethods(self):
        """Test all Textbox methods to ensure they work correctly."""
        print("Testing all Textbox methods...")
        
        # Test state management methods
        print("1. Testing state management methods:")
        original_state = self.textbox.state()
        print(f"  - Original state: {original_state}")
        
        # Test disable/enable
        self.textbox.disable()
        disabled_state = self.textbox.state()
        print(f"  - After disable: {disabled_state}")
        print(f"  - isEnabled(): {self.textbox.isEnabled()}")
        
        self.textbox.enable()
        enabled_state = self.textbox.state()
        print(f"  - After enable: {enabled_state}")
        print(f"  - isEnabled(): {self.textbox.isEnabled()}")
        
        # Test box method
        print("2. Testing box method:")
        box = self.textbox.box()
        print(f"  - Box type: {type(box)}")
        
        # Test append method with various parameters
        print("3. Testing append method:")
        self.textbox.append("\n[Method Test] Append with default params. ", "black")
        self.textbox.append("Append with color. ", "red")
        self.textbox.append("Append with size. ", "black", 16)
        self.textbox.append("Append with color and size.\n", "blue", 18)
        
        # Test insertTo method with various positions
        print("4. Testing insertTo method:")
        self.textbox.insertTo("end", "[Method Test] Insert at end. ", "green")
        self.textbox.insertTo("1.0", "[START] ", "purple", 14)
        self.textbox.insertTo("3.10", "[MIDDLE] ", "orange", 12)
        
        # Test addWidget method
        print("5. Testing addWidget method:")
        test_button = ctk.CTkButton(self.textbox, text="Test Button", 
                                   command=lambda: print("Test button clicked!"))
        self.textbox.addWidget(test_button, margin=" ")
        self.textbox.append("[Widget added] ", "brown", 12)
        
        print("All Textbox methods tested successfully!")
        self.textbox.append("\n[TEST COMPLETE] All methods tested successfully!\n", "green", 14)

    def clearText(self):
        """Clear all text from the textbox."""
        self.textbox.delete("1.0", tk.END)
        self.textbox.append(
            "Text cleared. Add new text using the controls below.\n", "black", 12)

    def toggleState(self):
        """Toggle between enabled and disabled states."""
        if self.textbox.isEnabled():
            self.textbox.disable()
            self.toggle_btn.configure(text="Enable")
        else:
            self.textbox.enable()
            self.toggle_btn.configure(text="Disable")

    def getText(self):
        """Get and display the current text content."""
        content = self.textbox.get("1.0", tk.END)
        print("Current text content:")
        print("-" * 60)
        print(content)
        print("-" * 60)

        # Show a message
        self.textbox.insertTo(
            tk.END, "\nText content printed to console.\n", "blue", 12)

    def insertAtPosition(self):
        """Insert text at line 1 position."""
        self.textbox.insertTo("1.0", "[INSERTED AT START] ", "brown", 14)

    def insertAtSpecificPosition(self):
        """Insert text at line 2, position 5."""
        self.textbox.insertTo("2.5", "[INSERTED AT 2.5] ", "purple", 12)

    def insertWithPosition(self):
        """Insert text at the specified position."""
        text = self.text_entry.get()
        color = self.color_var.get()
        size = int(self.size_var.get()) if self.size_var.get() else None
        position = self.pos_var.get()

        if text:
            print(f"Inserting text: {text} at position: {position} with color: {color} and size: {size}")
            self.textbox.insertTo(position, text + " ", color, size)
            self.text_entry.delete(0, tk.END)

    def addStyledText(self):
        """Add text with the specified color and size."""
        text = self.text_entry.get()
        color = self.color_var.get()
        size = int(self.size_var.get()) if self.size_var.get() else None

        if text:
            print(f"Adding text: {text} with color: {color} and size: {size}")
            self.textbox.append(text + " ", color, size)
            self.text_entry.delete(0, tk.END)

    def addWidgetToTextbox(self):
        """Add a button widget to the textbox."""
        button = ctk.CTkButton(self.textbox, text="Click Me!", 
                              command=lambda: print("Button in textbox clicked!"))
        self.textbox.addWidget(button, margin=" ")
        self.textbox.append("Button added to textbox. ", "green", 12)

    def checkState(self):
        """Check and display the current state of the textbox."""
        state = self.textbox.state()
        is_enabled = self.textbox.isEnabled()
        print(f"Textbox state: {state}")
        print(f"Textbox is enabled: {is_enabled}")
        
        self.textbox.append(f"\nState checked: {state}, Enabled: {is_enabled}\n", "blue", 12)

    def checkBoxInfo(self):
        """Check and display information about the underlying box."""
        box = self.textbox.box()
        print(f"Box type: {type(box)}")
        print(f"Box configuration: {box.configure()}")
        
        self.textbox.append("\nBox information printed to console.\n", "purple", 12)

    def enableTextbox(self):
        """Enable the textbox."""
        self.textbox.enable()
        self.textbox.append("\nTextbox enabled.\n", "green", 12)
        self.toggle_btn.configure(text="Disable")

    def disableTextbox(self):
        """Disable the textbox."""
        self.textbox.disable()
        self.textbox.append("\nTextbox disabled.\n", "red", 12)
        self.toggle_btn.configure(text="Enable")


def main():
    """Main function to run the example."""
    # Set customtkinter appearance
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    # Create and run the application
    app = TextboxExample()
    app.mainloop()


if __name__ == "__main__":
    main()
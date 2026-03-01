import tkinter as tk
import customtkinter as ctk
from tomwidgets.widget.basic import Text


class TextExample(ctk.CTk):
    """Main application class for Text widget example."""

    def __init__(self):
        """Initialize the application."""
        super().__init__()

        self.title("Text Widget Example - tomwidgets")
        self.geometry("800x600")

        # Configure grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)  # Title
        self.grid_rowconfigure(1, weight=0)  # Description
        self.grid_rowconfigure(2, weight=1)  # Text widget
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
                                         text="This example demonstrates the Text widget - a tkinter Text widget with enhanced styling capabilities including per-text color and size formatting using tags.",
                                         font=ctk.CTkFont(size=12),
                                         justify="left",
                                         wraplength=760)
        description_label.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="ew")

        # Create the Text widget
        self.text_widget = Text(self, wrap="word", width=80, height=20)
        self.text_widget.grid(row=2, column=0, padx=20, pady=(0, 20), sticky="nsew")

        # Add scrollbar to text widget
        scrollbar = ctk.CTkScrollbar(self, command=self.text_widget.yview)
        scrollbar.grid(row=2, column=1, padx=(0, 20), pady=(0, 20), sticky="ns")
        self.text_widget.configure(yscrollcommand=scrollbar.set)

        # Controls frame
        self.setupControls()

        # Populate with sample content
        self.populateSampleContent()

    def setupControls(self):
        """Setup control buttons and inputs."""
        controls_frame = ctk.CTkFrame(self)
        controls_frame.grid(row=3, column=0, padx=20, pady=20, sticky="ew")
        controls_frame.grid_columnconfigure(0, weight=1)

        # Control buttons
        button_frame = ctk.CTkFrame(controls_frame)
        button_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        # Configure button grid
        for i in range(4):
            button_frame.grid_columnconfigure(i, weight=1)

        # Clear button
        clear_btn = ctk.CTkButton(button_frame, text="Clear Text",
                                   command=self.clearText)
        clear_btn.grid(row=0, column=0, padx=5, pady=5)

        # Enable/Disable button
        self.toggle_btn = ctk.CTkButton(button_frame, text="Disable",
                                         command=self.toggleState)
        self.toggle_btn.grid(row=0, column=1, padx=5, pady=5)

        # Get Text button
        get_text_btn = ctk.CTkButton(button_frame, text="Get Text",
                                      command=self.getText)
        get_text_btn.grid(row=0, column=2, padx=5, pady=5)

        # Insert at position button
        insert_pos_btn = ctk.CTkButton(button_frame, text="Insert at Line 1",
                                        command=self.insertAtPosition)
        insert_pos_btn.grid(row=0, column=3, padx=5, pady=5)

        # Styling controls frame
        style_frame = ctk.CTkFrame(controls_frame)
        style_frame.grid(row=1, column=0, columnspan=4, padx=5, pady=5, sticky="ew")

        # Configure style frame grid
        for i in range(3):
            style_frame.grid_columnconfigure(i, weight=1)

        # Text input
        text_label = ctk.CTkLabel(style_frame, text="Text:")
        text_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.text_entry = ctk.CTkEntry(style_frame, placeholder_text="Enter text to add")
        self.text_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        # Color selection
        color_label = ctk.CTkLabel(style_frame, text="Color:")
        color_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        self.color_var = ctk.StringVar(style_frame, value="black")
        color_combo = ctk.CTkComboBox(style_frame,
                                      values=["black", "red", "blue", "green", "purple", "orange", "brown"],
                                      variable=self.color_var)
        color_combo.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        # Size selection
        size_label = ctk.CTkLabel(style_frame, text="Size:")
        size_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")

        self.size_var = ctk.StringVar(style_frame, value="12")
        size_combo = ctk.CTkComboBox(style_frame,
                                      values=["8", "10", "12", "14", "16", "18", "20", "24", "28"],
                                      variable=self.size_var)
        size_combo.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

        # Add text button
        add_text_btn = ctk.CTkButton(style_frame, text="Add Text",
                                     command=self.addStyledText)
        add_text_btn.grid(row=0, column=2, rowspan=3, padx=10, pady=10)

    def populateSampleContent(self):
        """Populate the text widget with sample content."""
        # Clear any existing content
        self.text_widget.delete("1.0", tk.END)

        # Add sample content demonstrating different features
        self.text_widget.append("Text Widget Demonstration\n", "black", 18)
        self.text_widget.append("=" * 50 + "\n\n", "black", 12)

        # Basic text with different colors
        self.text_widget.append("1. Basic Text Styling:\n", "black", 16)
        self.text_widget.append("This is normal black text. ", "black")
        self.text_widget.append("This is red text. ", "red")
        self.text_widget.append("This is blue text. ", "blue")
        self.text_widget.append("This is green text.\n\n", "green")

        # Text with different sizes
        self.text_widget.append("2. Font Size Variations:\n", "black", 16)
        self.text_widget.append("Small text (8pt) ", "black", 8)
        self.text_widget.append("Normal text (12pt) ", "black", 12)
        self.text_widget.append("Large text (18pt) ", "black", 18)
        self.text_widget.append("Very large text (24pt)\n\n", "black", 24)

        # Combined color and size
        self.text_widget.append("3. Combined Color and Size:\n", "black", 16)
        self.text_widget.append("Small red text ", "red", 10)
        self.text_widget.append("Medium blue text ", "blue", 16)
        self.text_widget.append("Large green text\n\n", "green", 20)

        # Multi-line text with styling
        self.text_widget.append("4. Multi-line Styled Text:\n", "black", 16)
        self.text_widget.append("Line 1: Normal text\n", "black")
        self.text_widget.append("Line 2: ", "black")
        self.text_widget.append("Red bold text\n", "red", 14)
        self.text_widget.append("Line 3: ", "black")
        self.text_widget.append("Blue large text\n", "blue", 18)
        self.text_widget.append("Line 4: Mixed ", "black")
        self.text_widget.append("styles ", "purple", 16)
        self.text_widget.append("in one line\n\n", "orange", 12)

        # Insert at specific positions
        self.text_widget.append("5. Insert at Specific Positions:\n", "black", 16)
        self.text_widget.append("Original text line.\n", "black")
        
        # Insert at beginning of line 1
        self.text_widget.insertTo("1.0", "[START] ", "purple", 14)
        
        # Insert in the middle
        self.text_widget.insertTo("6.15", "[MIDDLE] ", "orange", 16)
        
        self.text_widget.append("\nUse the controls below to test the widget functionality.\n", "black", 12)

    def clearText(self):
        """Clear all text from the widget."""
        self.text_widget.delete("1.0", tk.END)
        self.text_widget.append("Text cleared. Add new text using the controls below.\n", "black", 12)

    def toggleState(self):
        """Toggle between enabled and disabled states."""
        if self.text_widget.isEnabled():
            self.text_widget.disable()
            self.toggle_btn.configure(text="Enable")
        else:
            self.text_widget.enable()
            self.toggle_btn.configure(text="Disable")

    def getText(self):
        """Get and display the current text content."""
        content = self.text_widget.get("1.0", tk.END)
        print("Current text content:")
        print("-" * 50)
        print(content)
        print("-" * 50)
        
        # Show a message
        self.text_widget.insertTo(tk.END, "\nText content printed to console.\n", "blue", 12)

    def insertAtPosition(self):
        """Insert text at a specific position."""
        self.text_widget.insertTo("1.0", "[INSERTED AT START] ", "brown", 14)

    def addStyledText(self):
        """Add text with the specified color and size."""
        text = self.text_entry.get()
        color = self.color_var.get()
        size = int(self.size_var.get()) if self.size_var.get() else None

        if text:
            print(f"Adding text: {text} with color: {color} and size: {size}")
            self.text_widget.append(text + " ", color, size)
            self.text_entry.delete(0, tk.END)


def main():
    """Main function to run the example."""
    # Set customtkinter appearance
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    # Create and run the application
    app = TextExample()
    app.mainloop()


if __name__ == "__main__":
    main()
import tkinter as tk
from customtkinter import CTk, CTkButton, CTkLabel, CTkFrame
from tomwidgets.widget.PopMenu import PopMenu


class PopMenuExample(CTk):
    def __init__(self):
        super().__init__()
        
        self.title("PopMenu Example")
        self.geometry("600x400")
        
        # Create main frame
        main_frame = CTkFrame(self)
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Title label
        title_label = CTkLabel(main_frame, text="PopMenu Widget Example", 
                              font=("Arial", 20, "bold"))
        title_label.pack(pady=20)
        
        # Instructions
        instructions = CTkLabel(main_frame, 
                               text="Right-click anywhere in the window to open the context menu\n"
                                    "or click the buttons below to open specific menus",
                               font=("Arial", 14))
        instructions.pack(pady=10)
        
        # Create button frame
        button_frame = CTkFrame(main_frame)
        button_frame.pack(pady=30)
        
        # Button to open file menu
        file_button = CTkButton(button_frame, text="Open File Menu",
                               command=self.open_file_menu)
        file_button.pack(pady=10, padx=20)
        
        # Button to open edit menu
        edit_button = CTkButton(button_frame, text="Open Edit Menu", 
                               command=self.open_edit_menu)
        edit_button.pack(pady=10, padx=20)
        
        # Button to open format menu
        format_button = CTkButton(button_frame, text="Open Format Menu",
                                 command=self.open_format_menu)
        format_button.pack(pady=10, padx=20)
        
        # Status label
        self.status_label = CTkLabel(main_frame, text="No action performed yet",
                                   font=("Arial", 12))
        self.status_label.pack(pady=20)
        
        # Create menus
        self.create_menus()
        
        # Bind right-click to show context menu
        self.bind("<Button-3>", self.show_context_menu)
        main_frame.bind("<Button-3>", self.show_context_menu)
        button_frame.bind("<Button-3>", self.show_context_menu)
    
    def create_menus(self):
        """Create various popup menus for demonstration"""
        
        # Context menu with mixed commands
        self.context_menu = PopMenu(self, [
            ("New File", lambda: self.update_status("New File created")),
            ("Open File", lambda: self.update_status("Open File dialog")),
            ("Save", lambda: self.update_status("File saved")),
            None,  # Separator
            ("Cut", lambda: self.update_status("Cut to clipboard")),
            ("Copy", lambda: self.update_status("Copied to clipboard")),
            ("Paste", lambda: self.update_status("Pasted from clipboard")),
            None,  # Separator
            ("Preferences", lambda: self.update_status("Preferences opened"))
        ])
        
        # File menu with submenus
        self.file_menu = PopMenu(self, [
            ("New", lambda: self.update_status("New file created")),
            ("Open", lambda: self.update_status("Open file dialog")),
            ("Save", lambda: self.update_status("File saved")),
            ("Save As", lambda: self.update_status("Save As dialog")),
            None,  # Separator
            ("Recent Files", [
                ("document1.txt", lambda: self.update_status("Opened document1.txt")),
                ("document2.txt", lambda: self.update_status("Opened document2.txt")),
                ("project.py", lambda: self.update_status("Opened project.py")),
            ]),
            None,  # Separator
            ("Exit", lambda: self.quit())
        ])
        
        # Edit menu
        self.edit_menu = PopMenu(self, [
            ("Undo", lambda: self.update_status("Undo action")),
            ("Redo", lambda: self.update_status("Redo action")),
            None,  # Separator
            ("Find", lambda: self.update_status("Find dialog opened")),
            ("Replace", lambda: self.update_status("Replace dialog opened")),
            None,  # Separator
            ("Select All", lambda: self.update_status("All content selected")),
            ("Clear", lambda: self.update_status("Content cleared"))
        ])
        
        # Format menu with nested submenus
        self.format_menu = PopMenu(self, [
            ("Font", [
                ("Arial", lambda: self.update_status("Font set to Arial")),
                ("Times New Roman", lambda: self.update_status("Font set to Times New Roman")),
                ("Courier New", lambda: self.update_status("Font set to Courier New")),
                None,
                ("More Fonts...", lambda: self.update_status("Font dialog opened"))
            ]),
            ("Size", [
                ("Small", lambda: self.update_status("Font size set to small")),
                ("Medium", lambda: self.update_status("Font size set to medium")),
                ("Large", lambda: self.update_status("Font size set to large")),
                ("Custom...", lambda: self.update_status("Custom size dialog opened"))
            ]),
            ("Color", [
                ("Black", lambda: self.update_status("Color set to black")),
                ("Red", lambda: self.update_status("Color set to red")),
                ("Blue", lambda: self.update_status("Color set to blue")),
                ("Custom Color...", lambda: self.update_status("Color picker opened"))
            ]),
            None,  # Separator
            ("Bold", lambda: self.update_status("Bold toggled")),
            ("Italic", lambda: self.update_status("Italic toggled")),
            ("Underline", lambda: self.update_status("Underline toggled"))
        ])
    
    def show_context_menu(self, event):
        """Show context menu at mouse position"""
        self.context_menu.show()
    
    def open_file_menu(self):
        """Open file menu at button position"""
        self.file_menu.show()
    
    def open_edit_menu(self):
        """Open edit menu at button position"""
        self.edit_menu.show()
    
    def open_format_menu(self):
        """Open format menu at button position"""
        self.format_menu.show()
    
    def update_status(self, message):
        """Update the status label with the action performed"""
        self.status_label.configure(text=f"Action: {message}")


def main():
    """Main function to run the PopMenu example"""
    app = PopMenuExample()
    app.mainloop()


if __name__ == "__main__":
    main()
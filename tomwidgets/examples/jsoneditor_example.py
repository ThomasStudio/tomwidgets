import tkinter as tk
from customtkinter import CTk, CTkFrame, CTkLabel, CTkButton, CTkOptionMenu
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tomwidgets.widget.JsonEditor import JsonEditor
import json


class JsonEditorExample(CTk):
    def __init__(self):
        super().__init__()
        
        self.title("JsonEditor Example")
        self.geometry("800x600")
        
        # Create main frame
        main_frame = CTkFrame(self)
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Title label
        title_label = CTkLabel(main_frame, text="JsonEditor Widget Example", 
                              font=("Arial", 20, "bold"))
        title_label.pack(pady=20)
        
        # Instructions
        instructions = CTkLabel(main_frame, 
                               text="This example shows how to use the JsonEditor widget to edit JSON files.\n"
                                    "Select a JSON file from the dropdown below to load it into the editor.",
                               font=("Arial", 14))
        instructions.pack(pady=10)
        
        # File selection frame
        file_frame = CTkFrame(main_frame)
        file_frame.pack(fill="x", padx=10, pady=10)
        
        # File selection label
        file_label = CTkLabel(file_frame, text="Select JSON File:",
                            font=("Arial", 12))
        file_label.pack(side="left", padx=10, pady=10)
        
        # File selection dropdown
        self.file_var = tk.StringVar(value="example.json")
        file_dropdown = CTkOptionMenu(file_frame, 
                                     values=["example.json", "settings.json", "config.json"],
                                     variable=self.file_var,
                                     command=self.onFileChange)
        file_dropdown.pack(side="left", padx=10, pady=10)
        
        # Create JsonEditor widget
        self.json_editor = JsonEditor(main_frame, jsonFile="example.json")
        self.json_editor.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Status frame
        status_frame = CTkFrame(main_frame)
        status_frame.pack(fill="x", padx=10, pady=10)
        
        # Status label
        self.status_label = CTkLabel(status_frame, text="Ready", font=("Arial", 12))
        self.status_label.pack()
    
    def onFileChange(self, selected_file):
        """Handle JSON file change"""
        try:
            self.json_editor.setJsonFile(selected_file)
            self.status_label.configure(text=f"Loaded: {selected_file}")
        except Exception as e:
            self.status_label.configure(text=f"Error loading {selected_file}: {e}")


def create_sample_json_files():
    """Create sample JSON files for testing"""
    
    # Sample example.json content
    example_content = {
        "name": "John Doe",
        "age": 30,
        "city": "New York",
        "hobbies": ["reading", "swimming", "coding"],
        "active": True,
        "balance": 1234.56,
        "address": {
            "street": "123 Main St",
            "zipcode": "10001"
        }
    }
    
    # Sample settings.json content
    settings_content = {
        "theme": "dark",
        "language": "en",
        "font_size": 12,
        "auto_save": True,
        "max_recent_files": 10,
        "window_position": {"x": 100, "y": 100}
    }
    
    # Sample config.json content
    config_content = {
        "database_url": "localhost:5432",
        "debug_mode": False,
        "max_connections": 100,
        "timeout": 30,
        "features": {
            "logging": True,
            "caching": True,
            "compression": False
        }
    }
    
    # Write sample files if they don't exist
    if not os.path.exists("example.json"):
        with open("example.json", "w") as f:
            json.dump(example_content, f, indent=4)
        print("Created sample example.json")
    
    if not os.path.exists("settings.json"):
        with open("settings.json", "w") as f:
            json.dump(settings_content, f, indent=4)
        print("Created sample settings.json")
    
    if not os.path.exists("config.json"):
        with open("config.json", "w") as f:
            json.dump(config_content, f, indent=4)
        print("Created sample config.json")


def main():
    """Main function to run the JsonEditor example"""
    # Create sample JSON files
    create_sample_json_files()
    
    # Create and run the application
    app = JsonEditorExample()
    app.mainloop()


if __name__ == "__main__":
    main()
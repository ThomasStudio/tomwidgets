import tkinter as tk
from customtkinter import CTk, CTkFrame, CTkLabel, CTkButton, CTkOptionMenu
from tomwidgets.widget.ConfigEditor import ConfigEditor


class ConfigEditorExample(CTk):
    def __init__(self):
        super().__init__()
        
        self.title("ConfigEditor Example")
        self.geometry("800x600")
        
        # Create main frame
        main_frame = CTkFrame(self)
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Title label
        title_label = CTkLabel(main_frame, text="ConfigEditor Widget Example", 
                              font=("Arial", 20, "bold"))
        title_label.pack(pady=20)
        
        # Instructions
        instructions = CTkLabel(main_frame, 
                               text="This example shows how to use the ConfigEditor widget to edit configuration files.\n"
                                    "Select a configuration file from the dropdown below to load it into the editor.",
                               font=("Arial", 14))
        instructions.pack(pady=10)
        
        # File selection frame
        file_frame = CTkFrame(main_frame)
        file_frame.pack(fill="x", padx=10, pady=10)
        
        # File selection label
        file_label = CTkLabel(file_frame, text="Select Configuration File:",
                            font=("Arial", 12))
        file_label.pack(side="left", padx=10, pady=10)
        
        # File selection dropdown
        self.file_var = tk.StringVar(value="tools.ini")
        file_dropdown = CTkOptionMenu(file_frame, 
                                     values=["tools.ini", "settings.ini"],
                                     variable=self.file_var,
                                     command=self.onFileChange)
        file_dropdown.pack(side="left", padx=10, pady=10)
        
        # Create ConfigEditor widget
        self.config_editor = ConfigEditor(main_frame, configFile="tools.ini")
        self.config_editor.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Status frame
        status_frame = CTkFrame(main_frame)
        status_frame.pack(fill="x", padx=10, pady=10)
        
        # Status label
        self.status_label = CTkLabel(status_frame, text="Ready", font=("Arial", 12))
        self.status_label.pack()
    
    def onFileChange(self, selected_file):
        """Handle configuration file change"""
        try:
            self.config_editor.setConfigFile(selected_file)
            self.status_label.configure(text=f"Loaded: {selected_file}")
        except Exception as e:
            self.status_label.configure(text=f"Error loading {selected_file}: {e}")


def create_sample_config_files():
    """Create sample configuration files for testing"""
    import os
    
    # Sample tools.ini content
    tools_content = """[win]
dir = dir
explorer = explorer .
ip = ipconfig

[python]
create_env = python -m venv .venv
install = pip install {package_name}
activate = .venv\\Scripts\\activate

[git]
status = git status
commit = git commit -m "{message}"
push = git push
pull = git pull
"""
    
    # Sample settings.ini content
    settings_content = """[folder]
cmdtool = D:\\Mywork\\python\\CmdTool
temp = D:\\temp

[window]
toolwin_position = 0,0
basewin_position = 737,1841

[preferences]
theme = dark
language = en
font_size = 12
auto_save = true
"""
    
    # Write sample files if they don't exist
    if not os.path.exists("tools.ini"):
        with open("tools.ini", "w") as f:
            f.write(tools_content)
        print("Created sample tools.ini")
    
    if not os.path.exists("settings.ini"):
        with open("settings.ini", "w") as f:
            f.write(settings_content)
        print("Created sample settings.ini")


def main():
    """Main function to run the ConfigEditor example"""
    # Create sample configuration files
    create_sample_config_files()
    
    # Create and run the application
    app = ConfigEditorExample()
    app.mainloop()


if __name__ == "__main__":
    main()
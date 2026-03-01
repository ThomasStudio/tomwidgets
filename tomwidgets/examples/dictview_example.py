import customtkinter as ctk
from tomwidgets.widget.DictView import DictView


def create_example_window():
    # Create main window
    root = ctk.CTk()
    root.title("DictView Example")
    root.geometry("600x400")
    
    # Create a sample dictionary
    sample_dict = {
        "name": "John Doe",
        "age": 30,
        "city": "New York",
        "occupation": "Developer",
        "skills": ["Python", "JavaScript", "C++"],
        "is_active": True
    }
    
    # Create DictView widget with custom splitChar and lineChar
    dict_view = DictView(root, dictionary=sample_dict, 
                         width=580, height=380, keyColor="white", valueColor="gold", valueSize=20,
                         splitChar=" ", lineChar="  ")
    dict_view.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
    
    # Configure grid to expand with window
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    
    # Start the app
    root.mainloop()


def main():
    create_example_window()


if __name__ == "__main__":
    main()
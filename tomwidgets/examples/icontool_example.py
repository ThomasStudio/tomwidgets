import tkinter as tk
from tomwidgets.tools.IconTool import IconTool

def main():
    """Create and run the IconTool example."""
    # Create the main window
    root = tk.Tk()
    root.title("IconTool Example")
    
    # Set window size and position
    root.geometry("800x600+100+100")
    
    # Create the IconTool instance
    iconTool = IconTool(root, title="Icon Tool - Emoji & Segoe Browser")
    
    # Pack the IconTool to fill the window
    iconTool.pack(fill=tk.BOTH, expand=True)
    
    # Start the main loop
    root.mainloop()

if __name__ == "__main__":
    main()
import tkinter as tk
from tomwidgets.tools.RETool import RETool


def main():
    """Create and run the RETool example."""
    # Create the main window
    root = tk.Tk()
    root.title("RETool Example")
    
    # Create the RETool instance
    retool = RETool(root, title="Regular Expression Tool", showTitleBar=True, showFolderBar=True)
    retool.pack(fill=tk.BOTH, expand=True)
    
    # Set some initial text for testing
    retool.setInputText("""This is a sample text with numbers: 123, 456, 789.
It also contains words like: apple, banana, cherry.
And some special patterns: ABC123, test123, hello456.

Try selecting different regex patterns from the dropdown and pressing Enter to see the results!""")
    
    # Start the main loop
    root.mainloop()


if __name__ == "__main__":
    main()
import tkinter as tk
from ..tools.UrlTool import UrlTool


def createUrlToolExample():
    """Create and display a UrlTool example."""
    # Create root window
    root = tk.Tk()
    root.title("UrlTool Example")
    root.geometry("600x500")
    
    # Create UrlTool instance
    urltool = UrlTool(root, title="UrlTool", showTitleBar=True, 
                     showFolderBar=True, asWin=False)
    urltool.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    # Start the main loop
    root.mainloop()


if __name__ == "__main__":
    createUrlToolExample()
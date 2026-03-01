import tkinter as tk
from ..tools.PyInstall import PyInstall


def createPyInstallExample():
    """Create and display a PyInstall example."""
    # Create root window
    root = tk.Tk()
    root.title("PyInstall Example")
    root.geometry("600x500")
    
    # Create PyInstall instance
    pyinstall = PyInstall(root, title="PyInstall Tool", showTitleBar=True, 
                         showFolderBar=True, asWin=False)
    pyinstall.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    # Start the main loop
    root.mainloop()


if __name__ == "__main__":
    createPyInstallExample()
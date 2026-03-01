import os
import customtkinter as ctk
from tomwidgets import FolderBar
from tomwidgets.widget import Frame


class FolderBarExample:
    """Example application demonstrating FolderBar functionality."""

    def __init__(self):
        """Initialize the example application."""
        # Create main window
        self.root = ctk.CTk()
        self.root.title("FolderBar Example")
        self.root.geometry("600x400")

        # Configure grid
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)

        # Create UI
        self.createUi()

    def createUi(self):
        """Create the user interface."""
        # Title
        folderFrame = Frame(self.root)
        folderFrame.grid(row=0, column=0, padx=20, pady=10, sticky="w")

        # FolderBar 1: With initial folders
        initialFolders = [
            os.path.expanduser("~/"),
            os.path.expanduser("~/Documents"),
            os.path.expanduser("~/Downloads"),
            # Current script directory
            os.path.dirname(os.path.abspath(__file__))
        ]

        self.folderBar1 = FolderBar(folderFrame, title="Project Folders:",
                                    folders=initialFolders)
        self.folderBar1.pack(fill="x")

        # FolderBar 2: Empty initially
        self.folderBar2 = FolderBar(folderFrame, title="Custom Folders:")
        self.folderBar2.pack(fill="x")

        # Main content frame
        contentFrame = ctk.CTkFrame(self.root)
        contentFrame.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")
        contentFrame.grid_columnconfigure(0, weight=1)
        contentFrame.grid_rowconfigure(1, weight=1)

        # Log area
        logFrame = ctk.CTkFrame(contentFrame)
        logFrame.pack(fill="x")

        logLabel = ctk.CTkLabel(logFrame, text="Event Log:",
                                font=ctk.CTkFont(weight="bold"))
        logLabel.pack(side="left")

        self.logText = ctk.CTkTextbox(logFrame, height=100)
        self.logText.pack(side="left", fill="x", expand=True)

        # Control buttons
        buttonFrame = ctk.CTkFrame(contentFrame)
        buttonFrame.pack(fill="x")

        for i in range(4):
            buttonFrame.grid_columnconfigure(i, weight=1)

        # Add current directory button
        addCurrentBtn = ctk.CTkButton(buttonFrame, text="Add Current Dir",
                                      command=self.addCurrentDirectory)
        addCurrentBtn.grid(row=0, column=0, padx=5, pady=5)

        # Clear selection button
        clearBtn = ctk.CTkButton(buttonFrame, text="Clear Selection",
                                 command=self.clearSelection)
        clearBtn.grid(row=0, column=1, padx=5, pady=5)

        # Get info button
        infoBtn = ctk.CTkButton(buttonFrame, text="Get Folder Info",
                                command=self.getFolderInfo)
        infoBtn.grid(row=0, column=2, padx=5, pady=5)

        # Exit button
        exitBtn = ctk.CTkButton(buttonFrame, text="Exit",
                                command=self.root.quit)
        exitBtn.grid(row=0, column=3, padx=5, pady=5)

        # Bind event handlers
        self.bindEventHandlers()

    def bindEventHandlers(self):
        """Bind event handlers to FolderBar widgets."""
        # FolderBar 1: Basic event handling
        self.folderBar1.bindFolderChanged(self.onFolderBar1Changed)

        # FolderBar 2: Event with custom handling
        self.folderBar2.bindFolderChanged(self.onFolderBar2Changed)

    def logMessage(self, message: str):
        """
        Add a message to the log area.

        Args:
            message: The message to log
        """
        self.logText.insert("end", f"{message}\n")
        self.logText.see("end")

    def onFolderBar1Changed(self, event=None):
        """Handle FolderBar 1 folder selection change."""
        selectedFolder = self.folderBar1.getSelectedOption()
        currentDir = self.folderBar1.getCurrentDirectory()

        self.logMessage(f"📁 FolderBar 1: Selected '{selectedFolder}'")
        self.logMessage(f"   Current directory: {currentDir}")

    def onFolderBar2Changed(self, event=None):
        """Handle FolderBar 2 folder selection change."""
        selectedFolder = self.folderBar2.getSelectedOption()
        currentDir = self.folderBar2.getCurrentDirectory()

        self.logMessage(f"📂 FolderBar 2: Selected '{selectedFolder}'")
        self.logMessage(f"   Current directory: {currentDir}")

    def addCurrentDirectory(self):
        """Add current working directory to FolderBar 2."""
        currentDir = os.getcwd()
        self.folderBar2.addFolder(currentDir)
        self.logMessage(
            f"➕ Added current directory to FolderBar 2: {currentDir}")

    def clearSelection(self):
        """Clear selection in both FolderBars."""
        self.folderBar1.clearSelection()
        self.folderBar2.clearSelection()
        self.logMessage("🗑️  Cleared selections in both FolderBars")

    def getFolderInfo(self):
        """Get information about current folder selections."""
        self.logMessage("📊 Folder Information:")

        # FolderBar 1 info
        folders1 = self.folderBar1.getFolderList()
        selected1 = self.folderBar1.getSelectedOption()
        self.logMessage(
            f"   FolderBar 1: {len(folders1)} folders, selected: '{selected1}'")

        # FolderBar 2 info
        folders2 = self.folderBar2.getFolderList()
        selected2 = self.folderBar2.getSelectedOption()
        self.logMessage(
            f"   FolderBar 2: {len(folders2)} folders, selected: '{selected2}'")

    def run(self):
        """Run the example application."""
        self.logMessage("🚀 FolderBar Example Started")
        self.logMessage("💡 Try adding folders using the '+' button")
        self.logMessage("💡 Select folders to change current directory")
        self.root.mainloop()


def main():
    """Main function to run the example."""
    # Set appearance mode
    ctk.set_appearance_mode("Dark")
    ctk.set_default_color_theme("blue")

    # Create and run example
    example = FolderBarExample()
    example.run()


if __name__ == "__main__":
    main()

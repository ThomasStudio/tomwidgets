import customtkinter as ctk
from tomwidgets import MenuBtn, createMenuButton


class MenuBtnExample(ctk.CTk):
    """Example application demonstrating MenuBtn functionality."""

    def __init__(self):
        """Initialize the example application."""
        super().__init__()

        self.title("MenuBtn Example")
        self.geometry("600x500")

        # Configure grid layout
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.setupUI()

    def setupUI(self):
        """Setup the user interface components."""
        # Title label
        titleLabel = ctk.CTkLabel(self, text="MenuBtn Example",
                                  font=ctk.CTkFont(size=20, weight="bold"))
        titleLabel.grid(row=0, column=0, padx=20, pady=10, sticky="w")

        # Description label
        descLabel = ctk.CTkLabel(self,
                                 text="Click the buttons below to see different menu configurations",
                                 font=ctk.CTkFont(size=12))
        descLabel.grid(row=0, column=0, padx=20, pady=40, sticky="w")

        # Main content frame
        contentFrame = ctk.CTkFrame(self)
        contentFrame.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")
        contentFrame.grid_columnconfigure(0, weight=1)

        # Create different MenuBtn examples
        self.createBasicExample(contentFrame)
        self.createAdvancedExample(contentFrame)
        self.createDynamicExample(contentFrame)

    def createBasicExample(self, parent):
        """Create basic MenuBtn example."""
        frame = ctk.CTkFrame(parent)
        frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        # Section label
        label = ctk.CTkLabel(frame, text="Basic MenuBtn",
                             font=ctk.CTkFont(size=14, weight="bold"))
        label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        # Basic menu commands
        basicCommands = [
            ("New File", self.onNewFile),
            ("Open File", self.onOpenFile),
            ("Save", self.onSave),
            None,  # Separator
            ("Exit", self.onExit)
        ]

        # Create MenuBtn using class
        menuBtn1 = MenuBtn(frame, text="File Menu", menuCommands=basicCommands)
        menuBtn1.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        # Create MenuBtn using convenience function
        menuBtn2 = createMenuButton(frame, text="Edit Menu", menuCommands=[
            ("Undo", self.onUndo),
            ("Redo", self.onRedo),
            None,
            ("Cut", self.onCut),
            ("Copy", self.onCopy),
            ("Paste", self.onPaste)
        ])
        menuBtn2.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        MenuBtn(frame, menuCommands=[
            ("Undo", self.onUndo),
            ("Redo", self.onRedo),
        ]).grid(row=3, column=0, padx=10, pady=5, sticky="w")

    def createAdvancedExample(self, parent):
        """Create advanced MenuBtn example with submenus."""
        frame = ctk.CTkFrame(parent)
        frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        # Section label
        label = ctk.CTkLabel(frame, text="Advanced MenuBtn (with Submenus)",
                             font=ctk.CTkFont(size=14, weight="bold"))
        label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        # Advanced menu with submenus
        advancedCommands = [
            ("View", [
                ("Zoom In", self.onZoomIn),
                ("Zoom Out", self.onZoomOut),
                ("Reset Zoom", self.onResetZoom)
            ]),
            ("Tools", [
                ("Calculator", self.onCalculator),
                ("Notepad", self.onNotepad),
                None,
                ("Settings", self.onSettings)
            ]),
            None,
            ("Help", [
                ("Documentation", self.onDocumentation),
                ("About", self.onAbout)
            ])
        ]

        menuBtn = MenuBtn(frame, text="Advanced Menu",
                          menuCommands=advancedCommands)
        menuBtn.grid(row=1, column=0, padx=10, pady=5, sticky="w")

    def createDynamicExample(self, parent):
        """Create dynamic MenuBtn example with runtime modifications."""
        frame = ctk.CTkFrame(parent)
        frame.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        # Section label
        label = ctk.CTkLabel(frame, text="Dynamic MenuBtn",
                             font=ctk.CTkFont(size=14, weight="bold"))
        label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        # Create dynamic menu button
        self.dynamicMenuBtn = MenuBtn(frame, text="Dynamic Menu")
        self.dynamicMenuBtn.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        # Control buttons for dynamic menu
        addBtn = ctk.CTkButton(frame, text="Add Item",
                               command=self.addDynamicItem)
        addBtn.grid(row=2, column=0, padx=5, pady=2, sticky="w")

        clearBtn = ctk.CTkButton(
            frame, text="Clear Menu", command=self.clearDynamicMenu)
        clearBtn.grid(row=2, column=1, padx=5, pady=2, sticky="w")

        # Counter for dynamic items
        self.dynamicCounter = 1

    def addDynamicItem(self):
        """Add a new item to the dynamic menu."""
        itemText = f"Dynamic Item {self.dynamicCounter}"
        self.dynamicMenuBtn.addMenuCommand(
            itemText, lambda: self.onDynamicItem(self.dynamicCounter))
        self.dynamicCounter += 1

    def clearDynamicMenu(self):
        """Clear all items from the dynamic menu."""
        self.dynamicMenuBtn.clearMenuCommands()
        self.dynamicCounter = 1

    # Menu command handlers
    def onNewFile(self):
        print("New File clicked")

    def onOpenFile(self):
        print("Open File clicked")

    def onSave(self):
        print("Save clicked")

    def onExit(self):
        print("Exit clicked")
        self.quit()

    def onUndo(self):
        print("Undo clicked")

    def onRedo(self):
        print("Redo clicked")

    def onCut(self):
        print("Cut clicked")

    def onCopy(self):
        print("Copy clicked")

    def onPaste(self):
        print("Paste clicked")

    def onZoomIn(self):
        print("Zoom In clicked")

    def onZoomOut(self):
        print("Zoom Out clicked")

    def onResetZoom(self):
        print("Reset Zoom clicked")

    def onCalculator(self):
        print("Calculator clicked")

    def onNotepad(self):
        print("Notepad clicked")

    def onSettings(self):
        print("Settings clicked")

    def onDocumentation(self):
        print("Documentation clicked")

    def onAbout(self):
        print("About clicked")

    def onDynamicItem(self, itemNumber):
        print(f"Dynamic Item {itemNumber} clicked")


def main():
    """Main function to run the example."""
    app = MenuBtnExample()
    app.mainloop()


if __name__ == "__main__":
    main()

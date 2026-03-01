import customtkinter as ctk
from tomwidgets.widget import TitleBar, createTitleBar, VisibleBtn, Tk, Frame, Label, Entry, Button, Textbox, ScrollableFrame, Font
from tomwidgets.widget import BtnBar, BtnConfig


class TitleBarExample(Tk):
    """Example application demonstrating TitleBar functionality."""

    def __init__(self):
        """Initialize the example application."""
        super().__init__()

        self.title("TitleBar Example")
        self.geometry("800x600")

        # Configure grid layout
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.setupUI()

    def setupUI(self):
        """Setup the user interface components."""
        # Create menu commands for the title bar
        menuCommands = [
            ("File", [
                ("New", self.onNew),
                ("Open", self.onOpen),
                ("Save", self.onSave),
                None,
                ("Exit", self.onExit)
            ]),
            ("Edit", [
                ("Undo", self.onUndo),
                ("Redo", self.onRedo),
                None,
                ("Cut", self.onCut),
                ("Copy", self.onCopy),
                ("Paste", self.onPaste)
            ]),
            ("View", [
                ("Zoom In", self.onZoomIn),
                ("Zoom Out", self.onZoomOut),
                ("Reset Zoom", self.onResetZoom)
            ]),
            ("Help", [
                ("About", self.onAbout),
                ("Documentation", self.onDocumentation)
            ])
        ]

        # Create the main title bar
        self.titleBar = TitleBar(self, title="My Application",
                                 menuCommands=menuCommands)
        self.titleBar.grid(row=0, column=0, sticky="ew", padx=0, pady=0)

        # Main content area
        self.contentFrame = Frame(self)
        self.contentFrame.grid(
            row=1, column=0, sticky="nsew", padx=10, pady=10)
        self.contentFrame.grid_columnconfigure(0, weight=1)
        self.contentFrame.grid_rowconfigure(1, weight=1)

        # Control panel
        self.createControlPanel()

        # Content area with widgets that can be toggled
        self.createContentArea()

        # Bind content widgets to title bar's visibility button
        self.bindContentWidgets()

    def createControlPanel(self):
        """Create the control panel for testing TitleBar features."""
        controlFrame = Frame(self.contentFrame)
        controlFrame.grid(row=0, column=0, sticky="ew", padx=10, pady=10)

        # Section label
        label = Label(controlFrame, text="TitleBar Controls",
                      font=Font(size=14, weight="bold"))
        label.grid(row=0, column=0, columnspan=4, padx=10, pady=5, sticky="w")

        # Title control
        titleLabel = Label(controlFrame, text="Title:")
        titleLabel.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        self.titleEntry = Entry(
            controlFrame, placeholder_text="Enter new title")
        self.titleEntry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        self.titleEntry.insert(0, "My Application")

        titleBtn = Button(controlFrame, text="Update Title",
                          command=self.updateTitle)
        titleBtn.grid(row=1, column=2, padx=5, pady=5, sticky="w")

        # Visibility controls
        visLabel = Label(controlFrame, text="Visibility:")
        visLabel.grid(row=2, column=0, padx=5, pady=5, sticky="w")

        btnShowHide = BtnBar(controlFrame)
        btnShowHide.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        btnShowHide.addBtns([
            BtnConfig(name="Show All", callback=self.showAllWidgets),
            BtnConfig(name="Hide All", callback=self.hideAllWidgets),
            BtnConfig(name="BtnBar", callback=test_btnbar_integration),
        ])

        # Button text controls
        btnTextLabel = Label(controlFrame, text="Button Text:")
        btnTextLabel.grid(row=3, column=0, padx=5, pady=5, sticky="w")

        btnMenu = BtnBar(controlFrame)
        btnMenu.grid(row=3, column=1, padx=5, pady=5, sticky="w")
        btnMenu.addBtns([
            BtnConfig(name="Default Icons",
                      callback=self.setDefaultButtonText),
            BtnConfig(name="Text Labels", callback=self.setTextButtonText),
        ])

        # Configure column weights
        controlFrame.grid_columnconfigure(1, weight=1)

    def createContentArea(self):
        """Create the content area with widgets that can be toggled."""
        contentArea = Frame(self.contentFrame)
        contentArea.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        contentArea.grid_columnconfigure(0, weight=1)
        contentArea.grid_rowconfigure(1, weight=1)

        # Section label
        label = Label(contentArea, text="Content Area (Toggle with TitleBar Visibility Button)",
                      font=Font(size=14, weight="bold"))
        label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        # Create some sample widgets that can be toggled
        self.createSampleWidgets(contentArea)

    def createSampleWidgets(self, parent):
        """Create sample widgets for demonstration."""
        # Widgets frame
        widgetsFrame = Frame(parent)
        widgetsFrame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        widgetsFrame.grid_columnconfigure(0, weight=1)
        widgetsFrame.grid_rowconfigure(0, weight=1)

        # Create a scrollable frame for widgets
        scrollFrame = ScrollableFrame(widgetsFrame)
        scrollFrame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        # Sample widgets
        sampleWidgets = []

        # Text widget
        textLabel = Label(scrollFrame, text="Sample Text Widget:",
                          font=Font(weight="bold"))
        textLabel.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        sampleWidgets.append(textLabel)

        textWidget = Textbox(scrollFrame, height=100)
        textWidget.grid(row=1, column=0, padx=10, pady=5, sticky="ew")
        textWidget.insert(
            "1.0", "This is a sample text widget that can be toggled using the visibility button in the title bar.")
        sampleWidgets.append(textWidget)

        # Input widgets
        inputLabel = Label(scrollFrame, text="Sample Input Widgets:",
                           font=Font(weight="bold"))
        inputLabel.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        sampleWidgets.append(inputLabel)

        entry1 = Entry(scrollFrame, placeholder_text="Enter text here")
        entry1.grid(row=3, column=0, padx=10, pady=5, sticky="ew")
        sampleWidgets.append(entry1)

        entry2 = Entry(scrollFrame, placeholder_text="Another text field")
        entry2.grid(row=4, column=0, padx=10, pady=5, sticky="ew")
        sampleWidgets.append(entry2)

        # Button widgets
        buttonLabel = Label(scrollFrame, text="Sample Buttons:",
                            font=Font(weight="bold"))
        buttonLabel.grid(row=5, column=0, padx=10, pady=5, sticky="w")
        sampleWidgets.append(buttonLabel)

        button1 = Button(scrollFrame, text="Button 1",
                         command=lambda: print("Button 1 clicked"))
        button1.grid(row=6, column=0, padx=10, pady=5, sticky="w")
        sampleWidgets.append(button1)

        button2 = Button(scrollFrame, text="Button 2",
                         command=lambda: print("Button 2 clicked"))
        button2.grid(row=7, column=0, padx=10, pady=5, sticky="w")
        sampleWidgets.append(button2)

        # Store widgets for visibility control
        self.contentWidgets = sampleWidgets

        # Configure scroll frame column
        scrollFrame.grid_columnconfigure(0, weight=1)

    def bindContentWidgets(self):
        """Bind the content widgets to the title bar's visibility button."""
        self.titleBar.bindVisible(self.contentWidgets)

    def updateTitle(self):
        """Update the title bar title."""
        newTitle = self.titleEntry.get()
        if newTitle:
            self.titleBar.setTitle(newTitle)

    def showAllWidgets(self):
        """Show all content widgets."""
        self.titleBar.showAllWidgets()

    def hideAllWidgets(self):
        """Hide all content widgets."""
        self.titleBar.hideAllWidgets()

    def setDefaultButtonText(self):
        """Set default icon text for buttons."""
        self.titleBar.setMenuButtonText("☰")
        self.titleBar.setVisibleButtonText("👁", "👁")

    def setTextButtonText(self):
        """Set text labels for buttons."""
        self.titleBar.setMenuButtonText("Menu")
        self.titleBar.setVisibleButtonText("Show", "Hide")

    # Menu command handlers
    def onNew(self):
        print("New clicked")

    def onOpen(self):
        print("Open clicked")

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

    def onAbout(self):
        print("About clicked")

    def onDocumentation(self):
        print("Documentation clicked")


def test_btnbar_integration():
    """Test the BtnBar integration in TitleBar"""

    # Create main window
    root = ctk.CTk()
    root.title("TitleBar with BtnBar Test")
    root.geometry("800x200")

    # Create a frame to hold the title bar
    frame = ctk.CTkFrame(root)
    frame.pack(fill="x", padx=10, pady=10)

    # Create menu commands
    menu_commands = [
        ("File", [
            ("New", lambda: print("New clicked")),
            ("Open", lambda: print("Open clicked")),
            ("Save", lambda: print("Save clicked"))
        ]),
        ("Edit", [
            ("Cut", lambda: print("Cut clicked")),
            ("Copy", lambda: print("Copy clicked")),
            ("Paste", lambda: print("Paste clicked"))
        ])
    ]

    # Create title bar with BtnBar
    title_bar = TitleBar(frame, title="Test Title Bar",
                         menuCommands=menu_commands)
    title_bar.pack(fill="x")

    # Add some buttons to the BtnBar
    def btn1_callback():
        print("Button 1 clicked")

    def btn2_callback():
        print("Button 2 clicked")

    def btn3_callback():
        print("Button 3 clicked")

    # Add buttons to the BtnBar
    title_bar.addBtnToBar("Btn1", btn1_callback, tooltip="First button")
    title_bar.addBtnToBar("Btn2", btn2_callback, tooltip="Second button")
    title_bar.addBtnToBar("Btn3", btn3_callback, tooltip="Third button")

    # Create a content area
    content = ctk.CTkLabel(root, text="Content area below title bar",
                           font=ctk.CTkFont(size=16))
    content.pack(expand=True, fill="both", padx=20, pady=20)

    print("TitleBar with BtnBar created successfully!")
    print("Try clicking the buttons in the BtnBar (right side of title bar)")

    root.mainloop()


def main():
    """Main function to run the example."""
    app = TitleBarExample()
    app.mainloop()


if __name__ == "__main__":
    main()

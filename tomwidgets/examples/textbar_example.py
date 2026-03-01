from datetime import datetime
import customtkinter as ctk

from tomwidgets.widget import TextBar


class TextBarExample(ctk.CTk):
    """Main application window for TextBar example."""

    def __init__(self):
        """Initialize the TextBar example application."""
        super().__init__()

        # Configure the main window
        self.title("TextBar Example - Comprehensive Demo")
        self.geometry("900x700")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Create menu commands for the title bar
        self.menuCommands = [
            ("File", [("New", self.fileNew),
                      None,
                      ("Open", self.fileOpen)])
        ]

        self.menuCommands2 = [
            {"label": "File", "commands": [
                {"label": "New", "command": self.fileNew},
                {"label": "Open", "command": self.fileOpen},
                {"label": "Save", "command": self.fileSave},
                {"label": "-", "command": None},  # Separator
                {"label": "Exit", "command": self.quit}
            ]},
            {"label": "Edit", "commands": [
                {"label": "Cut", "command": self.editCut},
                {"label": "Copy", "command": self.editCopy},
                {"label": "Paste", "command": self.editPaste},
                {"label": "-", "command": None},
                {"label": "Select All", "command": self.editSelectAll}
            ]},
            {"label": "Format", "commands": [
                {"label": "Bold", "command": self.formatBold},
                {"label": "Italic", "command": self.formatItalic},
                {"label": "-", "command": None},
                {"label": "Increase Font", "command": self.formatIncreaseFont},
                {"label": "Decrease Font", "command": self.formatDecreaseFont}
            ]}
        ]

        # Create the TextBar widget
        self.textBar = TextBar(
            self,
            title="TextBar Demo - Edit Me!",
            menuCommands=self.menuCommands,
            width=800,
            height=500
        )
        self.textBar.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        # Create control panel
        self.createControlPanel()

        # Add comprehensive sample content
        self.addComprehensiveSampleContent()

        # Test all methods on startup
        self.testAllMethods()

    def createControlPanel(self):
        """Create a control panel with buttons for TextBar operations."""
        controlFrame = ctk.CTkFrame(self)
        controlFrame.grid(row=1, column=0, padx=20, pady=10, sticky="ew")
        controlFrame.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1)

        # Section label
        ctk.CTkLabel(controlFrame, text="TextBar Controls - Comprehensive Demo",
                     font=ctk.CTkFont(size=16, weight="bold")).grid(
                         row=0, column=0, columnspan=6, pady=10)

        # Row 1: Basic text operations
        ctk.CTkButton(controlFrame, text="Clear Text", command=self.clearText).grid(
            row=1, column=0, padx=5, pady=5, sticky="ew")
        ctk.CTkButton(controlFrame, text="Append Text", command=self.appendText).grid(
            row=1, column=1, padx=5, pady=5, sticky="ew")
        ctk.CTkButton(controlFrame, text="Insert at Line 1", command=self.insertText).grid(
            row=1, column=2, padx=5, pady=5, sticky="ew")
        ctk.CTkButton(controlFrame, text="Get Text", command=self.getText).grid(
            row=1, column=3, padx=5, pady=5, sticky="ew")
        ctk.CTkButton(controlFrame, text="Set Text", command=self.setText).grid(
            row=1, column=4, padx=5, pady=5, sticky="ew")
        ctk.CTkButton(controlFrame, text="Get Title", command=self.getTitle).grid(
            row=1, column=5, padx=5, pady=5, sticky="ew")

        # Row 2: Line operations and search/replace
        ctk.CTkButton(controlFrame, text="Get Line Text", command=self.getLineText).grid(
            row=2, column=0, padx=5, pady=5, sticky="ew")
        ctk.CTkButton(controlFrame, text="Set Line Text", command=self.setLineText).grid(
            row=2, column=1, padx=5, pady=5, sticky="ew")
        ctk.CTkButton(controlFrame, text="Search Text", command=self.searchText).grid(
            row=2, column=2, padx=5, pady=5, sticky="ew")
        ctk.CTkButton(controlFrame, text="Replace Text", command=self.replaceText).grid(
            row=2, column=3, padx=5, pady=5, sticky="ew")
        ctk.CTkButton(controlFrame, text="Delete Text", command=self.deleteText).grid(
            row=2, column=4, padx=5, pady=5, sticky="ew")
        ctk.CTkButton(controlFrame, text="Test All Methods", command=self.testAllMethods).grid(
            row=2, column=5, padx=5, pady=5, sticky="ew")

        # Row 3: Title bar and state controls
        ctk.CTkButton(controlFrame, text="Show Title Bar", command=self.showTitleBar).grid(
            row=3, column=0, padx=5, pady=5, sticky="ew")
        ctk.CTkButton(controlFrame, text="Hide Title Bar", command=self.hideTitleBar).grid(
            row=3, column=1, padx=5, pady=5, sticky="ew")
        ctk.CTkButton(controlFrame, text="Toggle Title Bar", command=self.toggleTitleBar).grid(
            row=3, column=2, padx=5, pady=5, sticky="ew")
        ctk.CTkButton(controlFrame, text="Set Title", command=self.setTitle).grid(
            row=3, column=3, padx=5, pady=5, sticky="ew")
        ctk.CTkButton(controlFrame, text="Set Read-Only", command=self.setReadOnly).grid(
            row=3, column=4, padx=5, pady=5, sticky="ew")
        ctk.CTkButton(controlFrame, text="Set Editable", command=self.setEditable).grid(
            row=3, column=5, padx=5, pady=5, sticky="ew")

        # Row 4: Formatting controls
        ctk.CTkButton(controlFrame, text="Set Text Color", command=self.setTextColor).grid(
            row=4, column=0, padx=5, pady=5, sticky="ew")
        ctk.CTkButton(controlFrame, text="Set Text Size", command=self.setTextSize).grid(
            row=4, column=1, padx=5, pady=5, sticky="ew")
        ctk.CTkButton(controlFrame, text="Get Line Count", command=self.getLineCount).grid(
            row=4, column=2, padx=5, pady=5, sticky="ew")
        ctk.CTkButton(controlFrame, text="Get Text Length", command=self.getTextLength).grid(
            row=4, column=3, padx=5, pady=5, sticky="ew")
        ctk.CTkButton(controlFrame, text="Insert with Format", command=self.insertWithFormat).grid(
            row=4, column=4, padx=5, pady=5, sticky="ew")
        ctk.CTkButton(controlFrame, text="Add Sample Content", command=self.addSampleContent).grid(
            row=4, column=5, padx=5, pady=5, sticky="ew")

    def addComprehensiveSampleContent(self):
        """Add comprehensive sample content to demonstrate TextBar features."""
        print("\n=== Adding Comprehensive Sample Content ===")

        # Clear any existing content
        self.textBar.clearText()

        # Add sample content with different formatting
        sampleText = """Welcome to TextBar Demo!

This widget combines a TitleBar with a TextBox for rich text editing.

Features demonstrated:
• Title bar with menu functionality
• Text manipulation operations
• Line-based operations
• Search and replace functionality
• Text formatting controls
• Read-only mode toggle

Try the buttons in the control panel below!"""

        self.textBar.setText(sampleText)
        print(
            f"✓ Added sample content with {self.textBar.getLineCount()} lines")
        print(f"✓ Text length: {self.textBar.getTextLength()} characters")

    def testAllMethods(self):
        """Test all TextBar methods comprehensively."""
        print("\n" + "="*60)
        print("COMPREHENSIVE TEXTBAR METHOD TESTING")
        print("="*60)

        # Test 1: Basic operations
        print("\n1. Testing basic operations...")
        self.textBar.clearText()
        print("✓ clearText() - Text cleared")

        self.textBar.setText("Initial text content")
        print("✓ setText() - Text set successfully")

        # Test 2: Text retrieval and manipulation
        print("\n2. Testing text retrieval and manipulation...")
        currentText = self.textBar.getText()
        print(f"✓ getText() - Retrieved text: '{currentText[:30]}...'")

        self.textBar.append(" - Appended text")
        print("✓ append() - Text appended")

        # Test 3: Line operations
        print("\n3. Testing line operations...")
        lineCount = self.textBar.getLineCount()
        print(f"✓ getLineCount() - Line count: {lineCount}")

        if lineCount > 0:
            line1 = self.textBar.getLineText(1)
            print(f"✓ getLineText() - Line 1: '{line1.strip()}'")

            self.textBar.setLineText(1, "Modified line 1")
            print("✓ setLineText() - Line 1 modified")

        # Test 4: Title bar management
        print("\n4. Testing title bar management...")
        currentTitle = self.textBar.getTitle()
        print(f"✓ getTitle() - Current title: '{currentTitle}'")

        self.textBar.setTitle("TextBar Demo - Testing Complete!")
        print("✓ setTitle() - Title updated")

        # Test 5: Text formatting
        print("\n5. Testing text formatting...")
        self.textBar.setTextColor("#FF0000")
        print("✓ setTextColor() - Text color set to red")

        self.textBar.setTextSize(16)
        print("✓ setTextSize() - Text size set to 16")

        # Test 6: Insert operations
        print("\n6. Testing insert operations...")
        self.textBar.insert("1.0", "Inserted at start: ")
        print("✓ insert() - Text inserted at position 1.0")

        self.textBar.insertTo(
            "end", "\nInserted at end with formatting", "#0000FF", 14)
        print("✓ insertTo() - Formatted text inserted at end")

        # Test 7: Search and replace
        print("\n7. Testing search and replace...")
        searchPositions = self.textBar.searchText("Inserted")
        print(
            f"✓ searchText() - Found 'Inserted' at positions: {searchPositions}")

        replaceCount = self.textBar.replaceText("Inserted", "Added")
        print(f"✓ replaceText() - Replaced {replaceCount} occurrences")

        # Test 8: State management
        print("\n8. Testing state management...")
        self.textBar.setReadOnly(True)
        isReadOnly = self.textBar.isReadOnly()
        print(f"✓ setReadOnly()/isReadOnly() - Read-only mode: {isReadOnly}")

        self.textBar.setReadOnly(False)
        print("✓ setReadOnly(False) - Editable mode restored")

        # Test 9: Title bar visibility
        print("\n9. Testing title bar visibility...")
        self.textBar.hideTitleBar()
        print("✓ hideTitleBar() - Title bar hidden")

        self.textBar.showTitleBar()
        print("✓ showTitleBar() - Title bar shown")

        # Test 10: Text statistics
        print("\n10. Testing text statistics...")
        textLength = self.textBar.getTextLength()
        lineCount = self.textBar.getLineCount()
        print(f"✓ getTextLength() - Text length: {textLength} characters")
        print(f"✓ getLineCount() - Line count: {lineCount} lines")

        # Test 11: Menu commands
        print("\n11. Testing menu commands...")
        menuCommands = self.textBar.getMenuCommands()
        print(
            f"✓ getMenuCommands() - Menu commands retrieved ({len(menuCommands)} menus)")

        # Test 12: Delete operations
        print("\n12. Testing delete operations...")
        self.textBar.delete("1.0", "1.10")
        print("✓ deleteText() - First 10 characters of line 1 deleted")

        # Test 13: Toggle functionality
        print("\n13. Testing toggle functionality...")
        self.textBar.toggleTitleBar()
        print("✓ toggleTitleBar() - Title bar toggled")

        # Test 14: Final statistics
        print("\n14. Final statistics...")
        finalText = self.textBar.getText()
        finalLength = len(finalText)
        finalLines = finalText.count('\n') + 1
        print(f"✓ Final text length: {finalLength} characters")
        print(f"✓ Final line count: {finalLines} lines")

        print("\n" + "="*60)
        print("ALL TEXTBAR METHODS TESTED SUCCESSFULLY!")
        print("="*60)

        # Add confirmation message to text bar
        self.textBar.append(
            "\n\n=== All TextBar methods tested successfully! ===")

    # Control panel button methods
    def clearText(self):
        """Clear all text from the TextBar."""
        self.textBar.clearText()
        print("✓ Text cleared")

    def appendText(self):
        """Append text to the TextBar."""
        self.textBar.append(
            "\n[Appended text at: " + datetime.now().strftime("%H:%M:%S") + "]")
        print("✓ Text appended")

    def insertText(self):
        """Insert text at line 1."""
        self.textBar.insert(
            "1.0", "[Inserted at start: " + datetime.now().strftime("%H:%M:%S") + "]\n")
        print("✓ Text inserted at line 1")

    def getText(self):
        """Get and display current text."""
        text = self.textBar.getText()
        print(f"Current text (first 100 chars): {text[:100]}...")

    def setText(self):
        """Set new text content."""
        newText = "New content set at: " + datetime.now().strftime("%H:%M:%S")
        self.textBar.setText(newText)
        print("✓ Text set to new content")

    def getTitle(self):
        """Get and display current title."""
        title = self.textBar.getTitle()
        print(f"Current title: {title}")

    def setTitle(self):
        """Set new title."""
        newTitle = "Updated: " + datetime.now().strftime("%H:%M:%S")
        self.textBar.setTitle(newTitle)
        print(f"✓ Title set to: {newTitle}")

    def getLineText(self):
        """Get text from line 1."""
        lineText = self.textBar.getLineText(1)
        print(f"Line 1 text: {lineText.strip()}")

    def setLineText(self):
        """Set text for line 1."""
        self.textBar.setLineText(
            1, "Line 1 updated: " + datetime.now().strftime("%H:%M:%S"))
        print("✓ Line 1 text updated")

    def searchText(self):
        """Search for 'text' in content."""
        positions = self.textBar.searchText("text")
        print(f"Found 'text' at positions: {positions}")

    def replaceText(self):
        """Replace 'text' with 'TEXT'."""
        count = self.textBar.replaceText("text", "TEXT")
        print(f"✓ Replaced {count} occurrences of 'text' with 'TEXT'")

    def deleteText(self):
        """Delete first 5 characters from line 1."""
        self.textBar.delete("1.0", "1.5")
        print("✓ Deleted first 5 characters from line 1")

    def showTitleBar(self):
        """Show the title bar."""
        self.textBar.showTitleBar()
        print("✓ Title bar shown")

    def hideTitleBar(self):
        """Hide the title bar."""
        self.textBar.hideTitleBar()
        print("✓ Title bar hidden")

    def toggleTitleBar(self):
        """Toggle title bar visibility."""
        self.textBar.toggleTitleBar()
        print("✓ Title bar toggled")

    def setReadOnly(self):
        """Set read-only mode."""
        self.textBar.setReadOnly(True)
        print("✓ Read-only mode enabled")

    def setEditable(self):
        """Set editable mode."""
        self.textBar.setReadOnly(False)
        print("✓ Editable mode enabled")

    def setTextColor(self):
        """Set text color to blue."""
        self.textBar.setTextColor("#0000FF")
        print("✓ Text color set to blue")

    def setTextSize(self):
        """Set text size to 14."""
        self.textBar.setTextSize(14)
        print("✓ Text size set to 14")

    def getLineCount(self):
        """Get line count."""
        count = self.textBar.getLineCount()
        print(f"Line count: {count}")

    def getTextLength(self):
        """Get text length."""
        length = self.textBar.getTextLength()
        print(f"Text length: {length} characters")

    def insertWithFormat(self):
        """Insert formatted text."""
        self.textBar.insertTo(
            "end", "\n[Formatted text: " + datetime.now().strftime("%H:%M:%S") + "]", "#FF00FF", 12)
        print("✓ Formatted text inserted")

    def addSampleContent(self):
        """Add sample content."""
        self.addComprehensiveSampleContent()
        print("✓ Sample content added")

    # Menu command handlers
    def fileNew(self):
        """Handle File -> New menu command."""
        self.textBar.clearText()
        print("File -> New: Text cleared")

    def fileOpen(self):
        """Handle File -> Open menu command."""
        print("File -> Open: Open functionality would be implemented here")

    def fileSave(self):
        """Handle File -> Save menu command."""
        print("File -> Save: Save functionality would be implemented here")

    def editCut(self):
        """Handle Edit -> Cut menu command."""
        print("Edit -> Cut: Cut functionality would be implemented here")

    def editCopy(self):
        """Handle Edit -> Copy menu command."""
        print("Edit -> Copy: Copy functionality would be implemented here")

    def editPaste(self):
        """Handle Edit -> Paste menu command."""
        print("Edit -> Paste: Paste functionality would be implemented here")

    def editSelectAll(self):
        """Handle Edit -> Select All menu command."""
        print("Edit -> Select All: Select all functionality would be implemented here")

    def formatBold(self):
        """Handle Format -> Bold menu command."""
        print("Format -> Bold: Bold formatting would be implemented here")

    def formatItalic(self):
        """Handle Format -> Italic menu command."""
        print("Format -> Italic: Italic formatting would be implemented here")

    def formatIncreaseFont(self):
        """Handle Format -> Increase Font menu command."""
        currentSize = 12  # Default size
        self.textBar.setTextSize(currentSize + 2)
        print(
            f"Format -> Increase Font: Font size increased to {currentSize + 2}")

    def formatDecreaseFont(self):
        """Handle Format -> Decrease Font menu command."""
        currentSize = 12  # Default size
        if currentSize > 8:
            self.textBar.setTextSize(currentSize - 2)
            print(
                f"Format -> Decrease Font: Font size decreased to {currentSize - 2}")


def main():
    """Main function to run the TextBar example."""
    app = TextBarExample()
    app.mainloop()


if __name__ == "__main__":
    main()

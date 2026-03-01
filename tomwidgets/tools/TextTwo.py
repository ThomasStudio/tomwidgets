import tkinter as tk
import customtkinter as ctk

from ..widget.BaseWin import BaseWin
from ..widget.InputBar import InputBar
from ..widget.BtnBar import BtnBar, BtnConfig
from ..widget.TextBar import TextBar


class TextTwo(BaseWin):
    def __init__(self, master=None, title="Dual Text",
                 showTitleBar=True, showFolderBar=False,
                 asWin=True, settingsFile='settings.ini', **kwargs):
        super().__init__(master, title=title, showTitleBar=showTitleBar,
                         showFolderBar=showFolderBar, asWin=asWin,
                         settingsFile=settingsFile, **kwargs)

        # Store text content
        self.t1Text = ""
        self.t2Text = ""
        self.searchText = ""
        self.replaceText = ""

        # Create UI components
        self.createUi()

        # Bind events
        self.bindEvents()

    def getCmds(self):
        """Override to add custom menu commands."""
        # Get the base menu from parent class
        baseMenu = super().getCmds()

        # Add TextTwo specific menu
        textTwoMenu = [
            ("TextTwo", [
                ("Switch Text", self.switchText),
                ("Compare Text", self.compareText),
                ("Move T1 to T2", self.moveT1ToT2),
                ("Move T2 to T1", self.moveT2ToT1),
                ("Clear T1", self.clearT1Text),
                ("Clear T2", self.clearT2Text)
            ])
        ]

        # Insert TextTwo menu at the beginning
        return textTwoMenu + baseMenu

    def createUi(self):
        """Create the TextTwo UI components."""
        # Create search bar
        self.createSearchBar()

        # Create horizontal button bar
        self.createHorizontalBtnBar()

        # Create text areas and vertical button bar
        self.createTextAreas()

    def createSearchBar(self):
        """Create the search and replace input bar."""
        # Create search input bar
        self.searchBar = InputBar(self.contentFrame, title="Search:")
        self.searchBar.grid(row=0, column=0, columnspan=3,
                            sticky="ew", padx=5, pady=5)

        # Create replace input bar
        self.replaceBar = InputBar(self.contentFrame, title="Replace:")
        self.replaceBar.grid(row=1, column=0, columnspan=3,
                             sticky="ew", padx=5, pady=5)

    def createHorizontalBtnBar(self):
        """Create the horizontal button bar for search operations."""
        # Define button configurations
        btnConfigs = [
            BtnConfig("Find", self.searchAll, tooltip="Search text"),
            BtnConfig("T1", isLabel=True),
            BtnConfig("Replace", self.replaceT1Text,
                      tooltip="Replace text in T1 area"),
            BtnConfig("Replace All", self.replaceAllT1Text,
                      tooltip="Replace all occurrences in T1 area"),
            BtnConfig("T2", isLabel=True),
            BtnConfig("Replace", self.replaceT2Text,
                      tooltip="Replace text in T2 area"),
            BtnConfig("Replace All", self.replaceAllT2Text,
                      tooltip="Replace all occurrences in T2 area")
        ]

        # Create horizontal button bar
        self.horizontalBtnBar = BtnBar(self.contentFrame,
                                       pady=3, padx=3)
        self.horizontalBtnBar.addBtns(btnConfigs)
        self.horizontalBtnBar.grid(row=2, column=0, columnspan=3,
                                   sticky="ew", padx=5, pady=5)

    def createTextAreas(self):
        """Create the T1 and T2 text areas with vertical button bar."""
        # Create T1 text area
        self.t1TextBar = TextBar(self.contentFrame, title="T1 Text",
                                 showTitleBar=True)
        self.t1TextBar.grid(row=3, column=0, sticky="nsew",
                            padx=(5, 2), pady=5)

        # Create vertical button bar
        self.createVerticalBtnBar()

        # Create T2 text area
        self.t2TextBar = TextBar(self.contentFrame, title="T2 Text",
                                 showTitleBar=True)
        self.t2TextBar.grid(row=3, column=2, sticky="nsew",
                            padx=(2, 5), pady=5)

        # Configure grid weights for proper resizing
        self.contentFrame.grid_columnconfigure(0, weight=1)
        self.contentFrame.grid_columnconfigure(
            1, weight=0)  # Fixed width for button bar
        self.contentFrame.grid_columnconfigure(2, weight=1)
        self.contentFrame.grid_rowconfigure(3, weight=1)

    def createVerticalBtnBar(self):
        """Create the vertical button bar between text areas."""
        # Define vertical button configurations
        btnConfigs = [
            BtnConfig("⇄", self.switchText,
                      tooltip="Switch text between T1 and T2"),
            BtnConfig("→", self.moveT1ToT2,
                      tooltip="Move T1 text to T2"),
            BtnConfig("←", self.moveT2ToT1,
                      tooltip="Move T2 text to T1"),
            BtnConfig("⇔", self.compareText,
                      tooltip="Compare T1 and T2 text"),
            BtnConfig("↻", self.clearCompareColor),
        ]

        # Create vertical button bar
        self.verticalBtnBar = BtnBar(self.contentFrame,
                                     pady=5, padx=5)

        # Configure vertical layout
        for config in btnConfigs:
            button = self.verticalBtnBar.addBtn(config)
            button.pack(side="top", fill="x", padx=2, pady=2)

        self.verticalBtnBar.grid(row=3, column=1, sticky="ns",
                                 padx=2, pady=5)

    def bindEvents(self):
        """Bind events for search functionality."""
        # Bind return key for search
        self.searchBar.bindReturn(self.onSearchReturn)
        self.replaceBar.bindReturn(self.onReplaceReturn)

        # Bind text change events
        self.t1TextBar.textBox.bind(
            "<<Modified>>", self.onT1TextModified)
        self.t2TextBar.textBox.bind(
            "<<Modified>>", self.onT2TextModified)

    def onSearchReturn(self, event=None):
        self.searchAll()

    def onReplaceReturn(self, event=None):
        """Handle replace when return key is pressed."""
        self.replaceT1Text()

    def onT1TextModified(self, event=None):
        """Handle T1 text modification."""
        if self.t1TextBar.textBox.edit_modified():
            self.t1TextBar.textBox.edit_modified(False)
            self.updateT1Text()

    def onT2TextModified(self, event=None):
        """Handle T2 text modification."""
        if self.t2TextBar.textBox.edit_modified():
            self.t2TextBar.textBox.edit_modified(False)
            self.updateT2Text()

    def updateT1Text(self):
        """Update the stored T1 text."""
        self.t1Text = self.t1TextBar.textBox.get("1.0", "end-1c")

    def updateT2Text(self):
        """Update the stored T2 text."""
        self.t2Text = self.t2TextBar.textBox.get("1.0", "end-1c")

    def switchText(self):
        """Switch text between T1 and T2 areas."""
        # Get current text
        t1Text = self.t1TextBar.textBox.get("1.0", "end-1c")
        t2Text = self.t2TextBar.textBox.get("1.0", "end-1c")

        # Swap text
        self.t1TextBar.textBox.delete("1.0", "end")
        self.t1TextBar.textBox.insert("1.0", t2Text)

        self.t2TextBar.textBox.delete("1.0", "end")
        self.t2TextBar.textBox.insert("1.0", t1Text)

        # Update stored text
        self.updateT1Text()
        self.updateT2Text()

        print("✓ Text switched between T1 and T2")

    def compareText(self):
        """Compare text between T1 and T2 areas with visual highlighting.
        T1 is the original text, T2 is the changed result.
        Only highlights differences in T2."""
        t1Text = self.t1TextBar.textBox.get("1.0", "end-1c")
        t2Text = self.t2TextBar.textBox.get("1.0", "end-1c")

        # Clear previous comparison highlights
        self.t1TextBar.textBox.tag_remove("added", "1.0", "end")
        self.t1TextBar.textBox.tag_remove("removed", "1.0", "end")
        self.t1TextBar.textBox.tag_remove("changed", "1.0", "end")
        self.t2TextBar.textBox.tag_remove("added", "1.0", "end")
        self.t2TextBar.textBox.tag_remove("removed", "1.0", "end")
        self.t2TextBar.textBox.tag_remove("changed", "1.0", "end")

        # Configure tag styles for visual highlighting (only in T2)
        self.t2TextBar.textBox.tag_config(
            "added", background="#0D670D")  # Light green
        self.t2TextBar.textBox.tag_config(
            "removed", background="#691824")  # Light red
        self.t2TextBar.textBox.tag_config(
            "changed", background="#453B04")  # Gold

        if t1Text == t2Text:
            print("✓ T1 and T2 text are identical")
            return

        # Calculate differences using line-by-line comparison
        t1Lines = t1Text.split('\n')
        t2Lines = t2Text.split('\n')

        print(f"✗ Text comparison results:")
        print(f"  T1 lines: {len(t1Lines)}")
        print(f"  T2 lines: {len(t2Lines)}")
        print(f"  T1 characters: {len(t1Text)}")
        print(f"  T2 characters: {len(t2Text)}")

        # Find and highlight differences (only in T2)
        maxLines = max(len(t1Lines), len(t2Lines))
        differencesFound = False

        for i in range(maxLines):
            t1Line = t1Lines[i] if i < len(t1Lines) else ""
            t2Line = t2Lines[i] if i < len(t2Lines) else ""

            if t1Line != t2Line:
                differencesFound = True

                if i < len(t2Lines):
                    t2LineStart = f"{i+1}.0"
                    t2LineEnd = f"{i+1}.end"

                if i >= len(t1Lines):
                    # Line added in T2 (not present in T1)
                    self.t2TextBar.textBox.tag_add(
                        "added", t2LineStart, t2LineEnd)
                    print(f"  Line {i+1}: Added in T2 - '{t2Line[:50]}...'" if len(
                        t2Line) > 50 else f"  Line {i+1}: Added in T2 - '{t2Line}'")
                elif i >= len(t2Lines):
                    # Line removed from T2 (present in T1 but not in T2)
                    # No highlighting in T2 for removed lines (they don't exist in T2)
                    print(f"  Line {i+1}: Removed from T2 - '{t1Line[:50]}...'" if len(
                        t1Line) > 50 else f"  Line {i+1}: Removed from T2 - '{t1Line}'")
                else:
                    # Line changed - highlight entire line in T2
                    self.t2TextBar.textBox.tag_add(
                        "changed", t2LineStart, t2LineEnd)

                    # Find character-level differences within the line (only in T2)
                    self.highlightLineDifferences(i+1, t1Line, t2Line)

                    print(f"  Line {i+1}: Changed")
                    print(f"    T1: {t1Line[:50]}..." if len(
                        t1Line) > 50 else f"    T1: {t1Line}")
                    print(f"    T2: {t2Line[:50]}..." if len(
                        t2Line) > 50 else f"    T2: {t2Line}")

        if not differencesFound and len(t1Lines) != len(t2Lines):
            print(f"  Files differ in line count only")

    def highlightLineDifferences(self, lineNum, t1Line, t2Line):
        """Highlight character-level differences within a line (only in T2)."""
        # Simple character-by-character comparison
        minLen = min(len(t1Line), len(t2Line))

        # Find all difference ranges
        diffRanges = []
        j = 0
        while j < minLen:
            if t1Line[j] != t2Line[j]:
                diffStart = j
                while j < minLen and t1Line[j] != t2Line[j]:
                    j += 1
                diffEnd = j
                diffRanges.append((diffStart, diffEnd))
            else:
                j += 1

        # Highlight differences in T2 only
        for diffStart, diffEnd in diffRanges:
            t2StartPos = f"{lineNum}.{diffStart}"
            t2EndPos = f"{lineNum}.{diffEnd}"
            self.t2TextBar.textBox.tag_add("changed", t2StartPos, t2EndPos)

        # Handle case where T2 line is longer than T1 line
        if len(t2Line) > len(t1Line):
            # T2 has extra characters (added in T2)
            startPos = f"{lineNum}.{len(t1Line)}"
            endPos = f"{lineNum}.end"
            self.t2TextBar.textBox.tag_add("added", startPos, endPos)

    def moveT1ToT2(self):
        """Move T1 text to T2 area."""
        t1Text = self.t1TextBar.textBox.get("1.0", "end-1c")
        self.t2TextBar.textBox.insert(tk.END, t1Text)
        self.updateT2Text()
        print("✓ T1 text moved to T2")

    def moveT2ToT1(self):
        """Move T2 text to T1 area."""
        t2Text = self.t2TextBar.textBox.get("1.0", "end-1c")
        self.t1TextBar.textBox.insert(tk.END, t2Text)
        self.updateT1Text()
        print("✓ T2 text moved to T1")

    def searchAll(self):
        self.searchT1()
        self.searchT2()

    def searchT1(self):
        self.searchTextBar(self.t1TextBar)

    def searchT2(self):
        self.searchTextBar(self.t2TextBar)

    def searchTextBar(self, textBar):
        self.searchText = self.searchBar.getValue()
        if self.searchText:
            self.highlightText(textBar, self.searchText)

    def replaceT1Text(self):
        """Replace text in T1 area."""
        self.searchText = self.searchBar.getValue()
        self.replaceText = self.replaceBar.getValue()

        if self.searchText and self.replaceText:
            self.replaceInText(self.t1TextBar,
                               self.searchText, self.replaceText)
            print(
                f"✓ Replaced '{self.searchText}' with '{self.replaceText}' in T1 text")

    def replaceT2Text(self):
        """Replace text in T2 area."""
        self.searchText = self.searchBar.getValue()
        self.replaceText = self.replaceBar.getValue()

        if self.searchText and self.replaceText:
            self.replaceInText(self.t2TextBar,
                               self.searchText, self.replaceText)
            print(
                f"✓ Replaced '{self.searchText}' with '{self.replaceText}' in T2 text")

    def replaceAllT1Text(self):
        """Replace all occurrences in T1 area."""
        self.searchText = self.searchBar.getValue()
        self.replaceText = self.replaceBar.getValue()

        if self.searchText and self.replaceText:
            self.replaceAllInText(
                self.t1TextBar, self.searchText, self.replaceText)
            print(
                f"✓ Replaced all '{self.searchText}' with '{self.replaceText}' in T1 text")

    def replaceAllT2Text(self):
        """Replace all occurrences in T2 area."""
        self.searchText = self.searchBar.getValue()
        self.replaceText = self.replaceBar.getValue()

        if self.searchText and self.replaceText:
            self.replaceAllInText(self.t2TextBar,
                                  self.searchText, self.replaceText)
            print(
                f"✓ Replaced all '{self.searchText}' with '{self.replaceText}' in T2 text")

    def highlightText(self, textBar, searchText):
        """Highlight search results in the specified text bar."""
        # Clear previous highlights
        textBar.textBox.tag_remove("search", "1.0", "end")

        # Search and highlight
        if searchText:
            startIndex = "1.0"
            while True:
                startIndex = textBar.textBox.search(
                    searchText, startIndex, "end")
                if not startIndex:
                    break
                endIndex = f"{startIndex}+{len(searchText)}c"
                textBar.textBox.tag_add("search", startIndex, endIndex)
                startIndex = endIndex

            # Configure highlight style
            textBar.textBox.tag_config(
                "search", background="yellow", foreground="black")

    def replaceInText(self, textBar, searchText, replaceText):
        """Replace first occurrence in the specified text bar."""
        # Find first occurrence
        startIndex = textBar.textBox.search(searchText, "1.0", "end")
        if startIndex:
            endIndex = f"{startIndex}+{len(searchText)}c"
            textBar.textBox.delete(startIndex, endIndex)
            textBar.textBox.insert(startIndex, replaceText)

    def replaceAllInText(self, textBar, searchText, replaceText):
        """Replace all occurrences in the specified text bar."""
        # Get all text
        content = textBar.textBox.get("1.0", "end-1c")

        # Replace all occurrences
        newContent = content.replace(searchText, replaceText)

        # Update text
        textBar.textBox.delete("1.0", "end")
        textBar.textBox.insert("1.0", newContent)

    def clearT1Text(self):
        """Clear T1 text area."""
        self.t1TextBar.textBox.delete("1.0", "end")
        self.updateT1Text()
        print("✓ T1 text cleared")

    def clearT2Text(self):
        """Clear T2 text area."""
        self.t2TextBar.textBox.delete("1.0", "end")
        self.updateT2Text()
        print("✓ T2 text cleared")

    def clearAllText(self):
        """Clear both T1 and T2 text areas."""
        self.clearT1Text()
        self.clearT2Text()
        print("✓ All text cleared")

    def clearCompareColor(self):
        """Clear all comparison highlighting from T1 and T2 text areas."""
        # Clear comparison highlights from both text areas
        self.t1TextBar.textBox.tag_remove("added", "1.0", "end")
        self.t1TextBar.textBox.tag_remove("removed", "1.0", "end")
        self.t1TextBar.textBox.tag_remove("changed", "1.0", "end")
        self.t2TextBar.textBox.tag_remove("added", "1.0", "end")
        self.t2TextBar.textBox.tag_remove("removed", "1.0", "end")
        self.t2TextBar.textBox.tag_remove("changed", "1.0", "end")

        print("✓ Comparison highlights cleared")

    def setT1Text(self, text):
        """Set text in T1 area."""
        self.t1TextBar.textBox.delete("1.0", "end")
        self.t1TextBar.textBox.insert("1.0", text)
        self.updateT1Text()

    def setT2Text(self, text):
        """Set text in T2 area."""
        self.t2TextBar.textBox.delete("1.0", "end")
        self.t2TextBar.textBox.insert("1.0", text)
        self.updateT2Text()

    def getT1Text(self):
        """Get text from T1 area."""
        return self.t1TextBar.textBox.get("1.0", "end-1c")

    def getT2Text(self):
        """Get text from T2 area."""
        return self.t2TextBar.textBox.get("1.0", "end-1c")


if __name__ == "__main__":
    # Create and run TextTwo example
    root = ctk.CTk()
    root.title("TextTwo Example")
    root.geometry("1000x700")

    textTwo = TextTwo(root, title="TextTwo Editor", asWin=False)
    textTwo.pack(fill="both", expand=True, padx=10, pady=10)

    # Set sample text
    textTwo.setT1Text(
        "This is sample T1 text.\nYou can edit this text.\nTry the search and replace features!")
    textTwo.setT2Text(
        "This is sample T2 text.\nYou can also edit this text.\nUse the buttons to switch or compare!")

    root.mainloop()

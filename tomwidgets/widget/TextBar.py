"""
TextBar Widget
==============

A text editing widget that combines a TitleBar at the top with a TextBox 
as content, providing methods to add text with custom size and color.
"""
import tkinter as tk

from .basic.Frame import Frame
from .TitleBar import TitleBar
from .basic.Textbox import Textbox
from .basic.Font import Font
from .PopMenu import PopMenu
from .InputBar import InputBar  # Add import for InputBar


class TextBar(Frame):
    """A text editing widget with title bar and customizable text content."""

    def __init__(self, master, title="", menuCommands=None, showTitleBar=True, **kwargs):
        """
        Initialize the TextBar.

        Args:
            master: The parent widget
            title: The title text to display in the title bar
            menuCommands: List of menu commands for the title bar menu
            showTitleBar: Whether to show the title bar (default: True)
            **kwargs: Additional arguments for Frame
        """
        # Set default size for text bar
        if 'width' not in kwargs:
            kwargs['width'] = 600
        if 'height' not in kwargs:
            kwargs['height'] = 400

        self.title = title

        # Initialize the base frame
        super().__init__(master, **kwargs)

        # Configure grid layout
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)  # Title bar (fixed height)
        self.grid_rowconfigure(1, weight=0)  # Find bar (fixed height)
        self.grid_rowconfigure(2, weight=1)  # Text box (expands)

        # Store components
        self.titleBar = None
        self.findBar = None
        self.textBox: Textbox = None
        self.contextMenu = None
        self._showTitleBar = showTitleBar
        self._showFindBar = True

        # Search tracking
        self.searchResults = []
        self.currentSearchIndex = -1
        self.searchHighlightTag = "search_highlight"

        # Create default menu commands if none provided
        if menuCommands is None:
            menuCommands = self.defaultMenu()
        else:
            menuCommands = menuCommands + self.defaultMenu()

        # Create the components
        self.createTitleBar(menuCommands)
        self.createFindBar()
        self.createTextBox()

        self.toggleFindBar()

    def defaultMenu(self):
        return [
            ("Copy", self.copyTextToClipboard),
            ("Paste", self.pasteFromClipboard),
            ("Cut", self.cutText),
            None,  # Separator
            ("Undo", self.undoText),
            ("Redo", self.redoText),
            None,  # Separator
            ("Strip", self.stripTextTrailingSpaces),
            ("Clear", self.clearText)
        ]

    def createTitleBar(self, menuCommands):
        """Create the title bar at the top."""
        self.titleBar = TitleBar(
            self, title=self.title, menuCommands=menuCommands)

        self.titleBar.addBtnToBar("🔎", self.toggleFindBar)

        if self._showTitleBar:
            self.titleBar.grid(row=0, column=0, sticky="ew", padx=0, pady=0)

    def createFindBar(self):
        """Create the find bar for text search."""
        self.findBar = InputBar(self, title="Find:", default="")
        self.findBar.grid(row=1, column=0, sticky="ew", padx=5, pady=2)

        # Configure find bar styling
        self.findBar.configInput(placeholder_text="Enter text to find...")

        # Bind Enter key to perform search
        self.findBar.bindReturn(self.onFindEnter)

        # Bind text change to real-time search (optional)
        self.findBar.value.trace_add('write', self.onFindTextChange)

    def createTextBox(self):
        """Create the text box as content."""
        box = self.textBox = Textbox(self)

        self.textBox.grid(row=2, column=0, sticky="nsew", padx=5, pady=5)

        # Bind text change events to update line count in title bar
        self.textBox.bind("<KeyRelease>", self._onTextChange)
        self.textBox.bind("<<Modified>>", self._onTextChange)

        # Set up modification tracking
        self.textBox.configure(autoseparators=True, undo=True)

        # Add right-click context menu
        self._createContextMenu()

        # Configure search highlight tag
        self.textBox.box().tag_configure(self.searchHighlightTag,
                                         background="#ff7300",
                                         foreground="black")

        self.titleBar.addVisible(box)

        # Initialize line count display
        self._updateTitleWithLineCount()

    def _createContextMenu(self):
        """Create the right-click context menu using PopMenu."""
        # Create PopMenu instance
        self.contextMenu = PopMenu(self.textBox, self.defaultMenu(), tearoff=0)

        # Bind right-click to show context menu
        self.textBox.bind("<Button-3>", self._showContextMenu)

    def _showContextMenu(self, event):
        """Show the right-click context menu."""
        if self.contextMenu:
            self.contextMenu.show()

    def _onTextChange(self, event=None):
        """Handle text change events to update line count in title bar."""
        self._updateTitleWithLineCount()

        # Reset modified flag for <<Modified>> events
        if hasattr(event, 'type') and str(event.type) == 'Modified':
            self.textBox.edit_modified(False)

    def _updateTitleWithLineCount(self):
        """Update the title bar to show current line count."""
        if self.titleBar:
            original_title = self.title
            line_count = self.getLineCount()
            self.titleBar.setTitle(f"{original_title} - {line_count}")

    def toggleFindBar(self):
        """Toggle the find bar visibility."""
        if self._showFindBar:
            self.findBar.hide()
            self._showFindBar = False
        else:
            self.findBar.show()
            self._showFindBar = True

    def onFindEnter(self, event=None):
        """Handle Enter key press in find bar."""
        searchText = self.findBar.getValue()
        if searchText:
            self.performSearch(searchText)

    def onFindTextChange(self, *args):
        """Handle text change in find bar (real-time search)."""
        searchText = self.findBar.getValue()
        if searchText:
            self.performSearch(searchText)
        else:
            self.clearSearchHighlights()

    def performSearch(self, searchText, caseSensitive=False):
        """Perform text search and highlight results."""
        # Clear previous highlights
        self.clearSearchHighlights()

        if not searchText:
            return

        # Get text content
        content = self.textBox.get("1.0", "end-1c")
        if not content:
            return

        # Prepare search text
        if not caseSensitive:
            searchTextLower = searchText.lower()
            contentLower = content.lower()
        else:
            searchTextLower = searchText
            contentLower = content

        # Find all occurrences
        self.searchResults = []
        start = 0

        while True:
            pos = contentLower.find(searchTextLower, start)
            if pos == -1:
                break

            # Calculate line and column
            lines = content[:pos].split('\n')
            lineNumber = len(lines)
            columnNumber = len(lines[-1]) if lines else 0

            # Calculate end position
            endPos = pos + len(searchText)
            endLines = content[:endPos].split('\n')
            endLineNumber = len(endLines)
            endColumnNumber = len(endLines[-1]) if endLines else 0

            # Store result
            self.searchResults.append({
                'start': pos,
                'end': endPos,
                'line': lineNumber,
                'column': columnNumber,
                'endLine': endLineNumber,
                'endColumn': endColumnNumber
            })

            # Highlight this occurrence
            startPos = f"{lineNumber}.{columnNumber}"
            endPos = f"{endLineNumber}.{endColumnNumber}"
            self.textBox.box().tag_add(self.searchHighlightTag, startPos, endPos)

            start = pos + 1

        # Update current search index
        if self.searchResults:
            self.currentSearchIndex = 0
            self.highlightCurrentSearch()

    def highlightCurrentSearch(self):
        """Highlight the current search result and scroll to it."""
        if not self.searchResults or self.currentSearchIndex < 0:
            return

        # Clear previous current highlight
        self.textBox.box().tag_remove("current_search", "1.0", "end")

        # Configure current search highlight
        self.textBox.box().tag_configure("current_search",
                                         background="orange",
                                         foreground="black")

        # Highlight current result
        result = self.searchResults[self.currentSearchIndex]
        startPos = f"{result['line']}.{result['column']}"
        endPos = f"{result['endLine']}.{result['endColumn']}"

        self.textBox.box().tag_add("current_search", startPos, endPos)

        # Scroll to the current result
        self.textBox.see(startPos)

    def clearSearchHighlights(self):
        """Clear all search highlights."""
        self.textBox.box().tag_remove(self.searchHighlightTag, "1.0", "end")
        self.textBox.box().tag_remove("current_search", "1.0", "end")
        self.searchResults = []
        self.currentSearchIndex = -1

    def findNext(self):
        """Find next occurrence."""
        if not self.searchResults:
            return

        self.currentSearchIndex = (
            self.currentSearchIndex + 1) % len(self.searchResults)
        self.highlightCurrentSearch()

    def findPrevious(self):
        """Find previous occurrence."""
        if not self.searchResults:
            return

        self.currentSearchIndex = (
            self.currentSearchIndex - 1) % len(self.searchResults)
        self.highlightCurrentSearch()

    def setTitle(self, title):
        """
        Set the title text.

        Args:
            title: The new title text
        """
        if self.titleBar:
            self.titleBar.setTitle(title)

    def getTitle(self):
        """
        Get the current title text.

        Returns:
            The current title text
        """
        return self.titleBar.getTitle() if self.titleBar else ""

    def setMenuCommands(self, menuCommands):
        """
        Set or update the menu commands.

        Args:
            menuCommands: List of menu commands
        """
        if self.titleBar:
            self.titleBar.setMenuCommands(menuCommands)

    def getMenuCommands(self):
        """
        Get the current menu commands.

        Returns:
            List of menu commands
        """
        return self.titleBar.getMenuCommands() if self.titleBar else []

    def showTitleBar(self):
        """Show the title bar."""
        if self.titleBar and not self._showTitleBar:
            self._showTitleBar = True
            self.titleBar.grid(row=0, column=0, sticky="ew", padx=0, pady=0)
            self.textBox.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

    def hideTitleBar(self):
        """Hide the title bar."""
        if self.titleBar and self._showTitleBar:
            self._showTitleBar = False
            self.titleBar.grid_forget()
            self.textBox.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

    def toggleTitleBar(self):
        """Toggle the title bar visibility."""
        if self._showTitleBar:
            self.hideTitleBar()
        else:
            self.showTitleBar()

    def clearText(self):
        """Clear all text from the text box."""
        state = self.textBox.state()
        self.setReadOnly(False)

        if self.textBox:
            self.textBox.delete("1.0", "end")

        self.textBox.state(state)

        # Update line count display
        self._updateTitleWithLineCount()

    def getText(self):
        """
        Get all text from the text box.

        Returns:
            The text content
        """
        return self.textBox.get("1.0", "end-1c") if self.textBox else ""

    def setText(self, text):
        """
        Set the text content, replacing existing content.

        Args:
            text: The new text content
        """
        if self.textBox:
            self.textBox.delete("1.0", "end")
            self.textBox.insert("1.0", text)

            # Update line count display
            self._updateTitleWithLineCount()

    def append(self, text: str, color: str = None, size: int = None):
        """
        Append text to the end of the current content.

        Args:
            text: The text to append
        """
        if self.textBox:
            self.textBox.append(text, color, size)
            self._updateTitleWithLineCount()

    def insert(self, index: str, text: str, color: str = None, size: int = None):
        self.insertTo(index, text, color, size)

    def insertTo(self, index: str = tk.END, text: str = "", color: str = None, size: int = None):
        """
        Insert text at a specific position with specified color and size.

        Args:
            index: The position to insert (e.g., "1.0" for line 1, column 0)
            text: The text to insert
            color: The color to set for the inserted text
            size: The font size for the inserted text (optional)
        """
        if self.textBox:
            self.textBox.insertTo(index, text, color, size)
            self._updateTitleWithLineCount()

    def delete(self, start, end):
        """
        Delete text from a specific range.

        Args:
            startLine: Starting line number (1-indexed)
            startCol: Starting column number (0-indexed)
            endLine: Ending line number (1-indexed)
            endCol: Ending column number (0-indexed)
        """
        if self.textBox:
            self.textBox.delete(start, end)

            # Update line count display
            self._updateTitleWithLineCount()

    def setTextColor(self, color):
        """
        Set text color for a specific range or entire text.

        Note: This affects the entire text box due to CTkTextbox limitations.

        Args:
            color: The color to set
        """
        if self.textBox:
            self.textBox.configure(text_color=color)

    def copyTextToClipboard(self):
        """Copy the text content to the clipboard."""
        try:
            text = self.getText()
            if text:
                # Clear clipboard and copy text
                self.clipboard_clear()
                self.clipboard_append(text)
        except Exception as e:
            print(f"Error copying to clipboard: {e}")

    def pasteFromClipboard(self):
        """Paste text from clipboard into the text box."""
        try:
            # Get clipboard content
            clipboard_text = self.clipboard_get()
            if clipboard_text:
                # Insert at current cursor position
                self.textBox.insert(tk.INSERT, clipboard_text)

                # Update line count display
                self._updateTitleWithLineCount()
        except Exception as e:
            print(f"Error pasting from clipboard: {e}")

    def cutText(self):
        """Cut selected text to clipboard."""
        try:
            # Check if there's a selection
            if self.textBox.tag_ranges(tk.SEL):
                # Copy to clipboard
                selected_text = self.textBox.get(tk.SEL_FIRST, tk.SEL_LAST)
                self.clipboard_clear()
                self.clipboard_append(selected_text)

                # Delete the selected text
                self.textBox.delete(tk.SEL_FIRST, tk.SEL_LAST)

                # Update line count display
                self._updateTitleWithLineCount()
        except Exception as e:
            print(f"Error cutting text: {e}")

    def undoText(self):
        """Undo the last text operation."""
        try:
            if self.textBox.edit_undo():
                self._updateTitleWithLineCount()
        except Exception as e:
            print(f"Error undoing: {e}")

    def redoText(self):
        """Redo the last undone text operation."""
        try:
            if self.textBox.edit_redo():
                self._updateTitleWithLineCount()
        except Exception as e:
            print(f"Error redoing: {e}")

    def stripTextTrailingSpaces(self):
        """Strip trailing spaces from each line of text."""
        try:
            text = self.getText()
            if text:
                # Split into lines, strip trailing spaces, and rejoin
                lines = text.splitlines()
                stripped_lines = [line.rstrip() for line in lines]
                stripped_text = '\n'.join(stripped_lines)

                # Update the text box with stripped text
                self.setText(stripped_text)

                self._updateTitleWithLineCount()
        except Exception as e:
            print(f"Error stripping trailing spaces: {e}")

    def setTextSize(self, size):
        """
        Set text size for a specific range or entire text.

        Note: This affects the entire text box due to CTkTextbox limitations.

        Args:
            size: The font size to set
        """
        if self.textBox:
            currentFont = self.textBox.cget("font")
            if isinstance(currentFont, Font):
                fontConfig = {
                    "family": currentFont.cget("family"),
                    "weight": currentFont.cget("weight"),
                    "size": size
                }
                newFont = Font(**fontConfig)
                self.textBox.configure(font=newFont)

    def setReadOnly(self, readOnly=True):
        """
        Set read-only mode.

        Args:
            readOnly: Whether to set read-only mode (default: True)
        """
        if self.textBox:
            state = "disabled" if readOnly else "normal"
            self.textBox.configure(state=state)

    def isReadOnly(self):
        """
        Check if the text box is in read-only mode.

        Returns:
            True if read-only, False otherwise
        """
        if self.textBox:
            return not self.textBox.isEnabled()
        return False

    def getTextLength(self):
        """
        Get the total length of text in the text box.

        Returns:
            Number of characters in the text box
        """
        if self.textBox:
            text = self.textBox.get("1.0", "end-1c")
            return len(text)
        return 0

    def getLineCount(self):
        """
        Get the number of lines in the text box.

        Returns:
            Number of lines
        """
        if self.textBox:
            text = self.textBox.get("1.0", "end-1c")
            return text.count('\n') + 1
        return 0

    def getLineText(self, lineNumber):
        """
        Get text from a specific line.

        Args:
            lineNumber: Line number (1-indexed)

        Returns:
            Text from the specified line
        """
        if self.textBox:
            startPos = f"{lineNumber}.0"
            endPos = f"{lineNumber}.end"
            return self.textBox.get(startPos, endPos)
        return ""

    def setLineText(self, lineNumber, text):
        """
        Set text for a specific line.

        Args:
            lineNumber: Line number (1-indexed)
            text: The new text for the line
        """
        if self.textBox:
            startPos = f"{lineNumber}.0"
            endPos = f"{lineNumber}.end"
            self.textBox.delete(startPos, endPos)
            self.textBox.insert(startPos, text)

            # Update line count display
            self._updateTitleWithLineCount()

    def searchText(self, searchText, caseSensitive=False):
        """
        Search for text in the content.

        Args:
            searchText: Text to search for
            caseSensitive: Whether search is case sensitive (default: False)

        Returns:
            List of positions where text is found
        """
        if self.textBox:
            content = self.textBox.get("1.0", "end-1c")
            if not caseSensitive:
                content = content.lower()
                searchText = searchText.lower()

            positions = []
            start = 0
            while True:
                pos = content.find(searchText, start)
                if pos == -1:
                    break
                positions.append(pos)
                start = pos + 1

            return positions
        return []

    def replaceText(self, searchText, replaceText, caseSensitive=False):
        """
        Replace text in the content.

        Args:
            searchText: Text to search for
            replaceText: Text to replace with
            caseSensitive: Whether search is case sensitive (default: False)

        Returns:
            Number of replacements made
        """
        if self.textBox:
            content = self.textBox.get("1.0", "end-1c")
            if not caseSensitive:
                contentLower = content.lower()
                searchTextLower = searchText.lower()
            else:
                contentLower = content
                searchTextLower = searchText

            count = 0
            start = 0
            while True:
                pos = contentLower.find(searchTextLower, start)
                if pos == -1:
                    break

                # Calculate line and column
                lines = content[:pos].split('\n')
                lineNumber = len(lines)
                columnNumber = len(lines[-1]) if lines else 0

                # Replace the text
                startPos = f"{lineNumber}.{columnNumber}"
                endPos = f"{lineNumber}.{columnNumber + len(searchText)}"
                self.textBox.delete(startPos, endPos)
                self.textBox.insert(startPos, replaceText)

                count += 1
                start = pos + len(replaceText)

                # Update content for next search
                content = self.textBox.get("1.0", "end-1c")
                if not caseSensitive:
                    contentLower = content.lower()

            # Update line count display after all replacements
            self._updateTitleWithLineCount()

            return count
        return 0

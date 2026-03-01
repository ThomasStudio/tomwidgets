"""
CodeWin Widget
==============

A code editor window that extends BaseWin with syntax highlighting support.
Supports multiple programming languages with auto-detection and manual selection.
"""

import re
from typing import List, Dict, Tuple
import os
import tkinter.filedialog as filedialog

from .BaseWin import BaseWin
from .OptionBar import OptionBar
from .InputBar import InputBar
from .TextBar import TextBar
from .Theme import Mode, ColorTheme

FileTypes = [
    ("All Files", "*.*"),
    ("Python Files", "*.py"),
    ("Java Files", "*.java"),
    ("Kotlin Files", "*.kt"),
    ("JavaScript Files", "*.js"),
    ("TypeScript Files", "*.ts"),
    ("HTML Files", "*.html"),
    ("CSS Files", "*.css"),
    ("Text Files", "*.txt")
]


class CodeWin(BaseWin):
    """A code editor window with syntax highlighting support."""

    def __init__(self, master=None, title="Code Editor",
                 language="python", showTitleBar=True, showFolderBar=False,
                 asWin=True, settingsFile='settings.ini', **kwargs):
        """
        Initialize the CodeWin widget.

        Args:
            master: The parent widget
            title: The window title
            language: Default programming language
            showTitleBar: Whether to show the TitleBar initially
            showFolderBar: Whether to show the FolderBar initially
            asWin: Whether to create as a window or frame
            settingsFile: Settings file path
            **kwargs: Additional arguments for BaseWin
        """
        super().__init__(master, title=title, showTitleBar=showTitleBar,
                         showFolderBar=showFolderBar, asWin=asWin,
                         settingsFile=settingsFile, **kwargs)

        # Store language and syntax highlighting configuration
        self.currentLanguage = language
        self.syntaxPatterns = self.getSyntaxPatterns()
        self.currentFilePath = None  # Track current file path

        # Create UI components
        self.createCodeUi()

        # Bind text change events for auto-highlighting
        self.bindTextChangeEvents()

    def getCmds(self):
        """Override to add file menu commands."""
        # Get the base menu from parent class
        baseMenu = super().getCmds()

        # Add File menu with Open, Save, Save As options
        fileMenu = [
            ("File", [
                ("Open", self.openFile),
                ("Save", self.saveFile),
                ("Save As", self.saveFileAs)
            ])
        ]

        # Insert File menu at the beginning of the menu list
        return fileMenu + baseMenu

    def openFile(self):
        """Open a file dialog to select and load a file."""
        filePath = filedialog.askopenfilename(
            title="Open File",
            filetypes=FileTypes
        )

        if filePath:
            try:
                with open(filePath, 'r', encoding='utf-8') as file:
                    content = file.read()
                    self.setText(content)
                    self.currentFilePath = filePath

                    # Update window title to show current file
                    self.updateWindowTitle(os.path.basename(filePath))

                    # Auto-detect language based on file extension
                    self.autoDetectLanguageFromFile(filePath)

                    print(f"✓ File opened: {filePath}")
            except Exception as e:
                print(f"✗ Error opening file: {e}")

    def saveFile(self):
        """Save the current content to the current file."""
        if self.currentFilePath:
            try:
                with open(self.currentFilePath, 'w', encoding='utf-8') as file:
                    content = self.getText()
                    file.write(content)
                    print(f"✓ File saved: {self.currentFilePath}")
            except Exception as e:
                print(f"✗ Error saving file: {e}")
        else:
            # If no current file path, use Save As
            self.saveFileAs()

    def saveFileAs(self):
        """Save the current content to a new file."""
        filePath = filedialog.asksaveasfilename(
            title="Save As",
            defaultextension=".txt",
            filetypes=FileTypes
        )

        if filePath:
            try:
                with open(filePath, 'w', encoding='utf-8') as file:
                    content = self.getText()
                    file.write(content)
                    self.currentFilePath = filePath

                    # Update window title to show current file
                    self.updateWindowTitle(os.path.basename(filePath))

                    print(f"✓ File saved as: {filePath}")
            except Exception as e:
                print(f"✗ Error saving file: {e}")

    def updateWindowTitle(self, fileName):
        """Update the window title to include the current file name."""
        self.titleBar.setTitle(f"{self.title} - {fileName}")

    def autoDetectLanguageFromFile(self, filePath):
        """Auto-detect language based on file extension."""
        extensionToLanguage = {
            '.py': 'python',
            '.java': 'java',
            '.kt': 'kotlin',
            '.js': 'javascript',
            '.ts': 'typescript',
            '.html': 'html',
            '.css': 'css',
        }

        _, ext = os.path.splitext(filePath)
        if ext.lower() in extensionToLanguage:
            detectedLang = extensionToLanguage[ext.lower()]
            if detectedLang != self.currentLanguage:
                self.currentLanguage = detectedLang
                self.languageBar.setSelectedOption(detectedLang.capitalize())
                self.applySyntaxHighlighting()
                print(f"✓ Language auto-detected from file: {detectedLang}")

    def getText(self):
        """Get the current text content from the TextBar."""
        return self.textBar.textBox.box().get("1.0", "end-1c")

    def setText(self, content):
        """Set the text content in the TextBar."""
        textWidget = self.textBar.textBox.box()
        textWidget.delete("1.0", "end")
        textWidget.insert("1.0", content)
        self.applySyntaxHighlighting()

    def createCodeUi(self):
        """Create the code editing UI components."""
        # Create OptionBar for language selection
        languages = ["Python", "Kotlin", "Java",
                     "JavaScript", "TypeScript", "HTML", "CSS"]
        self.languageBar = OptionBar(self.contentFrame,
                                     title="Language:",
                                     options=languages,
                                     defaultOption=self.currentLanguage.capitalize())
        self.languageBar.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

        # Create InputBar for search functionality
        self.searchBar = InputBar(self.contentFrame, title="Search:")
        self.searchBar.grid(row=0, column=1, sticky="ew", padx=5, pady=5)

        # Create TextBar for code editing
        self.textBar = TextBar(self.contentFrame, title="")
        self.textBar.grid(row=1, column=0, columnspan=2,
                          sticky="nsew", padx=5, pady=5)

        # Configure grid weights
        self.contentFrame.grid_columnconfigure(0, weight=0)
        self.contentFrame.grid_columnconfigure(1, weight=1)
        self.contentFrame.grid_rowconfigure(1, weight=1)

        # Bind events
        self.languageBar.optionMenu.configure(command=self.onLanguageChange)
        self.searchBar.bindReturn(self.onSearch)

    def bindTextChangeEvents(self):
        """Bind text change events for auto-highlighting."""
        # Get the text widget from TextBar
        textWidget = self.textBar.textBox.box()

        # Bind to text modification events
        textWidget.bind("<<Modified>>", self.onTextModified)
        textWidget.bind("<KeyRelease>", self.onKeyRelease)

    def onLanguageChange(self, selectedLanguage):
        """Handle language selection change.

        Args:
            selectedLanguage: The newly selected language
        """
        self.currentLanguage = selectedLanguage.lower()
        self.applySyntaxHighlighting()
        print(f"✓ Language changed to: {self.currentLanguage}")

    def onSearch(self, event=None):
        """Handle search functionality.

        Args:
            event: The event object (optional)
        """
        searchText = self.searchBar.getValue()
        if searchText:
            self.highlightSearchResults(searchText)

    def onTextModified(self, event=None):
        """Handle text modification for auto-highlighting.

        Args:
            event: The event object (optional)
        """
        textWidget = self.textBar.textBox.box()
        if textWidget.edit_modified():
            textWidget.edit_modified(False)
            self.autoDetectLanguage()
            self.applySyntaxHighlighting()

    def onKeyRelease(self, event=None):
        """Handle key release for real-time highlighting.

        Args:
            event: The event object (optional)
        """
        # Apply highlighting after a short delay to avoid performance issues
        self.after(100, self.applySyntaxHighlighting)

    def autoDetectLanguage(self):
        """Auto-detect the programming language based on content."""
        content = self.getText()

        # Language detection patterns
        detectionPatterns = {
            "python": [r"^\s*import\s+\w+", r"^\s*from\s+\w+", r" __name__ ", r"^\s*def\s+\w+", r"^\s*class\s+\w+"],
            "java": [r"^\s*import\s+[\w\.]+\*?\s*;", r"^\s*public\s+class\s+\w+", r"^\s*private\s+\w+"],
            "kotlin": [r"^\s*import\s+[\w\.]+\*?\s*", r"^\s*class\s+\w+", r"^\s*fun\s+\w+"],
            "javascript": [r"^\s*function\s+\w+", r"^\s*const\s+\w+", r"^\s*let\s+\w+"],
            "typescript": [r"^\s*interface\s+\w+", r"^\s*type\s+\w+", r"^\s*export\s+\w+"],
            "html": [r"^\s*<!DOCTYPE\s+html>", r"<html", r"<body"],
            "css": [r"^\s*body\s*{", r"^\s*html\s*{", r"^\s*@import\s+url\s*"]
        }

        scores = {}
        for lang, patterns in detectionPatterns.items():
            score = 0
            for pattern in patterns:
                if re.search(pattern, content, re.MULTILINE | re.IGNORECASE):
                    score += 1
            scores[lang] = score

        # Select language with highest score
        if scores:
            detectedLang = max(scores, key=scores.get)
            if scores[detectedLang] > 0 and detectedLang != self.currentLanguage:
                self.currentLanguage = detectedLang
                self.languageBar.setSelectedOption(detectedLang.capitalize())

    def getSyntaxPatterns(self) -> Dict[str, List[Tuple[str, str]]]:
        """Get syntax highlighting patterns for different languages.

        Returns:
            Dictionary mapping languages to pattern lists
        """
        return {
            "python": [
                (r'\b(def|class|import|from|as|if|else|elif|for|while|return|try|except|finally|with|pass|break|continue|lambda|yield|global|nonlocal|assert|del|in|is|not|and|or|True|False|None)\b', "keyword"),
                (r'\bclass\b\s+(\w+)\b', "class"),
                (r'\b([0-9]+(\.[0-9]*)?|\.[0-9]+)\b', "number"),
                (r'"[^"]*"|\'[^\']*\'', "string"),
                (r'#[^\n]*', "comment"),
                (r'"""[^\n]*"""', "comment"),
                (r"'''[^\n]*'''", "comment"),
                (r'\b(self)\b', "self"),
                # Method names before parentheses
                (r'\b(\w+)\s*(?=\()', "method"),
                # Class names after 'class' keyword
            ],
            "java": [
                (r'\b(public|private|protected|class|interface|extends|implements|static|final|void|int|long|double|float|char|boolean|String|if|else|for|while|do|switch|case|break|continue|return|try|catch|finally|throw|throws|new|this|super|import|package|true|false|null)\b', "keyword"),
                (r'\b([0-9]+(\.[0-9]*)?|\.[0-9]+)\b', "number"),
                (r'"[^"]*"|\'[^\']*\'', "string"),
                (r'//[^\n]*|/\\*.*?\\*/', "comment"),
                # Method names before parentheses
                (r'\b(\w+)\s*(?=\()', "method"),
                # Class names after 'class' keyword
                (r'\b(class\s+)(\w+)\b', "class"),
            ],
            "kotlin": [
                (r'\b(fun|class|interface|object|val|var|private|protected|public|internal|override|open|abstract|final|enum|data|sealed|typealias|constructor|init|this|super|if|else|when|for|while|do|try|catch|finally|throw|return|break|continue|import|package|as|is|in|!in|!is|null|true|false)\b', "keyword"),
                (r'\b([0-9]+(\.[0-9]*)?|\.[0-9]+)\b', "number"),
                (r'"[^"]*"|\'[^\']*\'', "string"),
                (r'//[^\n]*|/\\*.*?\\*/', "comment"),
                # Method names after 'fun' keyword
                (r'\b(fun\s+)(\w+)\b', "method"),
                # Class names after 'class' keyword
                (r'\b(class\s+)(\w+)\b', "class"),
            ],
            "javascript": [
                (r'\b(function|var|let|const|class|if|else|for|while|do|switch|case|break|continue|return|try|catch|finally|throw|new|this|super|import|export|default|extends|async|await|true|false|null|undefined|typeof|instanceof|in|delete|void|yield)\b', "keyword"),
                (r'\b([0-9]+(\.[0-9]*)?|\.[0-9]+)\b', "number"),
                (r'"[^"]*"|\'[^\']*\'|`[^`]*`', "string"),
                (r'//[^\n]*|/\\*.*?\\*/', "comment"),
                # Method names before parentheses
                (r'\b(\w+)\s*(?=\()', "method"),
                # Variable names that could be functions
                (r'\b(const|let|var)\s+(\w+)\s*(?==)', "method"),
                # Class names after 'class' keyword
                (r'\b(class\s+)(\w+)\b', "class"),
            ],
            "typescript": [
                (r'\b(function|var|let|const|class|interface|type|enum|namespace|module|import|export|default|extends|implements|private|protected|public|readonly|abstract|static|async|await|if|else|for|while|do|switch|case|break|continue|return|try|catch|finally|throw|new|this|super|true|false|null|undefined|typeof|instanceof|in|delete|void|yield)\b', "keyword"),
                (r'\b(class\s+)(\w+)\b', "class"),
                (r'\b([0-9]+(\.[0-9]*)?|\.[0-9]+)\b', "number"),
                (r'"[^"]*"|\'[^\']*\'|`[^`]*`', "string"),
                (r'//[^\n]*|/\\*.*?\\*/', "comment"),
                # Method names before parentheses
                (r'\b(\w+)\s*(?=\()', "method"),
                # Variable names that could be functions
                (r'\b(const|let|var)\s+(\w+)\s*(?==)', "method"),
                # Class names after 'class' keyword
            ],
            "html": [
                # HTML tags
                (r'<\s*[a-zA-Z][a-zA-Z0-9]*', "keyword"),
                (r'</\s*[a-zA-Z][a-zA-Z0-9]*\s*>', "keyword"),
                # HTML attributes
                (r'\b([a-zA-Z][a-zA-Z0-9]*)\s*=', "method"),
                # HTML attribute values
                (r'="[^"]*"', "string"),
                (r'=\'[^\']*\'', "string"),
                # HTML comments
                (r'<!--.*?-->', "comment"),
                # Doctype
                (r'<!.*?>', "comment"),
            ],
            "css": [
                # CSS selectors
                (r'[a-zA-Z][a-zA-Z0-9]*\s*{', "class"),
                (r'\.[a-zA-Z][a-zA-Z0-9_-]*', "class"),
                (r'#[a-zA-Z][a-zA-Z0-9_-]*', "class"),
                # At-rules like @media, @import
                (r'@[a-zA-Z][a-zA-Z0-9_-]*', "keyword"),
                # CSS properties
                (r'[a-zA-Z-]+\s*(?=:)', "method"),
                # CSS values
                (r':\s*[^;]*;', "string"),
                # CSS comments
                (r'/\\*.*?\\*/', "comment"),
                # Numbers in CSS
                (r'\b[0-9]+(\.[0-9]*)?(\s*(px|em|rem|%|pt|cm|mm|in|pc|ex|ch|vw|vh|vmin|vmax|s|ms|deg|rad|grad|turn|dpi|dpcm|dppx)?)\b', "number"),
            ]
        }

    def getSyntaxColors(self) -> Dict[str, str]:
        """Get syntax highlighting colors for different syntax elements.

        Returns:
            Dictionary mapping syntax elements to colors
        """
        if self.currentMode == Mode.Light:
            return {
                "keyword": "#0000FF",      # Blue for keywords
                "number": "#008000",      # Green for numbers
                "string": "#BA2121",      # Red for strings
                "comment": "#888888",     # Gray for comments
                "self": "#8B4513",        # SaddleBrown for self
                "method": "#FF4500",      # OrangeRed for methods
                "class": "#800080",       # Purple for classes
            }
        else:
            return {
                "keyword": "#105BC5",
                "number": "#20D820",
                "string": "#E83939",
                "comment": "#888888",
                "self": "#8B4513",
                "method": "#CBE126",
                "class": "#F223F6",
            }

    def applySyntaxHighlighting(self):
        """Apply syntax highlighting to the current text content."""
        if not self.currentLanguage or self.currentLanguage not in self.syntaxPatterns:
            return

        content = self.getText()
        if not content:
            return

        # Clear existing tags
        self.clearSyntaxTags()

        # Get patterns and colors for current language
        patterns = self.syntaxPatterns[self.currentLanguage]
        colors = self.getSyntaxColors()

        # Apply highlighting for each pattern
        for pattern, syntaxType in patterns:
            if syntaxType in colors:
                self.highlightPattern(pattern, colors[syntaxType])

    def clearSyntaxTags(self):
        """Clear all syntax highlighting tags."""
        textWidget = self.textBar.textBox.box()
        tagNames = textWidget.tag_names()
        for tag in tagNames:
            if tag.startswith("syntax_"):
                textWidget.tag_delete(tag)

    def highlightPattern(self, pattern: str, color: str):
        """Highlight text matching a specific pattern.

        Args:
            pattern: Regular expression pattern
            color: Color to apply
        """
        content = self.getText()
        if not content:
            return

        # Create a unique tag name
        tagName = f"syntax_{hash(pattern) & 0xFFFFFFFF}"

        # Configure the tag
        textWidget = self.textBar.textBox.box()
        textWidget.tag_configure(tagName, foreground=color)

        # Find and apply tags
        matches = re.finditer(pattern, content, re.MULTILINE | re.DOTALL)
        for match in matches:
            startPos = f"1.0+{match.start()}c"
            endPos = f"1.0+{match.end()}c"
            textWidget.tag_add(tagName, startPos, endPos)

    def highlightSearchResults(self, searchText: str):
        """Highlight search results in the text.

        Args:
            searchText: Text to search for
        """
        # Clear previous search highlights
        self.clearSearchHighlights()

        if not searchText:
            return

        content = self.getText()
        if not content:
            return

        # Create search tag
        searchTag = "search_highlight"
        textWidget = self.textBar.textBox.box()
        textWidget.tag_configure(
            searchTag, background="yellow", foreground="black")

        # Find and highlight matches
        pattern = re.escape(searchText)
        matches = re.finditer(pattern, content, re.IGNORECASE)
        for match in matches:
            startPos = f"1.0+{match.start()}c"
            endPos = f"1.0+{match.end()}c"
            textWidget.tag_add(searchTag, startPos, endPos)

    def clearSearchHighlights(self):
        """Clear search result highlights."""
        textWidget = self.textBar.textBox.box()
        if "search_highlight" in textWidget.tag_names():
            textWidget.tag_delete("search_highlight")

    def setLanguage(self, language: str):
        """Set the programming language manually.

        Args:
            language: Programming language to set
        """
        if language.lower() in self.syntaxPatterns:
            self.currentLanguage = language.lower()
            self.languageBar.setSelectedOption(language.capitalize())
            self.applySyntaxHighlighting()

    def getLanguage(self) -> str:
        """Get the current programming language.

        Returns:
            Current programming language
        """
        return self.currentLanguage

    def setCode(self, code: str, language: str = None):
        """Set code content with optional language.

        Args:
            code: Code content to set
            language: Programming language (optional)
        """
        if language:
            self.setLanguage(language)

        self.setText(code)
        self.applySyntaxHighlighting()

    def getCode(self) -> str:
        """Get the current code content.

        Returns:
            Current code content
        """
        return self.getText()

    def setText(self, text: str):
        """Set the text content.

        Args:
            text: Text to set
        """
        self.textBar.setText(text)

    def getText(self) -> str:
        """Get the current text content.

        Returns:
            Current text content
        """
        return self.textBar.getText()

    def searchAndReplace(self, searchText: str, replaceText: str, replaceAll: bool = False):
        """Search and replace functionality.

        Args:
            searchText: Text to search for
            replaceText: Text to replace with
            replaceAll: Whether to replace all occurrences
        """
        content = self.getText()
        if not content or not searchText:
            return

        # Perform search and replace
        if replaceAll:
            newContent = content.replace(searchText, replaceText)
            self.setText(newContent)
        else:
            # Find first occurrence and replace
            index = content.find(searchText)
            if index != -1:
                newContent = content[:index] + replaceText + \
                    content[index + len(searchText):]
                self.setText(newContent)

        # Re-apply syntax highlighting
        self.applySyntaxHighlighting()

    def showSearchBar(self):
        """Show the search bar."""
        self.searchBar.grid()

    def hideSearchBar(self):
        """Hide the search bar."""
        self.searchBar.grid_remove()

    def toggleSearchBar(self):
        """Toggle search bar visibility."""
        if self.searchBar.winfo_ismapped():
            self.hideSearchBar()
        else:
            self.showSearchBar()

    def setMode(self, mode, theme=ColorTheme.Gold):
        super().setMode(mode, theme)
        self.applySyntaxHighlighting()

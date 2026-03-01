import re
import tkinter as tk

from ..widget.BaseWin import BaseWin
from ..widget.OptionBar import OptionBar
from ..widget.InputBar import InputBar
from ..widget.BtnBar import BtnBar, BtnConfig
from ..widget.TextBar import TextBar
from ..widget.basic.Frame import Frame
from ..widget.basic.Entry import Entry


class RETool(BaseWin):
    def __init__(self, master=None, title="RETool", showTitleBar=True, showFolderBar=False, asWin=True, **kwargs):
        super().__init__(master, title, showTitleBar, showFolderBar, asWin, **kwargs)

        # Default regex patterns
        self.regexPatterns = [
            r"\d+",
            r"\w+",
            r"\s+",
            r"[A-Za-z]+",
            r"[0-9]+",
            r"[A-Za-z0-9]+",
            r"\b\w+\b",
            r"\b\d+\b",
            r"^\w+$",
            r"^\d+$"
        ]

        # Initialize UI components
        self.optionBar = None
        self.inputBar = None
        self.btnBar = None
        self.entry = None
        self.inputTextBar = None
        self.outputTextBar = None

        # Create the UI
        self.createUi()

    def createUi(self):
        """Create the user interface components."""
        # Create OptionBar for regex patterns
        self.createOptionBar()

        # Create InputBar to show selected pattern
        self.createInputBar()

        f = Frame(self.topFrame)
        f.grid(row=2, column=0, sticky="w", padx=5, pady=5)
        # Create BtnBar with Join, Switch, and Find buttons
        self.createBtnBar(f)

        # Create Entry for custom text input
        self.createEntry(f)

        # Create main frame with two TextBars
        self.createMainFrame()

    def createOptionBar(self):
        """Create the OptionBar for regex pattern selection."""
        self.optionBar = OptionBar(self.topFrame,
                                   title="Regex Patterns:",
                                   options=self.regexPatterns,
                                   defaultOption=self.regexPatterns[0])
        self.optionBar.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

        # Bind option selection to update input bar
        self.optionBar.bindEvent(self.onPatternSelected)

    def createInputBar(self):
        """Create the InputBar to display selected regex pattern."""
        self.inputBar = InputBar(self.topFrame, title="Selected Pattern:")
        self.inputBar.grid(row=1, column=0, sticky="ew", padx=5, pady=5)

        # Set initial pattern
        initialPattern = self.optionBar.getSelectedOption()
        self.inputBar.setValue(initialPattern)

        # Bind Enter key to run regex find
        self.inputBar.bindReturn(self.runRegexFind)

    def createBtnBar(self, parent):
        """Create the BtnBar with Join, Switch, and Find buttons."""
        btnConfigs = [
            BtnConfig("Join", self.onJoinClicked,
                      tooltip="Join text from Entry with output"),
            BtnConfig("Switch", self.onSwitchClicked,
                      tooltip="Switch text between input and output"),
            BtnConfig("Find", self.onFindClicked,
                      tooltip="Find text in Entry in both input and output")
        ]

        self.btnBar = BtnBar(parent)
        self.btnBar.pack(side=tk.LEFT)
        self.btnBar.addBtns(btnConfigs)

    def createEntry(self, parent):
        """Create the Entry widget for custom text input."""
        self.entry = Entry(parent)
        self.entry.pack(side=tk.LEFT)

    def createMainFrame(self):
        """Create the main frame with two TextBars."""
        f = self.mainFrame()

        # Configure grid layout for main frame
        f.grid_columnconfigure(0, weight=1)
        f.grid_columnconfigure(1, weight=1)
        f.grid_rowconfigure(0, weight=1)

        # Create input TextBar
        self.inputTextBar = TextBar(
            f, title="Input Text", showTitleBar=True)
        self.inputTextBar.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        # Create output TextBar
        self.outputTextBar = TextBar(
            f, title="Output Text", showTitleBar=True)
        self.outputTextBar.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

    def onPatternSelected(self, event=None):
        """Handle pattern selection from OptionBar."""
        selectedPattern = self.optionBar.getSelectedOption()
        self.inputBar.setValue(selectedPattern)

    def runRegexFind(self, event=None):
        """Run regex find operation on input text and show results in output."""
        try:
            # Get the selected pattern
            pattern = self.inputBar.getValue()

            # Get the input text
            inputText = self.inputTextBar.getText()

            if not pattern or not inputText:
                return

            # Find all matches using regex
            matches = re.findall(pattern, inputText)

            bar = self.outputTextBar
            bar.append(f"Matched: {len(matches)}\n")
            for match in matches:
                bar.append(f"{match}\n", "gold", "22")

            # Display results in output TextBar

        except re.error as e:
            self.outputTextBar.setText(f"Regex Error: {str(e)}")
        except Exception as e:
            self.outputTextBar.setText(f"Error: {str(e)}")

    def onJoinClicked(self):
        """Handle Join button click - join lines in output using Entry text as separator."""
        try:
            # Get text from Entry to use as separator
            separator = self.entry.get()

            # Get current output text
            outputText = self.inputTextBar.getText()

            if outputText:
                # Split the output text into lines
                lines = outputText.splitlines()

                # Join the lines using the separator from Entry
                if separator:
                    joinedText = separator.join(lines)
                else:
                    # If no separator, just join with empty string (remove line breaks)
                    joinedText = ''.join(lines)

                # Update output TextBar with the joined result
                self.outputTextBar.append(f"{joinedText}\n")

        except Exception as e:
            self.outputTextBar.setText(f"Join Error: {str(e)}")

    def onSwitchClicked(self):
        """Handle Switch button click - switch text between input and output."""
        try:
            # Get current text from both TextBars
            inputText = self.inputTextBar.getText()
            outputText = self.outputTextBar.getText()

            # Switch the text
            self.inputTextBar.setText(outputText)
            self.outputTextBar.setText(inputText)

        except Exception as e:
            self.outputTextBar.setText(f"Switch Error: {str(e)}")

    def onFindClicked(self):
        """Handle Find button click - find Entry text in both input and output."""
        try:
            # Get text from Entry
            searchText = self.entry.get()

            if not searchText:
                return

            # Get text from both TextBars
            inputText = self.inputTextBar.getText()
            outputText = self.outputTextBar.getText()

            # Clear existing highlights
            self.clearHighlights()

            # Find and highlight in input TextBar
            if inputText:
                self.highlightText(self.inputTextBar, searchText)

            # Find and highlight in output TextBar
            if outputText:
                self.highlightText(self.outputTextBar, searchText)

        except Exception as e:
            self.outputTextBar.setText(f"Find Error: {str(e)}")

    def highlightText(self, textBar, searchText):
        """Highlight the specified text in a TextBar with yellow color."""
        try:
            # Get the text content
            content = textBar.getText()

            if not content:
                return

            # Clear existing text
            textBar.clearText()

            # Insert text with highlighting
            startIdx = 0
            while True:
                # Find the next occurrence
                idx = content.find(searchText, startIdx)
                if idx == -1:
                    # Insert remaining text
                    if startIdx < len(content):
                        remainingText = content[startIdx:]
                        textBar.append(remainingText)
                    break

                # Insert text before the match
                if idx > startIdx:
                    beforeText = content[startIdx:idx]
                    textBar.append(beforeText)

                # Insert the match with yellow color
                textBar.append(searchText, "yellow")

                # Update start index
                startIdx = idx + len(searchText)

        except Exception as e:
            print(f"Highlight error: {e}")

    def clearHighlights(self):
        """Clear all text highlights in both TextBars."""
        try:
            # Get current text from both TextBars
            inputText = self.inputTextBar.getText()
            outputText = self.outputTextBar.getText()

            # Reset text without formatting
            self.inputTextBar.setText(inputText)
            self.outputTextBar.setText(outputText)

        except Exception as e:
            print(f"Clear highlights error: {e}")

    def addRegexPattern(self, pattern):
        """Add a new regex pattern to the OptionBar."""
        if pattern not in self.regexPatterns:
            self.regexPatterns.append(pattern)
            self.optionBar.setOptions(self.regexPatterns)

    def removeRegexPattern(self, pattern):
        """Remove a regex pattern from the OptionBar."""
        if pattern in self.regexPatterns:
            self.regexPatterns.remove(pattern)
            self.optionBar.setOptions(self.regexPatterns)

    def getInputText(self):
        """Get the text from the input TextBar."""
        return self.inputTextBar.getText()

    def setInputText(self, text):
        """Set the text in the input TextBar."""
        self.inputTextBar.setText(text)

    def getOutputText(self):
        """Get the text from the output TextBar."""
        return self.outputTextBar.getText()

    def setOutputText(self, text):
        """Set the text in the output TextBar."""
        self.outputTextBar.setText(text)

    def getSelectedPattern(self):
        """Get the currently selected regex pattern."""
        return self.optionBar.getSelectedOption()

    def setSelectedPattern(self, pattern):
        """Set the selected regex pattern."""
        if pattern in self.regexPatterns:
            self.optionBar.setSelectedOption(pattern)
            self.inputBar.setValue(pattern)

    def showAdvancedExamples(self):
        self.showTips("Advanced Examples", tipsAdvanced)

    def getCmds(self):
        """Override to add Python regex tips menu."""
        # Get the base menu commands
        baseMenu = super().getCmds()

        # Define Python regex tips submenu
        regexTipsMenu = [
            ("All", self.showAllPatterns),
            ("Basic Patterns", self.showBasicPatterns),
            ("Character Classes", self.showCharacterClasses),
            ("Quantifiers", self.showQuantifiers),
            ("Anchors", self.showAnchors),
            ("Groups & Lookarounds", self.showGroupsLookarounds),
            ("Common Examples", self.showCommonExamples),
            ("Advanced Examples", self.showAdvancedExamples)
        ]

        # Add regex tips menu to the base menu
        if isinstance(baseMenu, list):
            # Insert regex tips at the beginning
            baseMenu.insert(0, ("Regex Tips", regexTipsMenu))

        return baseMenu

    def showAllPatterns(self):
        tipsAll = "\n\n".join([tipsBasic, tipsCharacter, tipsQuantifiers,
                              tipsAnchors, tipsGroup, tipsCommon, tipsAdvanced])
        self.showTips("All Patterns", tipsAll)

    def showBasicPatterns(self):
        self.showTips("Basic Patterns", tipsBasic)

    def showCharacterClasses(self):
        self.showTips("Character Classes", tipsCharacter)

    def showQuantifiers(self):
        self.showTips("Quantifiers", tipsQuantifiers)

    def showAnchors(self):
        self.showTips("Anchors", tipsAnchors)

    def showGroupsLookarounds(self):
        self.showTips("Groups & Lookarounds", tipsGroup)

    def showCommonExamples(self):
        self.showTips("Common Examples", tipsCommon)

    def showTips(self, title, content):
        """Display regex tips in the output TextBar."""
        try:
            self.outputTextBar.setText(f"=== {title} ===\n{content}")
        except Exception as e:
            print(f"Error showing tips: {e}")


tipsBasic = r"""Basic Regex Patterns:

• \d - Matches any digit (0-9)
• \w - Matches any word character (a-z, A-Z, 0-9, _)
• \s - Matches any whitespace character
• . - Matches any character except newline
• [abc] - Matches any character in the brackets
• [^abc] - Matches any character NOT in the brackets"""


tipsCharacter = r"""Character Classes:

• \d - Digit [0-9]
• \D - Non-digit [^0-9]
• \w - Word character [a-zA-Z0-9_]
• \W - Non-word character [^a-zA-Z0-9_]
• \s - Whitespace [ \t\n\r\f\v]
• \S - Non-whitespace [^ \t\n\r\f\v]
• [a-z] - Lowercase letters
• [A-Z] - Uppercase letters
• [0-9] - Digits
• [a-zA-Z] - All letters"""

tipsQuantifiers = r"""Quantifiers:

• * - 0 or more occurrences
• + - 1 or more occurrences
• ? - 0 or 1 occurrence
• {n} - Exactly n occurrences
• {n,} - n or more occurrences
• {n,m} - Between n and m occurrences

Greedy vs Lazy:
• *? - Lazy (matches as few as possible)
• +? - Lazy
• ?? - Lazy"""

tipsAnchors = r"""Anchors:

• ^ - Start of string (or line in multi-line mode)
• $ - End of string (or line in multi-line mode)
• \b - Word boundary
• \B - Non-word boundary
• \A - Start of string (ignores multi-line)
• \Z - End of string (ignores multi-line)

Examples:
• ^hello - Starts with 'hello'
• world$ - Ends with 'world'
• \bword\b - Whole word 'word'"""

tipsGroup = r"""Groups & Lookarounds:

Capturing Groups:
• (pattern) - Capturing group
• (?:pattern) - Non-capturing group

Lookarounds:
• (?=pattern) - Positive lookahead
• (?!pattern) - Negative lookahead
• (?<=pattern) - Positive lookbehind
• (?<!pattern) - Negative lookbehind

Backreferences:
• \1, \2, etc. - Reference captured groups"""

tipsCommon = r"""Common Regex Examples:

Email: \b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b
Phone: \d{3}-\d{3}-\d{4}
URL: https?:\/\/(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b(?:[-a-zA-Z0-9()@:%_\+.~#?&\/=]*)
IP: \b(?:\d{1,3}\.){3}\d{1,3}\b
Date: \d{4}-\d{2}-\d{2}
Time: \d{2}:\d{2}(?::\d{2})?
Hex Color: #[0-9a-fA-F]{6}\b

More Examples:
Username: ^[a-zA-Z0-9_-]{3,16}$
Password: ^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$
Credit Card: ^\d{4}-\d{4}-\d{4}-\d{4}$
Zip Code: ^\d{5}(-\d{4})?$
HTML Tag: <([a-z]+)([^<]+)*(?:>(.*)<\/\1>|\s+\/>)
File Extension: \.[a-zA-Z0-9]+$
Number Range (1-100): ^([1-9]|[1-9][0-9]|100)$
Remove HTML Tags: <[^>]*>
Extract Numbers: \d+
Find Duplicate Words: \b(\w+)\s+\1\b
Match Quotes: "[^"]*"|'[^']*'
Validate JSON Key: "[^"]*"\s*:
Extract URLs: https?:\/\/[^\s]+
Find Comments: \/\/.*|\/\*[\s\S]*?\*\/
"""


tipsAdvanced = r"""Advanced Regex Examples:

Multi-line Email Validation: 
^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$

Complex Password (8+ chars, 1 upper, 1 lower, 1 digit, 1 special):
^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$

XML/HTML Attribute Extraction:
(\w+)="([^"]*)"|(\w+)='([^']*)'

CSS Color Values (hex, rgb, rgba, hsl, hsla):
#([a-fA-F0-9]{6}|[a-fA-F0-9]{3})|rgb\(\s*\d{1,3}\s*,\s*\d{1,3}\s*,\s*\d{1,3}\s*\)|rgba\(\s*\d{1,3}\s*,\s*\d{1,3}\s*,\s*\d{1,3}\s*,\s*[01]?(?:\.\d+)?\s*\)|hsl\(\s*\d{1,3}\s*,\s*\d{1,3}%\s*,\s*\d{1,3}%\s*\)|hsla\(\s*\d{1,3}\s*,\s*\d{1,3}%\s*,\s*\d{1,3}%\s*,\s*[01]?(?:\.\d+)?\s*\)

SQL Injection Detection:
(\b(UNION|SELECT|INSERT|UPDATE|DELETE|DROP|CREATE|ALTER)\b.*\b(WHERE|FROM|INTO|TABLE)\b|\b(OR|AND)\b\s*\d+\s*=\s*\d+|\b(EXEC|EXECUTE|XP_CMDSHELL)\b)

Log File Parsing (Apache/Nginx):
^(\S+) (\S+) (\S+) \[([^\]]+)\] "([A-Z]+) ([^ "]+) HTTP\/([0-9.]+)" (\d+) (\d+) "([^"]*)" "([^"]*)"

CSV Parsing (handles quoted fields):
("([^"]*)"|([^,\n]*)),?

Markdown Link Extraction:
\[([^\]]+)\]\(([^\)]+)\)

JSON Path Extraction:
\$\.([a-zA-Z_][a-zA-Z0-9_]*)(?:\[([0-9]+)\])?(?:\.([a-zA-Z_][a-zA-Z0-9_]*))*(?:\[([0-9]+)\])*

Domain Name Validation:
^([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}$

Time Format (12h/24h):
^(0?[1-9]|1[0-2]):[0-5][0-9]\s?(AM|PM)?$|^([01]?[0-9]|2[0-3]):[0-5][0-9]$

Currency Format (various):
^\$?\d{1,3}(?:,\d{3})*(?:\.\d{2})?$|^\$?\d+(?:\.\d{2})?$|^\d{1,3}(?: \d{3})*(?:,\d{2})?\s?[A-Z]{3}$

Phone Number (International):
^\+?[1-9]\d{1,14}$

Base64 Encoding Detection:
^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$

UUID Validation:
^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$"""

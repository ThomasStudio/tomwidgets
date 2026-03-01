from .TextBar import TextBar


class DictView(TextBar):
    def __init__(self, master, dictionary=None, title="Dict View",
                 keyColor="blue", keySize=10,
                 valueColor="green", valueSize=10, splitChar=" = ", lineChar="\n",
                 **kwargs):
        """
        Initialize the DictView widget.

        Args:
            master: The parent widget
            dictionary: The dictionary to display
            title: The title to show in the title bar
            keyColor: Color for dictionary keys
            keySize: Font size for dictionary keys
            valueColor: Color for dictionary values
            valueSize: Font size for dictionary values
            splitChar: Character/string used to separate keys and values
            lineChar: Character/string used to separate lines
            **kwargs: Additional arguments for TextBar
        """
        # Initialize the TextBar base class
        super().__init__(master, title=title, **kwargs)

        # Set default dictionary if none provided
        self.dictionary = dictionary or {}

        # Configure colors, sizes, and separators
        self.keyColor = keyColor
        self.keySize = keySize
        self.valueColor = valueColor
        self.valueSize = valueSize
        self.splitChar = splitChar
        self.lineChar = lineChar

        # Set up the UI
        self._setupDictView()

    def _setupDictView(self):
        """Set up the DictView UI"""
        # Make text box read-only
        self.setReadOnly(True)

        # Display the dictionary
        self._displayDictionary()

    def _displayDictionary(self):
        """Display the dictionary content with formatted keys and values"""
        # Clear existing text
        self.clearText()

        if self.dictionary:
            for key, value in self.dictionary.items():
                # Display key in configured color and size
                self.append(f"{key}{self.splitChar}", color=self.keyColor,
                            size=self.keySize)
                # Display value in configured color and size
                self.append(f"{value}{self.lineChar}", color=self.valueColor,
                            size=self.valueSize)
        else:
            self.append("Empty dictionary", color="gray", size=self.keySize)

    def setDictionary(self, dictionary):
        """Set a new dictionary to display

        Args:
            dictionary: The new dictionary to display
        """
        self.dictionary = dictionary or {}
        self._displayDictionary()

    def getDictionary(self):
        """Get the currently displayed dictionary

        Returns:
            The currently displayed dictionary
        """
        return self.dictionary

    def setKeyColor(self, color):
        """Set the color for dictionary keys

        Args:
            color: The new color for keys
        """
        self.keyColor = color
        self._displayDictionary()

    def getKeyColor(self):
        """Get the current color for dictionary keys

        Returns:
            The current color for keys
        """
        return self.keyColor

    def setKeySize(self, size):
        """Set the font size for dictionary keys

        Args:
            size: The new font size for keys
        """
        self.keySize = size
        self._displayDictionary()

    def getKeySize(self):
        """Get the current font size for dictionary keys

        Returns:
            The current font size for keys
        """
        return self.keySize

    def setValueColor(self, color):
        """Set the color for dictionary values

        Args:
            color: The new color for values
        """
        self.valueColor = color
        self._displayDictionary()

    def getValueColor(self):
        """Get the current color for dictionary values

        Returns:
            The current color for values
        """
        return self.valueColor

    def setValueSize(self, size):
        """Set the font size for dictionary values

        Args:
            size: The new font size for values
        """
        self.valueSize = size
        self._displayDictionary()

    def getValueSize(self):
        """Get the current font size for dictionary values

        Returns:
            The current font size for values
        """
        return self.valueSize

    def setSplitChar(self, char):
        """Set the character used to separate keys and values

        Args:
            char: The new separator character/string
        """
        self.splitChar = char
        self._displayDictionary()

    def getSplitChar(self):
        """Get the current character used to separate keys and values

        Returns:
            The current separator character/string
        """
        return self.splitChar

    def setLineChar(self, char):
        """Set the character used to separate lines

        Args:
            char: The new line separator character/string
        """
        self.lineChar = char
        self._displayDictionary()

    def getLineChar(self):
        """Get the current character used to separate lines

        Returns:
            The current line separator character/string
        """
        return self.lineChar


def createDictView(master, dictionary=None, title="Dict View", **kwargs):
    """
    Convenience function to create a DictView widget.

    Args:
        master: The parent widget
        dictionary: The dictionary to display
        title: The title to show in the title bar
        **kwargs: Additional arguments for DictView

    Returns:
        A new DictView instance
    """
    return DictView(master, dictionary=dictionary, title=title, **kwargs)
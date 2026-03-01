import customtkinter as ctk
from tomwidgets.tools.TextTwo import TextTwo
from tomwidgets.widget.Theme import Theme


def createTextTwoExample():
    """Create and configure a TextTwo example window."""
    # Create main window
    Theme.init()

    # Create TextTwo instance
    textTwo = TextTwo(title="TextTwo Editor")
    textTwo.pack(fill="both", expand=True, padx=10, pady=10)

    # Set sample text for demonstration
    sampleInputText = """This is the input text area.
You can edit this text freely.

Try the following features:
- Use the search bar to find text
- Use the replace bar to modify text
- Click the switch button (⇄) to swap text between areas
- Click the compare button (≡) to compare input and output
- Use the arrow buttons to move text between areas
- Try the search and replace buttons for both areas

Sample text for search testing:
The quick brown fox jumps over the lazy dog.
Hello world! This is a test sentence.
Search and replace functionality works here.
"""

    sampleOutputText = """This is the output text area.
You can also edit this text.

Features available:
- Dual text editing with synchronized operations
- Search and replace in both text areas
- Text comparison functionality
- Easy text transfer between input and output
- Vertical button bar for quick actions
- Horizontal button bar for search operations

Sample text for comparison:
The quick brown fox jumps over the lazy dog.
Hello universe! This is a different sentence.
Search and replace functionality works perfectly.
"""

    # Set the sample text
    textTwo.setT1Text(sampleInputText)
    textTwo.setT2Text(sampleOutputText)

    # Print instructions
    print("TextTwo Example Started!")
    print("=" * 50)
    print("Available Features:")
    print("1. Search Bar - Enter text to search in input/output")
    print("2. Replace Bar - Enter replacement text")
    print("3. Horizontal Buttons - Search/Replace operations")
    print("4. Vertical Buttons - Text manipulation between areas")
    print("5. Menu Commands - Additional text operations")
    print("=" * 50)

    textTwo.show()


def main():
    """Main function to run the TextTwo example."""
    # Set customtkinter appearance
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    createTextTwoExample()


if __name__ == "__main__":
    main()

import tkinter as tk


class Text(tk.Text):
    def __init__(self, parent, wrap="word", **kwargs):
        super().__init__(parent, wrap=wrap, **kwargs)

    def disable(self):
        self.config(state=tk.DISABLED)

    def enable(self):
        self.config(state=tk.NORMAL)

    def isEnabled(self) -> bool:
        return self['state'] == tk.NORMAL

    def show(self, text: str = "", color: str = 'white'):

        self.append(text, color)

    def append(self, text: str, color: str = 'black', size: int = None):
        """Add text to the TextBox with specified color and font size

        Args:
            text: The text to add
            color: The color for the text (default: 'black')
            size: The font size for the text (default: None, uses default font size)
        """
        # Save current state
        current_state = self['state']

        # Enable if disabled
        if current_state == tk.DISABLED:
            self.config(state=tk.NORMAL)

        # Calculate the range of the inserted text
        if text:
            # Get the position where we'll insert
            # Use "end-1c" to get the position of the last character, then insert after it
            if self.get(1.0, tk.END).strip():  # If there's existing text
                insert_pos = self.index(tk.END + "-1c")
            else:  # If the text widget is empty
                insert_pos = "1.0"

            # Insert the text
            self.insert(insert_pos, text)

            # Calculate the range of the inserted text
            # The text was inserted at insert_pos, so it occupies positions from insert_pos to insert_pos + length of text
            start_pos = insert_pos

            # Calculate end position by moving forward from start_pos by the number of lines and characters
            lines = text.split('\n')
            if len(lines) > 1:
                # Multi-line text
                end_pos = f"{int(insert_pos.split('.')[0]) + len(lines) - 1}.{len(lines[-1])}"
            else:
                # Single-line text
                end_pos = f"{insert_pos.split('.')[0]}.{int(insert_pos.split('.')[1]) + len(text)}"

            # Create a unique tag name for this color and size combination
            if size is not None:
                tag_name = f"color_{color}_size_{size}"
            else:
                tag_name = f"color_{color}"

            # Configure the tag if it doesn't exist
            if tag_name not in self.tag_names():
                if size is not None:
                    # Get current font configuration
                    current_font = self.cget("font")
                    if current_font:
                        # Parse current font and create new font with specified size
                        font_parts = current_font.split()
                        if len(font_parts) >= 2:
                            # Assume format like "Arial 12"
                            font_family = font_parts[0]
                            new_font = f"{font_family} {size}"
                        else:
                            # Fallback to default font family
                            new_font = f"Arial {size}"
                    else:
                        # No current font, create new one
                        new_font = f"Arial {size}"

                    self.tag_configure(
                        tag_name, foreground=color, font=new_font)
                else:
                    self.tag_configure(tag_name, foreground=color)

            # Apply the tag to the inserted text
            self.tag_add(tag_name, start_pos, end_pos)

        # Restore original state
        self.config(state=current_state)

    def insertTo(self, index: str = tk.END, text: str = "", color: str = 'black', size: int = None):
        """Insert text at specified index with color and font size

        Args:
            index: The position to insert text (e.g., "1.0", "2.5", tk.END)
            text: The text to insert
            color: The color for the text (default: 'black')
            size: The font size for the text (default: None, uses default font size)
        """
        # Save current state
        current_state = self['state']

        # Enable if disabled
        if current_state == tk.DISABLED:
            self.config(state=tk.NORMAL)

        # Insert the text at the specified index
        if text:
            # For tk.END insertions, we need to calculate the start position after insertion
            if index == tk.END:
                self.append(text, color, size)
                self.config(state=current_state)
                return
            else:
                # Insert the text using the parent's insert method
                self.insert(index, text)

                # Calculate the range of the inserted text
                lines = text.split('\n')

                # Regular position like "1.0", "2.5"
                start_pos = index
                line_num = int(index.split('.')[0])
                char_num = int(index.split('.')[1])

                if len(lines) > 1:
                    # Multi-line text
                    end_pos = f"{line_num + len(lines) - 1}.{len(lines[-1])}"
                else:
                    # Single-line text
                    end_pos = f"{line_num}.{char_num + len(text)}"

            # Create a unique tag name for this color and size combination
            if size is not None:
                tag_name = f"color_{color}_size_{size}"
            else:
                tag_name = f"color_{color}"

            # Configure the tag if it doesn't exist
            if tag_name not in self.tag_names():
                if size is not None:
                    # Get current font configuration
                    current_font = self.cget("font")
                    if current_font:
                        # Parse current font and create new font with specified size
                        font_parts = current_font.split()
                        if len(font_parts) >= 2:
                            # Assume format like "Arial 12"
                            font_family = font_parts[0]
                            new_font = f"{font_family} {size}"
                        else:
                            # Fallback to default font family
                            new_font = f"Arial {size}"
                    else:
                        # No current font, create new one
                        new_font = f"Arial {size}"

                    self.tag_configure(
                        tag_name, foreground=color, font=new_font)
                else:
                    self.tag_configure(tag_name, foreground=color)

            # Apply the tag to the inserted text
            self.tag_add(tag_name, start_pos, end_pos)

            print(
                f"Inserted text: {text} at {start_pos} to {end_pos} with tag {tag_name}")

        # Restore original state
        self.config(state=current_state)

    def addWidget(self, widget: tk.Widget = None, margin: str = " ", **kwargs):
        state = self['state']
        if not self.isEnabled():
            self.enable()

        self.window_create(tk.END, window=widget, **kwargs)
        self.insert(tk.END, margin)

        self.config(state=state)


def test():
    root = tk.Tk()
    text = Text(root)
    text.pack()
    text.show("hello world")

    text.configure(state="normal")

    for i in range(10):
        widget = tk.Label(root, width=12, text=f"Widget {i}", bd=1, relief="raised",
                          bg="#5C9BD5", foreground="white", padx=4, pady=4)
        text.window_create("insert", window=widget, padx=10, pady=10)

    test2(text)

    text.configure(state="disabled")

    root.mainloop()


def test2(text_box: Text):

    # Add text with different colors using original method
    text_box.append("Original addText method:\n", "black")
    text_box.append("Hello ", "black")
    text_box.append("World!", "red")
    text_box.append("\nThis is ", "black")
    text_box.append("blue ", "blue")
    text_box.append("text.\n\n", "black")

    # Add text with different colors and sizes using addText method
    text_box.append("addText method with size:\n", "black", 14)
    text_box.append("Large red text ", "red", 18)
    text_box.append("with normal black ", "black", 12)
    text_box.append("and small blue text", "blue", 10)
    text_box.append("\n\nMixed sizes: ", "black", 12)
    text_box.append("12pt ", "green", 12)
    text_box.append("16pt ", "red", 16)
    text_box.append("20pt ", "blue", 20)
    text_box.append("24pt text\n\n", size=24)

    # Test the new insert method
    text_box.append("New insert method tests:\n", "black", 16)

    # Insert at beginning of line 1
    text_box.insertTo("1.0", "[START] ", "purple", 14)

    # Insert in the middle of existing text (after "Hello ")
    text_box.insertTo("1.13", "[MIDDLE] ", "orange", 16)

    # Insert at specific positions with different colors and sizes
    text_box.insertTo("3.5", "[INSERTED] ", "brown", 12)
    text_box.insertTo("5.10", "[BIG] ", "darkblue", 20)
    text_box.insertTo("7.0", "[SMALL] ", "darkgreen", 10)

    # Insert at the end
    text_box.insertTo(tk.END, "\n[END] Inserted red at the end", "red", 24)

    text = "[END]Inserted purple at the end"
    text_box.insertTo(tk.END, text, size=33, color="purple")

    text_box.insertTo(tk.END, text)


if __name__ == '__main__':
    test()

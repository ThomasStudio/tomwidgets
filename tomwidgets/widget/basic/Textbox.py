import tkinter as tk
import customtkinter as ctk

from .BaseWidget import BaseWidget


class Textbox(ctk.CTkTextbox, BaseWidget):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        BaseWidget.__init__(self)

    def box(self):
        return self._textbox

    def state(self, state=None) -> str:
        box = self.box()
        if state is None:
            return box['state']
        else:
            box['state'] = state
            return box['state']

    def disable(self):
        self.state(tk.DISABLED)

    def enable(self):
        self.state(tk.NORMAL)

    def isEnabled(self) -> bool:
        return self.state() == tk.NORMAL

    def append(self, text: str, color: str = None, size: int = None):
        """Add text to the TextBox with specified color and font size

        Args:
            text: The text to add
            color: The color for the text (default: 'black')
            size: The font size for the text (default: None, uses default font size)
        """
        box = self.box()
        color = self.textColor(color)

        # Save current state
        current_state = box['state']

        # Enable if disabled
        if current_state == tk.DISABLED:
            self.configure(state=tk.NORMAL)

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
                    current_font = box.cget("font")
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

                    box.tag_configure(
                        tag_name, foreground=color, font=new_font)
                else:
                    box.tag_configure(tag_name, foreground=color)

            # Apply the tag to the inserted text
            self.tag_add(tag_name, start_pos, end_pos)

        # Restore original state
        self.configure(state=current_state)

    def insertTo(self, index: str = tk.END, text: str = "", color: str = None, size: int = None):
        """Insert text at specified index with color and font size

        Args:
            index: The position to insert text (e.g., "1.0", "2.5", tk.END)
            text: The text to insert
            color: The color for the text (default: 'black')
            size: The font size for the text (default: None, uses default font size)
        """
        # Save current state
        current_state = self.state()
        box = self.box()
        color = self.textColor(color)

        # Enable if disabled
        if current_state == tk.DISABLED:
            self.configure(state=tk.NORMAL)

        # Insert the text at the specified index
        if text:
            # For tk.END insertions, we need to calculate the start position after insertion
            if index == tk.END:
                self.append(text, color, size)
                self.configure(state=current_state)
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
                    current_font = box.cget("font")
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

                    box.tag_configure(
                        tag_name, foreground=color, font=new_font)
                else:
                    box.tag_configure(tag_name, foreground=color)

            # Apply the tag to the inserted text
            self.tag_add(tag_name, start_pos, end_pos)

            print(
                f"Inserted text: {text} at {start_pos} to {end_pos} with tag {tag_name}")

        # Restore original state
        self.configure(state=current_state)

    def addWidget(self, widget: tk.Widget = None, margin: str = " ", **kwargs):
        state = self.state()
        box = self.box()

        if not self.isEnabled():
            self.enable()

        box.window_create(tk.END, window=widget, **kwargs)
        self.insert(tk.END, margin)

        self.configure(state=state)

    def textColor(self, color: str = None) -> str:
        if color:
            return color

        theme = ctk.get_appearance_mode()

        return 'black' if theme == 'Light' else 'white'

    def clear(self):
        self.delete('1.0', tk.END)

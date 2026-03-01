import customtkinter as ctk
from tomwidgets.widget import WrapBtnBar, WrapBtnConfig, BtnBar, BtnConfig
from tomwidgets.widget.basic.Tk import Tk
from tomwidgets.widget.basic.Label import Label
from tomwidgets.widget.basic.Entry import Entry


class WrapBtnBarExample:
    """Example demonstrating WrapBtnBar functionality"""

    def __init__(self, root):
        """Initialize the example"""
        self.root = root
        self.root.title("WrapBtnBar Example")
        self.root.geometry("600x400")

        self._setup_ui()

    def _setup_ui(self):
        """Set up the user interface"""
        # Create main frame
        main_frame = ctk.CTkFrame(self.root)
        main_frame.pack(fill="both", expand=True)

        # Title
        title_label = Label(main_frame, text="WrapBtnBar Example",
                            font=("Arial", 18, "bold"))
        title_label.pack(pady=10)

        # Description
        desc_label = Label(main_frame,
                           text="Resize the window to see buttons automatically wrap to new lines.")
        desc_label.pack(pady=5)

        # Control panel
        control_frame = ctk.CTkFrame(main_frame)
        control_frame.pack(side="top", fill="x", padx=10, pady=5)

        # Width control
        Label(control_frame, text="Container Width:").pack(side="left", padx=5)
        self.width_var = ctk.StringVar(self.root, value="400")
        width_entry = Entry(
            control_frame, textvariable=self.width_var, width=100)
        width_entry.pack(side="left", padx=5)

        update_width_btn = ctk.CTkButton(control_frame, text="Update Width",
                                         command=self._update_width)
        update_width_btn.pack(side="left", padx=5)

        # Create WrapBtnBar with different button groups
        self.wrap_btn_bar = WrapBtnBar(main_frame,
                                       buttonStyle={"corner_radius": 8},
                                       padx=3,
                                       pady=5,
                                       height=80,
                                       width=200)
        self.wrap_btn_bar.pack(fill='y', expand=True, padx=10, pady=10)
        # self.wrap_btn_bar.pack(fill="both", expand=True, padx=10, pady=10)

        # Add buttons with different groups
        self._add_sample_buttons()

        # Action buttons frame
        action_frame = ctk.CTkFrame(main_frame)
        action_frame.pack(fill="x", padx=10, pady=5)

        btnBar = BtnBar(action_frame)
        btnBar.pack(fill="x")
        btnBar.addBtns([
            BtnConfig("Add", self._add_random_button),
            BtnConfig("Remove", self._remove_button),
            BtnConfig("Disable Group", self._disable_group),
            BtnConfig("Enable Group", self._enable_group),
            BtnConfig("Clear", self._clear_buttons),
        ])

    def _add_sample_buttons(self):
        """Add sample buttons to demonstrate functionality"""
        # File operations group
        file_buttons = [
            WrapBtnConfig("New", self._on_new, group="file",
                          style={"fg_color": "#4CAF50"}),
            WrapBtnConfig("Open", self._on_open, group="file",
                          style={"fg_color": "#2196F3"}),
            WrapBtnConfig("Save", self._on_save, group="file",
                          style={"fg_color": "#FF9800"}),
            WrapBtnConfig("Save As", self._on_save_as, group="file",
                          style={"fg_color": "#FF5722"}),
        ]
        self.wrap_btn_bar.addBtns(file_buttons)

        # Edit operations group
        edit_buttons = [
            WrapBtnConfig("Cut", self._on_cut, group="edit",
                          style={"fg_color": "#9C27B0"}),
            WrapBtnConfig("Copy", self._on_copy, group="edit",
                          style={"fg_color": "#673AB7"}),
            WrapBtnConfig("Paste", self._on_paste, group="edit",
                          style={"fg_color": "#3F51B5"}),
            WrapBtnConfig("Undo", self._on_undo, group="edit",
                          style={"fg_color": "#607D8B"}),
            WrapBtnConfig("Redo", self._on_redo, group="edit",
                          style={"fg_color": "#795548"}),
        ]
        self.wrap_btn_bar.addBtns(edit_buttons)

        # View operations group
        view_buttons = [
            WrapBtnConfig("Zoom In", self._on_zoom_in, group="view",
                          style={"fg_color": "#4CAF50"}),
            WrapBtnConfig("Zoom Out", self._on_zoom_out, group="view",
                          style={"fg_color": "#2196F3"}),
            WrapBtnConfig("Reset Zoom", self._on_reset_zoom, group="view",
                          style={"fg_color": "#FF9800"}),
            WrapBtnConfig("Full Screen", self._on_full_screen, group="view",
                          style={"fg_color": "#FF5722"}),
        ]
        self.wrap_btn_bar.addBtns(view_buttons)

        # Tools group
        tools_buttons = [
            WrapBtnConfig("Find", self._on_find, group="tools",
                          style={"fg_color": "#9C27B0"}),
            WrapBtnConfig("Replace", self._on_replace, group="tools",
                          style={"fg_color": "#673AB7"}),
            WrapBtnConfig("Settings", self._on_settings, group="tools",
                          style={"fg_color": "#3F51B5"}),
            WrapBtnConfig("Help", self._on_help, group="tools",
                          style={"fg_color": "#607D8B"}),
        ]
        self.wrap_btn_bar.addBtns(tools_buttons)

    def _update_width(self):
        """Update the container width"""
        try:
            width = int(self.width_var.get())
            self.wrap_btn_bar.configure(width=width)
        except ValueError:
            pass

    def _add_random_button(self):
        """Add a random button"""
        import random

        operations = ["Print", "Export", "Import",
                      "Share", "Upload", "Download"]
        colors = ["#4CAF50", "#2196F3", "#FF9800",
                  "#FF5722", "#9C27B0", "#673AB7"]

        name = random.choice(operations)
        color = random.choice(colors)

        config = WrapBtnConfig(
            name=f"{name}_{random.randint(1, 100)}",
            callback=lambda n=name: self._on_generic(n),
            group="random",
            style={"fg_color": color}
        )

        self.wrap_btn_bar.addBtn(config)

    def _remove_button(self):
        """Remove the last button"""
        all_btns = self.wrap_btn_bar.getAllBtns()
        if all_btns:
            last_btn_name = all_btns[-1]['data'].name
            self.wrap_btn_bar.removeBtn(last_btn_name)

    def _disable_group(self):
        """Disable the 'file' group"""
        self.wrap_btn_bar.disableGroup("file")

    def _enable_group(self):
        """Enable the 'file' group"""
        self.wrap_btn_bar.enableGroup("file")

    def _clear_buttons(self):
        """Clear all buttons"""
        self.wrap_btn_bar.clearBtns()

    def _refresh_layout(self):
        """Refresh the layout"""
        # Note: WrapBox handles layout automatically
        print("Layout refreshed - WrapBox handles automatic wrapping")

    # Button callback methods
    def _on_new(self):
        print("New file action triggered")

    def _on_open(self):
        print("Open file action triggered")

    def _on_save(self):
        print("Save file action triggered")

    def _on_save_as(self):
        print("Save as action triggered")

    def _on_cut(self):
        print("Cut action triggered")

    def _on_copy(self):
        print("Copy action triggered")

    def _on_paste(self):
        print("Paste action triggered")

    def _on_undo(self):
        print("Undo action triggered")

    def _on_redo(self):
        print("Redo action triggered")

    def _on_zoom_in(self):
        print("Zoom in action triggered")

    def _on_zoom_out(self):
        print("Zoom out action triggered")

    def _on_reset_zoom(self):
        print("Reset zoom action triggered")

    def _on_full_screen(self):
        print("Full screen action triggered")

    def _on_find(self):
        print("Find action triggered")

    def _on_replace(self):
        print("Replace action triggered")

    def _on_settings(self):
        print("Settings action triggered")

    def _on_help(self):
        print("Help action triggered")

    def _on_generic(self, operation):
        print(f"{operation} action triggered")


def main():
    """Main function to run the example"""
    root = Tk()
    app = WrapBtnBarExample(root)
    root.mainloop()


if __name__ == "__main__":
    main()

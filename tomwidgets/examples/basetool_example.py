import customtkinter as ctk
from tomwidgets.widget.BaseWin import BaseWin
from tomwidgets.widget.basic.Label import Label
from tomwidgets.widget.basic.Button import Button
from tomwidgets.widget.basic.Tk import Tk


class MyBaseTool(BaseWin):
    """Custom BaseTool example with enhanced functionality"""

    def __init__(self, master=None, title="BaseTool Example", asWin=True):
        """Initialize the custom BaseTool"""
        # Create the tool with custom title and both bars visible
        super().__init__(master=master, title=title,
                         showTitleBar=True, showFolderBar=True, asWin=asWin)

        # Set up the content
        self._setup_content()

    def getCmds(self):
        """Override to provide custom menu commands"""
        # Get the default commands from the parent
        menu = super().getCmds()

        # Add custom commands to the Window menu
        for i, (menu_name, menu_items) in enumerate(menu):
            if menu_name == "Window":
                # Add custom commands to the Window menu
                menu_items.insert(0, ("Toggle TitleBar", self.toggleTitleBar))
                menu_items.insert(
                    1, ("Change Tool Title", self._change_tool_title))
                break

        return menu

    def _setup_content(self):
        """Set up the content for the tool"""
        content_frame = self.mainFrame()

        # Add a title label
        title_label = Label(content_frame, text="BaseTool Enhanced Example",
                            font=("Arial", 20, "bold"))
        title_label.pack(pady=30)

        # Add a description
        desc_label = Label(content_frame,
                           text="This example shows how to use BaseTool with customizations\n"
                                "including TitleBar, FolderBar, and window management features.",
                           font=("Arial", 12))
        desc_label.pack(pady=10)

        # Add mode indicator
        mode_label = Label(content_frame,
                           text=f"Mode: {'WINDOW' if self.asWin else 'FRAME'}",
                           font=("Arial", 14, "bold"),
                           text_color="green" if self.asWin else "blue")
        mode_label.pack(pady=5)

        # Add buttons to demonstrate functionality
        button_frame = ctk.CTkFrame(content_frame)
        button_frame.pack(pady=30)

        # Toggle TitleBar button
        toggle_btn = Button(button_frame, text="Toggle TitleBar",
                            command=self.toggleTitleBar)
        toggle_btn.pack(side="left", padx=10)

        # Change title button
        change_title_btn = Button(button_frame, text="Change Title",
                                  command=self._change_tool_title)
        change_title_btn.pack(side="left", padx=10)

        # Toggle FolderBar button
        folderbar_btn = Button(button_frame, text="Toggle FolderBar",
                               command=self.toggleFolderBar)
        folderbar_btn.pack(side="left", padx=10)

        # Window management buttons (only in window mode)
        if self.asWin:
            # Maximize button
            maximize_btn = Button(button_frame, text="Maximize",
                                  command=self.toggleMaximize)
            maximize_btn.pack(side="left", padx=10)

            # Always on Top button
            on_top_btn = Button(button_frame, text="Toggle Always on Top",
                                command=self.toggleOnTop)
            on_top_btn.pack(side="left", padx=10)

            # Minimize button
            minimize_btn = Button(button_frame, text="Minimize",
                                  command=self.toggleMinimize)
            minimize_btn.pack(side="left", padx=10)

        # Add status indicators
        self._add_status_indicators(content_frame)

    def _add_status_indicators(self, parent):
        """Add status indicators for tool features"""
        status_frame = ctk.CTkFrame(parent)
        status_frame.pack(pady=20)

        # TitleBar status
        titlebar_status = Label(status_frame,
                                text="TitleBar: VISIBLE",
                                font=("Arial", 10, "bold"))
        titlebar_status.pack(side="left", padx=15)
        self.titlebar_status = titlebar_status

        # FolderBar status
        folderbar_status = Label(status_frame,
                                 text="FolderBar: VISIBLE",
                                 font=("Arial", 10, "bold"))
        folderbar_status.pack(side="left", padx=15)
        self.folderbar_status = folderbar_status

        # Window mode specific status indicators
        if self.asWin:
            # Maximized status
            maximized_status = Label(status_frame,
                                     text="Maximized: NO",
                                     font=("Arial", 10, "bold"))
            maximized_status.pack(side="left", padx=15)
            self.maximized_status = maximized_status

            # Always on Top status
            on_top_status = Label(status_frame,
                                  text="Always on Top: NO",
                                  font=("Arial", 10, "bold"))
            on_top_status.pack(side="left", padx=15)
            self.on_top_status = on_top_status

    def _change_tool_title(self):
        """Change the tool title"""
        current_title = self.getTitle()
        if "Updated" in current_title:
            new_title = "BaseTool Example"
        else:
            new_title = "BaseTool Example - Updated"
        self.setTitle(new_title)

        # Also update the window manager title if in window mode
        if self.asWin:
            self.win.title(new_title)

    def toggleTitleBar(self):
        """Override toggleTitleBar to update status indicator"""
        super().toggleTitleBar()
        self._update_titlebar_status()

    def toggleFolderBar(self):
        """Override toggleFolderBar to update status indicator"""
        super().toggleFolderBar()
        self._update_folderbar_status()

    def toggleMaximize(self):
        """Override toggleMaximize to update status indicator"""
        super().toggleMaximize()
        self._update_maximized_status()

    def toggleOnTop(self):
        """Override toggleOnTop to update status indicator"""
        super().toggleOnTop()
        self._update_on_top_status()

    def toggleMinimize(self):
        """Override toggleMinimize to update status indicator"""
        super().toggleMinimize()

    def _update_titlebar_status(self):
        """Update TitleBar status indicator"""
        status = "VISIBLE" if self.titleBarVisible else "HIDDEN"
        self.titlebar_status.configure(text=f"TitleBar: {status}")

    def _update_folderbar_status(self):
        """Update FolderBar status indicator"""
        status = "VISIBLE" if self.folderBarVisible else "HIDDEN"
        self.folderbar_status.configure(text=f"FolderBar: {status}")

    def _update_maximized_status(self):
        """Update maximized status indicator"""
        status = "YES" if self.isMaximized else "NO"
        self.maximized_status.configure(text=f"Maximized: {status}")

    def _update_on_top_status(self):
        """Update always on top status indicator"""
        status = "YES" if self.isOnTop else "NO"
        self.on_top_status.configure(text=f"Always on Top: {status}")


class EmbeddedBaseToolExample:
    """Example showing BaseTool used as an embedded frame"""

    def __init__(self):
        """Initialize the embedded example"""
        # Create the main window
        self.root = Tk()
        self.root.title("BaseTool Frame Mode Test")
        self.root.geometry("800x600")

        # Add main title
        main_title = Label(self.root, text="BaseTool Frame Mode Testing",
                           font=("Arial", 16, "bold"))
        main_title.pack(pady=10)

        # Add description
        desc = Label(self.root,
                     text="This demonstrates BaseTool used as a frame (asWin=False)\n"
                     "The embedded BaseTool has full functionality but runs as a frame component.",
                     font=("Arial", 10))
        desc.pack(pady=5)

        # Create the embedded BaseTool
        self.embedded_basetool = MyBaseTool(master=self.root,
                                            title="Embedded BaseTool",
                                            asWin=False)

        # Pack the embedded BaseTool to fill most of the window
        self.embedded_basetool.pack(fill="both", expand=True, padx=20, pady=15)

        # Add external controls
        self._add_external_controls()

    def _add_external_controls(self):
        """Add controls that operate on the embedded BaseTool from outside"""
        control_frame = ctk.CTkFrame(self.root)
        control_frame.pack(fill="x", padx=20, pady=10)

        # External TitleBar control
        ext_titlebar_btn = Button(control_frame, text="External: Toggle TitleBar",
                                  command=self.embedded_basetool.toggleTitleBar)
        ext_titlebar_btn.pack(side="left", padx=5)

        # External FolderBar control
        ext_folderbar_btn = Button(control_frame, text="External: Toggle FolderBar",
                                   command=self.embedded_basetool.toggleFolderBar)
        ext_folderbar_btn.pack(side="left", padx=5)

        # Test window mode comparison
        compare_btn = Button(control_frame, text="Compare with Window Mode",
                             command=self._compare_with_window_mode)
        compare_btn.pack(side="left", padx=5)

    def _compare_with_window_mode(self):
        """Open a window mode BaseTool for comparison"""
        compare_tool = MyBaseTool(title="Window Mode BaseTool", asWin=True)
        compare_tool.show()

    def show(self):
        """Show the test window"""
        self.root.mainloop()


def main():
    """Main function to run the BaseTool example"""
    print("=" * 60)
    print("BaseTool Example")
    print("=" * 60)
    print("\nThis example demonstrates BaseTool functionality in both modes:")
    print("1. Window Mode (asWin=True) - Standalone window")
    print("2. Frame Mode (asWin=False) - Embedded frame")

    print("\nKey Features Being Demonstrated:")
    print("✓ TitleBar with custom menu commands")
    print("✓ FolderBar functionality")
    print("✓ Window management (maximize, minimize, always on top)")
    print("✓ Settings management")
    print("✓ Mode switching (Window vs Frame)")
    print("✓ Status indicators")
    print("✓ Interactive controls")

    print("\nChoose mode:")
    print("1. Window Mode (Standalone window)")
    print("2. Frame Mode (Embedded in parent window)")
    print("3. Both modes for comparison")

    try:
        choice = input("\nEnter your choice (1, 2, or 3): ").strip()

        if choice == "1":
            print("\nStarting Window Mode...")
            tool = MyBaseTool(title="BaseTool Window Mode", asWin=True)
            tool.show()
        elif choice == "2":
            print("\nStarting Frame Mode...")
            embedded_example = EmbeddedBaseToolExample()
            embedded_example.show()
        elif choice == "3":
            print("\nStarting both modes for comparison...")
            # Start window mode
            window_tool = MyBaseTool(title="Window Mode BaseTool", asWin=True)
            # Start frame mode
            embedded_example = EmbeddedBaseToolExample()
            embedded_example.show()
        else:
            print("Invalid choice. Starting Window Mode by default.")
            tool = MyBaseTool(title="BaseTool Window Mode", asWin=True)
            tool.show()

    except KeyboardInterrupt:
        print("\n\nExample terminated by user.")
    except Exception as e:
        print(f"\nError: {e}")
        print("Starting Window Mode as fallback...")
        tool = MyBaseTool(title="BaseTool Window Mode", asWin=True)
        tool.show()


if __name__ == "__main__":
    main()

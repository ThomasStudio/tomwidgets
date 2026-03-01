import sys
import os

# Add the project root directory to the path to import tomwidgets
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, project_root)

from tomwidgets.widget import Stapling, PopMenu
from tomwidgets.widget.basic import Tk, Toplevel, Label, Button, Frame

def create_main_window():
    """Create the main demonstration window."""
    
    # Create main window
    root = Tk()
    root.title("Stapling Widget Example")
    root.geometry("400x300")
    
    # Create frame for content
    main_frame = Frame(root)
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)
    
    # Title label
    title_label = Label(main_frame, text="Stapling Widget Demo", font=("Arial", 16, "bold"))
    title_label.pack(pady=10)
    
    # Instructions
    instructions = Label(main_frame, text="Right-click anywhere in this window to see the stapling menu\n"
                                          "Select a corner symbol to position this window", 
                        font=("Arial", 10))
    instructions.pack(pady=10)
    
    # Corner symbols display
    corner_frame = Frame(main_frame)
    corner_frame.pack(pady=20)
    
    corners = [
        ("◤", "Top Left"),
        ("◥", "Top Right"),
        ("◣", "Bottom Left"),
        ("◢", "Bottom Right")
    ]
    
    for symbol, description in corners:
        corner_label = Label(corner_frame, text=f"{symbol} = {description}", font=("Arial", 12))
        corner_label.pack(anchor="w")
    
    # Create stapling instance
    stapling = Stapling(root)
    
    # Create popup menu with stapling options
    menu_data = stapling.getStaplingMenu()
    popup_menu = PopMenu(root, menu_data)
    
    def show_stapling_menu(event):
        """Show the stapling menu on right-click."""
        popup_menu.show()
    
    # Bind right-click to show menu
    root.bind("<Button-3>", show_stapling_menu)
    
    # Create button to demonstrate re-stapling
    def re_stapling():
        """Re-apply the last stapling position."""
        stapling.reStapling()
    
    re_stapling_btn = Button(main_frame, text="Re-apply Last Position", 
                            command=re_stapling)
    re_stapling_btn.pack(pady=10)
    
    # Status label
    status_label = Label(main_frame, text="Ready for stapling...", font=("Arial", 9))
    status_label.pack(pady=5)
    
    def update_status(symbol):
        """Update status label with current position."""
        status_label.config(text=f"Window positioned to: {symbol}")
    
    # Override the stapling method to update status
    original_stapling = stapling.stapling
    
    def stapling_with_status(xPos, yPos):
        original_stapling(xPos, yPos)
        # Determine which symbol was used based on position
        if xPos == '+0' and yPos == '+0':
            update_status("◤ Top Left")
        elif xPos == '-0' and yPos == '+0':
            update_status("◥ Top Right")
        elif xPos == '+0' and yPos == '-0':
            update_status("◣ Bottom Left")
        elif xPos == '-0' and yPos == '-0':
            update_status("◢ Bottom Right")
    
    stapling.stapling = stapling_with_status
    
    return root

def create_multiple_windows_demo():
    """Create a demo with multiple windows showing different stapling positions."""
    
    def create_stapled_window(title, xPos, yPos, bg_color):
        """Create a window and staple it to a specific position."""
        
        window = Toplevel()
        window.title(title)
        window.geometry("200x150")
        window.configure(bg=bg_color)
        
        # Create stapling instance
        stapling = Stapling(window)
        
        # Position the window
        window.update()  # Ensure window is rendered before stapling
        stapling.stapling(xPos, yPos)
        
        # Add content
        label = Label(window, text=title, bg=bg_color, font=("Arial", 12, "bold"))
        label.pack(pady=20)
        
        position_label = Label(window, text=f"Position: {xPos}, {yPos}", 
                              bg=bg_color, font=("Arial", 9))
        position_label.pack()
        
        return window
    
    # Create windows at different corners
    windows = [
        ("Top Left Window", "+0", "+0", "lightblue"),
        ("Top Right Window", "-0", "+0", "lightgreen"),
        ("Bottom Left Window", "+0", "-0", "lightyellow"),
        ("Bottom Right Window", "-0", "-0", "lightcoral")
    ]
    
    for title, xPos, yPos, color in windows:
        create_stapled_window(title, xPos, yPos, color)

def advanced_stapling_demo():
    """Advanced demo showing custom stapling positions."""
    
    def create_custom_window():
        """Create a window with custom stapling options."""
        
        window = Toplevel()
        window.title("Custom Stapling Demo")
        window.geometry("300x200")
        
        stapling = Stapling(window)
        
        # Custom positions frame
        frame = Frame(window)
        frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        Label(frame, text="Custom Stapling Positions", font=("Arial", 14, "bold")).pack(pady=10)
        
        # Custom position buttons
        positions = [
            ("Center Screen", "m", "m"),
            ("Left Center", "l", "m"),
            ("Right Center", "r", "m"),
            ("Top Center", "m", "t"),
            ("Bottom Center", "m", "b")
        ]
        
        for label, xPos, yPos in positions:
            Button(frame, text=label, 
                  command=lambda x=xPos, y=yPos: stapling.stapling(x, y)).pack(pady=5)
        
        # Initial position
        window.update()
        stapling.stapling("m", "m")  # Center initially
        
        return window
    
    return create_custom_window()

def main():
    """Main function to run the stapling example."""
    
    print("Starting Stapling Widget Example...")
    
    # Create main window
    root = create_main_window()
    
    # Add menu for additional demos
    def show_multiple_windows():
        create_multiple_windows_demo()
    
    def show_advanced_demo():
        advanced_stapling_demo()
    
    # Add demo buttons to main window
    demo_frame = Frame(root)
    demo_frame.pack(pady=20)
    
    Button(demo_frame, text="Show Multiple Windows Demo", 
          command=show_multiple_windows).pack(pady=5)
    
    Button(demo_frame, text="Show Advanced Stapling Demo", 
          command=show_advanced_demo).pack(pady=5)
    
    # Instructions footer
    footer = Label(root, text="Tip: Try resizing the window and re-stapling to see how it adapts", 
                  font=("Arial", 8), fg_color="gray")
    footer.pack(side="bottom", pady=10)
    
    print("Stapling example is ready!")
    print("- Right-click to see stapling menu")
    print("- Use buttons for additional demos")
    
    # Start the main loop
    root.mainloop()

if __name__ == "__main__":
    main()
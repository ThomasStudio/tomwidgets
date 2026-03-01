import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import customtkinter as ctk
from tomwidgets.widget.basic.Frame import Frame


class FrameExample(ctk.CTk):
    """Main application class for Frame example."""

    def __init__(self):
        """Initialize the application."""
        super().__init__()

        self.title("Frame Widget Example - tomwidgets")
        self.geometry("800x700")
        self.minsize(700, 600)

        # Configure grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)  # Title
        self.grid_rowconfigure(1, weight=0)  # Description
        self.grid_rowconfigure(2, weight=0)  # Control panel
        self.grid_rowconfigure(3, weight=1)  # Demo area

        self.demoFrames = {}  # Store references to demo frames
        self.setupUi()

    def setupUi(self):
        """Setup the user interface."""
        # Title label
        titleLabel = ctk.CTkLabel(self, text="Frame Widget Example",
                                  font=ctk.CTkFont(size=22, weight="bold"))
        titleLabel.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="ew")

        # Description label
        descLabel = ctk.CTkLabel(self, 
                                text="Enhanced frame container with event handling, dragging, and dynamic visibility control",
                                font=ctk.CTkFont(size=12))
        descLabel.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="ew")

        # Control panel
        self.setupControlPanel()

        # Demo area
        self.setupDemoArea()

    def setupControlPanel(self):
        """Setup the control panel with demo selection buttons."""
        controlFrame = ctk.CTkFrame(self)
        controlFrame.grid(row=2, column=0, padx=20, pady=10, sticky="ew")
        controlFrame.grid_columnconfigure(0, weight=1)

        # Create control buttons
        self.createControlButtons(controlFrame)

    def createControlButtons(self, parent):
        """Create buttons for different Frame demonstrations."""
        # Configure button frame grid
        for i in range(4):
            parent.grid_columnconfigure(i, weight=1)

        # Row 1: Basic layout demonstrations
        packButton = ctk.CTkButton(parent, text="Pack Layout",
                                  command=self.showPackLayout)
        packButton.grid(row=0, column=0, padx=10, pady=10)

        gridButton = ctk.CTkButton(parent, text="Grid Layout",
                                  command=self.showGridLayout)
        gridButton.grid(row=0, column=1, padx=10, pady=10)

        placeButton = ctk.CTkButton(parent, text="Place Layout",
                                   command=self.showPlaceLayout)
        placeButton.grid(row=0, column=2, padx=10, pady=10)

        nestedButton = ctk.CTkButton(parent, text="Nested Frames",
                                    command=self.showNestedFrames)
        nestedButton.grid(row=0, column=3, padx=10, pady=10)

        # Row 2: Advanced features
        eventButton = ctk.CTkButton(parent, text="Event Handling",
                                   command=self.showEventHandling)
        eventButton.grid(row=1, column=0, padx=10, pady=10)

        dragButton = ctk.CTkButton(parent, text="Dragging Frames",
                                  command=self.showDraggingFrames)
        dragButton.grid(row=1, column=1, padx=10, pady=10)

        visibilityButton = ctk.CTkButton(parent, text="Show/Hide",
                                        command=self.showVisibilityControl)
        visibilityButton.grid(row=1, column=2, padx=10, pady=10)

        styledButton = ctk.CTkButton(parent, text="Styled Frames",
                                    command=self.showStyledFrames)
        styledButton.grid(row=1, column=3, padx=10, pady=10)

        # Row 3: Utility functions
        clearButton = ctk.CTkButton(parent, text="Clear Demo Area",
                                   command=self.clearDemoArea,
                                   fg_color="#d9534f", hover_color="#c9302c")
        clearButton.grid(row=2, column=0, padx=10, pady=10)

        resetButton = ctk.CTkButton(parent, text="Reset All",
                                   command=self.resetAll,
                                   fg_color="#5bc0de", hover_color="#46b8da")
        resetButton.grid(row=2, column=1, padx=10, pady=10)

        infoButton = ctk.CTkButton(parent, text="Frame Info",
                                  command=self.showFrameInfo)
        infoButton.grid(row=2, column=2, padx=10, pady=10)

        allButton = ctk.CTkButton(parent, text="All Features",
                                 command=self.showAllFeatures)
        allButton.grid(row=2, column=3, padx=10, pady=10)

    def setupDemoArea(self):
        """Setup the demo area where frames will be displayed."""
        self.demoArea = ctk.CTkFrame(self, fg_color="transparent")
        self.demoArea.grid(row=3, column=0, padx=20, pady=20, sticky="nsew")
        
        # Configure demo area grid
        self.demoArea.grid_columnconfigure(0, weight=1)
        self.demoArea.grid_rowconfigure(0, weight=1)

        # Status label
        self.statusLabel = ctk.CTkLabel(self.demoArea, text="Select a demo to begin...",
                                       font=ctk.CTkFont(weight="bold"))
        self.statusLabel.grid(row=0, column=0, padx=10, pady=10)

    def updateStatus(self, message):
        """Update the status label."""
        self.statusLabel.configure(text=message)

    def clearDemoArea(self):
        """Clear all frames from the demo area."""
        for frame_id, frame_info in self.demoFrames.items():
            frame = frame_info['frame']
            if frame.winfo_ismapped():
                frame.hide()
        
        self.demoFrames.clear()
        self.updateStatus("Demo area cleared")

    def resetAll(self):
        """Reset the demo area to initial state."""
        self.clearDemoArea()
        self.updateStatus("Select a demo to begin...")

    # Frame demonstration methods
    def showPackLayout(self):
        """Demonstrate Frame with pack layout manager."""
        self.clearDemoArea()
        self.updateStatus("Pack Layout Demo - Frames arranged using pack()")

        # Create main container frame
        container = Frame(self.demoArea, fg_color="#2b2b2b", corner_radius=10)
        container.pack(padx=10, pady=10, fill="both", expand=True)
        self.demoFrames['pack_container'] = {'frame': container, 'type': 'container'}

        # Create multiple frames with pack layout
        frame1 = Frame(container, fg_color="#3a3a3a", corner_radius=8, height=80)
        frame1.pack(padx=10, pady=10, fill="x")
        
        label1 = ctk.CTkLabel(frame1, text="Frame 1 - Packed top", 
                             font=ctk.CTkFont(weight="bold"))
        label1.pack(padx=10, pady=10)
        self.demoFrames['pack_frame1'] = {'frame': frame1, 'type': 'demo'}

        frame2 = Frame(container, fg_color="#4a4a4a", corner_radius=8, height=80)
        frame2.pack(padx=10, pady=10, fill="x")
        
        label2 = ctk.CTkLabel(frame2, text="Frame 2 - Packed below frame 1", 
                             font=ctk.CTkFont(weight="bold"))
        label2.pack(padx=10, pady=10)
        self.demoFrames['pack_frame2'] = {'frame': frame2, 'type': 'demo'}

        frame3 = Frame(container, fg_color="#5a5a5a", corner_radius=8, height=80)
        frame3.pack(padx=10, pady=10, fill="x", side="bottom")
        
        label3 = ctk.CTkLabel(frame3, text="Frame 3 - Packed at bottom", 
                             font=ctk.CTkFont(weight="bold"))
        label3.pack(padx=10, pady=10)
        self.demoFrames['pack_frame3'] = {'frame': frame3, 'type': 'demo'}

    def showGridLayout(self):
        """Demonstrate Frame with grid layout manager."""
        self.clearDemoArea()
        self.updateStatus("Grid Layout Demo - Frames arranged using grid()")

        # Create main container frame
        container = Frame(self.demoArea, fg_color="#2b2b2b", corner_radius=10)
        container.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        
        # Configure container grid
        container.grid_columnconfigure(0, weight=1)
        container.grid_columnconfigure(1, weight=1)
        container.grid_rowconfigure(0, weight=1)
        container.grid_rowconfigure(1, weight=1)
        self.demoFrames['grid_container'] = {'frame': container, 'type': 'container'}

        # Create frames in grid layout
        frame1 = Frame(container, fg_color="#3a3a3a", corner_radius=8)
        frame1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        
        label1 = ctk.CTkLabel(frame1, text="Frame 1\nRow 0, Column 0", 
                             font=ctk.CTkFont(weight="bold"))
        label1.pack(expand=True)
        self.demoFrames['grid_frame1'] = {'frame': frame1, 'type': 'demo'}

        frame2 = Frame(container, fg_color="#4a4a4a", corner_radius=8)
        frame2.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        
        label2 = ctk.CTkLabel(frame2, text="Frame 2\nRow 0, Column 1", 
                             font=ctk.CTkFont(weight="bold"))
        label2.pack(expand=True)
        self.demoFrames['grid_frame2'] = {'frame': frame2, 'type': 'demo'}

        frame3 = Frame(container, fg_color="#5a5a5a", corner_radius=8)
        frame3.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        
        label3 = ctk.CTkLabel(frame3, text="Frame 3\nRow 1, Spanning 2 columns", 
                             font=ctk.CTkFont(weight="bold"))
        label3.pack(expand=True)
        self.demoFrames['grid_frame3'] = {'frame': frame3, 'type': 'demo'}

    def showPlaceLayout(self):
        """Demonstrate Frame with place layout manager."""
        self.clearDemoArea()
        self.updateStatus("Place Layout Demo - Frames positioned using place()")

        # Create main container frame
        container = Frame(self.demoArea, fg_color="#2b2b2b", corner_radius=10)
        container.place(relx=0.5, rely=0.5, relwidth=0.9, relheight=0.8, anchor="center")
        self.demoFrames['place_container'] = {'frame': container, 'type': 'container'}

        # Create frames with absolute positioning
        frame1 = Frame(container, fg_color="#3a3a3a", corner_radius=8, width=150, height=80)
        frame1.place(relx=0.1, rely=0.2, anchor="nw")
        
        label1 = ctk.CTkLabel(frame1, text="Frame 1\n10%, 20%", 
                             font=ctk.CTkFont(weight="bold"))
        label1.pack(expand=True)
        self.demoFrames['place_frame1'] = {'frame': frame1, 'type': 'demo'}

        frame2 = Frame(container, fg_color="#4a4a4a", corner_radius=8, width=150, height=80)
        frame2.place(relx=0.5, rely=0.5, anchor="center")
        
        label2 = ctk.CTkLabel(frame2, text="Frame 2\nCenter", 
                             font=ctk.CTkFont(weight="bold"))
        label2.pack(expand=True)
        self.demoFrames['place_frame2'] = {'frame': frame2, 'type': 'demo'}

        frame3 = Frame(container, fg_color="#5a5a5a", corner_radius=8, width=150, height=80)
        frame3.place(relx=0.8, rely=0.8, anchor="se")
        
        label3 = ctk.CTkLabel(frame3, text="Frame 3\n80%, 80%", 
                             font=ctk.CTkFont(weight="bold"))
        label3.pack(expand=True)
        self.demoFrames['place_frame3'] = {'frame': frame3, 'type': 'demo'}

    def showNestedFrames(self):
        """Demonstrate nested Frame structures."""
        self.clearDemoArea()
        self.updateStatus("Nested Frames Demo - Complex hierarchy of frames")

        mainFrame = Frame(self.demoArea, fg_color="#2b2b2b", corner_radius=10)
        mainFrame.place(relx=0.5, rely=0.5, relwidth=0.9, relheight=0.8, anchor="center")
        self.demoFrames['nested_main'] = {'frame': mainFrame, 'type': 'container'}

        # Top section
        topFrame = Frame(mainFrame, fg_color="#3a3a3a", corner_radius=8, height=100)
        topFrame.pack(padx=10, pady=10, fill="x")
        
        topLabel = ctk.CTkLabel(topFrame, text="Header Section", 
                               font=ctk.CTkFont(size=16, weight="bold"))
        topLabel.pack(padx=10, pady=10)
        self.demoFrames['nested_top'] = {'frame': topFrame, 'type': 'demo'}

        # Middle section with two columns
        middleFrame = Frame(mainFrame, fg_color="transparent")
        middleFrame.pack(padx=10, pady=10, fill="both", expand=True)
        middleFrame.grid_columnconfigure(0, weight=1)
        middleFrame.grid_columnconfigure(1, weight=1)
        middleFrame.grid_rowconfigure(0, weight=1)
        self.demoFrames['nested_middle'] = {'frame': middleFrame, 'type': 'container'}

        # Left column
        leftFrame = Frame(middleFrame, fg_color="#4a4a4a", corner_radius=8)
        leftFrame.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        
        leftLabel = ctk.CTkLabel(leftFrame, text="Left Panel", 
                                font=ctk.CTkFont(weight="bold"))
        leftLabel.pack(padx=10, pady=10)
        self.demoFrames['nested_left'] = {'frame': leftFrame, 'type': 'demo'}

        # Right column
        rightFrame = Frame(middleFrame, fg_color="#4a4a4a", corner_radius=8)
        rightFrame.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
        
        rightLabel = ctk.CTkLabel(rightFrame, text="Right Panel", 
                                 font=ctk.CTkFont(weight="bold"))
        rightLabel.pack(padx=10, pady=10)
        self.demoFrames['nested_right'] = {'frame': rightFrame, 'type': 'demo'}

        # Bottom section
        bottomFrame = Frame(mainFrame, fg_color="#3a3a3a", corner_radius=8, height=80)
        bottomFrame.pack(padx=10, pady=10, fill="x")
        
        bottomLabel = ctk.CTkLabel(bottomFrame, text="Footer Section", 
                                  font=ctk.CTkFont(weight="bold"))
        bottomLabel.pack(padx=10, pady=10)
        self.demoFrames['nested_bottom'] = {'frame': bottomFrame, 'type': 'demo'}

    def showEventHandling(self):
        """Demonstrate event handling capabilities."""
        self.clearDemoArea()
        self.updateStatus("Event Handling Demo - Hover over frames to see events")

        # Create main container frame
        container = Frame(self.demoArea, fg_color="#2b2b2b", corner_radius=10)
        container.place(relx=0.5, rely=0.5, relwidth=0.9, relheight=0.8, anchor="center")
        self.demoFrames['event_container'] = {'frame': container, 'type': 'container'}

        # Event log area
        logFrame = Frame(container, fg_color="#1a1a1a", corner_radius=8)
        logFrame.pack(padx=10, pady=10, fill="both", expand=True)
        
        logLabel = ctk.CTkLabel(logFrame, text="Event Log:", 
                               font=ctk.CTkFont(weight="bold"))
        logLabel.pack(padx=10, pady=5, anchor="w")
        
        self.eventLog = ctk.CTkTextbox(logFrame, height=150)
        self.eventLog.pack(padx=10, pady=5, fill="both", expand=True)
        self.demoFrames['event_log'] = {'frame': logFrame, 'type': 'demo'}

        # Interactive frames
        interactiveFrame = Frame(container, fg_color="#3a3a3a", corner_radius=8, height=100)
        interactiveFrame.pack(padx=10, pady=10, fill="x")
        
        interactiveLabel = ctk.CTkLabel(interactiveFrame, 
                                       text="Hover, click, and right-click this frame", 
                                       font=ctk.CTkFont(weight="bold"))
        interactiveLabel.pack(padx=10, pady=10)
        self.demoFrames['event_interactive'] = {'frame': interactiveFrame, 'type': 'demo'}

        # Bind events
        def logEvent(event_name):
            def handler(event):
                self.eventLog.insert("end", f"{event_name}: {event}\n")
                self.eventLog.see("end")
            return handler

        interactiveFrame.bind("<Enter>", logEvent("Mouse Enter"))
        interactiveFrame.bind("<Leave>", logEvent("Mouse Leave"))
        interactiveFrame.bind("<Button-1>", logEvent("Left Click"))
        interactiveFrame.bind("<Button-3>", logEvent("Right Click"))
        interactiveFrame.bind("<B1-Motion>", logEvent("Left Drag"))
        interactiveFrame.bind("<KeyPress>", logEvent("Key Press"))

    def showDraggingFrames(self):
        """Demonstrate draggable frames."""
        self.clearDemoArea()
        self.updateStatus("Dragging Frames Demo - Click and drag the frames")

        container = Frame(self.demoArea, fg_color="#2b2b2b", corner_radius=10)
        container.place(relx=0.5, rely=0.5, relwidth=0.9, relheight=0.8, anchor="center")
        self.demoFrames['drag_container'] = {'frame': container, 'type': 'container'}

        # Create draggable frames
        dragFrame1 = Frame(container, fg_color="#3a3a3a", corner_radius=8, width=120, height=80)
        dragFrame1.place(relx=0.2, rely=0.3)
        
        label1 = ctk.CTkLabel(dragFrame1, text="Drag Me 1", 
                             font=ctk.CTkFont(weight="bold"))
        label1.pack(expand=True)
        self.demoFrames['drag_frame1'] = {'frame': dragFrame1, 'type': 'demo'}

        dragFrame2 = Frame(container, fg_color="#4a4a4a", corner_radius=8, width=120, height=80)
        dragFrame2.place(relx=0.5, rely=0.5)
        
        label2 = ctk.CTkLabel(dragFrame2, text="Drag Me 2", 
                             font=ctk.CTkFont(weight="bold"))
        label2.pack(expand=True)
        self.demoFrames['drag_frame2'] = {'frame': dragFrame2, 'type': 'demo'}

        dragFrame3 = Frame(container, fg_color="#5a5a5a", corner_radius=8, width=120, height=80)
        dragFrame3.place(relx=0.7, rely=0.7)
        
        label3 = ctk.CTkLabel(dragFrame3, text="Drag Me 3", 
                             font=ctk.CTkFont(weight="bold"))
        label3.pack(expand=True)
        self.demoFrames['drag_frame3'] = {'frame': dragFrame3, 'type': 'demo'}

    def showVisibilityControl(self):
        """Demonstrate show/hide functionality."""
        self.clearDemoArea()
        self.updateStatus("Visibility Control Demo - Use buttons to show/hide frames")

        container = Frame(self.demoArea, fg_color="#2b2b2b", corner_radius=10)
        container.place(relx=0.5, rely=0.5, relwidth=0.9, relheight=0.8, anchor="center")
        self.demoFrames['visibility_container'] = {'frame': container, 'type': 'container'}

        # Control panel
        controlFrame = Frame(container, fg_color="#3a3a3a", corner_radius=8, height=60)
        controlFrame.pack(padx=10, pady=10, fill="x")
        
        # Control buttons
        buttonFrame = ctk.CTkFrame(controlFrame, fg_color="transparent")
        buttonFrame.pack(padx=10, pady=10)
        
        showButton = ctk.CTkButton(buttonFrame, text="Show All", 
                                  command=self.showAllFrames)
        showButton.pack(side="left", padx=5)
        
        hideButton = ctk.CTkButton(buttonFrame, text="Hide All", 
                                  command=self.hideAllFrames)
        hideButton.pack(side="left", padx=5)
        
        toggleButton = ctk.CTkButton(buttonFrame, text="Toggle Frame 2", 
                                    command=self.toggleFrame2)
        toggleButton.pack(side="left", padx=5)
        self.demoFrames['visibility_control'] = {'frame': controlFrame, 'type': 'demo'}

        # Demo frames
        frame1 = Frame(container, fg_color="#4a4a4a", corner_radius=8, height=60)
        frame1.pack(padx=10, pady=5, fill="x")
        
        label1 = ctk.CTkLabel(frame1, text="Frame 1 (Always visible)", 
                             font=ctk.CTkFont(weight="bold"))
        label1.pack(padx=10, pady=10)
        self.demoFrames['visibility_frame1'] = {'frame': frame1, 'type': 'demo'}

        frame2 = Frame(container, fg_color="#5a5a5a", corner_radius=8, height=60)
        frame2.pack(padx=10, pady=5, fill="x")
        
        label2 = ctk.CTkLabel(frame2, text="Frame 2 (Toggle visibility)", 
                             font=ctk.CTkFont(weight="bold"))
        label2.pack(padx=10, pady=10)
        self.demoFrames['visibility_frame2'] = {'frame': frame2, 'type': 'demo'}

        frame3 = Frame(container, fg_color="#6a6a6a", corner_radius=8, height=60)
        frame3.pack(padx=10, pady=5, fill="x")
        
        label3 = ctk.CTkLabel(frame3, text="Frame 3 (Hide with others)", 
                             font=ctk.CTkFont(weight="bold"))
        label3.pack(padx=10, pady=10)
        self.demoFrames['visibility_frame3'] = {'frame': frame3, 'type': 'demo'}

    def showAllFrames(self):
        """Show all frames in visibility demo."""
        self.demoFrames['visibility_frame1']['frame'].show()
        self.demoFrames['visibility_frame2']['frame'].show()
        self.demoFrames['visibility_frame3']['frame'].show()
        
        # for frame_id, frame_info in self.demoFrames.items():
        #     if frame_id.startswith('visibility_frame'):
        #         frame_info['frame'].show()
        # self.updateStatus("All frames shown")

    def hideAllFrames(self):
        """Hide all frames in visibility demo."""
        self.demoFrames['visibility_frame1']['frame'].hide()
        self.demoFrames['visibility_frame2']['frame'].hide()
        self.demoFrames['visibility_frame3']['frame'].hide()
        
        # for frame_id, frame_info in self.demoFrames.items():
        #     if frame_id.startswith('visibility_frame') and frame_id != 'visibility_frame1':
        #         frame_info['frame'].hide()
        # self.updateStatus("Frames 2 and 3 hidden")

    def toggleFrame2(self):
        """Toggle visibility of frame 2."""
        frame2 = self.demoFrames['visibility_frame2']['frame']
        if frame2.winfo_ismapped():
            frame2.hide()
            self.updateStatus("Frame 2 hidden")
        else:
            frame2.show()
            self.updateStatus("Frame 2 shown")

    def showStyledFrames(self):
        """Demonstrate styled frames with different appearances."""
        self.clearDemoArea()
        self.updateStatus("Styled Frames Demo - Various frame styles and themes")

        # Create main container frame
        container = Frame(self.demoArea, fg_color="#2b2b2b", corner_radius=10)
        container.place(relx=0.5, rely=0.5, relwidth=0.9, relheight=0.8, anchor="center")
        self.demoFrames['styled_container'] = {'frame': container, 'type': 'container'}

        # Different styled frames
        styles = [
            {"fg_color": "#3a3a3a", "border_color": "#5a5a5a", "border_width": 2, "corner_radius": 15},
            {"fg_color": "#2c3e50", "border_color": "#3498db", "border_width": 3, "corner_radius": 20},
            {"fg_color": "#27ae60", "border_color": "#2ecc71", "border_width": 1, "corner_radius": 5},
            {"fg_color": "#e74c3c", "border_color": "#c0392b", "border_width": 4, "corner_radius": 25},
            {"fg_color": "#f39c12", "border_color": "#d35400", "border_width": 2, "corner_radius": 10},
            {"fg_color": "#9b59b6", "border_color": "#8e44ad", "border_width": 3, "corner_radius": 30}
        ]

        for i, style in enumerate(styles):
            frame = Frame(container, **style, height=70)
            frame.pack(padx=10, pady=5, fill="x")
            
            label = ctk.CTkLabel(frame, text=f"Styled Frame {i+1}", 
                                font=ctk.CTkFont(weight="bold"))
            label.pack(padx=10, pady=10)
            self.demoFrames[f'styled_frame{i+1}'] = {'frame': frame, 'type': 'demo'}

    def showFrameInfo(self):
        """Display information about Frame widget capabilities."""
        self.clearDemoArea()
        self.updateStatus("Frame Information - Capabilities and usage")

        infoText = """
Frame Widget Capabilities:

✓ Extends CTkFrame with enhanced functionality
✓ Integrated EventHandler for mouse/keyboard events
✓ Built-in Dragging capabilities for movable frames
✓ Dynamic show/hide methods for visibility control
✓ Support for all layout managers (pack, grid, place)
✓ Theme integration and custom styling
✓ Nested frame structures for complex UIs
✓ Robust error handling and validation

Usage Examples:
- Create organized UI layouts
- Implement draggable panels
- Build dynamic interfaces with show/hide
- Handle user interactions with events
- Create themed application sections
        """



        container = Frame(self.demoArea, fg_color="#2b2b2b", corner_radius=10)
        container.place(relx=0.5, rely=0.5, relwidth=0.9, relheight=0.8, anchor="center")
        
        infoLabel = ctk.CTkLabel(container, text=infoText, 
                                font=ctk.CTkFont(size=12), justify="left")
        infoLabel.pack(padx=20, pady=20)
        self.demoFrames['info_container'] = {'frame': container, 'type': 'demo'}

    def showAllFeatures(self):
        """Demonstrate all Frame features in one comprehensive example."""
        self.clearDemoArea()
        self.updateStatus("All Features Demo - Comprehensive Frame demonstration")

        # This would be a more complex example combining multiple features
        # For simplicity, we'll show the nested frames example
        self.showNestedFrames()
        self.updateStatus("All Features - Nested frames with event handling and styling")


def main():
    """Main function to run the Frame example."""
    app = FrameExample()
    app.mainloop()


if __name__ == "__main__":
    main()
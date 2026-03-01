"""UrlTool - A tool for handling and opening URLs with dynamic parameters."""

from ..widget.BaseWin import BaseWin
from ..widget.InputBar import InputBar
from ..widget.BtnBar import BtnBar, BtnConfig
from ..widget.TextBar import TextBar
from ..widget.basic.Frame import Frame
import webbrowser
import re


class UrlTool(BaseWin):
    def __init__(self, master=None, title="UrlTool", **kwargs):
        super().__init__(master=master, title=title, **kwargs)

        # Store dynamic parameter inputs
        self.paramInputs = {}
        
        # Dictionary to store parameter values
        self.parameters = {}

        # Create the UI components
        self.createUi()

    def createUi(self):
        """Create the main UI components."""
        # Configure grid weights for proper expansion
        self.contentFrame.grid_columnconfigure(0, weight=1)
        self.contentFrame.grid_rowconfigure(0, weight=0)  # URL input
        self.contentFrame.grid_rowconfigure(1, weight=0)  # Parameter inputs
        self.contentFrame.grid_rowconfigure(2, weight=0)  # Formatted URL
        self.contentFrame.grid_rowconfigure(3, weight=0)  # Button bar
        self.contentFrame.grid_rowconfigure(4, weight=1)  # Status area

        # Create URL InputBar
        self.urlInputBar = InputBar(self.contentFrame, title="URL:")
        self.urlInputBar.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

        # Bind Enter key to open URL
        self.urlInputBar.input.bind("<Return>", lambda e: self.openUrl())

        # Create parameter frame (initially empty)
        self.paramFrame = Frame(self.contentFrame)
        self.paramFrame.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
        self.paramFrame.grid_columnconfigure(0, weight=1)

        # Create formatted URL InputBar
        self.formattedUrlInputBar = InputBar(self.contentFrame, title="Formatted")
        self.formattedUrlInputBar.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
        self.formattedUrlInputBar.input.configure(state="readonly")

        # Create BtnBar with 2 buttons
        self.btnBar = BtnBar(self.contentFrame)
        self.btnBar.grid(row=3, column=0, sticky="ew", padx=5, pady=5)

        # Add buttons to BtnBar
        self.btnBar.addBtn(BtnConfig("Open", self.openUrl))
        self.btnBar.addBtn(BtnConfig("Clear", self.clearInputs))

        # Create status display area
        self.statusText: TextBar = TextBar(self.contentFrame)
        self.statusText.grid(row=4, column=0, sticky="nsew", padx=5, pady=5)

        # Make status text read-only
        self.statusText.textBox.disable()

        # Monitor URL changes for parameter detection
        self.urlInputBar.input.bind("<KeyRelease>", self.detectParameters)
        
        # Monitor parameter input changes
        self.urlInputBar.input.bind("<KeyRelease>", lambda e: self.updateFormattedUrl())
        
        # Initial update of formatted URL
        self.updateFormattedUrl()

    def detectParameters(self, event=None):
        """Detect {xxx} parameters in URL and create input fields for them."""
        urlText = self.urlInputBar.getValue().strip()

        # Find all {parameter} patterns
        parameters = re.findall(r'\{([^}]+)\}', urlText)

        # Clear existing parameter inputs
        for widget in self.paramFrame.winfo_children():
            widget.destroy()
        self.paramInputs.clear()
        
        # Clear existing parameters and initialize new ones
        self.parameters.clear()
        for param in parameters:
            self.parameters[param] = ""

        # Create input fields for each parameter
        for i, param in enumerate(parameters):
            # Create InputBar for parameter
            paramInput = InputBar(self.paramFrame, title=f"{param}:")
            paramInput.grid(row=i, column=0, sticky="ew", padx=5, pady=2)

            # Store reference to this input
            self.paramInputs[param] = paramInput

            # Bind Enter key to open URL
            paramInput.input.bind("<Return>", lambda e: self.openUrl())
            
            # Monitor parameter input changes
            paramInput.input.bind("<KeyRelease>", lambda e: self.onParameterChanged())

        # Update status
        if parameters:
            self.updateStatus(f"Detected parameters: {', '.join(parameters)}")
        else:
            self.updateStatus("No parameters detected in URL")
        
        # Update formatted URL after parameter detection
        self.updateFormattedUrl()

    def onParameterChanged(self):
        """Handle changes to parameter values."""
        # Update parameter values from input bars
        for param, inputBar in self.paramInputs.items():
            self.parameters[param] = inputBar.getValue().strip()
        
        self.updateFormattedUrl()

    def formatUrlWithParameters(self):
        """Format the URL by replacing parameters with their values."""
        url = self.urlInputBar.getValue().strip()
        
        # Replace each parameter placeholder with its value
        for param_name, param_value in self.parameters.items():
            placeholder = f"{{{param_name}}}"
            url = url.replace(placeholder, param_value)
        
        return url

    def updateFormattedUrl(self):
        """Update the formatted URL display with parameter substitutions."""
        try:
            formatted_url = self.formatUrlWithParameters()
            self.formattedUrlInputBar.setValue(formatted_url)
        except Exception as e:
            self.formattedUrlInputBar.setValue("Error formatting URL")

    def openUrl(self):
        """Open the URL in browser with parameter substitution."""
        try:
            # Get base URL
            urlTemplate = self.urlInputBar.getValue().strip()

            if not urlTemplate:
                self.updateStatus("❌ Please enter a URL")
                return

            # Substitute parameters
            finalUrl = urlTemplate
            for param, inputBar in self.paramInputs.items():
                paramValue = inputBar.getValue().strip()
                if paramValue:
                    finalUrl = finalUrl.replace(f"{{{param}}}", paramValue)
                else:
                    # If parameter not provided, keep the placeholder
                    pass

            # Check if any parameters remain unsubstituted
            remainingParams = re.findall(r'\{([^}]+)\}', finalUrl)
            if remainingParams:
                self.updateStatus(
                    f"⚠️  Warning: Parameters {remainingParams} not substituted. Opening as-is.")

            # Open in browser
            webbrowser.open(finalUrl)
            self.updateStatus(f"✅ Opened URL: {finalUrl}")

        except Exception as e:
            self.updateStatus(f"❌ Error opening URL: {str(e)}")

    def clearInputs(self):
        """Clear all input fields."""
        # Clear URL input
        self.urlInputBar.clear()

        # Clear parameter inputs
        for paramInput in self.paramInputs.values():
            paramInput.clear()

        # Clear parameter frame
        for widget in self.paramFrame.winfo_children():
            widget.destroy()
        self.paramInputs.clear()

        self.paramFrame.resize()

        # Clear status
        self.updateStatus("All inputs cleared")

    def updateStatus(self, message):
        """Update the status display with a message."""
        # Enable text widget for editing
        self.statusText.textBox.enable()

        # Clear previous content and add new message
        self.statusText.clearText()
        self.statusText.append(message)

        # Disable text widget to make it read-only
        self.statusText.textBox.disable()

    def getCmds(self):
        """Override to add custom menu commands for UrlTool."""
        # Get base menu commands
        baseCmds = super().getCmds()

        # Add UrlTool specific commands
        urltoolCmds = [
            ("UrlTool", [
                ("Open URL", self.openUrl),
                ("Clear Inputs", self.clearInputs),
                ("Detect Parameters", self.detectParameters),
                ("Clear Status", lambda: self.updateStatus("Status cleared."))
            ])
        ]

        # Insert UrlTool commands at the beginning
        baseCmds = urltoolCmds + baseCmds

        return baseCmds
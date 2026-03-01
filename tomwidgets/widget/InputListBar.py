from .basic.Frame import Frame
from .InputBar import InputBar
from .basic.Button import Button
from .BtnBar import BtnBar, BtnConfig
from .OptionBar import OptionBar


DelIcon = "✕"


class Event:
    InputChange = "inputChange"
    DelInput = "delInput"


class OptionInput:
    def __init__(self, name: str, values: list, default=""):
        self.name = name
        self.values = values

        if default in values:
            self._default = default
        else:
            self._default = values[0] if values else ""

    def getDefault(self):
        return self._default

    def bind(self, bar: OptionBar):
        self.bar = bar
        bar.setOptions(self.values)
        bar.setSelectedOption(self._default)


class InputListBar(Frame):
    def __init__(self, master, showRemoveBtn=False, showBtnBar=False, **kwargs):
        super().__init__(master, **kwargs)

        self.showRemoveBtn = showRemoveBtn
        self.showBtnBar = showBtnBar

        # Configure grid layout
        self.grid_columnconfigure(0, weight=1)

        # Store arguments and InputBars
        self.arguments = {}
        self.inputBars: dict[str, InputBar] = {}
        self.removeBtns = {}
        self.rowCounter = 0

        # Create control buttons frame
        self.createBtnBar()

    def createBtnBar(self):
        bar = self.btnBar = BtnBar(self, padx=5, pady=0)
        bar.grid(row=1000, column=0, sticky="ew", pady=(10, 0))
        bar.addBtns([
            BtnConfig("Confirm", self.confirm),
            BtnConfig("Cancel", self.cancel),
        ])

        if not self.showBtnBar:
            bar.hide()

    def setArguments(self, arguments):
        # Clear existing arguments
        self.clearAllArguments()

        # Add new arguments
        self.addArguments(arguments)

    def addArguments(self, arguments):
        for name, value in arguments.items():
            self.addArgument(name, value)

    def addArgument(self, name, value=""):
        if name in self.arguments:
            # Update existing argument
            if isinstance(value, OptionInput):
                value.bind(self.inputBars[name])
            else:
                self.inputBars[name].setValue(str(value))
        else:
            self.createArgumentRow(name, value)

        self.arguments[name] = value

    def createArgumentRow(self, name, value):
        """Create a row with InputBar and remove button for an argument."""
        rowFrame = Frame(self)
        rowFrame.grid(row=self.rowCounter, column=0, sticky="ew", pady=2)
        rowFrame.grid_columnconfigure(0, weight=1)

        if isinstance(value, OptionInput):
            # Create OptionBar for the argument
            inputBar = OptionBar(rowFrame, title=name + ":")
            value.bind(inputBar)
            inputBar.grid(row=0, column=0, sticky="ew", padx=(0, 5))
        else:
            # Create InputBar for the argument
            inputBar = InputBar(rowFrame, title=name + ":",
                                default=str(value))
            inputBar.grid(row=0, column=0, sticky="ew", padx=(0, 5))

        inputBar.bindEvent(self.onInputChange)

        # Create remove button
        removeButton = Button(rowFrame, text=DelIcon, width=30, height=30,
                              command=lambda n=name: self.removeArgument(n))
        removeButton.grid(row=0, column=1, sticky="e")

        if not self.showRemoveBtn:
            removeButton.hide()

        # Store reference
        self.inputBars[name] = inputBar
        self.removeBtns[name] = removeButton
        self.rowCounter += 1

    def removeArgument(self, name):
        if name in self.arguments:
            # Remove from storage
            del self.arguments[name]

            # Destroy the InputBar and remove button
            if name in self.inputBars:
                self.inputBars[name].master.destroy()
                del self.inputBars[name]

                if name in self.removeBtns:
                    self.removeBtns[name].master.destroy()
                    del self.removeBtns[name]

            # Reorganize the grid layout
            self.reorganizeLayout()

            self.generateEvent(Event.DelInput)

    def removeArguments(self, names):
        for name in names:
            self.removeArgument(name)

    def reorganizeLayout(self):
        """Reorganize the grid layout after removing arguments."""
        # Reset row counter and recreate layout
        self.rowCounter = 0

        # Recreate all remaining arguments
        for name, value in self.arguments.items():
            # Find the existing rowFrame if it exists, otherwise create new
            if name in self.inputBars:
                # Destroy the existing rowFrame
                self.inputBars[name].master.destroy()
                del self.inputBars[name]

                if name in self.removeBtns:
                    self.removeBtns[name].master.destroy()
                    del self.removeBtns[name]

            self.createArgumentRow(name, value)

    def clearAllArguments(self):
        """Clear all arguments from the InputListBar."""
        # Destroy all argument rows
        # Use list() to avoid modification during iteration
        for name in list(self.inputBars.keys()):
            if name in self.inputBars:
                # Destroy the master (rowFrame) that contains the input bar and remove button
                self.inputBars[name].master.destroy()
                # Remove from dictionaries
                del self.inputBars[name]
                if name in self.arguments:
                    del self.arguments[name]

            if name in self.removeBtns:
                self.removeBtns[name].master.destroy()
                del self.removeBtns[name]

        # Clear any remaining entries
        self.arguments.clear()
        self.rowCounter = 0

        self.resizeGrid()

        # Trigger layout update to ensure proper UI cleanup
        self.reorganizeLayout()

    def getArguments(self):
        currentArgs = {}
        for name, inputBar in self.inputBars.items():
            if isinstance(inputBar, OptionBar):
                currentArgs[name] = inputBar.getSelectedOption()
            else:
                currentArgs[name] = inputBar.getValue()

        return currentArgs

    def confirm(self, event=None):
        """Confirm the arguments and generate confirm event."""
        self.generateEvent("confirm")

    def cancel(self, event=None):
        """Generate cancel event."""
        self.generateEvent("cancel")

    def onConfirm(self, callback):
        self.bindEvent(callback, "confirm")

    def onCancel(self, callback):
        self.bindEvent(callback, "cancel")

    def toggleBtnBar(self):
        """Toggle the visibility of the confirm and cancel buttons."""
        self.showBtnBar = not self.showBtnBar
        if self.showBtnBar:
            self.btnBar.show()
        else:
            self.btnBar.hide()

    def toggleRemoveBtn(self):
        """Toggle the visibility of the remove buttons."""
        self.showRemoveBtn = not self.showRemoveBtn
        for btn in self.removeBtns.values():
            if self.showRemoveBtn:
                btn.show()
            else:
                btn.hide()

    def bindInput(self, name, callback):
        """Bind a callback function to the input change event."""
        widget = self.inputBars[name]
        widget.bindEvent(callback)

    def updateInputs(self, args: dict):
        for name, value in args.items():
            if name in self.inputBars:
                inputBar = self.inputBars[name]
                if isinstance(inputBar, OptionBar):
                    inputBar.setSelectedOption(value)
                else:
                    inputBar.setValue(value)

    def onInputChange(self, event=None):
        self.generateEvent(Event.InputChange)

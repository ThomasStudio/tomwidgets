import os
from functools import partial
from tkinter import filedialog, messagebox

from .BaseWin import BaseWin
from .BtnBar import BtnBar, BtnConfig
from .CodeWin import CodeWin
from .InputListBar import InputListBar, OptionInput, Event as InputListBarEvent
from ..util.JsonFile import JsonFile
from ..Template.Template import Template, ConfigKeys, TemplateType


class Event:
    InputChange = "inputChange"


class TemplateWin(BaseWin):
    def __init__(self, master=None, title="Template Win", **kwargs):
        super().__init__(master, title=title, **kwargs)
        # Configuration
        self.configFile = "template.json"
        self.configDict = self.loadConfig()

        # Current template state
        self.template: Template = None
        self.isPreviewing = False
        self.originalContent = None

        # Setup UI
        self.setupUi()

    def loadConfig(self):
        defaultConfig = {
            "home": os.path.join(os.getcwd(), "templates"),
            "import_folders": [],
            "groups": []
        }

        jsonFile = JsonFile(self.configFile)

        if jsonFile.data:  # If there's existing data
            for key, value in defaultConfig.items():
                if key not in jsonFile.data:
                    jsonFile.data[key] = value
            jsonFile.update(jsonFile.data)
            return jsonFile.data
        else:
            jsonFile.update(defaultConfig)
            os.makedirs(defaultConfig["home"], exist_ok=True)
            return defaultConfig

    def saveConfig(self):
        JsonFile(self.configFile).update(self.configDict)

    def setupUi(self):
        """
        Setup the user interface
        """
        # Configure grid weights for proper expansion
        self.grid_rowconfigure(3, weight=1)  # For code editor
        self.grid_columnconfigure(0, weight=1)
        row = 1

        # Button bar
        btnBar = self.btnBar = BtnBar(self)
        btnBar.grid(row=row, column=0, sticky="ew", padx=5, pady=5)
        row += 1

        # Add buttons
        btnBar.addBtns([
            BtnConfig(name="Open", callback=self.openTemplate),
            BtnConfig(name="New", callback=self.createTemplate),
            BtnConfig(name="Add", callback=self.importTemplate),
            BtnConfig(isLabel=True, name=" "),
        ])

        # Input list bar for template arguments
        self.inputListBar = InputListBar(self, showRemoveBtn=True)
        self.inputListBar.grid(row=row, column=0, sticky="ew", padx=5, pady=5)
        self.inputListBar.bindEvent(
            self.onInputChange, InputListBarEvent.InputChange)
        self.inputListBar.bindEvent(
            self.onDelInput, InputListBarEvent.DelInput)
        row += 1

        # Code editor for template content
        self.codeWin = CodeWin(self, asWin=False, showTitleBar=False)
        self.codeWin.grid(row=row, column=0, sticky="nsew", padx=5, pady=5)
        self.codeWin.textBar.titleBar.addBtnsToBar([
            BtnConfig(name="preview", callback=self.togglePreview),
            BtnConfig(name="Render", callback=self.renderTemplate),
            BtnConfig(name="Save", callback=self.saveTemplate),
            BtnConfig(name="Reload", callback=self.reloadTemplate),
            BtnConfig(isLabel=True, name=" "),
            BtnConfig(name="Close", callback=self.resetTemplate),
            BtnConfig(name="Del", callback=self.deleteTemplate),

        ])
        row += 1

        self.hideTemplateWin()

    def openTemplate(self):
        """
        Open an existing template
        """
        templateDir = self.configDict.get(
            "home", os.path.join(os.getcwd(), "templates"))
        filePath = filedialog.askopenfilename(
            title="Open Template",
            initialdir=templateDir,
            filetypes=[("Templates", "*.*")]
        )

        if filePath:
            self.loadTemplate(filePath)

    def createTemplate(self):
        """
        Create a new template
        """
        templateDir = self.configDict.get(
            "home", os.path.join(os.getcwd(), "templates"))

        if self.template:
            templateDir = os.path.dirname(self.template.filePath)

        filePath = filedialog.asksaveasfilename(
            title="Create New Template",
            initialdir=templateDir,
            filetypes=[("Templates", "*.*")]
        )

        if filePath:
            # Create empty template file
            with open(filePath, 'w', encoding='utf-8') as f:
                f.write("{# New template #}\n")

            self.loadTemplate(filePath)

    def importTemplate(self):
        """
        Import an existing file as a template
        """
        sourcePath = filedialog.askopenfilename(
            title="Import Template",
            filetypes=[("All Files", "*.*")]
        )

        if sourcePath:
            templateDir = self.configDict.get(
                "home", os.path.join(os.getcwd(), "templates"))

            if self.template:
                templateDir = os.path.dirname(self.template.filePath)

            templateName = os.path.basename(sourcePath)
            destPath = os.path.join(templateDir, templateName)

            # Copy file to template directory
            with open(sourcePath, 'r', encoding='utf-8') as src, \
                    open(destPath, 'w', encoding='utf-8') as dst:
                dst.write(src.read())

            self.loadTemplate(destPath)

    def deleteTemplate(self):
        """
        Delete the current template
        """
        path = self.template.filePath
        if not path:
            messagebox.showwarning("Warning", "No template loaded to delete")
            return

        if messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete {path}?"):
            try:
                os.remove(path)
                self.resetTemplate()
                messagebox.showinfo("Success", "Template deleted successfully")
            except Exception as e:
                messagebox.showerror(
                    "Error", f"Failed to delete template: {e}")

    def loadTemplate(self, filePath):
        try:
            temp = self.template = Template(filePath=filePath)
            if not temp:
                return

            self.template = temp

            self.titleBar.setTitle(os.path.basename(filePath))

            # Load content in code editor
            self.updateCodeWin()
            self.originalContent = temp.source

            # Update input list bar with arguments
            self.updateInputListBar()

            # Enable the Save button since a template is now loaded
            self.showTemplateWin()

        except Exception as e:
            messagebox.showerror("Error", f"Failed to load template: {e}")

    def updateInputListBar(self):
        """update input list for template arguments"""
        args = {k: "" for k in self.template.variables()}
        conf = self.template.config()
        args.update({k: v for k, v in conf.items() if k in args})
        print(args)

        self.inputListBar.setArguments(args)
        self.addTemplateConfigToInput()

    def saveTemplate(self):
        """
        Save the current template
        """
        if not self.template or not self.template.filePath:
            messagebox.showwarning("Warning", "No template loaded to save")
            return

        if self.isPreviewing:
            self.togglePreview()

        try:
            if self.isPreviewing:
                return

            # Get the current content from the code editor
            content = self.codeWin.getText()
            content = self.updateTemplateConfigInContent(content)

            if self.template.updateTemplate(content):
                messagebox.showinfo(
                    "Success", f"Template saved successfully to {self.template.filePath}")
                self.reloadTemplate()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save template: {e}")

    def resetTemplate(self):
        """
        Reset the current template state
        """
        self.originalContent = None
        self.titleBar.setTitle("Template Tool")
        self.inputListBar.clearAllArguments()
        self.template = None

        # Disable the Save button since no template is loaded
        self.hideTemplateWin()

    def showTemplateWin(self):
        """
        show template win
        """
        # Enable the button using BtnBar's method
        self.btnBar.enableGroup("opened")
        self.codeWin.show()

    def hideTemplateWin(self):
        """
        hide tempalte win
        """
        # Disable the button using BtnBar's method
        self.btnBar.disableGroup("opened")
        self.codeWin.hide()

    def updateTemplateConfigInContent(self, content) -> str:
        conf = self.getInputs()
        temp = Template(content)
        temp.config(conf)

        return temp.source

    def renderContent(self, content: str = None) -> str:
        inputs = self.getInputs()
        try:
            if content:
                return Template(source=content).render(**inputs).lstrip()
            else:
                return self.template.render(**inputs).lstrip()
        except Exception as e:
            print(f"Error: Failed to run template: {e}")

        return None

    def renderTemplate(self):
        inputs = self.getInputs()

        # Determine output path based on configuration or user input
        outputPath = self.template.outputPath()
        if not outputPath:
            # Ask user for output location if not specified in config
            outputPath = filedialog.askdirectory(
                title="Select Output Directory",
                initialdir=os.path.dirname(outputPath),
            )

        if outputPath:
            outputFile = self.template.outputFilePath()

            if not os.path.exists(outputPath):
                os.makedirs(outputPath)
            elif os.path.exists(outputFile):
                if not messagebox.askyesno("Warning", f"File {outputFile} already exists. Overwrite?"):
                    return

            if self.template.saveRenderResult(outputFile, **inputs):
                messagebox.showinfo(
                    "Success", f"Template rendered successfully to {outputFile}")
            else:
                messagebox.showerror(
                    "Error", f"Failed to render template to {outputFile}")
        else:
            messagebox.showinfo(
                "Info", "Template rendering completed but no output file was selected")

    def getInputs(self):
        return self.inputListBar.getArguments()

    def updateInputs(self, args: dict):
        self.inputListBar.updateInputs(args)

    def preview(self):
        if self.isPreviewing:
            return

        content = self.originalContent = self.codeWin.getText()
        previewContent = self.renderContent(content)

        if previewContent:
            self.codeWin.setText(previewContent.strip())
        else:
            messagebox.showerror(
                "Error", "Failed to preview template. Check the template content and inputs.")

    def original(self):
        if self.isPreviewing == True:
            self.togglePreview()

    def togglePreview(self):
        if self.isPreviewing:
            self.codeWin.textBar.titleBar.btnBar.modifyBtn(
                "original", "preview")

            self.updateCodeWin(
                self.originalContent or self.template.sourceWithoutComments)
        else:
            self.codeWin.textBar.titleBar.btnBar.modifyBtn(
                "preview", "original")
            self.preview()

        self.isPreviewing = not self.isPreviewing

    def reloadTemplate(self):
        """
        Reload the current template from the file
        """
        if self.template:
            self.loadTemplate(self.template.filePath)
        else:
            messagebox.showerror(
                "Error", "No template file is currently open.")

    def addTemplateConfigToInput(self):
        try:
            conf = self.template.config()
            for key in conf.keys():
                if key == ConfigKeys.TEMPLATE_TYPE.value:
                    oi = OptionInput(ConfigKeys.TEMPLATE_TYPE.value, [
                        item.value for item in TemplateType], conf[key])
                    self.inputListBar.addArgument(key, oi)
                else:
                    self.inputListBar.addArgument(key, conf[key])

                self.inputListBar.bindInput(
                    key, partial(self.onTemplateConfigChange, key))
        except Exception as e:
            messagebox.showerror(
                "Error", f"Failed to load template config: {e}")

    def onTemplateConfigChange(self, key=None, event=None):
        dc = self.getInputs()
        self.template.config({key: dc[key]})

        self.updateCodeWin()

    def contentWithTemplateConfig(self, content: str = None):
        content = content or self.template.source or self.codeWin.getText()

        if not content:
            return content

        # Get the current content from the code editor
        return self.updateTemplateConfigInContent(content)

    def onInputChange(self, event=None):
        self.generateEvent(Event.InputChange)

        self.template.config(self.getInputs())
        self.updateCodeWin()

    def onDelInput(self, event=None, data=None):
        print(f"onDelInput: {data}")

    def updateCodeWin(self, content: str = None):
        content = content or self.template.sourceWithoutComments.lstrip()

        if content:
            self.codeWin.setText(content)

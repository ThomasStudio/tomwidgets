"""
CodeTool class for managing TemplateGroup operations
"""
from functools import partial
import tkinter as tk
from tkinter import filedialog, messagebox
from typing import Dict, Optional
import json

from ..widget.BaseWin import BaseWin
from ..widget.BtnBar import BtnBar, BtnConfig
from ..Template.TemplateGroup import TemplateGroup
from ..widget.basic.Textbox import Textbox
from ..widget.basic.Frame import Frame
from ..widget.TemplateWin import TemplateWin, Event as TemplateWinEvent
from ..widget.basic.Tabview import Tabview
from ..widget.WrapBtnBar import WrapBtnBar, WrapBtnConfig
from ..widget.TextBar import TextBar


class CodeTool(BaseWin):
    """
    A tool for managing TemplateGroup operations including:
    - Managing TemplateGroup (open, add, del, update)
    - Showing and updating TemplateGroup configuration
    - Showing and updating Template variables
    - Managing Templates
    - Rendering individual/all Templates in a TemplateGroup
    """

    def __init__(self, master=None, title="Code Tool", showTitleBar=True, showFolderBar=False, asWin=True, **kwargs):
        super().__init__(master=master, title=title, showTitleBar=showTitleBar,
                         showFolderBar=showFolderBar, asWin=asWin, **kwargs)

        # Initialize variables
        self.currentTemplateGroup: Optional[TemplateGroup] = None
        self.templateGroups: Dict[str, TemplateGroup] = {}

        # Create UI components
        self.createUi()

    def createUi(self):
        """Create the main UI components."""
        row = 0
        # Create button bar for main operations
        self.mainBtnBar = BtnBar(self.contentFrame)
        self.mainBtnBar.grid(row=row, column=0, sticky="ew", padx=5, pady=5)
        row += 1

        # Configure grid weights
        self.contentFrame.grid_columnconfigure(0, weight=1)
        self.contentFrame.grid_rowconfigure(1, weight=1)

        # Add buttons to main button bar
        self.mainBtnBar.addBtn(BtnConfig("Open", self.openTemplateGroup))
        self.mainBtnBar.addBtn(BtnConfig("New", self.newTemplateGroup))
        self.mainBtnBar.addBtn(BtnConfig(" ", isLabel=True))
        self.mainBtnBar.addBtn(
            BtnConfig("Close", self.closeTemplateGroup, group="opened"))
        # self.mainBtnBar.addBtn(BtnConfig("Save", self.saveTemplateGroup))

        # Create a frame for template group management
        self.managementFrame = Frame(self.contentFrame)
        self.managementFrame.grid(
            row=row, column=0, sticky="nsew", padx=5, pady=5)
        self.managementFrame.grid_columnconfigure(0, weight=1)
        self.managementFrame.grid_rowconfigure(0, weight=1)
        row += 1

        self.createTemplateTab(self.managementFrame)

        # Create a frame for configuration editing
        self.configFrame = Frame(self.contentFrame)
        self.configFrame.grid(row=row, column=0, sticky="ew", padx=5, pady=5)
        self.configFrame.grid_columnconfigure(0, weight=1)
        row += 1

        self.toggleOpened()

    def toggleOpened(self):
        if self.currentTemplateGroup:
            self.managementFrame.show()
            self.configFrame.show()
            self.mainBtnBar.enableGroup("opened")
        else:
            self.managementFrame.hide()
            self.configFrame.hide()
            self.mainBtnBar.disableGroup("opened")
            self.templatesBar.clear()

    def closeTemplateGroup(self):
        self.currentTemplateGroup = None
        self.toggleOpened()

    def createTemplateTab(self, frame):
        """Create a new TemplateWin for editing templates."""
        self.tabView = Tabview(frame)
        self.tabView.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        tab = self.templateTab = self.tabView.add("Templates")
        self.templatesBar: WrapBtnBar = WrapBtnBar(tab)
        self.templatesBar.pack(fill=tk.BOTH, expand=True)

        tab = self.configTab = self.tabView.add("Config")
        editor = self.configEditor = TextBar(tab)
        editor.pack(fill=tk.BOTH, expand=True)
        editor.titleBar.addBtnToBar("Reload", self.reloadConfig)
        editor.titleBar.addBtnToBar("Save", self.saveTemplateGroupConfig)

        tab = self.statusTab = self.tabView.add("Status")
        self.statusArea = Textbox(tab, wrap=tk.WORD)
        self.statusArea.pack(fill=tk.BOTH, expand=True)

    def openTemplateGroup(self):
        """Open an existing TemplateGroup from a folder."""
        folderPath = filedialog.askdirectory(
            title="Select Template Group Folder")
        if folderPath:
            try:
                templateGroup = TemplateGroup(folderPath=folderPath)
                groupName = folderPath.split(
                    '/')[-1] if folderPath else "unnamed"
                self.templateGroups[groupName] = templateGroup
                self.currentTemplateGroup = templateGroup
                self.updateStatus(
                    f"Opened TemplateGroup: {groupName} with {templateGroup.count()} templates")

                self.loadTemplateGroup()
            except Exception as e:
                messagebox.showerror(
                    "Error", f"Failed to open TemplateGroup: {str(e)}")

    def newTemplateGroup(self):
        """Create a new TemplateGroup."""
        folderPath = filedialog.askdirectory(
            title="Select Folder for New Template Group")
        if folderPath:
            try:
                templateGroup = TemplateGroup(folderPath=folderPath)
                groupName = folderPath.split(
                    '/')[-1] if folderPath else "new_group"
                self.templateGroups[groupName] = templateGroup
                self.currentTemplateGroup = templateGroup
                self.updateStatus(f"Created new TemplateGroup: {groupName}")
            except Exception as e:
                messagebox.showerror(
                    "Error", f"Failed to create TemplateGroup: {str(e)}")

    def loadTemplateGroup(self):
        """Load the current TemplateGroup into the UI."""
        self.toggleOpened()

        group = self.currentTemplateGroup
        if group:
            self.templatesBar.clear()
            self.templatesBar.addBtns(
                [WrapBtnConfig(name, partial(self.openTemplate, name)) for name, _ in group.templates.items()])

            self.configEditor.clearText()
            self.configEditor.insert(
                tk.END, json.dumps(group.config, indent=4))

    def saveTemplateGroup(self):
        """Save the current TemplateGroup configuration."""
        if self.currentTemplateGroup:
            try:
                self.currentTemplateGroup.saveConfig()
                self.updateStatus(
                    "TemplateGroup configuration saved successfully")
            except Exception as e:
                messagebox.showerror(
                    "Error", f"Failed to save TemplateGroup: {str(e)}")
        else:
            messagebox.showwarning("Warning", "No TemplateGroup loaded")

    def renderAllTemplates(self):
        """Render all templates in the current TemplateGroup."""
        if not self.currentTemplateGroup:
            messagebox.showwarning("Warning", "No TemplateGroup loaded")
            return

        try:
            results = self.currentTemplateGroup.renderAll(save=True)
            self.updateStatus(
                f"Rendered {len(results)} templates. Results saved to output directory.")
        except Exception as e:
            messagebox.showerror(
                "Error", f"Failed to render templates: {str(e)}")

    def updateStatus(self, message: str):
        """Update the status area with a message."""
        self.statusArea.delete("1.0", tk.END)
        self.statusArea.insert("1.0", message)

    def saveTemplateGroupConfig(self):
        group = self.currentTemplateGroup
        if not group:
            messagebox.showwarning("Warning", "No TemplateGroup loaded")
            return

        if not messagebox.askyesno("Confirm", "Save configuration?"):
            return

        content = self.configEditor.getText().strip()
        if len(content) == 0:
            messagebox.showwarning("Warning", "Empty configuration")
            return

        path = group.configPath

        try:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)

            group.reload()

            self.loadTemplateGroup()

            self.updateStatus(
                "TemplateGroup configuration saved successfully")
        except Exception as e:
            messagebox.showerror(
                "Error", f"Failed to save TemplateGroup: {str(e)}")

    def openTemplate(self, templateName: str):
        """Open the selected template in the editor."""
        if not self.currentTemplateGroup:
            messagebox.showwarning("Warning", "No TemplateGroup loaded")
            return

        template = self.currentTemplateGroup.templates.get(templateName)
        if not template:
            messagebox.showwarning(
                "Warning", f"Template {templateName} not found")
            return

        win = TemplateWin(title=templateName)
        win.loadTemplate(template.filePath)
        win.bindEvent(partial(self.onInputChange, win),
                      TemplateWinEvent.InputChange)
        win.show()

    def reloadConfig(self):
        group = self.currentTemplateGroup
        if not group:
            messagebox.showwarning("Warning", "No TemplateGroup loaded")
            return False

        group.reload()

        self.configEditor.clearText()
        self.configEditor.insert(
            tk.END, json.dumps(group.config, indent=4))

        return True

    def onInputChange(self, templateWin: TemplateWin, event=None):
        name = templateWin.template.name()
        args = templateWin.getInputs()

        print(f"Input changed: {name} {args}")

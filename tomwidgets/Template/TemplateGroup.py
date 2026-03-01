"""
TemplateGroup class to manage a group of Template objects
"""
import json
import os
from typing import Dict, List, Optional
from .Template import Template, Env

ConfigFileName = 'template.json'
ConfigFolder = "config"
DefaultConfig = {
    "targetRoot": "templates/output",
}


class TemplateGroup:
    """
    Class to manage a group of Template objects from a folder
    """

    def __init__(self, folderPath: Optional[str] = None):
        self.templates: Dict[str, Template] = {}
        self.config = DefaultConfig.copy()
        self.targetRoot = DefaultConfig["targetRoot"]

        self.folderPath = folderPath

        configPath = self.configPath = os.path.join(
            folderPath, ConfigFolder, ConfigFileName) if folderPath else None

        # If config path is provided, load configuration from the file
        if configPath and os.path.exists(configPath):
            self.loadConfig(configPath)
        else:
            # Create default config if config path is provided but file doesn't exist
            if configPath:
                self.createDefaultConfig(configPath)

        # If folder path is provided, load templates from folder
        if folderPath:
            if folderPath and os.path.exists(folderPath):
                self.loadFromFolder(folderPath)

    def loadConfig(self, configPath: str = None, config: Dict = DefaultConfig):
        """if configPath is None: load configuration from config"""
        self.config = config.copy()

        if configPath:
            with open(configPath, 'r', encoding='utf-8') as f:
                config = self.config = json.load(f)

        self.targetRoot = config.get('targetRoot', None)

    def createDefaultConfig(self, configPath: str):
        # Ensure the directory exists
        os.makedirs(os.path.dirname(configPath), exist_ok=True)

        with open(configPath, 'w', encoding='utf-8') as f:
            json.dump(DefaultConfig, f, indent=2)

        # Load the newly created config
        self.loadConfig()

    def saveConfig(self, configPath: Optional[str] = None):
        path_to_use = configPath or self.configPath

        if not path_to_use:
            raise ValueError(
                "No configuration path provided or set during initialization")

        config = {
            "targetRoot": self.targetRoot,
        }

        # Ensure the directory exists
        os.makedirs(os.path.dirname(path_to_use), exist_ok=True)

        with open(path_to_use, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2)

    def reload(self):
        self.templates: Dict[str, Template] = {}
        self.targetRoot: Optional[str] = None

        self.loadConfig(self.configPath)
        self.loadFromFolder(self.folderPath)

    def loadFromFolder(self, folderPath: str):
        if not os.path.exists(folderPath):
            raise ValueError(f"Folder path does not exist: {folderPath}")

        self.folderPath = folderPath
        self.templates = {}

        for filename in os.listdir(folderPath):
            filePath = os.path.join(folderPath, filename)
            if os.path.isfile(filePath):
                # Create Template from file
                template = Template(filePath=filePath)
                self.templates[filename] = template

    def get(self, name: str) -> Optional[Template]:
        return self.templates.get(name)

    def update(self, name: str, template: Template) -> bool:
        self.templates[name] = template
        return True

    def delete(self, name: str) -> bool:
        if name in self.templates:
            del self.templates[name]
            return True
        return False

    def getAllVariables(self) -> Dict[str, List[str]]:
        allVariables = {}
        for name, template in self.templates.items():
            allVariables[name] = list(template.variables())
        return allVariables

    def renderAll(self, save: bool = False, **kwargs) -> Dict[str, str]:
        renderedResults = {}

        for name, template in self.templates.items():
            params = {}
            params.update(kwargs)

            renderd = template.render(**params)
            renderedResults[name] = renderd

            if save:
                path = template.outputFilePath(self.targetRoot)
                template.saveRenderResult(path, params)

        return renderedResults

    def listTemplateKeys(self) -> List[str]:
        return list(self.templates.keys())

    def count(self) -> int:
        return len(self.listTemplateKeys())

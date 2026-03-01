"""
TemplateX class that extends Jinja2.Template functionality
"""
from __future__ import annotations
import jinja2
import os
import re
from enum import Enum
from jinja2 import Environment, meta


# Create a Jinja2 environment
Env = Environment(loader=jinja2.FileSystemLoader(searchpath="./"))


class ConfigKeys(Enum):
    TEMPLATE_TYPE = "template-type"
    TARGET_PATH = "target-path"
    ROOT_PATH = "root-path"


class TemplateType(Enum):
    NEW = "template-new"
    UPDATE = "template-update"

    def getType(value):
        for item in TemplateType:
            if item.value == value:
                return item
        return None


DefaultTemplateConfig = {
    ConfigKeys.TEMPLATE_TYPE.value: TemplateType.NEW.value,
    ConfigKeys.ROOT_PATH.value: "",
    ConfigKeys.TARGET_PATH.value: "templates/output",
}


class Template:
    """
    Extended Template class with additional functionality
    """

    def __init__(self, source=None, filePath=None):
        """
        Create template from source or filePath
        :param source: Template source string
        :param filePath: Path to template file
        """
        self.filePath = filePath
        self.source = source
        self._template = None
        self._config = DefaultTemplateConfig.copy()

        if source is not None:
            # Create template from source
            self.source = source
            self._template = Env.from_string(source)
        elif filePath is not None and os.path.exists(filePath):
            # Create template from filePath
            with open(filePath, 'r', encoding='utf-8') as f:
                source = f.read()
            self.source = source
            # Load template from file using the environment
            self._template = Env.from_string(source)
            self.filePath = filePath
        else:
            raise ValueError(
                "Either source or filePath must be provided and valid")

        self.config()

    def variables(self):
        """
        Return all variables in template content
        """
        return list(GetVariables(self.source))

    def updateTemplate(self, source=None):
        """
        Update template file with new source
        :param source: New template source
        """
        if source is None:
            return False

        if self.filePath is None:
            raise ValueError(
                "Template was created from source only, no file path available to update")

        if not os.path.exists(self.filePath):
            return False

        self.source = source
        with open(self.filePath, "w", encoding="utf-8") as f:
            f.write(self.source)

        self.reload()
        return True

    def reload(self):
        path = self.filePath
        if path is not None and os.path.exists(path):
            # Create template from filePath
            with open(path, 'r', encoding='utf-8') as f:
                source = f.read()
            self.source = source
            # Load template from file using the environment
            self._template = Env.from_string(source)

        self.config()

    def saveRenderResult(self, path=None, **kwargs) -> bool:
        """
        Save rendered template to file
        :param path: Path to save the rendered result
        :param kwargs: Variables to render the template with
        """
        try:
            path = path or self.outputFilePath()

            outputPath = os.path.dirname(path)
            if not os.path.exists(outputPath):
                os.makedirs(outputPath)

            renderedContent = self._template.render(**kwargs).lstrip()
            with open(path, "w", encoding="utf-8") as f:
                f.write(renderedContent)
        except Exception as e:
            print(f"Error: Failed to save rendered template to {path}: {e}")
            return False

        return True

    def render(self, **kwargs):
        """
        Render the template with given variables
        """
        return self._template.render(**kwargs)

    def comments(self, keys: list[str] = None) -> list[str]:
        """
        Return all comments in template source if keys is None
        If keys is not None, return comments which contain any key
        :param keys: List of keys to search for in comments (None for all comments)
        :return: List of comments
        """
        # Find all Jinja2 comments {# ... #}
        comment_pattern = r'\{#\s*(.*?)\s*#\}'
        all_comments = re.findall(comment_pattern, self.source, re.DOTALL)

        if keys is None:
            return all_comments

        # Filter comments that contain any of the keys
        filtered_comments = []
        for comment in all_comments:
            for key in keys:
                if key.lower() in comment.lower():
                    filtered_comments.append(comment)
                    break  # Add comment only once even if it contains multiple keys

        return filtered_comments

    @property
    def sourceWithoutComments(self):
        """
        Return the template source without any comments
        """
        # Remove all Jinja2 comments {# ... #} from the source
        comment_pattern = r'\{#\s*.*?\s*#\}'
        return re.sub(comment_pattern, '', self.source, flags=re.DOTALL).lstrip()

    def config(self, data: dict = None) -> dict:
        """
        if data == None:
            get config in source
        else:
            set config to source        
        """
        print(f"config: {data}")
        if data == None:
            self._getConfig()
        else:
            self._setConfig(data)

        return self._config

    def _getConfig(self):
        self._config = DefaultTemplateConfig.copy()
        match = self.comments()

        for k, v in [item.split("=") for item in match if "=" in item]:
            self._config[k.strip()] = v.strip()

        print(f"getConfig: {self._config}")

    def _setConfig(self, data: dict):
        for key in data.keys():
            self._config[key] = data[key]

        print("self._config:", self._config)
        self.source = "\n".join(
            [f"{{# {key}={self._config[key]} #}}" for key in self._config.keys()]) + "\n\n" + self.sourceWithoutComments.lstrip()

        return self._config

    def outputPath(self, root: str = None) -> str:
        """
        Get output path from config or use default
        :param root: Root path to use instead of config value (optional)
        :return: Output path
        """
        conf = self.config()
        root = root or conf.get(ConfigKeys.ROOT_PATH.value)
        return os.path.join(root, conf.get(ConfigKeys.TARGET_PATH.value))

    def outputFilePath(self, root: str = None) -> str:
        return os.path.join(self.outputPath(root=root), os.path.basename(self.filePath))

    def name(self):
        if self.filePath is None:
            return None

        return os.path.basename(self.filePath)


def GetVariables(source: str):
    """get variables from template source"""
    return meta.find_undeclared_variables(Env.parse(source))

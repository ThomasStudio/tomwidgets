from __future__ import annotations
from ast import Module
import importlib
import re
import os
import shutil
from typing import *
import unittest
from importlib import machinery

import jinja2
from jinja2 import (
    Environment,
    FileSystemLoader,
    meta,
    nodes,
    environment,
)

from jinja2.defaults import (
    BLOCK_END_STRING,
    BLOCK_START_STRING,
    COMMENT_END_STRING,
    COMMENT_START_STRING,
    KEEP_TRAILING_NEWLINE,
    LSTRIP_BLOCKS,
    TRIM_BLOCKS,
    VARIABLE_END_STRING,
    VARIABLE_START_STRING,
)


# region variables
TemplatePath = "templates"
DefaultConfigFile = "resource/default_config.py"

Env = Environment(loader=FileSystemLoader(searchpath="./"))

ConfigFileName = "_config.py"

# endregion

# region class


class Templates:
    """
    import template file
    load tempate file
    generate code by template
    modify template file
    preview generated code
    generate file at target path
    modify exists file
    """

    @staticmethod
    def LoadTemplates(path=TemplatePath) -> list[Templates]:
        result = []
        if not os.path.exists(path):
            return result

        for f in os.listdir(path):
            p = os.sep.join([path, f])
            if os.path.isdir(p):
                result.append(Templates(p))

        return result

    @staticmethod
    def CreateTemplatesFolder(folder: str) -> bool:
        if not Templates.CheckFolderName(folder):
            return False

        curFolders = os.listdir(TemplatePath)
        if folder in curFolders:
            return True

        os.mkdir(os.sep.join([TemplatePath, folder]))

        shutil.copyfile(DefaultConfigFile, os.sep.join(
            [TemplatePath, folder, ConfigFileName]))

        return True

    @staticmethod
    def CheckFolderName(folder: str) -> bool:
        if folder is None or len(folder.strip()) == 0:
            return False

        folder = folder.strip()

        result = re.match(r"^[a-zA-Z]+[a-zA-Z0-9]*", folder)

        if result is None:
            return False

        if result.group(0) == folder:
            return True

        return False

    @staticmethod
    def CheckFileName(name: str) -> bool:
        if name is None or len(name.strip()) == 0:
            return False

        name = name.strip()

        if name.endswith("."):
            return False

        if ".." in name:
            return False

        result = re.match(r"^[a-zA-Z]+[a-zA-Z0-9\.]*", name)

        if result is None:
            return False

        if result.group(0) == name:
            return True

        return False

    @staticmethod
    def DeleteTemplatesFolder(folder: str):
        target = os.sep.join([TemplatePath, folder])

        if not os.path.exists(target):
            return True

        shutil.rmtree(target)

        return True

    def __init__(self, path: str) -> None:
        self.init(path)

        self.loadTemplate()

    def init(self, path: str):
        self.path = path
        self.name = os.path.basename(path)
        self.templates: list[TemplateJ2] = []

        self.configFile: TemplateJ2 = None
        self.configs: dict[str, TemplateJ2] = dict()
        self.paths: list[TemplateJ2] = []

        self.variables = dict()

    def loadTemplate(self):
        if not os.path.exists(self.path):
            self.init(self.path)
            return

        for f in os.listdir(self.path):
            p = os.sep.join([self.path, f])
            if os.path.isfile(p):
                if f.lower() == ConfigFileName.lower():
                    self.configFile = Template(Path(p))
                    self.variables.update({
                        k: "" for k in self.configFile.variables()
                    })
                else:
                    t = Template(Path(p))
                    self.templates.append(t)
                    self.variables.update({
                        k: "" for k in t.variables()
                    })

        if self.configFile is not None:
            config = LoadModule(self.configFile.filename)
            self.loadConfig(config)

    def loadConfig(self, config):
        if config is None:
            return

        if hasattr(config, "templates"):
            templates = config.templates

            for k in templates:
                self.configs[k] = Template(templates[k], k)

        if hasattr(config, "paths"):
            paths = config.paths
            for k in paths:
                self.paths.append(Template(paths[k], k))

    def dump(self, maxSourceLen=65):
        """
        maxSourceLen :
            <=0, print all source
            > 0, print only maxSourceLen chars
        """

        maxSourceLen = 65

        def getSource(source: str):
            if maxSourceLen <= 0 or len(source) < maxSourceLen:
                return source
            else:
                return f"======== show first {maxSourceLen} chars of source ========\n{source[:maxSourceLen]}"

        def fetchConfigTemplates():
            if self.configFile is None:
                return ""

            source = self.configFile.source.strip()

            id1 = source.find('"""')
            id1 = source.find('"""', id1 + 3)
            id2 = source.find("templates", id1)

            return source[id2:].strip()

        output = "\n"

        output += f"\nTemplates({self.path}) dump"
        output += f"\n\n    ======= File templates ========"
        for x in self.templates:
            output += f"""
    file: {x.filename}
        variables:{x.variables()}
        source length : {len(x.source)}
        source: {getSource(x.source)}"""

        output += f"\n\n    ======== Config file ========"
        if self.configFile is None:
            output += "\nNo Config file"
        else:
            configSource = fetchConfigTemplates()
            output += f"""
        file: {self.configFile.filename}
            source length : {len(configSource)}
            source: {getSource(configSource).strip()}
        """

        output += f"\n    ======== Configuration templates ========"
        for key in self.configs.keys():
            x = self.configs[key]
            output += f"""
    key: {x.key}
        variables:{x.variables()}
        source length : {len(x.source)}
        source: {getSource(x.source)}"""

        output += "\n"

        print(output)

        return output

    def allVariables(self) -> dict:
        """get all variables, include templates in config file"""
        for key in self.configs.keys():
            t = self.configs[key]
            self.variables.update(
                {
                    t.key: t.render(self.variables)
                })
        return self.variables

    def createTemplate(self, fileName: str, checkName=True) -> bool:
        if checkName and not Templates.CheckFileName(fileName):
            return False

        fileName = fileName.strip()
        if self.hasFile(fileName):
            return False

        path = os.sep.join([TemplatePath, self.name, fileName])

        with open(path, "w", encoding="utf-8") as f:
            f.close()

        self.reload()

        return True

    def hasFile(self, fileName: str):
        if fileName is None:
            return False
        fileName = fileName.strip()

        if len(fileName) == 0:
            return False

        fileList = [x.file() for x in self.templates if x.isFile]

        if fileName in fileList:
            return True
        else:
            return False

    def deleteTemplateFile(self, template: TemplateJ2) -> bool:
        if not template.isFile:
            return False

        if os.path.exists(template.filename):
            os.remove(template.filename)

        self.reload()
        return True

    def reload(self):
        self.init(self.path)
        self.loadTemplate()

    def get(self, fileName: str) -> TemplateJ2:
        fileDict = {x.file(): x for x in self.templates if x.isFile}
        if fileName in fileDict.keys():
            return fileDict[fileName]

        return None

    def renderPath(self, fileName: str):
        if fileName is None or len(fileName.strip()) == 0:
            return None

        fileName = fileName.strip()

        for p in self.paths:
            if p.key == fileName:
                return p.render(self.variables).replace("/", os.sep).replace("\\", os.sep)

        return fileName


class TemplateJ2(jinja2.Template):
    """
    source :
        original tempate string
    key :
        key of the template, it can be used as file template variable input
    isFile :
        True if it is a template file
        False if it is a tempalte string
    """

    @staticmethod
    def Template(sourceOrPath: str, key: str = None) -> TemplateJ2:
        if os.path.exists(sourceOrPath):
            temp = TemplateJ2.GetTemplateByPath(sourceOrPath)
        else:
            temp = TemplateJ2.GetTemplateBySource(sourceOrPath)

        if temp:
            temp.key = key

        return temp

    @staticmethod
    def GetTemplateBySource(source: str) -> TemplateJ2:
        temp = TemplateJ2(source)
        temp.init(source=source, isFile=False)
        return temp

    @staticmethod
    def GetTemplateByPath(path: str) -> TemplateJ2:
        try:
            source = GetContent(path)
            temp = TemplateJ2(source)
            temp.init(source=source, isFile=True, filename=path)
            return temp
        except Exception as e:
            print("GetTemplateByPath:", e)
            return None

    def init(self, source: str, isFile: bool = False, filename: str = None, key: str = None) -> None:
        self.source = source
        self.isFile = isFile
        self.filename = filename
        self.key = key

    def variables(self) -> dict:
        return GetVariables(self.source)

    def saveRenderResult(self, path: str, **kwargs):
        with open(path, "w", encoding="utf-8") as f:
            self.stream(kwargs).dump(f)

    def updateTemplate(self, source: str = None) -> bool:
        if not os.path.exists(self.filename) or source is None:
            return False

        self.source = source

        with open(self.filename, "w", encoding="utf-8") as f:
            f.write(self.source)
            f.close()

        return True

    def file(self) -> str:
        """get base filename

        Returns:
            str: base filename
        """
        return os.path.basename(self.filename)

    def isConfigFile(self) -> bool:
        return self.file() == ConfigFileName

# endregion


# region function


def Template(sourceOrPath: str, key: str = None) -> TemplateJ2:
    return TemplateJ2.Template(sourceOrPath, key)


def Path(p: str):
    """The path in Jinja2 only accept / as separator"""
    return p.replace("\\", "/")


def GetVariables(source: str):
    """get variables from template source"""
    return meta.find_undeclared_variables(Env.parse(source))


def GetContent(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


def LoadModule(path: str):
    """load a python file dynamic

    Args:
        path (str): the file path of target

    Returns:
        module: the object load from target file, None if the target is not exists or any other exception
    """
    if path is None or not os.path.exists(path):
        return None

    try:
        loader = machinery.SourceFileLoader("module", path)
        spec = importlib.util.spec_from_loader("module", loader)
        module = importlib.util.module_from_spec(spec)
        loader.exec_module(module)
        return module
    except Exception as e:
        print(e)

    return None


# endregion


# region unit Test


class TestTemplate(unittest.TestCase):
    def testTemplate(self):
        temp1 = Template("Hello {{name}}")
        print(temp1.render())
        print(temp1.render(name="Tom"))
        print(temp1.source)
        print(temp1.filename)
        print(f"isFile = {temp1.isFile}")
        print("name", temp1.name)
        temp1.name = "helloName"
        print("name", temp1.name)

        self.assertEqual(temp1.render(), "Hello ")
        self.assertEqual(temp1.render(name="hello"), "Hello hello")

    def testTemplate2(self):
        TEMPLATE_FILE = "templates/test/test.py"
        temp = Template(TEMPLATE_FILE)
        print(temp.render())
        print(temp.render(aaaa="aaaa"))
        print(temp.source)
        print(temp.filename)
        print("name", temp.name)
        print(f"isFile = {temp.isFile}")

    def testTemplate3(self):
        TEMPLATE_FILE = "templates/test/test.py"
        temp = Env.get_template(TEMPLATE_FILE)
        print(temp.render())
        print(temp.render(aaaa="aaaa"))
        print(temp.filename)
        print("name", temp.name)

    def testTemplateLoader(self):
        TEMPLATE_FILE = "templates/test/test.py"
        template = Template(TEMPLATE_FILE)

        print(template.render(aaaa="aaaa"))
        print(template.render(bbbb="bbbb"))
        print(template.render(aaaa="aaaa", bbbb="bbbb"))

        self.assertIsNotNone(template.render(aaaa="aaaa"))
        self.assertIsNotNone(template.render(bbbb="bbbb"))
        self.assertIsNotNone(template.render(aaaa="aaaa", bbbb="bbbb"))

    def testGetVariables(self):
        temp = Template("Hello {{name}}")

        print("template", type(temp))
        print("variables:", temp.variables())

        self.assertIsNotNone(temp.variables())
        self.assertTrue(len(temp.variables()) > 0)

    def testGetVariables2(self):
        TEMPLATE_FILE = "templates/test/test.py"
        temp = Template(TEMPLATE_FILE)

        print("template", type(temp))

        print("variables:", temp.variables())

        self.assertIsNotNone(GetVariables(temp))

    def testGetSource(self):
        TEMPLATE_FILE = "templates/test/test.py"
        temp1 = Template(TEMPLATE_FILE)

        print(temp1.source)
        self.assertIsNotNone(temp1.source)

        source = """ test {{name1}}, {{name2}}    """
        temp2 = Template(source)

        print(temp2.source)
        self.assertIsNotNone(temp2.source)

    def testTemplates(self):
        tempsList = Templates.LoadTemplates()

        for x in tempsList:
            x.dump()

        self.assertIsNotNone(tempsList)
        self.assertTrue(len(tempsList) > 0)

    def testLoadModule(self):
        module = LoadModule("templates/test/_config.py")
        print(module.templates, type(module))

    def testSaveFile(self):
        temp = Template("hello {{name}}")
        temp.saveRenderResult(
            "d:\\temp\\testTemplate.txt", name="helloaasddfasd")

    def testUpdateTemplate(self):
        temp = Template("templates/test/test.py")
        temp.updateTemplate("hello {{testUpdateTemplate}} 111 222")

    def testFolderName(self):
        testList = [
            "123",
            "1231231asdf",
            "1231231A",
            "_a1231",
            "_1231",
            "a1?231",
            "a12,31",
            "AAAA123,",
            "aaaa",
            "AAAA",
            "AAAA123",
            "a1231231A",
        ]

        for x in testList:
            print(x, "  ", Templates.CheckFolderName(x))

    def testFolderName(self):
        testList = [
            "123",
            "1231231asdf",
            "1231231A",
            "_a1231",
            "_1231",
            "a1?231",
            "a12,31",
            "AAAA123,",
            "aaaa..a",
            "aaaa.a.",
            "aaaa.a.b",
            "AAAA...a.",
            "AAAA123..a..",

            "aaaa",
            "AAAA",
            "AAAA123",
            "a1231231A",

            "AAAA123.a",
            "a1231231A123",
        ]

        for x in testList:
            print(x, "  ", Templates.CheckFileName(x))


# endregion

if __name__ == "__main__":
    # unittest.main()
    # TestTemplate().testTemplates()
    # TestTemplate().testUpdateTemplate()
    TestTemplate().testFolderName()

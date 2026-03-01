"""configuration file management class

tools.ini format:

[win]
dir = dir
explorer = explorer .
ip = ipconfig

[python]
create_env = python -m venv .venv
install = pip install {package_name}
activate = .venv\Scripts\activate

settings.ini format:

[folder]
cmdtool = D:\Mywork\python\CmdTool
temp = D:\temp

[window]
toolwin_position = 0,0
basewin_position = 737,1841

"""
import sys
import os
import datetime
import configparser


ToolsConfigFile = 'tools.ini'
SettingsFile = 'settings.ini'


class Config(object):
    def __init__(self, configFile=ToolsConfigFile):
        """Initialize Config object with specified configuration file"""
        self.configFile = configFile
        if not os.path.exists(self.configFile):
            print(f"Config file not found: {self.configFile}")

        self.config = configparser.ConfigParser()
        self.config.read(configFile)

    def sections(self):
        """Get all sections"""
        return self.config.sections()

    def options(self, section):
        """Get all options under specified section"""
        try:
            return self.config.options(section)
        except configparser.NoSectionError:
            return []

    def has_option(self, section, option):
        """Check if specified section has specified option"""
        return section in self.config and option in self.config[section]

    def items(self, section):
        """Get all key-value pairs under specified section"""
        try:
            return self.config.items(section)
        except configparser.NoSectionError:
            return []

    def get(self, section, option, default=None):
        """Get the value of configuration item, return default if not exist"""
        try:
            return self.config.get(section, option)
        except (configparser.NoSectionError, configparser.NoOptionError):
            return default

    def getint(self, section, option, default=None):
        """Get integer type configuration item"""
        try:
            return self.config.getint(section, option)
        except (configparser.NoSectionError, configparser.NoOptionError, ValueError):
            return default

    def getboolean(self, section, option, default=None):
        """Get boolean type configuration item"""
        try:
            return self.config.getboolean(section, option)
        except (configparser.NoSectionError, configparser.NoOptionError, ValueError):
            return default

    def getfloat(self, section, option, default=None):
        """Get float type configuration item"""
        try:
            return self.config.getfloat(section, option)
        except (configparser.NoSectionError, configparser.NoOptionError, ValueError):
            return default

    def _get_list(self, section, option, converter=str, default=None):
        """General list parsing method"""
        value = self.get(section, option)
        if value is None:
            return default or []
        try:
            return [converter(item.strip()) for item in value.split(',')]
        except ValueError:
            return default or []

    def getlist(self, section, option, default=None):
        """Get string list"""
        return self._get_list(section, option, converter=str, default=default)

    def getlistint(self, section, option, default=None):
        """Get integer list"""
        return self._get_list(section, option, converter=int, default=default)

    def getlistfloat(self, section, option, default=None):
        """Get float list"""
        return self._get_list(section, option, converter=float, default=default)

    def getlistbool(self, section, option, default=None):
        """Get boolean list"""
        def bool_converter(value):
            return value.lower() in ('true', 'yes', '1', 'y')
        return self._get_list(section, option, converter=bool_converter, default=default)

    def getlistdatetime(self, section, option, default=None):
        """Get datetime list"""
        def datetime_converter(value):
            return datetime.datetime.strptime(value.strip(), '%Y-%m-%d %H:%M:%S')
        return self._get_list(section, option, converter=datetime_converter, default=default)

    def write(self):
        """Write configuration to file"""
        try:
            with open(self.configFile, 'w', encoding='utf-8') as f:
                self.config.write(f)
            return True
        except Exception as e:
            print(f"Failed to write configuration file: {e}", file=sys.stderr)
            return False

    def add_section(self, section):
        """Add section"""
        if not self.config.has_section(section):
            self.config.add_section(section)
        return self.write()

    def add_option(self, section, option, value):
        """Add or modify configuration item"""
        if not self.config.has_section(section):
            self.config.add_section(section)
        self.config.set(section, option, str(value))
        return self.write()

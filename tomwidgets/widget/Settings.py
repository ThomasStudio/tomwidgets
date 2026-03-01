import os
from .Config import Config
from tkinter import Misc, Widget
from .FolderBar import FolderBar


class Settings(Misc):
    """
        [folder]
        python = D:/temp/python
        temp = D:/temp

        [window]
        basewin_position = 1135,1886
    """

    def __init__(self, settingsFile: str, parent: Widget):
        self.settingsFile = settingsFile

        if not os.path.exists(settingsFile):
            self.createSettingsFile()

        self.settings = Config(settingsFile)
        self.win = parent.winfo_toplevel()

        if hasattr(self, 'asWin') and self.asWin:
            self.isWin = True
        else:
            self.isWin = False

        if self.isWin:
            self.win.protocol("WM_DELETE_WINDOW", self.onClose)

        self.folderBars = []
        self.folders = {}
        self.getFolders()

        self.loadPosition()

    def onClose(self):
        self.savePosition()
        self.win.destroy()

    def savePosition(self):
        class_name = self.__class__.__name__
        if not self.isWin:
            return

        # settings.ini is share between many windows, reload it before save it
        self.reloadSettings()

        win = self.win

        print(f"save position {class_name}:{win.winfo_x()},{win.winfo_y()}")
        self.settings.add_option('window', f'{class_name}_position',
                                 f"{win.winfo_x()},{win.winfo_y()}")
        self.settings.write()

    def loadPosition(self):
        class_name = self.__class__.__name__
        if not self.isWin:
            return

        print(f"load position {class_name}")

        pos = self.settings.get('window', f'{class_name}_position',)
        if pos:
            x, y = map(int, pos.split(','))
            self.win.geometry(f"+{x}+{y}")

    def reloadSettings(self, settingsFile: str = None):
        """Reload configuration"""
        self.settingsFile = settingsFile or self.settingsFile
        self.settings = Config(self.settingsFile)

    def getFolders(self) -> dict:
        """Get folders from settings"""
        folders = self.settings.items('folder')
        if folders:
            self.folders = dict(folders)

        for bar in self.folderBars:
            bar.setFolderList([self.folders[f] for f in self.folders])

        self.event_generate('<<FoldersUpdated>>', when='tail')

    def createFolderBar(self, master, title="Folders") -> FolderBar:
        import os
        parent = master or self.master
        currentFolder = os.getcwd()

        folders = [self.folders[f] for f in self.folders]
        if currentFolder not in folders:
            folders = [currentFolder]+folders

        bar = FolderBar(parent, title=title, folders=[])
        bar.setFolderList(folders)

        self.folderBars.append(bar)
        return bar

    def createSettingsFile(self, settingsFile: str = None):
        """
        Create a default settings.ini file with initial configuration.

        Args:
            settingsFile: Path to the settings file (defaults to self.settingsFile)
        """
        if settingsFile is None:
            settingsFile = self.settingsFile

        # Create default settings configuration
        default_settings = """# Application Settings Configuration
# This file contains application settings and window positions.

[folder]
c = c:/

[window]
# Window position settings for different application windows
# Format: window_name_position = x,y
toolwin_position = 100,100
cmdwin_position = 300,300
"""

        # Create directory if it doesn't exist
        settings_dir = os.path.dirname(settingsFile)
        if settings_dir and not os.path.exists(settings_dir):
            os.makedirs(settings_dir)

        # Write the default settings configuration to file
        with open(settingsFile, 'w', encoding='utf-8') as f:
            f.write(default_settings)

        print(f"Created default settings file: {settingsFile}")

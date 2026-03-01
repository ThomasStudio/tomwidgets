from ..widget.BaseWin import BaseWin
from ..widget.basic.CheckBox import CheckBox
from ..widget.basic.OptionMenu import OptionMenu


class Urls(BaseWin):
    def __init__(self, master=None, title="Urls", **kwargs):
        super().__init__(master=master, title=title, showFolderBar=False, **kwargs)

        if self.systemTitleVisible:
            self.toggleSystemTitle()

        if not self.isOnTop:
            self.toggleOnTop()
            
        self.titleBar.hideAllWidgets()

        # Store URLs from configuration
        self.urlDict = {}

        # Currently selected URL
        self.selectedUrl = ""

        # Private mode flag
        self.privateMode = True

        # Load URLs from configuration
        self.loadUrlsFromConfig()

        # Create the UI components
        self.createUi()

    def getCmds(self):
        cmds = super().getCmds()
        cmds.insert(0, None)
        return cmds

    def loadUrlsFromConfig(self):
        from ..widget.Config import Config
        try:
            # Read the tools.ini file
            config = Config("tools.ini")

            # Check if url section exists
            if 'url' in list(config.sections()):
                items = config.items('url')
                items.reverse()
                self.urlDict = {name: url for name, url in items}

            for key in self.urlDict.keys():
                self.addMenuCommand(
                    key, lambda k=key: self.onUrlSelected(k), prepend=True)

        except Exception as e:
            return

    def createUi(self):
        self.createUrlSelector(self.topFrame)
        self.createPrivateCheckbox(self.topFrame)

    def createUrlSelector(self, parent):
        urlNames = list(self.urlDict.keys())

        # Create OptionMenu
        self.urlOptionMenu = OptionMenu(
            parent, values=urlNames, command=self.onUrlSelected)
        self.urlOptionMenu.pack(side="left")

    def createPrivateCheckbox(self, parent):
        box = self.privateCheckbox = CheckBox(parent, text="pri")
        box.pack(side="left")
        box.select()

        # Bind checkbox change event
        box.configure(command=self.onPrivateModeChanged)

    def onUrlSelected(self, selectedName):
        """Handle URL selection change."""
        if selectedName in self.urlDict:
            self.selectedUrl = self.urlDict[selectedName]
            self.openUrl(self.selectedUrl)

    def onPrivateModeChanged(self):
        """Handle private mode checkbox change."""
        self.privateMode = self.privateCheckbox.get()

    def fetchUrl(self, url):
        """ fetch url from string """
        idx = url.find("://")
        if idx == -1:
            return url

        return url[idx+3:]

    def openUrl(self, url):
        url = self.fetchUrl(url)

        if not url:
            return

        try:
            import subprocess

            cmd = f"start msedge {url}"

            if self.privateMode:
                cmd += " --inprivate"

            try:
                # Try to open with specific browser in private mode
                subprocess.Popen(cmd, shell=True)
                return
            except:
                return

        except Exception as e:
            return

    def getUrlCount(self):
        """Get the number of URLs loaded from config."""
        return len(self.urlDict)

    def getUrlNames(self):
        """Get the list of URL names."""
        return list(self.urlDict.keys())

    def getUrlByName(self, name):
        """Get URL by name."""
        return self.urlDict.get(name, "")


def createUrls(master=None, title="URL Manager", **kwargs):
    """Convenience function to create Urls instance."""
    return Urls(master=master, title=title, **kwargs)


if __name__ == "__main__":
    # Test the Urls tool
    import tkinter as tk

    root = tk.Tk()
    root.title("URL Manager Test")
    root.geometry("400x300")

    urlsTool = Urls(root)
    urlsTool.pack(fill=tk.BOTH, expand=True)

    root.mainloop()

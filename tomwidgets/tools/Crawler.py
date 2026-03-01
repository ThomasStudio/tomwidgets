import re
from urllib.parse import urlparse

from ..widget.BaseWin import BaseWin
from ..widget.InputBar import InputBar
from ..widget.BtnBar import BtnBar, BtnConfig
from .TextTwo import TextTwo


class Crawler(BaseWin):
    def __init__(self, master=None, title="Web Crawler",
                 showTitleBar=True, showFolderBar=False,
                 asWin=True, settingsFile='settings.ini', **kwargs):
        super().__init__(master, title=title, showTitleBar=showTitleBar,
                         showFolderBar=showFolderBar, asWin=asWin,
                         settingsFile=settingsFile, **kwargs)

        # Store crawler data
        self.currentUrl = ""
        self.downloadedHtml = ""
        self.searchPattern = ""
        self.searchResults = []

        # Create UI components
        self.createUi()

        # Bind events
        self.bindEvents()

    def getCmds(self):
        # Get the base menu from parent class
        baseMenu = super().getCmds()

        # Add Crawler specific menu
        crawlerMenu = [
            ("Crawler", [
                ("Download Current URL", self.downloadHtml),
                ("Search in Downloaded", self.searchInDownloaded),
                ("Clear All", self.clearAll),
                ("Copy URL", self.copyCurrentUrl),
                ("Paste URL", self.pasteToUrlBar)
            ])
        ]

        # Insert Crawler menu at the beginning
        return crawlerMenu + baseMenu

    def createUi(self):
        # Create URL input bar
        self.createUrlBar()

        # Create search input bar
        self.createSearchBar()

        # Create button bar
        self.createButtonBar()

        # Create TextTwo for displaying content
        self.createTextTwo()

    def createUrlBar(self):
        self.urlBar = InputBar(self.contentFrame, title="URL:", default="https://")
        self.urlBar.grid(row=0, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

        # Configure grid for proper resizing
        self.contentFrame.grid_columnconfigure(0, weight=1)

    def createSearchBar(self):
        self.searchBar = InputBar(self.contentFrame, title="RE find:")
        self.searchBar.grid(row=1, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

    def createButtonBar(self):
        # Define button configurations
        btnConfigs = [
            BtnConfig("Download", self.downloadHtml, tooltip="Download HTML from URL"),
            BtnConfig("Search", self.searchInDownloaded, tooltip="Search with regex in downloaded content"),
            BtnConfig("Clear", self.clearAll, tooltip="Clear all content"),
            BtnConfig("Copy URL", self.copyCurrentUrl, tooltip="Copy current URL to clipboard"),
            BtnConfig("Validate URL", self.validateUrl, tooltip="Validate URL format")
        ]

        # Create button bar
        self.buttonBar = BtnBar(self.contentFrame, pady=3, padx=3)
        self.buttonBar.addBtns(btnConfigs)
        self.buttonBar.grid(row=2, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

    def createTextTwo(self):
        # Create TextTwo instance (as frame, not window)
        tt = self.textTwo = TextTwo(self.contentFrame, title="Content Viewer", 
                              showTitleBar=False, showFolderBar=False, asWin=False)
        tt.grid(row=3, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)

        # Configure grid weights for proper resizing
        self.contentFrame.grid_rowconfigure(3, weight=1)
        
        tt.searchBar.hide()
        tt.replaceBar.hide()
        tt.horizontalBtnBar.hide()

    def bindEvents(self):
        # Bind return key for URL input
        self.urlBar.bindReturn(self.onUrlEnter)
        self.searchBar.bindReturn(self.onSearchEnter)

    def onUrlEnter(self, event=None):
        self.downloadHtml()

    def onSearchEnter(self, event=None):
        self.searchInDownloaded()

    def downloadHtml(self):
        import requests

        url = self.urlBar.getValue().strip()
        
        if not url:
            print("[!] Please enter a valid URL")
            return

        if not self.validateUrlFormat(url):
            print("[!] Invalid URL format")
            return

        try:
            print(f"[>] Downloading from: {url}")
            
            # Set headers to mimic a browser
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            
            self.downloadedHtml = response.text
            self.currentUrl = url
            
            # Display in TextTwo T1 area
            self.textTwo.setT1Text(self.downloadedHtml)
            
            print(f"[+] Downloaded {len(self.downloadedHtml)} characters")
            
        except requests.exceptions.RequestException as e:
            errorMsg = f"[-] Download failed: {str(e)}"
            print(errorMsg)
            self.textTwo.setT1Text(errorMsg)
        except Exception as e:
            errorMsg = f"[-] Unexpected error: {str(e)}"
            print(errorMsg)
            self.textTwo.setT1Text(errorMsg)

    def searchInDownloaded(self):
        if not self.downloadedHtml:
            print("[!] No downloaded content to search")
            return

        searchPattern = self.searchBar.getValue().strip()
        if not searchPattern:
            print("[!] Please enter a search pattern")
            return

        try:
            print(f"[>] Searching for pattern: {searchPattern}")
            
            # Compile regex pattern
            pattern = re.compile(searchPattern, re.IGNORECASE | re.MULTILINE)
            
            # Find all matches
            matches = pattern.finditer(self.downloadedHtml)
            self.searchResults = list(matches)
            
            if not self.searchResults:
                resultText = "No matches found"
                print("[-] No matches found")
            else:
                # Create formatted results
                resultLines = []
                resultLines.append(f"Found {len(self.searchResults)} matches:")
                resultLines.append("-" * 50)
                
                for i, match in enumerate(self.searchResults, 1):
                    matchText = match.group()
                    # Truncate long matches
                    if len(matchText) > 100:
                        matchText = matchText[:100] + "..."
                    
                    resultLines.append(f"Match {i} (position {match.start()}-{match.end()}):")
                    resultLines.append(f"  {matchText}")
                    resultLines.append("")
                
                resultText = "\n".join(resultLines)
                print(f"[+] Found {len(self.searchResults)} matches")
            
            # Display results in TextTwo T2 area
            self.textTwo.setT2Text(resultText)
            
        except re.error as e:
            errorMsg = f"[-] Invalid regex pattern: {str(e)}"
            print(errorMsg)
            self.textTwo.setT2Text(errorMsg)
        except Exception as e:
            errorMsg = f"[-] Search error: {str(e)}"
            print(errorMsg)
            self.textTwo.setT2Text(errorMsg)

    def clearAll(self):
        self.urlBar.setValue("")
        self.searchBar.setValue("")
        self.textTwo.clearT1Text()
        self.textTwo.clearT2Text()
        self.textTwo.clearCompareColor()
        self.downloadedHtml = ""
        self.searchResults = []
        print("[*] All content cleared")

    def copyCurrentUrl(self):
        if self.currentUrl:
            self.clipboard_clear()
            self.clipboard_append(self.currentUrl)
            print(f"[*] URL copied to clipboard: {self.currentUrl}")
        else:
            print("[!] No URL to copy")

    def pasteToUrlBar(self):
        try:
            clipboardContent = self.clipboard_get()
            self.urlBar.setValue(clipboardContent)
            print(f"[*] Pasted to URL bar: {clipboardContent}")
        except:
            print("[!] No content in clipboard")

    def validateUrl(self):
        url = self.urlBar.getValue().strip()
        if self.validateUrlFormat(url):
            print("✅ URL format is valid")
        else:
            print("❌ URL format is invalid")

    def validateUrlFormat(self, url):
        try:
            result = urlparse(url)
            return all([result.scheme, result.netloc])
        except:
            return False

    def getCurrentUrl(self):
        return self.currentUrl

    def getDownloadedHtml(self):
        return self.downloadedHtml

    def getSearchResults(self):
        return self.searchResults
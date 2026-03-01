# region metadata
__version__ = "1.1.0"
__author__ = "Thomas Mei"
__description__ = "A lot of complext widgets and theme tool"

# endregion metadata

# region model
from .model import Cmd
from .model import CmdHistory
from .model import Emoji
from .model import Segoe
# endregion model


# region tools
from .tools import Crawler
from .tools import CodeTool
from .tools import IconTool
from .tools import PyInstall
from .tools import RETool
from .tools import TextTwo
from .tools import Urls
from .tools import UrlTool
# endregion tools

# region util
from .util import ClassUtil, SingletonBase, SingletonMeta
from .util import EventBus
from .util import ModuleUtil
# endregion util


# region widget

from .widget import BaseWin
from .widget import BtnBar, BtnConfig
from .widget import CmdEditor
from .widget import CmdMgr
from .widget import CmdWin
from .widget import CodeWin
from .widget import ComboBar
from .widget import Config
from .widget import ConfigWin
from .widget import DictView, createDictView
from .widget import FolderBar
from .widget import InputBar
from .widget import InputBox
from .widget import MenuBtn, createMenuButton
from .widget import InfoBox, showMessageBox
from .widget import OptionBar
from .widget import PopMenu
from .widget import Settings
from .widget import Stapling
from .widget import TextBar
from .widget import Theme, CTkOptionMenu
from .widget import TitleBar, createTitleBar
from .widget import ToolWin
from .widget import VisibleBtn
from .widget import WinMgr
from .widget import WrapBox
from .widget import WrapBtnBar, WrapBtnConfig


from .widget import Button
from .widget import CheckBox
from .widget import ComboBox
from .widget import Entry
from .widget import EventHandler
from .widget import Font
from .widget import Frame
from .widget import Image
from .widget import InputDialog
from .widget import Label
from .widget import OptionMenu
from .widget import ProgressBar
from .widget import RadioButton
from .widget import ScrollableFrame
from .widget import Scrollbar
from .widget import SegmentedButton
from .widget import Slider
from .widget import Switch
from .widget import Tabview
from .widget import Textbox
from .widget import Tk
from .widget import Toplevel

# endregion widget
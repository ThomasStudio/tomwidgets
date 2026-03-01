from customtkinter import ThemeManager, AppearanceModeTracker
import customtkinter as ctk
from enum import Enum


class ColorTheme(Enum):
    Gold = "theme_gold.json"
    Blue = "blue"
    Green = "green"
    DarkBlue = "dark-blue"


class Mode(Enum):
    Dark = 'dark'
    Light = 'light'
    System = 'system'


class Theme(ThemeManager):
    currentMode: str = Mode.Dark.value
    currentColorTheme: str = ColorTheme.Gold.value

    @staticmethod
    def init(mode=None, theme=None, fontSize=20):
        if isinstance(mode, Mode):
            mode = mode.value

        if isinstance(theme, ColorTheme):
            theme = theme.value

        if mode is None:
            mode = Theme.currentMode
        else:
            Theme.currentMode = mode

        if theme is None:
            theme = Theme.currentColorTheme
        else:
            Theme.currentColorTheme = theme

        print(f"Initializing Theme: mode={mode}, theme={theme}")

        ctk.set_appearance_mode(mode)
        ctk.set_default_color_theme(Theme.themePath(theme))
        Theme.changeFontSize(fontSize)

    @staticmethod
    def modeList():
        return [(item.name, item.value) for item in Mode]

    @staticmethod
    def colorThemeList():
        return [(item.name, item.value) for item in ColorTheme]

    @staticmethod
    def themePath(theme=ColorTheme.Gold):
        if theme in Theme._built_in_themes:
            return theme

        from os import path

        return path.join(path.dirname(path.abspath(__file__)), "theme", theme)

    @staticmethod
    def mode():
        return AppearanceModeTracker.appearance_mode

    @staticmethod
    def get(attr):
        mode = Theme.mode()
        name = type(attr).__name__

        if isinstance(attr, CTkFont):
            return Theme.theme[name]

        values = Theme.theme[name][attr.value]

        if isinstance(values, (list, tuple, dict)):
            return values[mode]
        else:
            return values

    @staticmethod
    def font():
        return Theme.get(CTkFont.System)

    @staticmethod
    def fg():
        return "gold"

    @staticmethod
    def bg():
        return "gray10"

    @staticmethod
    def changeFontSize(size: int):
        Theme.theme['CTkFont']['size'] = size

    @staticmethod
    def changeFont(font={'size': 20, 'family': 'Arial', 'weight': 'bold'}):
        Theme.theme['CTkFont'] = font

    @staticmethod
    def defaultTextColor():
        if ctk.get_appearance_mode().lower() == Mode.Dark:
            return "white"
        else:
            return "black"


class Main(Enum):
    fg = "fg"
    bg = "bg"


class CTk(Enum):
    fg_color = "fg_color"


class CTkToplevel(Enum):
    fg_color = "fg_color"


class CTkFrame(Enum):
    corner_radius = "corner_radius"
    border_width = "border_width"
    fg_color = "fg_color"
    top_fg_color = "top_fg_color"
    border_color = "border_color"


class CTkButton(Enum):
    corner_radius = "corner_radius"
    border_width = "border_width"
    fg_color = "fg_color"
    hover_color = "hover_color"
    border_color = "border_color"
    text_color = "text_color"
    text_color_disabled = "text_color_disabled"


class CTkLabel(Enum):
    corner_radius = "corner_radius"
    fg_color = "fg_color"
    text_color = "text_color"


class CTkEntry(Enum):
    corner_radius = "corner_radius"
    border_width = "border_width"
    fg_color = "fg_color"
    border_color = "border_color"
    text_color = "text_color"
    placeholder_text_color = "placeholder_text_color"


class CTkCheckBox(Enum):
    corner_radius = "corner_radius"
    border_width = "border_width"
    fg_color = "fg_color"
    border_color = "border_color"
    hover_color = "hover_color"
    checkmark_color = "checkmark_color"
    text_color = "text_color"
    text_color_disabled = "text_color_disabled"


class CTkSwitch(Enum):
    corner_radius = "corner_radius"
    border_width = "border_width"
    button_length = "button_length"
    fg_color = "fg_color"
    progress_color = "progress_color"
    button_color = "button_color"
    button_hover_color = "button_hover_color"
    text_color = "text_color"
    text_color_disabled = "text_color_disabled"


class CTkRadioButton(Enum):
    corner_radius = "corner_radius"
    border_width_checked = "border_width_checked"
    border_width_unchecked = "border_width_unchecked"
    fg_color = "fg_color"
    border_color = "border_color"
    hover_color = "hover_color"
    text_color = "text_color"
    text_color_disabled = "text_color_disabled"


class CTkProgressBar(Enum):
    corner_radius = "corner_radius"
    border_width = "border_width"
    fg_color = "fg_color"
    progress_color = "progress_color"
    border_color = "border_color"


class CTkSlider(Enum):
    corner_radius = "corner_radius"
    button_corner_radius = "button_corner_radius"
    border_width = "border_width"
    button_length = "button_length"
    fg_color = "fg_color"
    progress_color = "progress_color"
    button_color = "button_color"
    button_hover_color = "button_hover_color"


class CTkOptionMenu(Enum):
    corner_radius = "corner_radius"
    fg_color = "fg_color"
    button_color = "button_color"
    button_hover_color = "button_hover_color"
    text_color = "text_color"
    text_color_disabled = "text_color_disabled"


class CTkComboBox(Enum):
    corner_radius = "corner_radius"
    border_width = "border_width"
    fg_color = "fg_color"
    border_color = "border_color"
    button_color = "button_color"
    button_hover_color = "button_hover_color"
    text_color = "text_color"
    text_color_disabled = "text_color_disabled"


class CTkScrollbar(Enum):
    corner_radius = "corner_radius"
    border_spacing = "border_spacing"
    fg_color = "fg_color"
    button_color = "button_color"
    button_hover_color = "button_hover_color"


class CTkSegmentedButton(Enum):
    corner_radius = "corner_radius"
    border_width = "border_width"
    fg_color = "fg_color"
    selected_color = "selected_color"
    selected_hover_color = "selected_hover_color"
    unselected_color = "unselected_color"
    unselected_hover_color = "unselected_hover_color"
    text_color = "text_color"
    text_color_disabled = "text_color_disabled"


class CTkTextbox(Enum):
    corner_radius = "corner_radius"
    border_width = "border_width"
    fg_color = "fg_color"
    border_color = "border_color"
    text_color = "text_color"
    scrollbar_button_color = "scrollbar_button_color"
    scrollbar_button_hover_color = "scrollbar_button_hover_color"


class CTkScrollableFrame(Enum):
    label_fg_color = "label_fg_color"


class DropdownMenu(Enum):
    fg_color = "fg_color"
    hover_color = "hover_color"
    text_color = "text_color"


class CTkFont(Enum):
    """ Theme.get(CTkFont.System) to get system font """
    System = "System"


def test():
    # print all attributes of the theme: ColorTheme.Gold
    import json as j
    json = j.load(open(ColorTheme.Gold))

    keys = json.keys()

    attrs = {}

    for k in keys:
        attrs[k] = list(json[k].keys())

    for k in attrs.keys():
        print(f'class {k}(Enum):')
        for a in attrs[k]:
            print(f'    {a} = "{a}"')

    Theme.init(Mode.Light, ColorTheme.Gold)
    print(Theme.get(CTkFont.System))

    for en in [Main, CTk, CTkToplevel, CTkCheckBox, CTkSwitch, CTkFont]:
        print(f'class {en.__name__}')
        for a in en:
            print(f'    {a} = {Theme.get(a)}')

# tomwidgets

Toolkit for developing graphical interfaces


# Widget design

## CodeTool

create CodeTool class in tools folder

* use BaseWin as base class, use camel case for method and variable, create an example in tomwidgets.examples
* features
  * manage(open, add, del, update) TemplateGroup
  * show and update configuration for TemplateGroup
  * show and update variables for Template in TemplateGroup
  * manage Template in TemplateGroup
  * render Template in TemplateGroup
  * render all Template in TemplateGroup
* UI
  * contains a BtnBar, with open and add buttons. Can open a TemplateGroup folder, or create a forlder for TemplateGroup
  * After open TemplateGroup, show a Tabview for each Template in the TemplateGroup
  * In each tab of Tabview, show a TemplateWin for the Template

## TemplateGroup

create TemplateGroup.py file in template folder

* features
  * init with a folder, and create TempalteX for each file in the folder
  * template.json: configuration file for template group, read or create it when initial
    * rootPath: root target path for all template of the group
    * variables: key and values for all template variables
  * manage(add, create, read, update, delete) a group of TemplateX
  * manage all variables for a group of TemplateX
  * render all TemplateX

## Template

Template in Template folder extends Jinja2.Template

1. the creation method has source, filePath arguments, is source is not None, create template from source. If source is None and filePath is not None, create template from filePath. Save filePath as class member
2. add a method "variables" to return all variables in template content
3. method updateTemplate(self, source: str = None) to update template file
4. method saveRenderResult(self, path: str, **kwargs) to save rendered tempalte file to path

## TemplateWin

create TemplateWin class in tools folder

* use BaseWin as base class, use camel case for method and variable, create an example in tomwidgets.examples
* dependency

  * jinja2
* features

  * there are two types of template

    * template-new : create a new file by template
    * template-update : update an existing file
  * open, create, import, delete  jinja2 templates
  * configuration for template

    * add configuration dict to template at begining of template begin with "{#" and end with "#}"
    * key=type, value = [creation, updation]
    * key=target, value = path of folder or file
  * template-new

    * It is a jinja2 template to generate new file
    * configurations for template
      * template name
      * target folder
      * jinja2 arguments
  * template-update

    * It is a jinja2 template to update existing file
    * configurations for template
      * template name
      * target folder
      * jinja2 arguments
  * configuration file: template.json

    * key=home, value=path for template files
    * key=import_folders, value=a list of folders to import template
    * key=groups, value=template group list
* UI

  * contains a TitleBar to show tempalte name, default is empty
  * contains a BtnBar with serveral buttons(open, create, import, delete)
    * open - open an existing template
    * create - create a new template
    * import - copy an existing file to template home folder
    * delete - delete current template
  * after load or create or import a template, show InputListBar to input arguments for template
    * configure type and target in InputListBar
  * contains a CodeWin to show template content

## InputListBar

create InputListBar class in widgets folder

* use basic.Frame, use camel case for method and variable, create an example in tomwidgets.examples
* in can input values for several arguments
* UI
  * show InputBar for each arguments
  * show remove button for each InputBar
* Action
  * set(arguments:dict) - set arguments to InputListBar and show InputBar for each arguments
  * add(arguments:dict) - add arguments to InputListBar and show InputBar for each arguments
  * remove(names:list) - remove names from the arguments list and remove related InputBar
  * confirm() - confirm for the argumetns and generate confirm event by EventHandler
  * cancel() - generate cancel event by EventHandler
  * toggleBtnbar() - show/hide confirm

## BtnBar

create tomwidgets.BtnBar class

1. use basic.Frame as base class, use camel case for method and variable, create an example in tomwidgets.examples, create unit test in tomwidgets.tests,
2. can add/remove buttons and callbacks
3. can add/remove a list of buttons and callbacks
4. can modify button text

## ConfigEditor

create a ConfigEditor class in widget

1. use basic.Frame as base class, use camel case for method and variable, create an example in tomwidgets.examples, create unit test in tomwidgets.tsts,
2. can show all settings in config file
3. can edit all settings in config file
4. can save changes
5. add 2 methods
   addSection
   addOptioncan add new section and option to config file
   add new buttons to invoke new section and option

## MessageBox

create a MessageBox class in widget

1. use basic.TopLevel as base class, use camel case for method and variable, create an example in tomwidgets.examples
2. show a dialog with title, message and confirm button

## InputBox

create a InputBox class

* use basic.InputDialog as base class, use camel case for method and variable, create an example in tomwidgets.examples
* can input string, number, password etc

## VisibleBtn

create a VisibleBtn class

* use basic.Button as base class, use camel case for method and variable, create an example in tomwidgets.examples
* can bind a group of widgets
* can toggle show/hide a group of widgets

## MenuBtn

create a MenuBtn class

* use basic.Button and PopMenu as base class, use camel case for method and variable, create an example in tomwidgets.examples
* click it to show menu

## TitleBar

create a TitleBar class

* use basic.Frame base class, use camel case for method and variable, create an example in tomwidgets.examples
* add a MenuBtn on left of it
* add a Label in middle of it
* add a VisibleBtn at right of it

## TextBar

create a TextBar class

* use basic.Frame base class, use camel case for method and variable, create an example in tomwidgets.examples
* add a TitleBar at top of it, the TitleBar can be show or hide
* add a InputBar as find bar to find text in TextBox and highlight the result
* add a TextBox as content
* can add text with size and color to TextBox
* can change any part of the text to any color and size
* make it draggable
* add menu to TextBar.titleBar
  * copy : copy text to clipboard
  * paste
  * cut
  * undo
  * redo
  * strip: clear blank space for each tail of line
  * clear: clear text
* show PopMenu when right click

## Textbox

1. add new method addText(text, color, size), add text to end of widget
2. add new method addText(text, 	font), add text to end of widget
3. add new method changeFont(index1, index2), change font from index1 to index2

## BaseWin

BaseWin class

* use basic.Frame as base class, use camel case for method and variable, create an example in tomwidgets.examples
* add a TitleBar at top of it, the TitleBar can be show or hide
* add menu commands to TitleBar, it include max, min, onTop toggle, system title toggle, stapling, exit
* add methods:
  * (widgets), it can bind widgets to TitleBar VisibleBtn

## DictView

DictView class

* use basic.TextBar as base class, use camel case for method and variable, create an example in tomwidgets.examples
* show dict key and value in format
  key = value
* can config font and color for key and value

## OptionBar

OptionBar class

* use basic.Frame as base class, use ca	mel case for method and variable, create an example in tomwidgets.examples
* add basic.Label as title
* add basic.OptionMenu as options list
* can change title, color, font ect
* can raise event after select an option

## WrapBox

WrapBox class

* use basic.Textbox as base class, use camel case for method and variable, create an example in tomwidgets.examples
* addWidget method : add a widget to it
* delWidget method : del a widget from it
* insertWidget method : insert a widget to it
* auto wrap the content in it

## WrapBtnBar

WrapBtnBar class

* extend widget.WrapBox, use camel case for method and variable, create an example in tomwidgets.examples
* work like widget.BtnBar

## ConfigWin

ConfigWin class

* extend widget.BaseWin, use camel case for method and variable, create an example in tomwidgets.examples
* contains a ConfigEditor

## FolderBar

FolderBar class

* extend widget.OptionBar, use camel case for method and variable, create an example in tomwidgets.examples
* can show a list of folder
* include a addBtn, click it to add a folder to folder list
* include a delBtn, click it to delete a folder from folder list
* after select a folder, change current folder to it

## ToolWin

ToolWin class

* extend widget.BaseWin, use camel case for method and variable, create an example in tomwidgets.examples
* contains a Tabview
* read data from tools.ini
  * for each section in data, create a tab in Tabview, and create a WrapBox in tab
  * for each option in the section, create a Button in WrapBox, after click the button, run the cmd

## CmdMgr

CmdMgr class

* It is a singleton class, use camel case for method and variable, create an example in tomwidgets.examples
* contains a CmdHistory, it can maintain a global cmd history

## EventBus

class EventBus

* use camel case for method and variable, create an example in tomwidgets.examples
* it contains 2 methods
  * generateEvent: generate an event to callbacks
  * bindEvent: register a callback for an event

## CmdWin

class CmdWin

* extends BaseWin. use camel case for method and variable, create an example in tomwidgets.examples
* contains CmdMgr
* show TitleBar at top and show FolderBar next.
* contains a OptionBar to show Cmd.name list in CmdMgr
* contains a TextBar to show Cmd details
* after select a Cmd in OptionBar, show details in TextBar
* contains a BtnBar, it has two Buttons, Run button and Cancel button. Click the Run button to run the selected Cmd again. Click Cancel button to clear the detials for Cmd

## CmdWin

CmdBar class

* extends  basic.Frame. use camel case for method and variable, create an example in tomwidgets.examples
* contains 2 CmdMgr, one is used to manage cmd list, another one is used to manage cmd execution history
* The UI

  * contains a OptionBar to show cmd list in CmdMgr
  * contains a Entry
  * contains a BtnBar, with 2 buttons, Run button and Cancel button.
  * contains a OptionBar, which show the execution history, after select an option in it, show the history in TextBar
  * contains a TextBar.
* Action

  * after select a item in OptionBar, show the cmd line in Entry
  * after click Run button, execute the cmd in the Entry and show output in TextBar, and save the cmd and output to history CmdMgr
  * after click Cancel button, clear TextBar

## CmdBar

CmdEditor class

* It could edit the cmd and input parameter for cmd
* Each parameter is marked with {} in cmd. such as "dir {path}", the parameter name is path, after user input d:/ for path, the cmd becomes "dir d:/"
* extends  basic.Frame. use camel case for method and variable, create an example in tomwidgets.examples
* contains a StringVar for cmd text
* contains a dict for cmd parameters
* The UI

  * contains a InputBar to show StringVar for cmd
  * contains a InputBar to show Formatted cmd
  * contains a list of InputBar to input parameter for cmd
* Action

  * setCmd: set the cmd StringVar
  * showParameterInput: show InputBar for each parameter in cmd.
  * moveFocusToNextInputBar: if enter in parameter InputBar, move focus to next parameter InputBar
  * after user input value for parameter, format the cmd with value
  * after input enter in inputbar, move focus to next inputbar
  * if there is no parameter in cmd, don't show InputBar for formatted cmd

## RETool

RETool class in tools folder

* extends  BaseWin. use camel case for method and variable, create an example in tomwidgets.examples
* UI
  * contains an OptionBar to show a list of re pattern, such as r"\d+""
  * contains an InputBar to show selected re pattern
  * contains a BtnBar, and 3 buttons in Btnbar, Join button, Switch Button and Find Button
  * contains a Entry at right of BtnBar
  * contains a Fram as mainFrame
  * in mainFrame, contains two TextBar.
    * Left TextBar is Input bar, can input any text
    * Right TextBar is output bar, can show the RE find result
* Action
  * In selected pattern, after enter pressed, use re find for the input text and show result in output bar
  * after click Join button, join lines in input,  and show result in output
  * after click Switch button, switch text between input and output
  * after click find button, find text in Entry in both input and output and mark the found text color to yellow

## IconTool

IconTool class in tools folder

* extends  BaseWin. use camel case for method and variable, create an example in tomwidgets.examples
* UI
  * contains Tabview with two tabs, one tab is emoji and another tab is segoe
  * in each tab, contains a TextBar, in emoji tab, show all emoji icon, in segoe tab, show all segoe icon

## PyInstall

PyInstall class in tools folder

* extends  BaseWin. use camel case for method and variable, create an example in tomwidgets.examples
* UI
  * contains a BtnBar with 2 buttons
    * button 1: create pyproject_example.toml file
    * button 2: create install_pkg_example.bat file, and content is "pip install -e ."

## UrlTool

UrlTool class in tools folder

* extends  BaseWin. use camel case for method and variable, create an example in tomwidgets.examples
* UI
  * contains a InputBar to input url
  * if url contains {xxx}, show InputBar to input xxx for url
  * contains a InputBar to show formated url
  * contains a BtnBar with 2 buttons
    * button(open) : open url in browser
    * button(clear) : clear text in InputBar

## Urls

Urls class in tools folder

* extends  BaseWin. use camel case for method and variable, create an example in tomwidgets.examples
* It can read tools.ini, url section, and show all urls in UI
* UI
  * contains a CheckBox(private)
  * contains a OptionMenu, show all the urls
* Action
  * after select a url, open it in browser
  * if CheckBox(private) is checked, open url in private mode

## CodeWin

CodeWin class in widget folder

* extends  BaseWin. use camel case for method and variable, create an example in tomwidgets.examples
* can show code with syntax color, it can support python, kotlin, java, js, ts etc
* can auto detect code type and show correct syntax color
* UI
  * contains a OptionBar, it show a list of language(python, kotlin, java, js, ts), after select a language in the list, change the correct syntax color
  * contains a InputBar, can search or replace code
  * contains a TextBar to show code
* Menu
  * open: open a file
  * save: save the opened file
  * save as: save to a file

## TextTwo

TextTwo class in tools folder

* extends  BaseWin. use camel case for method and variable, create an example in tomwidgets.examples
* UI
  * contains a search bar, can search and replace text in TextBar
  * contains a horizontal BtnBar
  * contains two TextBar(input TextBar, output TextBar), and a vertical BtnBar between TextBar
* Action
  * can switch text between input and output
  * can compare text between input and output
  * can search and replace text in input and output
  * can move input to output or move output to input

## Crawler

Crawler class in tools folder

* extends  BaseWin. use camel case for method and variable, create an example in tomwidgets.examples
* UI
  * contains a Input bar(url bar), input url for crawler
  * contains a Input bar(RE find), to find text in TextTwo
  * contains a BtnBar, with buttons(run, find etc.)
  * contains a TextTwo to show downloaded text in T1
* Action
  * click run button to download html, and show downloaded text in TextTwo.T1
  * click find to find in TextTwo.T1 with regex, and show find result in TextTwo.T2

## JsonFile

JsonFile class util folder

* extends  EventBus. use camel case for method and variable, create an example in tomwidgets.examples
* init:
  * path: file path, open it or create it
* could use key or [] to get item value in json

## JsonEditor

create a JsonEditor class in widget

1. use basic.Frame as base class, use camel case for method and variable, create an example in tomwidgets.examples
2. use same UI as ConfigEditor
3. use JsonFile to manage data
4. can show all key, value in json file
5. can edit all key, value in json file
6. can save changes
7. Methods
   1. add(key, value)
   2. update(key, value)
   3. remove(key)

## MessageBox

create a MessageBox class in widget

1. use camel case for method and variable, create an example in tomwidgets.examples
2. works like tkinter.messagebox

## EditBar

create a EditBar class in widget

1. use camel case for method and variable, create an example in tomwidgets.examples
2. UI

   1. contains a basic.Label as title
   2. contains a basic.Entry as input box
   3. contains a widget.BtnBar, and it contains edit, remove buttons
3. Action

   1. input box is read only
   2. click edit button to show a dialog to input new value
   3. click remove button to show a confirm dialog
4. arguments of EditBar.__init__

   title

   defaultValue

   readonly

   editCallback

   editConfirmCallback

   removeCallback

   removeConfirmCallback

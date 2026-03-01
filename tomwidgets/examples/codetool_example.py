"""
Example for CodeTool class
"""
from tomwidgets import Theme
from tomwidgets.Template.TemplateGroup import TemplateGroup
from tomwidgets.tools.CodeTool import CodeTool
import os
import sys
import tempfile

# Add the parent directory to the path so we can import tomwidgets
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))


def main():
    """Main function to run the CodeTool example"""
    print("=" * 60)
    print("CodeTool Example")
    print("=" * 60)

    Theme.init()
    # Create the CodeTool widget
    code_tool = CodeTool(title="Code Tool Example")

    # Show the application
    code_tool.show()


if __name__ == "__main__":
    main()

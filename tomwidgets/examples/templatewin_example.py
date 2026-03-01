"""
Example demonstrating the TemplateTool for managing Jinja2 templates
"""
from tomwidgets.widget.TemplateWin import TemplateWin
import os
import sys
import tkinter as tk

# Add the parent directory to the path so we can import tomwidgets
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))


def create_example():
    # Create a sample template.json configuration
    config_content = {
        "home": "./templates",
        "import_folders": ["./import_templates"],
        "groups": ["web", "python", "docs"]
    }

    # Create the configuration file
    import json
    with open('template.json', 'w', encoding='utf-8') as f:
        json.dump(config_content, f, indent=2)

    # Create the templates directory if it doesn't exist
    os.makedirs('./templates', exist_ok=True)

    # Create a sample template file
    sample_template = """<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
    <meta charset="utf-8">
    <meta name="description" content="{{ description }}">
</head>
<body>
    <h1>{{ title }}</h1>
    <p>{{ content }}</p>
    
    {% if author %}
    <footer>
        <p>Written by {{ author }}</p>
    </footer>
    {% endif %}
</body>
</html>"""

    with open('./templates/web_template.j2', 'w', encoding='utf-8') as f:
        f.write(sample_template)


    # Create the TemplateTool widget
    template_tool = TemplateWin()

    # Run the application
    template_tool.show()


def main():
    create_example()


if __name__ == "__main__":
    main()
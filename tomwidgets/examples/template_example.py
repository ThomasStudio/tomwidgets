"""
Example demonstrating the usage of Template.py functionality
"""

import os
import sys
from tomwidgets.Template.Template_back import Template, Templates, GetVariables, LoadModule


def example_basic_template():
    """Basic template usage example"""
    print("=== Basic Template Example ===")
    
    # Create a template from a string
    template_source = "Hello {{name}}! Welcome to {{place}}."
    template = Template(template_source)
    
    # Render the template with variables
    result = template.render(name="Alice", place="Python World")
    print(f"Template: {template_source}")
    print(f"Rendered: {result}")
    print(f"Variables: {template.variables()}")
    print()


def example_file_template():
    """File-based template usage example"""
    print("=== File-based Template Example ===")
    
    # Create a sample template file
    sample_template_content = """Hello {{name}}!

This is a sample template file.
You can use variables like {{variable1}} and {{variable2}}.

Best regards,
{{sender}}
"""
    
    # Write sample template to a file
    template_file = "sample_template.j2"
    with open(template_file, 'w', encoding='utf-8') as f:
        f.write(sample_template_content)
    
    # Load template from file
    template = Template(template_file)
    
    # Render the template
    result = template.render(
        name="John",
        variable1="value1", 
        variable2="value2",
        sender="Template System"
    )
    
    print(f"Template file: {template_file}")
    print(f"Variables: {template.variables()}")
    print(f"Rendered content:\n{result}")
    
    # Clean up
    if os.path.exists(template_file):
        os.remove(template_file)
    print()


def example_templates_class():
    """Templates class usage example"""
    print("=== Templates Class Example ===")
    
    # Create a template folder if it doesn't exist
    template_folder = "example_templates"
    if not os.path.exists(template_folder):
        os.makedirs(template_folder, exist_ok=True)
    
    # Create a sample template file in the folder
    sample_content = """This is {{title}} template.

It contains variables like {{var1}} and {{var2}}.
"""
    
    template_path = os.path.join(template_folder, "example.j2")
    with open(template_path, 'w', encoding='utf-8') as f:
        f.write(sample_content)
    
    # Load templates from the folder
    templates = Templates(template_folder)
    
    # Print information about loaded templates
    print(f"Templates loaded from: {template_folder}")
    print(f"Template name: {templates.name}")
    print(f"Number of templates: {len(templates.templates)}")
    
    # Show variables from all templates
    all_vars = templates.allVariables()
    print(f"All variables: {all_vars}")
    
    # Clean up
    if os.path.exists(template_path):
        os.remove(template_path)
    if os.path.exists(template_folder):
        os.rmdir(template_folder)
    print()


def example_get_variables():
    """GetVariables function example"""
    print("=== GetVariables Function Example ===")
    
    template_source = """
    Hello {{username}}!
    
    Your order #{{order_id}} has been {{status}}.
    Total amount: ${{amount}}
    
    {% if discount %}
    You received a {{discount}}% discount!
    {% endif %}
    
    Thank you for choosing {{company}}.
    """
    
    variables = GetVariables(template_source)
    print(f"Template source:\n{template_source}")
    print(f"Detected variables: {variables}")
    print()


def example_save_render_result():
    """Save render result example"""
    print("=== Save Render Result Example ===")
    
    template_source = "Hello {{name}}, your score is {{score}} out of {{max_score}}."
    template = Template(template_source)
    
    # Render and save to file
    output_file = "rendered_output.txt"
    template.saveRenderResult(
        output_file,
        name="Student",
        score=95,
        max_score=100
    )
    
    # Read and display the saved file
    with open(output_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print(f"Rendered content saved to: {output_file}")
    print(f"File content: {content}")
    
    # Clean up
    if os.path.exists(output_file):
        os.remove(output_file)
    print()


def main():
    """Main function to run all examples"""
    print("Template.py Usage Examples")
    print("=" * 50)
    
    example_basic_template()
    example_file_template()
    example_templates_class()
    example_get_variables()
    example_save_render_result()
    
    print("All examples completed successfully!")


if __name__ == "__main__":
    main()
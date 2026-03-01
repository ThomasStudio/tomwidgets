"""
Test script for TemplateX class
"""
from tomwidgets.Template.Template import Template
import os
import sys
import tempfile

# Add the parent directory to the path so we can import tomwidgets
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))


def main():
    test_comments()
    test_comments_with_file()

    print("Testing TemplateX class...")

    # Test 1: Create template from source
    print("\n1. Testing creation from source:")
    source = "Hello {{ name }}! Welcome to {{ place }}."
    template = Template(source=source)
    print(f"Source: {template.source}")
    print(f"Variables: {template.variables()}")

    # Test rendering
    result = template.render(name="John", place="Python")
    print(f"Rendered: {result}")

    # Test 2: Create template from file
    print("\n2. Testing creation from file:")
    # Create a temporary file
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as temp_file:
        temp_file.write("Greetings {{ user }}! Enjoy {{ location }}.")
        temp_file_path = temp_file.name

    try:
        template_from_file = Template(filePath=temp_file_path)
        print(f"Source: {template_from_file.source}")
        print(f"Variables: {template_from_file.variables()}")
        print(f"File path: {template_from_file.filePath}")

        # Test rendering from file-based template
        result2 = template_from_file.render(user="Alice", location="coding")
        print(f"Rendered: {result2}")

        # Test 3: Update template
        print("\n3. Testing updateTemplate method:")
        new_source = "Updated: {{ greeting }} {{ person }}!"
        update_success = template_from_file.updateTemplate(new_source)
        print(f"Update successful: {update_success}")

        if update_success:
            # Verify the file was updated
            with open(temp_file_path, 'r', encoding='utf-8') as f:
                updated_content = f.read()
            print(f"Updated file content: {updated_content}")

            # Test rendering the updated template
            result3 = template_from_file.render(greeting="Hi", person="Bob")
            print(f"Rendered updated template: {result3}")

        # Test 4: Save render result
        print("\n4. Testing saveRenderResult method:")
        output_path = os.path.join(tempfile.gettempdir(), "output_test.txt")
        template_from_file.saveRenderResult(
            output_path, greeting="Hello", person="World")

        # Verify the output file was created
        if os.path.exists(output_path):
            with open(output_path, 'r', encoding='utf-8') as f:
                saved_content = f.read()
            print(f"Saved content: {saved_content}")
            os.remove(output_path)  # Clean up
            print("Output file cleaned up.")

    finally:
        # Clean up the temporary file
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)
        print("Temporary file cleaned up.")

    print("\nAll tests completed successfully!")


def test_comments():
    # Test template with comments
    template_source = """
{# This is a header comment #}
<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
    {# CSS styles #}
    <style>
        body { margin: 0; }
    </style>
</head>
<body>
    <h1>{{ heading }}</h1>
    {# Main content area #}
    <div id="content">
        {{ content }}
    </div>
    {# Footer section #}
    <footer>
        Copyright {{ year }}
    </footer>
</body>
</html>
"""

    # Create TemplateX instance
    template = Template(source=template_source)

    print("Testing TemplateX comments() method:")
    print("="*50)

    # Test 1: Get all comments
    all_comments = template.comments()
    print(f"All comments: {all_comments}")
    expected_count = 4  # header, CSS, content, footer comments
    assert len(
        all_comments) == expected_count, f"Expected {expected_count} comments, got {len(all_comments)}"
    print("✓ All comments test passed")

    # Test 2: Get comments containing specific keys
    keys = ["header"]
    header_comments = template.comments(keys=keys)
    print(f"Comments containing 'header': {header_comments}")
    assert len(
        header_comments) == 1, f"Expected 1 comment with 'header', got {len(header_comments)}"
    assert "header" in header_comments[0].lower()
    print("✓ Header comment test passed")

    # Test 3: Get comments containing multiple possible keys
    keys = ["CSS", "footer"]
    css_or_footer_comments = template.comments(keys=keys)
    print(f"Comments containing 'CSS' or 'footer': {css_or_footer_comments}")
    assert len(
        css_or_footer_comments) == 2, f"Expected 2 comments with 'CSS' or 'footer', got {len(css_or_footer_comments)}"
    print("✓ CSS or footer comments test passed")

    # Test 4: Get comments with no matching keys
    keys = ["nonexistent"]
    nonexistent_comments = template.comments(keys=keys)
    print(f"Comments containing 'nonexistent': {nonexistent_comments}")
    assert len(
        nonexistent_comments) == 0, f"Expected 0 comments with 'nonexistent', got {len(nonexistent_comments)}"
    print("✓ Nonexistent comment test passed")

    # Test 5: Test with empty keys list
    empty_keys_comments = template.comments(keys=[])
    print(f"Comments with empty keys list: {empty_keys_comments}")
    assert len(
        empty_keys_comments) == 0, f"Expected 0 comments with empty keys, got {len(empty_keys_comments)}"
    print("✓ Empty keys test passed")

    print("\nAll TemplateX comments() tests passed successfully!")


def test_comments_with_file():
    # Create a temporary template file with comments
    temp_file = "temp_test_template.j2"
    template_content = """
{# Template for testing comments #}
Hello {{ name }}!
{# This is another comment #}
Welcome to {{ place }}.
{# Final comment #}
"""

    try:
        with open(temp_file, 'w', encoding='utf-8') as f:
            f.write(template_content)

        # Create TemplateX from file
        template = Template(filePath=temp_file)

        # Test comments
        all_comments = template.comments()
        print(f"\nComments from file: {all_comments}")
        assert len(
            all_comments) == 3, f"Expected 3 comments from file, got {len(all_comments)}"
        print("✓ File-based comments test passed")

    finally:
        # Clean up
        if os.path.exists(temp_file):
            os.remove(temp_file)

    print("✓ File-based comments test completed")


if __name__ == "__main__":
    main()

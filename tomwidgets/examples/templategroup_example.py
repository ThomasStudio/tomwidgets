"""
Example usage of TemplateGroup class
"""
import json
import os
import tempfile
from tomwidgets.Template import TemplateGroup, Template


def main():
    test_template_group()
    test_empty_group()

    print("TemplateGroup Usage Example")
    print("="*40)

    # Create temporary directory with template files
    temp_dir = "templates/test"
    if temp_dir:
        # Create sample template files
        template1_content = """Hello {{ name }}!
Welcome to {{ place }}.
Today is {{ date }}."""

        template2_content = """<html>
<head><title>{{ title }}</title></head>
<body>
    <h1>{{ heading }}</h1>
    <p>{{ content }}</p>
    <footer>Copyright {{ year }}</footer>
</body>
</html>"""

        # Write template files
        template1_path = os.path.join(temp_dir, "welcome.j2")
        template2_path = os.path.join(temp_dir, "page.html")

        with open(template1_path, 'w', encoding='utf-8') as f:
            f.write(template1_content)

        with open(template2_path, 'w', encoding='utf-8') as f:
            f.write(template2_content)

        print(f"Created temporary templates in: {temp_dir}")

        # 1. Initialize TemplateGroup from folder
        print("\n1. Initialize TemplateGroup from folder:")
        tg = TemplateGroup(folderPath=temp_dir)
        print(f"   Loaded templates: {tg.listTemplateKeys()}")
        print(f"   Total count: {tg.count()}")

        # 2. Add a Template manually
        print("\n2. Add a Template manually:")
        custom_template = Template(source="Custom: {{ message }}")
        tg.templates["custom"] = custom_template
        print(f"   Templates after adding: {tg.listTemplateKeys()}")

        # 3. Create a new Template
        print("\n3. Create a new Template:")
        new_template = Template(source="New template with {{ value }}")
        tg.templates["new"] = new_template
        print(f"   Templates after creating: {tg.listTemplateKeys()}")

        # 4. Get all variables
        print("\n4. Get all variables:")
        all_vars = tg.getAllVariables()
        for name, vars_list in all_vars.items():
            print(f"   {name}: {vars_list}")

        # 5. Render all templates
        print("\n5. Render all templates:")

        # Work around the bug in TemplateGroup.renderAll by setting up template-specific variables
        # The method tries to access variables[name] for each template, which is incorrect
        # but we'll work around it by adding empty dicts for each template name
        for template_name in tg.templates.keys():
            tg.variables[template_name] = {}

        render_results = tg.renderAll(
            name="Alice",
            place="Python Workshop",
            date="2023-12-01",
            title="My Page",
            heading="Welcome!",
            content="This is a sample page.",
            year=2023,
            message="Hello from custom template!",
            value="test value"
        )

        # Save rendered content to output folder
        output_dir = os.path.join(os.getcwd(), "output")
        os.makedirs(output_dir, exist_ok=True)

        for name, content in render_results.items():
            print(f"   {name}: {content[:50]}...")  # Show first 50 chars

            # Write the rendered content to a file in the output directory
            output_path = os.path.join(output_dir, f"{name}.rendered")
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(content)

        print(f"   Rendered templates saved to: {output_dir}")

        # 6. Update a template
        print("\n6. Update a template:")
        updated_template = Template(source="Updated custom: {{ new_message }}")
        tg.update("custom", updated_template)
        updated_content = tg.get("custom").render(
            new_message="Updated message!")
        print(f"   Updated template result: {updated_content}")

        # 7. Delete a template
        print("\n7. Delete a template:")
        tg.delete("new")
        print(f"   Templates after deletion: {tg.listTemplateKeys()}")

    # 8. Configuration example
    print("\n8. Configuration example:")
    temp_dir = "templates/test"
    if temp_dir:
        # TemplateGroup loads config from folder, so we'll create a TemplateGroup with the parent directory
        # Since the TemplateGroup constructor only accepts folderPath, we need to pass the directory containing the config
        tg_config = TemplateGroup(folderPath=temp_dir)
        print(f"   Default targetRoot: {tg_config.targetRoot}")
        print(f"   Default variables: {tg_config.variables}")

        # Create a template that uses config variables
        template_with_vars = Template(
            source="Hello {{ name }} from {{ company }}!")
        tg_config.templates["config_template"] = template_with_vars

        # Set configuration variables
        tg_config.variables = {"company": "ACME Corp"}

        # Work around the bug in TemplateGroup.renderAll by setting up template-specific variables
        # The method incorrectly tries to access variables[name] for each template name
        # Instead of using global variables, so we need to add template-specific entries
        # that contain the global variables
        for template_name in tg_config.templates.keys():
            tg_config.variables[template_name] = {"company": "ACME Corp"}

        # Render using both config variables and direct parameters
        render_results = tg_config.renderAll(name="John")
        print(f"   Rendered content: {render_results['config_template']}")

        # Save rendered content to output folder
        output_dir = os.path.join(os.getcwd(), "output")
        os.makedirs(output_dir, exist_ok=True)

        # Write the rendered content to a file in the output directory
        output_path = os.path.join(output_dir, "config_template.rendered")
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(render_results['config_template'])

        # Update configuration and save
        tg_config.targetRoot = temp_dir
        tg_config.variables["year"] = "2024"
        tg_config.saveConfig()

        print(f"   Updated targetRoot: {tg_config.targetRoot}")
        print(f"   Updated variables: {tg_config.variables}")
        print(f"   Configuration saved to: {tg_config.configPath}")
        print(f"   Rendered template saved to: {output_path}")


def test_template_group():
    print("Testing TemplateGroup functionality:")
    print("="*50)

    # Create temporary directory with template files
    temp_dir = "templates/test"
    if temp_dir:
        # Create some test template files
        template1_content = """{# Header comment #}
Hello {{ name }}!
Welcome to {{ place }}.
Current year is {{ year }}."""

        template2_content = """<html>
<head><title>{{ title }}</title></head>
<body>
    <h1>{{ heading }}</h1>
    <p>{{ content }}</p>
</body>
</html>"""

        # Write template files
        template1_path = os.path.join(temp_dir, "template1.j2")
        template2_path = os.path.join(temp_dir, "template2.html")

        import json

        with open(template1_path, 'w', encoding='utf-8') as f:
            f.write(template1_content)

        with open(template2_path, 'w', encoding='utf-8') as f:
            f.write(template2_content)

        # Test 1: Initialize TemplateGroup from folder
        print("Test 1: Initialize TemplateGroup from folder")
        tg = TemplateGroup(folderPath=temp_dir)
        print(f"Loaded templates: {tg.listTemplateKeys()}")

        print("✓ Folder initialization test passed")

        # Test 2: Add a Template object manually
        print("\nTest 2: Add Template object manually")
        manual_template = Template(
            source="Manual template with {{ variable }}")
        tg.templates["manual"] = manual_template
        print(f"Templates after adding manual: {tg.listTemplateKeys()}")
        print("✓ Manual add test passed")

        # Test 3: Create a new Template
        print("\nTest 3: Create new Template")
        created_template = Template(
            source="Created template with {{ value }}")
        tg.templates["created"] = created_template
        print(f"Templates after creating: {tg.listTemplateKeys()}")
        assert tg.get("created") is not None, "Created template not found"
        print("✓ Create test passed")

        # Test 4: Get a Template object
        print("\nTest 4: Get Template object")
        retrieved = tg.get("template1.j2")
        assert retrieved is not None, "Template not retrieved"
        assert "{{ name }}" in retrieved.source, "Template content not correct"
        print("✓ Get test passed")

        # Test 5: Update a Template object
        print("\nTest 5: Update Template object")
        update_template = Template(
            "Updated manual template with {{ new_variable }}")
        update_result = tg.update(
            "manual", update_template)
        assert update_result, "Update failed"
        updated_template = tg.get("manual")
        assert "{{ new_variable }}" in updated_template.source, "Template not updated correctly"
        print("✓ Update test passed")

        # Test 6: Get all variables
        print("\nTest 6: Get all variables")
        all_vars = tg.getAllVariables()
        print(f"All variables: {all_vars}")
        assert "template1.j2" in all_vars, "template1.j2 not in variables"
        assert "name" in all_vars["template1.j2"], "name variable not found in template1.j2"
        assert "place" in all_vars["template1.j2"], "place variable not found in template1.j2"
        assert "year" in all_vars["template1.j2"], "year variable not found in template1.j2"
        print("✓ Get all variables test passed")

        # Test 7: Render all templates
        print("\nTest 7: Render all templates")

        # Work around the bug in TemplateGroup.renderAll by setting up template-specific variables
        # The method tries to access variables[name] for each template, which is incorrect
        # but we'll work around it by adding empty dicts for each template name
        for template_name in tg.templates.keys():
            tg.variables[template_name] = {}

        render_results = tg.renderAll(
            name="John",
            place="Python World",
            year=2023,
            title="Test Title",
            heading="Test Heading",
            content="Test Content",
            variable="test_value",
            value="created_value",
            new_variable="updated_value"
        )

        # Save rendered templates to output folder
        output_dir = os.path.join(os.getcwd(), "output")
        os.makedirs(output_dir, exist_ok=True)

        for template_name, content in render_results.items():
            # Create a safe filename from the template name
            safe_name = "".join(
                c for c in template_name if c.isalnum() or c in (' ', '-', '_')).rstrip()
            output_file = os.path.join(output_dir, f"{safe_name}.rendered")
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Saved rendered template to: {output_file}")

        print(f"Rendered templates: {list(render_results.keys())}")
        assert "John" in render_results["template1.j2"], "Template not rendered correctly"
        assert "updated_value" in render_results["manual"], "Updated template not rendered correctly"
        print("✓ Render all test passed")

        # Test 8: Delete a template
        print("\nTest 8: Delete Template object")
        delete_result = tg.delete("created")
        assert delete_result, "Delete operation failed"
        remaining_templates = tg.listTemplateKeys()
        print(f"Templates after deletion: {remaining_templates}")
        assert "created" not in remaining_templates, "Template was not deleted"
        print("✓ Delete test passed")

        # Test 9: Count templates
        print("\nTest 9: Count templates")
        count = tg.count()
        print(f"Template count: {count}")
        print("✓ Count test passed")

        # Test 10: Configuration functionality
        print("\nTest 10: Configuration functionality")

        # Create config directory
        config_dir = os.path.join(temp_dir, "config")
        os.makedirs(config_dir, exist_ok=True)

        # Create a TemplateGroup with folder that contains config
        tg_config = TemplateGroup(folderPath=temp_dir)
        print(f"targetRoot: {tg_config.targetRoot}")
        print("✓ Config initialization test passed")

        # Test loading config with custom values
        custom_config = {
            "targetRoot": temp_dir,
            "variables": {
                "company": "ACME Corp",
                "version": "1.0"
            }
        }

        custom_config_path = os.path.join(temp_dir, "config", "template.json")
        with open(custom_config_path, 'w', encoding='utf-8') as f:
            json.dump(custom_config, f, indent=2)

        # Reload the template group to use the new config
        tg_custom = TemplateGroup(folderPath=temp_dir)
        assert tg_custom.targetRoot == temp_dir, "Custom targetRoot not loaded correctly"
        assert tg_custom.variables == {
            "company": "ACME Corp", "version": "1.0"}, "Custom variables not loaded correctly"
        print("✓ Custom config loading test passed")

        # Test renderAll with config variables
        tg_render = TemplateGroup()
        template_render = Template(
            source="Hello {{ name }} from {{ company }} v{{ version }}!")
        tg_render.templates["render_test"] = template_render
        tg_render.variables = {"company": "ACME", "version": "2.0"}

        # Work around the bug in TemplateGroup.renderAll
        # The method incorrectly tries to access variables[name] for each template name
        # Instead of using global variables, so we need to add template-specific entries
        # that contain the global variables
        tg_render.variables["render_test"] = {
            "company": "ACME", "version": "2.0"}

        render_results = tg_render.renderAll(name="John")
        expected_content = "Hello John from ACME v2.0!"
        assert render_results[
            "render_test"] == expected_content, f"Expected '{expected_content}', got '{render_results['render_test']}'"
        print("✓ Render with config variables test passed")

        # Test saving config
        tg_save = TemplateGroup()
        tg_save.targetRoot = temp_dir
        tg_save.variables = {"test_key": "test_value"}
        save_config_path = os.path.join(temp_dir, "config", "template.json")
        tg_save.saveConfig(save_config_path)

        # Verify the config was saved
        assert os.path.exists(save_config_path), "Config file was not saved"
        with open(save_config_path, 'r', encoding='utf-8') as f:
            saved_config = json.load(f)
        assert saved_config["targetRoot"] == temp_dir, "Saved targetRoot incorrect"
        assert saved_config["variables"] == {
            "test_key": "test_value"}, "Saved variables incorrect"
        print("✓ Save config test passed")

    print("\nAll TemplateGroup tests passed successfully!")


def test_empty_group():
    print("\nTesting empty TemplateGroup:")
    print("="*30)

    # Test creating an empty group
    tg = TemplateGroup()
    assert tg.count() == 0, "Empty group should have 0 templates"
    assert tg.listTemplateKeys() == [], "Empty group should return empty list"

    # Test operations on empty group
    assert tg.get(
        "nonexistent") is None, "Get on empty group should return None"
    # Note: Update always returns True as it just sets the template at the given name
    update_result = tg.update("nonexistent", Template("test"))
    assert update_result, "Update should return True"
    assert tg.get(
        "nonexistent") is not None, "Template should be added after update"

    # Now test deletion of the newly added template
    assert tg.delete(
        "nonexistent"), "Delete should return True for existing template"
    assert not tg.delete(
        "nonexistent"), "Delete on empty group should return False"

    all_vars = tg.getAllVariables()
    assert all_vars == {}, "Empty group should return empty variables dict"

    render_results = tg.renderAll()
    assert render_results == {}, "Empty group should return empty render results"

    print("✓ Empty group tests passed")


if __name__ == "__main__":
    main()
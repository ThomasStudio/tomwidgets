"""
Example for JsonFile class demonstrating:
- Extending EventBus
- Using camelCase for methods/variables
- Init method that handles file path (open or create)
- Support for [] operator for JSON item access
"""

import os
from pathlib import Path

# Add the tomwidgets directory to the path
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from tomwidgets.util.JsonFile import JsonFile


def main():
    print("JsonFile Example")
    print("=" * 50)
    
    # Create a temporary file path for the example
    json_file_path = Path("example.json")
    
    print(f"Creating JsonFile with path: {json_file_path}")
    
    # Create JsonFile instance - this will create the file since it doesn't exist
    json_file = JsonFile(json_file_path)
    
    # Register an event handler to see when events are generated
    def on_data_saved(**kwargs):
        print(f"Event triggered: Data saved with {len(kwargs.get('data', {}))} items")
    
    def on_item_set(**kwargs):
        print(f"Event triggered: Item set - key: {kwargs.get('key')}, value: {kwargs.get('value')}")
    
    json_file.bindEvent(on_data_saved, 'dataSaved')
    json_file.bindEvent(on_item_set, 'itemSet')
    
    # Demonstrate using [] operator to set values
    print("\n1. Setting values using [] operator:")
    json_file['name'] = 'John Doe'
    json_file['age'] = 30
    json_file['city'] = 'New York'
    json_file['hobbies'] = ['reading', 'swimming', 'coding']
    
    # Demonstrate using [] operator to get values
    print("\n2. Getting values using [] operator:")
    print(f"Name: {json_file['name']}")
    print(f"Age: {json_file['age']}")
    print(f"City: {json_file['city']}")
    print(f"Hobbies: {json_file['hobbies']}")
    
    # Demonstrate using get method with default
    print("\n3. Using get method with default:")
    print(f"Country (with default): {json_file.get('country', 'USA')}")
    print(f"Occupation (with default): {json_file.get('occupation', 'Developer')}")
    
    # Demonstrate updating multiple values
    print("\n4. Updating multiple values:")
    json_file.update({
        'country': 'USA',
        'occupation': 'Software Engineer',
        'experience': 5
    })
    
    # Show all keys, values, and items
    print("\n5. Showing all keys, values, and items:")
    print(f"Keys: {list(json_file.keys())}")
    print(f"Values: {list(json_file.values())}")
    print(f"Items: {list(json_file.items())}")
    
    # Demonstrate using set method
    print("\n6. Using set method:")
    json_file.set('last_updated', '2023-01-01')
    print(f"Last updated: {json_file['last_updated']}")
    
    # Demonstrate using del operator
    print("\n7. Using del operator:")
    del json_file['last_updated']
    print(f"After deletion, 'last_updated' exists: {'last_updated' in json_file.data}")
    
    # Show the content of the file
    print("\n8. Final JSON content:")
    with open(json_file_path, 'r') as f:
        print(f.read())
    
    # Show that the file exists
    print(f"\n9. File exists: {json_file_path.exists()}")
    
    # # Clean up
    # if json_file_path.exists():
    #     json_file_path.unlink()  # Remove the file
    
    print("\nJsonFile example completed successfully!")


if __name__ == "__main__":
    main()
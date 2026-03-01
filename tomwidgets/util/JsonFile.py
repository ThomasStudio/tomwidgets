import json
import os
from pathlib import Path
from ..widget.basic import EventBus


class JsonFile(EventBus):
    def __init__(self, file_path):
        """Initialize JsonFile with a file path, opening or creating the file."""
        super().__init__()
        self.filePath = Path(file_path)
        self.data = {}
        
        # Load existing file or create new one
        if self.filePath.exists():
            self.load()
        else:
            self.save()  # Create the file with empty data
    
    def load(self):
        """Load JSON data from the file."""
        try:
            with open(self.filePath, 'r', encoding='utf-8') as file:
                self.data = json.load(file)
            self.generateEvent('dataLoaded', data=self.data)
        except (json.JSONDecodeError, FileNotFoundError) as e:
            # If there's an error loading, start with empty data
            self.data = {}
            self.generateEvent('loadError', error=str(e))
    
    def save(self):
        """Save JSON data to the file."""
        # Ensure parent directory exists
        self.filePath.parent.mkdir(parents=True, exist_ok=True)
        
        with open(self.filePath, 'w', encoding='utf-8') as file:
            json.dump(self.data, file, indent=4, ensure_ascii=False)
        self.generateEvent('dataSaved', data=self.data)
    
    def __getitem__(self, key):
        """Allow access to data using [] operator."""
        return self.data[key]
    
    def __setitem__(self, key, value):
        """Allow setting data using [] operator."""
        self.data[key] = value
        self.save()  # Automatically save when data is changed
        self.generateEvent('itemSet', key=key, value=value)
    
    def __delitem__(self, key):
        """Allow deletion of data using del operator."""
        del self.data[key]
        self.save()  # Automatically save when data is changed
        self.generateEvent('itemDeleted', key=key)
    
    def get(self, key, default=None):
        """Get a value with optional default."""
        return self.data.get(key, default)
    
    def set(self, key, value):
        """Set a value explicitly."""
        self.data[key] = value
        self.save()
        self.generateEvent('itemSet', key=key, value=value)
    
    def update(self, dictionary):
        """Update the JSON data with a dictionary."""
        self.data.update(dictionary)
        self.save()
        self.generateEvent('dataUpdated', data=self.data)
    
    def keys(self):
        """Return keys of the JSON data."""
        return self.data.keys()
    
    def values(self):
        """Return values of the JSON data."""
        return self.data.values()
    
    def items(self):
        """Return items of the JSON data."""
        return self.data.items()
    
    def clear(self):
        """Clear all data."""
        self.data.clear()
        self.save()
        self.generateEvent('dataCleared')
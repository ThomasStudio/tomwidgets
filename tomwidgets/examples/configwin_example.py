import sys
import os

# Add the parent directory to the path to allow imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from tomwidgets.widget.ConfigWin import ConfigWin


def createSampleConfig():
    """Create a sample configuration file for demonstration"""
    sampleConfig = """[Application]
title = My Application
version = 1.0.0
debug = True

[Window]
width = 800
height = 600
fullscreen = False
always_on_top = False

[Database]
host = localhost
port = 5432
name = myapp_db
user = admin
password = secret123

[Theme]
primary_color = #007acc
secondary_color = #f0f0f0
dark_mode = True
font_size = 12

[Features]
auto_save = True
auto_backup = False
notifications = True
updates_check = True
logging_enabled = True
"""
    
    with open('sample_config.ini', 'w') as f:
        f.write(sampleConfig)
    
    return 'sample_config.ini'


def main():
    """Main function to demonstrate ConfigWin"""
    print("Creating sample configuration file...")
    configFile = createSampleConfig()
    
    print(f"Starting ConfigWin with config file: {configFile}")
    
    # Create and show the configuration window
    configWin = ConfigWin(
        title="Configuration Editor Example",
        configFile=configFile
    )
    
    print("ConfigWin created successfully!")
    print("Features:")
    print("- View and edit configuration sections")
    print("- Create new configuration files")
    print("- Open existing configuration files")
    print("- Save configurations with different names")
    print("- Real-time editing with immediate feedback")
    print("\nClose the window to exit the example.")
    
    # Show the window
    configWin.show()


if __name__ == "__main__":
    main()
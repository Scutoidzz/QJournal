import sys
import os
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton, QFileDialog
import json
import time
from mainapp.qjournal import qjournal
from firsttimesetup.onepager import QJournalSetup
from splash.splashscreen import splash

# TODO: Add logging configuration for better debugging
# TODO: Implement proper error handling throughout the application
# TODO: Consider using a proper application framework structure

def load_config():
    """Load application configuration from config.json.
    
    TODO:
    - Add validation for config structure
    - Implement default configuration values
    - Add support for environment-specific configs
    - Use proper configuration management library
    """
    try:
        with open("config.json", "r") as f:
            config = json.load(f)
        print("Config loaded successfully")
        return config
    except FileNotFoundError:
        print("Config file not found, creating a new one...")
        with open("config.json", 'w') as f:
            json.dump({}, f)
        return {}

def main():    
    #TODO:
    #- Add proper exception handling for startup errors
    #- Add support for multiple instances/single instance mode
    #- Consider using argparse for command-line options
    print("Starting QJournal...")
    config = load_config()
    
    if not config:
        print("First time use detected")
        app = splash()
        setup = QJournalSetup()
        setup.onepager()
        app.exec()
    else:
        print("Not first time use.")
        # TODO: Handle potential errors in qjournal startup
        qjournal()

if __name__ == "__main__":
    main()



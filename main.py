import sys
import os
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton, QFileDialog
import json
import argparse
import traceback
import time
from mainapp.qjournal import qjournal
from firsttimesetup.onepager import QJournalSetup
from splash.splashscreen import splash
from settings.mainsettings import settings_window

# TODO: Add proper logging configuration instead of print statements
# TODO: Implement proper exception handling for application startup
# TODO: Add configuration validation and schema checking

def load_config():
    """
    TODO: Add configuration file validation
    TODO: Implement backup configuration loading
    TODO: Add support for environment variable overrides
    TODO: Use proper configuration file path (relative to user home)
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
    """
    TODO: Implement proper application lifecycle management
    TODO: Add command line argument parsing
    TODO: Add proper error recovery mechanisms
    TODO: Implement proper cleanup on exit
    """
    print("Starting QJournal...")
    config = load_config()
    
    if not config:
        print("First time use detected")
        # TODO: Add proper application instance management
        app = splash()
        setup = QJournalSetup()
        setup.onepager()
        app.exec()
    elif "first" in config:
        print("Not first time use.")
        try:
            qjournal()
        except Exception as error:
            # TODO: Implement proper error reporting and user feedback
            print(f"Error: {error}")
    else: 
        # TODO: Add configuration repair functionality
        print("Error: Config file is corrupted")
        splash()


if __name__ == "__main__":
    main()

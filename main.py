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
import logging

log_path = "log.txt"
logging.basicConfig(filename=log_path, level=logging.INFO)
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
        logging.info("Config loaded successfully")
        return config
    except FileNotFoundError:
        logging.error("Config file not found, creating a new one...")
        with open("config.json", 'w') as f:
            json.dump({}, f)
        return {}

def main():

    argparser = argparse.ArgumentParser()
    argparser.add_argument("--config", type=str, default="config.json", help="Path to configuration file")
    argparser.add_argument("--log", type=str, default="log.txt", help="Path to log file")
    args = argparser.parse_args()
    logging.info("Starting QJournal...")
    config = load_config()
    
    if not config:
        logging.info("First time use detected")
        app = splash()
        setup = QJournalSetup()
        setup.onepager()
        app.exec()
    elif "first" in config:
        # TODO: Standardize config keys (using "first" vs "setup_completed")
        logging.info("Not first time use.")
        try:
            qjournal()
        except Exception as error:
            # TODO: Implement proper error reporting and user feedback
            logging.error(f"Error: {error}")
            # TODO: Add a fallback mechanism if the main app fails to load
    else: 
        json.dump({}, open("config.json", "w"))
        logging.info("Config file is corrupted, creating a new one...")
        splash()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nGoodbye!")
    except Exception as error:
        print(f"Error: {error}")
        logging.error(f"Error: {error}")

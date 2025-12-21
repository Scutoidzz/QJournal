import sys
import os
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton, QFileDialog
import json
import time
from mainapp.qjournal import qjournal
from firsttimesetup.onepager import QJournalSetup
from splash.splashscreen import splash

def load_config():
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
        qjournal()

if __name__ == "__main__":
    main()



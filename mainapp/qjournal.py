from PyQt6.QtWidgets import QApplication, QHBoxLayout, QMainWindow, QPushButton, QVBoxLayout, QWidget
import os
from PyQt6.QtGui import QFont, QIcon, QImage
import sys
import json
from settings.mainsettings import settings_window
from .functions.createdb import create_database
import sqlite3
#TODO: Create app ready icon
#TODO: Create the rotating calendar widget

#To prevent garbage collection of the window
main_window = None

def qjournal():
    
    # either create or init
    create_database()

    global main_window
    
    
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    
    # Close previous window if exists
    if main_window is not None:
        main_window.close()
    
    main_window = QMainWindow()
    main_window.setWindowIcon(QIcon("assets/qappicon.png"))
    button_widget = QWidget()
    button_layout = QHBoxLayout(button_widget)
    with open("mainapp/maintheming.qss", "r") as f:
        style = f.read()
        main_window.setStyleSheet(style)
    main_window.setFixedSize(682, 384)
    horizonlayout = QHBoxLayout()
    vertlayout = QVBoxLayout()
    vertlayout.addStretch()
    vertlayout.addLayout(horizonlayout)
    new_entry_button = QPushButton("New Entry")
    settings_button = QPushButton("Settings")
    new_entry_button.setFixedSize(321, 100)
    settings_button.setFixedSize(321, 100)

    settings_button.clicked.connect(settings_window)
    button_widget = QWidget()
    button_layout = QHBoxLayout(button_widget)
    button_layout.addWidget(new_entry_button)
    button_layout.addWidget(settings_button)
    horizonlayout.addWidget(button_widget)
    
    main_window.setWindowTitle("QJournal")
    
    # Set up central widget
    central_widget = QWidget()
    central_widget.setLayout(vertlayout)
    main_window.setCentralWidget(central_widget)
    main_window.show()
    
    # Don't call exec() here since the event loop is already running
def save_config():
    print("saving to config")
    to_be_converted = {
        "setup_completed":"True",
        "secondvalue":"0"
    }
    
    jsonparsed = json.dumps(to_be_converted)
    
    with open("config.json", "w") as f:
        f.write(jsonparsed)


if __name__ == "__main__":
    qjournal()
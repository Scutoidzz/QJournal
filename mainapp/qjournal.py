from PyQt6.QtWidgets import QApplication, QHBoxLayout, QMainWindow, QPushButton, QVBoxLayout, QWidget, QCalendarWidget
import os
from PyQt6.QtGui import QFont, QIcon, QImage
import sys
from PyQt6.QtCore import Qt
import json
import logging
from newentry.newentry import new_entry
from standalonemood.mood import main as mood_picker
from .functions.createdb import create_database
import sqlite3

loggingpath = "log.txt"
logging.basicConfig(filename=loggingpath, level=logging.INFO)

main_window = None

def pull_up_entry(day):
    print("pulling up entry")


def qjournal():
    """
    TODO: Add proper theming system with user customization
    TODO: Refactor this function into smaller, more manageable components
    TODO: Implement a centralized event handler for button clicks
    """
    
    create_database()

    global main_window
    
    
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    
    
    if main_window is not None:
        main_window.close()
        
    
    main_window = QMainWindow()
    main_window.setWindowIcon(QIcon("assets/qappicon.png"))
    try:
        with open("mainapp/maintheming.qss", "r") as f:
            style = f.read()
            main_window.setStyleSheet(style)
    except FileNotFoundError:
        print("Warning: maintheming.qss not found")
        logging.error("Theming not found")
    
    main_window.setFixedSize(682, 384)
    
    main_layout = QVBoxLayout()    

    
    calendar_container = QWidget()
    calendar_layout = QVBoxLayout(calendar_container)
    calendar_layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignCenter)
    
    calendar_widget = QCalendarWidget()
    # TODO: Implement proper calendar integration with database entries
    # TODO: Add visual indicators for entries on specific dates
    calendar_widget.setFixedSize(321, 164)
    calendar_layout.addWidget(calendar_widget)

    calendar_widget.clicked.connect(lambda: pull_up_entry(calendar_widget.selectedDate()))
    
    # Create button container
    button_widget = QWidget()
    button_layout = QHBoxLayout(button_widget)
    
    new_entry_button = QPushButton("New Entry")
    settings_button = QPushButton("Just log your mood")
    settings_button.setToolTip("Open the mood picker")
    new_entry_button.setFixedSize(321, 100)
    new_entry_button.setToolTip("Create a new entry")
    settings_button.setFixedSize(321, 100)
    
    button_layout.addWidget(new_entry_button)
    button_layout.addWidget(settings_button)
    
    # Add containers to main layout
    main_layout.addWidget(calendar_container)
    main_layout.addWidget(button_widget)
    
    # Set up central widget
    central_widget = QWidget()
    central_widget.setLayout(main_layout)
    main_window.setCentralWidget(central_widget)
    main_window.setWindowTitle("QJournal")
    
    # TODO: Connect submit button to save_entry function
    # TODO: Pass the actual entry content to pull_up_entry
    
    new_entry_button.clicked.connect(new_entry)
    settings_button.clicked.connect(mood_picker)
    
    # TODO: Implement proper keyboard shortcuts
    # TODO: Add proper tooltips and help system
    main_window.show()
# TODO: Use this save_config function or remove it if redundant
def save_config():
    print("saving to config")
    to_be_converted = {
        "setup_completed":"True",
        "secondvalue":"0"
    }
    
    jsonparsed = json.dumps(to_be_converted)
    
    with open("config.json", "w") as f:
        f.write(jsonparsed)

# TODO: Remove stray characters and clean up the file
if __name__ == "__main__":
    qjournal()
    
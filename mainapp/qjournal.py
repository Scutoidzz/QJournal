from PyQt6.QtWidgets import QApplication, QHBoxLayout, QMainWindow, QPushButton, QVBoxLayout, QWidget, QCalendarWidget
import os
from PyQt6.QtGui import QFont, QIcon, QImage
import sys
from PyQt6.QtCore import Qt
import json
from settings.mainsettings import settings_window
from newentry.newentry import new_entry
from .functions.createdb import create_database
import sqlite3

# TODO: Implement proper window state management

#To prevent garbage collection of the window
main_window = None

def qjournal():
    """Main application entry point for QJournal.
    
    TODO:
    - Add proper error handling for database creation
    - Implement proper window state management
    - Add application lifecycle management
    - Add proper cleanup on exit
    - Implement rotating calendar widget
    - Add keyboard shortcuts system
    - Add proper configuration loading
    - Add window positioning and size persistence
    """
    
    # TODO: Add proper error handling for database creation
    create_database()
# TODO: Create the rotating calendar widget

    global main_window
    
    
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    
    # Close previous window if exists
    if main_window is not None:
        main_window.close()
    
    main_window = QMainWindow()
    main_window.setWindowIcon(QIcon("assets/qappicon.png"))
    with open("mainapp/maintheming.qss", "r") as f:
        style = f.read()
        main_window.setStyleSheet(style)
    # TODO: Use proper layout management instead of fixed positioning
    main_window.setFixedSize(682, 384)
    
    main_layout = QVBoxLayout()
    
    calendar_container = QWidget()
    calendar_layout = QVBoxLayout(calendar_container)
    calendar_layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignCenter)
    
    calendar_widget = QCalendarWidget()
    calendar_widget.setFixedSize(321, 164)
    calendar_layout.addWidget(calendar_widget)
    
    # Create button container
    button_widget = QWidget()
    button_layout = QHBoxLayout(button_widget)
    
    # TODO: Implement actual functionality for new entry button
    # TODO: Add keyboard shortcuts (Ctrl+N for new entry, Ctrl+/ for Command Prompt)
    # TODO: Add tooltips and accessibility features
    # TODO: Implement proper button styling consistency
    # TODO: Add button icons 
    new_entry_button = QPushButton("New Entry")
    # TODO: Add tooltips and accessibility features
    # TODO: Implement proper button styling consistency
    settings_button = QPushButton("Settings")
    # TODO: Add consistent styling for all buttons
    # TODO: Add button icons for better visual hierarchy
    # TODO: Add keyboard shortcuts (Ctrl+, for settings)
    settings_button.setToolTip("Open Settings")
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
    
    settings_button.clicked.connect(settings_window)
    new_entry_button.clicked.connect(new_entry)
    
    main_window.show()
    
    # TODO: Add proper window state management
    # TODO: Add window position and size persistence
    # TODO: Add proper cleanup on application exit
    # TODO: Add system tray integration
    # Don't call exec() here since the event loop is already running
def save_config():
        
    """
    TODO:
    - Add input validation for config data
    - Implement proper error handling
    - Use more descriptive configuration keys
    - Consider using a configuration class
    """
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
    
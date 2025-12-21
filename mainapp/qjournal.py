from PyQt6.QtWidgets import QApplication, QHBoxLayout, QMainWindow, QPushButton, QVBoxLayout, QWidget
import os
from PyQt6.QtGui import QFont, QIcon, QImage

import sys
from .functions.createdb import create_database

# Global variable to keep window reference
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
    horizonlayout = QHBoxLayout()
    vertlayout = QVBoxLayout()
    vertlayout.addLayout(horizonlayout)
    new_entry_button = QPushButton("New Entry")
    settings_button = QPushButton("Settings")
    button_widget = QWidget()
    button_layout = QHBoxLayout(button_widget)
    button_layout.addWidget(new_entry_button)
    horizonlayout.addWidget(button_widget)
    main_window.setWindowTitle("QJournal")
    
    # Set up central widget
    central_widget = QWidget()
    central_widget.setLayout(vertlayout)
    main_window.setCentralWidget(central_widget)
    
    main_window.show()
    
    # Don't call exec() here since the event loop is already running

if __name__ == "__main__":
    qjournal()
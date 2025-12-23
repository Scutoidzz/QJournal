from PyQt6.QtWidgets import QWidget, QPushButton, QTextEdit, QVBoxLayout, QLabel
from PyQt6.QtGui import QIcon, QFont, QPixmap
from PyQt6.QtCore import Qt
import sys
import os
import sqlite3
import json
import atexit

def for_atexit():
    print("Bye bro...")

def new_entry():

    global new_entry_window
    

    # URGENT:  Create a cloud activity indicator
    """
    TODO:
    - Implement actual save functionality for entries
    - Add database integration for storing entries
    - Add title field for entries
    - Add mood/tag selection
    - Implement proper window management and cleanup
    - Add keyboard shortcuts (Ctrl+S to save, Ctrl+Q to quit)
    - Add auto-save functionality
    - Add character counter and word count
    - Add proper error handling for database operations
    - Add entry validation (empty content check)
    - Add timestamp display
    """
    print("New entry")
    new_entry_window  = QWidget()
    try:
        new_entry_window.setWindowIcon(QIcon("assets/qappicon.png"))
    except: 
        print("There was an error loading the app icon")
    new_entry_window.setWindowTitle("New Entry")
    new_entry_window.setFixedSize(682, 384)
    layout = QVBoxLayout()
    new_entry_window.setLayout(layout)

    new_entry_label = QLabel("New Entry")
    new_entry_label.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
    layout.addWidget(new_entry_label)
    font = QFont("Arial", 34)
    new_entry_label.setFont(font)

    entry_input = QTextEdit()
    entry_input.setPlaceholderText("Create a journal entry")
    entry_input.setFixedSize(682, 200)
    layout.addWidget(entry_input)

    submit_button = QPushButton("Submit")
    submit_button.setFixedSize(321, 100)
    submit_button.move(20, 20)

    cancel_button = QPushButton("Cancel")
    cancel_button.setFixedSize(321, 100)



    mood_button = QPushButton("Mood")
    mood_button.setFixedSize(682, 50)

    buttonbarlayout = QHBoxLayout()
    layout.addWidget(mood_button)
    buttonbarlayout.addWidget(submit_button)
    buttonbarlayout.addWidget(cancel_button)
    layout.addLayout(buttonbarlayout)



    # TODO: Add save button with proper functionality
    # TODO: Add cancel button
    # TODO: Add mood selection widget
    # TODO: Add tag input system
    # TODO: Add window state management
    
    new_entry_window.show()
    
    # TODO: Prevent window garbage collection
    # TODO: Add proper cleanup on window close

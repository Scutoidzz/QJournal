
from PyQt6.QtWidgets import QWidget, QPushButton, QTextEdit, QVBoxLayout, QLabel, QHBoxLayout
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import Qt
from .mood import mood_picker
import sys
import os  
import sqlite3
import json
import atexit

# TODO: Implement proper entry management syste

def for_atexit():
    """
    TODO: Implement proper application cleanup
    TODO: Add proper resource management
    TODO: Add proper state persistence
    """
    print("""Bye bro...""")

def save_entry():
    """
    TODO: Add proper data validation and sanitization
    TODO: Add proper error handling and user feedback
    TODO: Implement proper timestamp and metadata handling
    """
    # BUG: This currently saves hardcoded text. It should pull from the entry_input widget.
    # TODO: Pass the EntryWindow instance or find a way to access entry_input.toPlainText()
    conn = sqlite3.connect("QJournal.db")
    cursor = conn.cursor()
    #TODO: Add the actual sql options
    cursor.execute("INSERT INTO entries (title, content) VALUES (?, ?)", ("New Entry", "Entry content"))
    conn.commit()
    conn.close()

def go_back():
    """
    TODO: Implement proper window state management
    TODO: Add proper unsaved changes warning
    TODO: Implement proper navigation history
    """
    new_entry_window.close()

def mood():
    mood_picker()
    sqlite3.connect("QJournal.db").cursor().execute("INSERT INTO mood (mood) VALUES (?)", (mood_picker(),))

def new_entry():
    """
    TODO: Implement proper entry creation workflow
    TODO: Add proper template system for entries
    TODO: Add proper spell checking and grammar tools
    """
    global new_entry_window
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
    # TODO: Implement proper rich text editing toolbar
    # TODO: Add proper auto-save functionality
    # TODO: Add proper text formatting options
    entry_input.setPlaceholderText("Create a journal entry")
    entry_input.setFixedSize(642, 200)
    layout.addWidget(entry_input)

    submit_button = QPushButton("Submit")
    submit_button.setFixedSize(321, 100)
    # BUG: submit_button.move(20, 20) has no effect because it's managed by buttonbarlayout later.
    # TODO: Use layout alignment or spacers instead of manual positioning.
    submit_button.move(20, 20)
    
    # TODO: Connect submit_button to save_entry function
    # submit_button.clicked.connect(save_entry)

    cancel_button = QPushButton("Cancel")
    cancel_button.setFixedSize(321, 100)
    cancel_button.clicked.connect(go_back)
    

    # LOWPRIORITY: Add icons to buttons
    # TODO: Implement proper button styling and hover effects
    # TODO: Add proper keyboard shortcuts for buttons
 
    mood_button = QPushButton("Mood") 
    # TODO: Implement proper mood tracking system
    # TODO: Add proper mood selection interface
    # TODO: Add proper mood analytics and insights 
    mood_button.setFixedSize(642, 50)
    mood_button.clicked.connect(mood)

    buttonbarlayout = QHBoxLayout()
    layout.addWidget(mood_button)

    buttonbarlayout.addWidget(submit_button)    
    buttonbarlayout.addWidget(cancel_button)
    layout.addLayout(buttonbarlayout)

    submit_button.clicked.connect(save_entry)
    cancel_button.clicked.connect(go_back)
    
    
    # TODO: Add proper form submission logic
    # TODO: Implement proper window close handling

    new_entry_window.show()
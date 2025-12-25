
from PyQt6.QtWidgets import QWidget, QPushButton, QTextEdit, QVBoxLayout, QLabel, QHBoxLayout
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import Qt
from .mood import mood_picker
import sys
import os  
import sqlite3
import json
import atexit


def for_atexit():
    """
    TODO: Implement proper application cleanup
    TODO: Add proper resource management
    TODO: Add proper state persistence
    """
    print("""Bye bro...""")

def save_entry(entry_input):
    """
    TODO: Add proper data validation and sanitization
    TODO: Add proper error handling and user feedback
    TODO: Implement proper timestamp and metadata handling
    """
    conn = sqlite3.connect("QJournal.db")
    cursor = conn.cursor()
    # TODO: Use parameterized queries for all inputs to prevent SQL injection.
    cursor.execute("INSERT INTO entries (title, content) VALUES (?, ?)", ("Entry", f"{entry_input.toPlainText()}"))
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
    # TODO: Avoid calling mood_picker() multiple times as it might trigger multiple UI popups.
    m = mood_picker()
    sqlite3.connect("QJournal.db").cursor().execute("INSERT INTO mood (mood) VALUES (?)", (m,))

def new_entry():
    """
    TODO: Implement proper entry creation workflow
    """
    global new_entry_window
    print("New entry")
    new_entry_window = QWidget()
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
    entry_input.setFixedSize(642, 200)
    layout.addWidget(entry_input)

    submit_button = QPushButton("Submit")
    submit_button.setFixedSize(321, 100)
    
    cancel_button = QPushButton("Cancel")
    cancel_button.setFixedSize(321, 100)
    cancel_button.clicked.connect(go_back)
    
    mood_button = QPushButton("Mood") 
    mood_button.setFixedSize(642, 50)
    mood_button.clicked.connect(mood)

    buttonbarlayout = QHBoxLayout()
    layout.addWidget(mood_button)

    buttonbarlayout.addWidget(submit_button)    
    buttonbarlayout.addWidget(cancel_button)
    layout.addLayout(buttonbarlayout)

    submit_button.clicked.connect(lambda: save_entry(entry_input))
    cancel_button.clicked.connect(go_back)

    new_entry_window.show()
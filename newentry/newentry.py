from PyQt6.QtWidgets import QWidget, QPushButton, QTextEdit, QVBoxLayout, QLabel, QHBoxLayout
from PyQt6.QtGui import QIcon, QFont, QPixmap
from PyQt6.QtCore import Qt
import sys
import os
import sqlite3
import json
import atexit

def for_atexit():
    print("""Bye bro...""")

def save_entry():
    sqlite3.connect("QJournal.db")

def go_back():
    new_entry_window.close()

def new_entry():
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
    entry_input.setPlaceholderText("Create a journal entry")
    entry_input.setFixedSize(642, 200)
    layout.addWidget(entry_input)

    submit_button = QPushButton("Submit")
    submit_button.setFixedSize(321, 100)
    #TODO: Create a mockup to find the move
    submit_button.move(20, 20)

    cancel_button = QPushButton("Cancel")
    cancel_button.setFixedSize(321, 100)
    cancel_button.clicked.connect(go_back)
    

    # LOWPRIORITY: Add icons to buttons
 
    mood_button = QPushButton("Mood") 
    mood_button.setFixedSize(642, 50)

    buttonbarlayout = QHBoxLayout()
    layout.addWidget(mood_button)

    buttonbarlayout.addWidget(submit_button)    
    buttonbarlayout.addWidget(cancel_button)
    layout.addLayout(buttonbarlayout)

    new_entry_window.show()
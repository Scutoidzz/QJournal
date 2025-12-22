from PyQt6.QtWidgets import QWidget, QPushButton, QTextEdit, QVBoxLayout
from PyQt6.QtGui import QIcon, QFont, QPixmap
from PyQt6.QtCore import Qt
import sys
import os
import sqlite3
import json
import atexit

def new_entry():
    print("New entry")
    window  = QWidget()
    window.setWindowIcon(QIcon("assets/qjournalicon.png"))
    window.setWindowTitle("New Entry")
    window.setFixedSize(682, 384)
    layout = QVBoxLayout()
    window.setLayout(layout)

    new_entry_label = QLabel("New Entry")
    new_entry_label.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
    layout.addWidget(new_entry_label)
    font = ("Arial", 34)
    new_entry_label.setFont(font)

    entry_input = QTextEdit()
    entry_input.setPlaceholderText("Create a journal entry")
    entry_input.setFixedSize(682, 200)
    layout.addWidget(entry_input)
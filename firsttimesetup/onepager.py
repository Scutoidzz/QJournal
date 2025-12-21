from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import Qt
from mainapp.qjournal import qjournal
import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QPushButton
import os 
import sqlite3
import json
import atexit

def onepager():
    print("Setup")
    font = QFont()
    font.setPointSize(30)
    font.setFamily("Arial")
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("QJournal")
    window.setWindowIcon(QIcon("assets/qlogo.png"))
    window.resize(682, 384)
    

    layouth = QVBoxLayout()
    window.setLayout(layouth)
    window.show()
    

    QJournal = QLabel("QJournal")
    QJournal.setFont(font)
    QJournal.setAlignment(Qt.AlignmentFlag.AlignCenter)
    start_button = QPushButton("Start")
    
    layouth.addWidget(QJournal)
    layouth.addWidget(start_button)

    start_button.clicked.connect(qjournal)
    sys.exit(app.exec())

"""
def saver():
    firsttime = {
        "firsttime": "false"
    }

    jsonparsed = json.dumps(firsttime)

    file = open("setup.json", "json")
    with open("setup.json", "a") as f:
        f.write(jsonparsed)
"""



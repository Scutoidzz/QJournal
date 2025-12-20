from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QHBoxLayout, QLabel, QWidget, QVBoxLayout, QTextEdit, QPushButton, QFileDialog
import os 
import sys
import sqlite3
import json
import atexit

def for_atexit():
    print("Starting mainapp")
def onepager(app):
    print("Setup")
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("QJournal")
    window.setWindowIcon(QIcon("assets/qlogo.png"))
    window.resize(600, 400)
    
    layoutv = QVBoxLayout()
    layouth = QHBoxLayout()
    layouth.addLayout(layoutv)
    window.addLayout(layouth)
    window.show()
    

    QJournal = QLabel("QJournal")
    start_button = QPushButton("Start")
    
    layoutv.addWidget(QJournal)
    layoutv.addWidget(QJournal)

def saver():
    firsttime = {
        "firsttime": "false"
    }

    jsonparsed = json.dumps(firsttime)

    file = open("setup.json", "json")
    with open("setup.json", "a") as f:
        f.write(jsonparsed)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    onepager()
    sys.exit(app.exec())



from PyQt6.QtGui import QIcon, QFont, QPixmap
from PyQt6.QtCore import Qt
from mainapp.qjournal import qjournal
import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QPushButton, QFrame, QHBoxLayout
import os 
import sqlite3
import json
import atexit



class QJournalSetup():

    def loadstyle(self):
        with open ("firsttimesetup/fts.qss", "r") as f:
            style = f.read()
            return style


    def onepager(self):
        style = self.loadstyle()
        print("Setup - creating window")
        font = QFont("Arial", 30)
        
        # Get existing QApplication instance
        app = QApplication.instance()
        if app is None:
            app = QApplication(sys.argv)
        
        # Create the main window
        self.window = QWidget()
        self.window.setWindowTitle("QJournal")
        
        try:
            self.window.setWindowIcon(QIcon("assets/qappicon.png"))
            
        except Exception as error:
            print(f"Error with window icon: {error}")
        
        self.window.setFixedSize(682, 384)
        
        layouth = QVBoxLayout()
        self.window.setLayout(layouth)
        self.window.setStyleSheet(style)


        
        QJournal = QLabel("QJournal")
        QJournal.move(291, 50)
        QJournal.setFont(font)

        start_button = QPushButton("Start")
        start_button.move(291, 172)
        start_button.setFixedSize(100, 50)


        layouth.addWidget(QJournal)
        layouth.addWidget(start_button)
        
        # Create a horizontal layout for separator and image
        content_container = QWidget()
        content_layout = QHBoxLayout(content_container)
        content_layout.setContentsMargins(0, 0, 0, 0)
        
        # Create separator
        seperator_line = QFrame()
        seperator_line.setFrameShape(QFrame.Shape.VLine)
        seperator_line.setLineWidth(2)
        seperator_line.setStyleSheet("""
            QFrame {
                background-color: #666;
                color: #666;
                min-height: 382px;
                max-height: 382px;
            }
        """)
        
        original_image = QPixmap("assets/journalsplash.png")
        cropped_image = original_image.copy(0, 0, 341, 382)
        introprinter = QLabel()
        introprinter.setPixmap(cropped_image)
        introprinter.setFixedSize(341, 382)  
        introprinter.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        
        content_layout.addStretch()  
        content_layout.addWidget(introprinter, 1)   
        
        layouth.addWidget(content_container)

        
        start_button.clicked.connect(self.start_qjournal)
        
        print("Setup - showing window")
        self.window.show()
        self.window.raise_() 
        self.window.activateWindow() 
        print("Setup - window should be visible now")
    
    def start_qjournal(self):
        print("Starting QJournal...")
        saver()
        qjournal()



def saver():
    firsttime = {
        "firsttime": "false"
    }

    jsonparsed = json.dumps(firsttime, indent=4)
    
    config_path = "setup.json"
    
    try:
        with open(config_path, 'w') as f:
            f.write(jsonparsed)
    except IOError as e:
        print(f"Error saving configuration: {e}")
        raise


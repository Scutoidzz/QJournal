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
            self.window.setWindowIcon(QIcon("assets/qlogo.png"))
        except Exception as error:
            print(f"Error with window icon: {error}")
        
        self.window.setFixedSize(682, 384)
        
        layouth = QVBoxLayout()
        self.window.setLayout(layouth)
        self.window.setStyleSheet(style)


        
        # TODO: Consider adding a proper application icon and splash screen
        QJournal = QLabel("QJournal")
        QJournal.move(291, 50)
        QJournal.setFont(font)





        # TODO: Add tooltips and accessibility features for better UX
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
        
        # Create image label with cropped image
        original_image = QPixmap("assets/journalsplash.png")
        # Crop to show just the left half of the image (341px)
        cropped_image = original_image.copy(0, 0, 341, 382)
        introprinter = QLabel()
        introprinter.setPixmap(cropped_image)
        introprinter.setFixedSize(341, 382)  # Match the cropped size
        introprinter.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        
        content_layout.addStretch()  # Left spacer to center separator
        content_layout.addWidget(seperator_line)
        content_layout.addWidget(introprinter, 1)  # Stretch to fill remaining space 
        
        layouth.addWidget(content_container)

        
        # TODO: Add error handling for the qjournal function call
        start_button.clicked.connect(self.start_qjournal)
        
        # TODO: Add proper application cleanup on exit
        print("Setup - showing window")
        self.window.show()
        self.window.raise_()  # Bring window to front
        self.window.activateWindow()  # Activate window
        print("Setup - window should be visible now")
    
    def start_qjournal(self):
        """Start the main qjournal application"""
        print("Starting QJournal...")
        saver()  # Save that setup is complete
        qjournal()



def saver():
    """
    Saves the first-time setup status to a JSON file.
    
    TODO: This function has several issues that need to be addressed:
    1. The file opening mode 'json' is invalid, should be 'w' for write
    2. File handles should be properly closed using context managers
    3. Add error handling for file operations
    4. Consider using a more descriptive function name
    5. Add input validation
    6. Consider using a configuration management library
    """
    firsttime = {
        "firsttime": "false"
    }

    # TODO: Use proper indentation for better readability in the JSON file
    jsonparsed = json.dumps(firsttime, indent=4)
    
    # TODO: Use a proper configuration directory (e.g., appdirs library)
    config_path = "setup.json"
    
    try:
        with open(config_path, 'w') as f:
            f.write(jsonparsed)
    except IOError as e:
        # TODO: Implement proper error handling and logging
        print(f"Error saving configuration: {e}")
        raise


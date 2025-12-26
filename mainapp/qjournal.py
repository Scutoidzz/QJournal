from PyQt6.QtWidgets import QApplication, QHBoxLayout, QMainWindow, QPushButton, QVBoxLayout, QWidget, QCalendarWidget, QMessageBox
from PyQt6.QtGui import QFont, QIcon, QAction, QKeySequence
from PyQt6.QtCore import Qt, QDate
import sys
import os
import sqlite3
import logging
import json
from pathlib import Path

from newentry.newentry import new_entry
from standalonemood.mood import main as mood_picker
from .functions.createdb import create_database
from functions.configs import get_db_path, get_app_dir

loggingpath = "log.txt"
logging.basicConfig(filename=loggingpath, level=logging.INFO)

class QJournalWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        create_database()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("QJournal")
        self.setWindowIcon(QIcon("assets/qappicon.png"))
        self.setFixedSize(682, 500)

        # Load Stylesheet
        style_path = Path("mainapp/maintheming.qss")
        if style_path.exists():
            with open(style_path, "r") as f:
                self.setStyleSheet(f.read())
        else:
            logging.warning("maintheming.qss not found")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # Calendar Section
        self.calendar_widget = QCalendarWidget()
        self.calendar_widget.setGridVisible(True)
        self.calendar_widget.clicked.connect(self.view_entries_for_date)
        main_layout.addWidget(self.calendar_widget)

        # Button Section
        button_layout = QHBoxLayout()
        
        self.new_entry_button = QPushButton("New Entry")
        self.new_entry_button.setToolTip("Create a new journal entry (Ctrl+N)")
        self.new_entry_button.setFixedSize(321, 100)
        self.new_entry_button.clicked.connect(new_entry)
        
        self.mood_button = QPushButton("Log Mood Only")
        self.mood_button.setToolTip("Quickly log your mood (Ctrl+M)")
        self.mood_button.setFixedSize(321, 100)
        self.mood_button.clicked.connect(mood_picker)
        
        button_layout.addWidget(self.new_entry_button)
        button_layout.addWidget(self.mood_button)
        main_layout.addLayout(button_layout)

        # Keyboard Shortcuts
        self.setup_shortcuts()

    def setup_shortcuts(self):
        new_entry_action = QAction(self)
        new_entry_action.setShortcut(QKeySequence("Ctrl+N"))
        new_entry_action.triggered.connect(new_entry)
        self.addAction(new_entry_action)

        mood_action = QAction(self)
        mood_action.setShortcut(QKeySequence("Ctrl+M"))
        mood_action.triggered.connect(mood_picker)
        self.addAction(mood_action)

        quit_action = QAction(self)
        quit_action.setShortcut(QKeySequence("Ctrl+Q"))
        quit_action.triggered.connect(self.close)
        self.addAction(quit_action)

    def view_entries_for_date(self, date):
        # Actually QDate.toString("yyyy-MM-dd")
        date_query = date.toString(Qt.DateFormat.ISODate)
        
        logging.info(f"Viewing entries for {date_query}")
        db_path = get_db_path()
        
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute(
                "SELECT title, content, mood, created_at FROM entries WHERE date(created_at) = ?", 
                (date_query,)
            )
            entries = cursor.fetchall()
            conn.close()

            if not entries:
                QMessageBox.information(self, "No Entries", f"No entries found for {date.toString('MMMM d, yyyy')}")
                return

            entry_list = []
            for title, content, mood, created_at in entries:
                time_str = created_at.split()[1] if ' ' in created_at else ""
                entry_list.append(f"<b>{title}</b> at {time_str}<br>Mood: {mood}<br>{content}<hr>")

            msg_box = QMessageBox(self)
            msg_box.setWindowTitle(f"Entries for {date.toString('MMMM d, yyyy')}")
            msg_box.setText("".join(entry_list))
            msg_box.setTextFormat(Qt.TextFormat.RichText)
            msg_box.exec()

        except Exception as e:
            logging.error(f"Error fetching entries: {e}")
            QMessageBox.critical(self, "Database Error", f"Could not fetch entries: {e}")

def save_config(setup_completed=True):
    """
    Saves the configuration to the proper application directory.
    """
    config_path = get_app_dir() / "config.json"
    config_data = {
        "setup_completed": setup_completed,
        "last_updated": Path().absolute().as_posix()
    }
    try:
        with open(config_path, "w") as f:
            json.dump(config_data, f, indent=4)
        logging.info(f"Config saved to {config_path}")
    except Exception as e:
        logging.error(f"Error saving config: {e}")

main_window = None

def qjournal():
    """
    Main entry point for the QJournal application interface.
    """
    global main_window
    main_window = QJournalWindow()
    main_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    qjournal()
    sys.exit(app.exec())
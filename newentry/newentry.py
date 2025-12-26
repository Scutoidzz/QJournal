from PyQt6.QtWidgets import QWidget, QPushButton, QTextEdit, QVBoxLayout, QLabel, QHBoxLayout, QMessageBox
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import Qt
from .mood import mood_picker
import sys
import os  
import sqlite3
import logging
from functions.configs import get_db_path

class NewEntryWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.current_mood = None
        self.is_saved = False
        self.init_ui()

    def init_ui(self):
        try:
            self.setWindowIcon(QIcon("assets/qappicon.png"))
        except Exception: 
            logging.error("There was an error loading the app icon")
        
        self.setWindowTitle("New Entry - QJournal")
        self.setFixedSize(682, 450)
        
        layout = QVBoxLayout()
        self.setLayout(layout)

        new_entry_label = QLabel("New Journal Entry")
        new_entry_label.setFont(QFont("Arial", 24, QFont.Weight.Bold))
        layout.addWidget(new_entry_label)

        self.entry_input = QTextEdit()
        self.entry_input.setPlaceholderText("Write your thoughts here...")
        layout.addWidget(self.entry_input)

        self.mood_label = QLabel("Mood: Not selected")
        layout.addWidget(self.mood_label)

        mood_button = QPushButton("Select Mood") 
        mood_button.clicked.connect(self.pick_mood)
        layout.addWidget(mood_button)

        button_layout = QHBoxLayout()
        
        self.submit_button = QPushButton("Save Entry")
        self.submit_button.clicked.connect(self.save_entry)
        
        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.close)
        
        button_layout.addWidget(self.submit_button)    
        button_layout.addWidget(self.cancel_button)
        layout.addLayout(button_layout)

    def pick_mood(self):
        # For now, keeping the existing mood_picker logic but we should refactor it too
        # To get the value back, we might need to modify mood_picker
        m = mood_picker()
        self.current_mood = m
        self.mood_label.setText(f"Mood: {m if m is not None else 'Selected'}")

    def save_entry(self):
        content = self.entry_input.toPlainText().strip()
        if not content:
            QMessageBox.warning(self, "Empty Entry", "Please write something before saving.")
            return

        db_path = get_db_path()
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            # Standardized title "Journal Entry" or could add a field for it
            cursor.execute(
                "INSERT INTO entries (title, content, mood) VALUES (?, ?, ?)", 
                ("Journal Entry", content, str(self.current_mood) if self.current_mood else None)
            )
            conn.commit()
            conn.close()
            self.is_saved = True
            QMessageBox.information(self, "Saved", "Your journal entry has been saved.")
            self.close()
        except sqlite3.Error as e:
            logging.error(f"Database error while saving entry: {e}")
            QMessageBox.critical(self, "Error", f"Could not save entry: {e}")

    def closeEvent(self, event):
        if not self.is_saved and self.entry_input.toPlainText().strip():
            reply = QMessageBox.question(
                self, 'Unsaved Changes',
                "You have unsaved changes. Are you sure you want to exit?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, 
                QMessageBox.StandardButton.No
            )

            if reply == QMessageBox.StandardButton.Yes:
                event.accept()
            else:
                event.ignore()
        else:
            event.accept()

def new_entry():
    """
    Entry point to launch the New Entry window.
    """
    global _new_entry_window_instance
    _new_entry_window_instance = NewEntryWindow()
    _new_entry_window_instance.show()
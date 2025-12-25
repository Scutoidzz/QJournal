from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QSlider
from PyQt6.QtGui import QFont, QIcon
from PyQt6.QtCore import Qt
import sys
import os
import sqlite3
import json
import atexit
import logging

def save_mood(slider):
    mood = slider.value()
    conn = sqlite3.connect("QJournal.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO mood (mood) VALUES (?)", (mood,))
    conn.commit()
    conn.close()

mood_window = None

def main():
    global mood_window
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    mood_window = QWidget()
    window = mood_window
    window.setWindowIcon(QIcon("assets/qappicon.png"))
    window.setWindowTitle("Mood Picker")
    window.setFixedSize(682, 384)
    layout = QVBoxLayout()
    window.setLayout(layout)
    mood_label = QLabel("Mood")
    mood_label.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
    layout.addWidget(mood_label)
    font = QFont("Inter, Helvetica, Arial", 34)
    mood_label.setFont(font)
    mood_slider = QSlider(Qt.Orientation.Horizontal)
    mood_slider.setRange(0, 40)
    mood_slider.setValue(20)
    mood_slider.setTickPosition(QSlider.TickPosition.NoTicks)
    mood_slider.setTickInterval(1)
    mood_slider.setSingleStep(1)
    mood_slider.setFixedSize(642, 50)
    layout.addWidget(mood_slider)

    mood_button = QPushButton("Save")
    mood_button.setFixedSize(642, 50)
    layout.addWidget(mood_button)
    mood_button.clicked.connect(lambda: save_mood(mood_slider))
    window.show()
    
    if __name__ == "__main__":
        sys.exit(app.exec())
    else:
        app.exec()
from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QSlider
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
import sys
import os
import sqlite3
import json
import atexit
import logging

def main():
    window = QWidget()
    window.setWindowIcon(QIcon("assets/qappicon.png"))
    window.setWindowTitle("Mood Picker")
    window.setFixedSize(682, 384)
    layout = QVBoxLayout()
    window.setLayout(layout)
    mood_label = QLabel("Mood")
    mood_slider = QSlider(Qt.Orientation.Horizontal)
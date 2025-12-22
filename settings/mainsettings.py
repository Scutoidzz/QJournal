from PyQt6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QLineEdit, QGridLayout
import sys
from PyQt6.QtCore import Qt
import os

def settings_window():
    layout = QVBoxLayout()
    window = QWidget()
    window.setLayout(layout)
    
    search_bar = QLineEdit()
    search_bar.setFrameShape(Qt.FrameShape.BoxShape)
    search_bar.setFlags(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignTop)
    
    layout.addWidget(search_bar)

    settings_label = QLabel("Settings")
    layout.addWidget(settings_label)

    sys.exit(app.exec())
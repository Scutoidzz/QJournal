from PyQt6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QLineEdit, QGridLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QPixmap
import os
import sys


settings_window_instance = None

def settings_window():
    global settings_window_instance
    layout = QVBoxLayout()
    window = QWidget()
    window.setLayout(layout)
    
    search_bar = QLineEdit()
    search_bar.setAlignment(Qt.AlignmentFlag.AlignCenter)
    search_bar.setPlaceholderText("Search")

    layout.addWidget(search_bar)

    settings_label = QLabel("Settings")
    layout.addWidget(settings_label)

    cloud_button = QPushButton("Cloud")

    sync_to_cloud_button = QPushButton("Sync to Cloud")
    sync_to_cloud_button.setFixedSize(125, 50)

    cloud_button.move(200, 20)
    
    layout.addWidget(cloud_button)




    if settings_window_instance is not None:
        settings_window_instance.close()
    
    window.setWindowTitle("Settings")
    window.setFixedSize(682, 384)
    window.show()
    
    settings_window_instance = window

    
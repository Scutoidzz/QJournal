from PyQt6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QLineEdit, QGridLayout
from PyQt6.QtCore import Qt
import os

# Global reference to prevent garbage collection
settings_window_instance = None

def settings_window():
    global settings_window_instance
    #TODO: Add the rest of the settings buttons
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
    cloud_button.setFixedSize(100, 50)
    #TODO: Improve button locations 

    cloud_button.move(200, 20)




    # Close previous settings window if exists
    if settings_window_instance is not None:
        settings_window_instance.close()
    
    window.setWindowTitle("Settings")
    window.setFixedSize(682, 384)
    window.show()
    
    # Store reference to prevent garbage collection
    settings_window_instance = window

    
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt6.QtGui import QIcon, QPixmap
import sys
import os

def cloud_settings():
    print("Loading the cloud settings...")
    window = QWidget()
    window.setWindowTitle("Cloud Settings")
    window.setWindowIcon(QIcon("assets/qappicon.png"))
    window.setFixedSize(682, 384)
    layout = QVBoxLayout()
    window.setLayout(layout)
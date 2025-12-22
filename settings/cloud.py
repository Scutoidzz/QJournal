from PyQt6.QtWidgets import QFrame, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QPixmap
import requests

def cloud_settings():
    print("Loading cloud settings")
    window = QWidget()
    window.setWindowTitle("Cloud Settings")
    layout = QHBoxLayout()
    window.setLayout(layout)

    backbox = QFrame
    backbox.setframeShape(QFrame.Shape.StyledPanel)
    backbox.setFrameShadow(QFrame.Shadow.Raised)
    layout.addWidget(backbox)

    providerlabel = QLabel("Provider")
    layout.addWidget(providerlabel)
    providerlabel.move(10, 10)
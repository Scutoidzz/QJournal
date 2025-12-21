from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel
from PyQt6.QtGui import QImage, QIcon, QPixmap
import os
import sys
import time 

#ToDO: create a first time splash screen
def splash():
    window = QWidget()
    window.setWindowTitle("QJournal")
    window.setWindowIcon(QIcon("assets/qlogo.png"))
    window.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
    layout = QHBoxLayout()
    window.setLayout(layout)
    window.setFixedSize(682, 384)
    print("Starting")
    screen_image = QPixmap("assets/journalsplash.png")
    layout.addWidget(QLabel(screen_image))
    time.sleep(5)
    


    #TODO: Create an image for the splash screen
    #TODO: Close after 5 seconds with time.sleep(5)
    
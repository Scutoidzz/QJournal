from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QHBoxLayout, QSlider
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import Qt
import os
import sys

def mood_to_entry(mood_slider):
    mood_window.close()
    return mood_slider

def mood_picker():
    global mood_window
    
    mood_window = QWidget()
    mood_window.setWindowIcon(QIcon("assets/qappicon.png"))
    mood_window.setWindowTitle("Mood Picker")
    mood_window.setFixedSize(682, 384)
    layout = QVBoxLayout()
    mood_window.setLayout(layout)
    mood_slider = QSlider(Qt.Orientation.Horizontal)
    mood_slider.setRange(0, 20)
    mood_slider.setValue(10)
    mood_slider.setTickPosition(QSlider.TickPosition.TicksLeft)
    mood_slider.setTickInterval(1)
    mood_slider.setSingleStep(1)

    mood_slider.setPageStep(1)
    mood_slider.setTracking(True)
    mood_slider.setStyleSheet("mood.qss")
    layout.addWidget(mood_slider)
    
    submit_to_entry = QPushButton("Submit")
    submit_to_entry.setFixedSize(321, 100)
    submit_to_entry.clicked.connect(lambda: mood_to_entry(mood_slider.value()))
    submit_to_entry.move(341, 284)
    layout.addWidget(submit_to_entry)
    
    
    
    mood_window.show()
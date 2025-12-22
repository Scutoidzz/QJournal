from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QSlider, QCheckBox, QRadioButton, QPushButton
from PyQt6.QtCore import Qt


class QSwitch(QtWidgets.QSlider):
    def __init__(self):
        super().__init__()
        unedited = QSlider()
        unedited.setOrientation(Qt.Orientation.Horizontal)
        unedited.setMinimum(0)
        unedited.setMaximum(1)
        unedited.setValue(0)
        unedited.setStyleSheet("QSlider::groove:horizontal { height: 10px; background: #ccc; border-radius: 5px;}")

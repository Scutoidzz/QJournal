from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QSlider, QCheckBox, QRadioButton, QPushButton
from PyQt6.QtCore import Qt


class QSwitch(QtWidgets.QSlider):
    def __init__(self, parent=None):
        super().__init__(parent)
        unedited = QSlider()
        unedited.setOrientation(Qt.Orientation.Horizontal)
        unedited.setMinimum(0)
        unedited.setMaximum(1)
        unedited.setValue(0)
        unedited.setStyleSheet("QSlider::groove:horizontal { height: 10px; background: #ccc; border-radius: 5px;}  QSlider::groove:horizontal:hover {height: 10px; background: #fff; border-radius: 0px;}")
        
        # See if this is callable
        return unedited.value()

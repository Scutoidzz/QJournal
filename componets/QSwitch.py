from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QSlider
from PyQt6.QtCore import Qt


class QSwitch(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        unedited = QSlider()
        unedited.setOrientation(Qt.Orientation.Horizontal)
        unedited.setMinimum(0)
        unedited.setMaximum(1)
        unedited.setValue(0)
        #TODO: Implement the rest of the switch
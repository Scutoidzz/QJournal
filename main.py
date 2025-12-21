import sys
import os
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton, QFileDialog
import json
import time
from firsttimesetup.onepager import onepager

configuration = config.json

if config.json == "" or config.json == None or config.json == "{}":
    firsttimeuse = True
else:
    firsttimeuse = False

if firsttimeuse:
    onepager()



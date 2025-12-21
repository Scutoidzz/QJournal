import sys
import os
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton, QFileDialog
import json
import time
from mainapp.qjournal import qjournal
from firsttimesetup.onepager import QJournalSetup
from splash.splashscreen import splash
try:
    config = json.load(open("config.json", "r"))
except FileNotFoundError:
    with open("config.json", 'x') as f:
        f.write("{}")
    time.sleep(1)
    json.load(open("config.json", "r"))


if config == "" or config == "{}":
    firsttimeuse = 1
else:
    firsttimeuse = 0

if firsttimeuse == 1:
    splash()
    QJournalSetup() 
else: 
    qjournal()



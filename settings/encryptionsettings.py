from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QPushButton, QRadioButton
import os
import sys
import time
from .functions.configs import os_name, os_version

def encryption_settings():
    backendlabel = QLabel("Encryption Backend")
    encryption_none = QRadioButton("Plain Encryption")
    encryption_base = QRadioButton("Base64 Encryption")
    encryption_hashlib = QRadioButton("Hashlib Encryption")
    encryption_hashlib.setToolTip("Requires a password to use")
    encryption_none.setToolTip("No encryption")
    encryption_base.setToolTip("Best for most users")

    # See if this fixes the garbage collection issues
    return encryption_none, encryption_base, encryption_hashlib

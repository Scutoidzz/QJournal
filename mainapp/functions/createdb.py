import sqlite3
import os
import sys
from .configs import get_configurations

from pathlib import Path

def create_database():
    sqlite3.connect("qJournal.db")
    s3 = sqlite3.cursor()
    s3.execute("CREATE TABLE IF NOT EXISTS entries (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, content TEXT, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")
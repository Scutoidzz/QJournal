import sqlite3 
import os
import sys
import json

sqlite3.connect("qJournal.db")
cursor = sqlite3.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS entries (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, content TEXT, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")

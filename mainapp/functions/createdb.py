import sqlite3
import os
import sys
from .configs import get_configurations
from pathlib import Path

def create_database():
    try:
        # Create a database connection and get a cursor
        conn = sqlite3.connect("qJournal.db")
        cursor = conn.cursor()
        
        # Create the table if it doesn't exist
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS entries (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                title TEXT, 
                content TEXT, 
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Commit the changes
        conn.commit()
        return True
        
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False
    finally:
        # Make sure connection is closed
        if 'conn' in locals():
            conn.close()
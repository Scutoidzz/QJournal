import sqlite3
import os
import sys
import logging
from functions.configs import get_db_path
from pathlib import Path

def create_database():
    """  
    Initializes the database with necessary tables and schema.
    """
    db_path = get_db_path()
    try:
        logging.info(f"Initializing database at {db_path}")
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Create the entries table with mood column
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS entries (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                title TEXT, 
                content TEXT, 
                mood TEXT,
                tags TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Add basic indexes
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_entries_created_at ON entries(created_at)")
        
        conn.commit()
        return True
        
    except sqlite3.Error as e:
        logging.error(f"Database creation error: {e}")
        return False
    finally:
        if 'conn' in locals():
            conn.close()
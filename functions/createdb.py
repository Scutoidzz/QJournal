import sqlite3 
import os
import sys
import json
import logging as log
import regex

def log_errors():
    log.basicConfig(level=log.ERROR)
    

def create_database():
    """
    TODO:
    - Add database migration support for schema changes
    - Implement proper database connection pooling
    - Add database backup and recovery mechanisms
    - Add database indexing for better performance
    """
    # TODO: Make database path configurable
    # TODO: Add proper error handling for database file permissions
    conn = sqlite3.connect("qJournal.db")
    
    try:
        cursor = conn.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS entries (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                title TEXT, 
                content TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                mood INTEGER,
                tags TEXT,
                regex_detected TEXT
            )
        """) 
        
        # Commit the changes and close the connection
        conn.commit()
        return True
        
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        print("Create an issue on GitHub at scutoidzz/QJournal")
        
        return False
    finally:
        if conn:
        
            conn.close()

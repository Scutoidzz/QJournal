import sqlite3
import os
from pathlib import Path

def create_database():
    """
    Create a new SQLite database for QJournal if it doesn't exist.
    Returns the database connection.
    """
    # Get the user's home directory
    home = str(Path.home())
    
    # Create .qjournal directory if it doesn't exist
    qjournal_dir = os.path.join(home, '.qjournal')
    os.makedirs(qjournal_dir, exist_ok=True)
    
    # Database file path
    db_path = os.path.join(qjournal_dir, 'qjournal.db')
    
    # Connect to SQLite database (creates it if it doesn't exist)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Create tables if they don't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS entries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        content TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    
    # Create a table for tags
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tags (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL
    )
    ''')
    
    # Create a table for entry-tag relationships
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS entry_tags (
        entry_id INTEGER,
        tag_id INTEGER,
        PRIMARY KEY (entry_id, tag_id),
        FOREIGN KEY (entry_id) REFERENCES entries (id) ON DELETE CASCADE,
        FOREIGN KEY (tag_id) REFERENCES tags (id) ON DELETE CASCADE
    )
    ''')
    
    # Create an index for faster lookups
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_entries_created ON entries(created_at)')
    
    # Commit changes and return the connection
    conn.commit()
    return conn

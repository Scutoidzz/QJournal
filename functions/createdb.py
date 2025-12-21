"""
Database creation and management module for QJournal.

This module handles the creation and initialization of the SQLite database
used by the QJournal application.

TODO:
- Add database migration support for schema updates
- Implement database connection pooling
- Add support for database encryption
- Add database backup functionality
- Add database integrity checks
- Add support for multiple database backends (SQLite, PostgreSQL, etc.)
- Add database performance optimization
- Add proper logging instead of print statements
- Add support for database transactions
- Add database connection retry logic
"""

import os
import sqlite3 as sql
from pathlib import Path
from typing import Optional, Dict, Any, List, Tuple

# TODO: Move to configuration
DATABASE_PATH = "qjournal.db"
SCHEMA_VERSION = 1

# TODO: Consider using an ORM like SQLAlchemy or peewee
# TODO: Add proper type hints for database operations

def get_database_connection() -> sql.Connection:
    """Create and return a database connection.
    
    Returns:
        sql.Connection: A connection to the SQLite database.
        
    Raises:
        sql.Error: If the connection cannot be established.
    """
    try:
        # TODO: Add connection pooling
        conn = sql.connect(DATABASE_PATH)
        # Enable foreign key constraints
        conn.execute("PRAGMA foreign_keys = ON")
        return conn
    except sql.Error as e:
        # TODO: Add proper error handling and logging
        print(f"Error connecting to database: {e}")
        raise

def create_database() -> None:
    """Initialize the database with the required tables and schema.
    
    This function creates the database file if it doesn't exist and ensures
    all required tables are present with the correct schema.
    
    Raises:
        sql.Error: If there's an error creating the database or tables.
    """
    # Create database directory if it doesn't exist
    db_path = Path(DATABASE_PATH)
    db_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Check if database exists and get its version
    db_exists = db_path.exists()
    
    try:
        with get_database_connection() as conn:
            cursor = conn.cursor()
            
            # Create version table if it doesn't exist
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS schema_version (
                    version INTEGER PRIMARY KEY,
                    applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            if not db_exists:
                # This is a new database, set the initial version
                cursor.execute('''
                    INSERT INTO schema_version (version) VALUES (?)
                ''', (SCHEMA_VERSION,))
                
                # Create tables for a new database
                _create_initial_schema(cursor)
                conn.commit()
                print(f"Created new database at {DATABASE_PATH}")
            else:
                # Existing database - check if schema needs to be updated
                cursor.execute('SELECT MAX(version) FROM schema_version')
                current_version = cursor.fetchone()[0] or 0
                
                if current_version < SCHEMA_VERSION:
                    # TODO: Implement database migrations
                    print(f"Database needs migration from version {current_version} to {SCHEMA_VERSION}")
                    # _migrate_database(conn, current_version, SCHEMA_VERSION)
    
    except sql.Error as e:
        print(f"Error initializing database: {e}")
        # TODO: Add proper error handling and rollback
        raise

def _create_initial_schema(cursor: sql.Cursor) -> None:
    """Create the initial database schema.
    
    Args:
        cursor: Database cursor to execute SQL commands.
        
    TODO:
    - Add more tables as needed (tags, categories, etc.)
    - Add proper indexes for performance
    - Add constraints and data validation
    - Consider using a schema migration tool
    """
    # Journal entries table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            is_pinned BOOLEAN DEFAULT 0,
            is_archived BOOLEAN DEFAULT 0,
            word_count INTEGER DEFAULT 0,
            mood_rating INTEGER CHECK(mood_rating >= 1 AND mood_rating <= 5),
            -- TODO: Add more fields as needed
            -- location TEXT,
            -- weather TEXT,
            -- tags TEXT,  -- Consider a separate tags table
            UNIQUE(created_at) ON CONFLICT REPLACE
        )
    ''')
    
    # Tags table (for categorizing entries)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tags (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            color TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Entry-tag relationship (many-to-many)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS entry_tags (
            entry_id INTEGER,
            tag_id INTEGER,
            PRIMARY KEY (entry_id, tag_id),
            FOREIGN KEY (entry_id) REFERENCES entries (id) ON DELETE CASCADE,
            FOREIGN KEY (tag_id) REFERENCES tags (id) ON DELETE CASCADE
        )
    ''')
    
    # Create indexes for better query performance
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_entries_created_at ON entries(created_at)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_entries_updated_at ON entries(updated_at)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_entries_is_pinned ON entries(is_pinned)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_entries_is_archived ON entries(is_archived)')
    
    # TODO: Add more tables as needed (attachments, reminders, etc.)

def _migrate_database(conn: sql.Connection, from_version: int, to_version: int) -> None:
    """Migrate the database schema from one version to another.
    
    Args:
        conn: Database connection.
        from_version: Current database version.
        to_version: Target database version.
        
    TODO: Implement proper database migrations
    """
    # TODO: Implement database migration logic
    # This is a placeholder for future migration logic
    pass

# TODO: Add more database utility functions as needed
def backup_database(backup_path: str = None) -> str:
    """Create a backup of the database.
    
    Args:
        backup_path: Path where to save the backup. If None, creates a timestamped backup.
        
    Returns:
        str: Path to the created backup file.
        
    TODO:
    - Add compression for backups
    - Add support for incremental backups
    - Add verification of backup integrity
    """
    import shutil
    from datetime import datetime
    
    if backup_path is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = f"{DATABASE_PATH}.backup_{timestamp}"
    
    try:
        shutil.copy2(DATABASE_PATH, backup_path)
        print(f"Database backup created at {backup_path}")
        return backup_path
    except Exception as e:
        print(f"Error creating database backup: {e}")
        raise

# TODO: Add more database utility functions as needed
# - get_entry_count()
# - get_entries_by_date_range()
# - search_entries()
# - get_tags_for_entry()
# - add_tag_to_entry()
# - remove_tag_from_entry()
# - etc.
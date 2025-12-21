import os
from pathlib import Path

def get_config():
    """
    Get the application configuration.
    Returns a dictionary with configuration values.
    """
    # Get the user's home directory
    home = str(Path.home())
    qjournal_dir = os.path.join(home, '.qjournal')
    
    # Ensure the .qjournal directory exists
    os.makedirs(qjournal_dir, exist_ok=True)
    
    # Database path
    db_path = os.path.join(qjournal_dir, 'qjournal.db')
    
    # Application configuration
    config = {
        'database': {
            'path': db_path,
            'type': 'sqlite'
        },
        'app': {
            'name': 'QJournal',
            'version': '1.0.0',
            'data_dir': qjournal_dir,
            'log_file': os.path.join(qjournal_dir, 'qjournal.log')
        },
        'ui': {
            'theme': 'dark',  # Can be 'light' or 'dark'
            'font_size': 12,
            'recent_entries_limit': 10
        }
    }
    
    return config

def get_database_path():
    """Helper function to get just the database path."""
    return get_config()['database']['path']

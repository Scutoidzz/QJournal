import os
import sys
import platform
import logging
import getpass
from pathlib import Path

# Constants
APP_NAME = "QJournal"

def get_app_dir():
    """Returns the application directory in the user's home folder."""
    home = Path.home()
    if sys.platform == "win32":
        app_dir = home / "AppData" / "Roaming" / APP_NAME
    elif sys.platform == "darwin":
        app_dir = home / "Library" / "Application Support" / APP_NAME
    else:
        app_dir = home / ".config" / APP_NAME
    
    app_dir.mkdir(parents=True, exist_ok=True)
    return app_dir

def get_db_path():
    """Returns the path to the main database file."""
    return get_app_dir() / "qJournal.db"

# a file with system variables.

def os_name():
    """
    Returns a normalized OS name string.
    """
    try:
        system = platform.system().lower()
        if "linux" in system:
            return "linux"
        elif "windows" in system:
            return "windows"
        elif "darwin" in system:
            return "mac"
        elif "java" in system:
            return "java"
        return system
    except Exception as e:
        logging.error(f"Error getting OS name using platform: {e}")
        # Fallback to os.name
        osname = os.name
        if osname == "posix":
            return "linux"
        elif osname == "nt":
            return "windows"
        return osname

def os_version():
    """
    Returns the operating system's release version.
    """
    try:
        # platform.release() gives the version/release (e.g., '10' for Windows or '5.15.0' for Linux)
        version = platform.release()
        return version
    except Exception as e:
        logging.error(f"Error getting OS version: {e}")
        return "Unknown"

def username():
    """
    Returns the current logged-in username with multiple fallbacks.
    """
    try:
        # getpass.getuser() looks at environment variables and password database
        return getpass.getuser()
    except Exception as e:
        logging.error(f"Error getting username using getpass: {e}")
        # Manual fallbacks for environment variables
        return os.environ.get("USER") or os.environ.get("USERNAME") or os.environ.get("LOGNAME") or "unknown_user"
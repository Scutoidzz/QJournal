import sys
import os
from PyQt6.QtWidgets import QApplication, QMessageBox
import json
import argparse
import traceback
import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
from mainapp.qjournal import qjournal
from firsttimesetup.onepager import QJournalSetup
from splash.splashscreen import splash

# Constants
APP_NAME = "QJournal"
DEFAULT_CONFIG_NAME = "config.json"
DEFAULT_LOG_NAME = "log.txt"

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

def setup_logging():
    """Configures centralized logging with rotation."""
    app_dir = get_app_dir()
    log_path = app_dir / DEFAULT_LOG_NAME
    
    handler = RotatingFileHandler(log_path, maxBytes=1024*1024*5, backupCount=5)
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[handler, logging.StreamHandler(sys.stdout)]
    )
    return log_path

def load_config():
    """
    Loads configuration with support for user home directory,
    environment variable overrides, and local migration.
    """
    app_dir = get_app_dir()
    config_path = app_dir / DEFAULT_CONFIG_NAME
    
    # Environment variable override
    env_config = os.environ.get("QJOURNAL_CONFIG")
    if env_config:
        config_path = Path(env_config)

    try:
        if not config_path.exists():
            # Check for local config for migration
            local_config = Path(DEFAULT_CONFIG_NAME)
            if local_config.exists():
                logging.info("Migrating local config to application directory...")
                with open(local_config, "r") as f:
                    config = json.load(f)
                with open(config_path, "w") as f:
                    json.dump(config, f, indent=4)
                return config
            return {}

        with open(config_path, "r") as f:
            config = json.load(f)
        logging.info(f"Config loaded successfully from {config_path}")
        return config
    except Exception as e:
        logging.error(f"Error loading config: {e}")
        return {}

def main():
    setup_logging()
    
    argparser = argparse.ArgumentParser(description="QJournal - A Personal Privacy-Focused Journal")
    argparser.add_argument("--config", type=str, help="Path to custom configuration file")
    args = argparser.parse_args()

    if args.config:
        os.environ["QJOURNAL_CONFIG"] = args.config

    logging.info("Starting QJournal...")
    
    # Create the QApplication instance here so it lives throughout the app life
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)

    config = load_config()
    
    # Standardized key: setup_completed
    # Support migration from 'first' key or setup.json
    setup_completed = config.get("setup_completed") or config.get("first") == "false"
    
    # Check for setup.json (legacy fallback)
    if not setup_completed and Path("setup.json").exists():
        try:
            with open("setup.json", "r") as f:
                setup_data = json.load(f)
                if setup_data.get("firsttime") == "false":
                    setup_completed = True
        except:
            pass

    if not setup_completed:
        logging.info("First time use or setup incomplete detected")
        # splash handles its own loop or just shows and returns
        splash() 
        setup = QJournalSetup()
        setup.onepager()
    else:
        logging.info("Setup already completed.")
        try:
            qjournal()
        except Exception as error:
            logging.error(f"Application error: {error}")
            logging.error(traceback.format_exc())
            QMessageBox.critical(None, "Error", f"A critical error occurred: {error}")
            return

    # Start the event loop
    sys.exit(app.exec())


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nGoodbye!")
    except Exception as error:
        logging.critical(f"Unhandled exception: {error}")
        logging.critical(traceback.format_exc())
        print(f"Fatal error: {error}")


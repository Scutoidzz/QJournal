import os
import json
import logging
from pathlib import Path
from functions.configs import get_app_dir

CONFIG_FILENAME = "config.json"

def get_configurations():
    """
    Loads application configurations with merging and error handling.
    """
    config_path = get_app_dir() / CONFIG_FILENAME
    
    # Default configuration schema
    config = {
        "setup_completed": False,
        "theme": "default",
        "language": "en",
        "last_opened_date": None
    }

    try:
        if config_path.exists():
            with open(config_path, "r") as f:
                stored_config = json.load(f)
                config.update(stored_config)
        else:
            logging.info("No config file found, using defaults.")
    except Exception as e:
        logging.error(f"Failed to load configurations: {e}")
    
    return config

def update_configuration(key, value):
    """
    Updates a specific configuration key and saves to file.
    """
    config = get_configurations()
    config[key] = value
    
    config_path = get_app_dir() / CONFIG_FILENAME
    try:
        with open(config_path, "w") as f:
            json.dump(config, f, indent=4)
        return True
    except Exception as e:
        logging.error(f"Failed to save configuration: {e}")
        return False
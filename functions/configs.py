
import os
import sys
import platform
import logging

# a file with system variables.
# TODO: Implement proper system information gathering
# TODO: Add proper platform-specific optimizations

def os_name():
    #TODO Add these entries to exception handling
    try:
        osname = os.name
        if osname == "posix":
            osname = "linux"
        elif osname == "nt":
            osname = "windows"
        elif osname == "java":
            osname = "java"
        elif osname == "darwin":
            osname = "mac"
    except:
        logging.error("There was an error getting the OS name")
        logging.info("switching to platform")
        osname = platform.system()
    return osname

def os_version():
    """
    TODO: Implement proper version parsing and normalization
    TODO: Add proper error handling and logging
    TODO: Add support for version comparison utilities
    """
    try:
        osversion = sys.version
        osversionstring = platform.version()
    except: 
        print("There was an error getting the OS name")
    return osversion

def username():
    """
    TODO: Implement proper username detection with fallbacks
    TODO: Add proper error handling and logging
    TODO: Add support for different user name formats
    """

    try:
        username = os.getlogin()
    except:
        print("There was an error getting the username")
    return username
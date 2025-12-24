
import os
import sys
import platform

# a file with system variables.
# TODO: Implement proper system information gathering
# TODO: Add proper error handling and logging
# TODO: Add proper platform-specific optimizations

def os_name():
    """
    TODO: Implement proper OS detection with fallbacks
    TODO: Add proper error handling and logging
    TODO: Add support for more OS variants
    """
    
    try:
        osname = os.name
    except:
        print("There was an error getting the OS name")
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
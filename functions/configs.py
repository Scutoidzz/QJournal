
import os
import sys
import platform

# a file with system variables.

def os_name():
    
    try:
        osname = os.name
    except:
        print("There was an error getting the OS name")
    return osname

def os_version():
    try:
        osversion = sys.version
        osversionstring = platform.version()
    except: 
        print("There was an error getting the OS name")
    return osversion

def username():

    try:
        username = os.getlogin()
    except:
        print("There was an error getting the username")
    return username
import os
import sys
import platform

# a file with system variables.

def os_name():
    osname = os.name
    return osname

def os_version():
    osversion = sys.version
    return osversion

def username():
    username = os.getlogin()
    return username
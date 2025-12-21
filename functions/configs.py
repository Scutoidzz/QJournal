import os
import sys

# a file with system variables.

def os_name():
    osname = os.name()
    return osname

def os_version():
    osversion = os.uname().version
    return osversion
#!usr/bin/env python3
""" Demonstrating Subprocesses"""
__author__= 'Eva Linehan (eva.linehan18@imperial.ac.uk)'
__version__ = 0.01
__date__ = 'Nov 2018'
__licence__ = 'OS Practical'

""" This is blah blah"""

# Use the subprocess.os module to get a list of files and directories 
# in your ubuntu home directory 

# Hint: look in subprocess.os and/or subprocess.os.path and/or 
# subprocess.os.walk for helpful functions

import subprocess
import re

#################################
#~Get a list of files and 
#~directories in your home/ that start with an uppercase 'C'

# Type your code here:

# Get the user's home directory.
home = subprocess.os.path.expanduser("~")

# Create a list to store the results.
FilesDirsStartingWithC = []
FDSWCc = []
DSWCc = []
# Use a for loop to walk through the home directory.

for (directory, subdir, files) in subprocess.os.walk(home):
    for name in subdir:
       if re.match('C', name):
           FilesDirsStartingWithC.append(name) 
    for name in files:
        if re.match('C', name):
            FilesDirsStartingWithC.append(name)
print(FilesDirsStartingWithC)
  
#################################
# Get files and directories in your home/ that start with either an 
# upper or lower case 'C'

# Type your code here:
for (directory, subdir, files) in subprocess.os.walk(home):
    for name in subdir:
       if re.match('^[Cc]', name):
           FDSWCc.append(name) 
    for name in files:
        if re.match('^[Cc]', name):
            FDSWCc.append(name)
print(FDSWCc)



#################################
# Get only directories in your home/ that start with either an upper or 
#~lower case 'C' 

# Type your code here:
for (directory, subdir, files) in subprocess.os.walk(home):
    for name in subdir:
       if re.match('^[Cc]', name):
           DSWCc.append(name) 
print(DSWCc)


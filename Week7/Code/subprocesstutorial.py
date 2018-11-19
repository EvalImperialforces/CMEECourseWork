#!usr/bin/env python3
""" Demonstrating Subprocesses"""
__author__= 'Eva Linehan (eva.linehan18@imperial.ac.uk)'
__version__ = 0.01
__date__ = 'Nov 2018'
__licence__ = 'In class exercise'

import subprocess

p = subprocess.Popen(["echo","I'm talkin' to you bash!"], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
# Unix need a standard input and 2 outputs (output or error)
# Spawning 2 outs - invoking shell env. and runs command
# If you want to do anything with output then you pipe it

stdout, stderr = p.communicate(timeout=60) 
# Opens the pipes
# try and accept clause - timeout after specified time so you know
# whether it worked it or not.
# p.kill

stderr
# Encoded: operating in bytes

stdout
# Needs to be decoded
print(stdout.decode())

p = subprocess.Popen(["ls", "-l"], stdout=subprocess.PIPE)
stdout, stderr = p.communicate()
print(stdout.decode())

p = subprocess.Popen(["python", "boilerplate.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE) # A bit silly! 
stdout, stderr = p.communicate()
print(stdout.decode())

MyPath = subprocess.os.path.join('directory', 'subdirectory', 'file')
MyPath


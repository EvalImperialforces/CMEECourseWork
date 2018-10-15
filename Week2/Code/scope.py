#!/usr/bin/env python3
""" Script to test local and global variables. """
__author__= 'Eva Linehan (eva.linehan18@imperial.ac.uk)'
__version__ = 0.01
__date__ = 'Oct 2018'
__licence__ = 'Inclass practical'


## Try this first

_a_global = 10

def a_function():
    """ Prints defined variables within function"""
    _a_global = 5
    _a_local = 4
    print ("Inside the function, the value is", _a_global)
    print ("Inside the function, the value is", _a_local)
    return None

a_function()
print("Outside the function, the value is", _a_global)
# Prints global variable 

## Now try this

_a_global = 10

def a_function():
    """ Prints defined variables within function """
    global _a_global #This variable can now be used inside and outside the function
    _a_global = 5
    _a_local = 4
    print ("Inside the function, the value is", _a_global)
    print ("Inside the function, the value is", _a_local)
    return None

a_function()
print("Outside the function, the value is", _a_global)

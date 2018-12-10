#!/usr/bin/env python3
""" Boilerplate example. """
__appname__ = '[boilerplate.py]'
__author__  = 'Eva Linehan (eval2495@gmail.com)'
__version__ = '0.0.1'
__licence__ = 'Test'

## imports ##
import sys # module to interface our program with the operating system

## constants ##

## functions ##
def main(argv):
    """ Main entry point of the program """
    print ('This is a boilerplate')
    return 0

if __name__ =="__main__":
    print('This program is being run by itself')
    status = main(sys.argv)
    sys.exit(status)

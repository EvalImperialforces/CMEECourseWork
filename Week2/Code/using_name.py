#!/usr/bin/env python3
""" Script to test __name__ = __main__ function. """
__author__= 'Eva Linehan (eva.linehan18@imperial.ac.uk)'
__version__ = 0.01
__date__ = 'Oct 2018'
__licence__ = 'Inclass practical'

# Filename: using_name.py

if __name__ == '__main__':
    print('This program is being run by itself')
else:
    print('I am being imported from another module')
    

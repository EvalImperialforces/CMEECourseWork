#!/usr/bin/env python3
""" Sample script to understand debugger. """
__author__= 'Eva Linehan (eva.linehan18@imperial.ac.uk)'
__version__ = 0.01
__date__ = 'Oct 2018'
__licence__ = 'Inclass practical'

def createabug(x=0):
    """ Function to divide x ^^3 by 0 which does not compute. """
    y=x**3
    import ipdb; ipdb.set_trace()
    z=0
    y=y/z
    return y

createabug(2)

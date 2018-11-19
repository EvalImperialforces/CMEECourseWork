#!usr/bin/env python3
""" Demonstrating profililng in Python."""
__author__= 'Eva Linehan (eva.linehan18@imperial.ac.uk)'
__version__ = 0.01
__date__ = 'Nov 2018'
__licence__ = 'In class exercise'


def my_squares(iters):
# Squaring values and adding to list "out".
    out = []
    for i in range(iters):
        out.append(i**2) # Add squared "iters" value each time
    return out

def my_join(iters, string):
    # Adding "iters" value to empty string 
    out = ''
    for i in range(iters):
        out += string.join(", ") # Adding "iters" value to string with ,'s in between
    return out

def run_my_funcs(x,y):
    print(x,y)
    my_squares(x)
    my_join(x,y)
    return 0

run_my_funcs(10000000,"My string")
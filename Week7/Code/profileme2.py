#!usr/bin/env python3
""" Demonstrating profililng in Python, improving on profileme.py."""
__author__= 'Eva Linehan (eva.linehan18@imperial.ac.uk)'
__version__ = 0.01
__date__ = 'Nov 2018'
__licence__ = 'In class exercise'

def my_squares(iters):
    out = [i ** 2 for i in range(iters)] # Using list comprehension to append in list
    return out

def my_join(iters, string):
    out = ''
    for i in range(iters):
        out += ", " + string # Replaced .join with an explicit string concatenation.
    return out

def run_my_funcs(x,y):
    #Running both functions at the same time
    print(x,y)
    my_squares(x)
    my_join(x,y)
    return 0

run_my_funcs(10000000,"My string")
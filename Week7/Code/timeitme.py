#!usr/bin/env python3
""" Demonstrating profililng in Python."""
__author__= 'Eva Linehan (eva.linehan18@imperial.ac.uk)'
__version__ = 0.01
__date__ = 'Nov 2018'
__licence__ = 'In class exercise'

# Loop vs. list comprehensions

iters = 1000000

import timeit

from profileme import my_squares as my_squares_loops

from profileme2 import my_squares as my_squares_lc

#%timeit my_squares_loops(iters)
#%timeit my_squares_lc(iters)

# Loop vs. join method for strings

mystring = "my string"

from profileme import my_join as my_join_join

from profileme2 import my_join as my_join

#%timeit(my_join_join(iters, mystring))
#%timeit(my_join(iters, mystring))

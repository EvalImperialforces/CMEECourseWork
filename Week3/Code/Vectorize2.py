#!usr/bin/env python3
"""  Modifing stochastic Ricker model to increase run time. """
__author__= 'Eva Linehan (eva.linehan18@imperial.ac.uk)'
__version__ = 0.01
__date__ = 'Dec 2018'
__licence__ = 'Inclass practical'

import numpy as np
import time


def stochrick (p0 = np.random.uniform(0.5,1.5,(1000)), r = 1.2, K = 1, sigma = 0.2, numyears = 100):
    """ Discrete population model"""
    N = np.zeros((numyears, len(p0))) # Numpy array of zeros
    N[0,] = p0 # First column will be populations
    for year in range(1,numyears): # For the range of years specified apply equation to each population 
        N[year] = N[year-1]*np.exp(r*(1-N[year-1,]/K)+np.random.normal(1,sigma, len(p0)))
        return N 


t0 = time.time()
stochrick()
t1 = time.time()
runtime = t1-t0

print("The execution time for Vectorize2.py was {}".format(runtime))
#!usr/bin/env python3
"""  Vectorization example to compare the process time of vectors in comparison to loops. """
__author__= 'Eva Linehan (eva.linehan18@imperial.ac.uk)'
__version__ = 0.01
__date__ = 'Dec 2018'
__licence__ = 'Inclass practical' 

import numpy as np
import scipy as sc
import time

M = np.random.rand(1000, 1000)
#M = sc.matrix(M)
#print(M.shape)

def SumALLELEMENTS(M):
    Dimensions = M.shape
    Tot = 0
    for i in range(1,Dimensions[0]):
        for j in range(1,Dimensions[1]):
            Tot = Tot + M[i,j]
    return(Tot)


t0 = time.time()
SumALLELEMENTS(M)
t1 = time.time()
runtime = t1-t0


print("The execution time for Vectorize.1 py was {}".format(runtime))

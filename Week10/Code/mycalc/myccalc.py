import os
import ctypes

so_filepath = "{}/libmycalc.so".format(os.getcwd())

#from ctypes import *
ctypes.cdll.Loadlibrary(so_filepath)
myccalc = ctypes.CDLL(so_filepath)  #Reference for functions in libmycalc

myccalc.add.floats.argtypes = [ctypes.c_float, ctypes.c_float] 
# Instructing python to understand add.floats function from myccalc library
# Input variables will be ctype c floats
myccalc.add.floats.restype = ctypes.c_float
# Heres what will be passed back 

# For every function in memory write a bindings file

# Use function

func = add.floats(9.7,5)
print(func)


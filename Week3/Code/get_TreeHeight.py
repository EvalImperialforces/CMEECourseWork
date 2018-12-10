#!usr/bin/env python3
""" Generate a csv output file of tree height with input file name """
__author__= 'Eva Linehan (eva.linehan18@imperial.ac.uk)'
__version__ = 0.01
__date__ = 'Dec 2018'
__licence__ = 'Inclass practical' 

import csv
import sys
import numpy as np

def Treeheight (Degrees, Distance):
    """ Calculate tree heights usring degrees and radians"""
    radians = Degrees*(np.pi/180)
    height = Distance*(np.tan(radians))
    return height

#import pandas as pd
#df = pd.read_csv(sys.argv[1])
#df["Height_m"] = (lambda: height: height = df.Distance*(np.tan(df.Degrees*(np.pi/180))) 
#df.write_csv(sys.argv[1].replace(".csv", "_withtreeheight.csv"))

# Read Degrees and Distance from csv into numpy array
with open(sys.argv[1], 'r') as infile: # Read in file from command line
    lines = infile.readlines()
    nparray = np.zeros((len(lines) - 1, 2)) # Numpy array of zeros of length columns minus the headers
    for c, line in enumerate(lines[1:]): # for lines after header
        array = line.split(',') # Split by commas
        Distance = float(array[1]) # Make distance a float array of first element in data
        Degrees = float(array[2]) # Make degrees a float array of third element in data
        nparray[c][0] = Distance # For each iteration put distance in first position of numpy array
        nparray[c][-1] = Degrees # For each iteration put degrees in last position of numpy array

# Make a numpy array of tree height
outputarr = np.zeros((len(nparray), 1)) # Numpy array of zeros same length as Distance/Degrees array with 1 column
for c, vals in enumerate(nparray):
    height = Treeheight(vals[-1], vals[0]) # Calculate treeheight 
    outputarr[c] = height # Input height to array

finalarray = np.append(nparray, outputarr, axis = 1) # Bind the degree/distance and height numpy arrays

outpath = "../Results/{}".format(sys.argv[1].split("/")[-1].replace(".csv", "_withtreeheight.csv")) # Outpath for renaming file and saving to Results directory

print("Saving file")
headers = ",".join(["Distance", "Degrees", "Height (m)"]) # Headers for output csv
np.savetxt(outpath,
           finalarray,
           delimiter=",",
           header = headers,
           comments='') # Input final array with headers into .csv file









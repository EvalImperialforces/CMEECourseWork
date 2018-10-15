#!usr/bin/env python3
""" Missing oaks problem.

Usng doctests to confirm working function and modifying script to handle typos.

 """
__author__= 'Eva Linehan (eva.linehan18@imperial.ac.uk)'
__version__ = 0.01
__date__ = 'Oct 2018'
__licence__ = 'Inclass practical'

import csv
import sys
import pdb
import doctest

#Define function
def is_an_oak(name):
    """ Returns True if genus name is 'quercus'

    >>> is_an_oak('quercuss robur')
    False

    >>> is_an_oak('fraxinus excelsior')
    False

    >>> is_an_oak('pinus sylvertris')
    False

    >>> is_an_oak('quercus cerris')
    True

    """
    return name.lower().split(' ')[0]=='quercus'
    # .split seperates string by the space (in between genus and species) to ensure the first element (species in this case) will be quercus.

def main(argv): 
    """ Removing headers in taxa, print the genus of trees with 'FOUND AN OAK' for any of the variables from is_an_oak. For output file 'JustOaksData.csv' print headers in first row followed by oak species"""    
    f = open('../Data/TestOaksData.csv','r')
    g = open('../Data/JustOaksData.csv','w')
    taxa = csv.reader(f)
    headers = next(taxa, None) #Skip the headers
    csvwrite = csv.writer(g)
    oaks = set()
    c = 0
    for row in taxa:
        c += 1
        print(row)
        print ("The genus is: ") 
        print(row[0])
        if is_an_oak(row[0]):
            print('FOUND AN OAK!\n')
        if c == 1:
            if headers:
                csvwrite.writerow(headers)
    csvwrite.writerow([row[0], row[1]])   
    return 0

if (__name__ == "__main__"):
    status = main(sys.argv)
    sys.exit (status)

doctest.testmod()

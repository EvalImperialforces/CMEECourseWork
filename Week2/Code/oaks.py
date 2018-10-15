#!usr/bin/env python3
""" Loop and list comprehension exercises to create a set of oak species from a list of tree species. """
__author__= 'Eva Linehan (eva.linehan18@imperial.ac.uk)'
__version__ = 0.01
__date__ = 'Oct 2018'
__licence__ = 'Inclass practical'

## Finds just those taxa that are oak trees from a list of species

taxa = [ 'Quercus robur',
         'Fraxinus excelsior',
         'Pinus sylvestris',
         'Quercus cerris',
         'Quercus petraea']

def is_an_oak(name):
    """ Function to return just oak species in lower case. """
    return name.lower().startswith('quercus')

## Using for loops
oaks_loops = set()
for species in taxa:
    if is_an_oak(species):
        oaks_loops.add(species)
print (oaks_loops)

## Using list comprehensions
oaks_lc = set([species for species in taxa if is_an_oak(species)])
print(oaks_lc)

##Get names in upper case using loops
oaks_loops = set ()
for species in taxa:
    if is_an_oak(species):
        oaks_loops.add (species.upper())
print(oaks_loops)

##Get names in UPPER CASE using list comprehensions
oaks_lc = set([species.upper() for species in taxa if is_an_oak(species)])
print(oaks_lc)

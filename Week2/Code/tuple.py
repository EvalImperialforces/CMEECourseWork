#!/usr/bin/env python3
""" Script to print tuples from birds on seperate lines """
__author__= 'Eva Linehan (eva.linehan18@imperial.ac.uk)'
__version__ = 0.01
__date__ = 'Oct 2018'
__licence__ = 'Inclass practical'

birds = ( ('Passerculus sandwichensis','Savannah sparrow',18.7),
          ('Delichon urbica','House martin',19),
          ('Junco phaeonotus','Yellow-eyed junco',19.5),
          ('Junco hyemalis','Dark-eyed junco',19.6),
          ('Tachycineata bicolor','Tree swallow',20.2),
        )

# Birds is a tuple of tuples of length three: latin name, common name, mass.
# write a (short) script to print these on a separate line or output block by species 
# Hints: use the "print" command! You can use list comprehensions!

#Each tuple is mapped as a string and joined to a newline character to print on individual lines. 
bird2 = map(str,birds)
print('\n'.join(bird2))



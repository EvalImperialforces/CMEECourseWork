#!usr/bin/env python3
""" Uses regex to get list of kingdom, phylum, species from file.
"""
__author__= 'Eva Linehan (eva.linehan18@imperial.ac.uk)'
__version__ = 0.01
__date__ = 'Nov 2018'
__licence__ = 'Blackbirds Practical'



import re

# Read the file (using a different, more python 3 way, just for fun!)
with open('../Data/blackbirds.txt', 'r') as f:
    text = f.read()

# replace \t's and \n's with a spaces:
text = text.replace('\t',' ')
text = text.replace('\n',' ')
# You may want to make other changes to the text. 

# In particular, note that there are "strange characters" (these are accents and
# non-ascii symbols) because we don't care for them, first transform to ASCII:

text = text.encode('ascii', 'ignore') # first encode into ascii bytes
text = text.decode('ascii', 'ignore') # Now decode back to string

#print(text)
# Now extend this script so that it captures the Kingdom, Phylum and Species
# name for each species and prints it out to screen neatly.

KPS = r"Kingdom\s(\w+).+?Phylum\s(\w+).+?Species\s(\w+\s\w+)"
# Finds Kingdom space and captures text character until reaching another character (end of word)
# and continues through every character until the instance of Phylum and so on and so forth
l = re.findall(KPS, text)

print("{k:<10}{p:<10}{s:<10}".format(k="Kingdom", p="Phylum", s="Species"))
# print headers 10 spaces to the left
print("-"*40)
# Dotted line under header

for i in l:
    print("{x1:<10}{x2:<10}{x3:<10}".format(x1=i[0], x2=i[1], x3=i[2]))
    # Print each tuple 10 spaces to the left
    #print("  ".join(i))


# Hint: you may want to use re.findall(my_reg, text)... Keep in mind that there
# are multiple ways to skin this cat! Your solution could involve multiple
# regular expression calls (easier!), or a single one (harder!)


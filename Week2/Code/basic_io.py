#!usr/bin/env python3
""" Example of printing input files, generating output files and storing objects. """
__author__= 'Eva Linehan (eva.linehan18@imperial.ac.uk)'
__version__ = 0.01
__date__ = 'Oct 2018'
__licence__ = 'Inclass practical'


##############################
#FILE INPUT
##############################
# Open a file for reading - CREATING AN OBJECT
f=open('../Sandbox/test.txt','r')
# use "implicit" for loop:
# if the object is a file, python will cycle over lines
for line in f: 
    print(line)
# OPENS OBJECT F IN LOOP
# close the file
f.close ()

# Same example, skip the blank line

f = open('../Sandbox/test.txt','r')
for line in f:
    if len(line.strip()) > 0:
        print(line)
f.close()


##############################
#FILE OUTPUT
##############################
# Save the elements of a list to a file

list_to_save = range(100)

f = open('../Sandbox/testout.txt','w')
for i in list_to_save:
    f.write(str(i) + '\n')

f.close ()


##############################
# STORING OBJECTS
##############################
# To save an object (even complex) for later use

my_dictionary = {"a key": 10, "another key": 11}

import pickle


f = open('../Sandbox/testp.p', 'wb')

pickle.dump(my_dictionary, f)

f.close()

# 'testp.p' is binary file, 'as f' is the variable or alias in this case.
# pickle.dump (variable, location) 

with open('../Sandbox/testp.p', 'wb') as f:   
# with command autocloses. 
    pickle.dump(my_dictionary, f)

print("Done")

## Load the data again
f = open('../Sandbox/testp.p','rb')
another_directory = pickle.load(f)
f.close()


with open('../Sandbox/testp.p', "rb") as f:
    another_directory = pickle.load(f)  


print(another_directory)

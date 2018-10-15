#!usr/bin/env python3
""" Importing, reading and writing .csv files in python. """
__author__= 'Eva Linehan (eva.linehan18@imperial.ac.uk)'
__version__ = 0.01
__date__ = 'Oct 2018'
__licence__ = 'Inclass practical'

# Read a file containing:
# 'Species','Infraorder', 'Family', 'Distribution','Body mass male (Kg)'
f = open('../Data/testcsv.csv','r')

csvread = csv.reader(f)
temp = []
for row in csvread:
    temp.append(tuple(row))
    print (row)
    print("The species is",row[0])

f.close()

# CSVREAD TO READ OPEN FILE (F). TEMP IS THE FRANE WHERE INFO WILL GO. ONCE IT IS ORGANIZED (IN THIS CASE TUPLE ROW AND PRINT) 

# write a file containing only species name and Body mass
f = open ('../Data/testcsv.csv','r')
g = open ('../Data/bodymass.csv','w')

csvread = csv.reader(f)
csvwrite = csv.writer(g)
for row in csvread:
    print(row)
    csvwrite.writerow([row[0], row[4]])

f.close()
g.close()

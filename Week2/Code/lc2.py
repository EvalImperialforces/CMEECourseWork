#!usr/bin/env python3
""" List comprehensions and conventional loops of average UK rainfall for 1910 by month """
__author__= 'Eva Linehan (eva.linehan18@imperial.ac.uk)'
__version__ = 0.01
__date__ = 'Oct 2018'
__licence__ = 'Inclass practical'

# Average UK Rainfall (mm) for 1910 by month
# http://www.metoffice.gov.uk/climate/uk/datasets
rainfall = (('JAN',111.4),
            ('FEB',126.1),
            ('MAR', 49.9),
            ('APR', 95.3),
            ('MAY', 71.8),
            ('JUN', 70.2),
            ('JUL', 97.1),
            ('AUG',140.2),
            ('SEP', 27.0),
            ('OCT', 89.4),
            ('NOV',128.4),
            ('DEC',142.2),
           )


# (1) Use a list comprehension to create a list of month,rainfall tuples where
# the amount of rain was greater than 100 mm.

Rainfallover100mm = [x for x in rainfall if x[1]>=100]
print (Rainfallover100mm)

# (2) Use a list comprehension to create a list of just month names where the
# amount of rain was less than 50 mm. 

Rainfallless50mm = [x for x in rainfall if x[1]<50]
print (Rainfallless50mm)

# (3) Now do (1) and (2) using conventional loops (you can choose to do 
# this before 1 and 2 !). 

#Loop for (1)           
Rainfallover100mm=[]
Item=list(rainfall)
for x in rainfall:
    if x[1]>100:
        Rainfallover100mm.append(x)
print(Rainfallover100mm)


#Loop for (2)
Rainfallless50mm=[]
Item=list(rainfall)
for x in rainfall:
    if x[1]<50:
        Rainfallless50mm.append(x)
print(Rainfallless50mm)


# ANNOTATE WHAT EVERY BLOCK OR IF NECESSARY, LINE IS DOING! 

# ALSO, PLEASE INCLUDE A DOCSTRING AT THE BEGINNING OF THIS FILE THAT 
# SAYS WHAT THE SCRIPT DOES AND WHO THE AUTHOR IS

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
# For every rainfall measurement in months in tuple, if rainfall is greater than 100mm add to list and print
print (Rainfallover100mm)

# (2) Use a list comprehension to create a list of just month names where the
# amount of rain was less than 50 mm. 

Rainfallless50mm = [x for x in rainfall if x[1]<50]
# For every rainfall measurement in months in tuple, if rainfall is less than 50mm add to list and print
print (Rainfallless50mm)

# (3) Now do (1) and (2) using conventional loops (you can choose to do 
# this before 1 and 2 !). 

#Loop for (1)           
Rainfallover100mm=[]
Item=list(rainfall)
for x in rainfall: # For months and measurements in rainfall tuple
    if x[1]>100: # If measurements are greater than 100mm
        Rainfallover100mm.append(x) # Append to list
print(Rainfallover100mm)


#Loop for (2)
Rainfallless50mm=[]
Item=list(rainfall)
for x in rainfall: # For months and measurements in rainfall tuple
    if x[1]<50: # If measurements are less than 50mm
        Rainfallless50mm.append(x) # Append to list
print(Rainfallless50mm)




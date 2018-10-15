#!/usr/bin/env python3
""" Control flow exercises. """
__author__= 'Eva Linehan (eva.linehan18@imperial.ac.uk)'
__version__ = 0.01
__date__ = 'Oct 2018'
__licence__ = 'Inclass practical'


for i in range (3, 17):
    print ('hello')

for j in range(12):
    if j % 3 == 0:
        print('hello')

for j in range(15):
    if j % 5 ==3:
        print ('hello')

z = 0
while z!= 15:
    print ('hello')
    z = z + 3

z = 12
while z < 100:
    if z == 31:
        for k in range(7):
            print ('hello')
    elif z == 18:
        print ('hello')
    z = z + 1

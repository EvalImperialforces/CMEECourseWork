#!usr/bin/env python3
""" Numerical integration using Lotka-Volterra model for a predator-prey system in two-dimensional space"""
__author__= 'Eva Linehan (eva.linehan18@imperial.ac.uk)'
__version__ = 0.01
__date__ = 'Nov 2018'
__licence__ = 'Lotka-Volterra Model Class Exercise'

import scipy as sc
import scipy.integrate as integrate

def dCR_dt(pops, t=0): # pops is a list, t is time 
    # 0 is default value = can run irrespective of input

    R = pops[0]
    C = pops[1]
    dRdt = r * R - a * R * C 
    dCdt = -z * C + e * a * R * C
    
    return sc.array([dRdt, dCdt]) # Must return scipy array

r = 1.
a = 0.1 
z = 1.5
e = 0.75

t = sc.linspace(0, 15,  1000) # Defining time vector
# 0-15 is arbitrary, depends on organism lifecycle
# 1000 also arbitrary but hints at precision of resolution. 1000 subdivisions.

# Setting initial conditions for populations
R0 = 10 #R0 = 10 resources at beginning
C0 = 5 # 5 consumers
RC0 = sc.array([R0, C0]) #Function must take array as an input

# Numerically integrate the system from starting conditions
pops, infodict = integrate.odeint(dCR_dt, RC0, t, full_output=True) 
# integrate.odient (function, y array:initial condition on y, time array, full output: true if return a dict of optional outputs)
# Odeint(egration) is an Gauss Newton algorithm, takes starting values and feeds to function
# tags timestep to create 2 vectors within function each time to recreate curve.


pops

infodict.keys()
infodict['message']

## Plotting in Python

import matplotlib.pylab as p

f1= p.figure()

p.plot(t, pops[:,0], 'g-', label='Resource density') # Plot
p.plot(t, pops[:,1]  , 'b-', label='Consumer density')
p.grid()
p.legend(loc='best')
p.xlabel('Time')
p.ylabel('Population density')
p.title('Consumer-Resource population dynamics')
#p.show()# Display the figure

f1.savefig('../Results/LV1_model.pdf')

f2 = p.figure()

p.plot(pops[:,0], pops[:,1]  , 'r-')
p.grid()
p.xlabel('Resource density')
p.ylabel('Consumer density')
p.title('Consumer-Resource population dynamics')
#p.show()

f2.savefig('../Results/Phaseportait.pdf')
#!usr/bin/env python3
""" Numerical integration using Lotka-Volterra model, altering variable input and plotting result"""
__author__= 'Eva Linehan (eva.linehan18@imperial.ac.uk)'
__version__ = 0.01
__date__ = 'Nov 2018'
__licence__ = 'Lotka-Volterra Model Practical'

import scipy as sc
import scipy.integrate as integrate
import argparse


def dCR_dt(pops, t=0): #pops is a list, t is time 
    #0 is default value = can run irrespective of input

    R = pops[0]
    C = pops[1]
    K = 50
    dRdt = (r * R)*(1-(R/K)) - a * R * C 
    dCdt = -z * C + e * a * R * C
    
    return sc.array([dRdt, dCdt]) # Must return scipy array


p = argparse.ArgumentParser()
p.add_argument('values', nargs="*", type=float)
args = p.parse_args()

if len(args.values) != 4:

    r = 1.6
    a = 0.2
    z = 1.2
    e = 0.6
else:
    r = (args.values[0]) # instrinsic growth rate of population
    a = (args.values[1]) # search rate of resource (area x time)
    z = (args.values[2]) # mortality
    e = (args.values[3]) # efficiency in energy to consumer biomass


t = sc.linspace(0, 30,  1500) # 0-15 is arbitrary, depends on organism lifecycle
# 1000 also arbitrary but hints at precision of resolution. 1000 subdivisions.

R0 = 10 #R0 = population at beginning
C0 = 5 
RC0 = sc.array([R0, C0]) 

pops, infodict = integrate.odeint(dCR_dt, RC0, t, full_output=True)
# Optional output
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
p.text(8, 24, 'r = {:.2}, a = {:.2}, z = {:.2}, e = {:.2}'.format(r, a, z, e))
p.show()# Display the figure

f1.savefig('../Results/LV2_model.pdf')



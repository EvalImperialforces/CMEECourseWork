#!usr/bin/env python3
""" Generate random links and nodes in a food web to save as PDF"""
__author__= 'Eva Linehan (eva.linehan18@imperial.ac.uk)'
__version__ = 0.01
__date__ = 'Nov 2018'
__licence__ = 'Food Web Network Practical'

import networkx as nx
import scipy as sc
import matplotlib.pyplot as p

# Generating links and randomly connected network

def GenRdnAdjList(N=2, C=0.5): # C = Probability of connectance
    """ Building random adjacent connectedness probability list """
    Ids = range(N)
    ALst = []
    for i in Ids: # For i in range (N)
        if sc.random.uniform(0,1,1) < C: # Don't go over the connectedness probability (C)
            # Pick 1 number (connectedness value) from 0 to 1 (start range, end range, how many numbers picked)
            Lnk = sc.random.choice(Ids,2).tolist() # Output will be array so must force to list
            # Select 2 random species and add to list
            # Lump together the 2 randomly species chosen and probability below C.
            if Lnk[0] != Lnk[1]: #avoid self (e.g., cannibalistic) loops
                ALst.append(Lnk)
    return ALst

MaxN = 30 
C = 0.75

AdjL = sc.array(GenRdnAdjList(MaxN,C))
# An array of the function output with variables MaxN and C.
AdjL

#Generating species nodes 

Sps = sc.unique(AdjL) # Species IDs
SizRan = ([-10, 10]) # On log 10 scale
Sizs = sc.random.uniform(SizRan[0],SizRan[1],MaxN) 
# Generate 30 random species IDs from -10 to 10
Sizs

p.hist(Sizs)
p.hist(10 ** Sizs)

p.close('all')

pos = nx.circular_layout(Sps) # Circular layout of species

G = nx.Graph()

G.add_nodes_from(Sps)
G.add_edges_from(tuple(AdjL)) # this function needs a tuple input

NodSizs= 1000 * (Sizs-min(Sizs))/(max(Sizs)-min(Sizs))
# Multiplied by 1000 to increase node thickness proportionally

p.figure()
nx.draw_networkx(G, pos, node_size = NodSizs)
p.savefig('../Results/FW.pdf')
p.show()



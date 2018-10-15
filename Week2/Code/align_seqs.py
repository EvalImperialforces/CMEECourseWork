#!usr/bin/env python3
""" Aligning DNA sequences and assigning a score based on the start position and number of base matches. """
__author__= 'Eva Linehan (eva.linehan18@imperial.ac.uk)'
__version__ = 0.01
__date__ = 'Oct 2018'
__licence__ = 'Inclass practical'
 
# Sequences in input file
#seq2 = "ATCGCCGGATTACGGG"
#seq1 = "CAATTCGGAT"

import sys
""" 
Processes DNA sequences from .fasta file to print best alignment and score in .txt file.
"""
seq_dict = {}
with open("../Data/Seqs_input.fasta") as f:
    for line in f:
        if line.startswith(">"):
            key = line.split(">")[-1].rstrip()
            # For header, file title is printed by returning the last item in the line with no trailing characters
        else:
            if key in seq_dict.keys():
                seq_dict[key] += line.rstrip() 
            # Remove trailing characters from sequence and add to key.
            else:
                seq_dict[key] = line.rstrip()
print(seq_dict)

seq1 = seq_dict['Seq1']
seq2 = seq_dict['Seq2']

     
# Assign the longer sequence s1, and the shorter to s2
# l1 is length of the longest, l2 that of the shortest

l1 = len(seq1)
l2 = len(seq2)
if l1 >= l2:
    s1 = seq1
    s2 = seq2
else:
    s1 = seq2
    s2 = seq1
    l1, l2 = l2, l1 # swap the two lengths

## A function that computes a score by returning the number of matches starting
## from arbitrary startpoint (chosen by user)
def calculate_score(s1, s2, l1, l2, startpoint):
    matched = "" # to hold string displaying alignements
    score = 0
    for i in range(l2):
        if (i + startpoint) < l1:
            if s1[i + startpoint] == s2[i]: # if the bases match
                matched = matched + "*"
                score = score + 1
            else:
                matched = matched + "-"

    # some formatted output
    print("." * startpoint + matched)           
    print("." * startpoint + s2)
    print(s1)
    print(score) 
    print(" ")

    return score

### Test the function with some example starting points:
### calculate_score(s1, s2, l1, l2, 0)
### calculate_score(s1, s2, l1, l2, 1)
### calculate_score(s1, s2, l1, l2, 5)

### now try to find the best match (highest score) for the two sequences
my_best_align = None
my_best_score = -1

for i in range(l1): # Note that you just take the last alignment with the highest score
    z = calculate_score(s1, s2, l1, l2, i)
    if z > my_best_score:
        my_best_align = "." * i + s2 # think about what this is doing!
        my_best_score = z 
print(my_best_align)
print(s1)
print("Best score:", my_best_score)

# Save to an output
output = "../Results/Best_Match.txt"
outfile = '{}\n {}\nBest Score {}'.format(my_best_align, s1, my_best_score) #Formats output to print best alignment followed by best score
with open("../Results/Best_Match.txt", "w") as output:
    output.write(outfile)
print ("Done!")




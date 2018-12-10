#!usr/bin/env python3

""" Aligning DNA sequences from any .fasta file, assigning a score based on the start position 
and number of base matches. """

__author__= 'Eva Linehan (eva.linehan18@imperial.ac.uk)'
__version__ = 0.01
__date__ = 'Dec 2018'
__licence__ = 'Extra credit practical exercise'


import sys
import pickle


# If no arguments are given use default sequences 1 and 2 and find length.
if len(sys.argv) == 1:
    seq2 = "ATCGCCGGATTACGGG"
    seq1 = "CAATTCGGAT"
    l1 = len(seq1)
    l2 = len(seq2)

# Else create a dictionary with key as file name and value as sequence in file
else:
    seq_dict = {}
    for files in (sys.argv[1:]): # Open files and and read lines
        file1 = open(files)
        file1_str = file1.readlines() # Reads each line from file into a list
        for line in file1_str:
            if line.startswith(">"):
                key = line.split(">")[-1].rstrip()
                    # For header, file title is printed by returning the last item in the line with no trailing characters
            else:
                if key in seq_dict.keys():
                    seq_dict[key] += line.rstrip() 
                # Remove trailing characters from sequence and add to key.
                else:
                    seq_dict[key] = line.rstrip()
    keys_list = [key for key in seq_dict.keys()] # Create a list of keys in dictionary
    l1 = len(seq_dict[keys_list[0]]) # Get the length of the value at that key
    l2 = len(seq_dict[keys_list[1]])
    seq1 = seq_dict[keys_list[0]] # Sequence 1 is value of key 1
    seq2 = seq_dict[keys_list[1]] # Sequence 2 is value of key 2


if l1 >= l2:
    s1 = seq1
    s2 = seq2
else:
    s1 = seq2
    s2 = seq1
    l1, l2 = l2, l1 # swap the two lengths


def calculate_score(s1, s2, l1, l2, startpoint):
    """A function that computes a score by returning the number of matches starting
    from arbitrary startpoint (chosen by user) """
    matched = "" # to hold string displaying alignements
    score = 0
    for i in range(l2):
        if (i + startpoint) < l1:
            if s1[i + startpoint] == s2[i]: # if the bases match
                matched = matched + "*"
                score = score + 1
            else:
                matched = matched + "-"
    #print(matched)
    return score

### now try to find the best match (highest score) for the two sequences
my_best_score = -1

best_aligns = []

for i in range(l1): # Note that you just take the last alignment with the highest score 
    z = calculate_score(s1, s2, l1, l2, i)
    if z == my_best_score: # If z is equal to initial best score, append to list
        best_aligns.append("." * i + s2)
        my_best_score = z 
    if z > my_best_score: # If z is greater than, append to empty list
        best_aligns = []
        best_aligns.append("." * i + s2)
        my_best_score = z      
# print(best_aligns)

outlist = [] 
for i in best_aligns:
    outlist.append("{}\n{}\n\nBest Score: {}\n\n".format(i, s1, my_best_score)) 
# Append best alignments in the following format       
#outstr = [print(x) for x in outlist] 
outstr = ''.join(outlist) # Convert list to string for output.write in output file



## Save to an output
output = "../Results/Best_Match_Better.txt"
with open("../Results/Best_Match_better.txt", "w") as output:
    output.write(outstr)
print ("Done!")

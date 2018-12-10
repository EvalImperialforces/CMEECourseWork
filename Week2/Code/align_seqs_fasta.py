#!usr/bin/env python3

""" Aligning DNA sequences from any .fasta file, assigning a score based on the start position 
and number of base matches. """

__author__= 'Eva Linehan (eva.linehan18@imperial.ac.uk)'
__version__ = 0.01
__date__ = 'Dec 2018'
__licence__ = 'Extra credit practical exercise'


import sys

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
    keys_list = [key for key in seq_dict.keys()] # Make a list of dictionary keys
    l1 = len(seq_dict[keys_list[0]]) # Get the length of the value at that key
    l2 = len(seq_dict[keys_list[1]])
    seq1 = seq_dict[keys_list[0]] # Sequence 1 is value of key 1
    seq2 = seq_dict[keys_list[1]] # Sequence 2 is value of key 2


# Assign the longer sequence s1, and the shorter to s2
# l1 is length of the longest, l2 that of the shortest
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

    return score

### now try to find the best match (highest score) for the two sequences
my_best_align = None
my_best_score = -1

for i in range(l1): # Note that you just take the last alignment with the highest score
    z = calculate_score(s1, s2, l1, l2, i)
    if z > my_best_score:
        my_best_align = "." * i + s2 # think about what this is doing!
        my_best_score = z 
#print(my_best_align)
#print(s1)
#print("Best score:", my_best_score)

# Save to an output
output = "../Results/Best_Match.txt"
outfile = '{}\n {}\nBest Score {}'.format(my_best_align, s1, my_best_score) #Formats output to print best alignment followed by best score
with open("../Results/Best_Match_fasta.txt", "w") as output:
    output.write(outfile)
print ("Done!")

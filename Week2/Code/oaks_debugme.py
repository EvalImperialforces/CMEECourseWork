import csv
import sys
import pdb
import doctest

#Define function
def is_an_oak(name):
    """ Returns True if name is starts with 'quercus'

    >>> is_an_oak('quercuss robur')
    True

    >>> is_an_oak('fraxinus excelsior')
    False

    >>> is_an_oak('pinus sylvertris')
    False

    >>> is_an_oak('quercus cerris')
    True

    """
    return name.lower().split(' ')[0]=='quercus'

def main(argv): 
    f = open('../Data/TestOaksData.csv','r')
    g = open('../Data/JustOaksData.csv','w')
    taxa = csv.reader(f)
    headers = next(taxa, None) #Skip the headers
    csvwrite = csv.writer(g)
    oaks = set()
    c = 0
    for row in taxa:
        c += 1
        print(row)
        print ("The genus is: ") 
        print(row[0])
        if is_an_oak(row[0]):
            print('FOUND AN OAK!\n')
        if headers:
            if c == 1:
                csvwrite.writerow(headers)
    csvwrite.writerow([row[0], row[1]])   
    return 0

if (__name__ == "__main__"):
    status = main(sys.argv)
    sys.exit (status)

doctest.testmod()
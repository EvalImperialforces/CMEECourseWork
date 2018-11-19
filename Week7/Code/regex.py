#!usr/bin/env python3
""" Demonstrating Regular Expressions"""
__author__= 'Eva Linehan (eva.linehan18@imperial.ac.uk)'
__version__ = 0.01
__date__ = 'Nov 2018'
__licence__ = 'In class exercise'


####### In class exercises ########

import re

my_string = "a given string"

match = re.search(r'\s', my_string) 
# Match a space, r = raw and \s = whitespace
print(match) # Only tells you if object was found, gives you the location of memory

match.group() # Shows you the match 

match = re.search(r'\d', my_string) 
# Match a numeric(integer) character (\d)
print(match) # Only tells you if object was found

MyStr = 'an example'

match = re.search(r'\w*\s', MyStr) 
# Match a single "word" character and space

if match:
    print('found a match:', match.group())
else:
    print('did not find a match')

match = re.search(r'2' , "it takes 2 to 2 tango 2")
match.group()

match = re.search(r'\d' , "it takes 2 to tango") 
# Match a number
match.group()

match = re.search(r'\d.*' , "it takes 2 to tango") 
# Match a number, followed by any character ('.') any number of times('*')
match.group()

match = re.search(r'\s\w*$', 'once upon a time') 
# Match a space with a word proceeding the end of a string
# Get word at the end of a string
match.group()

match = re.search(r'\s\w{1,3}\s', 'once upon a time')
# Match a space followed by a word with characters from 1 -3 (no greater than 3) followed by space
match.group()

re.search(r'\w*\s\d.*\d', 'take 2 grams of H2O').group()
# Match a text character any number of times followed by a space and a digit
# with any character in between up to another digit

re.search(r'^\w*.*\s', 'once upon a time').group()
# Match a word at the start of a string until the end of that word followed by any character 
# inbetween and match that as many times up to a space (the last space)

re.search(r'^\w*.*?\s', 'once upon a time').group() 
# '\w*' means that it will find the word and continue till you come to something other than the word
# Word at start of string and anything inbetween up to the first instance of a space

re.search(r'\w*\s.+?\d', 'take 2 grams of H20').group()
# Word up to a space, digit, space and everything inbetween until you reach a digit.

re.search(r'^\w*.+?\s', 'once in a far away land upon a time').group()
# Takes everything in between first word and plus continues on to next space. 
# Has to have another character after 'once' which is a space
# + makes dot a must sign. Has to have a word and character before it and then we find the next space
# After once there must be another character of something which happens to be upon until the next space.


re.search(r'<.+>', 'This is a <EM>first</EM> test').group()
# HTML tag '<' and everything inbetween but there must be more characters
# until we reach '>'

re.search(r'\d*\.?\d*','1432.75+60.22i').group()
# Digit and everything in betwen until we find a '.' and 
# stop at the next instance of the next digit and repeat the digit 
# 0 or more times until we reach something else ('+').

re.search(r'[AGTC]+', 'the sequence ATTCGT').group()
# Find any AGTC characters and repeat 0 or more times.

re.search(r'\s+[A-Z]{1}\w+\s\w+', 'The bird-shit frog''s name is Theloderma asper').group()
# Space and repeat until we reach any uppercase letter once. Then that text characacter
# 0 or more times space and text character 0 or more times.

MyStr = 'Samraat Pawar, s.pawar@imperial.ac.uk, Systems biology and ecological theory'
match = re.search(r"[\w\s]+,\s[\w\.@]+,\s[\w\s&]+",MyStr)
# Any word and space before ',' with a space followed by any word and @ before ',' etc.
match.group()


##### RegExercise Practical ######

# Ex.1
re.search(r'[\w\s\?\+]+', 'Ma?ry Ken Brena? Barbie Opheli@ OGorman').group()

# Ex.2
# 1. Match lower case 'abc' at the start of string and any 'a' and 'b' repeating 
# until a space, tab and digit.

# 2. Digit at the start of the string match once but no more than twice
# up to slash and a digit no more than once, slash 4 digits (Date)

# 3. Space or no space followed by uppercase or lowercase letters or slashes and commas and spaces 
# and repeat until you reach another space.

# Ex.3
MyStr = "19/05/2020 18/05/1998 05/01/2001"
#re.sub(r'(\d{2})(\d{2})(\d{4})', r'\3/\2/\1', MyStr)


### Grouping regex patterns ###
#MyStr = 'Samraat Pawar, s.pawar@imperial.ac.uk, Systems biology and ecological theory'
#match = re.search(r"[\w\s]+,\s[\w\.-]+@[\w\.-]+,\s[\w\s&]+",MyStr)
#if match:
#    print(match.group(0))
#    print(match.group(1))
#    print(match.group(2))
#    print(match.group(3))

#emails = re.findall(r'[\w\.-]+@[\w\.-]+', MyStr) 
# Robust way to find emails of all kinds
#for email in emails:
#    print(email)


#import urllib3

#con = urllib3.PoolManager() # Open a connetion
#r = conn.request('GET', 'https://www.imperial.ac.uk/silwood-park/academic-staff/')
#webpage_html = r.data # read in page contents
# Read in bytes and decode because of language UTF8 

#type(webpage_html)

#My_Data = webpage_html.decode() # Decode to language
#print(My_Data)


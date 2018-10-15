#!/usr/bin/env python3
""" Control flow 'foo_x' exercises to run as script or importable module. """

__author__  = 'Eva Linehan (eval2496@gmail.com)'
__version__ = '0.0.1'
__date__ = 'Oct 2018'
__licence__ = 'Inclass practical'

import sys

def foo1(x):
    """ Computes value (x) to the power of 0.5"""
    return x ** 0.5

def foo2(x, y):
    """ If x is greater than y, returns x. Otherwise y will be returned"""
    if x > y:
        return x
    return y

def foo3(x, y, z):
    """ Changes position of variables depending on value. If x is bigger than y, variables are swapped. If y is greater than z, the variables are swapped"""
    if x > y:
        tmp = y
        y = x
        x = tmp
    if y > z:
        tmp = z
        z = y
        y = tmp
    return [x, y, z]

def foo4(x=2):
    """ Calculates factorials iteratively by multiplying result by successively larger numbers in the range"""
    result = 1
    for i in range(1, x + 1):
        result = result * i
    return result

def foo5(x): # a recursive function
    """ Calculates factorials recursively """
    if x == 1:
        return 1
    return x * foo5(x - 1)

def foo6(x): # Calculate the factorial of x in a different way
    """ Calculates factorials iteratively by multiplying x by x-1 and so on as long as x>=1"""
    facto = 1
    while x >= 1:
        facto = facto * x
        x = x - 1
    return facto

def main(argv):
    print(foo1(6))
    print(foo2(3,3))
    print(foo3(5,4,6))
    print(foo4(12))
    print(foo5(20))
    print(foo6(9))
    return 0

if (__name__ == "__main__"):
    status = main(sys.argv)
    sys.exit(status)

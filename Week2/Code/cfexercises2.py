#!/usr/bin/env python3

""" Modifying cfexercises2.py to make it a module"""

__author__  = 'Eva Linehan (eval2496@gmail.com)'
__version__ = '0.0.1'

import sys

def foo1(x):
    return x ** 0.5

def foo2(x, y):
    if x > y:
        return x
    return y

def foo3(x, y, z):
    if x > y:
        tmp = y
        y = x
        x = tmp
    if y > z:
        tmp = z
        z = y
        y = tmp
    return [x, y, z]

def foo4(x):
    result = 1
    for i in range(1, x + 1):
        result = result * i
    return result

def foo5(x): # a recursive function
    if x == 1:
        return 1
    return x * foo5(x - 1)

def main(argv):
    print(foo1(6))
    print(foo2(3,3))
    print(foo3(5,4,6))
    print(foo4(12))
    print(foo5(20))
    return 0

if (__name__ == "__main__"):
    status = main(sys.argv)
    sys.exit(status)
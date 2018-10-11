#!/usr/bin/env python3


def createabug(x=0):
    y=x**3
    import ipdb; ipdb.set_trace()
    z=0
    y=y/z
    return y

createabug(2)

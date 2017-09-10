#!/usr/bin/python

import function

sg = "caoyong"
def num_add(x, y):
    global c
    c = x + y
    print("%d + %d is %d" % (x, y, c))
    print("{0} + {1} is {2}".format(x, y, c))
    print(sg)


function.printMax(78, 23)
c = 123
num_add(45, 67)

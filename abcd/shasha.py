#!/usr/bin/python
import time
n = 1
flag = 1
while flag :
    print("the number is %d:"%n)
    print("the number is {0}:".format(n))
    n = n + 1
    time.sleep(1)
    if n > 10:
        flag = 0
else:
    print("RBQ")

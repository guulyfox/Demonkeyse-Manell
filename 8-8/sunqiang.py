#!/usr/bin/python3

def A():
    b = 10
    def B():
        nonlocal b
        #b = 20
        b = b + 1
        c = b + 1
        return c
    return B


F=A()

print(A()())

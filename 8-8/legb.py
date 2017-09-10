#!/usr/bin/python3

'''
sanle python
'''

x = 88
y = "cali"


def f1():
    '''test legb rules'''
    x = 99
    # global y
    # y = 'RBQ'

    def f2():
        print(x, y, __name__, __doc__)
    f2()


f1()

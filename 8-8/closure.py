#!/usr/bin/python3


def line_conf():
    def line(x):
        return 2 * x + 1
    return line    # return a function


my_line = line_conf()
print(my_line(5))
print(my_line(8))

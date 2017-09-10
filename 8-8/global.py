#!/usr/bin/python3

def line_conf():
    b = 14
    def line(x):
        nonlocal b # I will take upstait variable 
        b += 1
        return 2 * x + b
    return line

b = 5
my_line = line_conf()
print(my_line(5))

print(my_line.__closure__)
print(my_line.__closure__[0].cell_contents)

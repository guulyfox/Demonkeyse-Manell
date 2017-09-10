#! /usr/bin/python3

a = input("please input a number")
try:
    if a.isalpha():
        raise ValueError
    if a.isdigit():
        pass
    else:
        raise TypeError
    a = int(a) + 1
    assert  2  <= a <= 101
except ValueError:
    print("please do not input a alpha")
except TypeError:
    print("please input a number, do not use special character.")
except AssertionError:
    print("please input a number in 1 or 100")
else :
    print("good job, %d" %(a - 1))

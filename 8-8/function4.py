#!/usr/bin/python


def func():
   global x
   print("x is %d"%(x))
   x = 5
   print("Changed local x to %d"%(x))


x = 60
func()
print("Value of x is %d"%(x))

#!/usr/bin/python

num = input("please input a number in 1-100:")

if num.isdigit():
   if  1 <= int(num) <= 100:
       print(num)
   else:
       print("please input a number in 1-100")
elif num.isalpha():
   print("please input 1-100 number")
else:
   print("please don't input  specific character")

try:
    num = input ("please input a number in 1-100:")
    if not num.isdigit():
        raise TypeError
    else:
        if 1<= int(num) <= 100:
            print(num)
        else:
            raise ValueError
except TypeError:
    print("please don't input specific character and alphabet")
except ValueError:
    print("please input number in range of 1 to 100")

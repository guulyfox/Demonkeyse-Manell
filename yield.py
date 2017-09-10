#!/usr/bin/python

def g():
   n = 1
   while n:
       yield n
       n += 1

def main():
   a = input("How many times do you want to do?")
   flag = int(a)
   ge = g()
   type(ge)
   while flag:
       print(next(ge))
       flag -= 1

main()

#!/usr/bin/python3
def r_return(n):
   print("You love me.")
   while n > 0:
       print("before return")
       #return n
       yield n
       n = n - 1
       print("after return")

rr = r_return(4)
#print(rr)
flag = 4 
while flag:
    print(next(rr))
    flag -= 1
